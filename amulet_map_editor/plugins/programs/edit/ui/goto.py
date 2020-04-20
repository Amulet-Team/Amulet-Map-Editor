from typing import Optional, Tuple
import wx
from amulet_map_editor.amulet_wx.simple import SimpleDialog


def show_goto(parent, x: float, y: float, z: float) -> Optional[Tuple[float, float, float]]:
    dialog = SimpleDialog(parent, 'Replace', wx.HORIZONTAL)
    panel = dialog.custom_panel
    x_text = wx.StaticText(panel, label='x:')
    x = wx.SpinCtrlDouble(panel, min=-30000000, max=30000000, initial=x)
    y_text = wx.StaticText(panel, label='y:')
    y = wx.SpinCtrlDouble(panel, min=-30000000, max=30000000, initial=y)
    z_text = wx.StaticText(panel, label='z:')
    z = wx.SpinCtrlDouble(panel, min=-30000000, max=30000000, initial=z)
    panel.add_object(x_text, 0, wx.CENTER | wx.ALL)
    panel.add_object(x, 1, wx.CENTER | wx.ALL)
    panel.add_object(y_text, 0, wx.CENTER | wx.ALL)
    panel.add_object(y, 1, wx.CENTER | wx.ALL)
    panel.add_object(z_text, 0, wx.CENTER | wx.ALL)
    panel.add_object(z, 1, wx.CENTER | wx.ALL)

    dialog.Fit()

    if dialog.ShowModal() == wx.ID_OK:
        return x.GetValue(), y.GetValue(), z.GetValue()
