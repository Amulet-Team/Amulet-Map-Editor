import wx
from typing import Tuple, Dict

import amulet_nbt
from amulet_nbt import SNBTType
from amulet.api.block import PropertyDataTypes, PropertyType, PropertyTypeMultiple
from amulet_map_editor.api.image import ADD_ICON, SUBTRACT_ICON
from .events import MultiplePropertiesChangeEvent
from .base import BaseMultipleProperty


class ModdedMultipleProperty(BaseMultipleProperty):
    def __init__(self, parent: wx.Window):
        super().__init__(parent)
        header_sizer = wx.BoxSizer(wx.HORIZONTAL)
        add_button = wx.BitmapButton(
            self, bitmap=ADD_ICON.bitmap(30, 30), size=(30, 30)
        )
        header_sizer.Add(add_button)
        self._sizer.Add(header_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        label = wx.StaticText(self, label="Property Name", style=wx.ALIGN_CENTER)
        header_sizer.Add(label, 1, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        label = wx.StaticText(
            self, label="Property Value (SNBT)", style=wx.ALIGN_CENTER
        )
        header_sizer.Add(label, 1, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        header_sizer.AddStretchSpacer(1)

        self._property_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(
            self._property_sizer, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 5
        )

        add_button.Bind(wx.EVT_BUTTON, lambda evt: self._add_property())

        self._property_index = 0
        self._properties: Dict[int, Tuple[wx.TextCtrl, wx.TextCtrl]] = {}

    def _post_property_change(self):
        wx.PostEvent(self, MultiplePropertiesChangeEvent(self.selected_properties))

    def _add_property(self, name: str = "", value: SNBTType = ""):
        self.Freeze()
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._property_index += 1
        subtract_button = wx.BitmapButton(
            self, bitmap=SUBTRACT_ICON.bitmap(30, 30), size=(30, 30)
        )
        sizer.Add(subtract_button, 0, wx.ALIGN_CENTER_VERTICAL)
        index = self._property_index
        subtract_button.Bind(
            wx.EVT_BUTTON, lambda evt: self._on_remove_property(sizer, index)
        )
        name_entry = wx.TextCtrl(self, value=name, style=wx.TE_CENTER)
        sizer.Add(name_entry, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
        name_entry.Bind(wx.EVT_TEXT, lambda evt: self._post_property_change())
        value_entry = wx.TextCtrl(self, value=value, style=wx.TE_CENTER)
        sizer.Add(value_entry, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
        snbt_text = wx.StaticText(self, style=wx.ALIGN_CENTER)
        sizer.Add(snbt_text, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
        self._change_value(value, snbt_text)
        value_entry.Bind(wx.EVT_TEXT, lambda evt: self._on_value_change(evt, snbt_text))

        self._property_sizer.Add(sizer, 1, wx.TOP | wx.EXPAND, 5)
        self._properties[self._property_index] = (name_entry, value_entry)
        self.Fit()
        self.TopLevelParent.Layout()
        self.Thaw()

    def _on_value_change(self, evt, snbt_text: wx.StaticText):
        self._change_value(evt.GetString(), snbt_text)
        self._post_property_change()
        evt.Skip()

    def _change_value(self, snbt: SNBTType, snbt_text: wx.StaticText):
        try:
            nbt = amulet_nbt.from_snbt(snbt)
        except:
            snbt_text.SetLabel("Invalid SNBT")
            snbt_text.SetBackgroundColour((255, 200, 200))
        else:
            if isinstance(nbt, PropertyDataTypes):
                snbt_text.SetLabel(nbt.to_snbt())
                snbt_text.SetBackgroundColour(wx.NullColour)
            else:
                snbt_text.SetLabel(f"{nbt.__class__.__name__} not valid")
                snbt_text.SetBackgroundColour((255, 200, 200))
        self.Layout()

    def _on_remove_property(self, sizer: wx.Sizer, key: int):
        self.Freeze()
        self._property_sizer.Detach(sizer)
        sizer.Clear(True)
        del self._properties[key]
        self.TopLevelParent.Layout()
        self.Thaw()
        self._post_property_change()

    @property
    def properties(self) -> PropertyType:
        properties = {}
        for name_ui, value_ui in self._properties.values():
            try:
                nbt = amulet_nbt.from_snbt(value_ui.GetValue())
            except:
                continue
            name: str = name_ui.GetValue()
            if name and isinstance(nbt, PropertyDataTypes):
                properties[name] = nbt
        return properties

    @properties.setter
    def properties(self, properties: PropertyType):
        self._property_sizer.Clear(True)
        self._properties.clear()
        self._property_index = 0
        for name, value in properties.items():
            self._add_property(name, value.to_snbt())

    @property
    def all_properties(self) -> PropertyTypeMultiple:
        return {prop: (val,) for prop, val in self.properties.items()}

    @all_properties.setter
    def all_properties(self, all_properties: PropertyTypeMultiple):
        props = {}
        for prop, val in all_properties.items():
            if val:
                props[prop] = val[0]
        self.properties = props

    # TODO: implement this properly
    @property
    def selected_properties(self) -> PropertyTypeMultiple:
        return {prop: (val,) for prop, val in self.properties.items()}

    @selected_properties.setter
    def selected_properties(self, properties: PropertyTypeMultiple):
        props = {}
        for prop, val in properties.items():
            if val:
                props[prop] = val[0]
        self.properties = props
