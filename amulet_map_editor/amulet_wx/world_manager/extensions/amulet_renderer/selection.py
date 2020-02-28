import numpy
from OpenGL.GL import *
from ..amulet_renderer import shaders
import itertools
from typing import Tuple


class Selection:
    def __init__(self, identifier: str, texture_bounds: Tuple[float, float, float, float]):
        self.identifier = identifier
        self._select_state = 0  # number of points selected
        self._loc = numpy.zeros(6)
        self._shader = None
        self._trm_mat_loc = None
        self._vao = None
        self._vbo = None
        self._verts = numpy.zeros((6*2*3, 10), dtype=numpy.float32)
        self._verts[:, 5:9] = texture_bounds
        self._draw_count = 36

    @property
    def select_state(self) -> int:
        return self._select_state

    @property
    def min(self) -> numpy.ndarray:
        return self._loc[:3]

    @min.setter
    def min(self, val):
        self._loc[:3] = val

    @property
    def max(self) -> numpy.ndarray:
        return self._loc[3:]

    @max.setter
    def max(self, val):
        self._loc[3:] = val

    def create_geometry(self):
        _box_coordinates = numpy.array(
            list(
                itertools.product(
                    *self._loc.reshape((2, 3)).T.tolist()
                )
            )
        )
        _cube_face_lut = numpy.array([  # This maps to the verticies used (defined in cube_vert_lut)
            0, 4, 5, 1,
            3, 7, 6, 2,
            4, 0, 2, 6,
            5, 4, 6, 7,
            1, 5, 7, 3,
            0, 1, 3, 2
        ])
        _texture_uv = numpy.array([0, 0, 1, 1], numpy.float)
        _uv_slice = [0, 1, 2, 1, 2, 3, 0, 3]

        _tri_face = numpy.array([0, 1, 2, 0, 2, 3]*6, numpy.uint32).reshape((6, 6)) + numpy.arange(0, 24, 4).reshape((6,1))
        _verts = _box_coordinates[_cube_face_lut[_tri_face]]
        _texture_coords = _texture_uv[_uv_slice*6].reshape(-1, 2)[_tri_face, :]  # texture vertices
        self._verts[:, :3] = _verts.reshape((-1, 3))
        self._verts[:, 3:5] = _texture_coords.reshape(-1, 2)

        glBindVertexArray(self._vao)
        glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
        glBufferData(GL_ARRAY_BUFFER, self._verts.size * 4, self._verts, GL_DYNAMIC_DRAW)

    def _setup(self):
        """Set up an empty VAO"""
        if self._vao is None:
            self._vao = glGenVertexArrays(1)
            glBindVertexArray(self._vao)
            self._vbo = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
            self.create_geometry()
            glBufferData(GL_ARRAY_BUFFER, self._verts.size*4, self._verts, GL_DYNAMIC_DRAW)
            # vertex attribute pointers
            glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(0))
            glEnableVertexAttribArray(0)
            # texture coords attribute pointers
            glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(12))
            glEnableVertexAttribArray(1)
            # texture coords attribute pointers
            glVertexAttribPointer(2, 4, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(20))
            glEnableVertexAttribArray(2)
            # tint value
            glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(36))
            glEnableVertexAttribArray(3)

            glBindVertexArray(0)

            self._shader = shaders.get_shader(self.identifier, 'render_chunk')
            self._trm_mat_loc = glGetUniformLocation(self._shader, "transformation_matrix")

    def unload(self):
        if self._vao is not None:
            glDeleteVertexArrays(1, self._vao)
            self._vao = None

    def draw(self, transformation_matrix):
        self._setup()
        if self._vao:
            glUseProgram(self._shader)
            glUniformMatrix4fv(self._trm_mat_loc, 1, GL_FALSE, transformation_matrix)
            glBindVertexArray(self._vao)
            glDrawArrays(GL_TRIANGLES, 0, self._draw_count)
