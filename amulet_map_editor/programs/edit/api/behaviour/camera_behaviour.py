from typing import TYPE_CHECKING, Optional, Tuple
import math
import wx
import time

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.api.opengl.data_types import CameraRotationType

from .base_behaviour import BaseBehaviour
from .ortho_navigation import screen_delta_to_world
from ..events import (
    InputHeldEvent,
    EVT_INPUT_HELD,
    InputPressEvent,
    EVT_INPUT_PRESS,
    InputReleaseEvent,
    EVT_INPUT_RELEASE,
)
from ..key_config import (
    ACT_MOVE_UP,
    ACT_MOVE_DOWN,
    ACT_MOVE_FORWARDS,
    ACT_MOVE_BACKWARDS,
    ACT_MOVE_LEFT,
    ACT_MOVE_RIGHT,
    ACT_CHANGE_MOUSE_MODE,
    ACT_INCR_SPEED,
    ACT_DECR_SPEED,
    ACT_ZOOM_IN,
    ACT_ZOOM_OUT,
    ACT_CHANGE_PROJECTION,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class CameraBehaviour(BaseBehaviour):
    """Adds the normal behaviour for the camera."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
        self._previous_mouse_lock = self.canvas.camera.rotating = False
        self._toggle_mouse_time = 0
        self._last_camera_rotation: CameraRotationType = (0.0, 0.0)
        # middle-mouse drag panning (top-down only)
        self._dragging = False
        self._drag_last: Optional[Tuple[int, int]] = None
        # frame-rate-independent keyboard movement
        self._last_held_time = time.time()

    def bind_events(self):
        """Set up all events required to run."""
        self.canvas.Bind(EVT_INPUT_HELD, self._on_input_held)
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)
        self.canvas.Bind(EVT_INPUT_RELEASE, self._on_input_release)
        self.canvas.Bind(wx.EVT_KEY_DOWN, self._on_key_press)
        self.canvas.Bind(wx.EVT_KILL_FOCUS, self._on_loss_focus)
        # middle-mouse drag panning
        self.canvas.Bind(wx.EVT_MIDDLE_DOWN, self._on_middle_down)
        self.canvas.Bind(wx.EVT_MIDDLE_UP, self._on_middle_up)
        self.canvas.Bind(wx.EVT_MOTION, self._on_drag_motion)
        self.canvas.Bind(wx.EVT_MOUSE_CAPTURE_LOST, self._on_capture_lost)

    def _on_key_press(self, evt: wx.KeyEvent):
        key = evt.GetUnicodeKey() or evt.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            self._escape()
        evt.Skip()

    def _on_middle_down(self, evt: wx.MouseEvent):
        """Start a middle-mouse drag pan (top-down only)."""
        if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            self._dragging = True
            self._drag_last = evt.GetPosition()
            if not self.canvas.HasCapture():
                self.canvas.CaptureMouse()
            self.canvas.SetCursor(wx.Cursor(wx.CURSOR_SIZING))
        evt.Skip()

    def _on_drag_motion(self, evt: wx.MouseEvent):
        """Pan the camera to follow a middle-mouse drag (top-down only)."""
        if self._dragging and self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            pos = evt.GetPosition()
            if self._drag_last is not None:
                dx = pos[0] - self._drag_last[0]
                dy = pos[1] - self._drag_last[1]
                world_dx, world_dz = screen_delta_to_world(
                    dx,
                    dy,
                    self.canvas.camera.fov,
                    self.canvas.camera.aspect_ratio,
                    *self.canvas.GetSize(),
                )
                x, y, z = self.canvas.camera.location
                # move the camera opposite the drag so the map follows the cursor
                x -= world_dx
                z -= world_dz
                self.canvas.camera.location_rotation = (x, y, z), (180, 90)
            self._drag_last = pos
        evt.Skip()

    def _on_middle_up(self, evt: wx.MouseEvent):
        """End a middle-mouse drag pan."""
        self._end_drag()
        evt.Skip()

    def _on_capture_lost(self, evt):
        """End a drag if the mouse capture is lost."""
        self._end_drag()
        evt.Skip()

    def _end_drag(self):
        if self._dragging:
            self._dragging = False
            self._drag_last = None
            if self.canvas.HasCapture():
                self.canvas.ReleaseMouse()
            self.canvas.SetCursor(wx.NullCursor)

    def _on_input_press(self, evt: InputPressEvent):
        """Logic to run each time the input press event is run."""
        if evt.action_id == ACT_CHANGE_PROJECTION:
            if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
                self._last_camera_rotation = self.canvas.camera.rotation
                self.canvas.camera.rotation = 180, 90
                self.canvas.camera.projection_mode = Projection.TOP_DOWN
            elif self.canvas.camera.projection_mode == Projection.TOP_DOWN:
                self.canvas.camera.rotation = self._last_camera_rotation
                self.canvas.camera.projection_mode = Projection.PERSPECTIVE
        elif evt.action_id == ACT_CHANGE_MOUSE_MODE:
            self.canvas.SetFocus()
            self._previous_mouse_lock = self.canvas.camera.rotating
            self._capture_mouse()
            self._toggle_mouse_time = time.time()

    def _on_input_release(self, evt: InputReleaseEvent):
        """Logic to run each time the input release event is run."""
        if evt.action_id == ACT_CHANGE_MOUSE_MODE:
            if self._previous_mouse_lock or time.time() - self._toggle_mouse_time > 0.1:
                self._release_mouse()
            else:
                self._capture_mouse()
        elif evt.action_id == ACT_INCR_SPEED:
            if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
                self.canvas.camera.move_speed *= 1.1
        elif evt.action_id == ACT_DECR_SPEED:
            if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
                self.canvas.camera.move_speed /= 1.1
        elif evt.action_id == ACT_ZOOM_IN:
            if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
                self.canvas.camera.fov = max(0.5, self.canvas.camera.fov / 1.2)
        elif evt.action_id == ACT_ZOOM_OUT:
            if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
                self.canvas.camera.fov = min(5000.0, self.canvas.camera.fov * 1.2)

    def _on_input_held(self, evt: InputHeldEvent):
        """Logic to run each time the input held event is run."""
        # time-scale the movement so the effective speed is independent of the
        # timer cadence. The old code moved per-tick amounts at 30Hz, so a
        # scale of dt * 30 preserves those speeds at any frame rate.
        now = time.time()
        dt = now - self._last_held_time
        self._last_held_time = now
        if not 0.0 < dt < 0.2:
            # gap after idle (or clock anomaly) -> assume one 60Hz frame
            dt = 1 / 60
        scale = dt * 30.0

        forward = up = right = pitch = yaw = 0
        up += (ACT_MOVE_UP in evt.action_ids) - (ACT_MOVE_DOWN in evt.action_ids)
        forward += (ACT_MOVE_FORWARDS in evt.action_ids) - (
            ACT_MOVE_BACKWARDS in evt.action_ids
        )
        right += (ACT_MOVE_RIGHT in evt.action_ids) - (ACT_MOVE_LEFT in evt.action_ids)

        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            if self.canvas.camera.rotating:
                delta_x, delta_y = self.canvas.mouse.delta_xy
                pitch = delta_y * 0.07
                yaw = delta_x * 0.07
                self.canvas.mouse.warp_middle()
                self.canvas.mouse.reset_delta()
            self.move_camera_relative(forward, up, right, pitch, yaw, scale)
        elif self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            if self.canvas.camera.rotating:
                delta_x, delta_y = self.canvas.mouse.delta_xy
                width, height = self.canvas.GetSize()
                width = max(1, width)
                height = max(1, height)
                forward += 2 * self.canvas.camera.fov * delta_y / height
                right -= (
                    2
                    * self.canvas.camera.fov
                    * self.canvas.camera.aspect_ratio
                    * delta_x
                    / width
                )
                self.canvas.mouse.warp_middle()
                self.canvas.mouse.reset_delta()
                # the rotating pan is driven by absolute mouse deltas which are
                # already frame-rate independent, so scale is left at its
                # no-op value for the mouse-pan (ortho) path.
                self.move_camera_relative(forward, up, right, pitch, yaw, scale)
            else:
                x, y, z = self.canvas.camera.location
                x += right * scale * self.canvas.camera.fov / 30
                z -= forward * scale * self.canvas.camera.fov / 30
                self.canvas.camera.location_rotation = (x, y, z), (180, 90)

        evt.Skip()

    def move_camera_relative(self, forward, up, right, pitch, yaw, scale=1.0):
        """Move the camera relative to its current location.

        :param scale: Multiplier applied to keyboard translation to make the
            effective speed independent of the timer cadence. Rotation
            (pitch/yaw) and the mouse-delta-driven ortho pan are not scaled as
            they are already frame-rate independent.
        """
        if not any((forward, up, right, pitch, yaw)):
            # if not self.canvas.camera.rotating and self._mouse_moved:
            #     self._mouse_moved = False
            #     self._selection_moved = True
            return
        x, y, z = self.canvas.camera.location
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            ry, rx = self.canvas.camera.rotation
            x += (
                self.canvas.camera.move_speed
                * scale
                * -(
                    math.cos(math.radians(ry)) * right
                    + math.sin(math.radians(ry)) * forward
                )
            )
            y += self.canvas.camera.move_speed * scale * up
            z += (
                self.canvas.camera.move_speed
                * scale
                * (
                    math.cos(math.radians(ry)) * forward
                    - math.sin(math.radians(ry)) * right
                )
            )
            rx += self.canvas.camera.rotate_speed * pitch
            ry += self.canvas.camera.rotate_speed * yaw
        else:
            ry, rx = 180, 90
            x += right
            z -= forward

        self.canvas.camera.location_rotation = (x, y, z), (ry, rx)

    def _capture_mouse(self):
        self.canvas.SetCursor(wx.Cursor(wx.CURSOR_BLANK))
        self.canvas.mouse.warp_middle()
        self.canvas.mouse.reset_delta()
        self.canvas.mouse.lock()
        self.canvas.camera.rotating = True

    def _release_mouse(self):
        """Release the mouse"""
        self.canvas.mouse.unlock()
        self.canvas.SetCursor(wx.NullCursor)
        self.canvas.camera.rotating = False

    def _on_loss_focus(self, evt):
        """Event fired when the user tabs out of the window."""
        self._escape()
        evt.Skip()

    def _escape(self):
        """Release the mouse and remove all key presses to the camera doesn't fly off into the distance."""
        # self._persistent_actions.clear()
        self.canvas.buttons.unpress_all()
        self._release_mouse()
