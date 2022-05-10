import wx
from amulet_map_editor import lang


class WarningDialog(wx.Dialog):
    def __init__(self, parent: wx.Window):
        super().__init__(parent, style=wx.CAPTION)
        self.SetTitle(lang.get("warning_dialog.title"))

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        content = wx.StaticText(
            self,
            wx.ID_ANY,
            lang.get("warning_dialog.content"),
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        content.Wrap(750)
        main_sizer.Add(content, 1, wx.ALL | wx.EXPAND, 5)

        button_sizer = wx.StdDialogButtonSizer()
        main_sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self._do_not_show = wx.CheckBox(
            self, wx.ID_ANY, lang.get("warning_dialog.do_not_show_again")
        )
        button_sizer.Add(self._do_not_show, 0, wx.ALIGN_CENTER_VERTICAL, 0)

        self._understand_button = wx.Button(
            self, wx.ID_ANY, lang.get("warning_dialog.i_understand")
        )
        self._understand_button.SetDefault()
        button_sizer.Add(self._understand_button, 0, 0, 0)

        button_sizer.Realize()

        self.SetSizer(main_sizer)
        main_sizer.Fit(self)

        self.SetAffirmativeId(self._understand_button.GetId())

        self.Layout()

    @property
    def do_not_show_again(self) -> bool:
        return self._do_not_show.GetValue()
