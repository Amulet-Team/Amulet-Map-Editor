import numpy
from OpenGL.GL import *
import itertools
from typing import Tuple, Dict, Any, Optional, List

from amulet_map_editor.opengl.mesh.base.tri_mesh import TriMesh, Drawable
from amulet.api.selection import SelectionGroup, SelectionBox
from amulet.api.data_types import BlockCoordinatesAny, BlockCoordinatesNDArray, PointCoordinatesAny


class RenderSelectionGroup(Drawable):
    def __init__(self,
                 context_identifier: str,
                 texture_bounds: Dict[Any, Tuple[float, float, float, float]],
                 texture: int
                 ):
        self._context_identifier = context_identifier
        self._texture_bounds = texture_bounds
        self._texture = texture
        self._boxes: List[RenderSelection] = []
        self._active: Optional[int] = None
        self._temp_box = self._new_render_selection()


        self._last_position = numpy.array([0, 0, 0], dtype=numpy.int)
        self._hover_box: Optional[int] = None

    def _new_render_selection(self):
        return RenderSelection(self._context_identifier, self._texture_bounds, self._texture)

    def _add_render_selection(self):
        self._boxes.append(
            self._new_render_selection()
        )

    def _merge_temp_box(self):
        """
        Duplicate the temporary selection, append and activate it.
        :return:
        """
        box = self._new_render_selection()  # create a new render selection
        box.point1, box.point2 = self._temp_box.point1, self._temp_box.point2  # copy over the attributes
        self._boxes.append(box)  # add it
        self._active = len(self._boxes) - 1  # and make it active

    def deselect(self):
        while self._boxes:
            box = self._boxes.pop()
            box.unload()
        self._active = None

    def delete_active(self):
        if self._active is not None:
            box = self._boxes.pop(self._active)
            box.unload()
            if self._boxes:
                self._active -= 1
                if self._active < 0:
                    self._active = 0
            else:
                self._active = None

    def update_position(self, position: PointCoordinatesAny, box_index: Optional[int]):
        self._last_position = position
        self._hover_box = box_index
        self._temp_box.point1 = self._temp_box.point2 = position
        if self._boxes:
            self.active_selection.set_active_point(position)

    def box_click(self, add_modifier: bool = False) -> Optional[BlockCoordinatesNDArray]:
        active_selection = self.active_selection
        if active_selection is None:  # if there is no active selection
            self._merge_temp_box()
        else:  # if there is an active selection
            if active_selection.is_static:  # if it is is_static
                if self._hover_box == self._active:  # if the cursor was hovering over the current selection
                    active_selection.unlock(self._last_position)  # unlock it
                    return self._last_position
                elif self._hover_box is not None:  # if hovering over a different selected box
                    self._active = self._hover_box  #  activate that selection box
                else:  # if no hovered selection box
                    self._merge_temp_box()
                    if not add_modifier:  # if the addition modifier is not active
                        for _ in range(len(self._boxes)-1):  # remove all other boxes
                            box = self._boxes.pop(0)
                            box.unload()
                            self._active -= 1
            else:
                active_selection.lock()

    def __iter__(self):
        for box in self._boxes:
            if box.is_static:
                yield box

    def __contains__(self, position: BlockCoordinatesAny):
        return any(position in box for box in self._boxes)

    def __getitem__(self, index: int) -> "RenderSelection":
        return self._boxes[index]

    @property
    def active_selection(self) -> Optional["RenderSelection"]:
        if self._active is not None:
            return self._boxes[self._active]

    def draw(self, transformation_matrix: numpy.ndarray, active: bool, camera_position: PointCoordinatesAny):
        for index, box in enumerate(self._boxes):
            box.draw(transformation_matrix, active and index == self._active, camera_position)
        if self.active_selection is None or self.active_selection.is_static:
            self._temp_box.draw(transformation_matrix, False, camera_position=camera_position)

    def closest_intersection(self, origin: PointCoordinatesAny, vector: PointCoordinatesAny) -> Tuple[Optional[int], Optional["RenderSelection"]]:
        """
        Returns the index for the closest box in the look vector
        :param origin:
        :param vector:
        :return: Index for the closest box. None if no intersection.
        """
        multiplier = 999999999
        index_return = None
        box_return = None
        for index, box in enumerate(self._boxes):
            if box.is_static:
                mult = box.intersects_vector(origin, vector)
                if mult is not None and mult < multiplier:
                    index_return = index
                    box_return = box
        return index_return, box_return

    def create_selection_group(self) -> SelectionGroup:
        return SelectionGroup([
            SelectionBox(box.min, box.max) for box in self._boxes if box.is_static
        ])


class RenderSelection(TriMesh):
    def __init__(self,
                 context_identifier: str,
                 texture_bounds: Dict[Any, Tuple[float, float, float, float]],
                 texture: int
                 ):
        super().__init__(context_identifier, texture)
        self._free_edges = numpy.array([[False, False, False], [True, True, True]], dtype=numpy.bool)  # which edges can be moved by a call to set_active_point
        self._points: numpy.ndarray = numpy.zeros((2, 3), dtype=numpy.int)  # The points set using point1 and point2
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

    @property
    def is_static(self) -> bool:
        return not self.is_dynamic

    @property
    def is_dynamic(self) -> bool:
        return numpy.any(self._free_edges)

    @property
    def unlock_count(self) -> int:
        """
        The number of dimensions that the box is being resized in.
        :return: 0-3
        """
        return numpy.count_nonzero(self._free_edges)

    def __contains__(self, position: BlockCoordinatesAny) -> bool:
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
        return position in self and numpy.any(numpy.any(position == self._points, axis=0))

    def intersects_vector(self, origin: PointCoordinatesAny, vector: PointCoordinatesAny) -> Optional[float]:
        """
        Determine if a look vector from a given point collides with this selection box.
        :param origin: Location of the origin of the vector
        :param vector: The look vector
        :return: Multiplier of the vector to the collision location. None if it does not collide
        """
        # Logic based on https://www.scratchapixel.com/lessons/3d-basic-rendering/minimal-ray-tracer-rendering-simple-shapes/ray-box-intersection

        (tmin, tymin, tzmin), (tmax, tymax, tzmax) = numpy.sort((self._bounds - numpy.array(origin)) / numpy.array(vector), axis=0)

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

    def lock(self):
        """
        Lock all edges and make the box static
        :return:
        """
        self._free_edges[:] = False

    def unlock(self, position: BlockCoordinatesAny):
        """
        Unlock 1-3 edges based on position.
        If position is on the face that face will be unlocked.
        If the position is on an edge the two faces will be unlocked.
        If the position is on a corner the three faces will be unlocked.
        If the box has a dimension of size 1 it will only resize the first point.
        :param position:
        :return:
        """
        if self.in_boundary(position):
            self._free_edges[:] = position == self._points
            self._free_edges[1, self._free_edges[0]] = False

    def _mark_recreate(self):
        self._bounds_ = None
        self._rebuild = True

    def set_active_point(self, position: BlockCoordinatesAny):
        self._points[self._free_edges] = numpy.array([position, position])[self._free_edges]
        self._mark_recreate()

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
        self.verts[:36, :3], self.verts[:36, 3:5] = self._create_box(self.min-0.005, self.max+0.005)
        self.verts[:36, 3:5] /= 16
        self.verts[36:72, :3], self.verts[36:72, 3:5] = self._create_box(self.point1-0.01, self.point1+1.01)
        self.verts[72:, :3], self.verts[72:, 3:5] = self._create_box(self.point2-0.01, self.point2+1.01)

        self.change_verts()
        self._volume = numpy.product(self.max - self.min)
        self._rebuild = False

    def draw(self, transformation_matrix: numpy.ndarray, active=False, camera_position: PointCoordinatesAny = None):
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
        glCullFace(GL_BACK)

        glDisable(GL_DEPTH_TEST)
        self._draw_mode = GL_LINE_STRIP
        self.draw_count = 36
        for start in range(0, draw_count, 36):
            self.draw_start = start
            super()._draw(transformation_matrix)
        glEnable(GL_DEPTH_TEST)
