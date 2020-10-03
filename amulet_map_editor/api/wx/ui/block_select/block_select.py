import wx
from typing import Tuple

import PyMCTranslate

from amulet_map_editor.api.wx.ui.base_select import BaseSelect


class BlockSelect(BaseSelect):
    TypeName = "Block"

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str,
        version_number: Tuple[int, int, int],
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

    def _populate_namespace(self):
        version = self._translation_manager.get_version(
            self._platform, self._version_number
        )
        namespaces = version.block.namespaces(self._force_blockstate)
        self._do_text_event = False
        self._namespace_combo.Set(namespaces)

    def _populate_item_name(self):
        version = self._translation_manager.get_version(
            self._platform, self._version_number
        )
        self._names = version.block.base_names(self.namespace, self._force_blockstate)
        self._list_box.SetItems(self._names)


if __name__ == "__main__":

    def main():
        app = wx.App()
        translation_manager = PyMCTranslate.new_translation_manager()
        dialog = wx.Dialog(None)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(BlockSelect(dialog, translation_manager, "java", (1, 16, 0), False))
        dialog.Show()
        dialog.Fit()
        app.MainLoop()

    main()
