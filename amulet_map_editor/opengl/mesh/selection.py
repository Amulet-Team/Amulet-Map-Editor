import numpy
from OpenGL.GL import *
import itertools
from amulet_map_editor.opengl.mesh.base.tri_mesh import TriMesh
from typing import Tuple, Dict, Any, Optional, List
from amulet.api.data_types import BlockCoordinatesAny, PointCoordinatesAny, PointCoordinatesNDArray


class RenderSelection(TriMesh):
    def __init__(self,
                 context_identifier: str,
                 texture_bounds: Dict[Any, Tuple[float, float, float, float]],
                 texture: int
                 ):
        super().__init__(context_identifier, texture)
        self._select_state = 0  # number of points selected
        self._points: numpy.ndarray = numpy.zeros((2, 3))  # The points set using point1 and point2
        self._bounds_: Optional[numpy.ndarray] = None  # The min and max locations
        self.verts = numpy.zeros((6*2*3*3, self._vert_len), dtype=numpy.float32)
        self._rebuild = True
        self._volume = 1

        missing_no = texture_bounds.get(('minecraft', 'missing_no'), (0, 0, 0, 0))
        self.verts[:36, 5:9] = texture_bounds.get(('amulet', 'ui/selection'), missing_no)
        self.verts[36:72, 5:9] = texture_bounds.get(('amulet', 'ui/selection_green'), missing_no)
        self.verts[72:, 5:9] = texture_bounds.get(('amulet', 'ui/selection_blue'), missing_no)
        self.verts[:, 9:12] = 1
        self.draw_count = 36
        self._draw_mode = GL_TRIANGLES

    def __contains__(self, position: BlockCoordinatesAny):
        point = numpy.array(position)
        m = self.min
        return numpy.all(self.min <= point) and numpy.all(point < self.max)

    def intersects_vector(self, origin: PointCoordinatesNDArray, vector: PointCoordinatesNDArray) -> Optional[float]:
        """
        Determine if a look vector from a given point collides with this selection box.
        :param origin: Location of the origin of the vector
        :param vector: The look vector
        :return: Multiplier of the vector to the collision location. None if it does not collide
        """
        # Logic based on https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-box-intersection
        (tmin, tymin, tzmin), (tmax, tymax, tzmax) = numpy.sort((self._bounds - origin) / vector, axis=0)

        if tmin > tymax or tymin > tmax:
            return None

        if tymin > tmin:
            tmin = tymin

        if tymax < tmax:
            tmax = tymax

        if tmin > tzmax or tzmin > tmax:
            return None

        if tzmin > tmin:
            tmin = tzmin

        if tzmax < tmax:
            tmax = tzmax

        return tmin if tmin >= 0 else tmax

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

    @property
    def point1(self) -> numpy.ndarray:
        return self._points[0]

    @point1.setter
    def point1(self, val):
        if not numpy.array_equal(self._points[0], val):
            self._points[0] = val
            self._bounds_ = None
            self._rebuild = True

    @property
    def point2(self) -> numpy.ndarray:
        return self._points[1]

    @point2.setter
    def point2(self, val):
        if not numpy.array_equal(self._points[1], val):
            self._points[1] = val
            self._bounds_ = None
            self._rebuild = True

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
        _cube_face_lut = numpy.array([  # This maps to the vertices used (defined in cube_vert_lut)
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

    def _create_geometry(self):
        self._setup()
        if self.select_state >= 0:
            self.verts[:36, :3], self.verts[:36, 3:5] = self._create_box(self.min-0.005, self.max+0.005)
            self.verts[:36, 3:5] /= 16
        if self.select_state >= 1:
            self.verts[36:72, :3], self.verts[36:72, 3:5] = self._create_box(self.point1-0.01, self.point1+1.01)
            self.verts[72:, :3], self.verts[72:, 3:5] = self._create_box(self.point2-0.01, self.point2+1.01)

        self.change_verts()
        self._volume = numpy.product(self.max - self.min)
        self._rebuild = False

    def draw(self, transformation_matrix: numpy.ndarray, active=True, camera_position: PointCoordinatesAny = None):
        """
        Draw the selection box
        :param transformation_matrix: 4x4 transformation matrix for the camera
        :param active: If the selection box is the active selection (draw corner boxes)
        :param camera_position: The position of the camera. Used to flip draw direction if camera inside box.
        :return:
        """
        self._setup()
        if self._rebuild:
            self._create_geometry()
        self._draw_mode = GL_TRIANGLES
        self.draw_start = 0

        if camera_position is not None and camera_position in self:
            glCullFace(GL_FRONT)
        else:
            glCullFace(GL_BACK)

        if active and self._volume > 1:
            draw_count = self.draw_count = 108
        else:
            draw_count = self.draw_count = 36
        super()._draw(transformation_matrix)

        glDisable(GL_DEPTH_TEST)
        self._draw_mode = GL_LINE_STRIP
        self.draw_count = 36
        for start in range(0, draw_count, 36):
            self.draw_start = start
            super()._draw(transformation_matrix)
        glEnable(GL_DEPTH_TEST)
        glCullFace(GL_BACK)
