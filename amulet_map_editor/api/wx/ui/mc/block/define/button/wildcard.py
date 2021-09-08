from typing import Tuple, Dict, Any
import wx

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple

from amulet_map_editor.api.wx.ui.simple import SimpleDialog
from amulet_map_editor.api.wx.ui.mc.api import WildcardMCBlock
from amulet_map_editor.api.wx.ui.mc.block.define.widget import WildcardBlockDefine
from amulet_map_editor.api.wx.ui.mc.block.define.button.base import (
    BaseBlockDefineButton,
)
from amulet.api.block import PropertyTypeMultiple


class WildcardBlockDefineButton(BaseBlockDefineButton, WildcardMCBlock):
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
        show_pick_block: bool = False,
        max_char_length: int = 99999,
        state: Dict[str, Any] = None,
    ):
        state = state or {}
        state.setdefault("selected_properties", selected_properties)
        state.setdefault("all_properties", all_properties)
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
        WildcardMCBlock.__init__(self, **state)

    def _on_press(self, evt):
        dialog = SimpleDialog(self, "Pick a Block")
        self._block_widget = WildcardBlockDefine(
            dialog,
            self._translation_manager,
            wx.HORIZONTAL,
            self.platform,
            self.version_number,
            self.force_blockstate,
            self.namespace,
            self.base_name,
            self.selected_properties,
            self.all_properties,
        )
        dialog.sizer.Add(self._block_widget)
        dialog.Fit()
        if dialog.ShowModal() == wx.ID_OK:
            self._set_platform(self._block_widget.platform)
            self._set_version_number(self._block_widget.version_number)
            self._set_force_blockstate(self._block_widget.force_blockstate)
            self._set_namespace(self._block_widget.namespace)
            self._set_base_name(self._block_widget.base_name)
            self._set_all_properties(self._block_widget.all_properties)
            self._set_selected_properties(self._block_widget.selected_properties)
            self.update_button()
        self._block_widget = None
        dialog.Destroy()

    def update_button(self):
        """Update the text on the button from the internal state."""
        if self.selected_properties:
            properties = [
                f"{key}:({'|'.join([v.to_snbt() for v in val])})"
                for key, val in self.selected_properties.items()
            ]
            self.SetLabel(f" {self.namespace}:{self.base_name}[{','.join(properties)}]")
            properties_str = ",\n".join(properties)
            self.SetToolTip(f"{self.namespace}:{self.base_name}[\n{properties_str}\n]")
        else:
            self.SetLabel(f" {self.namespace}:{self.base_name}")
            self.SetToolTip(f"{self.namespace}:{self.base_name}")

    def _on_push(self) -> bool:
        update = super()._on_push()
        self._set_namespace(self.namespace)
        self._set_base_name(self.base_name)
        self._set_all_properties(self.all_properties)
        self._set_selected_properties(self.selected_properties)
        update = self._block_widget is not None and (
            update
            or self.namespace != self._block_widget.namespace
            or self.base_name != self._block_widget.base_name
            or self.all_properties != self._block_widget.all_properties
            or self.selected_properties != self._block_widget.selected_properties
        )
        if update:
            (
                self._block_widget.namespace,
                self._block_widget.base_name,
                self._block_widget.all_properties,
                self._block_widget.selected_properties,
            ) = (
                self.namespace,
                self.base_name,
                self.all_properties,
                self.selected_properties,
            )
        self.update_button()
        return update


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
