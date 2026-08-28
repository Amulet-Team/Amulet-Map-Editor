import wx
import wx.lib.scrolledpanel
from typing import Tuple, Optional, Dict, Mapping, Union

import PyMCTranslate
from amulet.api.block import PropertyType, Block, PropertyValueType
from amulet.api.block_entity import BlockEntity
from amulet_nbt import SNBTType, AbstractBaseTag

from amulet_map_editor.api.wx.ui.base_define import BaseDefine
from amulet_map_editor.api.wx.ui.block_select import BlockSelect

from amulet_map_editor.api.wx.ui.block_select.properties import (
    PropertySelect,
    WildcardSNBTType,
)


class BlockDefine(BaseDefine):
    def __init__(
        self,
        parent,
        translation_manager: PyMCTranslate.TranslationManager,
        orientation=wx.VERTICAL,
        platform: str = None,
        version_number: Tuple[int, int, int] = None,
        force_blockstate: bool = None,
        namespace: str = None,
        block_name: str = None,
        properties: Mapping[str, Union[SNBTType, PropertyValueType]] = None,
        wildcard_properties=False,
        show_pick_block: bool = False,
        **kwargs,
    ):
        super().__init__(
            parent,
            translation_manager,
            BlockSelect,
            orientation,
            platform,
            version_number,
            namespace,
            default_name=block_name,
            show_pick=show_pick_block,
            force_blockstate=force_blockstate,
            **kwargs,
        )

        right_sizer = wx.BoxSizer(wx.VERTICAL)
        if orientation == wx.HORIZONTAL:
            self._sizer.Add(right_sizer, 1, wx.EXPAND | wx.TOP | wx.RIGHT | wx.BOTTOM, 5)
        else:
            self._sizer.Add(right_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, 5)

        self._property_picker = PropertySelect(
            self,
            translation_manager,
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            self._picker.namespace,
            self._picker.name,
            {
                key: val.to_snbt() if isinstance(val, AbstractBaseTag) else val
                for key, val in (properties or {}).items()
            },
            wildcard_properties,
        )
        right_sizer.Add(self._property_picker, 1, wx.EXPAND)

    def _on_picker_change(self, evt):
        self._update_properties()
        evt.Skip()

    def _update_properties(self):
        self._property_picker.version_block = (
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            self._picker.namespace,
            self._picker.name,
        )

    @property
    def force_blockstate(self) -> bool:
        return self._version_picker.force_blockstate

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        self._version_picker.force_blockstate = force_blockstate

    @property
    def block_name(self) -> str:
        return self._picker.name

    @block_name.setter
    def block_name(self, block_name: str):
        self._picker.name = block_name

    @property
    def str_properties(self) -> Dict[str, "WildcardSNBTType"]:
        return self._property_picker.str_properties

    @str_properties.setter
    def str_properties(self, str_properties: Dict[str, "WildcardSNBTType"]):
        self._property_picker.str_properties = str_properties

    @property
    def properties(self) -> PropertyType:
        return self._property_picker.properties

    @properties.setter
    def properties(self, properties: PropertyType):
        self._property_picker.properties = properties

    @property
    def block(self) -> Block:
        return Block(self.namespace, self.block_name, self.properties)

    @block.setter
    def block(self, block: Block):
        self._picker.set_namespace(block.namespace)
        self._picker.set_name(block.base_name)
        self._update_properties()
        self.properties = block.properties

    @property
    def block_entity(self) -> Optional[BlockEntity]:
        return None  # TODO

    @block_entity.setter
    def block_entity(self, block_entity: Optional[BlockEntity]):
        if block_entity is not None:
            pass  # TODO

    @property
    def universal_block(self) -> Tuple[Block, Optional[BlockEntity]]:
        return self._translation_manager.get_version(
            self.platform, self.version_number
        ).block.to_universal(self.block, self.block_entity, self.force_blockstate)[:2]

    @universal_block.setter
    def universal_block(self, universal_block: Tuple[Block, Optional[BlockEntity]]):
        block, block_entity = universal_block
        v_block, v_block_entity = self._translation_manager.get_version(
            self.platform, self.version_number
        ).block.from_universal(block, block_entity, self.force_blockstate)[:2]
        if isinstance(v_block, Block):
            self.block = v_block
            self.block_entity = v_block_entity


if __name__ == "__main__":

    def main():
        from amulet_map_editor.api.wx.ui.block_select.properties import (
            EVT_PROPERTIES_CHANGE,
        )
        from amulet_map_editor.api.wx.ui.widget_size_changed import EVT_WIDGET_SIZE_CHANGED
        from amulet_map_editor.api.wx.ui.simple import SimpleScrollablePanel

        translation_manager = PyMCTranslate.new_translation_manager()

        class Replace(SimpleScrollablePanel):
            def __init__(self, parent: wx.Window):
                SimpleScrollablePanel.__init__(self, parent)

                self._original_block = BlockDefine(
                    self,
                    translation_manager,
                    wx.VERTICAL,
                    wildcard_properties=True,
                    show_pick_block=True,
                )
                self._sizer.Add(self._original_block, 0, wx.EXPAND)
                self._replacement_block = BlockDefine(
                    self, translation_manager, wx.VERTICAL, show_pick_block=True
                )
                self._sizer.Add(self._replacement_block, 0, wx.TOP | wx.EXPAND, 10)

            def DoGetBestClientSize(self):
                sizer = self.GetSizer()
                if sizer is None:
                    return -1, -1
                else:
                    sx, sy = self.GetSizer().CalcMin()
                    return (
                        sx + wx.SystemSettings.GetMetric(wx.SYS_VSCROLL_X),
                        sy + wx.SystemSettings.GetMetric(wx.SYS_HSCROLL_Y),
                    )

        app = wx.App()

        dialog = wx.Dialog(None, style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER)
        sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        dialog.SetSizer(sizer_h)
        sizer_v = wx.BoxSizer(wx.VERTICAL)
        sizer_h.Add(sizer_v, 0, wx.EXPAND)
        sizer_v.Add(
            Replace(dialog),
            # BlockDefine(dialog, translation_manager, show_pick_block=True),
            0,
            wx.ALL | wx.EXPAND,
            5,
        )
        dialog.Show()
        dialog.Fit()

        def on_properties_change(evt):
            print("Properties changed:", evt.properties)

        dialog.Bind(EVT_PROPERTIES_CHANGE, on_properties_change)

        def on_layout_change(evt):
            dialog.Layout()
            evt.Skip()

        dialog.Bind(EVT_WIDGET_SIZE_CHANGED, on_layout_change)

        app.MainLoop()

    main()
