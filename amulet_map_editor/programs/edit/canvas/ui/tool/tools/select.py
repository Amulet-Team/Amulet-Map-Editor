from typing import TYPE_CHECKING, Type, Any
import wx

from .base_tool_ui import BaseToolUI

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class SelectOptions(wx.BoxSizer, BaseToolUI):
    def __init__(self, canvas: 'EditCanvas'):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        BaseToolUI.__init__(self, canvas)

        self.Add(wx.Panel(canvas))

        # self._x1: wx.SpinCtrl = self._add_row('x1', wx.SpinCtrl, min=-30000000, max=30000000)
        # self._y1: wx.SpinCtrl = self._add_row('y1', wx.SpinCtrl, min=-30000000, max=30000000)
        # self._z1: wx.SpinCtrl = self._add_row('z1', wx.SpinCtrl, min=-30000000, max=30000000)
        # self._x1.Bind(wx.EVT_SPINCTRL, self._green_corner_input_change)
        # self._y1.Bind(wx.EVT_SPINCTRL, self._green_corner_input_change)
        # self._z1.Bind(wx.EVT_SPINCTRL, self._green_corner_input_change)
        #
        # self._x2: wx.SpinCtrl = self._add_row('x2', wx.SpinCtrl, min=-30000000, max=30000000)
        # self._y2: wx.SpinCtrl = self._add_row('y2', wx.SpinCtrl, min=-30000000, max=30000000)
        # self._z2: wx.SpinCtrl = self._add_row('z2', wx.SpinCtrl, min=-30000000, max=30000000)
        # self._x2.Bind(wx.EVT_SPINCTRL, self._blue_corner_input_change)
        # self._y2.Bind(wx.EVT_SPINCTRL, self._blue_corner_input_change)
        # self._z2.Bind(wx.EVT_SPINCTRL, self._blue_corner_input_change)
        #
        # self._x1.Disable()
        # self._y1.Disable()
        # self._z1.Disable()
        # self._x2.Disable()
        # self._y2.Disable()
        # self._z2.Disable()
        #
        # self._x1.SetBackgroundColour((160, 215, 145))
        # self._y1.SetBackgroundColour((160, 215, 145))
        # self._z1.SetBackgroundColour((160, 215, 145))
        #
        # self._x2.SetBackgroundColour((150, 150, 215))
        # self._y2.SetBackgroundColour((150, 150, 215))
        # self._z2.SetBackgroundColour((150, 150, 215))
        #
        # self._canvas().Bind(EVT_BOX_GREEN_CORNER_CHANGE, self._green_corner_renderer_change)
        # self._canvas().Bind(EVT_BOX_BLUE_CORNER_CHANGE, self._blue_corner_renderer_change)
        # self._canvas().Bind(EVT_BOX_COORDS_ENABLE, self._enable_scrolls)

    def enable(self):
        self.canvas.select_mode = 0

    def disable(self):
        pass

    def _add_row(self, label: str, wx_object: Type[wx.Object], **kwargs) -> Any:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.Add(sizer, 0, 0)
        name_text = wx.StaticText(self, label=label)
        sizer.Add(name_text, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        obj = wx_object(self, **kwargs)
        sizer.Add(obj, flag=wx.CENTER | wx.ALL, border=5)
        return obj

    # def _green_corner_input_change(self, _):
    #     self._canvas().active_selection.point1 = [self._x1.GetValue(), self._y1.GetValue(), self._z1.GetValue()]
    #
    # def _blue_corner_input_change(self, _):
    #     self._canvas().active_selection.point2 = [self._x2.GetValue(), self._y2.GetValue(), self._z2.GetValue()]
    #
    # def _green_corner_renderer_change(self, evt):
    #     self._x1.SetValue(evt.x)
    #     self._y1.SetValue(evt.y)
    #     self._z1.SetValue(evt.z)
    #
    # def _blue_corner_renderer_change(self, evt):
    #     self._x2.SetValue(evt.x)
    #     self._y2.SetValue(evt.y)
    #     self._z2.SetValue(evt.z)
    #
    # def _enable_scrolls(self, evt):
    #     self._x1.Enable(evt.enabled)
    #     self._y1.Enable(evt.enabled)
    #     self._z1.Enable(evt.enabled)
    #     self._x2.Enable(evt.enabled)
    #     self._y2.Enable(evt.enabled)
    #     self._z2.Enable(evt.enabled)
