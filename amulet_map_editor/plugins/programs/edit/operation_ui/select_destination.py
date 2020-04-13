import wx
import numpy
from typing import Optional, List, Callable, Type, Any

from amulet.api.structure import Structure
from amulet_map_editor.amulet_wx.simple import SimplePanel


class SelectDestinationUI(SimplePanel):
    def __init__(self, parent, cancel_callback, confirm_callback):
        super().__init__(parent)
        self._cancel_callback = cancel_callback
        self._confirm_callback = confirm_callback
        self._locations = None

        self._operation_path: Optional[str] = None
        self._operation: Optional[Callable] = None
        self._operation_input_definitions: Optional[List[str]] = None
        self._structure: Optional[Structure] = None
        self._options: Optional[dict] = None

        self._x: wx.SpinCtrl = self._add_row('x', wx.SpinCtrl, min=-30000000, max=30000000)
        self._y: wx.SpinCtrl = self._add_row('y', wx.SpinCtrl, min=-30000000, max=30000000)
        self._z: wx.SpinCtrl = self._add_row('z', wx.SpinCtrl, min=-30000000, max=30000000)
        self._copy_air: wx.CheckBox = self._add_row('Copy Air', wx.CheckBox)
        self._x.Bind(wx.EVT_SPINCTRL, self._on_location_change)
        self._y.Bind(wx.EVT_SPINCTRL, self._on_location_change)
        self._z.Bind(wx.EVT_SPINCTRL, self._on_location_change)

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.add_object(sizer, 0, 0)
        self._cancel = wx.Button(self, label="Cancel")
        sizer.Add(self._cancel, flag=wx.CENTER, border=5)
        self._confirm = wx.Button(self, label="Confirm")
        sizer.Add(self._confirm, flag=wx.CENTER, border=5)

        self._cancel.Bind(wx.EVT_BUTTON, self._on_cancel)
        self._confirm.Bind(wx.EVT_BUTTON, self._on_confirm)

    def bind_locations(self, locations: List[numpy.ndarray]):
        self._locations = locations

    def setup(self, operation_path: Any, operation: Callable, operation_input_definitions: List[str], structure: Structure, options: dict):
        self._operation_path = operation_path
        self._operation = operation
        self._operation_input_definitions = operation_input_definitions
        self._structure = structure
        self._locations.clear()
        self._locations.append(structure.selection.min)
        self._x.SetValue(structure.selection.min[0])
        self._y.SetValue(structure.selection.min[1])
        self._z.SetValue(structure.selection.min[2])
        self._copy_air.SetValue(options.get('copy_air', False))
        self._options = options

    def _add_row(self, label: str, wx_object: Type[wx.Object], **kwargs) -> Any:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.add_object(sizer, 0, 0)
        name_text = wx.StaticText(self, label=label)
        sizer.Add(name_text, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        obj = wx_object(self, **kwargs)
        sizer.Add(obj, flag=wx.CENTER | wx.ALL, border=5)
        return obj

    def _on_location_change(self, evt):
        self._locations[-1] = numpy.array([self._x.GetValue(), self._y.GetValue(), self._z.GetValue()])

    def _on_cancel(self, evt):
        self._cancel_callback()

    def _on_confirm(self, evt):
        self._options['location'] = (self._x.GetValue(), self._y.GetValue(), self._z.GetValue())
        self._options['copy_air'] = self._copy_air.GetValue()
        self._confirm_callback(
            self._operation_path,
            self._operation,
            self._operation_input_definitions,
            options=self._options,
            structure=self._structure
        )
