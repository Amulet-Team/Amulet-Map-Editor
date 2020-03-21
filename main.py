import wx
from amulet_map_editor.amulet_ui import AmuletMainWindow
from amulet_map_editor import config

if __name__ == "__main__":
    app = wx.App()
    frame = AmuletMainWindow(None)
    app.MainLoop()
    config.save()
