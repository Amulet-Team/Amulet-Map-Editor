import wx
from typing import Union
from ...base_ui import BaseUI

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]


class BaseToolUI(BaseUI):
    @property
    def name(self) -> str:
        raise NotImplementedError

    def enable(self):
        pass

    def disable(self):
        self.canvas.reset_bound_events()

    def bind_events(self):
        pass
