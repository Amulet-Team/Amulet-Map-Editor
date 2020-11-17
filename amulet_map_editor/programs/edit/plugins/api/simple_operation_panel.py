import wx
from typing import TYPE_CHECKING

from amulet.api.selection import SelectionGroup
from amulet.api.data_types import Dimension, OperationReturnType

from .operation_ui import OperationUI

if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class SimpleOperationPanel(wx.Panel, OperationUI):
    def __init__(
        self, parent: wx.Window, canvas: "EditCanvas", world: "World", options_path: str
    ):
        wx.Panel.__init__(self, parent)
        OperationUI.__init__(self, parent, canvas, world, options_path)

        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

    def _add_run_button(self, label="Run Operation"):
        self._run_button = wx.Button(self, label=label)
        self._run_button.Bind(wx.EVT_BUTTON, self._run_operation)
        self._sizer.Add(self._run_button, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)
        self.Layout()

    def _run_operation(self, _):
        self.canvas.run_operation(
            lambda: self._operation(
                self.world, self.canvas.dimension, self.canvas.selection_group
            )
        )

    def _operation(
        self, world: "World", dimension: Dimension, selection: SelectionGroup
    ) -> OperationReturnType:
        raise NotImplementedError
