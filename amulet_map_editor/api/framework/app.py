import wx
from .amulet_ui import AmuletUI
import sys
import locale


class AmuletApp(wx.App):
    def OnInit(self):
        self._frame = AmuletUI(None)
        self.SetTopWindow(self._frame)
        self._frame.Show()
        return True

    def InitLocale(self):
        # https://discuss.wxpython.org/t/what-is-wxpython-doing-to-the-locale-to-makes-pandas-crash/34606/18
        if sys.version_info[:2] >= (3, 8):
            super().InitLocale()
        else:
            self.ResetLocale()
            lang, enc = locale.getlocale()
            if lang is None:
                self._initial_locale = wx.Locale(wx.LANGUAGE_DEFAULT)
