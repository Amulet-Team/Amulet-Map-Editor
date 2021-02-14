from typing import List, Union
import numpy
from .render_selection_group import (
    RenderSelectionGroup,
)
from amulet_map_editor.api.opengl.mesh.selection import RenderSelectionHighlightable


class RenderSelectionGroupHighlightable(RenderSelectionGroup):
    """A group of selection boxes to be drawn with an added editable box."""

    def _new_render_selection(self):
        return RenderSelectionHighlightable(
            self._context_identifier, self.resource_pack
        )

    def reset_highlight_edges(self):
        self._boxes: List[RenderSelectionHighlightable]
        for box in self._boxes:
            box.reset_highlight_edges()

    def set_highlight_edges(
        self, box_index: int, highlight_edges: Union[numpy.ndarray, bool]
    ):
        self._boxes: List[RenderSelectionHighlightable]
        self._boxes[box_index].set_highlight_edges(highlight_edges)
