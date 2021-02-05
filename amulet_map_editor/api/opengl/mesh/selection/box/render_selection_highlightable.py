from typing import Tuple, Union
import numpy

from .render_selection import RenderSelection
from amulet_map_editor.api.opengl.resource_pack import OpenGLResourcePack


class RenderSelectionHighlightable(RenderSelection):
    """A drawable selection box with edges that can be highlighted"""

    def __init__(self, context_identifier: str, resource_pack: OpenGLResourcePack):
        super().__init__(context_identifier, resource_pack)
        # which edges are highlighted
        self._highlight_edges = numpy.zeros((2, 3), dtype=numpy.bool)

    @property
    def highlight_colour(self) -> Tuple[float, float, float]:
        return 0.5, 0.5, 1.0

    def reset_highlight_edges(self):
        if numpy.any(self._highlight_edges):
            self.set_highlight_edges(False)

    def set_highlight_edges(self, highlight_edges: Union[numpy.ndarray, bool]):
        self._highlight_edges[:] = highlight_edges
        self._mark_recreate()

    def _create_geometry_(self):
        super()._create_geometry_()
        self.verts[:36, 9:12] = self.box_tint

        indexes = numpy.zeros(6, numpy.uint8)
        if self.point2[0] > self.point1[0]:
            indexes[[1, 3]] = 0, 3
        else:
            indexes[[1, 3]] = 3, 0

        if self.point2[1] > self.point1[1]:
            indexes[[0, 5]] = 1, 4
        else:
            indexes[[0, 5]] = 4, 1

        if self.point2[2] > self.point1[2]:
            indexes[[2, 4]] = 2, 5
        else:
            indexes[[2, 4]] = 5, 2

        # [1, 0, 2, 3, 5, 4]

        # 0 down 1
        # 1 west 0
        # 2 north 2
        # 3 east 3
        # 4 south 5
        # 5 up 4

        self.verts[:36][
            numpy.repeat(self._highlight_edges.ravel()[indexes], 6), 9:12
        ] = self.highlight_colour
