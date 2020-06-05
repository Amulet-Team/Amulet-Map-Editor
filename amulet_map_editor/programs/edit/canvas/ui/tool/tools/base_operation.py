import wx
from typing import TYPE_CHECKING, Optional

from amulet_map_editor.amulet_wx.ui.simple import SimpleChoiceAny
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
        self.Add(self._operation_choice)
        self._operation_sizer = wx.BoxSizer(wx.VERTICAL)
        self.Add(self._operation_sizer)

        # self._operation_change()

    def bind_events(self):
        pass

    @property
    def _operations(self) -> OperationStorageType:
        raise NotImplementedError

    @property
    def operation(self) -> str:
        return self._operation_choice.GetAny()

    def _on_operation_change(self, evt):
        self._operation_change()
        evt.Skip()

    def _unload_active_operation(self):
        if self._active_operation is not None:
            self._active_operation.unload()
            if isinstance(self._active_operation, wx.Window):
                self._active_operation.Destroy()
            elif isinstance(self._active_operation, wx.Sizer):
                self._operation_sizer.GetItem(self._active_operation).DeleteWindows()
            self._active_operation = None

    def _operation_change(self):
        operation_path = self._operation_choice.GetAny()
        if operation_path:
            operation = self._operations[operation_path]
            self.disable()
            self._active_operation = operation(self.canvas, self.canvas, self.canvas.world)
            self._operation_sizer.Add(self._active_operation, 1, wx.EXPAND)
            self.Layout()

    def enable(self):
        self._operation_change()

    def disable(self):
        self._unload_active_operation()
