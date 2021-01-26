from wx import glcanvas
from .camera import Camera


class ControllableCamera(Camera):
    """A slight modification to the default camera to add speed attributes."""

    __slots__ = (
        "_move_speed",
        "_rotate_speed",
    )

    def __init__(self, canvas: glcanvas.GLCanvas):
        super().__init__(canvas)
        self._move_speed = 2.0
        self._rotate_speed = 2.0

    @property
    def move_speed(self) -> float:
        """The speed that the camera moves at."""
        return self._move_speed

    @move_speed.setter
    def move_speed(self, val: float):
        """Set the speed that the camera moves at."""
        assert type(val) in (int, float)
        self._move_speed = val

    @property
    def rotate_speed(self) -> float:
        """The speed that the camera rotates at."""
        return self._rotate_speed

    @rotate_speed.setter
    def rotate_speed(self, val: float):
        """Set the speed that the camera rotates at."""
        assert type(val) in (int, float)
        self._rotate_speed = val
