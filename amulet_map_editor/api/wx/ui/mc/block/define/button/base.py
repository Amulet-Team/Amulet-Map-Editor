import wx
from typing import Optional

import PyMCTranslate
from amulet_map_editor.api.wx.ui.mc.block.define import BaseBlockDefine
from amulet_map_editor.api.wx.ui.mc.state import StateHolder, BlockState
from amulet_map_editor.api.wx.ui.simple import SimpleDialog


class BaseBlockDefineButton(wx.Button, StateHolder):
    _block_widget: Optional[BaseBlockDefine]

    def __init__(
        self,
        parent: wx.Window,
        state: BlockState,
        *,
        show_pick_block: bool = False,
        max_char_length: int = 99999,
    ):
        assert isinstance(state, BlockState)
        StateHolder.__init__(self, state)
        wx.Button.__init__(self, parent, style=wx.BU_LEFT)
        self._block_widget: Optional[BaseBlockDefine] = None
        self.Bind(wx.EVT_BUTTON, self._on_press)
        self._show_pick_block = show_pick_block
        self._max_char_length = max(3, max_char_length)
        self.update_button()

    @classmethod
    def from_data(
        cls,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        show_pick_block: bool = False,
        max_char_length: int = 99999,
        **kwargs,
    ):
        return cls(
            parent,
            BlockState(translation_manager, **kwargs),
            show_pick_block=show_pick_block,
            max_char_length=max_char_length,
        )

    def SetLabel(self, label: str):
        if len(label) > self._max_char_length:
            label = f"{label[:self._max_char_length]}..."
        super().SetLabel(label)

    def _on_press(self, evt):
        dialog = SimpleDialog(self, "Pick a Block")
        self._block_widget = self._create_block_define(dialog)
        dialog.sizer.Add(self._block_widget, 1, wx.EXPAND)
        dialog.Fit()
        if dialog.ShowModal() == wx.ID_OK:
            self.state = self._block_widget.state
            self.update_button()
        self._block_widget = None
        dialog.Destroy()

    def _create_block_define(self, dialog: wx.Dialog) -> BaseBlockDefine:
        raise NotImplementedError

    def update_button(self):
        raise NotImplementedError
