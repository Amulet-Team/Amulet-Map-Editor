import wx

import PyMCTranslate
from amulet.api.block import PropertyType


class BaseSubWildcardPropertySelect(wx.Panel):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
    ):
        super().__init__(parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)
        self._translation_manager = translation_manager

    @property
    def properties(self) -> PropertyType:
        raise NotImplementedError

    @properties.setter
    def properties(self, properties: PropertyType):
        raise NotImplementedError
