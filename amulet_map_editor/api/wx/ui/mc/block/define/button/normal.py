from typing import Tuple, Optional
import wx

import PyMCTranslate
from amulet.api.block import Block, PropertyType
from amulet.api.block_entity import BlockEntity
from amulet_map_editor.api.wx.ui.simple import SimpleDialog
from amulet_map_editor.api.wx.ui.mc.base import NormalMCBlockAPI
from amulet_map_editor.api.wx.ui.mc.block.define.widget import BlockDefine

from amulet_map_editor.api.wx.ui.mc.block.define.button.base import BaseBlockDefineButton


class BlockDefineButton(BaseBlockDefineButton, NormalMCBlockAPI):
    def __init__(self, parent: wx.Window, translation_manager: PyMCTranslate.TranslationManager, *args, **kwargs):
        super().__init__(parent)
        self._dialog = SimpleDialog(parent, "Pick a Block")
        self._block_widget = BlockDefine(self._dialog, translation_manager, wx.HORIZONTAL, *args, **kwargs)
        self._dialog.sizer.Add(self._block_widget)
        self.update_button()

    def update_button(self):
        """Update the text on the button from the internal state."""
        self.SetLabel(self.block.full_blockstate)

    @property
    def properties(self) -> PropertyType:
        return self._block_widget.properties

    @properties.setter
    def properties(self, properties: PropertyType):
        self.set_properties(properties)
        self.update_button()

    def set_properties(self, properties: PropertyType):
        self._block_widget.properties = properties

    @property
    def block(self) -> Block:
        """The block object stored in this button."""
        return Block(self.namespace, self.block_name, self.properties)

    @block.setter
    def block(self, block: Block):
        self.set_block(block)
        self.update_button()

    def set_block(self, block: Block):
        self.set_namespace(block.namespace)
        self.set_block_name(block.base_name)
        self.set_properties(block.properties)

    @property
    def block_entity(self) -> Optional[BlockEntity]:
        return self._block_widget.block_entity

    @block_entity.setter
    def block_entity(self, block_entity: Optional[BlockEntity]):
        self.set_block_entity(block_entity)
        self.update_button()

    def set_block_entity(self, block_entity: Optional[BlockEntity]):
        self._block_widget.block_entity = block_entity

    @property
    def universal_block(self) -> Tuple[Block, Optional[BlockEntity]]:
        return self._block_widget.universal_block

    @universal_block.setter
    def universal_block(self, universal_block: Tuple[Block, Optional[BlockEntity]]):
        self.set_universal_block(universal_block)
        self.update_button()

    def set_universal_block(self, universal_block: Tuple[Block, Optional[BlockEntity]]):
        self._block_widget.universal_block = universal_block


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    dialog = wx.Dialog(
        None,
        title="WildcardBlockDefine",
        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
    )
    sizer = wx.BoxSizer()
    dialog.SetSizer(sizer)
    sizer.Add(
        BlockDefineButton(dialog, translation_manager),
        0,
        wx.ALL,
        5,
    )
    dialog.Show()
    dialog.Fit()
    dialog.Bind(wx.EVT_CLOSE, lambda evt: dialog.Destroy())


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
