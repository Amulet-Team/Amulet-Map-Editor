# Main application entry point.
# It is split off from toplevel `main.py` so that the wrapper scripts that setuptools creates can call it
# These scripts are created automatically when the application is installed as a Pip package.

import wx
from .amulet_ui import AmuletMainWindow
from . import log
import traceback


def run():
    try:
        app = wx.App()
        frame = AmuletMainWindow(None)
        app.MainLoop()
    except Exception as e:
        log.critical(
            f"Amulet Crashed. Sorry about that. Please report it to a developer if you think this is an issue. \n{traceback.format_exc()}"
        )
        input("Press ENTER to continue.")
