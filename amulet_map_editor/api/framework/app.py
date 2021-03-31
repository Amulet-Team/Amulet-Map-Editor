import wx
from .amulet_ui import AmuletUI
from amulet_map_editor import log


class AmuletApp(wx.App):
    def __init__(self):
        super().__init__()
        self._frame = AmuletUI(None)
        self.locale = wx.Locale(wx.LANGUAGE_DEFAULT)

    # def InitLocale(self):
    #     # https://discuss.wxpython.org/t/what-is-wxpython-doing-to-the-locale-to-makes-pandas-crash/34606/18
    #     self.ResetLocale()
    #     import locale
    #     lang, enc = locale.getdefaultlocale()
    #     self._initial_locale = wx.Locale(lang, lang[:2], lang)
    #     try:
    #         locale.setlocale(locale.LC_ALL, lang)
    #     except locale.Error:
    #         locale.setlocale(locale.LC_ALL, (lang, enc))
