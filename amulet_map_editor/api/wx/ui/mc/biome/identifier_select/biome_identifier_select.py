from typing import Dict, Any
import wx

from amulet_map_editor.api.wx.ui.mc.base.base_identifier_select import (
    BaseIdentifierSelect,
)
from amulet_map_editor.api.wx.ui.mc.base.api.biome import MCBiomeIdentifier
from amulet_map_editor.api.wx.ui.mc.biome.identifier_select.events import (
    BiomeIDChangeEvent,
    EVT_BIOME_ID_CHANGE,
)


class BiomeIdentifierSelect(BaseIdentifierSelect, MCBiomeIdentifier):
    """
    A UI consisting of a namespace choice, biome name search box and list of biome names.
    """

    @property
    def type_name(self) -> str:
        return "Biome"

    def _init_state(self, state: Dict[str, Any]):
        MCBiomeIdentifier.__init__(self, **state)

    def _populate_namespace(self):
        version = self._translation_manager.get_version(
            self.platform, self.version_number
        )
        namespaces = list(
            set(
                [biome_id.split(":", 1)[0] for biome_id in version.biome.biome_ids]
            )
        )
        self._namespace_combo.Set(namespaces)

    def _populate_base_name(self):
        version = self._translation_manager.get_version(
            self.platform, self.version_number
        )
        namespace = f"{self.namespace}:"
        namespace_size = len(namespace)

        self._base_names = [
            biome_id[namespace_size:]
            for biome_id in version.biome.biome_ids
            if biome_id.startswith(namespace)
        ]
        self._base_name_list_box.SetItems(self._base_names)

    def _post_event(
        self,
        old_namespace: str,
        old_base_name: str,
        new_namespace: str,
        new_base_name: str,
    ):
        wx.PostEvent(
            self,
            BiomeIDChangeEvent(
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
    import PyMCTranslate

    translation_manager = PyMCTranslate.new_translation_manager()
    dialog = wx.Dialog(
        None,
        title="BiomeIdentifierSelect",
        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
    )
    sizer = wx.BoxSizer()
    dialog.SetSizer(sizer)
    widget = BiomeIdentifierSelect(dialog, translation_manager, "java", (1, 16, 0), False)

    def on_change(evt: BiomeIDChangeEvent):
        print(evt.old_namespace, evt.old_base_name, evt.namespace, evt.base_name)

    widget.Bind(EVT_BIOME_ID_CHANGE, on_change)
    sizer.Add(
        widget,
        1,
        wx.ALL | wx.EXPAND,
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
