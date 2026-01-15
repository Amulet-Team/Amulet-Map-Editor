import wx
from typing import TYPE_CHECKING

from amulet.api.selection import SelectionGroup
from amulet.api.data_types import Dimension, OperationReturnType

from amulet_map_editor.programs.edit.api.operations import DefaultOperationUI

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class SimpleOperationPanel(wx.Panel, DefaultOperationUI):
    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        wx.Panel.__init__(self, parent)
        DefaultOperationUI.__init__(self, parent, canvas, world, options_path)

        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

    def _add_run_button(self, label="Run Operation"):
        self._run_button = wx.Button(self, label=label)
        self._run_button.Bind(wx.EVT_BUTTON, self._run_operation)
        self._sizer.Add(
            self._run_button, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 5
        )
        self.Layout()

    def _run_operation(self, _):
        if not self._pre_operation():
            return
        self.canvas.run_operation(
            lambda: self._operation(
                self.world, self.canvas.dimension, self.canvas.selection.selection_group
            )
        )

    def _pre_operation(self) -> bool:
        """
        Run code before running the operation.
        This code is not included in the operation time.
        This can be used to get extra options e.g. a save location.
        Return True to continue with the operation.
        """
        return True

    def _operation(
        self, world: "BaseLevel", dimension: Dimension, selection: SelectionGroup
    ) -> OperationReturnType:
        raise NotImplementedError
