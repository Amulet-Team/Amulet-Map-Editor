from __future__ import annotations
from typing import Type, Tuple

import atexit

import wx

from amulet_map_editor import CONFIG

PRE_EXISTING_CONFIG = CONFIG.get("window_preferences", {})


def write_config():
    CONFIG.put("window_preferences", PRE_EXISTING_CONFIG)


atexit.register(write_config)


class ExtendedTLW(wx.TopLevelWindow):
    __resized: bool
    __size: Tuple[int, int]
    __position: Tuple[int, int]


def on_idle(self: ExtendedTLW):
    qualified_name = ".".join((self.__module__, self.__class__.__name__))

    def wrapper(evt):
        if self.__resized:
            self.__resized = False
            PRE_EXISTING_CONFIG[qualified_name] = {
                "size": self.__size,
                "position": self.__position,
                "is_full_screen": self.IsMaximized(),
            }
        evt.Skip()

    return wrapper


def on_resize(self: ExtendedTLW):
    def wrapper(evt):
        self.__resized = True
        if not self.IsMaximized():
            # only store the non-maximised state
            self.__position = self.GetPosition().Get()
            self.__size = self.GetSize().Get()
        evt.Skip()

    return wrapper


def preserve_ui_preferences(clazz: Type[wx.TopLevelWindow]):
    assert issubclass(
        clazz, wx.TopLevelWindow
    ), "This takes a subclass of a top level window."
    original_init = clazz.__init__
    qualified_name = ".".join((clazz.__module__, clazz.__name__))

    def __init__(self: wx.TopLevelWindow, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.__resized = False
        self.__position = self.GetPosition().Get()
        self.__size = self.GetSize().Get()
        self: ExtendedTLW

        if qualified_name in PRE_EXISTING_CONFIG:
            window_config = PRE_EXISTING_CONFIG[qualified_name]
            self.SetPosition(window_config["position"])
            self.SetSize(window_config["size"])
            self.Maximize(window_config.get("is_full_screen", False))
        else:
            self.Maximize()
        self.Layout()
        self.Refresh()

        self.Bind(wx.EVT_MOVE, on_resize(self))
        self.Bind(wx.EVT_SIZE, on_resize(self))
        self.Bind(wx.EVT_IDLE, on_idle(self))

    clazz.__init__ = __init__
    return clazz
