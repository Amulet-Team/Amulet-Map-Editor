import wx
import weakref
from typing import Optional, Any, Callable

from .select_destination import SelectDestinationUI
from .select_operation import SelectOperationUI


class OperationUI(wx.Panel):
    def __init__(self, parent, world, run_operation, run_main_operation):
        wx.Panel.__init__(self, parent)

        self._world = weakref.ref(world)
        self._canvas = None
        self._run_main_operation = run_main_operation

        middle_sizer = wx.BoxSizer(wx.VERTICAL)

        self._operation_ui: Optional[SelectOperationUI] = SelectOperationUI(self, world, run_operation)
        middle_sizer.Add(self._operation_ui)
        # self._operation_ui.Bind(wx.EVT_ENTER_WINDOW, self._steal_focus_operation)
        self._operation_ui.Layout()
        self._operation_ui.Fit()
        self._select_destination_ui: Optional[SelectDestinationUI] = SelectDestinationUI(
            self,
            self._destination_select_cancel,
            self._destination_select_confirm
        )
        middle_sizer.Add(self._select_destination_ui)
        # self._select_destination_ui.Bind(wx.EVT_ENTER_WINDOW, self._steal_focus_destination)
        self._select_destination_ui.Layout()
        self._select_destination_ui.Fit()
        self._select_destination_ui.Hide()

        self.SetSizer(middle_sizer)
        middle_sizer.Fit(self)
        self.Layout()

    def set_canvas(self, canvas):
        self._canvas = weakref.ref(canvas)
        self._select_destination_ui.bind_locations(canvas.structure_locations)

    def enable_select_destination_ui(self, operation_path: Any, operation: Callable, operation_input_definitions: List[str], structure: Structure, options: dict):
        self._select_destination_ui.setup(operation_path, operation, operation_input_definitions, structure, options)
        self._hide_all()
        self._select_destination_ui.Show()
        self.Fit()
        self._canvas().structure = structure
        self._canvas().select_mode = 1

    def _destination_select_cancel(self):
        self.enable_operation_ui()

    def _destination_select_confirm(self, *args, **kwargs):
        self._select_destination_ui.Disable()
        self._run_main_operation(*args, **kwargs)
        self._select_destination_ui.Enable()
        self.enable_operation_ui()

    def enable_operation_ui(self):
        self._hide_all()
        self._operation_ui.Show()
        self._canvas().select_mode = 0
        self.Fit()

    def hide(self):
        self.Hide()

    def _hide_all(self):
        self._operation_ui.Hide()
        self._select_destination_ui.Hide()

    @property
    def operation(self):
        return self._operation_ui.operation
