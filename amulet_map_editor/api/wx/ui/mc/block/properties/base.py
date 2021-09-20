import wx

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple
from amulet_map_editor.api.wx.ui.mc.state import StateHolder, BlockState


class BasePropertySelect(wx.Panel, StateHolder):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        state: BlockState = None,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
    ):
        if not isinstance(state, BlockState):
            state = BlockState(
                translation_manager,
                platform=platform,
                version_number=version_number,
                force_blockstate=force_blockstate,
                namespace=namespace,
                base_name=base_name,
            )
        StateHolder.__init__(self, state)
        wx.Panel.__init__(self, parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)
