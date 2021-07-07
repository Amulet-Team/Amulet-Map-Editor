import wx
import PyMCTranslate

from amulet.api.block import PropertyTypeMultiple
from amulet_map_editor.api.wx.ui.simple import SimpleDialog
from amulet_map_editor.api.wx.ui.mc.base import WildcardMCBlockAPI
from amulet_map_editor.api.wx.ui.mc.block.define.widget import WildcardBlockDefine
from amulet_map_editor.api.wx.ui.mc.block.define.button.base import BaseBlockDefineButton


class WildcardBlockDefineButton(BaseBlockDefineButton, WildcardMCBlockAPI):
    def __init__(self, parent: wx.Window, translation_manager: PyMCTranslate.TranslationManager, *args, **kwargs):
        super().__init__(parent)
        self._dialog = SimpleDialog(parent, "Pick a Block")
        self._block_widget = WildcardBlockDefine(self._dialog, translation_manager, wx.HORIZONTAL, *args, **kwargs)
        self._dialog.sizer.Add(self._block_widget)
        self.update_button()

    def update_button(self):
        """Update the text on the button from the internal state."""
        if self.selected_properties:
            properties = [f"{key}:({'|'.join([v.to_snbt() for v in val])})" for key, val in self.selected_properties.items()]
            self.SetLabel(f"{self.namespace}:{self.block_name}[{','.join(properties)}]")
            properties_str = ',\n'.join(properties)
            self.SetToolTip(f"{self.namespace}:{self.block_name}[\n{properties_str}\n]")
        else:
            self.SetLabel(f"{self.namespace}:{self.block_name}")
            self.SetToolTip(f"{self.namespace}:{self.block_name}")

    @property
    def selected_properties(self) -> PropertyTypeMultiple:
        return self._block_widget.selected_properties

    @selected_properties.setter
    def selected_properties(self, selected_properties: PropertyTypeMultiple):
        self.set_selected_properties(selected_properties)
        self.update_button()

    def set_selected_properties(self, selected_properties: PropertyTypeMultiple):
        self._block_widget.selected_properties = selected_properties

    @property
    def all_properties(self) -> PropertyTypeMultiple:
        """The values that exist for every property."""
        return self._block_widget.all_properties

    @all_properties.setter
    def all_properties(self, all_properties: PropertyTypeMultiple):
        self.set_all_properties(all_properties)
        self.update_button()

    def set_all_properties(self, all_properties: PropertyTypeMultiple):
        self._block_widget.all_properties = all_properties


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
        WildcardBlockDefineButton(dialog, translation_manager),
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
