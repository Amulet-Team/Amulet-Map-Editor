import wx
from typing import Dict, Tuple


from amulet.api.block import PropertyDataTypes, PropertyType, PropertyValueType
from .events import SinglePropertiesChangeEvent
from .base import BaseSingleProperty

StatesType = Dict[str, Tuple[Tuple[PropertyValueType, ...], int]]


class AutomaticSingleProperty(BaseSingleProperty):
    """
    A UI from which a user can choose one value for each property.

    The UI is automatically populated from the given specification.
    """

    _states: StatesType

    def __init__(
        self,
        parent: wx.Window,
    ):
        super().__init__(parent)

        self._property_sizer = wx.FlexGridSizer(2, 5, 5)
        label = wx.StaticText(self, label="Property Name", style=wx.ALIGN_CENTER)
        self._property_sizer.Add(label, 1, wx.ALIGN_CENTER)
        label = wx.StaticText(
            self, label="Property Value (SNBT)", style=wx.ALIGN_CENTER
        )
        self._property_sizer.Add(label, 1, wx.ALIGN_CENTER)

        self._sizer.Add(self._property_sizer, 1, wx.ALL | wx.EXPAND, 5)

        self._states: StatesType = {}
        self._properties: Dict[str, wx.Choice] = {}

    @property
    def states(self) -> StatesType:
        """
        A dictionary mapping the string property names to the valid states and the index of the default state.
        """
        return self._states

    @states.setter
    def states(self, states: StatesType):
        self._states = {}
        for key, (choices, default) in states.items():
            if isinstance(key, str):
                valid_choices = tuple(
                    choice
                    for choice in choices
                    if isinstance(choice, PropertyDataTypes)
                )
                if valid_choices:
                    self._states[key] = (
                        valid_choices,
                        default if default < len(valid_choices) else 0,
                    )
        self.Freeze()
        self._tear_down_properties()

        props = {}
        for name, (choices, default) in self._states.items():
            self._create_property(name, choices)
            props[name] = choices[default]
        self.properties = props
        self.Fit()
        self.GetTopLevelParent().Layout()
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

    def _post_change(self):
        wx.PostEvent(
            self,
            SinglePropertiesChangeEvent(self.properties),
        )

    def _create_property(self, name: str, choices: Tuple[PropertyValueType]):
        label = wx.StaticText(self, label=name)
        self._property_sizer.Add(label, 0, wx.ALIGN_CENTER)
        choice = wx.Choice(self, choices=[c.to_snbt() for c in choices])
        self._property_sizer.Add(choice, 0, wx.EXPAND)
        choice.Bind(
            wx.EVT_CHOICE,
            lambda evt: self._post_change(),
        )
        self._properties[name] = choice

    @property
    def properties(self) -> PropertyType:
        return {
            name: self._states[name][0][choice.GetSelection()]
            for name, choice in self._properties.items()
        }

    @properties.setter
    def properties(self, properties: PropertyType):
        is_frozen = self.IsFrozen()
        if not is_frozen:
            self.Freeze()
        for name, nbt in properties.items():
            if name in self._properties:
                if isinstance(nbt, PropertyDataTypes) and nbt in self._states[name][0]:
                    self._properties[name].SetSelection(
                        self._states[name][0].index(nbt)
                    )
                else:
                    self._properties[name].SetSelection(self._states[name][1])
        if not is_frozen:
            self.Thaw()
