import numpy
from OpenGL.GL import *
from typing import Tuple, Dict, Any

from amulet.api.data_types import BlockCoordinatesAny, PointCoordinatesAny
from .render_selection import RenderSelection


class RenderSelectionEditable(RenderSelection):
    """A drawable selection box with additional editing controls"""
    def __init__(self,
                 context_identifier: str,
                 texture_bounds: Dict[Any, Tuple[float, float, float, float]],
                 texture: int
                 ):
        super().__init__(
            context_identifier,
            texture_bounds,
            texture
        )
        self._being_resized = False
        self._free_edges = numpy.array([[False, False, False], [True, True, True]], dtype=numpy.bool)  # which edges can be moved by a call to set_active_point

    def _init_verts(self, texture_bounds: Dict[Any, Tuple[float, float, float, float]]):
        missing_no = texture_bounds.get(('minecraft', 'missing_no'), (0, 0, 0, 0))
        self.verts = numpy.zeros((6 * 2 * 3 * 3, self._vert_len), dtype=numpy.float32)
        self.verts[:36, 5:9] = texture_bounds.get(('amulet', 'ui/selection'), missing_no)
        self.verts[36:72, 5:9] = texture_bounds.get(('amulet', 'ui/selection_green'), missing_no)
        self.verts[72:, 5:9] = texture_bounds.get(('amulet', 'ui/selection_blue'), missing_no)
        self.verts[:, 9:12] = 1

    @property
    def is_static(self) -> bool:
        return not self.is_dynamic

    @property
    def is_dynamic(self) -> bool:
        return numpy.any(self._free_edges)

    @property
    def being_resized(self) -> bool:
        """
        Is the selection being modified.
        :return:
        """
        return self._being_resized

    def lock(self):
        """
        Lock all edges and make the box static
        :return:
        """
        self._free_edges[:] = False
        self._being_resized = False

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
            self._being_resized = True

    def _mark_recreate(self):
        self._bounds = None
        self._rebuild = True

    def set_active_point(self, position: BlockCoordinatesAny):
        self._points[self._free_edges] = numpy.array([position, position])[self._free_edges]
        self._mark_recreate()

    def _create_geometry_(self):
        super()._create_geometry_()
        self.verts[36:72, :3], self.verts[36:72, 3:5] = self._create_box(
            self.point1 - self.min - 0.01 + (self.min % 16),
            self.point1 - self.min + 1.01 + (self.min % 16)
        )
        self.verts[72:, :3], self.verts[72:, 3:5] = self._create_box(
            self.point2 - self.min - 0.01 + (self.min % 16),
            self.point2 - self.min + 1.01 + (self.min % 16)
        )

    def draw(self, transformation_matrix: numpy.ndarray, camera_position: PointCoordinatesAny = None):
        """
        Draw the selection box
        :param transformation_matrix: 4x4 transformation matrix for the camera
        :param camera_position: The position of the camera. Used to flip draw direction if camera inside box.
        :return:
        """
        self._setup()
        if self._rebuild:
            self._create_geometry()
        self._draw_mode = GL_TRIANGLES
        self.draw_start = 0

        transformation_matrix = numpy.matmul(self.transformation_matrix, transformation_matrix)

        if camera_position is not None and camera_position in self:
            glCullFace(GL_FRONT)
        else:
            glCullFace(GL_BACK)

        draw_count = self.draw_count = 36 + (self._volume > 1) * 2 * 36
        super()._draw(transformation_matrix)
        glCullFace(GL_BACK)

        # draw the lines around the boxes
        glDisable(GL_DEPTH_TEST)
        self._draw_mode = GL_LINE_STRIP
        self.draw_count = 36
        for start in range(0, draw_count, 36):
            self.draw_start = start
            super()._draw(transformation_matrix)
        glEnable(GL_DEPTH_TEST)
