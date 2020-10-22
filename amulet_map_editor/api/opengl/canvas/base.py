import wx
from wx import glcanvas
from OpenGL.GL import *
import uuid
import numpy
import math
from typing import Optional
from amulet_map_editor.api.opengl.data_types import (
    CameraLocationType,
    CameraRotationType,
)
from amulet_map_editor.api.opengl.matrix import rotation_matrix_yx, projection_matrix, displacement_matrix


class BaseCanvas(glcanvas.GLCanvas):
    def __init__(self, parent: wx.Window):
        display_attributes = wx.glcanvas.GLAttributes()
        display_attributes.PlatformDefaults().MinRGBA(8, 8, 8, 8).DoubleBuffer().Depth(
            24
        ).EndList()
        super().__init__(parent, display_attributes, size=parent.GetClientSize())
        self._projection = [70.0, 4 / 3, 0.1, 10000.0]
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
        return self._projection[0]

    @fov.setter
    def fov(self, fov: float):
        self._projection[0] = fov
        self._transformation_matrix = None

    @property
    def aspect_ratio(self) -> float:
        return self._projection[1]

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio: float):
        self._projection[1] = aspect_ratio
        self._transformation_matrix = None

    @staticmethod
    def rotation_matrix(yaw, pitch):
        return rotation_matrix_yx(math.radians(yaw+180), math.radians(pitch))

    def projection_matrix(self):
        # camera projection
        fovy, aspect, z_near, z_far = self._projection
        fovy = math.radians(fovy)
        return projection_matrix(fovy, aspect, z_near, z_far)

    @property
    def transformation_matrix(self) -> numpy.ndarray:
        """The world to projection matrix."""
        # camera translation
        if self._transformation_matrix is None:
            self._transformation_matrix = numpy.matmul(
                self.projection_matrix(),
                numpy.matmul(
                    self.rotation_matrix(*self.camera_rotation),
                    displacement_matrix(*-numpy.array(self.camera_location)),
                )
            )

        return self._transformation_matrix
