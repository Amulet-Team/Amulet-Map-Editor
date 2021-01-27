from typing import TYPE_CHECKING, Type, Any
import wx

from amulet_map_editor.api.wx.util.validators import IntValidator
from amulet_map_editor.programs.edit.api.ui.tool import CameraToolUI
from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.programs.edit.api.events import (
    EVT_BOX_CHANGE,
    EVT_BOX_DISABLE_INPUTS,
    EVT_BOX_ENABLE_INPUTS,
)
from amulet_map_editor.programs.edit.api.behaviour import PointerBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class SelectOptions(wx.BoxSizer, CameraToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        CameraToolUI.__init__(self, canvas)

        self._pointer_behaviour = PointerBehaviour(self.canvas)

        self._button_panel = wx.Panel(canvas)
        button_sizer = wx.BoxSizer(wx.VERTICAL)
        self._button_panel.SetSizer(button_sizer)
        delete_button = wx.Button(self._button_panel, label="Delete")
        button_sizer.Add(delete_button, 0, wx.ALL | wx.EXPAND, 5)
        delete_button.Bind(wx.EVT_BUTTON, lambda evt: self.canvas.delete())
        copy_button = wx.Button(self._button_panel, label="Copy")
        button_sizer.Add(copy_button, 0, wx.ALL | wx.EXPAND, 5)
        copy_button.Bind(wx.EVT_BUTTON, lambda evt: self.canvas.copy())
        cut_button = wx.Button(self._button_panel, label="Cut")
        button_sizer.Add(cut_button, 0, wx.ALL | wx.EXPAND, 5)
        cut_button.Bind(wx.EVT_BUTTON, lambda evt: self.canvas.cut())
        paste_button = wx.Button(self._button_panel, label="Paste")
        button_sizer.Add(paste_button, 0, wx.ALL | wx.EXPAND, 5)
        paste_button.Bind(wx.EVT_BUTTON, lambda evt: self.canvas.paste_from_cache())
        self.Add(self._button_panel, 0, wx.ALIGN_CENTER_VERTICAL)

        self._x1: wx.SpinCtrl = self._add_row(
            "x1", wx.SpinCtrl, min=-30000000, max=30000000
        )
        self._y1: wx.SpinCtrl = self._add_row(
            "y1", wx.SpinCtrl, min=-30000000, max=30000000
        )
        self._z1: wx.SpinCtrl = self._add_row(
            "z1", wx.SpinCtrl, min=-30000000, max=30000000
        )
        self._x1.Bind(wx.EVT_SPINCTRL, self._box_input_change)
        self._y1.Bind(wx.EVT_SPINCTRL, self._box_input_change)
        self._z1.Bind(wx.EVT_SPINCTRL, self._box_input_change)
        self._x1.SetValidator(IntValidator())
        self._y1.SetValidator(IntValidator())
        self._z1.SetValidator(IntValidator())

        self._x2: wx.SpinCtrl = self._add_row(
            "x2", wx.SpinCtrl, min=-30000000, max=30000000
        )
        self._y2: wx.SpinCtrl = self._add_row(
            "y2", wx.SpinCtrl, min=-30000000, max=30000000
        )
        self._z2: wx.SpinCtrl = self._add_row(
            "z2", wx.SpinCtrl, min=-30000000, max=30000000
        )
        self._x2.Bind(wx.EVT_SPINCTRL, self._box_input_change)
        self._y2.Bind(wx.EVT_SPINCTRL, self._box_input_change)
        self._z2.Bind(wx.EVT_SPINCTRL, self._box_input_change)
        self._x2.SetValidator(IntValidator())
        self._y2.SetValidator(IntValidator())
        self._z2.SetValidator(IntValidator())

        self._x1.Disable()
        self._y1.Disable()
        self._z1.Disable()
        self._x2.Disable()
        self._y2.Disable()
        self._z2.Disable()

        self._x1.SetBackgroundColour((160, 215, 145))
        self._y1.SetBackgroundColour((160, 215, 145))
        self._z1.SetBackgroundColour((160, 215, 145))

        self._x2.SetBackgroundColour((150, 150, 215))
        self._y2.SetBackgroundColour((150, 150, 215))
        self._z2.SetBackgroundColour((150, 150, 215))

    @property
    def name(self) -> str:
        return "Select"

    def bind_events(self):
        CameraToolUI.bind_events(self)
        self.canvas.Bind(EVT_BOX_CHANGE, self._box_renderer_change)
        self.canvas.Bind(EVT_BOX_ENABLE_INPUTS, self._enable_scrolls)
        self.canvas.Bind(EVT_BOX_DISABLE_INPUTS, self._disable_scrolls)
        self._pointer_behaviour.bind_events()

    def enable(self):
        super().enable()
        self.Layout()
        # self.canvas.selection_editable = True

    def disable(self):
        super().disable()

    def _add_row(self, label: str, wx_object: Type[wx.Object], **kwargs) -> Any:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._button_panel.GetSizer().Add(sizer, 0, 0)
        name_text = wx.StaticText(self._button_panel, label=label)
        sizer.Add(name_text, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        obj = wx_object(self._button_panel, **kwargs)
        sizer.Add(obj, flag=wx.CENTER | wx.ALL, border=5)
        return obj

    def _box_input_change(self, _):
        (x1, y1, z1) = (self._x1.GetValue(), self._y1.GetValue(), self._z1.GetValue())
        (x2, y2, z2) = (self._x2.GetValue(), self._y2.GetValue(), self._z2.GetValue())
        if x2 >= x1:
            x2 += 1
        else:
            x1 += 1

        if y2 >= y1:
            y2 += 1
        else:
            y1 += 1

        if z2 >= z1:
            z2 += 1
        else:
            z1 += 1
        self.canvas.active_selection_corners = (
            (x1, y1, z1),
            (x2, y2, z2),
        )

    def _box_renderer_change(self, evt):
        (x1, y1, z1), (x2, y2, z2) = evt.corners
        if x2 > x1:
            x2 -= 1
        else:
            x1 -= 1

        if y2 > y1:
            y2 -= 1
        else:
            y1 -= 1

        if z2 > z1:
            z2 -= 1
        else:
            z1 -= 1
        self._x1.SetValue(x1)
        self._y1.SetValue(y1)
        self._z1.SetValue(z1)
        self._x2.SetValue(x2)
        self._y2.SetValue(y2)
        self._z2.SetValue(z2)
        evt.Skip()

    def _enable_scrolls(self, evt):
        self._set_scroll_state(True)
        evt.Skip()

    def _disable_scrolls(self, evt):
        self._set_scroll_state(False)

    def _set_scroll_state(self, state: bool):
        for scroll in (self._x1, self._y1, self._z1, self._x2, self._y2, self._z2):
            scroll.Enable(state)

    def _on_draw(self, evt):
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
        self.canvas.renderer.draw_level()
        self._pointer_behaviour.draw()
        # self.canvas.renderer.draw_selection()
        self.canvas.renderer.end_draw()
