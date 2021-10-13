import wx
from typing import Dict
from collections import namedtuple

import amulet_nbt
from amulet_nbt import SNBTType
from amulet.api.block import PropertyDataTypes, PropertyType
from amulet_map_editor import lang
from amulet_map_editor.api.image import ADD_ICON, SUBTRACT_ICON
from amulet_map_editor.api.wx.ui.mc.state import BlockState
from amulet_map_editor.api.wx.ui.events import ChildSizeEvent
from .base import BaseSingleProperty

PropertyStorage = namedtuple(
    "PropertyStorage", ("sizer", "key_entry", "value_entry", "snbt_text")
)


class BaseModdedSingleProperty(BaseSingleProperty):
    """
    A UI from which a user can choose one value for each property.

    This is used when the block is not know so the user can define the properties themselves.
    """

    state: BlockState
    _properties: Dict[int, PropertyStorage]

    def __init__(self, parent: wx.Window, state: BlockState):
        super().__init__(parent, state)
        header_sizer = wx.BoxSizer(wx.HORIZONTAL)
        add_button = wx.BitmapButton(
            self, bitmap=ADD_ICON.bitmap(30, 30), size=(30, 30)
        )
        header_sizer.Add(add_button)
        self._sizer.Add(header_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        label = wx.StaticText(
            self, label=lang.get("widget.mc.block.property.name"), style=wx.ALIGN_CENTER
        )
        header_sizer.Add(label, 1, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        label = wx.StaticText(
            self,
            label=lang.get("widget.mc.block.property.value"),
            style=wx.ALIGN_CENTER,
        )
        header_sizer.Add(label, 1, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        header_sizer.AddStretchSpacer(1)

        self._property_sizer = wx.BoxSizer(wx.VERTICAL)
        self._sizer.Add(
            self._property_sizer, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 5
        )

        add_button.Bind(wx.EVT_BUTTON, self._on_add_property)

        self._property_id = 0
        self._properties = {}

    def _resize(self):
        wx.PostEvent(self, ChildSizeEvent(0))

    def _rebuild_properties(self):
        self.Freeze()
        self._tear_down_properties()
        for name, prop in self.state.properties.items():
            self._create_property(name, prop.to_snbt())
        self.Fit()
        self.Thaw()

    def _tear_down_properties(self):
        self._property_sizer.Clear(True)
        self._properties.clear()
        self._property_id = 0

    def _create_property(self, name: str = "", value: SNBTType = ""):
        """
        Add a property to the UI with the given data.

        :param name: The name of the property.
        :param value: The SNBT text of the value for that property.
        :return:
        """
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._property_id += 1
        subtract_button = wx.BitmapButton(
            self, bitmap=SUBTRACT_ICON.bitmap(30, 30), size=(30, 30)
        )
        sizer.Add(subtract_button, 0, wx.ALIGN_CENTER_VERTICAL)
        property_id = self._property_id
        subtract_button.Bind(
            wx.EVT_BUTTON, lambda evt: self._on_remove_property(property_id)
        )
        name_entry = wx.TextCtrl(self, value=name, style=wx.TE_CENTER)
        sizer.Add(name_entry, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
        name_entry.Bind(wx.EVT_TEXT, self._on_key_change)
        value_entry = wx.TextCtrl(self, value=value, style=wx.TE_CENTER)
        sizer.Add(value_entry, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
        snbt_text = wx.StaticText(self, style=wx.ALIGN_CENTER)
        sizer.Add(snbt_text, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
        self._change_snbt_text(value, snbt_text)
        value_entry.Bind(
            wx.EVT_TEXT, lambda evt: self._on_value_change(evt, property_id)
        )

        self._property_sizer.Add(sizer, 1, wx.TOP | wx.EXPAND, 5)
        self._properties[self._property_id] = PropertyStorage(
            sizer, name_entry, value_entry, snbt_text
        )
        self.Layout()
        self._resize()

    def _update_properties(self):
        if self.state.properties != self._get_ui_properties():
            self._rebuild_properties()

    def _get_ui_properties(self) -> PropertyType:
        properties = {}
        for prop in self._properties.values():
            try:
                nbt = amulet_nbt.from_snbt(prop.value_entry.GetValue())
            except:
                continue
            name: str = prop.key_entry.GetValue()
            if name and isinstance(nbt, PropertyDataTypes):
                properties[name] = nbt
        return properties

    def _if_do_state_change(self) -> bool:
        return not self.state.is_supported

    def _on_key_change(self, evt):
        wx.CallAfter(self._on_property_change)
        evt.Skip()

    def _on_value_change(self, evt, property_id: int):
        self._change_snbt_text(evt.GetString(), self._properties[property_id].snbt_text)
        wx.CallAfter(self._on_property_change)
        evt.Skip()

    def _change_snbt_text(self, snbt: SNBTType, snbt_text: wx.StaticText):
        try:
            nbt = amulet_nbt.from_snbt(snbt)
        except:
            snbt_text.SetLabel(lang.get("widget.mc.block.property.invalid_snbt"))
            snbt_text.SetBackgroundColour((255, 200, 200))
        else:
            if isinstance(nbt, PropertyDataTypes):
                snbt_text.SetLabel(nbt.to_snbt())
                snbt_text.SetBackgroundColour(wx.NullColour)
            else:
                snbt_text.SetLabel(
                    lang.get("widget.mc.block.property.invalid_value_fstring").format(
                        val=nbt.__class__.__name__
                    )
                )
                snbt_text.SetBackgroundColour((255, 200, 200))
        self.Layout()

    def _on_add_property(self, evt):
        self._create_property()
        self._on_property_change()

    def _on_remove_property(self, property_id: int):
        property_state = self._properties.pop(property_id)
        self._property_sizer.Detach(property_state.sizer)
        property_state.sizer.Clear(True)
        self.Layout()
        self._resize()
        self._on_property_change()


class ModdedSingleProperty(BaseModdedSingleProperty):
    def __init__(self, parent: wx.Window, state: BlockState):
        super().__init__(parent, state)
        self._rebuild_properties()
