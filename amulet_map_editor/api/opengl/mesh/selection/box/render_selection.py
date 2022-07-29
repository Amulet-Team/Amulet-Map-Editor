import numpy
from OpenGL.GL import (
    GL_TRIANGLES,
    GL_DYNAMIC_DRAW,
    glCullFace,
    GL_FRONT,
    GL_BACK,
    glDisable,
    glEnable,
    GL_DEPTH_TEST,
    GL_LINE_STRIP,
    glGetBooleanv,
    glGetIntegerv,
    GL_CULL_FACE_MODE,
)
import itertools
from typing import Tuple, Optional, Union

from amulet.api.selection import SelectionBox, SelectionGroup
from amulet_map_editor.api.opengl.mesh.tri_mesh import TriMesh
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePack,
    OpenGLResourcePackManagerStatic,
)
from amulet.api.data_types import BlockCoordinatesAny, PointCoordinatesAny
from amulet_map_editor.api.opengl.matrix import displacement_matrix
from amulet_map_editor.api.opengl.data_types import RGBColour
from .colours import colours


class RenderSelection(TriMesh, OpenGLResourcePackManagerStatic):
    """A drawable selection box"""

    def __init__(self, context_identifier: str, resource_pack: OpenGLResourcePack):
        TriMesh.__init__(self, context_identifier, resource_pack)
        self._points: numpy.ndarray = numpy.zeros(
            (2, 3), dtype=numpy.int64
        )  # The points set using point1 and point2
        self._bounds: Optional[numpy.ndarray] = None  # The min and max locations
        self.transformation_matrix = numpy.eye(4, dtype=numpy.float64)
        self._needs_rebuild = True
        self._volume = 1

        self._init_verts()
        self.draw_count = 36
        self._draw_mode = GL_TRIANGLES

    @property
    def box_tint(self) -> RGBColour:
        """The tint colour to apply to the white texture."""
        return colours.get("box_normal", (1, 1, 1))

    def _init_verts(self):
        """Initialise the vertex values"""
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

    def _offset_points(self) -> numpy.ndarray:
        points = self._points.copy()
        points[0] -= self.point1 > self.point2
        points[1] -= self.point1 <= self.point2
        return points

    def _from_offset_points(self, offset_points: numpy.ndarray):
        points = offset_points.copy()
        points[0] += offset_points[0] > offset_points[1]
        points[1] += offset_points[0] <= offset_points[1]
        self._points[:] = points

    @property
    def vertex_usage(self):
        return GL_DYNAMIC_DRAW

    @property
    def draw_mode(self):
        return self._draw_mode

    def _mark_recreate(self):
        self._bounds = None
        self._needs_rebuild = True

    @property
    def points(self) -> numpy.ndarray:
        return self._points.copy()

    @points.setter
    def points(self, points: numpy.ndarray):
        if not isinstance(points, numpy.ndarray) and points.shape == (2, 3):
            raise TypeError("points must be a numpy array of size 2x3.")
        self.point1, self.point2 = points

    @property
    def point1(self) -> numpy.ndarray:
        return self.points[0]

    @point1.setter
    def point1(self, val: PointCoordinatesAny):
        if not numpy.array_equal(self._points[0], val):
            self._points[0] = numpy.floor(val)
            self._mark_recreate()

    @property
    def point2(self) -> numpy.ndarray:
        return self.points[1]

    @point2.setter
    def point2(self, val: PointCoordinatesAny):
        if not numpy.array_equal(self._points[1], val):
            self._points[1] = numpy.floor(val)
            self._mark_recreate()

    @property
    def bounds(self) -> numpy.ndarray:
        """The array storing min and max locations"""
        if self._bounds is None:
            self._bounds = numpy.sort(self._points, 0)
        return self._bounds

    @property
    def selection_box(self) -> SelectionBox:
        return SelectionBox(self.point1, self.point2)

    @selection_box.setter
    def selection_box(self, selection_box: SelectionBox):
        if not isinstance(selection_box, SelectionBox):
            raise TypeError("selection_box must be a SelectionBox.")
        self.point1 = selection_box.point_1
        self.point2 = selection_box.point_2

    @property
    def selection_group(self) -> SelectionGroup:
        return SelectionGroup(self.selection_box)

    @property
    def min(self) -> numpy.ndarray:
        return self.bounds[0]

    @property
    def max(self) -> numpy.ndarray:
        return self.bounds[1]

    def _create_box(
        self, box_min: PointCoordinatesAny, box_max: PointCoordinatesAny
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        return self._create_box_faces(
            box_min, box_max, True, True, True, True, True, True
        )

    @staticmethod
    def _create_box_faces(
        box_min: PointCoordinatesAny,
        box_max: PointCoordinatesAny,
        up: bool = False,
        down: bool = False,
        north: bool = False,
        south: bool = False,
        east: bool = False,
        west: bool = False,
    ) -> Tuple[numpy.ndarray, numpy.ndarray]:
        box = numpy.sort([box_min, box_max], 0)
        _face_count = sum([up, down, north, south, east, west])
        if not _face_count:
            raise ValueError("At least one of the faces must be enabled.")
        _box_coordinates = numpy.array(list(itertools.product(*box.T.tolist())))
        _cube_face_lut = numpy.array(
            [  # This maps to the vertices used (defined in cube_vert_lut)
                0,
                4,
                5,
                1,  # down
            ]
            * down
            + [0, 1, 3, 2] * west  # west
            + [4, 0, 2, 6] * north  # north
            + [5, 4, 6, 7] * east  # east
            + [1, 5, 7, 3] * south  # south
            + [3, 7, 6, 2] * up  # up
        )
        box = box.ravel()
        _texture_index = numpy.array(
            [0, 2, 3, 5] * down  # down
            + [2, 1, 5, 4] * west  # west
            + [3, 1, 0, 4] * north  # north
            + [5, 1, 2, 4] * east  # east
            + [0, 1, 3, 4] * south  # south
            + [0, 5, 3, 2] * up,  # up
            numpy.uint32,
        )
        _uv_slice = numpy.array(
            [0, 1, 2, 1, 2, 3, 0, 3] * _face_count, dtype=numpy.uint32
        ).reshape((_face_count, 8)) + numpy.arange(0, _face_count * 4, 4).reshape(
            (_face_count, 1)
        )

        _tri_face = numpy.array([0, 1, 2, 2, 3, 0] * _face_count, numpy.uint32).reshape(
            (_face_count, 6)
        ) + numpy.arange(0, _face_count * 4, 4).reshape((_face_count, 1))
        return (
            _box_coordinates[_cube_face_lut[_tri_face]].reshape((-1, 3)),
            box[_texture_index[_uv_slice]]
            .reshape(-1, 2)[_tri_face, :]
            .reshape((-1, 2)),
        )

    def _create_geometry_(self):
        self.verts[:36, :3], self.verts[:36, 3:5] = self._create_box(
            self.min % 16 - 0.005, self.min % 16 + self.max - self.min + 0.005
        )
        self.verts[:36, 3:5] /= 16

    def _create_geometry(self):
        self._setup()
        self._create_geometry_()

        self.transformation_matrix = displacement_matrix(*self.min - self.min % 16)

        self.change_verts()
        self._volume = numpy.product(self.max - self.min)
        self._needs_rebuild = False

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
        if self._needs_rebuild:
            self._create_geometry()
        self._draw_mode = GL_TRIANGLES

        transformation_matrix = numpy.matmul(camera_matrix, self.transformation_matrix)

        depth_state = glGetBooleanv(GL_DEPTH_TEST)
        cull_state = glGetIntegerv(GL_CULL_FACE_MODE)

        if camera_position is not None and camera_position in self:
            if cull_state == GL_BACK:
                glCullFace(GL_FRONT)
            elif cull_state == GL_FRONT:
                glCullFace(GL_BACK)

        self.draw_start = 0
        self.draw_count = 36
        super()._draw(transformation_matrix)

        # draw the lines around the boxes
        if depth_state:
            glDisable(GL_DEPTH_TEST)
        self._draw_mode = GL_LINE_STRIP
        super()._draw(transformation_matrix)
        if depth_state:
            glEnable(GL_DEPTH_TEST)

        glCullFace(cull_state)
