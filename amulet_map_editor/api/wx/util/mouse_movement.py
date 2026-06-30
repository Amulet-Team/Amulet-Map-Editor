import os
from typing import Tuple

import wx

try:
    from wayland_lock_pointer import PointerLocker
except ImportError:
    PointerLocker = None

from .window_container import WindowContainer


class MouseMovement(WindowContainer):
    """A class to get and set the cursor position and track changes."""

    def __init__(self, window: wx.Window):
        super().__init__(window)
        # The mouse position in range [0, 1]
        self._x: float = 0
        self._y: float = 0

        # The sum of all the deltas since it was last reset.
        # When the mouse moves, the delta is added to this value
        self._delta_x: float = 0
        self._delta_y: float = 0

        self._wayland_lock: PointerLocker | None = None

    def bind_events(self):
        """Set up all events required to run."""
        self.window.Bind(wx.EVT_MOTION, self._on_mouse_motion)

    def _to_relative(self, x: float, y: float) -> Tuple[float, float]:
        """Convert the x and y values to relative values 0 to 1"""
        dx, dy = self.window.GetSize()
        dx = max(1, dx)
        dy = max(1, dy)
        return x / dx, y / dy

    def _to_absolute(self, x: float, y: float) -> Tuple[int, int]:
        """Convert the relative values to absolute values."""
        dx, dy = self.window.GetSize()
        return int(x * dx), int(y * dy)

    def _on_mouse_motion(self, evt):
        """Event fired when the mouse is moved."""
        x, y = self._to_relative(*evt.GetPosition())
        self._delta_x += x - self._x
        self._delta_y += y - self._y
        self._x = x
        self._y = y
        evt.Skip()

    def _screen_middle(self) -> Tuple[int, int]:
        """Get the pixel coordinate of the middle of the screen"""
        x, y = self.window.GetSize()
        return int(x / 2), int(y / 2)

    def warp_middle(self):
        """Warp the cursor to the middle of the screen."""
        self.xy = self._screen_middle()

    def set_middle(self):
        """Set the start point to the middle of the screen. Does not warp."""
        pass

    def _warp(self, x: int, y: int):
        # Warp to the position.
        self.window.WarpPointer(x, y)
        # On some platforms warping does not move the cursor (wayland).
        # We must update the last position to the new position
        self._x, self._y = self._to_relative(
            *self.window.ScreenToClient(*wx.GetMousePosition())
        )

    @property
    def x(self) -> int:
        """The x pixel location of the mouse in the parent window."""
        return self.xy[0]

    @x.setter
    def x(self, x: int):
        """Set the x pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event.
        Under Wayland the mouse will not move"""
        self._warp(x, self.y)

    @property
    def y(self) -> int:
        """The y pixel location of the mouse in the parent window."""
        return self.xy[1]

    @y.setter
    def y(self, y: int):
        """Set the y pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event.
        Under Wayland the mouse will not move"""
        self._warp(self.x, y)

    @property
    def xy(self) -> Tuple[int, int]:
        """The x and y pixel location of the mouse in the parent window."""
        return self._to_absolute(self._x, self._y)

    @xy.setter
    def xy(self, xy: Tuple[int, int]):
        """Set the x and y pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event.
        Under Wayland the mouse will not move"""
        assert len(xy) == 2, "xy must be an iterable of two ints"
        x, y = map(int, xy)
        self._warp(x, y)

    def reset_delta(self):
        """Reset the mouse delta values.
        The amount the mouse has moved will be reset and the start position will become the current position.
        :return:
        """
        self._delta_x = self._delta_y = 0

    @property
    def delta_x(self) -> int:
        """The x pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this.
        """
        return self.delta_xy[0]

    @property
    def delta_y(self) -> int:
        """The y pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this.
        """
        return self.delta_xy[1]

    @property
    def delta_xy(self) -> Tuple[int, int]:
        """The x and y pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this.
        """
        return self._to_absolute(self._delta_x, self._delta_y)

    @property
    def mouse_xy_relative(self) -> tuple[float, float]:
        """
        The coordinate of the mouse in the window [-1.0, 1.0]
        """
        return self._x * 2 - 1, self._y * 2 - 1

    if PointerLocker is not None and os.environ.get("XDG_SESSION_TYPE") == "wayland":

        def _on_relative_motion(self, dx: float, dy: float) -> None:
            dx, dy = self._to_relative(dx, dy)
            self._delta_x += dx
            self._delta_y += dy

        def lock(self) -> None:
            if self._wayland_lock is None:
                self._wayland_lock = PointerLocker(
                    self.window.GetTopLevelParent().GetHandle()
                )
                self._wayland_lock.set_motion_callback(self._on_relative_motion)
                self._wayland_lock.lock()

        def unlock(self) -> None:
            if self._wayland_lock is not None:
                if self._wayland_lock.is_locked():
                    self._wayland_lock.unlock()
                self._wayland_lock = None

    else:

        def lock(self) -> None:
            pass

        def unlock(self) -> None:
            pass
