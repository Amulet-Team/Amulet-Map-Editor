from typing import Optional, Tuple
import wx
import re

from amulet.api.data_types import PointCoordinates

from amulet_map_editor import lang
from amulet_map_editor.api.wx.ui.simple import SimpleDialog
from amulet_map_editor.api import image

CoordRegex = re.compile(
    r"^"  # match the start
    r"\s*"  # leading whitespace
    r"(?P<x>-?[0-9]+\.?[0-9]*)"  # the x coordinate
    r"((?:,\s*)|(?:\s+))"  # separator 1
    r"(?P<y>-?[0-9]+\.?[0-9]*)"  # the y coordinate
    r"((?:,\s*)|(?:\s+))"  # separator 2
    r"(?P<z>-?[0-9]+\.?[0-9]*)"  # the z coordinate
    r",?\s*"  # trailing comma and whitespace
    r"$"  # matches the end
)


def show_goto(
    parent: wx.Window, x: float, y: float, z: float
) -> Optional[Tuple[float, float, float]]:
    dialog = GoTo(parent, lang.get("program_3d_edit.goto_ui.title"), (x, y, z))
    if dialog.ShowModal() == wx.ID_OK:
        return dialog.location


class GoTo(SimpleDialog):
    def __init__(self, parent: wx.Window, title: str, start: PointCoordinates):
        super().__init__(parent, title, wx.HORIZONTAL)
        x, y, z = start
        x_text = wx.StaticText(self, label=lang.get("program_3d_edit.goto_ui.x_label"))
        self.x = wx.SpinCtrlDouble(self, min=-30000000, max=30000000, initial=x)
        self.x.SetToolTip(lang.get("program_3d_edit.goto_ui.x_label_tooltip"))
        self.x.SetDigits(2)
        y_text = wx.StaticText(self, label=lang.get("program_3d_edit.goto_ui.y_label"))
        self.y = wx.SpinCtrlDouble(self, min=-30000000, max=30000000, initial=y)
        self.y.SetToolTip(lang.get("program_3d_edit.goto_ui.y_label_tooltip"))
        self.y.SetDigits(2)
        z_text = wx.StaticText(self, label=lang.get("program_3d_edit.goto_ui.z_label"))
        self.z = wx.SpinCtrlDouble(self, min=-30000000, max=30000000, initial=z)
        self.z.SetToolTip(lang.get("program_3d_edit.goto_ui.z_label_tooltip"))
        self.z.SetDigits(2)
        self.sizer.Add(x_text, 0, wx.CENTER | wx.ALL, 5)
        self.sizer.Add(self.x, 1, wx.CENTER | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)
        self.sizer.Add(y_text, 0, wx.CENTER | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)
        self.sizer.Add(self.y, 1, wx.CENTER | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)
        self.sizer.Add(z_text, 0, wx.CENTER | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)
        self.sizer.Add(self.z, 1, wx.CENTER | wx.TOP | wx.BOTTOM | wx.RIGHT, 5)
        self.x.Bind(wx.EVT_CHAR, self._on_text)
        self.y.Bind(wx.EVT_CHAR, self._on_text)
        self.z.Bind(wx.EVT_CHAR, self._on_text)

        copy_button = wx.BitmapButton(
            self, bitmap=image.icon.tablericons.copy.bitmap(20, 20)
        )
        copy_button.Bind(wx.EVT_BUTTON, lambda evt: self._copy())
        copy_button.SetToolTip(lang.get("program_3d_edit.goto_ui.copy_button_tooltip"))
        self.bottom_sizer.Insert(0, copy_button, 0, wx.ALL, 5)

        paste_button = wx.BitmapButton(
            self, bitmap=image.icon.tablericons.clipboard.bitmap(20, 20)
        )
        paste_button.Bind(wx.EVT_BUTTON, lambda evt: self._paste())
        paste_button.SetToolTip(
            lang.get("program_3d_edit.goto_ui.paste_button_tooltip")
        )
        self.bottom_sizer.Insert(1, paste_button, 0, wx.TOP | wx.BOTTOM | wx.RIGHT, 5)
        self.Fit()

    @property
    def location(self) -> PointCoordinates:
        return self.x.GetValue(), self.y.GetValue(), self.z.GetValue()

    def _on_text(self, evt):
        if evt.ControlDown() and evt.GetKeyCode() == 3:
            # Ctrl+C
            self._copy()
        elif evt.ControlDown() and evt.GetKeyCode() == 22:
            # Ctrl+V
            if not self._paste():
                evt.Skip()
        else:
            evt.Skip()

    def _copy(self):
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(
                wx.TextDataObject(
                    "{} {} {}".format(
                        round(self.x.GetValue(), 5),
                        round(self.y.GetValue(), 5),
                        round(self.z.GetValue(), 5),
                    )
                )
            )
            wx.TheClipboard.Close()

    def _paste(self) -> bool:
        text = ""
        text_data = wx.TextDataObject()
        if wx.TheClipboard.Open():
            success = wx.TheClipboard.GetData(text_data)
            wx.TheClipboard.Close()
            if success:
                text = text_data.GetText()
        match = CoordRegex.fullmatch(text)
        if match:
            self.x.SetValue(float(match.group("x")))
            self.y.SetValue(float(match.group("y")))
            self.z.SetValue(float(match.group("z")))
            return True
        return False
