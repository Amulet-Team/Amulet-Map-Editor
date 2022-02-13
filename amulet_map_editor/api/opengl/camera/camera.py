import numpy
from typing import Optional, Tuple, List
from enum import Enum
import wx
from wx import glcanvas
import math
from ..canvas_container import CanvasContainer
from ..data_types import CameraLocationType, CameraRotationType

from ..matrix import (
    rotation_matrix_yx,
    perspective_matrix,
    displacement_matrix,
    orthographic_matrix,
    TransformationMatrixType,
)


class Projection(Enum):
    TOP_DOWN = 0
    PERSPECTIVE = 1


_CameraMoveChangeEventType = wx.NewEventType()
EVT_CAMERA_MOVED = wx.PyEventBinder(_CameraMoveChangeEventType)


class CameraMovedEvent(wx.PyEvent):
    """Run when the camera has moved or rotated."""

    def __init__(
        self, camera_location: CameraLocationType, camera_rotation: CameraRotationType
    ):
        wx.PyEvent.__init__(self, eventType=_CameraMoveChangeEventType)
        self._location = camera_location
        self._rotation = camera_rotation

    @property
    def camera_location(self) -> CameraLocationType:
        """The location of the camera. (x, y, z)"""
        return self._location

    @property
    def camera_rotation(self) -> CameraRotationType:
        """The rotation of the camera. (yaw, pitch).
        This should behave the same as how Minecraft handles it.
        """
        return self._rotation


_ProjectionChangeEventType = wx.NewEventType()
EVT_PROJECTION_CHANGED = wx.PyEventBinder(_ProjectionChangeEventType)


class ProjectionChangedEvent(wx.PyEvent):
    """Run when the projection of the camera has changed."""

    def __init__(self, projection: Projection):
        wx.PyEvent.__init__(self, eventType=_ProjectionChangeEventType)
        self._projection = projection

    @property
    def projection(self) -> Projection:
        """The location of the camera. (x, y, z)"""
        return self._projection


class Camera(CanvasContainer):
    """A class to hold the state information of the camera."""

    _projection_matrix: Optional[TransformationMatrixType]
    _transformation_matrix: Optional[TransformationMatrixType]

    __slots__ = (
        "_location",
        "_rotation",
        "_projection_mode",
        "_fov",
        "_clipping",
        "_aspect_ratio",
        "_projection_matrix",
        "_transformation_matrix",
    )

    def __init__(self, canvas: glcanvas.GLCanvas):
        super().__init__(canvas)

        self._location: CameraLocationType = (0.0, 0.0, 0.0)
        self._rotation: CameraRotationType = (0.0, 0.0)
        self._projection_mode = Projection.PERSPECTIVE
        self._fov = [100.0, 70.0]
        self._clipping: List[Tuple[float, float]] = [
            (-(10**5), 10**5),
            (0.1, 10000.0),
        ]
        self._aspect_ratio = 4 / 3
        self._projection_matrix: Optional[TransformationMatrixType] = None
        self._transformation_matrix: Optional[TransformationMatrixType] = None

    def _reset_matrix(self):
        self._projection_matrix = None
        self._transformation_matrix = None

    def _notify_moved(self):
        """Post a CameraMovedEvent"""
        wx.PostEvent(self.canvas, CameraMovedEvent(self.location, self.rotation))

    @property
    def projection_mode(self) -> Projection:
        return self._projection_mode

    @projection_mode.setter
    def projection_mode(self, projection_mode: Projection):
        assert (
            projection_mode in Projection
        ), f"{projection_mode} is not a valid projection."
        if self._projection_mode != projection_mode:
            self._projection_mode = projection_mode
            self._reset_matrix()
            wx.PostEvent(self.canvas, ProjectionChangedEvent(self.projection_mode))

    @property
    def location(self) -> CameraLocationType:
        """The location of the camera. (x, y, z)"""
        return self._location

    @location.setter
    def location(self, camera_location: CameraLocationType):
        """Set the location of the camera. (x, y, z).
        Generates EVT_CAMERA_MOVED on the parent canvas."""
        if self.set_location(camera_location):
            self._notify_moved()

    def set_location(self, camera_location: CameraLocationType) -> bool:
        """Set the location of the camera. (x, y, z)."""
        assert (
            len(camera_location) == 3
        ), "camera_location must be an iterable of three floats."
        camera_location = tuple(map(float, camera_location))
        if camera_location != self._location:
            self._reset_matrix()
            self._location = camera_location
            return True
        return False

    @property
    def rotation(self) -> CameraRotationType:
        """The rotation of the camera. (yaw, pitch).
        This should behave the same as how Minecraft handles it.
        """
        return self._rotation

    @rotation.setter
    def rotation(self, camera_rotation: CameraRotationType):
        """Set the rotation of the camera. (yaw, pitch).
        yaw (-180 to 180), pitch (-90 to 90)
        This should behave the same as how Minecraft handles it.
        Generates EVT_CAMERA_MOVED on the parent canvas."""
        if self.set_rotation(camera_rotation):
            self._notify_moved()

    def set_rotation(self, camera_rotation: CameraRotationType) -> bool:
        """Set the rotation of the camera. (yaw, pitch).
        yaw (-180 to 180), pitch (-90 to 90)
        This should behave the same as how Minecraft handles it."""
        assert (
            len(camera_rotation) == 2
        ), "camera_rotation must be an iterable of two floats."
        ry, rx = map(float, camera_rotation)
        if not -180 <= ry < 180:
            ry %= 360
            if ry >= 180:
                ry -= 360
        if not -90 <= rx <= 90:
            rx = max(min(rx, 90), -90)
        camera_rotation = (ry, rx)
        if camera_rotation != self._rotation:
            self._reset_matrix()
            self._rotation = camera_rotation
            return True
        return False

    @property
    def location_rotation(self) -> Tuple[CameraLocationType, CameraRotationType]:
        """Get the camera location and rotation in one property."""
        return self.location, self.rotation

    @location_rotation.setter
    def location_rotation(
        self, location_rotation: Tuple[CameraLocationType, CameraRotationType]
    ):
        """Set the camera location and rotation in one property.
        Generates EVT_CAMERA_MOVED on the parent canvas."""
        location, rotation = location_rotation
        moved = self.set_location(location)
        rotated = self.set_rotation(rotation)
        if moved or rotated:
            self._notify_moved()

    def _set_fov(self, mode: Projection, fov: float):
        self._fov[mode.value] = float(fov)
        self._reset_matrix()

    @property
    def fov(self) -> float:
        """The field of view of the camera.
        The value will vary based on the projection mode."""
        return self._fov[self.projection_mode.value]

    @fov.setter
    def fov(self, fov: float):
        """Set the field of view of the camera.
        The value will vary based on the projection mode."""
        self._set_fov(self.projection_mode, fov)

    @property
    def perspective_fov(self) -> float:
        """The field of view of the camera in degrees when in perspective mode."""
        return self._fov[Projection.PERSPECTIVE.value]

    @perspective_fov.setter
    def perspective_fov(self, fov: float):
        """Set the field of view of the camera in degrees when in perspective mode."""
        self._set_fov(Projection.PERSPECTIVE, fov)

    @property
    def orthographic_fov(self) -> float:
        """The field of view of the camera when in orthographic mode."""
        return self._fov[Projection.TOP_DOWN.value]

    @orthographic_fov.setter
    def orthographic_fov(self, fov: float):
        """Set the field of view of the camera when in orthographic mode."""
        self._set_fov(Projection.TOP_DOWN, fov)

    def _set_clipping(self, mode: Projection, clipping: Tuple[float, float]):
        assert len(clipping) == 2, "camera_rotation must be an iterable of two floats."
        self._clipping[mode.value] = tuple(map(float, clipping))
        self._reset_matrix()

    @property
    def perspective_clipping(self) -> Tuple[float, float]:
        """The near and far clipping distance when in perspective mode."""
        return self._clipping[Projection.PERSPECTIVE.value]

    @perspective_clipping.setter
    def perspective_clipping(self, clipping: Tuple[float, float]):
        """Set the near and far clipping distance when in perspective mode."""
        self._set_clipping(Projection.PERSPECTIVE, clipping)

    @property
    def orthographic_clipping(self) -> Tuple[float, float]:
        """The near and far clipping distance when in orthographic mode."""
        return self._clipping[Projection.TOP_DOWN.value]

    @orthographic_clipping.setter
    def orthographic_clipping(self, clipping: Tuple[float, float]):
        """Set the near and far clipping distance when in orthographic mode."""
        self._set_clipping(Projection.TOP_DOWN, clipping)

    @property
    def aspect_ratio(self) -> float:
        """The aspect ratio of the camera (width/weight)"""
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio: float):
        """Set the aspect ratio of the camera (width/weight)"""
        self._aspect_ratio = float(aspect_ratio)
        self._reset_matrix()

    @staticmethod
    def rotation_matrix(yaw, pitch) -> TransformationMatrixType:
        """Helper function to get a rotation matrix for yaw and pitch.

        :param yaw: Yaw in degrees.
        :param pitch: Pitch in degrees.
        :return: A 4x4 rotation matrix.
        """
        return rotation_matrix_yx(math.radians(yaw + 180), math.radians(pitch))

    @property
    def camera_matrix(self) -> TransformationMatrixType:
        """The matrix to convert world space to camera space."""
        return numpy.matmul(
            self.rotation_matrix(*self.rotation),
            displacement_matrix(*-numpy.array(self.location)),
        )

    @property
    def projection_matrix(self) -> TransformationMatrixType:
        """The matrix to convert camera space to screen space."""
        if self._projection_matrix is None:
            if self.projection_mode == Projection.TOP_DOWN:
                self._projection_matrix = self.orthographic_matrix
            else:
                self._projection_matrix = self.perspective_matrix
            self._projection_matrix.flags.writeable = False

        return self._projection_matrix

    @property
    def orthographic_matrix(self) -> TransformationMatrixType:
        """The orthographic matrix to convert camera space to screen space."""
        near, far = self._clipping[self.projection_mode.value]
        return orthographic_matrix(self.fov, self.aspect_ratio, near, far)

    @property
    def perspective_matrix(self) -> TransformationMatrixType:
        """The perspective matrix to convert camera space to screen space."""
        z_near, z_far = self._clipping[self.projection_mode.value]
        return perspective_matrix(
            math.radians(self.fov), self.aspect_ratio, z_near, z_far
        )

    @property
    def transformation_matrix(self) -> TransformationMatrixType:
        """The world to projection matrix."""
        # camera translation
        if self._transformation_matrix is None:
            self._transformation_matrix = numpy.matmul(
                self.projection_matrix, self.camera_matrix
            )
            self._transformation_matrix.flags.writeable = False

        return self._transformation_matrix
