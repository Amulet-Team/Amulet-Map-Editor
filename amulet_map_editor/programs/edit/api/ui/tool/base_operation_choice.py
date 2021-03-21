import wx
from typing import TYPE_CHECKING, Optional

from amulet_map_editor import log
from amulet_map_editor.api.image import REFRESH_ICON
from amulet_map_editor.api.wx.ui.simple import SimpleChoiceAny

from amulet_map_editor.programs.edit.api.operations import (
    OperationUIType,
)
from amulet_map_editor.programs.edit.api.operations.manager import UIOperationManager
from .base_tool_ui import BaseToolUI

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class BaseOperationChoiceToolUI(wx.BoxSizer, BaseToolUI):
    OperationGroupName = None
    _active_operation: Optional[OperationUIType]

    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        BaseToolUI.__init__(self, canvas)

        self._active_operation: Optional[OperationUIType] = None
        self._last_active_operation_id: Optional[str] = None

        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self._operation_choice = SimpleChoiceAny(self.canvas)
        self._reload_operation = wx.BitmapButton(
            self.canvas, bitmap=REFRESH_ICON.bitmap(16, 16)
        )
        self._reload_operation.SetToolTip("Reload Operations")

        horizontal_sizer.Add(self._operation_choice)
        horizontal_sizer.Add(self._reload_operation)

        self.Add(horizontal_sizer)

        assert isinstance(
            self.OperationGroupName, str
        ), "OperationGroupName has not been set or is not a string."

        self._operations = UIOperationManager(self.OperationGroupName)

        self._operation_choice.SetItems(
            {op.identifier: op.name for op in self._operations.operations}
        )
        self._operation_choice.Bind(wx.EVT_CHOICE, self._on_operation_change)

        self._reload_operation.Bind(wx.EVT_BUTTON, self._on_reload_operations)

        self._operation_sizer = wx.BoxSizer(wx.VERTICAL)
        self.Add(self._operation_sizer, 1, wx.EXPAND)

    @property
    def name(self) -> str:
        """The name of the group of operations."""
        raise NotImplementedError

    @property
    def active_operation_id(self) -> str:
        """The identifier of the operation selected by the choice input.
        Note if in the process of changing this may be different to self._active_operation."""
        return self._operation_choice.GetCurrentObject()

    def _on_operation_change(self, evt):
        """Run when the operation selection changes."""
        if (
            self.active_operation_id
            and self._last_active_operation_id != self.active_operation_id
        ):
            self._setup_operation()
            self.canvas.reset_bound_events()
        evt.Skip()

    def _setup_operation(self):
        """Remove the old operation and create the UI for the new operation."""
        operation_path = self.active_operation_id
        if operation_path:
            # only reload the operation if the
            operation = self._operations[operation_path]
            if self._active_operation is not None:
                self._active_operation.disable()
                if isinstance(self._active_operation, wx.Window):
                    self._active_operation.Destroy()
                elif isinstance(self._active_operation, wx.Sizer):
                    self._operation_sizer.GetItem(
                        self._active_operation
                    ).DeleteWindows()
            self._active_operation = operation(
                self.canvas, self.canvas, self.canvas.world
            )
            self._last_active_operation_id = operation.identifier
            self._operation_sizer.Add(
                self._active_operation, *self._active_operation.wx_add_options
            )
            self._active_operation.enable()
            self.Layout()

    def bind_events(self):
        if self._active_operation is not None:
            self._active_operation.bind_events()

    def enable(self):
        if self._active_operation is None:
            self._setup_operation()
        else:
            self._active_operation.enable()

    def disable(self):
        if self._active_operation is not None:
            self._active_operation.disable()

    def _on_reload_operations(self, evt):
        """Run when the button is pressed to reload the operations."""
        self.reload_operations()

    def reload_operations(self):
        """Reload all operations and repopulate the UI."""
        # store the id of the old operation
        operation_id = self.active_operation_id

        # reload the operations
        self._operations.reload()

        # repopulate the selection
        self._operation_choice.SetItems(
            {op.identifier: op.name for op in self._operations.operations}
        )

        if operation_id:
            identifiers = self._operation_choice.values

            if identifiers:
                if operation_id in identifiers:
                    self._operation_choice.SetSelection(identifiers.index(operation_id))
                else:
                    log.info(f"Operation {operation_id} was not found.")
                    self._operation_choice.SetSelection(0)
            else:
                log.error("No operations found. Something has gone wrong.")

            self._setup_operation()
            self.canvas.reset_bound_events()
