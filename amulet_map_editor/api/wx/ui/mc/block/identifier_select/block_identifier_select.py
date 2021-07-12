from typing import Dict, Any
import wx

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple
from amulet_map_editor.api.wx.ui.mc.base.base_identifier_select import BaseIdentifierSelect
from amulet_map_editor.api.wx.ui.mc.base.api.block import BaseMCBlock
from amulet_map_editor.api.wx.ui.mc.block.identifier_select.events import BlockIDChangeEvent, EVT_BLOCK_ID_CHANGE


class BlockIdentifierSelect(BaseIdentifierSelect, BaseMCBlock):
    """
    A UI consisting of a namespace choice, block name search box and list of block names.
    """

    @property
    def type_name(self) -> str:
        return "Block"

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str,
        version_number: VersionNumberTuple,
        force_blockstate: bool,
        namespace: str = None,
        block_name: str = None,
        show_pick_block: bool = False,
    ):
        super().__init__(
            parent,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            block_name,
            show_pick_block,
        )

    def _init_state(self, state: Dict[str, Any]):
        BaseMCBlock.__init__(self, **state)

    def _populate_namespace(self):
        version = self._translation_manager.get_version(
            self.platform, self.version_number
        )
        self._namespace_combo.Set(version.block.namespaces(self.force_blockstate))

    def _populate_base_name(self):
        version = self._translation_manager.get_version(
            self.platform, self.version_number
        )
        self._base_names = version.block.base_names(self.namespace, self.force_blockstate)
        self._base_name_list_box.SetItems(self._base_names)

    def _post_event(self, old_namespace: str, old_base_name: str, new_namespace: str, new_base_name: str):
        wx.PostEvent(
            self,
            BlockIDChangeEvent(
                new_namespace,
                new_base_name,
                old_namespace,
                old_base_name,
            ),
        )


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    dialog = wx.Dialog(
        None, title="BlockIdentifierSelect", style=wx.DEFAULT_DIALOG_STYLE | wx.DIALOG_NO_PARENT | wx.RESIZE_BORDER
    )
    sizer = wx.BoxSizer()
    dialog.SetSizer(sizer)
    widget = BlockIdentifierSelect(dialog, translation_manager, "java", (1, 16, 0), False)

    def on_change(evt: BlockIDChangeEvent):
        print(evt.old_namespace, evt.old_base_name, evt.namespace, evt.base_name)
    widget.Bind(EVT_BLOCK_ID_CHANGE, on_change)
    sizer.Add(
        widget,
        1,
        wx.ALL | wx.EXPAND,
        5,
    )
    dialog.Bind(wx.EVT_CLOSE, lambda evt: dialog.Destroy())
    dialog.Show()
    dialog.Fit()


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
