import wx

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple
from amulet_map_editor.api.wx.ui.mc.base.base_identifier_select import (
    BaseIdentifierSelect,
)
from amulet_map_editor.api.wx.ui.mc.state import BlockResourceIDState
from amulet_map_editor.api.wx.ui.mc.block.identifier_select.events import (
    BlockIDChangeEvent,
    EVT_BLOCK_ID_CHANGE,
)


class BlockIdentifierSelect(BaseIdentifierSelect):
    """
    A UI consisting of a namespace choice, block name search box and list of block names.
    """

    @property
    def type_name(self) -> str:
        return "Block"

    def _create_default_state(
        self,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
    ) -> BlockResourceIDState:
        return BlockResourceIDState(
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
        )

    def _post_event(
        self,
        namespace: str,
        base_name: str,
    ):
        wx.PostEvent(
            self,
            BlockIDChangeEvent(
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
        title="BlockIdentifierSelect",
        style=wx.DEFAULT_DIALOG_STYLE | wx.DIALOG_NO_PARENT | wx.RESIZE_BORDER,
    )
    sizer = wx.BoxSizer()
    dialog.SetSizer(sizer)
    widget = BlockIdentifierSelect(
        dialog,
        translation_manager,
        platform="java",
        version_number=(1, 16, 0),
        force_blockstate=False,
    )

    def on_change(evt: BlockIDChangeEvent):
        print(evt.namespace, evt.base_name)

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
