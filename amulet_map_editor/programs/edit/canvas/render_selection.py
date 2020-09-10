from typing import TYPE_CHECKING
import wx
import weakref

from amulet_map_editor.api.opengl.mesh.selection import RenderSelectionGroupEditable
from .events import BoxChangeEvent, BoxEditToggleEvent
from amulet_map_editor.api.opengl.resource_pack import OpenGLResourcePack

if TYPE_CHECKING:
    from .edit_canvas import EditCanvas


class EditProgramRenderSelectionGroup(RenderSelectionGroupEditable):
    def __init__(
        self,
        canvas: "EditCanvas",
        context_identifier: str,
        resource_pack: OpenGLResourcePack,
    ):
        super().__init__(context_identifier, resource_pack)
        self._canvas = weakref.ref(canvas)

    @property
    def canvas(self) -> "EditCanvas":
        return self._canvas()

    def _post_box_change_event(self):
        wx.PostEvent(self.canvas, BoxChangeEvent(corners=self.active_selection_corners))

    def _post_box_enable_inputs_event(self):
        super()._post_box_enable_inputs_event()
        wx.PostEvent(self.canvas, BoxEditToggleEvent(edit=False))

    def _post_box_disable_inputs_event(self):
        super()._post_box_disable_inputs_event()
        wx.PostEvent(self.canvas, BoxEditToggleEvent(edit=True))
