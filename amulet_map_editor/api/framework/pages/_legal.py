from dataclasses import dataclass
from typing import Optional

import wx
import wx.lib.scrolledpanel
import wx.lib.agw.hyperlink

from amulet_map_editor.api import lang


@dataclass
class Licence:
    library_name: str
    library_url: str | list[str]
    licence_name: str
    licence_text: str


class SimpleScrollablePanel(wx.lib.scrolledpanel.ScrolledPanel):
    """A scrolled panel that automatically sets itself up."""

    def __init__(self, parent: wx.Window, sizer_dir=wx.VERTICAL, **kwargs):
        super().__init__(parent, **kwargs)
        self.sizer = wx.BoxSizer(sizer_dir)
        self.SetSizer(self.sizer)
        self.SetupScrolling()
        self.SetAutoLayout(True)

    def DoGetBestClientSize(self):
        sizer = self.GetSizer()
        if sizer is None:
            return -1, -1
        else:
            sx, sy = sizer.CalcMin()
            return (
                sx + wx.SystemSettings.GetMetric(wx.SYS_VSCROLL_X),
                sy,
            )


class LicenceDialog(wx.Dialog):
    def __init__(self, parent: Optional[wx.Window] = None):
        super().__init__(parent, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        self.SetTitle(lang.get("main_menu.licence_title"))
        self.SetMinSize((300, 300))
        self.SetSize((700, 600))
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        self._scroller = SimpleScrollablePanel(self)
        self._sizer.Add(self._scroller, 1, flag=wx.EXPAND)

        for licence in Licences:
            pane = wx.CollapsiblePane(
                self._scroller,
                label=f"{licence.library_name} - {licence.licence_name}",
                style=wx.CP_DEFAULT_STYLE | wx.CP_NO_TLW_RESIZE,
            )
            pane.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self._layout)
            self._scroller.sizer.Add(pane)
            pane_widget = pane.GetPane()
            pane_sizer = wx.BoxSizer(wx.VERTICAL)
            pane_widget.SetSizer(pane_sizer)

            urls = licence.library_url
            if isinstance(urls, str):
                urls = [urls]
            for url in urls:
                hyperlink = wx.lib.agw.hyperlink.HyperLinkCtrl(
                    pane_widget, label=url, URL=""
                )
                pane_sizer.Add(
                    hyperlink, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 10
                )

            licence_text = wx.StaticText(
                pane_widget, label=licence.licence_text.strip("\r\n")
            )
            pane_sizer.Add(licence_text, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 10)

        button_sizer = self.CreateButtonSizer(wx.OK)
        self._sizer.Add(button_sizer, 0, wx.EXPAND | wx.ALL, 5)

    def _layout(self, evt) -> None:
        self.Layout()
        evt.Skip()


Licences = [
]
