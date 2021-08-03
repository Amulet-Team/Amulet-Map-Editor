import wx.lib.scrolledpanel
from typing import Tuple, Optional, Dict, Any

import PyMCTranslate

from amulet_map_editor.api.wx.ui.mc.base.base_define import BaseDefine
from amulet_map_editor.api.wx.ui.mc.block import BlockIdentifierSelect

from amulet_map_editor.api.wx.ui.mc.block import (
    BasePropertySelect,
    BlockIDChangeEvent,
    EVT_BLOCK_ID_CHANGE,
)
from amulet_map_editor.api.wx.ui.mc.base import BaseMCBlockIdentifier
from amulet_map_editor.api.wx.ui.mc.version import VersionChangeEvent


class BaseBlockDefine(BaseDefine, BaseMCBlockIdentifier):
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
        base_name: str = None,
        show_pick_block: bool = False,
        state: Dict[str, Any] = None,
    ):
        state = state or {}
        state.setdefault("translation_manager", translation_manager)
        state.setdefault("platform", platform)
        state.setdefault("version_number", version_number)
        state.setdefault("force_blockstate", force_blockstate)
        state.setdefault("namespace", namespace)
        state.setdefault("base_name", base_name)
        BaseDefine.__init__(
            self,
            parent,
            translation_manager,
            orientation,
            platform,
            version_number,
            force_blockstate,
            state=state,
        )
        self._picker = BlockIdentifierSelect(
            self,
            translation_manager,
            self.platform,
            self.version_number,
            self.force_blockstate,
            namespace,
            base_name,
            show_pick_block,
        )
        self._top_sizer.Add(self._picker, 0, wx.EXPAND | wx.TOP, 5)
        self._picker.Bind(EVT_BLOCK_ID_CHANGE, self._on_block_change)
        self._property_picker: Optional[BasePropertySelect] = None

    def _init_state(self, state: Dict[str, Any]):
        raise NotImplementedError

    def _on_version_change(self, evt: VersionChangeEvent):
        # TODO: Translate the block and properties to the new version
        raise NotImplementedError

    def _on_block_change(self, evt: BlockIDChangeEvent):
        self._set_namespace(evt.namespace)
        self._set_base_name(evt.base_name)
        self._property_picker.namespace = self.namespace
        self._property_picker.base_name = self.base_name

    def _on_property_change(self, evt):
        self.Layout()
        evt.Skip()

    def _on_push(self) -> bool:
        update = super()._on_push()
        if update:
            self._property_picker.platform = self.platform
            self._property_picker.version_number = self.version_number
            self._property_picker.force_blockstate = self.force_blockstate
        return update
