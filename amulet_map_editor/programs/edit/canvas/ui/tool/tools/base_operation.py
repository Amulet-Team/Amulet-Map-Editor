import wx
from typing import TYPE_CHECKING, Optional

from amulet_map_editor.api.wx.ui.simple import SimpleChoiceAny
from amulet_map_editor.programs.edit.plugins import (
    OperationUIType,
    OperationStorageType,
)
from amulet_map_editor.programs.edit.canvas.ui.tool.tools.base_tool_ui import BaseToolUI

from amulet_map_editor.api.image import REFRESH_ICON

from amulet_map_editor.api.logging import log

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas import EditCanvas


class BaseSelectOperationUI(wx.BoxSizer, BaseToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        BaseToolUI.__init__(self, canvas)
        self._active_operation: Optional[OperationUIType] = None

        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self._operation_choice = SimpleChoiceAny(self.canvas)
        self._reload_operation = wx.BitmapButton(
            self.canvas, bitmap=REFRESH_ICON.bitmap(16, 16)
        )
        self._reload_operation.SetToolTip("Reload selected operation")

        horizontal_sizer.Add(self._operation_choice)
        horizontal_sizer.Add(self._reload_operation)

        self.Add(horizontal_sizer)

        self._operation_choice.SetItems(
            {key: value.name for key, value in self._operations.items()}
        )
        self._operation_choice.Bind(wx.EVT_CHOICE, self._on_operation_change)

        self._reload_operation.Bind(wx.EVT_BUTTON, self._reload_operation_loader)

        self._operation_sizer = wx.BoxSizer(wx.VERTICAL)
        self.Add(self._operation_sizer, 1, wx.EXPAND)

        # self._operation_change()

    @property
    def name(self) -> str:
        raise NotImplementedError

    def bind_events(self):
        pass

    @property
    def _operations(self) -> OperationStorageType:
        raise NotImplementedError

    @property
    def operation(self) -> str:
        return self._operation_choice.GetCurrentObject()

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
        operation_path = self._operation_choice.GetCurrentObject()
        if operation_path:
            operation = self._operations[operation_path]
            self.disable()
            self._active_operation = operation(
                self.canvas, self.canvas, self.canvas.world
            )
            self._operation_sizer.Add(
                self._active_operation, *self._active_operation.wx_add_options
            )
            self.Layout()

    def _reload_operation_loader(self, evt):
        operation_path = self._operation_choice.GetCurrentObject()
        if operation_path:
            operation_loader, success = self._operations[operation_path].reload()
            if success:
                self._operations[operation_path] = operation_loader
            else:
                log.warning(f"Couldn't successfully reload {operation_path}")
                self.reload_operations()
            self._operation_change()

    def enable(self):
        self._operation_change()
        self.canvas.draw_structure = False
        self.canvas.draw_selection = True
        self.canvas.selection_editable = False

    def disable(self):
        super().disable()
        self._unload_active_operation()

    def reload_operations(self):
        self._operation_choice.SetItems(
            {key: value.name for key, value in self._operations.items()}
        )

        if not self.operation:
            return

        items = self._operation_choice.GetItems()
        operation_loader = self._operations[self.operation]

        if operation_loader.name in items and operation_loader.name != items[0]:
            self._operation_choice.SetValue(operation_loader.name)
        else:
            log.warning(
                f"Couldn't successfully reload currently selected operation: {self.operation}"
            )
            self._operation_choice.SetValue(self._operation_choice.GetItems()[0])

        self._operation_change()
