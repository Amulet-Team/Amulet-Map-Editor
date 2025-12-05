import wx
import wx.lib.agw.hyperlink

from amulet_map_editor import lang


class SupportDialog(wx.Dialog):
    def __init__(self, parent: wx.Window, wait_time: int, is_first: bool):
        super().__init__(parent, style=wx.CAPTION)
        self.SetTitle(lang.get("support_dialog.title"))

        self._wait_time = wait_time

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(
            self,
            wx.ID_ANY,
            lang.get("support_dialog.title"),
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        font = title.GetFont()
        font.SetPointSize(50)
        title.SetFont(font)
        main_sizer.Add(title, 0, wx.ALL | wx.EXPAND, 5)

        content_1 = wx.StaticText(
            self,
            wx.ID_ANY,
            lang.get("support_dialog.content_1"),
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        font = content_1.GetFont()
        font.SetPointSize(12)
        content_1.SetFont(font)
        content_1.Wrap(750)
        main_sizer.Add(content_1, 0, wx.EXPAND)

        main_sizer.AddSpacer(20)

        content_2 = wx.StaticText(
            self,
            wx.ID_ANY,
            lang.get("support_dialog.content_2"),
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        font = content_2.GetFont()
        font.SetPointSize(12)
        content_2.SetFont(font)
        content_2.Wrap(750)
        main_sizer.Add(content_2, 0, wx.EXPAND)

        main_sizer.AddSpacer(20)

        github_sponsor_link = wx.lib.agw.hyperlink.HyperLinkCtrl(
            self,
            wx.ID_ANY,
            lang.get("support_dialog.github_sponsor"),
            URL="https://github.com/sponsors/Amulet-Team",
        )
        font = github_sponsor_link.GetFont()
        font.SetPointSize(12)
        github_sponsor_link.SetFont(font)
        main_sizer.Add(github_sponsor_link, 0, wx.ALIGN_CENTER)

        main_sizer.AddSpacer(10)

        paypal_sponsor_link = wx.lib.agw.hyperlink.HyperLinkCtrl(
            self,
            wx.ID_ANY,
            lang.get("support_dialog.paypal_sponsor"),
            URL="https://www.paypal.com/donate/?hosted_button_id=6G7P8K36W7TX2",
        )
        font = paypal_sponsor_link.GetFont()
        font.SetPointSize(12)
        paypal_sponsor_link.SetFont(font)
        main_sizer.Add(paypal_sponsor_link, 0, wx.ALIGN_CENTER)

        main_sizer.AddSpacer(20)

        content_3 = wx.StaticText(
            self,
            wx.ID_ANY,
            lang.get("support_dialog.content_3"),
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        font = content_3.GetFont()
        font.SetPointSize(12)
        content_3.SetFont(font)
        content_3.Wrap(750)
        main_sizer.Add(content_3, 0, wx.EXPAND)

        main_sizer.AddSpacer(10)

        button_sizer = wx.StdDialogButtonSizer()
        main_sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self._ignore_button = wx.Button(self, wx.ID_CANCEL)
        self._ignore_button.SetDefault()
        self.SetEscapeId(self._ignore_button.GetId())
        button_sizer.Add(self._ignore_button)

        self._support_button = wx.Button(
            self, wx.ID_OK, lang.get("support_dialog.support_button")
        )
        if is_first:
            self._support_button.Disable()
        button_sizer.Add(self._support_button)
        self.SetAffirmativeId(self._support_button.GetId())

        self._set_ignore_text()

        button_sizer.Realize()

        self.SetSizer(main_sizer)
        main_sizer.Fit(self)

        self._timer = wx.Timer(self)
        if 0 < self._wait_time:
            self.Bind(wx.EVT_TIMER, self._on_timer, self._timer)
            self._timer.Start(1000)

        self.Layout()

    def _set_ignore_text(self) -> None:
        if 0 < self._wait_time:
            self._ignore_button.Disable()
            self._ignore_button.SetLabel(
                lang.get("support_dialog.ignore_button_wait").format(t=self._wait_time)
            )
        else:
            self._support_button.Enable()
            self._ignore_button.Enable()
            self._ignore_button.SetLabel(lang.get("support_dialog.ignore_button"))
        self.Layout()

    def _on_timer(self, evt) -> None:
        if 0 < self._wait_time:
            self._wait_time -= 1
        if self._wait_time <= 0:
            self._timer.Stop()
        self._set_ignore_text()
