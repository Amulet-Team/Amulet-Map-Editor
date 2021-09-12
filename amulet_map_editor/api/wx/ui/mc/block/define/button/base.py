import wx
from typing import Tuple, Optional, Dict, Any

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple

from amulet_map_editor.api.wx.ui.mc.api import BaseMCBlockIdentifier
from amulet_map_editor.api.wx.ui.mc.block.define import BaseBlockDefine


class BaseBlockDefineButton(wx.Button, BaseMCBlockIdentifier):
    _block_widget: Optional[BaseBlockDefine]

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
        show_pick_block: bool = False,
        max_char_length: int = 99999,
        state: Dict[str, Any] = None,
    ):
        state = state or {}
        state.setdefault("translation_manager", translation_manager)
        state.setdefault("platform", platform)
        state.setdefault("version_number", version_number)
        state.setdefault("force_blockstate", force_blockstate)
        state.setdefault("namespace", namespace)
        state.setdefault("base_name", base_name)
        # This is the init call to the class that stores the internal state of the data.
        # This needs to be at the start to ensure that the internal state is set up before anything else is done.
        # It is not a direct call to init so that subclasses of this class can substitute in which state subclass is used.
        self._init_state(state)
        wx.Button.__init__(self, parent, style=wx.BU_LEFT)
        self._block_widget: Optional[BaseBlockDefine] = None
        self.Bind(wx.EVT_BUTTON, self._on_press)
        self._show_pick_block = show_pick_block
        self._max_char_length = max(3, max_char_length)

    def _init_state(self, state: Dict[str, Any]):
        """
        Call the init method of the state manager.
        This is here so that nested classes do not have to init the state managers multiple times.
        """
        BaseMCBlockIdentifier.__init__(self, **state)

    def SetLabel(self, label: str):
        if len(label) > self._max_char_length:
            label = f"{label[:self._max_char_length]}..."
        super().SetLabel(label)

    def _on_press(self, evt):
        raise NotImplementedError

    def _on_push(self) -> bool:
        self._set_platform(self.platform)
        self._set_version_number(self.version_number)
        self._set_force_blockstate(self.force_blockstate)
        if self._block_widget is not None and (
            self.platform != self._block_widget.platform
            or self.version_number != self._block_widget.version_number
            or self.force_blockstate != self._block_widget.force_blockstate
        ):
            (
                self._block_widget.platform,
                self._block_widget.version_number,
                self._block_widget.force_blockstate,
            ) = (self.platform, self.version_number, self.force_blockstate)
            return True
        return False
