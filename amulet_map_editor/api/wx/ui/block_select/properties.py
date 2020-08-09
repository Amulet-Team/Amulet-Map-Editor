import wx
from wx.lib import newevent
from typing import Tuple, Dict, Optional, List, Union
import weakref

import PyMCTranslate
import amulet_nbt
from amulet_nbt import SNBTType
from amulet.api.block import PropertyDataTypes, PropertyType

WildcardSNBTType = Union[SNBTType, str]

from amulet_map_editor.api.image import ADD_ICON, SUBTRACT_ICON

(
    PropertiesChangeEvent,
    EVT_PROPERTIES_CHANGE,
) = newevent.NewCommandEvent()  # the properties changed


class PropertySelect(wx.Panel):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str,
        version_number: Tuple[int, int, int],
        force_blockstate: bool,
        namespace: str,
        block_name: str,
        properties: Dict[str, SNBTType] = None,
        wildcard_mode=False,
    ):
        super().__init__(parent, style=wx.BORDER_SIMPLE)
        self._parent = weakref.ref(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self._translation_manager = translation_manager

        self._platform: Optional[str] = None
        self._version_number: Optional[Tuple[int, int, int]] = None
        self._force_blockstate: Optional[bool] = None
        self._namespace: Optional[str] = None
        self._block_name: Optional[str] = None

        self._manual_enabled = False
        self._simple = SimplePropertySelect(self, translation_manager, wildcard_mode)
        sizer.Add(self._simple, 1, wx.EXPAND)
        self._manual = ManualPropertySelect(self, translation_manager)
        sizer.Add(self._manual, 1, wx.EXPAND)

        self._wildcard_mode = wildcard_mode

        self._set_version_block(
            (platform, version_number, force_blockstate, namespace, block_name)
        )
        self.set_properties(properties)

    @property
    def parent(self) -> wx.Window:
        return self._parent()

    @property
    def wildcard_mode(self) -> bool:
        return self._wildcard_mode

    @property
    def version_block(self) -> Tuple[str, Tuple[int, int, int], bool, str, str]:
        return (
            self._platform,
            self._version_number,
            self._force_blockstate,
            self._namespace,
            self._block_name,
        )

    @version_block.setter
    def version_block(
        self, version_block: Tuple[str, Tuple[int, int, int], bool, str, str]
    ):
        self._set_version_block(version_block)
        self.str_properties = None

    def _set_version_block(
        self, version_block: Tuple[str, Tuple[int, int, int], bool, str, str]
    ):
        version = version_block[:3]
        assert (
            version[0] in self._translation_manager.platforms()
            and version[1] in self._translation_manager.version_numbers(version[0])
            and isinstance(version[2], bool)
        ), f"{version} is not a valid version"
        self._platform, self._version_number, self._force_blockstate = version
        block = version_block[3:5]
        assert isinstance(block[0], str) and isinstance(
            block[1], str
        ), "The block namespace and block name must be strings"
        self._namespace, self._block_name = block
        self._set_ui()

    @property
    def str_properties(self) -> Dict[str, WildcardSNBTType]:
        if self._manual_enabled:
            return self._manual.properties
        else:
            return self._simple.properties

    @str_properties.setter
    def str_properties(self, properties: Dict[str, WildcardSNBTType]):
        self.set_properties(properties)
        wx.PostEvent(
            self, PropertiesChangeEvent(self.GetId(), properties=self.str_properties)
        )

    @property
    def properties(self) -> PropertyType:
        if self.wildcard_mode:
            raise Exception(
                "Accessing the properties attribute is invalid in wildcard mode"
            )
        return {
            key: amulet_nbt.from_snbt(val) for key, val in self.str_properties.items()
        }

    @properties.setter
    def properties(self, properties: PropertyType):
        self.str_properties = {
            key: val.to_snbt() for key, val in (properties or {}).items()
        }

    def set_properties(self, properties: Dict[str, SNBTType]):
        properties = properties or {}
        self.Freeze()
        if self._manual_enabled:
            self._manual.properties = properties
        else:
            self._simple.properties = properties
        self.TopLevelParent.Layout()
        self.Thaw()

    def _set_ui(self):
        self.Freeze()
        translator = self._translation_manager.get_version(
            self._platform, self._version_number
        ).block

        self._manual_enabled = self._block_name not in translator.base_names(
            self._namespace, self._force_blockstate
        )
        if self._manual_enabled:
            self._simple.Hide()
            self._manual.Show()
        else:
            self._simple.Show()
            self._simple.set_specification(
                translator.get_specification(
                    self._namespace, self._block_name, self._force_blockstate
                )
            )
            self._manual.Hide()
        self.Thaw()


class SimplePropertySelect(wx.Panel):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        wildcard_mode,
    ):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self._translation_manager = translation_manager

        header_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(header_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        label = wx.StaticText(self, label="Property Name", style=wx.ALIGN_CENTER)
        header_sizer.Add(label, 1)
        label = wx.StaticText(
            self, label="Property Value (SNBT)", style=wx.ALIGN_CENTER
        )
        header_sizer.Add(label, 1, wx.LEFT, 5)
        self._property_sizer = wx.GridSizer(2, 5, 5)
        sizer.Add(self._property_sizer, 0, wx.ALL | wx.EXPAND, 5)

        self._properties: Dict[str, wx.Choice] = {}
        self._specification: dict = {}
        self._wildcard_mode = wildcard_mode

    def set_specification(self, specification: dict):
        self._specification = specification

    @property
    def properties(self) -> Dict[str, SNBTType]:
        return {
            name: choice.GetString(choice.GetSelection())
            for name, choice in self._properties.items()
        }

    @properties.setter
    def properties(self, properties: Dict[str, SNBTType]):
        self.Freeze()
        self._properties.clear()
        self._property_sizer.Clear(True)
        spec_properties: Dict[str, List[str]] = self._specification.get(
            "properties", {}
        )
        spec_defaults = self._specification.get("defaults", {})

        for name, choices in spec_properties.items():
            label = wx.StaticText(self, label=name)
            self._property_sizer.Add(label, 0, wx.ALIGN_CENTER)
            if self._wildcard_mode:
                choices = ["*"] + choices
            choice = wx.Choice(self, choices=choices)
            self._property_sizer.Add(choice, 0, wx.EXPAND)
            choice.Bind(
                wx.EVT_CHOICE,
                lambda evt: wx.PostEvent(
                    self,
                    PropertiesChangeEvent(self.GetId(), properties=self.properties),
                ),
            )
            val = spec_defaults[name]
            if name in properties and val != "*":
                try:
                    snbt = amulet_nbt.from_snbt(properties[name]).to_snbt()
                except:
                    pass
                else:
                    if snbt in choices:
                        val = snbt
            if val in choices:
                choice.SetSelection(choices.index(val))
            self._properties[name] = choice
        self.Thaw()
        self.Fit()
        self.Layout()


class ManualPropertySelect(wx.Panel):
    def __init__(
        self, parent: wx.Window, translation_manager: PyMCTranslate.TranslationManager
    ):
        super().__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self._translation_manager = translation_manager

        header_sizer = wx.BoxSizer(wx.HORIZONTAL)
        add_button = wx.BitmapButton(
            self, bitmap=ADD_ICON.bitmap(30, 30), size=(30, 30)
        )
        header_sizer.Add(add_button)
        sizer.Add(header_sizer, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)
        label = wx.StaticText(self, label="Property Name", style=wx.ALIGN_CENTER)
        header_sizer.Add(label, 1, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        label = wx.StaticText(
            self, label="Property Value (SNBT)", style=wx.ALIGN_CENTER
        )
        header_sizer.Add(label, 1, wx.LEFT | wx.ALIGN_CENTER_VERTICAL, 5)
        header_sizer.AddStretchSpacer(1)

        self._property_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(
            self._property_sizer, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 5
        )

        add_button.Bind(wx.EVT_BUTTON, lambda evt: self._add_property())

        self._property_index = 0
        self._properties: Dict[int, Tuple[wx.TextCtrl, wx.TextCtrl]] = {}

    def _post_property_change(self):
        wx.PostEvent(
            self, PropertiesChangeEvent(self.GetId(), properties=self.properties)
        )

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
        self._change_value("", snbt_text)
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
    def properties(self) -> Dict[str, SNBTType]:
        properties = {}
        for name, value in self._properties.values():
            try:
                nbt = amulet_nbt.from_snbt(value.GetValue())
            except:
                continue
            if name.GetValue() and isinstance(nbt, PropertyDataTypes):
                properties[name.GetValue()] = nbt.to_snbt()
        return properties

    @properties.setter
    def properties(self, properties: Dict[str, SNBTType]):
        self._property_sizer.Clear(True)
        self._properties.clear()
        self._property_index = 0
        for name, value in properties.items():
            self._add_property(name, value)


if __name__ == "__main__":

    def main():
        translation_manager = PyMCTranslate.new_translation_manager()
        app = wx.App()
        dialog = wx.Dialog(None)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(
            PropertySelect(
                dialog,
                translation_manager,
                "java",
                (1, 16, 0),
                False,
                "minecraft",
                "oak_fence",
            ),
            1,
            wx.ALL,
            5,
        )
        dialog.Show()
        dialog.Fit()
        app.MainLoop()

    main()
