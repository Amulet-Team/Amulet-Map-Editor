import wx

import PyMCTranslate
from amulet.api.block import PropertyTypeMultiple


class BaseMultipleProperty(wx.Panel):
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
    def extra_properties(self) -> PropertyTypeMultiple:
        """
        The values that are checked for each property.
        This UI can have more than one property value checked (ticked).
        """
        raise NotImplementedError

    @extra_properties.setter
    def extra_properties(self, properties: PropertyTypeMultiple):
        raise NotImplementedError
