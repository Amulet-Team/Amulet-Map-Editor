import wx.lib.scrolledpanel
from typing import Tuple, Optional

import PyMCTranslate

from amulet_map_editor.api.wx.ui.mc.base.base_define import BaseDefine
from amulet_map_editor.api.wx.ui.mc.block import BlockSelect

from amulet_map_editor.api.wx.ui.mc.block.properties import (
    BasePropertySelect,
)


class BaseBlockDefine(BaseDefine):
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
        show_pick_block: bool = False,
        **kwargs,
    ):
        super().__init__(
            parent,
            translation_manager,
            BlockSelect,
            orientation,
            platform,
            version_number,
            namespace,
            default_name=block_name,
            show_pick=show_pick_block,
            force_blockstate=force_blockstate,
            **kwargs,
        )
        self._property_picker: Optional[BasePropertySelect] = None

    def _on_picker_change(self, evt):
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
            self._picker.namespace,
            self._picker.name,
        )

    @property
    def force_blockstate(self) -> bool:
        return self._version_picker.force_blockstate

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        self._version_picker.force_blockstate = force_blockstate

    @property
    def block_name(self) -> str:
        return self._picker.name

    @block_name.setter
    def block_name(self, block_name: str):
        self._picker.name = block_name
