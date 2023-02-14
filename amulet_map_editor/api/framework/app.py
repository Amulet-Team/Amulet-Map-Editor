import wx
from . import amulet_ui
import sys
import locale


class AmuletApp(wx.App):
    _amulet_ui: amulet_ui.AmuletUI

    def OnInit(self):
        self._amulet_ui = amulet_ui.AmuletUI(None)
        self.SetTopWindow(self._amulet_ui)
        self._amulet_ui.Show()
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

    def open_level(self, path: str):
        """
        Open a level and create a tab for it.
        If a tab already exists it will just be shown.

        :param path: The path to the level to open.
        """
        self._amulet_ui.open_level(path)

    def close_level(self, path: str):
        """
        Close a level tab.

        :param path: The path to the level to close.
        """
        self._amulet_ui.close_level(path)


def get_app() -> AmuletApp:
    """Get the app instance."""
    app = wx.App.Get()
    if isinstance(app, AmuletApp):
        return app
    else:
        raise Exception("wx App is not an instance of AmuletApp")


def open_level(path: str):
    """
    Open a level and create a tab for it.
    If a tab already exists it will just be shown.

    :param path: The path to the level to open.
    """
    get_app().open_level(path)


def close_level(path: str):
    """
    Close a level tab.

    :param path: The path to the level to close.
    """
    get_app().close_level(path)
