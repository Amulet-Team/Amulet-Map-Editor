from typing import Tuple, Dict, Any

import PyMCTranslate
import wx

from amulet_map_editor.api.wx.ui.mc.base.base_define import BaseDefine
from amulet_map_editor.api.wx.ui.mc.base.api.biome import BaseMCBiomeIdentifier
from amulet_map_editor.api.wx.ui.mc.biome.identifier_select.biome_identifier_select import (
    BiomeIdentifierSelect,
)
from amulet_map_editor.api.wx.ui.mc.biome.identifier_select.events import BiomeIDChangeEvent, EVT_BIOME_ID_CHANGE
from amulet_map_editor.api.wx.ui.mc.version.events import VersionChangeEvent


class BiomeDefine(BaseDefine, BaseMCBiomeIdentifier):
    """
    A UI that merges a version select widget with a biome select widget.
    """

    def __init__(
        self,
        parent,
        translation_manager: PyMCTranslate.TranslationManager,
        orientation=wx.VERTICAL,
        platform: str = None,
        version_number: Tuple[int, int, int] = None,
        namespace: str = None,
        base_name: str = None,
        show_pick_biome: bool = False,
        state: Dict[str, Any] = None,
    ):
        state = state or {}
        state.setdefault("namespace", namespace)
        state.setdefault("base_name", base_name)
        super().__init__(
            parent,
            translation_manager,
            orientation,
            platform,
            version_number,
            False,
            state=state,
            show_force_blockstate=False
        )
        self._picker = BiomeIdentifierSelect(
            self,
            translation_manager,
            self.platform,
            self.version_number,
            self.force_blockstate,
            namespace,
            base_name,
            show_pick_biome,
        )
        self._picker.Bind(EVT_BIOME_ID_CHANGE, self._on_biome_id_change)
        self._top_sizer.Add(self._picker, 1, wx.EXPAND | wx.TOP, 5)

    def _init_state(self, state: Dict[str, Any]):
        BaseMCBiomeIdentifier.__init__(self, **state)

    def _on_version_change(self, evt: VersionChangeEvent):
        old_platform, old_version = self.platform, self.version_number
        old_namespace, old_base_name = self.namespace, self.base_name

        self.set_platform(evt.platform)
        self.set_version_number(evt.version_number)
        self.set_force_blockstate(evt.force_blockstate)

        universal_biome = self._translation_manager.get_version(old_platform, old_version).biome.to_universal(f"{self.namespace}:{self.base_name}")
        new_biome = self._translation_manager.get_version(self.platform, self.version_number).biome.from_universal(universal_biome)
        namespace, base_name = new_biome.split(":", 1)

        self.set_namespace(namespace)
        self.set_base_name(base_name)

        self._picker.set_platform(self.platform)
        self._picker.set_version_number(self.version_number)
        self._picker.set_force_blockstate(self.force_blockstate)
        self._picker.set_namespace(self.namespace)
        self._picker.set_base_name(self.base_name)
        self._picker.push()

        wx.PostEvent(
            self,
            BiomeIDChangeEvent(
                self.namespace,
                self.base_name,
                old_namespace,
                old_base_name,
            ),
        )

    def _on_biome_id_change(self, evt: BiomeIDChangeEvent):
        self.set_namespace(evt.namespace)
        self.set_base_name(evt.base_name)
        wx.PostEvent(
            self,
            BiomeIDChangeEvent(
                evt.namespace,
                evt.base_name,
                evt.old_namespace,
                evt.old_base_name,
            ),
        )

    def push(self) -> bool:
        update = super().push()
        self.set_namespace(self.namespace)
        self.set_base_name(self.base_name)
        if update:
            # The version changed
            self._picker.set_platform(self.platform)
            self._picker.set_version_number(self.version_number)
            self._picker.set_force_blockstate(self.force_blockstate)
        if self.namespace != self._picker.namespace or self.base_name != self._picker.base_name:
            update = True
            self._picker.set_namespace(self.namespace)
            self._picker.set_base_name(self.base_name)
        if update:
            self._picker.push()
        return update


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    dialog = wx.Dialog(
        None,
        title="BiomeDefine",
        style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
    )
    sizer = wx.BoxSizer()
    dialog.SetSizer(sizer)
    sizer.Add(
        BiomeDefine(dialog, translation_manager, wx.HORIZONTAL),
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
