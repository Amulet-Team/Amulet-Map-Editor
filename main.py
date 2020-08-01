import wx
import amulet_map_editor.resources
from amulet_map_editor.amulet_ui import AmuletMainWindow
from amulet_map_editor import log
import traceback

if __name__ == "__main__":
    try:
        app = wx.App()
        frame = AmuletMainWindow(None)
        app.MainLoop()
    except Exception as e:
        log.critical(
            f"Amulet Crashed. Sorry about that. Please report it to a developer if you think this is an issue. \n{traceback.format_exc()}"
        )
        input("Press ENTER to continue.")
