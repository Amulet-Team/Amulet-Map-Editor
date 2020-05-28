import wx
from typing import Union
from ...base_ui import BaseUI

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]


class BaseToolUI(BaseUI):
    def enable(self):
        raise NotImplementedError

    def disable(self):
        raise NotImplementedError
