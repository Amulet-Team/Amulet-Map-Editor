from typing import Dict, Tuple, Any, TYPE_CHECKING
import wx
import weakref

from amulet_map_editor.opengl.mesh.selection import RenderSelectionGroupEditable
from .events import BoxChangeEvent, BoxEditToggleEvent

if TYPE_CHECKING:
    from .edit_canvas import EditCanvas


class EditProgramRenderSelectionGroup(RenderSelectionGroupEditable):
    def __init__(self,
                 canvas: "EditCanvas",
                 context_identifier: str,
                 texture_bounds: Dict[Any, Tuple[float, float, float, float]],
                 texture: int
                 ):
        super().__init__(context_identifier, texture_bounds, texture)
        self._canvas = weakref.ref(canvas)

    @property
    def canvas(self) -> "EditCanvas":
        return self._canvas()

    def _post_box_change_event(self):
        wx.PostEvent(self.canvas, BoxChangeEvent(corners=self.active_selection_corners))

    def _post_box_end_edit_event(self):
        wx.PostEvent(self.canvas, BoxEditToggleEvent(edit=False))

    def _post_box_start_edit_event(self):
        wx.PostEvent(self.canvas, BoxEditToggleEvent(edit=True))
