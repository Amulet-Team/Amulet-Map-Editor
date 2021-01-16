import wx
from typing import Callable
from amulet.api.level.world import World
from .base_edit_canvas import BaseEditCanvas


class EditCanvas(BaseEditCanvas):
    def __init__(self, parent: wx.Window, world: "World", close_callback: Callable):
        super().__init__(parent, world)
        self._close_callback = close_callback
