from typing import Tuple, Optional
import wx
import PyMCTranslate
from amulet.api.block import Block
from amulet.api.block_entity import BlockEntity
from amulet_map_editor.api.wx.ui.block_select import BlockDefine


class BlockSelectDialog(wx.Dialog):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        block: Tuple[Block, Optional[BlockEntity]],
        platform: str,
        version_number: Tuple[int, ...],
        force_blockstate: bool,
        *args,
        **kwargs
    ):
        # begin wxGlade: BlockSelectDialog.__init__
        kwargs["style"] = (
            kwargs.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        )
        super().__init__(parent, *args, **kwargs)
        self.SetTitle("Pick Block")

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self._block_define = BlockDefine(
            self,
            translation_manager,
            wx.HORIZONTAL,
            platform,
            version_number,
            force_blockstate,
        )
        self._block_define.universal_block = block
        sizer.Add(self._block_define, 1, wx.EXPAND | wx.LEFT | wx.TOP | wx.RIGHT, 5)

        button_sizer = wx.StdDialogButtonSizer()
        sizer.Add(button_sizer, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

        self.button_ok = wx.Button(self, wx.ID_OK, "")
        self.button_ok.SetDefault()
        button_sizer.AddButton(self.button_ok)

        self.button_cancel = wx.Button(self, wx.ID_CANCEL, "")
        button_sizer.AddButton(self.button_cancel)

        button_sizer.Realize()

        sizer.Fit(self)

        self.SetAffirmativeId(self.button_ok.GetId())
        self.SetEscapeId(self.button_cancel.GetId())

        self.Layout()

    @property
    def universal_block(self) -> Tuple[Block, Optional[BlockEntity]]:
        return self._block_define.universal_block

    @universal_block.setter
    def universal_block(self, universal_block: Tuple[Block, Optional[BlockEntity]]):
        self._block_define.universal_block = universal_block
