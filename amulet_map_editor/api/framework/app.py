import wx
from . import amulet_ui
import sys
import locale
import logging
import time
import os

from amulet_map_editor.api import config
from amulet_map_editor import __version__
from .warning_dialog import WarningDialog
from .licence_dialog import LicenceDialog

# Disable OpenGL_accelerate logging
logging.getLogger("OpenGL.acceleratesupport").setLevel(logging.CRITICAL)
logging.getLogger("OpenGL.GL.shaders").setLevel(logging.INFO)
logging.getLogger("PIL.PngImagePlugin").setLevel(logging.INFO)

log = logging.getLogger(__name__)

# Uses a conditional so if this breaks a build, we can just delete the file and it will skip the check
try:
    from amulet_map_editor.api.framework import update_check
except ImportError:
    update_check = None
    log.warning("Could not import update checker")


def centre_on_main_screen(window: wx.TopLevelWindow) -> None:
    # The normal CentreOnParent method makes the window no larger than its parent which is often undesired.
    # CentreOnScreen for some reason in select cases displays the window on the wrong screen.
    window.CentreOnScreen()

    if wx.Display.GetCount() and not wx.Display(0).GetGeometry().Intersects(
        window.GetRect()
    ):
        # If the window does not intersect the main screen, manually position the window.
        log.debug(f"Window {window} was incorrectly displayed.")
        screen_rect = wx.Display(0).GetGeometry()
        window_size = window.GetSize()

        x = screen_rect.x + max(20, (screen_rect.width - window_size.GetWidth()) // 2)
        y = screen_rect.y + max(20, (screen_rect.height - window_size.GetHeight()) // 2)
        window.Move(wx.Point(x, y))


class AmuletApp(wx.App):
    _amulet_ui: amulet_ui.AmuletUI

    def OnInit(self):
        for i in range(wx.Display.GetCount()):
            display = wx.Display(i)
            log.debug(f"Display {i} {display.GetGeometry()}")

        self._amulet_ui = amulet_ui.AmuletUI(None)
        self.SetTopWindow(self._amulet_ui)
        self._amulet_ui.Maximize()
        self._amulet_ui.Show()
        log.debug(
            f"Shown AmuletUI at {self._amulet_ui.GetRect()} maximised={self._amulet_ui.IsMaximized()}"
        )

        meta_config = config.get("amulet_meta", {})

        if not (getattr(sys, "frozen", False) or os.path.exists("/.flatpak-info")):
            licence_dialog_show_time = meta_config.get("licence_dialog_show_time", 0)
            if licence_dialog_show_time < time.time() - 3600 * 24 * 30:
                # Last shown more than a month ago
                licence_dialog = LicenceDialog(self._amulet_ui)
                centre_on_main_screen(licence_dialog)
                log.debug(f"Showing licence dialog at {licence_dialog.GetRect()}")
                if licence_dialog.ShowModal() == wx.ID_OK:
                    meta_config["licence_dialog_show_time"] = time.time()
                    config.put("amulet_meta", meta_config)
                else:
                    return False

        if not meta_config.get("do_not_show_warning_dialog", False):
            warning_dialog = WarningDialog(self._amulet_ui)
            centre_on_main_screen(warning_dialog)
            log.debug(f"Showing warning dialog at {warning_dialog.GetRect()}")
            warning_dialog.ShowModal()
            if warning_dialog.do_not_show_again:
                meta_config["do_not_show_warning_dialog"] = True
                config.put("amulet_meta", meta_config)

        if update_check:

            def _show_update_dialog(evt) -> None:
                update_dialog = update_check.UpdateDialog(
                    self._amulet_ui, __version__, evt.GetVersion()
                )
                centre_on_main_screen(update_dialog)
                log.debug(f"Showing update dialog at {update_dialog.GetRect()}")
                update_dialog.ShowModal()

            self._amulet_ui.Bind(
                update_check.EVT_UPDATE_CHECK,
                _show_update_dialog,
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
