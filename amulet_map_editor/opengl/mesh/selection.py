import numpy
from OpenGL.GL import *
import itertools
from typing import Tuple, Dict, Any, Optional
from amulet_map_editor.opengl.mesh.base.tri_mesh import TriMesh


class RenderSelection(TriMesh):
    def __init__(self,
        context_identifier: str,
        texture_bounds: Dict[Any, Tuple[float, float, float, float]]
    ):
        super().__init__(context_identifier)
        self._select_state = 0  # number of points selected
        self._points: numpy.ndarray = numpy.zeros((2, 3))  # The points set using point1 and point2
        self._bounds_: Optional[numpy.ndarray] = None  # The min and max locations
        self.verts = numpy.zeros((6*2*3*3, self._vert_len), dtype=numpy.float32)

        missing_no = texture_bounds.get(('minecraft', 'missing_no'), (0, 0, 0, 0))
        self.verts[:36, 5:9] = texture_bounds.get(('amulet', 'ui/selection'), missing_no)
        self.verts[36:72, 5:9] = texture_bounds.get(('amulet', 'ui/selection_green'), missing_no)
        self.verts[72:, 5:9] = texture_bounds.get(('amulet', 'ui/selection_blue'), missing_no)
        self.verts[:, 9:12] = 1
        self.draw_count = 36
        self._draw_mode = GL_TRIANGLES

    @property
    def vertex_usage(self):
        return GL_DYNAMIC_DRAW

    @property
    def draw_mode(self):
        return self._draw_mode

    @property
    def select_state(self) -> int:
        return self._select_state

    @select_state.setter
    def select_state(self, value: int):
        self._select_state = value
        self.draw_count = 36 * (2 * bool(self._select_state) + 1)

    @property
    def point1(self) -> numpy.ndarray:
        return self._points[0]

    @point1.setter
    def point1(self, val):
        self._points[0] = val
        self._bounds_ = None

    @property
    def point2(self) -> numpy.ndarray:
        return self._points[1]

    @point2.setter
    def point2(self, val):
        self._points[1] = val
        self._bounds_ = None

    @property
    def _bounds(self) -> numpy.ndarray:
        """The array storing min and max locations"""
        if self._bounds_ is None:
            self._bounds_ = numpy.sort(self._points, 0)
            self._bounds[1] += 1
        return self._bounds_

    @property
    def min(self) -> numpy.ndarray:
        return self._bounds[0]

    @property
    def max(self) -> numpy.ndarray:
        return self._bounds[1]

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
            0, 4, 5, 1,  # down
            0, 1, 3, 2,  # west
            4, 0, 2, 6,  # north
            5, 4, 6, 7,  # east
            1, 5, 7, 3,  # south
            3, 7, 6, 2,  # up
        ])
        box = box.ravel()
        _texture_index = numpy.array([
            0, 2, 3, 5,  # down
            2, 1, 5, 4,  # west
            3, 1, 0, 4,  # north
            5, 1, 2, 4,  # east
            0, 1, 3, 4,  # south
            0, 5, 3, 2,  # up
        ], numpy.uint32)
        _uv_slice = numpy.array([0, 1, 2, 1, 2, 3, 0, 3]*6, dtype=numpy.uint32).reshape((6, 8)) + numpy.arange(0, 24, 4).reshape((6, 1))

        _tri_face = numpy.array([0, 1, 2, 2, 3, 0] * 6, numpy.uint32).reshape((6, 6)) + numpy.arange(0, 24, 4).reshape((6, 1))
        return _box_coordinates[_cube_face_lut[_tri_face]].reshape((-1, 3)), box[_texture_index[_uv_slice]].reshape(-1, 2)[_tri_face, :].reshape((-1, 2))

    def create_geometry(self):
        if self._vao is None:
            self._setup()

        if self.select_state >= 0:
            self.verts[:36, :3], self.verts[:36, 3:5] = self._create_box(self.min-0.005, self.max+0.005)
            self.verts[:36, 3:5] /= 16
        if self.select_state >= 1:
            self.verts[36:72, :3], self.verts[36:72, 3:5] = self._create_box(self.point1-0.01, self.point1+1.01)
            self.verts[72:, :3], self.verts[72:, 3:5] = self._create_box(self.point2-0.01, self.point2+1.01)

        self.change_verts()

    def _setup(self):
        """Set up an empty VAO"""
        super()._setup()
        self.create_geometry()

    def draw(self, transformation_matrix: numpy.ndarray, draw_corners=True):
        self._draw_mode = GL_TRIANGLES
        self.draw_start = 0
        draw_count = self.draw_count
        if not draw_corners:
            self.draw_count = 36
        super().draw(transformation_matrix)

        glDisable(GL_DEPTH_TEST)
        self._draw_mode = GL_LINE_STRIP
        self.draw_count = 36
        super().draw(transformation_matrix)
        if draw_corners:
            for start in range(36, draw_count, 36):
                self.draw_start = start
                super().draw(transformation_matrix)
        self.draw_count = draw_count
        glEnable(GL_DEPTH_TEST)
