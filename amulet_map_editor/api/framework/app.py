import wx
from . import amulet_ui
import sys
import locale
import logging

from amulet_map_editor.api import config
from amulet_map_editor import __version__
from .warning_dialog import WarningDialog

log = logging.getLogger(__name__)

# Uses a conditional so if this breaks a build, we can just delete the file and it will skip the check
try:
    from amulet_map_editor.api.framework import update_check
except ImportError:
    update_check = None
    log.warning("Could not import update checker")


class AmuletApp(wx.App):
    _amulet_ui: amulet_ui.AmuletUI

    def OnInit(self):
        self._amulet_ui = amulet_ui.AmuletUI(None)
        self.SetTopWindow(self._amulet_ui)
        self._amulet_ui.Show()

        meta_config = config.get("amulet_meta", {})
        if not meta_config.get("do_not_show_warning_dialog", False):
            warning_dialog = WarningDialog(self._amulet_ui)
            warning_dialog.Centre()
            warning_dialog.ShowModal()
            if warning_dialog.do_not_show_again:
                meta_config["do_not_show_warning_dialog"] = True
                config.put("amulet_meta", meta_config)

        if update_check:
            self._amulet_ui.Bind(
                update_check.EVT_UPDATE_CHECK,
                lambda evt: update_check.UpdateDialog(
                    self._amulet_ui, __version__, evt.GetVersion()
                ).ShowModal(),
            )
            update_check.check_for_update(self._amulet_ui, __version__)

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
