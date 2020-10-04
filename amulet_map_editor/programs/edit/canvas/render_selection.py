from typing import TYPE_CHECKING, Optional, Any
import wx
import weakref

from amulet_map_editor.api.opengl.mesh.selection import RenderSelectionGroupEditable
from .events import (
    BoxChangeEvent,
    BoxDisableInputsEvent,
    BoxEnableInputsEvent,
    BoxChangeConfirmEvent,
)
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

    def _box_change_event(self):
        wx.PostEvent(self.canvas, BoxChangeEvent(corners=self.active_selection_corners))

    def _enable_inputs_event(self):
        super()._enable_inputs_event()
        wx.PostEvent(self.canvas, BoxEnableInputsEvent())

    def _disable_inputs_event(self):
        super()._disable_inputs_event()
        wx.PostEvent(self.canvas, BoxDisableInputsEvent())

    def _confirm_change_event(self):
        self.changed = True
        wx.PostEvent(self.canvas, BoxChangeConfirmEvent())


class RenderSelectionHistoryManager(ObjectHistoryManager):
    @property
    def value(self) -> EditProgramRenderSelectionGroup:
        return self._value

    def _unpack(self):
        corners, index = self._revision_manager.get_current_entry()
        self.value.set_all_selection_corners(corners)
        self.value.active_box_index = index

    def _pack_value(self, value: EditProgramRenderSelectionGroup) -> Optional[Any]:
        return (value.all_selection_corners, value.active_box_index)
