import wx
from typing import Tuple
from .window_container import WindowContainer


class MouseMovement(WindowContainer):
    """A class to get and set the cursor position and track changes."""
    def __init__(self, window: wx.Window):
        super().__init__(window)
        # the current mouse position
        self._mouse_x = 0
        self._mouse_y = 0

        # the resting position of the mouse from which to calculate the delta
        # if the mouse is warped this will become the warped point
        self._mouse_start_x = 0
        self._mouse_start_y = 0

        # the sum of all the deltas since it was last reset.
        # when the mouse is warped the delta before it was warped will be added to this value
        self._mouse_delta_x = 0
        self._mouse_delta_y = 0

    def set_up_events(self):
        """Set up all events required to run."""
        self.window.Bind(wx.EVT_MOTION, self._on_mouse_motion)

    def _on_mouse_motion(self, evt):
        """Event fired when the mouse is moved."""
        self._mouse_x, self._mouse_y = evt.GetPosition()

    def _screen_middle(self) -> Tuple[int, int]:
        """Get the pixel coordinate of the middle of the screen"""
        x, y = self.window.GetSize()
        return (
            int(x / 2),
            int(y / 2),
        )

    def warp_middle(self):
        """Warp the cursor to the middle of the screen."""
        self.mouse_xy = self._screen_middle()

    def _warp(self):
        self.window.WarpPointer(self._mouse_x, self._mouse_y)

    @property
    def mouse_x(self) -> int:
        """The x pixel location of the mouse in the parent window."""
        return self._mouse_x

    @mouse_x.setter
    def mouse_x(self, mouse_x: int):
        """Set the x pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event."""
        assert type(mouse_x) is int, "mouse_x must be an int"
        self._mouse_delta_x += self._mouse_x - self._mouse_start_x
        self._mouse_start_x = self._mouse_x = mouse_x
        self._warp()

    @property
    def mouse_y(self) -> int:
        """The y pixel location of the mouse in the parent window."""
        return self._mouse_y

    @mouse_y.setter
    def mouse_y(self, mouse_y: int):
        """Set the y pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event."""
        assert type(mouse_y) is int, "mouse_y must be an int"
        self._mouse_delta_y += self._mouse_y - self._mouse_start_y
        self._mouse_start_y = self._mouse_y = mouse_y
        self._warp()

    @property
    def mouse_xy(self) -> Tuple[int, int]:
        """The x and y pixel location of the mouse in the parent window."""
        return self._mouse_x, self._mouse_y

    @mouse_xy.setter
    def mouse_xy(self, mouse_xy: Tuple[int, int]):
        """Set the x and y pixel location of the mouse in the parent window.
        Will warp the cursor to this position and create a mouse move event."""
        assert type(mouse_xy) is tuple and len(mouse_xy) == 2 and all(type(c) is int for c in mouse_xy), "mouse_xy must be of the form Tuple[int, int]"
        mouse_x, mouse_y = mouse_xy
        self._mouse_delta_x += self._mouse_x - self._mouse_start_x
        self._mouse_delta_y += self._mouse_y - self._mouse_start_y
        self._mouse_start_x = self._mouse_x = mouse_x
        self._mouse_start_y = self._mouse_y = mouse_y
        self._warp()

    def reset_delta(self):
        """Reset the mouse delta values.
        The amount the mouse has moved will be reset and the start position will become the current position.
        :return:
        """
        self._mouse_delta_x = self._mouse_delta_y = 0
        self._mouse_start_x = self._mouse_x
        self._mouse_start_y = self._mouse_y

    @property
    def mouse_delta_x(self) -> int:
        """The x pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this."""
        return self._mouse_x - self._mouse_start_x + self._mouse_delta_x

    @property
    def mouse_delta_y(self) -> int:
        """The y pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this."""
        return self._mouse_y - self._mouse_start_y + self._mouse_delta_y

    @property
    def mouse_delta_xy(self) -> Tuple[int, int]:
        """The x and y pixel distance between the current location and the location when reset_delta was called.
        If the pointer was warped the offset before it was warped will be added to this."""
        return self.mouse_delta_x, self.mouse_delta_y
