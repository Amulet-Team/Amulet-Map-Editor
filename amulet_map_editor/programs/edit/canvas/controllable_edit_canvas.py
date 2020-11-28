from typing import TYPE_CHECKING, Set, Generator, Tuple
import wx
import numpy
import time
import math

from amulet.api.data_types import OperationYieldType
from wx.adv import RichToolTip

from .base_edit_canvas import BaseEditCanvas
from amulet_map_editor.api.opengl.canvas import Orthographic, Perspective
from amulet_map_editor import log
from amulet_map_editor.api.wx.util.key_config import (
    serialise_key_event,
    KeybindGroup,
    ActionLookupType,
    Escape,
)
from .events import (
    EditEscapeEvent,
    EVT_EDIT_ESCAPE,
    BoxClickEvent,
    EVT_BOX_CHANGE_CONFIRM,
    CreateUndoEvent,
    ProjectionChangeEvent,
)

if TYPE_CHECKING:
    from amulet.api.level import World


class ControllableEditCanvas(BaseEditCanvas):
    """Adds the user interaction logic to BaseEditCanvas"""

    def __init__(self, world_panel: wx.Window, world: "World", **kwargs):
        super().__init__(world_panel, world, **kwargs)
        self._mouse_x = self._mouse_y = 0
        self._last_mouse_x = 0
        self._last_mouse_y = 0
        self._mouse_moved = False  # has the mouse position changed since the last frame
        self._persistent_actions: Set[
            str
        ] = (
            set()
        )  # wx only fires events for when a key is initially pressed or released. This stores actions for keys that are held down.
        self._key_binds: ActionLookupType = (
            {}
        )  # a store for which keys run which actions
        self._box_select_time = 0
        self._toggle_mouse_time = 0
        self._selection_undo_timeout = 0
        self._previous_mouse_lock = self._mouse_lock

        # timer to deal with persistent actions
        self._input_timer = wx.Timer(self)

    def reset_bound_events(self):
        """Unbind all events and re-bind the default events.
        We are allowing users to bind custom events so we should have a way to reset what is bound."""
        super().reset_bound_events()
        self._bind_controllable_events()

    def _bind_controllable_events(self):
        self.Bind(wx.EVT_KILL_FOCUS, self._on_loss_focus)
        self.Bind(wx.EVT_MOTION, self._on_mouse_motion)

        # key press actions
        self.Bind(wx.EVT_LEFT_DOWN, self._press)
        self.Bind(wx.EVT_LEFT_UP, self._release)
        self.Bind(wx.EVT_MIDDLE_DOWN, self._press)
        self.Bind(wx.EVT_MIDDLE_UP, self._release)
        self.Bind(wx.EVT_RIGHT_DOWN, self._press)
        self.Bind(wx.EVT_RIGHT_UP, self._release)
        self.Bind(wx.EVT_KEY_DOWN, self._press)
        self.Bind(wx.EVT_KEY_UP, self._release)
        self.Bind(wx.EVT_NAVIGATION_KEY, self._press)
        self.Bind(wx.EVT_MOUSEWHEEL, self._release)

        self.Bind(EVT_EDIT_ESCAPE, self.selection.escape_event)
        self.Bind(EVT_BOX_CHANGE_CONFIRM, self._on_box_change_confirm)

        self.Bind(wx.EVT_TIMER, self._process_persistent_inputs, self._input_timer)

    def setup(self) -> Generator[OperationYieldType, None, None]:
        yield from super().setup()
        self._bind_controllable_events()

    def enable(self):
        super().enable()
        self._input_timer.Start(33)

    def disable(self):
        self._input_timer.Stop()
        super().disable()

    def set_key_binds(self, key_binds: KeybindGroup):
        self._key_binds = dict(zip(key_binds.values(), key_binds.keys()))

    def _press(self, evt):
        """Event to handle a number of different key presses"""
        self._process_action(evt, True)

    def _release(self, evt):
        """Event to handle a number of different key releases"""
        self._process_action(evt, False)

    def _process_action(self, evt, press: bool):
        """Logic to handle a key being pressed or released."""
        key = serialise_key_event(evt)
        evt.Skip()
        if key is None:
            return
        if key in self._key_binds:
            action = self._key_binds[key]
            if action in {
                "up",
                "down",
                "forwards",
                "backwards",
                "left",
                "right",
                "add box modifier",
            }:
                if press:
                    self._persistent_actions.add(action)
                elif action in self._persistent_actions:
                    self._persistent_actions.remove(action)

            elif press:  # run once on button press and frequently until released
                if action == "selection distance +":
                    self.select_distance += 1
                    self.select_distance2 += 1
                elif action == "selection distance -":
                    if self.select_distance > 1:
                        self.select_distance -= 1
                    if self.select_distance2 > 1:
                        self.select_distance2 -= 1
                elif action == "deselect boxes":
                    if not self._deselect():
                        self.selection.deselect_all()
                elif action == "remove box":
                    if not self._deselect():
                        self.selection.deselect_active()
                elif action == "box click":
                    if self.selection_editable:
                        self.box_select("add box modifier" in self._persistent_actions)
                        self._box_select_time = time.time()
                    wx.PostEvent(self, BoxClickEvent())
                elif action == "toggle mouse mode":
                    self.SetFocus()
                    self._previous_mouse_lock = self._mouse_lock
                    self._capture_mouse()
                    self._toggle_mouse_time = time.time()
                elif action == "inspect block":
                    self._inspect_block()
                elif action == "toggle 2d/3d":
                    self.projection_mode = not self.projection_mode

            else:  # run once on button release
                if action == "box click":
                    if (
                        self.selection_editable
                        and time.time() - self._box_select_time > 0.1
                    ):
                        self.selection.box_select_disable()
                elif action == "toggle mouse mode":
                    if self._previous_mouse_lock or time.time() - self._toggle_mouse_time > 0.1:
                        self._release_mouse()
                    else:
                        self._capture_mouse()
                elif action == "speed+":
                    if self.projection_mode == Perspective:
                        self._camera_move_speed *= 1.1
                    elif self.projection_mode == Orthographic:
                        self.fov = max(0.5, self.fov / 1.1)
                elif action == "speed-":
                    if self.projection_mode == Perspective:
                        self._camera_move_speed /= 1.1
                    elif self.projection_mode == Orthographic:
                        self.fov = min(1000.0, self.fov * 1.1)

        elif key[1] == Escape:
            self._escape()
            wx.PostEvent(self, EditEscapeEvent())
        elif not press:
            remove_actions = [
                self._key_binds[k] for k in self._key_binds if k[1] == key[1]
            ]
            for a in remove_actions:
                if a in self._persistent_actions:
                    self._persistent_actions.remove(a)

    def _get_block_info_message(self) -> str:
        x, y, z = self.cursor_location
        try:
            block = self.world.get_block(x, y, z, self.dimension)
            chunk = self.world.get_chunk(x >> 4, z >> 4, self.dimension)
            block_entity = chunk.block_entities.get((x, y, z), None)
            platform = self.world.world_wrapper.platform
            version = self.world.world_wrapper.version
            translator = self.world.translation_manager.get_version(
                platform,
                version,
            )
            (version_block, version_block_entity, _,) = translator.block.from_universal(
                block, block_entity, block_location=(x, y, z)
            )
            if isinstance(version, tuple):
                version_str = ".".join(str(v) for v in version[:4])
            else:
                version_str = str(version)
            block_data_text = f"x: {x}, y: {y}, z: {z}\n\n{platform.capitalize()} {version_str}\n{version_block}"
            if version_block_entity:
                version_block_entity_str = str(version_block_entity)
                block_data_text = f"{block_data_text}\n{version_block_entity_str}"

            block_data_text = f"{block_data_text}\n\nUniversal\n{block}"
            if block_entity:
                block_entity_str = str(block_entity)
                block_data_text = f"{block_data_text}\n{block_entity_str}"

            if chunk.biomes.dimension == 2:
                biome = chunk.biomes[x % 16, z % 16]
                try:
                    block_data_text = (
                        f"{block_data_text}\n\nBiome: {self.world.biome_palette[biome]}"
                    )
                except Exception as e:
                    log.error(e)
            elif chunk.biomes.dimension == 3:
                biome = chunk.biomes[(x % 16) // 4, y // 4, (z % 16) // 4]
                try:
                    block_data_text = (
                        f"{block_data_text}\n\nBiome: {self.world.biome_palette[biome]}"
                    )
                except Exception as e:
                    log.error(e)

        except Exception as e:
            log.error(e)
            return str(e)
        else:
            return block_data_text

    def _inspect_block(self):
        def truncate(s: str, max_line_length: int = None) -> str:
            if isinstance(max_line_length, int):
                max_line_length = max(-1, max_line_length)
                s = "\n".join(
                    [
                        line[: max_line_length - 3] + "..."
                        if len(line) > max_line_length
                        else line
                        for line in s.split("\n")
                    ]
                )
            return s

        if not self._mouse_moved:
            full_msg = self._get_block_info_message()
            msg = truncate(full_msg, 150)
            tooltip = RichToolTip("Inspect Block", msg)
            tooltip.ShowFor(self, wx.Rect(self._mouse_x, self._mouse_y, 1, 1))

    def _deselect(self) -> bool:
        """
        Additional deselect logic.
        :return: True if it has done something and further actions should be suppressed.
        """
        return False

    def box_select(self, add_modifier: bool = False):
        position = self.selection.box_select_toggle(add_modifier)
        if position is not None:
            self.select_distance2 = int(
                numpy.linalg.norm(position - self.camera_location)
            )

    def _on_box_change_confirm(self, evt):
        if self._selection_undo_timeout < time.time() - 1:
            self.world.history_manager.create_undo_point(True)
            wx.PostEvent(self, CreateUndoEvent())
            self._selection_undo_timeout = time.time()
        evt.Skip()

    def _process_persistent_inputs(self, evt):
        """Handle actions run by keys that are being held down."""
        forward = up = right = pitch = yaw = 0
        if "up" in self._persistent_actions:
            up += 1
        if "down" in self._persistent_actions:
            up -= 1
        if "forwards" in self._persistent_actions:
            forward += 1
        if "backwards" in self._persistent_actions:
            forward -= 1
        if "left" in self._persistent_actions:
            right -= 1
        if "right" in self._persistent_actions:
            right += 1

        if self.projection_mode == Perspective:
            if self._mouse_lock:
                pitch = self._mouse_delta_y * 0.07
                yaw = self._mouse_delta_x * 0.07
                self._mouse_delta_x = 0
                self._mouse_delta_y = 0
        elif self.projection_mode == Orthographic:
            if self._mouse_lock:
                width, height = self.GetSize()
                forward += self.fov * self._mouse_delta_y / height
                right -= self.fov * self.aspect_ratio * self._mouse_delta_x / width
                self._mouse_delta_x = 0
                self._mouse_delta_y = 0

        self.move_camera_relative(forward, up, right, pitch, yaw)
        evt.Skip()

    def move_camera_relative(self, forward, up, right, pitch, yaw):
        """Move the camera relative to its current location."""
        if not any((forward, up, right, pitch, yaw)):
            if not self._mouse_lock and self._mouse_moved:
                self._mouse_moved = False
                self._selection_moved = True
            return
        x, y, z = self.camera_location
        if self.projection_mode == Perspective:
            ry, rx = self.camera_rotation
        else:
            ry, rx = 180, 90
        x += self._camera_move_speed * -(
            math.cos(math.radians(ry)) * right + math.sin(math.radians(ry)) * forward
        )
        y += self._camera_move_speed * up
        z += self._camera_move_speed * (
            math.cos(math.radians(ry)) * forward - math.sin(math.radians(ry)) * right
        )

        if self.projection_mode == Perspective:
            rx += self._camera_rotate_speed * pitch
            if not -90 <= rx <= 90:
                rx = max(min(rx, 90), -90)
            ry += self._camera_rotate_speed * yaw
            if not -180 <= ry <= 180:
                ry += -int(numpy.sign(ry)) * 360
        self.camera_location = (x, y, z)
        self.camera_rotation = (ry, rx)

    @property
    def projection_mode(self) -> int:
        return self._projection_mode

    @projection_mode.setter
    def projection_mode(self, projection_mode: int):
        assert isinstance(projection_mode, int) and 0 <= projection_mode <= 1
        if self._projection_mode != projection_mode:
            self._projection_mode = projection_mode
            self._reset_matrix()
            if self.projection_mode == Orthographic:
                self.camera_rotation = 180, 90
            wx.PostEvent(self, ProjectionChangeEvent(mode=self.projection_mode))

    def _capture_mouse(self):
        self.SetCursor(wx.Cursor(wx.CURSOR_BLANK))
        self._mouse_delta_x = self._mouse_delta_y = 0
        self._last_mouse_x = self._last_mouse_y = 0
        self._mouse_lock = True
        self._selection_moved = True

    def _release_mouse(self):
        """Release the mouse"""
        self.SetCursor(wx.NullCursor)
        self._mouse_lock = False
        self._selection_moved = True

    def _screen_middle(self) -> Tuple[int, int]:
        """Get the pixel coordinate of the middle of the screen"""
        return (
            int(self.GetSize()[0] / 2),
            int(self.GetSize()[1] / 2),
        )

    def _on_mouse_motion(self, evt):
        """Event fired when the mouse is moved."""
        self.SetFocus()
        self._mouse_x, self._mouse_y = evt.GetPosition()
        if self._mouse_lock:
            if self._last_mouse_x == 0:
                # when lock starts self._last_mouse_x will be 0.
                # This sets up some things so that the screen does not jump to the cursor position
                self._last_mouse_x, self._last_mouse_y = self._screen_middle()
                self.WarpPointer(self._last_mouse_x, self._last_mouse_y)
                self._mouse_delta_x = self._mouse_delta_y = 0
            else:
                dx = self._mouse_x - self._last_mouse_x
                dy = self._mouse_y - self._last_mouse_y
                self._last_mouse_x, self._last_mouse_y = self._screen_middle()
                # only if location actually changed from the center, because WarpPointer may generate a mouse motion event
                # this check avoids using WarpPointer for events caused by WarpPointer
                if dx or dy:
                    self.WarpPointer(self._last_mouse_x, self._last_mouse_y)
                    self._mouse_delta_x += dx
                    self._mouse_delta_y += dy
        else:
            self._last_mouse_x, self._last_mouse_y = self._screen_middle()
            self._mouse_delta_x = self._mouse_x - self._last_mouse_x
            self._mouse_delta_y = self._mouse_y - self._last_mouse_y
            self._mouse_moved = True

    def _on_loss_focus(self, evt):
        """Event fired when the user tabs out of the window."""
        self._escape()
        evt.Skip()

    def _escape(self):
        """Release the mouse and remove all key presses to the camera doesn't fly off into the distance."""
        self._persistent_actions.clear()
        self._release_mouse()
