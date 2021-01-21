from typing import TYPE_CHECKING
import numpy
import math
import wx
import time

from amulet_map_editor.api.opengl.camera import Projection

from .base_behaviour import BaseBehaviour
from ..events import (
    InputHeldEvent,
    EVT_INPUT_HELD,
    InputPressEvent,
    EVT_INPUT_PRESS,
    InputReleaseEvent,
    EVT_INPUT_RELEASE,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class CameraBehaviour(BaseBehaviour):
    """Adds the normal behaviour for the camera."""
    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
        self._previous_mouse_lock = self._mouse_lock = False
        self._toggle_mouse_time = 0

    def set_up_events(self):
        """Set up all events required to run."""
        self.canvas.Bind(EVT_INPUT_HELD, self._on_input_held)
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)
        self.canvas.Bind(EVT_INPUT_RELEASE, self._on_input_release)
        self.canvas.Bind(wx.EVT_KEY_DOWN, self._on_key_press)
        self.canvas.Bind(wx.EVT_KILL_FOCUS, self._on_loss_focus)
        self.canvas.Bind(wx.EVT_MOTION, self._on_mouse_motion)

    def _on_mouse_motion(self, evt):
        self.canvas.SetFocus()
        evt.Skip()

    def _on_key_press(self, evt: wx.KeyEvent):
        key = evt.GetUnicodeKey() or evt.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            self._escape()
        evt.Skip()

    def _on_input_press(self, evt: InputPressEvent):
        """Logic to run each time the input press event is run."""
        if evt.action_id == "toggle 2d/3d":
            if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
                self.canvas.camera.rotation = 180, 90
                self.canvas.camera.projection_mode = Projection.TOP_DOWN
            elif self.canvas.camera.projection_mode == Projection.TOP_DOWN:
                self.canvas.camera.projection_mode = Projection.PERSPECTIVE
        elif evt.action_id == "toggle mouse mode":
            self.canvas.SetFocus()
            self._previous_mouse_lock = self._mouse_lock
            self._capture_mouse()
            self._toggle_mouse_time = time.time()

    def _on_input_release(self, evt: InputReleaseEvent):
        """Logic to run each time the input release event is run."""
        if evt.action_id == "toggle mouse mode":
            if (
                self._previous_mouse_lock
                or time.time() - self._toggle_mouse_time > 0.1
            ):
                self._release_mouse()
            else:
                self._capture_mouse()
        elif evt.action_id == "speed+":
            if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
                self.canvas.camera.move_speed *= 1.1
            elif self.canvas.camera.projection_mode == Projection.TOP_DOWN:
                self.canvas.camera.fov = max(0.5, self.canvas.camera.fov / 1.1)
        elif evt.action_id == "speed-":
            if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
                self.canvas.camera.move_speed /= 1.1
            elif self.canvas.camera.projection_mode == Projection.TOP_DOWN:
                self.canvas.camera.fov = min(1000.0, self.canvas.camera.fov * 1.1)

    def _on_input_held(self, evt: InputHeldEvent):
        """Logic to run each time the input held event is run."""
        forward = up = right = pitch = yaw = 0
        up += ("up" in evt.action_ids) - ("down" in evt.action_ids)
        forward += ("forwards" in evt.action_ids) - ("backwards" in evt.action_ids)
        right += ("right" in evt.action_ids) - ("left" in evt.action_ids)

        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            if self._mouse_lock:
                pitch = self.canvas.mouse.delta_y * 0.07
                yaw = self.canvas.mouse.delta_x * 0.07
                self.canvas.mouse.warp_middle()
                self.canvas.mouse.reset_delta()
            self.move_camera_relative(forward, up, right, pitch, yaw)
        elif self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            if self._mouse_lock:
                width, height = self.canvas.GetSize()
                forward += (
                    2 * self.canvas.camera.fov * self.canvas.mouse.delta_y / height
                )
                right -= (
                    2
                    * self.canvas.camera.fov
                    * self.canvas.camera.aspect_ratio
                    * self.canvas.mouse.delta_x
                    / width
                )
                self.canvas.mouse.warp_middle()
                self.canvas.mouse.reset_delta()
                self.move_camera_relative(forward, up, right, pitch, yaw)
            else:
                x, y, z = self.canvas.camera.location
                x += right * self.canvas.camera.fov / 30
                z -= forward * self.canvas.camera.fov / 30
                self.canvas.camera.location_rotation = (x, y, z), (180, 90)

        evt.Skip()

    def move_camera_relative(self, forward, up, right, pitch, yaw):
        """Move the camera relative to its current location."""
        if not any((forward, up, right, pitch, yaw)):
            # if not self._mouse_lock and self._mouse_moved:
            #     self._mouse_moved = False
            #     self._selection_moved = True
            return
        x, y, z = self.canvas.camera.location
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            ry, rx = self.canvas.camera.rotation
            x += self.canvas.camera.move_speed * -(
                math.cos(math.radians(ry)) * right
                + math.sin(math.radians(ry)) * forward
            )
            y += self.canvas.camera.move_speed * up
            z += self.canvas.camera.move_speed * (
                math.cos(math.radians(ry)) * forward
                - math.sin(math.radians(ry)) * right
            )
            rx += self.canvas.camera.rotate_speed * pitch
            if not -90 <= rx <= 90:
                rx = max(min(rx, 90), -90)
            ry += self.canvas.camera.rotate_speed * yaw
            if not -180 <= ry <= 180:
                ry += -int(numpy.sign(ry)) * 360
        else:
            ry, rx = 180, 90
            x += right
            z -= forward

        self.canvas.camera.location_rotation = (x, y, z), (ry, rx)

    def _capture_mouse(self):
        self.canvas.SetCursor(wx.Cursor(wx.CURSOR_BLANK))
        self.canvas.mouse.warp_middle()
        self.canvas.mouse.reset_delta()
        self._mouse_lock = True

    def _release_mouse(self):
        """Release the mouse"""
        self.canvas.SetCursor(wx.NullCursor)
        self._mouse_lock = False

    def _on_loss_focus(self, evt):
        """Event fired when the user tabs out of the window."""
        self._escape()
        evt.Skip()

    def _escape(self):
        """Release the mouse and remove all key presses to the camera doesn't fly off into the distance."""
        # self._persistent_actions.clear()
        self.canvas.buttons.unpress_all()
        self._release_mouse()
