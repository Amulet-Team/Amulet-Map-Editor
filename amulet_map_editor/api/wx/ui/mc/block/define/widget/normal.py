import wx
import wx.lib.scrolledpanel
from typing import Tuple, Optional

import PyMCTranslate
from amulet.api.block import PropertyType, Block
from amulet.api.block_entity import BlockEntity

from amulet_map_editor.api.wx.ui.mc.block.properties import (
    SinglePropertySelect,
    EVT_SINGLE_PROPERTIES_CHANGE,
)
from amulet_map_editor.api.wx.ui.mc.block.define.widget.base import BaseBlockDefine
from amulet_map_editor.api.wx.ui.mc.base import NormalMCBlockAPI


class BlockDefine(BaseBlockDefine, NormalMCBlockAPI):
    """
    A UI that merges a version select widget with a block select widget and a property select.
    """

    def __init__(
        self,
        parent,
        translation_manager: PyMCTranslate.TranslationManager,
        orientation=wx.VERTICAL,
        platform: str = None,
        version_number: Tuple[int, int, int] = None,
        force_blockstate: bool = None,
        namespace: str = None,
        block_name: str = None,
        properties: PropertyType = None,
        show_pick_block: bool = False,
        **kwargs,
    ):
        super().__init__(
            parent,
            translation_manager,
            orientation,
            platform,
            version_number,
            force_blockstate,
            namespace,
            block_name,
            show_pick_block=show_pick_block,
            **kwargs,
        )

        right_sizer = wx.BoxSizer(wx.VERTICAL)
        border = wx.LEFT if orientation == wx.HORIZONTAL else wx.TOP
        self._sizer.Add(right_sizer, 1, wx.EXPAND | border, 5)
        self._property_picker = SinglePropertySelect(
            self,
            translation_manager,
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            self._picker.namespace,
            self._picker.name,
            properties,
        )
        right_sizer.Add(self._property_picker, 1, wx.EXPAND)
        self._property_picker.Bind(
            EVT_SINGLE_PROPERTIES_CHANGE, self._on_property_change
        )

        self.Layout()

    @property
    def properties(self) -> PropertyType:
        return self._property_picker.properties

    @properties.setter
    def properties(self, properties: PropertyType):
        self._property_picker.properties = properties

    @property
    def block(self) -> Block:
        return Block(self.namespace, self.block_name, self.properties)

    @block.setter
    def block(self, block: Block):
        self._picker.namespace, self._picker.base_name = (
            block.namespace,
            block.base_name,
        )
        self._update_properties()
        self.properties = block.properties

    @property
    def block_entity(self) -> Optional[BlockEntity]:
        return None  # TODO

    @block_entity.setter
    def block_entity(self, block_entity: Optional[BlockEntity]):
        if block_entity is not None:
            pass  # TODO

    @property
    def universal_block(self) -> Tuple[Block, Optional[BlockEntity]]:
        return self._translation_manager.get_version(
            self.platform, self.version_number
        ).block.to_universal(self.block, self.block_entity, self.force_blockstate)[:2]

    @universal_block.setter
    def universal_block(self, universal_block: Tuple[Block, Optional[BlockEntity]]):
        block, block_entity = universal_block
        v_block, v_block_entity = self._translation_manager.get_version(
            self.platform, self.version_number
        ).block.from_universal(block, block_entity, self.force_blockstate)[:2]
        if isinstance(v_block, Block):
            self.block = v_block
            self.block_entity = v_block_entity


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    dialog = wx.Dialog(
        None,
        title="BlockDefine",
        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
    )
    sizer = wx.BoxSizer()
    dialog.SetSizer(sizer)
    sizer.Add(
        BlockDefine(dialog, translation_manager, wx.HORIZONTAL),
        1,
        wx.ALL | wx.EXPAND,
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
