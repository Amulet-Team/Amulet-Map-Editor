from typing import Optional, Tuple
import wx
from amulet_map_editor.api.wx.ui.simple import SimpleDialog
from amulet.api.data_types import PointCoordinates


def show_goto(
    parent: wx.Window, x: float, y: float, z: float
) -> Optional[Tuple[float, float, float]]:
    dialog = GoTo(parent, "Teleport", (x, y, z))
    if dialog.ShowModal() == wx.ID_OK:
        return dialog.location


class GoTo(SimpleDialog):
    def __init__(self, parent: wx.Window, title: str, start: PointCoordinates):
        super().__init__(parent, title, wx.HORIZONTAL)
        x, y, z = start
        x_text = wx.StaticText(self, label="x:")
        self.x = wx.SpinCtrlDouble(self, min=-30000000, max=30000000, initial=x)
        self.x.SetDigits(5)
        y_text = wx.StaticText(self, label="y:")
        self.y = wx.SpinCtrlDouble(self, min=-30000000, max=30000000, initial=y)
        self.y.SetDigits(5)
        z_text = wx.StaticText(self, label="z:")
        self.z = wx.SpinCtrlDouble(self, min=-30000000, max=30000000, initial=z)
        self.z.SetDigits(5)
        self.sizer.Add(x_text, 0, wx.CENTER | wx.ALL, 5)
        self.sizer.Add(self.x, 1, wx.CENTER | wx.ALL, 5)
        self.sizer.Add(y_text, 0, wx.CENTER | wx.ALL, 5)
        self.sizer.Add(self.y, 1, wx.CENTER | wx.ALL, 5)
        self.sizer.Add(z_text, 0, wx.CENTER | wx.ALL, 5)
        self.sizer.Add(self.z, 1, wx.CENTER | wx.ALL, 5)
        self.Fit()

    @property
    def location(self) -> PointCoordinates:
        return self.x.GetValue(), self.y.GetValue(), self.z.GetValue()

