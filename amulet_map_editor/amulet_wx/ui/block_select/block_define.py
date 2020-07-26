import wx
import wx.lib.scrolledpanel
from typing import Tuple

import PyMCTranslate
import amulet_nbt
from amulet.api.block import PropertyType

from amulet_map_editor.amulet_wx.ui.version_select import (
    VersionSelect,
    EVT_VERSION_CHANGE,
)
from amulet_map_editor.amulet_wx.ui.block_select.block import (
    BlockSelect,
    EVT_BLOCK_CHANGE,
)

if __name__ != "__main__":
    from amulet_map_editor.amulet_wx.ui.block_select.properties import PropertySelect


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
        **kwargs,
    ):
        super().__init__(parent)

        sizer = wx.BoxSizer(orientation)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(left_sizer, 1, wx.EXPAND)
        right_sizer = wx.BoxSizer(wx.VERTICAL)
        if orientation == wx.HORIZONTAL:
            sizer.Add(right_sizer, 1, wx.EXPAND | wx.LEFT, 5)
        else:
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
            **kwargs,
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
        )
        right_sizer.Add(self._property_picker, 1, wx.EXPAND)
        self._block_picker.Bind(EVT_BLOCK_CHANGE, self._on_block_change)

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
        self._property_picker.version_block = (
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            evt.namespace,
            evt.block_name,
        )
        evt.Skip()


if __name__ == "__main__":
    app = wx.App()
    from amulet_map_editor.amulet_wx.ui.block_select.properties import PropertySelect

    def main():
        translation_manager = PyMCTranslate.new_translation_manager()
        dialog = wx.Dialog(None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(BlockDefine(dialog, translation_manager, wx.HORIZONTAL), 1, wx.ALL | wx.EXPAND, 5)
        dialog.Show()
        dialog.Fit()
        app.MainLoop()

    main()
