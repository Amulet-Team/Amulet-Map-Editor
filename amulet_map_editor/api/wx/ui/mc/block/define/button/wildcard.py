import wx

import PyMCTranslate

from amulet_map_editor.api.wx.ui.mc.block.define.widget import WildcardBlockDefine
from amulet_map_editor.api.wx.ui.mc.block.define.button.base import (
    BaseBlockDefineButton,
)
from amulet_map_editor.api.wx.ui.mc.state import BlockState


class WildcardBlockDefineButton(BaseBlockDefineButton):
    state: BlockState

    def _create_block_define(self, dialog: wx.Dialog) -> WildcardBlockDefine:
        return WildcardBlockDefine(
            dialog,
            self.state.copy(),
            orientation=wx.HORIZONTAL,
        )

    def update_button(self):
        """Update the text on the button from the internal state."""
        if self.state.properties_multiple:
            properties = [
                f"{key}:({'|'.join([v.to_snbt() for v in val])})"
                for key, val in self.state.properties_multiple.items()
            ]
            self.SetLabel(
                f" {self.state.namespace}:{self.state.base_name}[{','.join(properties)}]"
            )
            properties_str = ",\n".join(properties)
            self.SetToolTip(
                f"{self.state.namespace}:{self.state.base_name}[\n{properties_str}\n]"
            )
        else:
            self.SetLabel(f" {self.state.namespace}:{self.state.base_name}")
            self.SetToolTip(f"{self.state.namespace}:{self.state.base_name}")


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    dialog = wx.Dialog(
        None,
        title="WildcardBlockDefineButton",
        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
    )
    sizer = wx.BoxSizer()
    dialog.SetSizer(sizer)
    sizer.Add(
        WildcardBlockDefineButton.from_data(dialog, translation_manager),
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
