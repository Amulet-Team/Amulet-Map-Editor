import wx

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple
from amulet.api.block import PropertyTypeMultiple
from amulet_map_editor.api.wx.ui.mc.block import WildcardBlockDefineButton
from .base import BaseBlockEntry


class FindBlockEntry(BaseBlockEntry):
    """A UI element that holds a wildcard block button and close button"""

    _button_props = BaseBlockEntry._button_props + (
        "all_properties",
        "selected_properties",
    )

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
        selected_properties: PropertyTypeMultiple = None,
        all_properties: PropertyTypeMultiple = None,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)
        self._block_button = WildcardBlockDefineButton(
            self,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
            selected_properties,
            all_properties,
        )
        self._sizer.Add(self._block_button, 1)
        self._init_close_button()

    @property
    def block_button(self) -> WildcardBlockDefineButton:
        return self._block_button
