import wx

import PyMCTranslate
from amulet_map_editor.api.wx.ui.mc.state import StateHolder, BlockState


class BasePropertySelect(wx.Panel, StateHolder):
    def __init__(
        self,
        parent: wx.Window,
        state: BlockState,
    ):
        assert isinstance(state, BlockState)
        StateHolder.__init__(self, state)
        wx.Panel.__init__(self, parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

    @classmethod
    def from_data(
        cls,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        **kwargs
    ):
        return cls(
            parent,
            BlockState(translation_manager, **kwargs),
        )
