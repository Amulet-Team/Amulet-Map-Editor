import wx
from typing import Tuple
from .window_container import WindowContainer


class MouseMovement(WindowContainer):
    """A class to get and set the cursor position and track changes."""

    def __init__(self, window: wx.Window):
        super().__init__(window)
        # the current mouse position
        self._x: float = 0
        self._y: float = 0

        # the resting position of the mouse from which to calculate the delta
        # if the mouse is warped this will become the warped point
        self._start_x: float = 0
        self._start_y: float = 0

        # the sum of all the deltas since it was last reset.
        # when the mouse is warped the delta before it was warped will be added to this value
        self._delta_x: float = 0
        self._delta_y: float = 0

    def bind_events(self):
        """Set up all events required to run."""
        self.window.Bind(wx.EVT_MOTION, self._on_mouse_motion)

    def _to_relative(self, x: int, y: int) -> Tuple[float, float]:
        """Convert the x and y values to relative values 0 to 1"""
        dx, dy = self.window.GetSize()
        return x / dx, y / dy

    def _to_absolute(self, x: float, y: float) -> Tuple[int, int]:
        """Convert the relative values to absolute values."""
        dx, dy = self.window.GetSize()
        return int(x * dx), int(y * dy)

    def _on_mouse_motion(self, evt):
        """Event fired when the mouse is moved."""
        self._x, self._y = self._to_relative(*evt.GetPosition())
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

    def set_middle(self):
        """Set the start point to the middle of the screen. Does not warp."""
        self._start_x, self._start_y = 0.5, 0.5

    def _warp(self):
        self.window.WarpPointer(*self._to_absolute(self._x, self._y))

    @property
    def x(self) -> int:
        """The x pixel location of the mouse in the parent window."""
        return self._to_absolute(self._x, 0)[0]

    @x.setter
    def x(self, x: int):
        """Set the x pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event."""
        assert type(x) is int, "x must be an int"
        self._delta_x += self._x - self._start_x
        self._start_x = self._x = self._to_relative(x, 0)[0]
        self._warp()

    @property
    def y(self) -> int:
        """The y pixel location of the mouse in the parent window."""
        return self._to_absolute(0, self._y)[1]

    @y.setter
    def y(self, y: int):
        """Set the y pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event."""
        assert type(y) is int, "y must be an int"
        self._delta_y += self._y - self._start_y
        self._start_y = self._y = self._to_relative(0, y)[1]
        self._warp()

    @property
    def xy(self) -> Tuple[int, int]:
        """The x and y pixel location of the mouse in the parent window."""
        return self._to_absolute(self._x, self._y)

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
        (self._start_x, self._start_y) = (self._x, self._y) = self._to_relative(x, y)
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
        return self.delta_xy[0]

    @property
    def delta_y(self) -> int:
        """The y pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this."""
        return self.delta_xy[1]

    @property
    def delta_xy(self) -> Tuple[int, int]:
        """The x and y pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this."""
        return self._to_absolute(
            self._x - self._start_x + self._delta_x,
            self._y - self._start_y + self._delta_y,
        )
