import numpy
from OpenGL.GL import *
import itertools
from typing import Tuple, Optional, Union

from amulet_map_editor.api.opengl.mesh.base.tri_mesh import TriMesh
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePack,
    OpenGLResourcePackManagerStatic,
)
from amulet.api.data_types import BlockCoordinatesAny, PointCoordinatesAny


class RenderSelection(TriMesh, OpenGLResourcePackManagerStatic):
    """A drawable selection box"""

    def __init__(self, context_identifier: str, resource_pack: OpenGLResourcePack):
        OpenGLResourcePackManagerStatic.__init__(self, resource_pack)
        TriMesh.__init__(
            self, context_identifier, resource_pack.get_atlas_id(context_identifier)
        )
        self._points: numpy.ndarray = numpy.zeros(
            (2, 3), dtype=numpy.int
        )  # The points set using point1 and point2
        self._bounds: Optional[numpy.ndarray] = None  # The min and max locations
        self.transformation_matrix = numpy.eye(4, dtype=numpy.float64)
        self._rebuild = True
        self._volume = 1

        self._init_verts()
        self.draw_count = 36
        self._draw_mode = GL_TRIANGLES

    @property
    def box_tint(self) -> Tuple[float, float, float]:
        return 1, 1, 1

    def _init_verts(self):
        self.verts = numpy.zeros((6 * 2 * 3, self._vert_len), dtype=numpy.float32)
        self.verts[:36, 5:9] = self.resource_pack.texture_bounds(
            self.resource_pack.get_texture_path("amulet", "amulet_ui/selection")
        )
        self.verts[:, 9:12] = self.box_tint

    def __contains__(
        self, position: Union[BlockCoordinatesAny, PointCoordinatesAny]
    ) -> bool:
        """
        Is the block position inside the selection box cuboid.
        :param position: (x, y, z)
        :return: True if the position is inside the box otherwise False
        """
        point = numpy.array(position)
        return numpy.all(self.min <= point) and numpy.all(point < self.max)

    def in_boundary(self, position: BlockCoordinatesAny) -> bool:
        """
        Is the block position in the surface layer of blocks inside the selection box cuboid.
        :param position: (x, y, z)
        :return: True if the position is inside the box otherwise False
        """
        return position in self and numpy.any(
            numpy.any(position == self._points, axis=0)
        )

    def intersects_vector(
        self, origin: PointCoordinatesAny, vector: PointCoordinatesAny
    ) -> Optional[float]:
        """
        Determine if a look vector from a given point collides with this selection box.
        :param origin: Location of the origin of the vector
        :param vector: The look vector
        :return: Multiplier of the vector to the collision location. None if it does not collide
        """
        # Logic based on https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-box-intersection

        (tmin, tymin, tzmin), (tmax, tymax, tzmax) = numpy.sort(
            (self.bounds - numpy.array(origin)) / numpy.array(vector), axis=0
        )

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

    def _mark_recreate(self):
        self._bounds = None
        self._rebuild = True

    @property
    def point1(self) -> numpy.ndarray:
        return self._points[0]

    @point1.setter
    def point1(self, val):
        if not numpy.array_equal(self._points[0], val):
            self._points[0] = val
            self._mark_recreate()

    @property
    def point2(self) -> numpy.ndarray:
        return self._points[1]

    @point2.setter
    def point2(self, val):
        if not numpy.array_equal(self._points[1], val):
            self._points[1] = val
            self._mark_recreate()

    @property
    def bounds(self) -> numpy.ndarray:
        """The array storing min and max locations"""
        if self._bounds is None:
            self._bounds = numpy.sort(self._points, 0)
            self.bounds[1] += 1
        return self._bounds

    @property
    def min(self) -> numpy.ndarray:
        return self.bounds[0]

    @property
    def max(self) -> numpy.ndarray:
        return self.bounds[1]

    @staticmethod
    def _create_box(box_min, box_max) -> Tuple[numpy.ndarray, numpy.ndarray]:
        box = numpy.array([box_min, box_max])
        _box_coordinates = numpy.array(list(itertools.product(*box.T.tolist())))
        _cube_face_lut = numpy.array(
            [  # This maps to the vertices used (defined in cube_vert_lut)
                0,
                4,
                5,
                1,  # down
                0,
                1,
                3,
                2,  # west
                4,
                0,
                2,
                6,  # north
                5,
                4,
                6,
                7,  # east
                1,
                5,
                7,
                3,  # south
                3,
                7,
                6,
                2,  # up
            ]
        )
        box = box.ravel()
        _texture_index = numpy.array(
            [
                0,
                2,
                3,
                5,  # down
                2,
                1,
                5,
                4,  # west
                3,
                1,
                0,
                4,  # north
                5,
                1,
                2,
                4,  # east
                0,
                1,
                3,
                4,  # south
                0,
                5,
                3,
                2,  # up
            ],
            numpy.uint32,
        )
        _uv_slice = numpy.array(
            [0, 1, 2, 1, 2, 3, 0, 3] * 6, dtype=numpy.uint32
        ).reshape((6, 8)) + numpy.arange(0, 24, 4).reshape((6, 1))

        _tri_face = numpy.array([0, 1, 2, 2, 3, 0] * 6, numpy.uint32).reshape(
            (6, 6)
        ) + numpy.arange(0, 24, 4).reshape((6, 1))
        return (
            _box_coordinates[_cube_face_lut[_tri_face]].reshape((-1, 3)),
            box[_texture_index[_uv_slice]]
            .reshape(-1, 2)[_tri_face, :]
            .reshape((-1, 2)),
        )

    def _create_geometry_(self):
        self.verts[:36, :3], self.verts[:36, 3:5] = self._create_box(
            (-0.005, -0.005, -0.005) + (self.min % 16),
            self.max - self.min + (self.min % 16) + 0.005,
        )
        self.verts[:36, 3:5] /= 16

    def _create_geometry(self):
        self._setup()
        self._create_geometry_()

        self.transformation_matrix[3, :3] = self.min - (self.min % 16)

        self.change_verts()
        self._volume = numpy.product(self.max - self.min)
        self._rebuild = False

    def draw(
        self, camera_matrix: numpy.ndarray, camera_position: PointCoordinatesAny = None
    ):
        """
        Draw the selection box
        :param camera_matrix: 4x4 transformation matrix for the camera
        :param camera_position: The position of the camera. Used to flip draw direction if camera inside box.
        :return:
        """
        self._setup()
        if self._rebuild:
            self._create_geometry()
        self._draw_mode = GL_TRIANGLES

        transformation_matrix = numpy.matmul(self.transformation_matrix, camera_matrix)

        if camera_position is not None and camera_position in self:
            glCullFace(GL_FRONT)
        else:
            glCullFace(GL_BACK)

        self.draw_start = 0
        self.draw_count = 36
        super()._draw(transformation_matrix)
        glCullFace(GL_BACK)

        # draw the lines around the boxes
        glDisable(GL_DEPTH_TEST)
        self._draw_mode = GL_LINE_STRIP
        super()._draw(transformation_matrix)
        glEnable(GL_DEPTH_TEST)
