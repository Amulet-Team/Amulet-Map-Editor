import wx
from typing import Dict, Tuple

from amulet.api.block import PropertyTypeMultiple, PropertyDataTypes
from ..events import MultiplePropertiesChangeEvent
from ..base import BaseMultipleProperty
from .popup import PropertyValueComboPopup


class AutomaticMultipleProperty(BaseMultipleProperty):
    def __init__(self, parent: wx.Window):
        super().__init__(parent)

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

    @property
    def all_properties(self) -> PropertyTypeMultiple:
        return self._states

    @all_properties.setter
    def all_properties(self, all_properties: PropertyTypeMultiple):
        self._states = {}
        for key, choices in all_properties.items():
            if isinstance(key, str):
                valid_choices = tuple(
                    choice
                    for choice in choices
                    if isinstance(choice, PropertyDataTypes)
                )
                if valid_choices:
                    self._states[key] = valid_choices
        self.Freeze()
        self._properties.clear()
        self._property_sizer.Clear(True)

        props = {}
        for name, choices in self._states.items():
            label = wx.StaticText(self, label=name)
            self._property_sizer.Add(label, 0, wx.ALIGN_CENTER)

            def create_choice():
                choice = wx.ComboCtrl(self, style=wx.CB_READONLY)
                popup = PropertyValueComboPopup([c.to_snbt() for c in choices])
                choice.SetPopupControl(popup)
                choice.SetValue(popup.GetStringValue())

                self._property_sizer.Add(choice, 0, wx.EXPAND)

                def on_close(evt):
                    choice.SetValue(popup.GetStringValue())
                    wx.PostEvent(
                        self,
                        MultiplePropertiesChangeEvent(self.selected_properties),
                    )

                choice.Bind(
                    wx.EVT_COMBOBOX_CLOSEUP,
                    on_close,
                )
                self._properties[name] = (choice, popup)

            create_choice()
            props[name] = choices
        self.selected_properties = props
        self.Fit()
        self.GetTopLevelParent().Layout()
        self.Thaw()

    @property
    def selected_properties(self) -> PropertyTypeMultiple:
        """
        The values that are checked for each property.
        This UI can have more than one property value checked (ticked).
        """
        return {
            prop: popup.checked_nbt for prop, (_, popup) in self._properties.items()
        }

    @selected_properties.setter
    def selected_properties(self, properties: PropertyTypeMultiple):
        self.Freeze()
        for name, nbt_tuple in properties.items():
            if name in self._properties:
                choice, popup = self._properties[name]
                popup.checked_nbt = nbt_tuple
                choice.SetValue(popup.GetStringValue())
        self.Thaw()
