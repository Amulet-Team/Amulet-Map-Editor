from __future__ import annotations

from typing import Type, Tuple, TypedDict, Dict

import atexit

import wx

from amulet_map_editor import CONFIG


class WindowConfig(TypedDict):
    size: Tuple[int, int]
    position: Tuple[int, int]
    is_full_screen: bool


PRE_EXISTING_CONFIG: Dict[str, WindowConfig] = CONFIG.get("window_preferences", {})


def write_config():
    CONFIG.put("window_preferences", PRE_EXISTING_CONFIG)


atexit.register(write_config)


def preserve_ui_preferences(cls: Type[wx.TopLevelWindow]):
    assert issubclass(
        cls, wx.TopLevelWindow
    ), "This takes a subclass of a top level window."

    qualified_name = ".".join((cls.__module__, cls.__qualname__))

    class TopLevelWindowWrapper(cls):
        __resized: bool
        __size: Tuple[int, int]
        __position: Tuple[int, int]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__resized = False
            self.__position = self.GetPosition().Get()
            self.__size = self.GetSize().Get()

            if qualified_name in PRE_EXISTING_CONFIG:
                window_config = PRE_EXISTING_CONFIG[qualified_name]
                x, y = window_config["position"]
                dx, dy = window_config["size"]

                # Check if the window header intersects on a connected display.
                display_count = wx.Display.GetCount()
                for i in range(display_count):
                    display = wx.Display(i)
                    geometry = display.GetGeometry()
                    if geometry.Intersects(wx.Rect(x, y, dx, 10)):
                        break
                else:
                    if display_count:
                        # If there is no display at that point move it to the first display.
                        display = wx.Display(0)
                        geometry = display.GetGeometry()
                        x = geometry.x
                        y = geometry.y

                self.SetPosition(wx.Point(x, y))
                self.SetSize(wx.Size(dx, dy))
                self.Maximize(window_config.get("is_full_screen", False))
            else:
                self.Maximize()
            self.Layout()
            self.Refresh()

            self.Bind(wx.EVT_MOVE, self.__on_resize)
            self.Bind(wx.EVT_SIZE, self.__on_resize)
            self.Bind(wx.EVT_IDLE, self.__on_idle)

        def __on_idle(self, evt):
            if self.__resized:
                self.__resized = False
                PRE_EXISTING_CONFIG[qualified_name] = {
                    "size": self.__size,
                    "position": self.__position,
                    "is_full_screen": self.IsMaximized(),
                }
            evt.Skip()

        def __on_resize(self, evt):
            self.__resized = True
            if not self.IsMaximized():
                # only store the non-maximised state
                self.__position = self.GetPosition().Get()
                self.__size = self.GetSize().Get()
            evt.Skip()

    return TopLevelWindowWrapper
