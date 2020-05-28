import wx
from wx import glcanvas
from OpenGL.GL import *
import uuid
import numpy
import math
from typing import Optional
from amulet_map_editor.opengl.data_types import CameraLocationType, CameraRotationType


class BaseCanvas(glcanvas.GLCanvas):
    def __init__(self, parent: wx.Window):
        attribs = (glcanvas.WX_GL_CORE_PROFILE, glcanvas.WX_GL_RGBA, glcanvas.WX_GL_DOUBLEBUFFER, glcanvas.WX_GL_DEPTH_SIZE, 24)
        super().__init__(parent, -1, size=parent.GetClientSize(), attribList=attribs)
        self._projection = [70.0, 4 / 3, 0.1, 10000.0]
        self._context = glcanvas.GLContext(self)  # setup the OpenGL context
        self.SetCurrent(self._context)
        self.context_identifier = str(uuid.uuid4())  # create a UUID for the context. Used to get shaders
        self._gl_texture_atlas = glGenTextures(1)  # Create the atlas texture location
        self._setup_opengl()  # set some OpenGL states

        self._transformation_matrix: Optional[numpy.ndarray] = None

    def _setup_opengl(self):
        glClearColor(0.5, 0.66, 1.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        glBindTexture(GL_TEXTURE_2D, self._gl_texture_atlas)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        glBindTexture(GL_TEXTURE_2D, 0)

    def _close(self):
        glDeleteTextures([self._gl_texture_atlas])

    @property
    def camera_location(self) -> CameraLocationType:
        raise NotImplementedError

    @property
    def camera_rotation(self) -> CameraRotationType:
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
    def rotation_matrix(pitch, yaw):
        c = math.cos(math.radians(yaw))
        s = math.sin(math.radians(yaw))

        y_rot = numpy.array(
            [
                [c, 0, -s, 0],
                [0, 1, 0, 0],
                [s, 0, c, 0],
                [0, 0, 0, 1]
            ],
            dtype=numpy.float32
        )

        # rotations
        c = math.cos(math.radians(pitch))
        s = math.sin(math.radians(pitch))

        x_rot = numpy.array(
            [
                [1, 0, 0, 0],
                [0, c, s, 0],
                [0, -s, c, 0],
                [0, 0, 0, 1]
            ],
            dtype=numpy.float32
        )

        return numpy.matmul(y_rot, x_rot)

    def projection_matrix(self):
        # camera projection
        fovy, aspect, z_near, z_far = self._projection
        fovy = math.radians(fovy)
        f = 1 / math.tan(fovy / 2)
        return numpy.array(
            [
                [f / aspect, 0, 0, 0],
                [0, f, 0, 0],
                [0, 0, (z_far + z_near) / (z_near - z_far), -1],
                [0, 0, (2 * z_far * z_near) / (z_near - z_far), 0]
            ],
            dtype=numpy.float32
        )

    @property
    def transformation_matrix(self) -> numpy.ndarray:
        # camera translation
        if self._transformation_matrix is None:
            transformation_matrix = numpy.eye(4, dtype=numpy.float32)
            transformation_matrix[3, :3] = numpy.array(self.camera_location) * -1

            transformation_matrix = numpy.matmul(transformation_matrix, self.rotation_matrix(*self.camera_rotation))
            self._transformation_matrix = numpy.matmul(transformation_matrix, self.projection_matrix())

        return self._transformation_matrix
