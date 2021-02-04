import numpy
from OpenGL.GL import (
    GL_TRIANGLES,
    glCullFace,
    GL_FRONT,
    GL_BACK,
    glDisable,
    GL_DEPTH_TEST,
    GL_LINE_STRIP,
    glEnable,
)
from typing import Tuple

from amulet.api.data_types import PointCoordinatesAny
from .render_selection_highlightable import RenderSelectionHighlightable
from amulet_map_editor.api.opengl.resource_pack import OpenGLResourcePack


class RenderSelectionEditable(RenderSelectionHighlightable):
    """A drawable selection box with additional editing controls"""

    def __init__(self, context_identifier: str, resource_pack: OpenGLResourcePack):
        super().__init__(context_identifier, resource_pack)
        # is the locked or is it being modified. Changes the colour of the faces.
        self._locked = True

    def _init_verts(self):
        self.verts = numpy.zeros((6 * 2 * 3 * 3, self._vert_len), dtype=numpy.float32)
        self.verts[:36, 5:9] = self.resource_pack.texture_bounds(
            self.resource_pack.get_texture_path("amulet", "amulet_ui/selection")
        )
        self.verts[36:72, 5:9] = self.resource_pack.texture_bounds(
            self.resource_pack.get_texture_path("amulet", "amulet_ui/selection_green")
        )
        self.verts[72:, 5:9] = self.resource_pack.texture_bounds(
            self.resource_pack.get_texture_path("amulet", "amulet_ui/selection_blue")
        )
        self.verts[:, 9:12] = self.box_tint

    @property
    def highlight_colour(self) -> Tuple[float, float, float]:
        if self.locked:
            return 0.5, 0.5, 1.0  # purple
        else:
            return 1.0, 0.7, 0.3  # orange

    @property
    def locked(self) -> bool:
        """Is the selection locked or not.
        If locked (True) the highlight colour will be used, if unlocked (False) the moving colour will be used."""
        return self._locked

    @locked.setter
    def locked(self, lock: bool):
        """Set if the selection locked or not.
        If locked (True) the highlight colour will be used, if unlocked (False) the moving colour will be used."""
        if not type(lock) is bool:
            raise TypeError("lock must be a bool")
        self._locked = lock

    def _create_geometry_(self):
        super()._create_geometry_()
        point1 = self.point1 - self.min + (self.min % 16) - (self.point2 <= self.point1)
        point2 = self.point2 - self.min + (self.min % 16) - (self.point2 > self.point1)
        self.verts[36:72, :3], self.verts[36:72, 3:5] = self._create_box(
            point1 - 0.01,
            point1 + 1.01,
        )
        self.verts[72:, :3], self.verts[72:, 3:5] = self._create_box(
            point2 - 0.01,
            point2 + 1.01,
        )

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

        transformation_matrix = numpy.matmul(camera_matrix, self.transformation_matrix)

        if camera_position is not None and camera_position in self:
            glCullFace(GL_FRONT)
        else:
            glCullFace(GL_BACK)

        self.draw_start = 0
        self.draw_count = 36
        super()._draw(transformation_matrix)
        glCullFace(GL_BACK)

        if self._volume > 1:
            self.draw_start = 36
            self.draw_count = 108
            super()._draw(transformation_matrix)
            self.draw_start = 0
            self.draw_count = 36

        # draw the lines around the boxes
        glDisable(GL_DEPTH_TEST)
        self._draw_mode = GL_LINE_STRIP
        for start in range(0, 36 + (self._volume > 1) * 2 * 36, 36):
            self.draw_start = start
            super()._draw(transformation_matrix)
        glEnable(GL_DEPTH_TEST)
