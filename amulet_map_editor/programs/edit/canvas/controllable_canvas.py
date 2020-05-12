from typing import TYPE_CHECKING
import wx

from .canvas import EditCanvas
from amulet_map_editor.opengl.mesh.world_renderer.world import sin, cos
from ..events import (
    CameraMoveEvent,
    BoxGreenCornerChangeEvent,
    BoxBlueCornerChangeEvent,
    BoxCoordsEnableEvent,
)
from amulet_map_editor.amulet_wx.key_config import serialise_key_event, KeybindGroup

if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet_map_editor.programs.edit.edit import EditExtension


key_map = {
    'up': wx.WXK_SPACE,
    'down': wx.WXK_SHIFT,
    'forwards': 87,
    'backwards': 83,
    'left': 65,
    'right': 68,

    'look_left': 74,
    'look_right': 76,
    'look_up': 73,
    'look_down': 75,
}


class ControllableEditCanvas(EditCanvas):
    def __init__(self, world_panel: 'EditExtension', world: 'World'):
        super().__init__(world_panel, world)
        self._persistent_actions = set()
        self._key_binds = {}

        self.Bind(wx.EVT_KILL_FOCUS, self._on_loss_focus)
        self.Bind(wx.EVT_MOTION, self._on_mouse_motion)

        self.Bind(wx.EVT_LEFT_DOWN, self._press)
        self.Bind(wx.EVT_LEFT_UP, self._release)
        self.Bind(wx.EVT_MIDDLE_DOWN, self._press)
        self.Bind(wx.EVT_MIDDLE_UP, self._release)
        self.Bind(wx.EVT_RIGHT_DOWN, self._press)
        self.Bind(wx.EVT_RIGHT_UP, self._release)
        self.Bind(wx.EVT_KEY_DOWN, self._press)
        self.Bind(wx.EVT_KEY_UP, self._release)
        self.Bind(wx.EVT_MOUSEWHEEL, self._release)

        self._input_timer = wx.Timer(self)
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
        self._process_action(evt, True)

    def _release(self, evt):
        self._process_action(evt, False)

    def _process_action(self, evt, press: bool):
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
                elif action == "selection distance -":
                    if self.select_distance > 1:
                        self.select_distance -= 1
                elif action == "deselect boxes":
                    self._selection_group.deselect()
                elif action == "remove box":
                    self._selection_group.delete_active()
            else:  # run once on button press and frequently until released
                if action == "box click":
                    self._box_click()
                elif action == "toggle selection mode":
                    self._toggle_selection_mode()
                elif action == "toggle mouse lock":
                    self._toggle_mouse_lock()
                elif action == "speed+":
                    self._camera_move_speed += 0.2
                elif action == "speed-":
                    self._camera_move_speed -= 0.2
                    if self._camera_move_speed < 0.1:
                        self._camera_move_speed = 0.1

        elif key[1] == wx.WXK_ESCAPE:
            self._escape()
        elif not press:
            remove_actions = [self._key_binds[k] for k in self._key_binds if k[1] == key[1]]
            for a in remove_actions:
                if a in self._persistent_actions:
                    self._persistent_actions.remove(a)

    def _toggle_mouse_lock(self):
        self.SetFocus()
        if self._mouse_lock:
            self._release_mouse()
        else:
            self.SetCursor(wx.Cursor(wx.CURSOR_BLANK))
            self._mouse_delta_x = self._mouse_delta_y = self._last_mouse_x = self._last_mouse_y = 0
            self._mouse_lock = True
            self._change_box_location()

    def _process_persistent_inputs(self, evt):
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
        if (forward, up, right, pitch, yaw) == (0, 0, 0, 0, 0):
            if not self._mouse_lock and self._mouse_moved:
                self._mouse_moved = False
                self._change_box_location()
            return
        self._camera[0] += self._camera_move_speed * (cos(self._camera[4]) * right + sin(self._camera[4]) * forward)
        self._camera[1] += self._camera_move_speed * up
        self._camera[2] += self._camera_move_speed * (sin(self._camera[4]) * right - cos(self._camera[4]) * forward)

        self._camera[3] += self._camera_rotate_speed * pitch
        if not -90 <= self._camera[3] <= 90:
            self._camera[3] = max(min(self._camera[3], 90), -90)
        self._camera[4] += self._camera_rotate_speed * yaw
        self._transformation_matrix = None
        self._render_world.camera = self._camera
        self._change_box_location()
        wx.PostEvent(self, CameraMoveEvent(x=self._camera[0], y=self._camera[1], z=self._camera[2], rx=self._camera[3], ry=self._camera[4]))

    def box_select(self, add_modifier: bool = False):
        position = self._selection_group.box_click(add_modifier)

        # if self._selection_box.select_state <= 1:
        #     self._selection_box.select_state += 1
        # elif self._selection_box.select_state == 2:
        #     self._selection_box.point1, self._selection_box.point2 = self._selection_box2.point1, self._selection_box2.point2
        #     self._selection_box.select_state = 1
        #     x, y, z = self._selection_box.point1
        #     wx.PostEvent(self, BoxGreenCornerChangeEvent(x=x, y=y, z=z))
        #     wx.PostEvent(self, BoxBlueCornerChangeEvent(x=x, y=y, z=z))
        # wx.PostEvent(self, BoxCoordsEnableEvent(enabled=self._selection_box.select_state == 2))

    def _box_click(self):
        if self.select_mode == 0:
            self.box_select("add box modifier" in self._persistent_actions)

    def _toggle_selection_mode(self):
        self._select_style = not self._select_style
        self._change_box_location()

    def _release_mouse(self):
        self.SetCursor(wx.NullCursor)
        self._mouse_lock = False

    def _on_mouse_motion(self, evt):
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
        self._escape()
        evt.Skip()

    def _escape(self):
        self._persistent_actions.clear()
        self._release_mouse()
