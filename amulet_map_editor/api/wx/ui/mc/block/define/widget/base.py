import PyMCTranslate
import wx

from amulet_map_editor.api.wx.ui.mc.base.base_define import BaseDefine
from amulet_map_editor.api.wx.ui.mc.block import BlockIdentifierSelect

from amulet_map_editor.api.wx.ui.mc.block import BasePropertySelect, EVT_BLOCK_ID_CHANGE
from amulet_map_editor.api.wx.ui.mc.state import BlockState


class BaseBlockDefine(BaseDefine):
    """
    A UI that merges a version select widget with a block select widget and a property select.
    """

    state: BlockState
    _identifier_select: BlockIdentifierSelect
    _property_picker: BasePropertySelect

    def __init__(
        self,
        parent,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        state: BlockState = None,
        orientation=wx.VERTICAL,
        show_pick_block: bool = False,
    ):
        assert isinstance(state, BlockState)
        BaseDefine.__init__(
            self,
            parent,
            translation_manager,
            state=state,
            orientation=orientation,
        )
        self._identifier_select = BlockIdentifierSelect(
            self,
            translation_manager,
            state=self.state,
            show_pick=show_pick_block,
        )
        self._identifier_select.Bind(EVT_BLOCK_ID_CHANGE, self._post_change)
        self._top_sizer.Add(self._identifier_select, 1, wx.EXPAND | wx.TOP, 5)
