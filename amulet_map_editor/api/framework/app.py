import wx
from .amulet_ui import AmuletUI

# from amulet_map_editor import log
import locale


class AmuletApp(wx.App):
    def OnInit(self):

        # log.info(str(locale.getdefaultlocale()))
        # log.info(str(locale.getlocale()))
        # self.locale = wx.Locale(wx.LANGUAGE_DEFAULT)
        self._frame = AmuletUI(None)
        self.SetTopWindow(self._frame)
        self._frame.Show()
        return True

    def InitLocale(self):
        # https://discuss.wxpython.org/t/what-is-wxpython-doing-to-the-locale-to-makes-pandas-crash/34606/18
        self.ResetLocale()
        lang, enc = locale.getlocale()
        if lang is None:
            self._initial_locale = wx.Locale(wx.LANGUAGE_DEFAULT)

    #     import locale
    #     lang, enc = locale.getdefaultlocale()
    #     self._initial_locale = wx.Locale(lang, lang[:2], lang)
    #     try:
    #         locale.setlocale(locale.LC_ALL, lang)
    #     except locale.Error:
    #         locale.setlocale(locale.LC_ALL, (lang, enc))
