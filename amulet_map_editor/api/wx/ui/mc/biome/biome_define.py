from typing import Tuple

import PyMCTranslate
import wx

from amulet_map_editor.api.wx.ui.mc.base.base_define import BaseDefine
from amulet_map_editor.api.wx.ui.mc.biome.biome_select import BiomeSelect


class BiomeDefine(BaseDefine):
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
        biome_name: str = None,
        show_pick_biome: bool = False,
        **kwargs,
    ):
        super().__init__(
            parent,
            translation_manager,
            BiomeSelect,
            orientation,
            platform,
            version_number,
            namespace,
            default_name=biome_name,
            show_pick=show_pick_biome,
            show_force_blockstate=False,
            **kwargs,
        )

    def _on_picker_change(self, evt):
        evt.Skip()

    @property
    def biome_name(self) -> str:
        return self._picker.name

    @biome_name.setter
    def biome_name(self, biome_name: str):
        self._picker.name = biome_name

    @property
    def biome(self) -> str:
        return f"{self.namespace}:{self.biome_name}"

    @biome.setter
    def biome(self, biome: str):
        namespace, biome_name = biome.split(":")
        self._picker.set_namespace(namespace)
        self._picker.set_name(biome_name)

    @property
    def universal_biome(self) -> str:
        return self._translation_manager.get_version(
            self.platform, self.version_number
        ).biome.to_universal(self.biome)

    @universal_biome.setter
    def universal_biome(self, universal_biome: str):
        self.biome = self._translation_manager.get_version(
            self.platform, self.version_number
        ).biome.from_universal(universal_biome)


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
