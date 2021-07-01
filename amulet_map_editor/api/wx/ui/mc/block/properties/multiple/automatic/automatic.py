import wx
from typing import Dict, List, Tuple

import PyMCTranslate
from amulet.api.block import PropertyTypeMultiple
from ..events import MultiplePropertiesChangeEvent
from ..base import BaseMultipleProperty
from .popup import PropertyValueComboPopup


class AutomaticMultipleProperty(BaseMultipleProperty):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
    ):
        super().__init__(parent, translation_manager)

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

        self._properties: Dict[str, Tuple[wx.ComboCtrl, PropertyValueComboPopup]] = {}
        self._specification: dict = {}

    def rebuild_ui(self, specification: dict):
        """
        Rebuild the UI.
        Run when the version or block is changed.
        """
        self._specification = specification
        self.Freeze()
        self._properties.clear()
        self._property_sizer.Clear(True)
        spec_properties: Dict[str, List[str]] = self._specification.get(
            "properties", {}
        )

        for name, choices in spec_properties.items():
            label = wx.StaticText(self, label=name)
            self._property_sizer.Add(label, 0, wx.ALIGN_CENTER)

            def create_choice():
                choice = wx.ComboCtrl(self, style=wx.CB_READONLY)
                popup = PropertyValueComboPopup(choices)
                choice.SetPopupControl(popup)
                choice.SetValue(popup.GetStringValue())

                self._property_sizer.Add(choice, 0, wx.EXPAND)

                def on_close(evt):
                    choice.SetValue(popup.GetStringValue())
                    wx.PostEvent(
                        self,
                        MultiplePropertiesChangeEvent(self.extra_properties),
                    )

                choice.Bind(
                    wx.EVT_COMBOBOX_CLOSEUP,
                    on_close,
                )
                self._properties[name] = (choice, popup)

            create_choice()
        self.Fit()
        self.GetTopLevelParent().Layout()
        self.Thaw()

    @property
    def extra_properties(self) -> PropertyTypeMultiple:
        """
        The values that are checked for each property.
        This UI can have more than one property value checked (ticked).
        """
        return {
            prop: popup.checked_nbt for prop, (_, popup) in self._properties.items()
        }

    @extra_properties.setter
    def extra_properties(self, properties: PropertyTypeMultiple):
        self.Freeze()
        for name, nbt_tuple in properties.items():
            if name in self._properties:
                choice, popup = self._properties[name]
                popup.checked_nbt = nbt_tuple
                choice.SetValue(popup.GetStringValue())
        self.Thaw()
