import wx
from wx.lib import newevent
from typing import Tuple, List, Optional
import os

import PyMCTranslate
from amulet_map_editor import IMG_DIR

NamespaceChangeEvent, EVT_NAMESPACE_CHANGE = newevent.NewEvent()  # the namespace entry changed
BlockNameChangeEvent, EVT_BLOCK_NAME_CHANGE = newevent.NewEvent()  # the block name entry changed
BlockChangeEvent, EVT_BLOCK_CHANGE = newevent.NewEvent()  # the block or namespace changed. Generated after EVT_BLOCK_NAME_CHANGE
PickBlockEvent, EVT_PICK_BLOCK = newevent.NewEvent()  # The pick block button was pressed


class BlockSelect(wx.Panel):
    def __init__(
            self,
            parent,
            translation_manager: PyMCTranslate.TranslationManager,
            platform: str,
            version_number: Tuple[int, int, int],
            force_blockstate: bool = None,
            namespace: str = None,
            block_name: str = None,
            show_pick_block: bool = True
    ):
        super().__init__(parent, style=wx.BORDER_SIMPLE)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        self._translation_manager = translation_manager

        self._platform: Optional[str] = None
        self._version_number: Optional[Tuple[int, int, int]] = None
        self._force_blockstate: Optional[bool] = None

        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._sizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 5)
        text = wx.StaticText(self, label="Namespace:", style=wx.ALIGN_CENTER)
        sizer.Add(text, 1, wx.ALIGN_CENTER_VERTICAL)
        self._namespace_combo = wx.ComboBox(self)
        sizer.Add(self._namespace_combo, 2)
        self._set_version((
            platform,
            version_number,
            force_blockstate or False
        ))
        self._populate_namespace()
        self._set_namespace(namespace)

        self._namespace_combo.Bind(wx.EVT_TEXT, lambda evt: wx.PostEvent(self, NamespaceChangeEvent(namespace=self.namespace)))

        self.Bind(EVT_NAMESPACE_CHANGE, self._on_namespace_change)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(sizer, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)
        header_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(header_sizer, 0, wx.EXPAND | wx.BOTTOM, 5)
        header_sizer.Add(
            wx.StaticText(self, label="Block name:", style=wx.ALIGN_CENTER),
            1, wx.ALIGN_CENTER_VERTICAL
        )
        search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        header_sizer.Add(search_sizer, 2, wx.EXPAND)
        self._block_search = wx.SearchCtrl(self)
        search_sizer.Add(self._block_search, 1, wx.ALIGN_CENTER_VERTICAL)
        self._block_search.Bind(wx.EVT_TEXT, self._on_search_change)
        if show_pick_block:
            pick_block_button = wx.BitmapButton(self, bitmap=wx.Bitmap(os.path.join(IMG_DIR, "icon", "pick.png")))
            search_sizer.Add(pick_block_button, 0, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
            pick_block_button.Bind(wx.EVT_BUTTON, lambda evt: wx.PostEvent(self, PickBlockEvent(widget=self)))
        self._block_list_box = wx.ListBox(self, style=wx.LB_SINGLE)
        sizer.Add(self._block_list_box, 1, wx.EXPAND)

        self._block_names: List[str] = []
        self._populate_block_name()
        self._set_block_name(block_name)
        self._block_list_box.Bind(wx.EVT_LISTBOX, lambda evt: self._post_block_change())

    def _post_block_change(self):
        wx.PostEvent(
            self,
            BlockNameChangeEvent(
                block_name=self.block_name
            )
        ),
        wx.PostEvent(
            self,
            BlockChangeEvent(
                namespace=self.namespace,
                block_name=self.block_name
            )
        )

    @property
    def version(self) -> Tuple[str, Tuple[int, int, int], bool]:
        return self._platform, self._version_number, self._force_blockstate

    @version.setter
    def version(self, version: Tuple[str, Tuple[int, int, int], bool]):
        self._set_version(version)
        self._populate_namespace()
        self.namespace = None

    def _set_version(self, version: Tuple[str, Tuple[int, int, int], bool]):
        assert version[0] in self._translation_manager.platforms() and \
               version[1] in self._translation_manager.version_numbers(version[0]) and \
               isinstance(version[2], bool), \
               f"{version} is not a valid version"
        self._platform, self._version_number, self._force_blockstate = version

    @property
    def namespace(self) -> str:
        return self._namespace_combo.GetValue()

    @namespace.setter
    def namespace(self, namespace: str):
        self._set_namespace(namespace)
        wx.PostEvent(self, NamespaceChangeEvent(namespace=self.namespace))

    def _set_namespace(self, namespace: str):
        namespace = namespace or "minecraft"
        if isinstance(namespace, str):
            if namespace in self._namespace_combo.GetItems():
                self._namespace_combo.SetSelection(self._namespace_combo.GetItems().index(namespace))
            else:
                self._namespace_combo.ChangeValue(namespace)

    @property
    def block_name(self) -> str:
        block_name: str = self._block_list_box.GetString(self._block_list_box.GetSelection())
        if self._block_list_box.GetSelection() == 0 and block_name.startswith("\""):
            block_name = block_name[1:-1]
        return block_name

    @block_name.setter
    def block_name(self, block_name: str):
        self._set_block_name(block_name)
        self._post_block_change()

    def _set_block_name(self, block_name: str):
        block_name = block_name or ""
        self._block_search.ChangeValue(block_name)
        self._update_block_name(block_name)

    def _populate_namespace(self):
        version = self._translation_manager.get_version(self._platform, self._version_number)
        namespaces = version.block.namespaces(self._force_blockstate)
        self._namespace_combo.SetItems(namespaces)  # TODO: This produces EVT_TEXT making the rest fire twice

    def _populate_block_name(self):
        version = self._translation_manager.get_version(self._platform, self._version_number)
        self._block_names = version.block.base_names(self.namespace, self._force_blockstate)
        self._block_list_box.SetItems(
            self._block_names
        )

    def _on_namespace_change(self, evt):
        self._populate_block_name()
        self.block_name = None
        evt.Skip()

    def _on_search_change(self, evt):
        search_str = evt.GetString()
        self._update_block_name(search_str)

    def _update_block_name(self, search_str: str):
        block_names = [bn for bn in self._block_names if search_str in bn]
        if search_str not in block_names:
            search_str = f"\"{search_str}\""
            block_names.insert(0, search_str)
        self._block_list_box.SetItems(
            block_names
        )
        if search_str in block_names:
            self._block_list_box.SetSelection(block_names.index(search_str))


if __name__ == '__main__':
    def main():
        translation_manager = PyMCTranslate.new_translation_manager()
        app = wx.App()
        for cls in (BlockSelect,):
            dialog = wx.Dialog(None)
            sizer = wx.BoxSizer()
            dialog.SetSizer(sizer)
            sizer.Add(cls(dialog, translation_manager, "java", (1, 16, 0)))
            dialog.Show()
            dialog.Fit()
        app.MainLoop()
    main()
