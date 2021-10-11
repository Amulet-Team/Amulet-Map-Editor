import wx

import PyMCTranslate
from amulet_map_editor.api.wx.ui.mc.state import BiomeResourceIDState
from amulet_map_editor.api.wx.ui.mc.base.base_identifier_select import (
    BaseIdentifierSelect,
)
from amulet_map_editor.api.wx.ui.mc.biome.identifier_select.events import (
    BiomeIDChangeEvent,
    EVT_BIOME_ID_CHANGE,
)


class BiomeIdentifierSelect(BaseIdentifierSelect):
    """
    A UI consisting of a namespace choice, biome name search box and list of biome names.
    """

    @property
    def type_name(self) -> str:
        return "Biome"

    @classmethod
    def from_data(
        cls,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        show_pick: bool = False,
        **kwargs
    ):
        return cls(
            parent,
            BiomeResourceIDState(translation_manager, **kwargs),
            show_pick=show_pick,
        )

    def _post_event(
        self,
        namespace: str,
        base_name: str,
    ):
        wx.PostEvent(
            self,
            BiomeIDChangeEvent(
                namespace,
                base_name,
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
    widget = BiomeIdentifierSelect.from_data(
        dialog,
        translation_manager,
        platform="java",
        version_number=(1, 16, 0),
        force_blockstate=False,
    )

    def on_change(evt: BiomeIDChangeEvent):
        print(evt.namespace, evt.base_name)

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
