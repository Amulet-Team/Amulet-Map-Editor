import numpy
from typing import Optional, Tuple
from enum import Enum
import wx
from wx import glcanvas
import math
from ..canvas_container import CanvasContainer
from ..data_types import (
    CameraLocationType,
    CameraRotationType,
)

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
        self._clipping = [(-(10 ** 5), 10 ** 5), (0.1, 10000.0)]
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
        self.set_location(camera_location)
        self._notify_moved()

    def set_location(self, camera_location: CameraLocationType):
        """Set the location of the camera. (x, y, z)."""
        assert (
            type(camera_location) in (tuple, list)
            and len(camera_location) == 3
            and all(type(v) in (int, float) for v in camera_location)
        ), "format for camera_location is invalid"
        self._reset_matrix()
        self._location = tuple(camera_location)

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
        self.set_rotation(camera_rotation)
        self._notify_moved()

    def set_rotation(self, camera_rotation: CameraRotationType):
        """Set the location of the camera. (x, y, z)."""
        assert (
            type(camera_rotation) in (tuple, list)
            and len(camera_rotation) == 2
            and all(type(v) in (int, float) for v in camera_rotation)
        ), "format for camera_rotation is invalid"
        self._reset_matrix()
        self._rotation = tuple(camera_rotation)

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
        self.set_location(location)
        self.set_rotation(rotation)
        self._notify_moved()

    @property
    def fov(self) -> float:
        """The field of view of the camera in degrees."""
        return self._fov[self.projection_mode.value]

    @fov.setter
    def fov(self, fov: float):
        """Set the field of view of the camera in degrees."""
        assert type(fov) in (int, float)
        self._fov[self.projection_mode.value] = fov
        self._reset_matrix()

    @property
    def aspect_ratio(self) -> float:
        """The aspect ratio of the camera (width/weight)"""
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio: float):
        """Set the aspect ratio of the camera (width/weight)"""
        assert type(aspect_ratio) in (int, float)
        self._aspect_ratio = aspect_ratio
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
                self.projection_matrix,
                self.camera_matrix,
            )

        return self._transformation_matrix
