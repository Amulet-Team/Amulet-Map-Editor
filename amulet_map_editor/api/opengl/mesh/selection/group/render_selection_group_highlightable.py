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
