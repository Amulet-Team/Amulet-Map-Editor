import wx
from typing import Type, Any, Tuple

from amulet.api.data_types import BlockCoordinates
from amulet_map_editor.api.wx.ui.simple import SimplePanel
from amulet_map_editor.api.wx.util.validators import IntValidator
from amulet_map_editor.api import config
from .events import LocationChangeEvent, TransformChangeEvent


class SelectLocationUI(SimplePanel):
    """A UI element that can be dropped into the EditCanvas and let the user pick a location for a structure.
    This UI does not allow for rotation."""

    def __init__(self, parent: wx.Window):
        SimplePanel.__init__(self, parent)
        self._setup_ui()

    def _add_row(self, label: str, wx_object: Type[wx.Object], **kwargs) -> Any:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.add_object(sizer, 0, wx.ALIGN_CENTER_HORIZONTAL)
        name_text = wx.StaticText(self, label=label)
        sizer.Add(name_text, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        obj = wx_object(self, **kwargs)
        sizer.Add(obj, flag=wx.CENTER | wx.ALL, border=5)
        return obj

    def _setup_ui(self):
        self._x: wx.SpinCtrl = self._add_row(
            "x", wx.SpinCtrl, min=-30000000, max=30000000
        )
        self._y: wx.SpinCtrl = self._add_row(
            "y", wx.SpinCtrl, min=-30000000, max=30000000
        )
        self._z: wx.SpinCtrl = self._add_row(
            "z", wx.SpinCtrl, min=-30000000, max=30000000
        )
        for ui in (self._x, self._y, self._z):
            ui.SetValidator(IntValidator())

        self._x.Bind(wx.EVT_SPINCTRL, self._on_location_change)
        self._y.Bind(wx.EVT_SPINCTRL, self._on_location_change)
        self._z.Bind(wx.EVT_SPINCTRL, self._on_location_change)

        self._copy_air: wx.CheckBox = self._add_row("Copy Air", wx.CheckBox)
        copy_air = config.get("edit_select_location", {}).get("copy_air", False)
        self._copy_air.SetValue(copy_air)
        self._copy_air.Bind(wx.EVT_CHECKBOX, self._save_config)

        self._copy_water: wx.CheckBox = self._add_row("Copy Water", wx.CheckBox)
        copy_water = config.get("edit_select_location", {}).get("copy_water", True)
        self._copy_water.SetValue(copy_water)
        self._copy_water.Bind(wx.EVT_CHECKBOX, self._save_config)

        self._copy_lava: wx.CheckBox = self._add_row("Copy Lava", wx.CheckBox)
        copy_lava = config.get("edit_select_location", {}).get("copy_lava", True)
        self._copy_lava.SetValue(copy_lava)
        self._copy_lava.Bind(wx.EVT_CHECKBOX, self._save_config)

    @property
    def location(self) -> BlockCoordinates:
        return self._x.GetValue(), self._y.GetValue(), self._z.GetValue()

    @location.setter
    def location(self, location: Tuple[int, int, int]):
        x, y, z = location
        self._x.SetValue(x)
        self._y.SetValue(y)
        self._z.SetValue(z)

    @property
    def copy_air(self) -> bool:
        return self._copy_air.GetValue()

    @copy_air.setter
    def copy_air(self, copy_air: bool):
        self._copy_air.SetValue(copy_air)

    @property
    def copy_water(self) -> bool:
        return self._copy_water.GetValue()

    @copy_water.setter
    def copy_water(self, copy_water: bool):
        self._copy_water.SetValue(copy_water)

    @property
    def copy_lava(self) -> bool:
        return self._copy_lava.GetValue()

    @copy_lava.setter
    def copy_lava(self, copy_lava: bool):
        self._copy_lava.SetValue(copy_lava)

    def _save_config(self, evt):
        select_config = config.get("edit_select_location", {})
        select_config["copy_air"] = self.copy_air
        select_config["copy_water"] = self.copy_water
        select_config["copy_lava"] = self.copy_lava
        config.put("edit_select_location", select_config)

    def _on_location_change(self, evt):
        wx.PostEvent(self, LocationChangeEvent(self.location))
        self._on_transform_change()

    def _on_transform_change(self):
        """The object transform has been changed by the user. Sends"""
        wx.PostEvent(self, TransformChangeEvent(self.location, (0, 0, 0), (1, 1, 1)))
