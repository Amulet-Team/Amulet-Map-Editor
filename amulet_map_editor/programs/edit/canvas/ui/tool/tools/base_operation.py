import wx
from typing import TYPE_CHECKING, Optional

from amulet_map_editor.amulet_wx.simple import SimpleChoiceAny
from amulet_map_editor.programs.edit.plugins import OperationUIType, OperationStorageType
from amulet_map_editor.programs.edit.canvas.ui.tool.tools.base_tool_ui import BaseToolUI

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas import EditCanvas


class BaseSelectOperationUI(wx.BoxSizer, BaseToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        BaseToolUI.__init__(self, canvas)
        self._active_operation: Optional[OperationUIType] = None

        self._operation_choice = SimpleChoiceAny(self.canvas)
        self._operation_choice.SetItems({key: value.name for key, value in self._operations.items()})
        self._operation_choice.Bind(wx.EVT_CHOICE, self._on_operation_change)
        self.AddStretchSpacer(1)
        self.Add(self._operation_choice)
        self._operation_sizer = wx.BoxSizer(wx.VERTICAL)
        self.Add(self._operation_sizer)
        self.AddStretchSpacer(1)

        self._operation_change()

    @property
    def _operations(self) -> OperationStorageType:
        raise NotImplementedError

    @property
    def operation(self) -> str:
        return self._operation_choice.GetAny()

    def _on_operation_change(self, evt):
        self._operation_change()
        evt.Skip()

    def _operation_change(self):
        operation_path = self._operation_choice.GetAny()
        if operation_path:
            operation = self._operations[operation_path]
            if self._active_operation is not None:
                self._active_operation.unload()
                self._operation_sizer.GetItem(self._active_operation).DeleteWindows()
            self._active_operation = operation(self.canvas, self.canvas, self.canvas.world)
            self._operation_sizer.Add(self._active_operation, 1, wx.EXPAND)
