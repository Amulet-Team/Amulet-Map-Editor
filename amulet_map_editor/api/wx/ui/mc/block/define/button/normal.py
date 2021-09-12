from typing import Tuple, Dict, Any
import wx

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple

from amulet_map_editor.api.wx.ui.simple import SimpleDialog
from amulet_map_editor.api.wx.ui.mc.api import NormalMCBlock
from amulet_map_editor.api.wx.ui.mc.block.define.widget import BlockDefine
from amulet_map_editor.api.wx.ui.mc.block.define.button.base import (
    BaseBlockDefineButton,
)
from amulet.api.block import PropertyType


class BlockDefineButton(BaseBlockDefineButton, NormalMCBlock):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
        properties: PropertyType = None,
        show_pick_block: bool = False,
        max_char_length: int = 99999,
        state: Dict[str, Any] = None,
    ):
        state = state or {}
        state.setdefault("properties", properties)
        BaseBlockDefineButton.__init__(
            self,
            parent,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
            show_pick_block=show_pick_block,
            max_char_length=max_char_length,
            state=state,
        )
        self.update_button()

    def _init_state(self, state: Dict[str, Any]):
        NormalMCBlock.__init__(self, **state)

    def _create_block_define(self, dialog: wx.Dialog) -> BlockDefine:
        return BlockDefine(
            dialog,
            self._translation_manager,
            wx.HORIZONTAL,
            self.platform,
            self.version_number,
            self.force_blockstate,
            self.namespace,
            self.base_name,
            self.properties,
        )

    def _update_from_block_define(self, block_define: BlockDefine):
        self._set_platform(self._block_widget.platform)
        self._set_version_number(self._block_widget.version_number)
        self._set_force_blockstate(self._block_widget.force_blockstate)
        self._set_namespace(self._block_widget.namespace)
        self._set_base_name(self._block_widget.base_name)
        self._set_properties(self._block_widget.properties)

    def _on_press(self, evt):
        dialog = SimpleDialog(self, "Pick a Block")
        self._block_widget = self._create_block_define(dialog)
        dialog.sizer.Add(self._block_widget, 1, wx.EXPAND)
        dialog.Fit()
        if dialog.ShowModal() == wx.ID_OK:
            self._update_from_block_define(self._block_widget)
            self.update_button()
        self._block_widget = None
        dialog.Destroy()

    def update_button(self):
        """Update the text on the button from the internal state."""
        blockstate = self.block.full_blockstate
        self.SetLabel(f" {blockstate}")
        self.SetToolTip(blockstate)

    def _on_push(self) -> bool:
        update = super()._on_push()
        self._set_namespace(self.namespace)
        self._set_base_name(self.base_name)
        self._set_properties(self.properties)
        update = self._block_widget is not None and (
            update
            or self.namespace != self._block_widget.namespace
            or self.base_name != self._block_widget.base_name
            or self.properties != self._block_widget.properties
        )
        if update:
            (
                self._block_widget.namespace,
                self._block_widget.base_name,
                self._block_widget.properties,
            ) = (self.namespace, self.base_name, self.properties)
        self.update_button()
        return False


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    dialog = wx.Dialog(
        None,
        title="BlockDefineButton",
        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
    )
    sizer = wx.BoxSizer()
    dialog.SetSizer(sizer)
    sizer.Add(
        BlockDefineButton(dialog, translation_manager),
        0,
        wx.ALL,
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
