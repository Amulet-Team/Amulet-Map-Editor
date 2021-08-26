import wx
import wx.lib.scrolledpanel
from typing import Tuple, Dict, Any

import PyMCTranslate
from amulet.api.block import PropertyType, Block

from amulet_map_editor.api.wx.ui.mc.block import (
    BlockIDChangeEvent,
    SinglePropertySelect,
    EVT_SINGLE_PROPERTIES_CHANGE,
    SinglePropertiesChangeEvent,
)
from amulet_map_editor.api.wx.ui.mc.block.define.widget.base import BaseBlockDefine
from amulet_map_editor.api.wx.ui.mc.block.define.events import (
    BlockChangeEvent,
    EVT_BLOCK_CHANGE,
)
from amulet_map_editor.api.wx.ui.mc.api import NormalMCBlock
from amulet_map_editor.api.wx.ui.mc.version import VersionChangeEvent


class BlockDefine(BaseBlockDefine, NormalMCBlock):
    """
    A UI that merges a version select widget with a block select widget and a property select.
    """

    def __init__(
        self,
        parent,
        translation_manager: PyMCTranslate.TranslationManager,
        orientation=wx.VERTICAL,
        platform: str = None,
        version_number: Tuple[int, int, int] = None,
        force_blockstate: bool = None,
        namespace: str = None,
        base_name: str = None,
        properties: PropertyType = None,
        show_pick_block: bool = False,
        state: Dict[str, Any] = None,
    ):
        state = state or {}
        state.setdefault("properties", properties)
        BaseBlockDefine.__init__(
            self,
            parent,
            translation_manager,
            orientation,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
            show_pick_block=show_pick_block,
            state=state,
        )

        right_sizer = wx.BoxSizer(wx.VERTICAL)
        border = wx.LEFT if orientation == wx.HORIZONTAL else wx.TOP
        self._sizer.Add(right_sizer, 1, wx.EXPAND | border, 5)
        self._property_picker = SinglePropertySelect(
            self,
            translation_manager,
            self.platform,
            self.version_number,
            self.force_blockstate,
            self.namespace,
            self.base_name,
            self.properties,
        )
        right_sizer.Add(self._property_picker, 1, wx.EXPAND)
        self._property_picker.Bind(
            EVT_SINGLE_PROPERTIES_CHANGE, self._on_property_change
        )
        self.Layout()

    def _init_state(self, state: Dict[str, Any]):
        NormalMCBlock.__init__(self, **state)

    def _on_version_change(self, evt: VersionChangeEvent):
        self.Freeze()
        old_platform, old_version, old_force_blockstate = (
            self.platform,
            self.version_number,
            self.force_blockstate,
        )
        old_namespace, old_base_name, old_properties = (
            self.namespace,
            self.base_name,
            self.properties,
        )

        self._set_platform(evt.platform)
        self._set_version_number(evt.version_number)
        self._set_force_blockstate(evt.force_blockstate)

        (
            universal_block,
            universal_block_entity,
            _,
        ) = self._translation_manager.get_version(
            old_platform, old_version
        ).block.to_universal(
            Block(old_namespace, old_base_name, old_properties),
            force_blockstate=self.force_blockstate,
        )
        new_block, _, _ = self._translation_manager.get_version(
            self.platform, self.version_number
        ).block.from_universal(
            universal_block, universal_block_entity, self.force_blockstate
        )

        if isinstance(new_block, Block):
            self._set_namespace(new_block.namespace)
            self._set_base_name(new_block.base_name)
            self._set_properties(new_block.properties)
        else:
            self._set_namespace(None)
            self._set_base_name(None)
            self._set_properties(None)

        (
            self._picker.platform,
            self._picker.version_number,
            self._picker.force_blockstate,
            self._picker.namespace,
            self._picker.base_name,
        ) = (
            self._property_picker.platform,
            self._property_picker.version_number,
            self._property_picker.force_blockstate,
            self._property_picker.namespace,
            self._property_picker.base_name,
        ) = (
            self.platform,
            self.version_number,
            self.force_blockstate,
            self.namespace,
            self.base_name,
        )
        self._property_picker.properties = self.properties

        wx.PostEvent(
            self,
            BlockChangeEvent(
                self.platform,
                self.version_number,
                self.force_blockstate,
                self.namespace,
                self.base_name,
                self.properties,
                old_platform,
                old_version,
                old_force_blockstate,
                old_namespace,
                old_base_name,
                old_properties,
            ),
        )
        self.Thaw()

    def _on_block_change(self, evt: BlockIDChangeEvent):
        old_namespace, old_base_name, old_properties = (
            self.namespace,
            self.base_name,
            self.properties,
        )
        super()._on_block_change(evt)
        self._set_properties(None)
        self._property_picker.properties = self.properties
        wx.PostEvent(
            self,
            BlockChangeEvent(
                self.platform,
                self.version_number,
                self.force_blockstate,
                self.namespace,
                self.base_name,
                self.properties,
                self.platform,
                self.version_number,
                self.force_blockstate,
                old_namespace,
                old_base_name,
                old_properties,
            ),
        )

    def _on_property_change(self, evt: SinglePropertiesChangeEvent):
        self.Layout()
        old_properties = self.properties
        self._set_properties(evt.properties)
        wx.PostEvent(
            self,
            BlockChangeEvent(
                self.platform,
                self.version_number,
                self.force_blockstate,
                self.namespace,
                self.base_name,
                self.properties,
                self.platform,
                self.version_number,
                self.force_blockstate,
                self.namespace,
                self.base_name,
                old_properties,
            ),
        )

    def _on_push(self) -> bool:
        update = super()._on_push()
        self._set_properties(self.properties)
        if update or self.properties != self._property_picker.properties:
            update = True
            self._property_picker.properties = self.properties
        return update


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    import amulet_nbt

    translation_manager = PyMCTranslate.new_translation_manager()
    for block in (
        (
            "minecraft",
            "oak_fence",
            {
                "east": amulet_nbt.TAG_String("false"),
                "north": amulet_nbt.TAG_String("true"),
                "south": amulet_nbt.TAG_String("false"),
                "west": amulet_nbt.TAG_String("false"),
            },
        ),
        (
            "modded",
            "block",
            {
                "test": amulet_nbt.TAG_String("hello"),
            },
        ),
    ):

        dialog = wx.Dialog(
            None,
            title=f"BlockDefine with block {block[0]}:{block[1]}",
            style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT,
        )
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        obj = BlockDefine(
            dialog,
            translation_manager,
            wx.HORIZONTAL,
            "java",
            (1, 16, 0),
            False,
            *block,
        )
        sizer.Add(
            obj,
            1,
            wx.ALL | wx.EXPAND,
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
                evt.old_platform,
                evt.old_version_number,
                evt.old_force_blockstate,
                evt.old_namespace,
                evt.old_base_name,
                evt.old_properties,
            )

        obj.Bind(EVT_BLOCK_CHANGE, on_change)

        def get_on_close(dialog_):
            def on_close(evt):
                dialog_.Destroy()

            return on_close

        dialog.Bind(wx.EVT_CLOSE, get_on_close(dialog))
        dialog.Show()
        dialog.Fit()


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
