import wx
import wx.lib.scrolledpanel
from typing import Tuple

import PyMCTranslate
from amulet.api.block import PropertyTypeMultiple

from amulet_map_editor.api.wx.ui.mc.block.properties import (
    MultiplePropertySelect,
    EVT_MULTIPLE_PROPERTIES_CHANGE,
)
from amulet_map_editor.api.wx.ui.mc.block.define.widget.base import BaseBlockDefine
from amulet_map_editor.api.wx.ui.mc.base import WildcardMCBlockAPI


class WildcardBlockDefine(BaseBlockDefine, WildcardMCBlockAPI):
    """
    A UI that merges a version select widget with a block select widget and a multi property select.
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
        properties: PropertyTypeMultiple = None,
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
        self._property_picker = MultiplePropertySelect(
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
            EVT_MULTIPLE_PROPERTIES_CHANGE, self._on_property_change
        )

        self.Layout()

    @property
    def selected_properties(self) -> PropertyTypeMultiple:
        """
        The values that are checked for each property.
        This UI can have more than one property value checked (ticked).
        """
        return self._property_picker.selected_properties

    @selected_properties.setter
    def selected_properties(self, selected_properties: PropertyTypeMultiple):
        self._property_picker.selected_properties = selected_properties

    @property
    def all_properties(self) -> PropertyTypeMultiple:
        """The values that exist for every property."""
        return self._property_picker.all_properties

    @all_properties.setter
    def all_properties(self, all_properties: PropertyTypeMultiple):
        self._property_picker.all_properties = all_properties


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
        WildcardBlockDefine(dialog, translation_manager, wx.HORIZONTAL),
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
