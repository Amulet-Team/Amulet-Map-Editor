import wx
import numpy
from typing import Optional, Callable, Type, Any, TYPE_CHECKING

from amulet.api.structure import Structure
from amulet.api.data_types import BlockCoordinates
from amulet_map_editor.amulet_wx.ui.simple import SimplePanel
from amulet_map_editor.amulet_wx.util.validators import IntValidator
from amulet_map_editor.programs.edit.canvas.ui.base_ui import BaseUI

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class SelectLocationUI(SimplePanel, BaseUI):
    """A UI element that can be dropped into the EditCanvas and let the user pick a location for a structure.
    This UI does not allow for rotation.
    Will send EVT_SELECT_CONFIRM when the user confirms the selection."""
    def __init__(
            self,
            parent: wx.Window,
            canvas: "EditCanvas",
            structure: Structure,
            confirm_callback: Callable[[], None]
    ):
        SimplePanel.__init__(self, parent)
        BaseUI.__init__(self, canvas)

        self._structure = structure
        self.canvas.structure_locations.clear()
        self.canvas.structure_locations.append(numpy.array([0, 0, 0]))
        self.canvas.structure = structure

        def _add_row(label: str, wx_object: Type[wx.Object], **kwargs) -> Any:
            sizer = wx.BoxSizer(wx.HORIZONTAL)
            self.add_object(sizer, 0, 0)
            name_text = wx.StaticText(self, label=label)
            sizer.Add(name_text, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=5)
            obj = wx_object(self, **kwargs)
            sizer.Add(obj, flag=wx.CENTER | wx.ALL, border=5)
            return obj

        self._x: wx.SpinCtrl = _add_row('x', wx.SpinCtrl, min=-30000000, max=30000000)
        self._y: wx.SpinCtrl = _add_row('y', wx.SpinCtrl, min=-30000000, max=30000000)
        self._z: wx.SpinCtrl = _add_row('z', wx.SpinCtrl, min=-30000000, max=30000000)
        for ui in (self._x, self._y, self._z):
            ui.SetValidator(IntValidator())
        self._copy_air: wx.CheckBox = _add_row('Copy Air', wx.CheckBox)
        self._x.Bind(wx.EVT_SPINCTRL, self._on_location_change)
        self._y.Bind(wx.EVT_SPINCTRL, self._on_location_change)
        self._z.Bind(wx.EVT_SPINCTRL, self._on_location_change)

        self._confirm = wx.Button(self, label="Confirm")
        self.sizer.Add(self._confirm, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5)

        self._confirm.Bind(wx.EVT_BUTTON, lambda evt: confirm_callback())

    @property
    def location(self) -> BlockCoordinates:
        return self._x.GetValue(), self._y.GetValue(), self._z.GetValue()

    @property
    def copy_air(self) -> bool:
        return self._copy_air.GetValue()

    @property
    def structure(self) -> Structure:
        return self._structure

    def _on_location_change(self, evt):
        self.canvas.structure_locations[-1] = numpy.array(self.location)
