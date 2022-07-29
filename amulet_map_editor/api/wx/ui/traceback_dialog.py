from typing import Optional
import wx
from amulet_map_editor.api import image


class TracebackDialog(wx.Dialog):
    def __init__(
        self,
        parent: Optional[wx.Window],
        title: str,
        error: str,
        traceback: str,
        **kwargs,
    ):
        kwargs["style"] = (
            kwargs.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        )
        wx.Dialog.__init__(self, parent, **kwargs)
        self.SetTitle(title)

        self._error = error
        self._traceback = traceback

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(main_sizer)

        error_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(error_sizer, 0, wx.EXPAND | wx.ALL, 5)

        bitmap_1 = wx.StaticBitmap(
            self, bitmap=image.icon.tablericons.alert_circle.bitmap(32, 32)
        )
        error_sizer.Add(bitmap_1, 0, 0, 0)

        error_text = wx.StaticText(self, wx.ID_ANY, error)
        error_sizer.Add(error_text, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        traceback_text = wx.TextCtrl(
            self,
            wx.ID_ANY,
            traceback,
            style=wx.TE_MULTILINE | wx.TE_READONLY,
            size=(800, -1),
        )
        main_sizer.Add(traceback_text, 1, wx.EXPAND, 0)

        button_sizer = wx.StdDialogButtonSizer()
        main_sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        copy_button = wx.Button(self, wx.ID_ANY, "Copy Error")
        copy_button.Bind(wx.EVT_BUTTON, self._on_copy_error)
        button_sizer.Add(copy_button, 0, 0, 0)

        button_ok = wx.Button(self, wx.ID_OK, "")
        button_ok.SetDefault()
        button_sizer.AddButton(button_ok)

        button_sizer.Realize()

        main_sizer.Fit(self)

        self.SetAffirmativeId(button_ok.GetId())

        self.Fit()
        self.Layout()

    def _on_copy_error(self, evt):
        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(
                wx.TextDataObject(f"{self._error}\n{self._traceback}")
            )
            wx.TheClipboard.Close()


class MyApp(wx.App):
    def OnInit(self):
        import traceback as traceback_

        try:
            raise Exception("Exception message")
        except Exception as e:
            err = str(e)
            tb = traceback_.format_exc()
        self.dialog = TracebackDialog(None, "title", err, tb)
        self.SetTopWindow(self.dialog)
        self.dialog.ShowModal()
        self.dialog.Destroy()
        return True


if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
