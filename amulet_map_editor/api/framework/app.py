import wx
from .amulet_ui import AmuletUI


class AmuletApp(wx.App):
    def __init__(self):
        super().__init__()
        self._frame = AmuletUI(None)

    def InitLocale(self):
        self.ResetLocale()
        import locale
        lang, enc = locale.getdefaultlocale()
        self._initial_locale = wx.Locale(lang, lang[:2], lang)
        try:
            locale.setlocale(locale.LC_ALL, lang)
        except locale.Error:
            locale.setlocale(locale.LC_ALL, (lang, enc))
