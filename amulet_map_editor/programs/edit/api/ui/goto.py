from typing import Optional, Tuple
import wx
from amulet_map_editor.api.wx.ui.simple import SimpleDialog


def show_goto(
    parent, x: float, y: float, z: float
) -> Optional[Tuple[float, float, float]]:
    dialog = SimpleDialog(parent, "Teleport", wx.HORIZONTAL)
    x_text = wx.StaticText(dialog, label="x:")
    x = wx.SpinCtrlDouble(dialog, min=-30000000, max=30000000, initial=x)
    y_text = wx.StaticText(dialog, label="y:")
    y = wx.SpinCtrlDouble(dialog, min=-30000000, max=30000000, initial=y)
    z_text = wx.StaticText(dialog, label="z:")
    z = wx.SpinCtrlDouble(dialog, min=-30000000, max=30000000, initial=z)
    dialog.sizer.Add(x_text, 0, wx.CENTER | wx.ALL)
    dialog.sizer.Add(x, 1, wx.CENTER | wx.ALL)
    dialog.sizer.Add(y_text, 0, wx.CENTER | wx.ALL)
    dialog.sizer.Add(y, 1, wx.CENTER | wx.ALL)
    dialog.sizer.Add(z_text, 0, wx.CENTER | wx.ALL)
    dialog.sizer.Add(z, 1, wx.CENTER | wx.ALL)

    dialog.Fit()

    if dialog.ShowModal() == wx.ID_OK:
        return x.GetValue(), y.GetValue(), z.GetValue()
