import wx
from typing import Dict, List

import PyMCTranslate
from amulet.api.block import PropertyDataTypes, PropertyType
from ...events import PropertiesChangeEvent
from ..base import BaseSubWildcardPropertySelect
from .popup import PropertyValueComboPopup


class SimpleWildcardPropertySelect(BaseSubWildcardPropertySelect):
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

        self._properties: Dict[str, PropertyValueComboPopup] = {}
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
                l = PropertyValueComboPopup(choices)
                choice.SetPopupControl(l)
                choice.SetValue(l.GetStringValue())

                self._property_sizer.Add(choice, 0, wx.EXPAND)

                def on_close(evt):
                    choice.SetValue(l.GetStringValue())
                    wx.PostEvent(
                        self,
                        PropertiesChangeEvent(self.GetId(), properties=self.properties),
                    )

                choice.Bind(
                    wx.EVT_COMBOBOX_CLOSEUP,
                    on_close,
                )
                self._properties[name] = l

            create_choice()
        self.properties = self._specification.get("defaults", {})
        self.Fit()
        self.GetTopLevelParent().Layout()
        self.Thaw()

    @property
    def properties(self) -> PropertyType:
        return {
            # name: amulet_nbt.from_snbt(choice.GetString(choice.GetSelection()))
            # for name, choice in self._properties.items()
        }

    @properties.setter
    def properties(self, properties: PropertyType):
        self.Freeze()
        for name, nbt in properties.items():
            if name in self._properties:
                if isinstance(nbt, PropertyDataTypes):
                    snbt = nbt.to_snbt()
                elif isinstance(nbt, str):
                    snbt = nbt
                else:
                    continue
                choice = self._properties[name]
                # index = choice.FindString(snbt)
                # if index != wx.NOT_FOUND:
                #     choice.SetSelection(index)
        self.Thaw()
