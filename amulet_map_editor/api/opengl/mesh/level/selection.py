from typing import Tuple
from amulet_map_editor.api.opengl.mesh.selection import (
    RenderSelection,
    RenderSelectionGroup,
)


class GreenRenderSelection(RenderSelection):
    @property
    def box_tint(self) -> Tuple[float, float, float]:
        return 0.7, 1.0, 0.7


class GreenRenderSelectionGroup(RenderSelectionGroup):
    def _new_render_selection(self):
        return GreenRenderSelection(self._context_identifier, self.resource_pack)
