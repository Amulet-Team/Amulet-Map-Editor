import wx
import wx.lib.scrolledpanel

import PyMCTranslate
import amulet_nbt
from amulet.api.data_types import VersionNumberTuple
from amulet.api.block import PropertyType
from amulet_map_editor.api.wx.ui.events import EVT_CHILD_SIZE

from amulet_map_editor.api.wx.ui.mc.block import (
    SinglePropertySelect,
    EVT_SINGLE_PROPERTIES_CHANGE,
    SinglePropertiesChangeEvent,
)
from amulet_map_editor.api.wx.ui.mc.block.define.widget.base import BaseBlockDefine
from amulet_map_editor.api.wx.ui.mc.block.define.events import (
    BlockChangeEvent,
    EVT_BLOCK_CHANGE,
)
from amulet_map_editor.api.wx.ui.mc.state import BlockState


class BlockDefine(BaseBlockDefine):
    """
    A UI that merges a version select widget with a block select widget and a property select.
    """

    state: BlockState
    _property_picker: SinglePropertySelect

    def __init__(
        self,
        parent,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        state: BlockState = None,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
        properties: PropertyType = None,
        show_pick_block: bool = False,
        orientation=wx.VERTICAL,
    ):
        if not isinstance(state, BlockState):
            state = BlockState(
                translation_manager,
                platform=platform,
                version_number=version_number,
                force_blockstate=force_blockstate,
                namespace=namespace,
                base_name=base_name,
                properties=properties,
            )
        BaseBlockDefine.__init__(
            self,
            parent,
            translation_manager,
            state=state,
            orientation=orientation,
            show_pick_block=show_pick_block,
        )

        right_sizer = wx.BoxSizer(wx.VERTICAL)
        border = wx.LEFT if orientation == wx.HORIZONTAL else wx.TOP
        self._sizer.Add(right_sizer, 1, wx.EXPAND | border, 5)
        self._property_picker = self._create_property_picker(translation_manager)
        self._property_picker.Bind(
            EVT_SINGLE_PROPERTIES_CHANGE, self._post_block_change
        )
        right_sizer.Add(self._property_picker, 1, wx.EXPAND)
        self.Layout()

    def _create_property_picker(
        self, translation_manager: PyMCTranslate.TranslationManager
    ) -> SinglePropertySelect:
        return SinglePropertySelect(self, translation_manager, state=self.state)

    def _post_block_change(self, evt: SinglePropertiesChangeEvent):
        wx.PostEvent(
            self,
            BlockChangeEvent(
                self.state.platform,
                self.state.version_number,
                self.state.force_blockstate,
                self.state.namespace,
                self.state.base_name,
                self.state.properties,
            ),
        )


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()

    def create_dialog(block):
        dialog = wx.Dialog(
            None,
            title=f"BlockDefine with block {block['namespace']}:{block['base_name']}",
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
        )
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        obj = BlockDefine(
            dialog,
            translation_manager,
            platform="java",
            version_number=(1, 16, 0),
            force_blockstate=False,
            **block,
            orientation=wx.HORIZONTAL,
        )

        sizer.Add(
            obj,
            1,
            wx.ALL,
            5,
        )

        def on_change(evt: BlockChangeEvent):
            print(
                evt.platform,
                evt.version_number,
                evt.force_blockstate,
                evt.namespace,
                evt.base_name,
                evt.properties,
            )

        def on_close(evt):
            dialog.Destroy()

        def on_child_size(evt):
            dialog.Layout()
            evt.Skip()

        obj.Bind(EVT_BLOCK_CHANGE, on_change)
        dialog.Bind(wx.EVT_CLOSE, on_close)
        dialog.Bind(EVT_CHILD_SIZE, on_child_size)
        dialog.Show()
        dialog.Fit()

    for block_ in (
        {
            "namespace": "minecraft",
            "base_name": "oak_fence",
            "properties": {
                "east": amulet_nbt.TAG_String("false"),
                "north": amulet_nbt.TAG_String("true"),
                "south": amulet_nbt.TAG_String("false"),
                "west": amulet_nbt.TAG_String("false"),
            },
        },
        {
            "namespace": "modded",
            "base_name": "block",
            "properties": {
                "test": amulet_nbt.TAG_String("hello"),
            },
        },
    ):
        create_dialog(block_)


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
