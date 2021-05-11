from amulet_map_editor.api.wx.ui.base_select import BaseSelect


class BiomeSelect(BaseSelect):
    """
    A UI consisting of a namespace choice, biome name search box and list of biome names.
    """

    @property
    def type_name(self) -> str:
        return "Biome"

    def _populate_namespace(self):
        version = self._translation_manager.get_version(
            self._platform, self._version_number
        )
        namespaces = list(
            set(
                [biome_id[: biome_id.find(":")] for biome_id in version.biome.biome_ids]
            )
        )
        self._do_text_event = False
        self._namespace_combo.Set(namespaces)

    def _populate_item_name(self):
        version = self._translation_manager.get_version(
            self._platform, self._version_number
        )
        self._names = [
            biome_id[len(self.namespace) + 1 :]
            for biome_id in version.biome.biome_ids
            if biome_id.startswith(self.namespace)
        ]
        self._list_box.SetItems(self._names)


if __name__ == "__main__":

    def main():
        import wx
        import PyMCTranslate

        app = wx.App()
        translation_manager = PyMCTranslate.new_translation_manager()
        dialog = wx.Dialog(None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(
            BiomeSelect(dialog, translation_manager, "java", (1, 16, 0), False),
            1,
            wx.ALL | wx.EXPAND,
            5,
        )
        dialog.Show()
        dialog.Fit()
        dialog.Bind(wx.EVT_CLOSE, lambda evt: dialog.Destroy())
        app.MainLoop()

    main()
