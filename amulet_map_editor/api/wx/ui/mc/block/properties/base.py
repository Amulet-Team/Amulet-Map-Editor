import wx
from typing import Tuple, Dict, Any

import PyMCTranslate
from amulet_map_editor.api.wx.ui.mc.base.api.block import BaseMCBlockIdentifier


class BasePropertySelect(wx.Panel, BaseMCBlockIdentifier):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str,
        version_number: Tuple[int, ...],
        force_blockstate: bool,
        namespace: str = None,
        base_name: str = None,
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

        wx.Panel.__init__(self, parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

    def _init_state(self, state: Dict[str, Any]):
        """
        Call the init method of the state manager.
        This is here so that nested classes do not have to init the state managers multiple times.
        """
        BaseMCBlockIdentifier.__init__(self, **state)
