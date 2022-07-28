import wx
from typing import Dict, Any, Tuple, Optional
from enum import Enum

from PyMCTranslate import TranslationManager
from amulet.api.block import PropertyValueType
from amulet_map_editor.api.wx.ui.mc.state import BlockState, StrEnum, State
from amulet_map_editor.api.wx.ui.mc.block import (
    BlockDefineButton,
    BlockDefine,
    SinglePropertySelect,
)
from amulet_map_editor.api.wx.ui.mc.block.properties.single.vanilla import (
    BaseVanillaSingleProperty,
)


class StateExtra(StrEnum, Enum):
    FromSrc = "from_src"


FromSrcType = Dict[str, bool]


class SrcBlockState(BlockState):
    def __init__(
        self,
        translation_manager: TranslationManager,
        *,
        from_source: FromSrcType = None,
        **kwargs,
    ):
        super().__init__(translation_manager, **kwargs)
        self._state[StateExtra.FromSrc] = self._sanitise_from_source(from_source)

    def _fix_new_state(self):
        super()._fix_new_state()
        self._state[StateExtra.FromSrc] = self._sanitise_from_source(self.from_source)

    def _sanitise_from_source(self, from_source: FromSrcType = None) -> FromSrcType:
        if not isinstance(from_source, dict):
            from_source = {}
        return {
            key: bool(from_source.get(key, True))
            for key in self.valid_properties.keys()
        }

    @property
    def from_source(self) -> FromSrcType:
        """Should the value for this property be driven by the source block."""
        return self._get_state(StateExtra.FromSrc)

    @from_source.setter
    def from_source(self, from_source: FromSrcType):
        self._set_state(StateExtra.FromSrc, from_source)


class CustomVanillaSingleProperty(BaseVanillaSingleProperty):
    """A modification of the normal vanilla property that adds a check box for each property."""

    state: SrcBlockState

    def __init__(
        self,
        parent: wx.Window,
        state: SrcBlockState,
        *,
        show_from_source: bool = False,
    ):
        assert isinstance(state, SrcBlockState)
        super().__init__(parent, state)
        self._show_from_source = show_from_source
        label = wx.StaticText(self, label="src", style=wx.ALIGN_CENTER)
        self._property_sizer.SetCols(3)
        self._property_sizer.Add(label, 1, wx.ALIGN_CENTER)
        label.Show(show_from_source)
        self._property_sizer.AddGrowableCol(0)
        self._property_sizer.AddGrowableCol(1)
        self._check_boxes: Dict[str, wx.CheckBox] = {}
        self._rebuild_properties()

    def _tear_down_properties(self):
        self._check_boxes.clear()
        super()._tear_down_properties()

    def _create_property(
        self,
        name: str,
        choices: Tuple[PropertyValueType, ...],
        default: PropertyValueType = None,
    ):
        super()._create_property(name, choices, default)
        check_box = wx.CheckBox(self)
        self._property_sizer.Add(check_box, 1, wx.ALIGN_CENTER)
        self._check_boxes[name] = check_box
        check_box.Bind(wx.EVT_CHECKBOX, lambda evt: self._on_src_change())
        check_box.Show(self._show_from_source)

    def show_from_source(self, show_from_source: bool):
        self._show_from_source = show_from_source
        for i in range(
            0, self._property_sizer.GetItemCount(), self._property_sizer.GetCols()
        ):
            self._property_sizer.Show(i + 2, show=show_from_source)
        self.Layout()

    def _get_ui_src(self) -> FromSrcType:
        return {
            key: check_box.GetValue() for key, check_box in self._check_boxes.items()
        }

    def _on_src_change(self):
        from_source = self._get_ui_src()
        if from_source != self.state.from_source:
            with self.state as state:
                state.from_source = from_source
            # wx.PostEvent(self, SinglePropertiesChangeEvent(self.state.from_source))

    def _on_state_change(self):
        super()._on_state_change()
        if self.state.is_changed(State.Properties) or self.state.is_changed(
            StateExtra.FromSrc
        ):
            if self.state.from_source != self._get_ui_src():
                for key, val in self.state.from_source.items():
                    self._check_boxes[key].SetValue(val)


class CustomSinglePropertySelect(SinglePropertySelect):
    _vanilla: CustomVanillaSingleProperty
    state: SrcBlockState

    def __init__(
        self,
        parent: wx.Window,
        state: SrcBlockState,
        *,
        show_from_source: bool = False,
    ):
        self._show_from_source = show_from_source
        super().__init__(
            parent,
            state,
        )

    def _create_automatic(self) -> CustomVanillaSingleProperty:
        return CustomVanillaSingleProperty(
            self, self.state, show_from_source=self._show_from_source
        )

    def show_from_source(self, show_from_source: bool):
        self._vanilla.show_from_source(show_from_source)


class CustomBlockDefine(BlockDefine):
    _property_picker: CustomSinglePropertySelect
    state: SrcBlockState

    def __init__(self, *args, show_from_source: bool = False, **kwargs):
        self._show_from_source = show_from_source
        super().__init__(*args, **kwargs)

    def _create_property_picker(self) -> SinglePropertySelect:
        return CustomSinglePropertySelect(
            self,
            self.state,
            show_from_source=self._show_from_source,
        )

    def show_from_source(self, show_from_source: bool):
        self._show_from_source = show_from_source
        self._property_picker.show_from_source(show_from_source)


class CustomBlockDefineButton(BlockDefineButton):
    _block_widget: Optional[CustomBlockDefine]

    def __init__(
        self,
        parent: wx.Window,
        state: BlockState,
        *,
        show_from_source: bool = False,
        **kwargs,
    ):
        self._show_from_source = show_from_source
        super().__init__(parent, state, **kwargs)

    def _create_block_define(self, dialog: wx.Dialog) -> BlockDefine:
        return CustomBlockDefine(
            dialog,
            self.state.copy(),
            orientation=wx.HORIZONTAL,
            show_from_source=self._show_from_source,
        )

    def show_from_source(self, show_from_source: bool):
        self._show_from_source = show_from_source
        if self._block_widget is not None:
            self._block_widget.show_from_source(show_from_source)
