from amulet_map_editor.api.wx.ui.base_select import BaseSelect


class BiomeSelect(BaseSelect):
    def _populate_namespace(self):
        version = self._translation_manager.get_version(
            self._platform, self._version_number
        )
        namespaces = list(set([
            biome_id[: biome_id.find(":")] for biome_id in version.biome.biome_ids
        ]))
        self._do_text_event = False
        self._namespace_combo.Set(namespaces)

    def _populate_item_name(self):
        version = self._translation_manager.get_version(
            self._platform, self._version_number
        )
        self._names = [
            biome_id
            for biome_id in version.biome.biome_ids
            if biome_id.startswith(self.namespace)
        ]
        self._list_box.SetItems(self._names)
