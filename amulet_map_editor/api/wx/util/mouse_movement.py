import wx
from typing import Tuple
from .window_container import WindowContainer


class MouseMovement(WindowContainer):
    """A class to get and set the cursor position and track changes."""

    def __init__(self, window: wx.Window):
        super().__init__(window)
        # the current mouse position
        self._x = 0
        self._y = 0

        # the resting position of the mouse from which to calculate the delta
        # if the mouse is warped this will become the warped point
        self._start_x = 0
        self._start_y = 0

        # the sum of all the deltas since it was last reset.
        # when the mouse is warped the delta before it was warped will be added to this value
        self._delta_x = 0
        self._delta_y = 0

    def set_up_events(self):
        """Set up all events required to run."""
        self.window.Bind(wx.EVT_MOTION, self._on_mouse_motion)

    def _on_mouse_motion(self, evt):
        """Event fired when the mouse is moved."""
        self._x, self._y = evt.GetPosition()
        evt.Skip()

    def _screen_middle(self) -> Tuple[int, int]:
        """Get the pixel coordinate of the middle of the screen"""
        x, y = self.window.GetSize()
        return (
            int(x / 2),
            int(y / 2),
        )

    def warp_middle(self):
        """Warp the cursor to the middle of the screen."""
        self.xy = self._screen_middle()

    def _warp(self):
        self.window.WarpPointer(self._x, self._y)

    @property
    def x(self) -> int:
        """The x pixel location of the mouse in the parent window."""
        return self._x

    @x.setter
    def x(self, x: int):
        """Set the x pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event."""
        assert type(x) is int, "x must be an int"
        self._delta_x += self._x - self._start_x
        self._start_x = self._x = x
        self._warp()

    @property
    def y(self) -> int:
        """The y pixel location of the mouse in the parent window."""
        return self._y

    @y.setter
    def y(self, y: int):
        """Set the y pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event."""
        assert type(y) is int, "y must be an int"
        self._delta_y += self._y - self._start_y
        self._start_y = self._y = y
        self._warp()

    @property
    def xy(self) -> Tuple[int, int]:
        """The x and y pixel location of the mouse in the parent window."""
        return self._x, self._y

    @xy.setter
    def xy(self, xy: Tuple[int, int]):
        """Set the x and y pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event."""
        assert (
            type(xy) is tuple and len(xy) == 2 and all(type(c) is int for c in xy)
        ), "xy must be of the form Tuple[int, int]"
        x, y = xy
        self._delta_x += self._x - self._start_x
        self._delta_y += self._y - self._start_y
        self._start_x = self._x = x
        self._start_y = self._y = y
        self._warp()

    def reset_delta(self):
        """Reset the mouse delta values.
        The amount the mouse has moved will be reset and the start position will become the current position.
        :return:
        """
        self._delta_x = self._delta_y = 0
        self._start_x = self._x
        self._start_y = self._y

    @property
    def delta_x(self) -> int:
        """The x pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this."""
        return self._x - self._start_x + self._delta_x

    @property
    def delta_y(self) -> int:
        """The y pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this."""
        return self._y - self._start_y + self._delta_y

    @property
    def delta_xy(self) -> Tuple[int, int]:
        """The x and y pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this."""
        return self.delta_x, self.delta_y
