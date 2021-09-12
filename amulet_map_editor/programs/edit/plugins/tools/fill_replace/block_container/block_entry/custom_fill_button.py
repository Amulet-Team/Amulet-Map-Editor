import wx
from typing import Dict, Any, Tuple, Optional

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple
from amulet.api.block import PropertyType, PropertyValueType
from amulet_map_editor.api.wx.ui.mc.block import (
    BlockDefineButton,
    BlockDefine,
    SinglePropertySelect,
)
from amulet_map_editor.api.wx.ui.mc.block.properties.single.automatic import (
    AutomaticSingleProperty,
)


class CustomAutomaticSingleProperty(AutomaticSingleProperty):
    def __init__(
        self,
        parent: wx.Window,
        from_source: bool = False,
    ):
        self._from_source = from_source
        super().__init__(parent)
        label = wx.StaticText(self, label="src", style=wx.ALIGN_CENTER)
        self._property_sizer.SetCols(3)
        self._property_sizer.Add(label, 1, wx.ALIGN_CENTER)
        label.Show(from_source)
        self._property_sizer.AddGrowableCol(0)
        self._property_sizer.AddGrowableCol(1)
        self._check_boxes: Dict[str, wx.CheckBox] = {}

    def _tear_down_properties(self):
        self._check_boxes.clear()
        super()._tear_down_properties()

    def _create_property(self, name: str, choices: Tuple[PropertyValueType]):
        super()._create_property(name, choices)
        check_box = wx.CheckBox(self)
        self._property_sizer.Add(check_box, 1, wx.ALIGN_CENTER)
        self._check_boxes[name] = check_box
        check_box.Bind(wx.EVT_CHECKBOX, lambda evt: self._post_change())
        check_box.Show(self._from_source)

    def set_from_source(self, from_source: bool):
        self._from_source = from_source
        for i in range(0, self._property_sizer.GetItemCount(), self._property_sizer.GetCols()):
            self._property_sizer.Show(i+2, show=from_source)
        self.Layout()


class CustomSinglePropertySelect(SinglePropertySelect):
    _simple: CustomAutomaticSingleProperty

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str,
        version_number: VersionNumberTuple,
        force_blockstate: bool,
        namespace: str = None,
        base_name: str = None,
        properties: PropertyType = None,
        state: Dict[str, Any] = None,
        from_source: bool = False,
    ):
        self._from_source = from_source
        super().__init__(
            parent,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
            properties,
            state=state
        )

    def _create_automatic(self) -> CustomAutomaticSingleProperty:
        prop = CustomAutomaticSingleProperty(self, from_source=self._from_source)
        return prop

    def set_from_source(self, from_source: bool):
        self._simple.set_from_source(from_source)


class CustomBlockDefine(BlockDefine):
    _property_picker: CustomSinglePropertySelect

    def __init__(self, *args, from_source: bool = False, **kwargs):
        self._from_source = from_source
        super().__init__(*args, **kwargs)

    def _create_properties(self) -> SinglePropertySelect:
        return CustomSinglePropertySelect(
            self,
            self._translation_manager,
            self.platform,
            self.version_number,
            self.force_blockstate,
            self.namespace,
            self.base_name,
            self.properties,
            from_source=self._from_source
        )

    def set_from_source(self, from_source: bool):
        self._from_source = from_source
        self._property_picker.set_from_source(from_source)


class CustomBlockDefineButton(BlockDefineButton):
    _block_widget: Optional[CustomBlockDefine]

    def __init__(self, *args, from_source: bool = False, **kwargs):
        self._from_source = from_source
        super().__init__(*args, **kwargs)

    def _create_block_define(self, dialog: wx.Dialog) -> BlockDefine:
        return CustomBlockDefine(
            dialog,
            self._translation_manager,
            wx.HORIZONTAL,
            self.platform,
            self.version_number,
            self.force_blockstate,
            self.namespace,
            self.base_name,
            self.properties,
            from_source=self._from_source
        )

    def _update_from_block_define(self, block_define: BlockDefine):
        super()._update_from_block_define(block_define)

    # @property
    # def from_source(self) -> Dict[str, bool]:

    def set_from_source(self, from_source: bool):
        self._from_source = from_source
        if self._block_widget is not None:
            self._block_widget.set_from_source(from_source)
