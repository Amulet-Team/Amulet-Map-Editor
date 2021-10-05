import wx
from typing import Dict, Tuple

import amulet_nbt
from amulet.api.block import PropertyTypeMultiple, PropertyValueType
from amulet_map_editor.api.wx.ui.mc.state import BlockState
from ..base import BaseMultipleProperty
from .popup import PropertyValueComboPopup


class BaseVanillaMultipleProperty(BaseMultipleProperty):
    """
    A UI from which a user can choose zero or more values for each property.

    The UI is automatically populated from the given specification.
    """

    state: BlockState

    def __init__(self, parent: wx.Window, state: BlockState):
        super().__init__(parent, state)

        header_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._sizer.Add(header_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        label = wx.StaticText(self, label="Property Name", style=wx.ALIGN_CENTER)
        header_sizer.Add(label, 1)
        label = wx.StaticText(
            self, label="Property Value (SNBT)", style=wx.ALIGN_CENTER
        )
        header_sizer.Add(label, 1, wx.LEFT, 5)
        self._property_sizer = wx.GridSizer(2, 5, 5)
        self._sizer.Add(self._property_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self._states: PropertyTypeMultiple = {}
        self._properties: Dict[str, Tuple[wx.ComboCtrl, PropertyValueComboPopup]] = {}

    def _rebuild_properties(self):
        self._tear_down_properties()
        valid_properties = self.state.valid_properties
        current_properties = self.state.properties_multiple
        for name in valid_properties:
            self._create_property(
                name, valid_properties[name], current_properties[name]
            )
        self.Fit()
        self.Layout()

    def _tear_down_properties(self):
        self._properties.clear()
        self._property_sizer.Clear(True)

    def _create_property(
        self,
        name: str,
        choices: Tuple[PropertyValueType, ...],
        selected: Tuple[PropertyValueType, ...] = None,
    ):
        label = wx.StaticText(self, label=name)
        self._property_sizer.Add(label, 0, wx.ALIGN_CENTER)

        choice = wx.ComboCtrl(self, style=wx.CB_READONLY)
        if selected is None:
            selected = [bool] * len(choices)
        else:
            selected = [c in choices for c in selected]
        popup = PropertyValueComboPopup([c.to_snbt() for c in choices], selected)
        choice.SetPopupControl(popup)
        choice.SetValue(popup.GetStringValue())
        self._property_sizer.Add(choice, 0, wx.EXPAND)

        def on_closeup(evt):
            choice.SetValue(popup.GetStringValue())
            self._on_property_change()

        choice.Bind(wx.EVT_COMBOBOX_CLOSEUP, on_closeup)
        self._properties[name] = (choice, popup)

    def _update_properties(self):
        for name, choices in self.state.properties_multiple.items():
            property_ui = self._properties[name][1]
            property_ui.SetCheckedStrings([c.to_snbt() for c in choices])

    def _get_ui_properties_multiple(self) -> PropertyTypeMultiple:
        return {
            prop: tuple(amulet_nbt.from_snbt(v) for v in popup.GetCheckedStrings())
            for prop, (_, popup) in self._properties.items()
        }

    def _if_do_state_change(self) -> bool:
        return self.state.is_supported


class VanillaMultipleProperty(BaseVanillaMultipleProperty):
    def __init__(self, parent: wx.Window, state: BlockState):
        super().__init__(parent, state)
        self._rebuild_properties()
