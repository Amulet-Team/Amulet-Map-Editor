import wx
from wx import glcanvas
from .camera import Camera


_SpeedChangedEventType = wx.NewEventType()
EVT_SPEED_CHANGED = wx.PyEventBinder(_SpeedChangedEventType)


class SpeedChangedEvent(wx.PyEvent):
    """Run when the speed of the camera has changed."""

    def __init__(self, speed: float):
        wx.PyEvent.__init__(self, eventType=_SpeedChangedEventType)
        self._speed = speed

    @property
    def speed(self) -> float:
        """The speed of the camera."""
        return self._speed


class ControllableCamera(Camera):
    """A slight modification to the default camera to add speed attributes."""

    __slots__ = ("_move_speed", "_rotate_speed")

    def __init__(self, canvas: glcanvas.GLCanvas):
        super().__init__(canvas)
        self._move_speed = 2.0
        self._rotate_speed = 2.0
        self._rotating = False

    @property
    def move_speed(self) -> float:
        """The speed that the camera moves at."""
        return self._move_speed

    @move_speed.setter
    def move_speed(self, val: float):
        """Set the speed that the camera moves at."""
        self._move_speed = float(val)
        wx.PostEvent(self.canvas, SpeedChangedEvent(self.move_speed))

    @property
    def rotate_speed(self) -> float:
        """The speed that the camera rotates at."""
        return self._rotate_speed

    @rotate_speed.setter
    def rotate_speed(self, val: float):
        """Set the speed that the camera rotates at."""
        self._rotate_speed = float(val)

    @property
    def rotating(self):
        """Is the camera rotating (True) or fixed (False)"""
        return self._rotating

    @rotating.setter
    def rotating(self, rotating: bool):
        """Set if the camera is rotating (True) or fixed (False)"""
        self._rotating = bool(rotating)
        self._notify_moved()
