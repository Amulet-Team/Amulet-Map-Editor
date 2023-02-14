import wx
from typing import TYPE_CHECKING, Optional
import traceback
import logging

import os
import sys
import subprocess

from amulet_map_editor.api import image
from amulet_map_editor.api.wx.ui.simple import SimpleChoiceAny
from amulet_map_editor.api.wx.ui.traceback_dialog import TracebackDialog

from amulet_map_editor.programs.edit.api.operations import OperationUIType
from amulet_map_editor.programs.edit.api.operations.manager import UIOperationManager
from .base_tool_ui import BaseToolUI

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

log = logging.getLogger(__name__)


class BaseOperationChoiceToolUI(wx.BoxSizer, BaseToolUI):
    OperationGroupName = None
    _active_operation: Optional[OperationUIType]

    ShowOpenFolder = True

    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        BaseToolUI.__init__(self, canvas)

        self._active_operation: Optional[OperationUIType] = None
        self._last_active_operation_id: Optional[str] = None

        horizontal_sizer = wx.BoxSizer(wx.HORIZONTAL)

        assert isinstance(
            self.OperationGroupName, str
        ), "OperationGroupName has not been set or is not a string."
        # The operation selection
        self._operation_choice = SimpleChoiceAny(self.canvas)
        horizontal_sizer.Add(self._operation_choice)
        self._operations = UIOperationManager(self.OperationGroupName)
        self._operation_choice.SetItems(
            {op.identifier: op.name for op in self._operations.operations}
        )
        self._operation_choice.Bind(wx.EVT_CHOICE, self._on_operation_change)

        # The reload button
        self._reload_operation = wx.BitmapButton(
            self.canvas, bitmap=image.REFRESH_ICON.bitmap(16, 16)
        )
        self._reload_operation.SetToolTip("Reload Operations")
        horizontal_sizer.Add(self._reload_operation)
        self._reload_operation.Bind(wx.EVT_BUTTON, self._on_reload_operations)

        # The open folder button
        if self.ShowOpenFolder:
            self._open_folder = wx.BitmapButton(
                self.canvas, bitmap=image.TABLERICONS.folder.bitmap(16, 16)
            )
            self._open_folder.SetToolTip("Open Plugin Folder")
            horizontal_sizer.Add(self._open_folder)
            self._open_folder.Bind(wx.EVT_BUTTON, self._on_open_folder)

        self.Add(horizontal_sizer)

        self._operation_sizer = wx.BoxSizer(wx.VERTICAL)
        self.Add(self._operation_sizer, 1, wx.EXPAND)

    @property
    def name(self) -> str:
        """The name of the group of operations."""
        raise NotImplementedError

    @property
    def active_operation_id(self) -> str:
        """The identifier of the operation selected by the choice input.
        Note if in the process of changing this may be different to self._active_operation.
        """
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
            self._operation_sizer.Clear(delete_windows=True)
            try:
                self._active_operation = operation(
                    self.canvas, self.canvas, self.canvas.world
                )
                self._operation_sizer.Add(
                    self._active_operation, *self._active_operation.wx_add_options
                )
                self._active_operation.enable()
            except Exception as e:
                # If something went wrong clear the created UI
                self._active_operation = None
                self._operation_sizer.Clear(delete_windows=True)
                for window in self.canvas.GetChildren():
                    window: wx.Window
                    # remove orphaned windows.
                    # If the Sizer.Add method was not run it will not be in self._operation_sizer
                    if window.GetContainingSizer() is None:
                        window.Destroy()
                log.error("Error loading Operation UI.", exc_info=True)
                dialog = TracebackDialog(
                    self.canvas,
                    "Error loading Operation UI.",
                    str(e),
                    traceback.format_exc(),
                )
                dialog.ShowModal()
                dialog.Destroy()
            finally:
                self._last_active_operation_id = operation.identifier
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

    def _on_open_folder(self, evt):
        path = self._operations.public_path
        if not os.path.exists(path):
            os.makedirs(path)
        if sys.platform == "win32":
            os.startfile(path)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, path])
