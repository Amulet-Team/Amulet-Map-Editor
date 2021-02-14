from __future__ import annotations

import atexit

import wx

from amulet_map_editor import CONFIG

PRE_EXISTING_CONFIG = CONFIG.get("window_preferences", {})


def write_config():
    CONFIG.put("window_preferences", PRE_EXISTING_CONFIG)


atexit.register(write_config)


def on_idle(self):
    global PRE_EXISTING_CONFIG

    qualified_name = ".".join((self.__module__, self.__class__.__name__))

    def wrapper(evt):
        update_cfg = False
        if self.__resized:
            self.__resized = False
            update_cfg = True
        if self.__moved:
            self.__moved = False
            update_cfg = True
        if update_cfg:
            PRE_EXISTING_CONFIG[qualified_name] = {
                "size": self.GetSize().Get(),
                "position": self.GetPosition().Get(),
            }
            self.Refresh()
            self.Layout()
        evt.Skip()

    return wrapper


def on_size(self):
    def wrapper(evt):
        self.__resized = True
        evt.Skip()

    return wrapper


def on_move(self):
    def wrapper(evt):
        self.__moved = True
        evt.Skip()

    return wrapper


def preserve_ui_preferences(clazz):
    original_init = clazz.__init__
    qualified_name = ".".join((clazz.__module__, clazz.__name__))

    def __init__(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.__resized = False
        self.__moved = False

        if qualified_name in PRE_EXISTING_CONFIG:
            self.SetSize(PRE_EXISTING_CONFIG[qualified_name]["size"])
            self.SetPosition(PRE_EXISTING_CONFIG[qualified_name]["position"])
            self.Refresh()

        self.Bind(wx.EVT_MOVE, on_move(self))
        self.Bind(wx.EVT_SIZE, on_size(self))
        self.Bind(wx.EVT_IDLE, on_idle(self))

    clazz.__init__ = __init__
    return clazz
