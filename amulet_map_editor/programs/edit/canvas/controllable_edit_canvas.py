from typing import TYPE_CHECKING, Set
import wx
import numpy
import time

from .base_edit_canvas import BaseEditCanvas
from amulet_map_editor.opengl.mesh.world_renderer.world import sin, cos
from amulet_map_editor.amulet_wx.util.key_config import serialise_key_event, KeybindGroup, ActionLookupType, Escape
from .events import EditEscapeEvent, EVT_EDIT_ESCAPE

if TYPE_CHECKING:
    from amulet.api.world import World


class ControllableEditCanvas(BaseEditCanvas):
    """Adds the user interaction logic to BaseEditCanvas"""
    def __init__(self, world_panel: wx.Window, world: 'World'):
        super().__init__(world_panel, world)
        self._last_mouse_x = 0
        self._last_mouse_y = 0
        self._mouse_moved = False  # has the mouse position changed since the last frame
        self._persistent_actions: Set[str] = set()  # wx only fires events for when a key is initially pressed or released. This stores actions for keys that are held down.
        self._key_binds: ActionLookupType = {}  # a store for which keys run which actions
        self._box_select_time = 0

        # timer to deal with persistent actions
        self._input_timer = wx.Timer(self)
        self._bind_controllable_events()

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
        self.Bind(wx.EVT_MOUSEWHEEL, self._release)

        self.Bind(EVT_EDIT_ESCAPE, self._selection_group.escape_event)

        self.Bind(wx.EVT_TIMER, self._process_persistent_inputs, self._input_timer)

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

            elif press:  # run once on button release
                if action == "selection distance +":
                    self.select_distance += 1
                    self.select_distance2 += 1
                elif action == "selection distance -":
                    if self.select_distance > 1:
                        self.select_distance -= 1
                    if self.select_distance2 > 1:
                        self.select_distance2 -= 1
                elif action == "deselect boxes":
                    self._selection_group.deselect_all()
                elif action == "remove box":
                    self._selection_group.deselect_active()
                elif action == "box click":
                    if self.selection_editable:
                        self.box_select("add box modifier" in self._persistent_actions)
                        self._box_select_time = time.time()
                elif action == "inspect block":
                    x, y, z = self.cursor_location
                    try:
                        block = self.world.get_block(x, y, z, self.dimension)
                        block_entity = self.world.get_chunk(x >> 4, z >> 4, self.dimension).block_entities.get((x, y, z), None)
                        translator = self.world.translation_manager.get_version(
                            self.world.world_wrapper.platform, self.world.world_wrapper.version
                        )
                        version_block, version_block_entity, _ = translator.block.from_universal(block, extra_input=block_entity)
                        print(f"{version_block}\n{version_block_entity}\n\t{block}\n\t{block_entity}")
                    except Exception as e:
                        print(e)

            else:  # run once on button press and frequently until released
                if action == "box click":
                    if self.selection_editable and time.time() - self._box_select_time > 0.1:
                        self._selection_group.box_select_disable()
                elif action == "toggle mouse mode":
                    self._toggle_mouse_lock()
                elif action == "speed+":
                    self._camera_move_speed *= 1.1
                elif action == "speed-":
                    self._camera_move_speed /= 1.1

        elif key[1] == Escape:
            self._escape()
            wx.PostEvent(self, EditEscapeEvent())
        elif not press:
            remove_actions = [self._key_binds[k] for k in self._key_binds if k[1] == key[1]]
            for a in remove_actions:
                if a in self._persistent_actions:
                    self._persistent_actions.remove(a)

    def box_select(self, add_modifier: bool = False):
        position = self._selection_group.box_select_toggle(add_modifier)
        if position is not None:
            self.select_distance2 = int(numpy.linalg.norm(position - self.camera_location))

    def _process_persistent_inputs(self, evt):
        """Handle actions run by keys that are being held down."""
        forward, up, right, pitch, yaw = 0, 0, 0, 0, 0
        if 'up' in self._persistent_actions:
            up += 1
        if 'down' in self._persistent_actions:
            up -= 1
        if 'forwards' in self._persistent_actions:
            forward += 1
        if 'backwards' in self._persistent_actions:
            forward -= 1
        if 'left' in self._persistent_actions:
            right -= 1
        if 'right' in self._persistent_actions:
            right += 1

        if self._mouse_lock:
            pitch = self._mouse_delta_y * 0.07
            yaw = self._mouse_delta_x * 0.07
            self._mouse_delta_x = 0
            self._mouse_delta_y = 0
        else:
            pitch = 0
            yaw = 0
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
        rx, ry = self.camera_rotation
        x += self._camera_move_speed * (cos(ry) * right + sin(ry) * forward)
        y += self._camera_move_speed * up
        z += self._camera_move_speed * (sin(ry) * right - cos(ry) * forward)

        rx += self._camera_rotate_speed * pitch
        if not -90 <= rx <= 90:
            rx = max(min(rx, 90), -90)
        ry += self._camera_rotate_speed * yaw
        self.camera_location = self._render_world.camera_location = (x, y, z)
        self.camera_rotation = self._render_world.camera_rotation = (rx, ry)

    def _toggle_mouse_lock(self):
        """Toggle mouse selection mode."""
        self.SetFocus()
        if self._mouse_lock:
            self._release_mouse()
        else:
            self.SetCursor(wx.Cursor(wx.CURSOR_BLANK))
            self._mouse_delta_x = self._mouse_delta_y = self._last_mouse_x = self._last_mouse_y = 0
            self._mouse_lock = True
        self._selection_moved = True

    def _release_mouse(self):
        """Release the mouse"""
        self.SetCursor(wx.NullCursor)
        self._mouse_lock = False

    def _on_mouse_motion(self, evt):
        """Event fired when the mouse is moved."""
        self.SetFocus()
        if self._mouse_lock:
            if self._last_mouse_x == 0:
                self._last_mouse_x, self._last_mouse_y = (
                    int(self.GetSize()[0] / 2),
                    int(self.GetSize()[1] / 2),
                )
                self.WarpPointer(self._last_mouse_x, self._last_mouse_y)
                self._mouse_delta_x = self._mouse_delta_y = 0
            else:
                mouse_x, mouse_y = evt.GetPosition()
                dx = mouse_x - self._last_mouse_x
                dy = mouse_y - self._last_mouse_y
                self._last_mouse_x, self._last_mouse_y = (
                    int(self.GetSize()[0] / 2),
                    int(self.GetSize()[1] / 2),
                )
                # only if location actually changed from the center, because WarpPointer may generate a mouse motion event
                # this check avoids using WarpPointer for events caused by WarpPointer
                if dx or dy:
                    self.WarpPointer(self._last_mouse_x, self._last_mouse_y)
                    self._mouse_delta_x += dx
                    self._mouse_delta_y += dy
        else:
            mouse_x, mouse_y = evt.GetPosition()
            self._last_mouse_x, self._last_mouse_y = (
                int(self.GetSize()[0] / 2),
                int(self.GetSize()[1] / 2),
            )
            self._mouse_delta_x = mouse_x - self._last_mouse_x
            self._mouse_delta_y = mouse_y - self._last_mouse_y
            self._mouse_moved = True

    def _on_loss_focus(self, evt):
        """Event fired when the user tabs out of the window."""
        self._escape()
        evt.Skip()

    def _escape(self):
        """Release the mouse and remove all key presses to the camera doesn't fly off into the distance."""
        self._persistent_actions.clear()
        self._release_mouse()
