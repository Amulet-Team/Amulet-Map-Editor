import wx
from typing import TYPE_CHECKING, Optional
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)

from amulet_map_editor import log
from amulet_map_editor.api.image import REFRESH_ICON
from amulet_map_editor.api.wx.ui.simple import SimpleChoiceAny
from amulet_map_editor.api.opengl.camera import Projection

from amulet_map_editor.programs.edit.api.operations import (
    OperationUIType,
)
from amulet_map_editor.programs.edit.api.operations.manager import UIOperationManager
from .camera_tool_ui import CameraToolUI

from amulet_map_editor.programs.edit.api.behaviour import StaticSelectionBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class BaseSelectOperationUI(wx.BoxSizer, CameraToolUI):
    OperationGroupName = None

    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        CameraToolUI.__init__(self, canvas)

        self._selection = StaticSelectionBehaviour(self.canvas)

        self._active_operation: Optional[OperationUIType] = None

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
        raise NotImplementedError

    @property
    def operation(self) -> str:
        return self._operation_choice.GetCurrentObject()

    def _unload_active_operation(self):
        """Unload and destroy the UI for the active operation."""
        if self._active_operation is not None:
            self._active_operation.unload()
            if isinstance(self._active_operation, wx.Window):
                self._active_operation.Destroy()
            elif isinstance(self._active_operation, wx.Sizer):
                self._operation_sizer.GetItem(self._active_operation).DeleteWindows()
            self._active_operation = None

    def _on_operation_change(self, evt):
        """Run when the operation selection changes."""
        self._setup_operation()
        evt.Skip()

    def _setup_operation(self):
        """Create the UI for the new operation."""
        operation_path = self._operation_choice.GetCurrentObject()
        if operation_path:
            operation = self._operations[operation_path]
            self._unload_active_operation()
            self._active_operation = operation(
                self.canvas, self.canvas, self.canvas.world
            )
            self._operation_sizer.Add(
                self._active_operation, *self._active_operation.wx_add_options
            )
            self.Layout()

    def bind_events(self):
        super().bind_events()
        self._selection.bind_events()

    def enable(self):
        super().enable()
        self._selection.update_selection()
        self._setup_operation()

    def disable(self):
        super().disable()
        self._unload_active_operation()

    def _on_reload_operations(self, evt):
        """Run when the button is pressed to reload the operations."""
        self.reload_operations()

    def reload_operations(self):
        """Reload all operations and repopulate the UI."""
        # store the id of the old operation
        operation_id = self.operation

        # reload the operations
        self._operations.reload()

        # repopulate the selection
        self._operation_choice.SetItems(
            {op.identifier: op.name for op in self._operations.operations}
        )

        if operation_id:
            operation_loader = self._operations[operation_id]
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

    def _on_draw(self, evt):
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.canvas.renderer.draw_level()
        self._selection.draw()
        self.canvas.renderer.end_draw()
