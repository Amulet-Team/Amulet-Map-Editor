from typing import TYPE_CHECKING, Type, Any, Optional
import wx

from amulet.operations.paste import paste_iter

from amulet_map_editor.api.wx.util.validators import IntValidator
from amulet_map_editor.programs.edit.canvas.ui.tool.tools.base_tool_ui import BaseToolUI
from amulet_map_editor.programs.edit.canvas.ui.select_location import SelectTransformUI
from amulet_map_editor.programs.edit.canvas.events import (
    EVT_PASTE,
    EVT_BOX_CHANGE,
    EVT_BOX_DISABLE_INPUTS,
    EVT_BOX_ENABLE_INPUTS,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class SelectOptions(wx.BoxSizer, BaseToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        BaseToolUI.__init__(self, canvas)

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
        paste_button.Bind(wx.EVT_BUTTON, lambda evt: self.canvas.paste())
        self.Add(self._button_panel, 0, wx.ALIGN_CENTER_VERTICAL)

        self._paste_panel: Optional[SelectTransformUI] = None

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
        self.canvas.Bind(EVT_PASTE, self._paste)
        self._canvas().Bind(EVT_BOX_CHANGE, self._box_renderer_change)
        self._canvas().Bind(EVT_BOX_ENABLE_INPUTS, self._enable_scrolls)
        self._canvas().Bind(EVT_BOX_DISABLE_INPUTS, self._disable_scrolls)

    def _remove_paste(self):
        if self._paste_panel is not None:
            self._paste_panel.Destroy()
            self._paste_panel = None

    def _paste(self, evt):
        structure = evt.structure
        self._button_panel.Hide()
        self._remove_paste()
        self.canvas.selection_editable = False
        self._paste_panel = SelectTransformUI(
            self.canvas, self.canvas, structure, self._paste_confirm
        )
        self.Add(self._paste_panel, 0, wx.ALIGN_CENTER_VERTICAL)
        self.Layout()

    def _paste_confirm(self):
        self.canvas.run_operation(
            lambda: paste_iter(
                self.canvas.world,
                self.canvas.dimension,
                self._paste_panel.structure,
                self._paste_panel.location,
                (1, 1, 1),
                self._paste_panel.rotation,
                self._paste_panel.copy_air,
                self._paste_panel.copy_water,
                self._paste_panel.copy_lava,
            )
        )

    def enable(self):
        self._remove_paste()
        self._button_panel.Show()
        self.Layout()
        self.canvas.draw_structure = False
        self.canvas.draw_selection = True
        self.canvas.selection_editable = True

    def disable(self):
        super().disable()
        self._remove_paste()

    def _add_row(self, label: str, wx_object: Type[wx.Object], **kwargs) -> Any:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._button_panel.GetSizer().Add(sizer, 0, 0)
        name_text = wx.StaticText(self._button_panel, label=label)
        sizer.Add(name_text, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        obj = wx_object(self._button_panel, **kwargs)
        sizer.Add(obj, flag=wx.CENTER | wx.ALL, border=5)
        return obj

    def _box_input_change(self, _):
        self.canvas.active_selection_corners = (
            (self._x1.GetValue(), self._y1.GetValue(), self._z1.GetValue()),
            (self._x2.GetValue(), self._y2.GetValue(), self._z2.GetValue()),
        )

    def _box_renderer_change(self, evt):
        (x1, y1, z1), (x2, y2, z2) = evt.corners
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
