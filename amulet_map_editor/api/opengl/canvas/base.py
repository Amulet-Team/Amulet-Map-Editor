import wx
from wx import glcanvas
from OpenGL.GL import (
    GL_DEPTH_TEST,
    glEnable,
    glGenTextures,
    GL_CULL_FACE,
    glDepthFunc,
    GL_LEQUAL,
    GL_BLEND,
    glBlendFunc,
    GL_SRC_ALPHA,
    GL_ONE_MINUS_SRC_ALPHA,
    glDeleteTextures,
)
import uuid
import numpy
import math
from typing import Optional
import sys
from amulet_map_editor.api.opengl.data_types import (
    CameraLocationType,
    CameraRotationType,
)
from amulet_map_editor.api.opengl.matrix import (
    rotation_matrix_yx,
    perspective_matrix,
    displacement_matrix,
    orthographic_matrix,
)

Orthographic = 0
Perspective = 1


class BaseCanvas(glcanvas.GLCanvas):
    def __init__(self, parent: wx.Window):
        display_attributes = wx.glcanvas.GLAttributes()
        display_attributes.PlatformDefaults().MinRGBA(8, 8, 8, 8).DoubleBuffer().Depth(
            24
        ).EndList()
        super().__init__(parent, display_attributes, size=parent.GetClientSize())
        self._projection_mode = Perspective
        self._fov = [100.0, 70.0]
        self._clipping = [
            (-10000.0, 10000.0),
            (0.1, 10000.0)
        ]
        self._aspect_ratio = 4 / 3
        self._projection_matrix: Optional[numpy.ndarray] = None
        if sys.platform == "linux":
            # setup the OpenGL context. This apparently fixes #84
            self._context = glcanvas.GLContext(self)
        else:
            context_attributes = wx.glcanvas.GLContextAttrs()
            context_attributes.CoreProfile().OGLVersion(
                3, 3
            ).Robust().ResetIsolation().EndList()
            self._context = glcanvas.GLContext(
                self, ctxAttrs=context_attributes
            )  # setup the OpenGL context
        self.SetCurrent(self._context)
        self._context_identifier = str(
            uuid.uuid4()
        )  # create a UUID for the context. Used to get shaders
        self._gl_texture_atlas = glGenTextures(1)  # Create the atlas texture location
        self._setup_opengl()  # set some OpenGL states

        self._transformation_matrix: Optional[numpy.ndarray] = None

    @property
    def context_identifier(self) -> str:
        return self._context_identifier

    def _setup_opengl(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def _close(self):
        glDeleteTextures([self._gl_texture_atlas])

    def _reset_matrix(self):
        self._projection_matrix = None
        self._transformation_matrix = None

    @property
    def camera_location(self) -> CameraLocationType:
        raise NotImplementedError

    @property
    def camera_rotation(self) -> CameraRotationType:
        """The rotation of the camera. (yaw, pitch).
        This should behave the same as how Minecraft handles it.
        """
        raise NotImplementedError

    @property
    def fov(self) -> float:
        return self._fov[self._projection_mode]

    @fov.setter
    def fov(self, fov: float):
        self._fov[self._projection_mode] = fov
        self._reset_matrix()

    @property
    def aspect_ratio(self) -> float:
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio: float):
        self._aspect_ratio = aspect_ratio
        self._reset_matrix()

    @staticmethod
    def rotation_matrix(yaw, pitch):
        return rotation_matrix_yx(math.radians(yaw + 180), math.radians(pitch))

    @property
    def camera_matrix(self) -> numpy.ndarray:
        """The matrix to convert world space to camera space."""
        return numpy.matmul(
            self.rotation_matrix(*self.camera_rotation),
            displacement_matrix(*-numpy.array(self.camera_location)),
        )

    @property
    def projection_matrix(self) -> numpy.ndarray:
        """The matrix to convert camera space to screen space."""
        if self._projection_matrix is None:
            if self._projection_mode == Orthographic:
                self._projection_matrix = self.orthographic_matrix
            else:
                self._projection_matrix = self.perspective_matrix

        return self._projection_matrix

    @property
    def orthographic_matrix(self) -> numpy.ndarray:
        """The orthographic matrix to convert camera space to screen space."""
        near, far = self._clipping[self._projection_mode]
        return orthographic_matrix(self.fov, self.aspect_ratio, near, far)

    @property
    def perspective_matrix(self) -> numpy.ndarray:
        """The perspective matrix to convert camera space to screen space."""
        z_near, z_far = self._clipping[self._projection_mode]
        return perspective_matrix(math.radians(self.fov), self.aspect_ratio, z_near, z_far)

    @property
    def transformation_matrix(self) -> numpy.ndarray:
        """The world to projection matrix."""
        # camera translation
        if self._transformation_matrix is None:
            self._transformation_matrix = numpy.matmul(
                self.projection_matrix,
                self.camera_matrix,
            )

        return self._transformation_matrix
