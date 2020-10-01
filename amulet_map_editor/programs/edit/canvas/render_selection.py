from typing import TYPE_CHECKING, Optional, Any
import wx
import weakref

from amulet_map_editor.api.opengl.mesh.selection import RenderSelectionGroupEditable
from .events import BoxChangeEvent, BoxEditToggleEvent
from amulet_map_editor.api.opengl.resource_pack import OpenGLResourcePack
from amulet.api.history.history_manager import ObjectHistoryManager
from amulet.api.history import Changeable


if TYPE_CHECKING:
    from .edit_canvas import EditCanvas


class EditProgramRenderSelectionGroup(RenderSelectionGroupEditable, Changeable):
    def __init__(
        self,
        canvas: "EditCanvas",
        context_identifier: str,
        resource_pack: OpenGLResourcePack,
    ):
        RenderSelectionGroupEditable.__init__(self, context_identifier, resource_pack)
        Changeable.__init__(self)
        self._canvas = weakref.ref(canvas)

    @property
    def canvas(self) -> "EditCanvas":
        return self._canvas()

    def _post_box_change_event(self):
        wx.PostEvent(self.canvas, BoxChangeEvent(corners=self.active_selection_corners))

    def _post_box_enable_inputs_event(self):
        super()._post_box_enable_inputs_event()
        self.changed = True
        wx.PostEvent(self.canvas, BoxEditToggleEvent(edit=False))

    def _post_box_disable_inputs_event(self):
        super()._post_box_disable_inputs_event()
        wx.PostEvent(self.canvas, BoxEditToggleEvent(edit=True))


class RenderSelectionHistoryManager(ObjectHistoryManager):
    @property
    def value(self) -> EditProgramRenderSelectionGroup:
        return self._value

    def _unpack(self):
        self.value.set_state_no_event(*self._revision_manager.get_current_entry())

    def _pack_value(self, value: EditProgramRenderSelectionGroup) -> Optional[Any]:
        return (
            value.all_selection_corners,
            value.active_box_index
        )
