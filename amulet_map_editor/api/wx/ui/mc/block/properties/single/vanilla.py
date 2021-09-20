import wx
from typing import Dict, Tuple

from amulet.api.block import PropertyType, PropertyValueType
from amulet_map_editor.api.wx.ui.mc.state import BlockState, State
from amulet_map_editor.api.wx.ui.simple import ChoiceRaw
from .base import BaseSingleProperty


class BaseVanillaSingleProperty(BaseSingleProperty):
    """
    A UI from which a user can choose one value for each property.

    The UI is automatically populated from the given specification.
    """

    state: BlockState

    def __init__(self, parent: wx.Window, state: BlockState):
        super().__init__(parent, state)

        self._property_sizer = wx.FlexGridSizer(2, 5, 5)
        label = wx.StaticText(self, label="Property Name", style=wx.ALIGN_CENTER)
        self._property_sizer.Add(label, 1, wx.ALIGN_CENTER)
        label = wx.StaticText(
            self, label="Property Value (SNBT)", style=wx.ALIGN_CENTER
        )
        self._property_sizer.Add(label, 1, wx.ALIGN_CENTER)

        self._sizer.Add(self._property_sizer, 1, wx.ALL | wx.EXPAND, 5)

        self._properties: Dict[str, ChoiceRaw] = {}

    def _rebuild_properties(self):
        self.Freeze()
        self._tear_down_properties()
        for name, choices in self.state.valid_properties.items():
            self._create_property(name, choices)
        self.Fit()
        self.Thaw()

    def _tear_down_properties(self):
        self._properties.clear()
        child: wx.SizerItem
        for i, child in enumerate(self._property_sizer.GetChildren()):
            if i >= self._property_sizer.GetCols():
                if child.IsWindow():
                    child.GetWindow().Destroy()
                elif child.IsSizer():
                    child.GetSizer().Clear(True)
                    self._property_sizer.Remove(self._property_sizer.GetCols())
                elif child.IsSpacer():
                    self._property_sizer.Remove(self._property_sizer.GetCols())
                else:
                    raise Exception

    def _update_properties(self):
        for name, nbt in self.state.properties.items():
            property_ui = self._properties[name]
            property_ui.SetSelection(property_ui.SetObject(nbt))

    def _on_state_change(self):
        if self.state.base_name in self.state.valid_base_names:
            if self.state.is_changed(State.BaseName):
                self._rebuild_properties()
            elif self.state.is_changed(State.Properties):
                self._update_properties()

    def _on_property_change(self, evt):
        properties = self._get_ui_properties()
        if properties != self.state.properties:
            with self.state as state:
                state.properties = properties

    def _create_property(self, name: str, choices: Tuple[PropertyValueType]):
        label = wx.StaticText(self, label=name)
        self._property_sizer.Add(label, 0, wx.ALIGN_CENTER)
        choice = ChoiceRaw(self, choices=[c.to_snbt() for c in choices])
        self._property_sizer.Add(choice, 0, wx.EXPAND)
        choice.Bind(
            wx.EVT_CHOICE,
            self._on_property_change,
        )
        self._properties[name] = choice

    def _get_ui_properties(self) -> PropertyType:
        return {
            name: choice.GetCurrentObject() for name, choice in self._properties.items()
        }


class VanillaSingleProperty(BaseVanillaSingleProperty):
    def __init__(self, parent: wx.Window, state: BlockState):
        super().__init__(parent, state)
        self._rebuild_properties()
