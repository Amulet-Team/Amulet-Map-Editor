from __future__ import annotations

from os.path import abspath, join, exists
import json
import atexit

import wx

PRE_EXISTING_CONFIG = {}

_path = abspath(join(".", "config", 'window_preferences.config'))

if exists(_path):
    fp = open(_path)
    PRE_EXISTING_CONFIG = json.load(fp)
    fp.close()


def write_config():
    cfg_fp = open(_path, 'w+')
    json.dump(PRE_EXISTING_CONFIG, cfg_fp)
    cfg_fp.close()


atexit.register(write_config)


def on_idle(self):
    global PRE_EXISTING_CONFIG

    qualified_name = '.'.join((self.__module__, self.__class__.__name__))

    def wrapper(event):
        update_cfg = False
        if self.__resized:
            self.__resized = False
            update_cfg = True
        if self.__moved:
            self.__moved = False
            update_cfg = True
        if update_cfg:
            PRE_EXISTING_CONFIG[qualified_name] = {
                'size': self.GetSize().Get(),
                'position': self.GetPosition().Get()
            }
            self.Refresh()
            self.Layout()

    return wrapper


def on_size(self):

    def wrapper(event):
        self.__resized = True

    return wrapper


def on_move(self):

    def wrapper(event):
        self.__moved = True

    return wrapper


def preserve_ui_preferences(clazz):
    original_init = clazz.__init__
    qualified_name = '.'.join((clazz.__module__, clazz.__name__))

    def __init__(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.__resized = False
        self.__moved = False

        if qualified_name in PRE_EXISTING_CONFIG:
            self.SetSize(PRE_EXISTING_CONFIG[qualified_name]['size'])
            self.SetPosition(PRE_EXISTING_CONFIG[qualified_name]['position'])
            self.Refresh()

        self.Bind(wx.EVT_MOVE, on_move(self))
        self.Bind(wx.EVT_SIZE, on_size(self))
        self.Bind(wx.EVT_IDLE, on_idle(self))

    clazz.__init__ = __init__
    return clazz
