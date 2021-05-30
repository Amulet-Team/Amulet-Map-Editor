import wx
from typing import Tuple, Dict, List, Union

import PyMCTranslate
import amulet_nbt
from amulet_nbt import SNBTType
from amulet.api.block import PropertyDataTypes, PropertyType
from amulet_map_editor.api.image import ADD_ICON, SUBTRACT_ICON
from .events import PropertiesChangeEvent
from .base_property import BasePropertySelect


class PropertySelect(BasePropertySelect):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str,
        version_number: Tuple[int, int, int],
        force_blockstate: bool,
        namespace: str,
        block_name: str,
        properties: PropertyType = None,
    ):
        super().__init__(
            parent,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            namespace,
            block_name,
            style=wx.BORDER_SIMPLE)

        self._manual_enabled = False
        self._simple = SimplePropertySelect(self, translation_manager)
        self._sizer.Add(self._simple, 1, wx.EXPAND)
        self._manual = ManualPropertySelect(self, translation_manager)
        self._sizer.Add(self._manual, 1, wx.EXPAND)

        if properties is None:
            properties = {}
        self._set_properties(properties)
        self._rebuild_ui()

    def _get_properties(self) -> PropertyType:
        if self._manual_enabled:
            return self._manual.properties
        else:
            return self._simple.properties

    def _set_properties(self, properties: PropertyType):
        self.Freeze()
        if self._manual_enabled:
            self._manual.properties = properties
        else:
            self._simple.properties = properties
        self.TopLevelParent.Layout()
        self.Thaw()

    def _rebuild_ui(self):
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
            self._manual.Hide()
            self._simple.Show()
            self._simple.rebuild_ui(
                translator.get_specification(
                    self._namespace, self._block_name, self._force_blockstate
                )
            )
        self.Thaw()


class BaseSubPropertySelect(wx.Panel):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
    ):
        super().__init__(parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)
        self._translation_manager = translation_manager

    @property
    def properties(self) -> PropertyType:
        raise NotImplementedError

    @properties.setter
    def properties(self, properties: PropertyType):
        raise NotImplementedError


class SimplePropertySelect(BaseSubPropertySelect):
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

        self._properties: Dict[str, wx.Choice] = {}
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
            choice = wx.Choice(self, choices=choices)
            self._property_sizer.Add(choice, 0, wx.EXPAND)
            choice.Bind(
                wx.EVT_CHOICE,
                lambda evt: wx.PostEvent(
                    self,
                    PropertiesChangeEvent(self.GetId(), properties=self.properties),
                ),
            )
            self._properties[name] = choice
        self.properties = self._specification.get("defaults", {})
        self.Fit()
        self.GetTopLevelParent().Layout()
        self.Thaw()

    @property
    def properties(self) -> PropertyType:
        return {
            name: amulet_nbt.from_snbt(choice.GetString(choice.GetSelection()))
            for name, choice in self._properties.items()
        }

    @properties.setter
    def properties(self, properties: PropertyType):
        self.Freeze()
        for name, nbt in properties.items():
            if name in self._properties:
                if isinstance(nbt, amulet_nbt.BaseValueType):
                    snbt = nbt.to_snbt()
                elif isinstance(nbt, str):
                    snbt = nbt
                else:
                    continue
                choice = self._properties[name]
                index = choice.FindString(snbt)
                if index != wx.NOT_FOUND:
                    choice.SetSelection(index)
        self.Thaw()


class ManualPropertySelect(BaseSubPropertySelect):
    def __init__(
        self, parent: wx.Window, translation_manager: PyMCTranslate.TranslationManager
    ):
        super().__init__(parent, translation_manager)
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


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    for block in (("minecraft", "oak_fence"), ("modded", "block")):
        dialog = wx.Dialog(None, title=f"PropertySelect with block {block[0]}:{block[1]}", style=wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER | wx.DIALOG_NO_PARENT)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(
            PropertySelect(dialog, translation_manager, "java", (1, 16, 0), False, *block),
            1,
            wx.ALL,
            5,
        )

        def get_on_close(dialog_):
            def on_close(evt):
                dialog_.Destroy()

            return on_close

        dialog.Bind(wx.EVT_CLOSE, get_on_close(dialog))
        dialog.Show()
        dialog.Fit()
