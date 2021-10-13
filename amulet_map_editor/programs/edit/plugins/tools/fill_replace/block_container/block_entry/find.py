import wx

from amulet_map_editor.api.wx.ui.mc.block import WildcardBlockDefineButton
from .base import BaseBlockEntry
from .custom_fill_button import SrcBlockState


class FindBlockEntry(BaseBlockEntry):
    """A UI element that holds a wildcard block button and close button"""

    def __init__(
        self,
        parent: wx.Window,
        state: SrcBlockState,
    ):
        super().__init__(parent)
        self._init_close_button()
        self._block_button = WildcardBlockDefineButton(
            self,
            state,
            max_char_length=40,
        )
        self._sizer.Add(self._block_button, 1)

    @property
    def block_button(self) -> WildcardBlockDefineButton:
        return self._block_button
