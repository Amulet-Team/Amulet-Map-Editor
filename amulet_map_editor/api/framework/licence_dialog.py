import webbrowser

import wx
import wx.lib.agw.hyperlink

from amulet_map_editor import lang

_padding = 20


class LicenceDialog(wx.Dialog):
    def __init__(self, parent: wx.Window):
        super().__init__(parent, style=wx.CAPTION)
        self.SetTitle(lang.get("licence_dialog.title"))

        root_sizer = wx.BoxSizer(wx.VERTICAL)
        root_sizer.AddSpacer(_padding)

        root_sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        root_sizer.Add(root_sizer_2)

        root_sizer_2.AddSpacer(_padding)
        self._main_sizer = wx.BoxSizer(wx.VERTICAL)
        root_sizer_2.Add(self._main_sizer)
        root_sizer_2.AddSpacer(_padding)

        root_sizer.AddSpacer(_padding)

        title = wx.StaticText(
            self,
            wx.ID_ANY,
            lang.get("licence_dialog.header"),
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        font = title.GetFont()
        font.SetPointSize(25)
        title.SetFont(font)
        self._main_sizer.Add(title, 0, wx.ALL | wx.EXPAND, 5)

        self._add_line(lang.get("licence_dialog.content_1"))
        self._main_sizer.AddSpacer(20)
        self._add_line(lang.get("licence_dialog.content_2"))
        self._main_sizer.AddSpacer(20)
        self._add_line(lang.get("licence_dialog.content_3"))
        self._main_sizer.AddSpacer(20)
        self._add_line(lang.get("licence_dialog.content_4"))

        self._main_sizer.AddSpacer(10)

        button_sizer = wx.StdDialogButtonSizer()
        root_sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self._quit_button = wx.Button(
            self, wx.ID_CANCEL, lang.get("licence_dialog.quit_button")
        )
        self.SetEscapeId(self._quit_button.GetId())
        button_sizer.Add(self._quit_button)

        self._buy_button = wx.Button(
            self, wx.ID_ANY, lang.get("licence_dialog.buy_button")
        )
        self._buy_button.SetDefault()
        self._buy_button.Bind(wx.EVT_BUTTON, self._buy)
        button_sizer.Add(self._buy_button)

        self._continue_button = wx.Button(
            self, wx.ID_OK, lang.get("licence_dialog.continue_button")
        )
        button_sizer.Add(self._continue_button)
        self.SetAffirmativeId(self._continue_button.GetId())

        button_sizer.Realize()

        self.SetSizer(root_sizer)
        root_sizer.Fit(self)

        self.Layout()

    def _add_line(self, text: str) -> None:
        content = wx.StaticText(
            self,
            wx.ID_ANY,
            text,
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        font = content.GetFont()
        font.SetPointSize(12)
        content.SetFont(font)
        content.Wrap(750)
        self._main_sizer.Add(content, 0, wx.EXPAND)

    @staticmethod
    def _buy(_) -> None:
        webbrowser.open("https://www.amuletmc.com/")
