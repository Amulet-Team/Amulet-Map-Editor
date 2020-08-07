import wx
import wx.lib.scrolledpanel
from typing import Tuple, Optional, Dict

import PyMCTranslate
import amulet_nbt
from amulet.api.block import PropertyType, Block
from amulet.api.block_entity import BlockEntity
from amulet.api.data_types import VersionNumberTuple, PlatformType

from amulet_map_editor.amulet_wx.ui.version_select import (
    VersionSelect,
    EVT_VERSION_CHANGE,
)
from amulet_map_editor.amulet_wx.ui.block_select.block import (
    BlockSelect,
    EVT_BLOCK_CHANGE,
)

from amulet_map_editor.amulet_wx.ui.block_select.properties import (
    PropertySelect,
    WildcardSNBTType,
    EVT_PROPERTIES_CHANGE,
)


class BlockDefine(wx.Panel):
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
        nbt: amulet_nbt.TAG_Compound = None,
        show_nbt: bool = True,
        wildcard_properties=False,
        show_pick_block: bool = False,
        **kwargs,
    ):
        super().__init__(parent)

        self._translation_manager = translation_manager
        sizer = wx.BoxSizer(orientation)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        if orientation == wx.HORIZONTAL:
            sizer.Add(left_sizer, 1, wx.EXPAND)
            sizer.Add(right_sizer, 1, wx.EXPAND | wx.LEFT, 5)
        else:
            sizer.Add(left_sizer, 2, wx.EXPAND)
            sizer.Add(right_sizer, 1, wx.EXPAND | wx.TOP, 5)

        self._version_picker = VersionSelect(
            self,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            **kwargs,
        )
        left_sizer.Add(self._version_picker, 0, wx.EXPAND)

        self._block_picker = BlockSelect(
            self,
            translation_manager,
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            namespace,
            block_name,
            show_pick_block,
        )
        left_sizer.Add(self._block_picker, 1, wx.EXPAND | wx.TOP, 5)
        self._version_picker.Bind(EVT_VERSION_CHANGE, self._on_version_change)

        self._property_picker = PropertySelect(
            self,
            translation_manager,
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            self._block_picker.namespace,
            self._block_picker.block_name,
            properties,
            wildcard_properties,
        )
        right_sizer.Add(self._property_picker, 1, wx.EXPAND)
        self._block_picker.Bind(EVT_BLOCK_CHANGE, self._on_block_change)
        self._property_picker.Bind(EVT_PROPERTIES_CHANGE, self._on_property_change)

        self.SetSizerAndFit(sizer)
        self.Layout()

    def _on_version_change(self, evt):
        self._block_picker.version = (
            evt.platform,
            evt.version_number,
            evt.force_blockstate,
        )
        evt.Skip()

    def _on_block_change(self, evt):
        self._update_properties()
        evt.Skip()

    def _on_property_change(self, evt):
        self.Layout()
        evt.Skip()

    def _update_properties(self):
        self._property_picker.version_block = (
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            self._block_picker.namespace,
            self._block_picker.block_name,
        )

    @property
    def platform(self) -> PlatformType:
        return self._version_picker.platform

    @platform.setter
    def platform(self, platform: PlatformType):
        self._version_picker.platform = platform

    @property
    def version_number(self) -> VersionNumberTuple:
        return self._version_picker.version_number

    @version_number.setter
    def version_number(self, version_number: VersionNumberTuple):
        self._version_picker.version_number = version_number

    @property
    def force_blockstate(self) -> bool:
        return self._version_picker.force_blockstate

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        self._version_picker.force_blockstate = force_blockstate

    @property
    def version(self) -> Tuple[PlatformType, VersionNumberTuple, bool]:
        return self._version_picker.version

    @version.setter
    def version(self, version: Tuple[PlatformType, VersionNumberTuple, bool]):
        self._version_picker.version = version

    @property
    def namespace(self) -> str:
        return self._block_picker.namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self._block_picker.namespace = namespace

    @property
    def block_name(self) -> str:
        return self._block_picker.block_name

    @block_name.setter
    def block_name(self, block_name: str):
        self._block_picker.block_name = block_name

    @property
    def str_properties(self) -> Dict[str, "WildcardSNBTType"]:
        return self._property_picker.str_properties

    @str_properties.setter
    def str_properties(self, str_properties: Dict[str, "WildcardSNBTType"]):
        self._property_picker.str_properties = str_properties

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
        self._block_picker.set_namespace(block.namespace)
        self._block_picker.set_block_name(block.base_name)
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


if __name__ == "__main__":

    def main():
        app = wx.App()
        translation_manager = PyMCTranslate.new_translation_manager()
        dialog = wx.Dialog(None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
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
        app.MainLoop()

    main()
