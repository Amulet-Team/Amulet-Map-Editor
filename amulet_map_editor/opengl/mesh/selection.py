import numpy
from OpenGL.GL import *
from amulet_map_editor.opengl import shaders
import itertools
from typing import Tuple


class Selection:
    def __init__(self,
        identifier: str,
        white_texture_bounds: Tuple[float, float, float, float],
        green_texture_bounds: Tuple[float, float, float, float],
        blue_texture_bounds: Tuple[float, float, float, float]
    ):
        self.identifier = identifier
        self._select_state = 0  # number of points selected
        self._loc = numpy.zeros(6)
        self._shader = None
        self._trm_mat_loc = None
        self._vao = None
        self._vbo = None
        self._verts = numpy.zeros((6*2*3*3, 10), dtype=numpy.float32)
        self._verts[:36, 5:9] = white_texture_bounds
        self._verts[36:72, 5:9] = green_texture_bounds
        self._verts[72:, 5:9] = blue_texture_bounds
        self._draw_count = 36

    @property
    def select_state(self) -> int:
        return self._select_state

    @select_state.setter
    def select_state(self, value: int):
        self._select_state = value

    @property
    def point1(self) -> numpy.ndarray:
        return self._loc[:3]

    @point1.setter
    def point1(self, val):
        self._loc[:3] = val

    @property
    def point2(self) -> numpy.ndarray:
        return self._loc[3:]

    @point2.setter
    def point2(self, val):
        self._loc[3:] = val

    @property
    def min(self) -> numpy.ndarray:
        return numpy.min(self._loc.reshape((2, 3)), 0)

    @property
    def max(self) -> numpy.ndarray:
        return numpy.max(self._loc.reshape((2, 3)), 0)

    @staticmethod
    def _create_box(box_min, box_max) -> Tuple[numpy.ndarray, numpy.ndarray]:
        box = numpy.array([box_min, box_max])
        _box_coordinates = numpy.array(
            list(
                itertools.product(
                    *box.T.tolist()
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
        box = box.ravel()
        _texture_index = numpy.array([
            0, 2, 3, 5,
            0, 2, 3, 5,
            0, 1, 3, 4,
            2, 1, 5, 4,
            0, 1, 3, 4,
            2, 1, 5, 4,
        ], numpy.uint32)
        _uv_slice = numpy.array([0, 1, 2, 1, 2, 3, 0, 3]*6, dtype=numpy.uint32).reshape((6, 8)) + numpy.arange(0, 24, 4).reshape((6, 1))

        _tri_face = numpy.array([0, 1, 2, 0, 2, 3] * 6, numpy.uint32).reshape((6, 6)) + numpy.arange(0, 24, 4).reshape((6, 1))
        return _box_coordinates[_cube_face_lut[_tri_face]].reshape((-1, 3)), box[_texture_index[_uv_slice]].reshape(-1, 2)[_tri_face, :].reshape((-1, 2))

    def create_geometry(self):
        self._setup()
        box_min = self.min
        box_max = self.max

        if self.select_state >= 0:
            self._verts[:36, :3], self._verts[:36, 3:5] = self._create_box(box_min-0.005, box_max+0.005)
        if self.select_state >= 1:
            self._verts[36:72, :3], self._verts[36:72, 3:5] = self._create_box(box_min-0.01, box_min+1.01)
            self._verts[72:, :3], self._verts[72:, 3:5] = self._create_box(box_max-1.01, box_max+0.01)

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
            vao = self._vao
            self._vao = None
            glDeleteVertexArrays(1, self._vao)

    def draw(self, transformation_matrix):
        self._setup()
        if self._vao:
            glUseProgram(self._shader)
            glUniformMatrix4fv(self._trm_mat_loc, 1, GL_FALSE, transformation_matrix)
            glBindVertexArray(self._vao)
            glDrawArrays(GL_TRIANGLES, 0, self._draw_count * (2*bool(self._select_state)+1))
