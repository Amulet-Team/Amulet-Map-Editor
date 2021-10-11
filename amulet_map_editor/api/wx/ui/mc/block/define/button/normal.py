import wx
import copy

import PyMCTranslate

from amulet_map_editor.api.wx.ui.mc.block.define.widget import BlockDefine
from amulet_map_editor.api.wx.ui.mc.block.define.button.base import (
    BaseBlockDefineButton,
)
from amulet_map_editor.api.wx.ui.mc.state import BlockState


class BlockDefineButton(BaseBlockDefineButton):
    state: BlockState

    def _create_block_define(self, dialog: wx.Dialog) -> BlockDefine:
        return BlockDefine(
            dialog,
            copy.deepcopy(self.state),
            orientation=wx.HORIZONTAL,
        )

    def update_button(self):
        """Update the text on the button from the internal state."""
        blockstate = f"{self.state.namespace}:{self.state.base_name}"
        if self.state.properties:
            props = ",".join(
                f"{key}={val}" for key, val in self.state.properties.items()
            )
            blockstate = f"{blockstate}[{props}]"
        self.SetLabel(f" {blockstate}")
        self.SetToolTip(blockstate)


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
        BlockDefineButton.from_data(dialog, translation_manager),
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
