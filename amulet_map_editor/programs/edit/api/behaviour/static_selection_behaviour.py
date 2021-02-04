from typing import TYPE_CHECKING
from amulet_map_editor.api.opengl.mesh.selection import RenderSelectionGroup
from ..events import EVT_SELECTION_CHANGE

from .base_behaviour import BaseBehaviour
from amulet_map_editor.api.opengl.camera import Projection

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class StaticSelectionBehaviour(BaseBehaviour):
    """Adds the logic for a static selection."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
        self._selection = RenderSelectionGroup(
            self.canvas.context_identifier,
            self.canvas.renderer.opengl_resource_pack,
        )

    def bind_events(self):
        self.canvas.Bind(EVT_SELECTION_CHANGE, self._on_selection_change)

    def _on_selection_change(self, evt):
        """Update the render selection based on the updated selection."""
        self.update_selection()
        evt.Skip()

    def update_selection(self):
        """Pull the latest selection from the canvas."""
        self._selection.selection_group = self.canvas.selection.selection_group

    def draw(self):
        if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            camera = None
        else:
            camera = self.canvas.camera.location
        self._selection.draw(self.canvas.camera.transformation_matrix, camera)
