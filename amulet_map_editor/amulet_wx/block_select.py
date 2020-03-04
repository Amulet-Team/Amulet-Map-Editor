from .wx_util import SimplePanel, SimpleText, SimpleChoice, SimpleChoiceAny
import wx
import PyMCTranslate
import amulet_nbt
from typing import Tuple, List, Optional, Type
from amulet.api.block import Block


history = {}


class VersionSelect(SimplePanel):
    def __init__(self, parent, translation_manager: PyMCTranslate.TranslationManager):
        super().__init__(parent)
        self._populated = False

        self._translation_manager = translation_manager
        self._platform_list: Optional[SimpleChoice] = None
        self._version_list: Optional[SimpleChoiceAny] = None
        self._blockstate_button: Optional[wx.CheckBox] = None
        self._setup_ui()
        self._set_platforms()

    def _add_ui_element(self, label: str, obj: Type[wx.Control]) -> wx.Control:
        panel = SimplePanel(self, wx.HORIZONTAL)
        self.add_object(panel, 0)
        text = SimpleText(panel, label)
        panel.add_object(text, 0, wx.CENTER | wx.ALL)
        wx_obj = obj(panel)
        panel.add_object(wx_obj, 0, wx.CENTER | wx.ALL)
        return wx_obj

    def _setup_ui(self):
        self._platform_list = self._add_ui_element("Platform", SimpleChoice)
        self._version_list = self._add_ui_element("Version", SimpleChoiceAny)
        self._blockstate_button = self._add_ui_element("Force Blockstate", wx.CheckBox)

        self._platform_list.Bind(wx.EVT_CHOICE, self._update_version)
        self._version_list.Bind(wx.EVT_CHOICE, self._update_blockstate)
        self._blockstate_button.Bind(wx.EVT_CHECKBOX, self._update_namespace)

    @property
    def platform(self) -> str:
        return self._platform_list.GetString(self._platform_list.GetSelection())

    @property
    def version(self) -> Tuple[int, int, int]:
        return self._version_list.GetAny()

    @property
    def force_blockstate(self) -> bool:
        return self._blockstate_button.GetValue()

    def _set_platforms(self, value: str = None):
        self._platform_list.SetItems(
            self._translation_manager.platforms()
        )
        self._platform_list.SetSelection(0)
        self._set_versions()

    def _update_version(self, evt):
        self._set_versions()
        evt.Skip()

    def _set_versions(self, value: Tuple[int, int, int] = None):
        self._version_list.SetItems(
            self._translation_manager.version_numbers(self.platform)
        )
        self._set_blockstate()

    def _update_blockstate(self, evt):
        self._set_blockstate()
        evt.Skip()

    def _set_blockstate(self):
        if self._translation_manager.get_version(self.platform, self.version).has_abstract_format:
            self._blockstate_button.Enable()
        else:
            self._blockstate_button.Disable()
        self._set_namespace()

    def _update_namespace(self, evt):
        self._set_namespace()
        evt.Skip()

    def _set_namespace(self):
        pass


class BlockSelect(VersionSelect):
    def __init__(self, parent, translation_manager: PyMCTranslate.TranslationManager):
        self._namespace_list: Optional[SimpleChoice] = None
        self._base_name_list: Optional[SimpleChoice] = None
        super().__init__(parent, translation_manager)

    def _setup_ui(self):
        super()._setup_ui()
        self._namespace_list = self._add_ui_element("Namespace", SimpleChoice)
        self._base_name_list = self._add_ui_element("Base name", SimpleChoice)

        self._namespace_list.Bind(wx.EVT_CHOICE, self._update_base_name)
        self._base_name_list.Bind(wx.EVT_CHOICE, self._update_properties)

    @property
    def namespace(self) -> str:
        return self._namespace_list.GetString(self._namespace_list.GetSelection())

    @property
    def base_name(self) -> str:
        return self._base_name_list.GetString(self._base_name_list.GetSelection())

    def _set_namespace(self):
        version = self._translation_manager.get_version(self.platform, self.version)
        self._namespace_list.SetItems(
            version.block.namespaces(self.force_blockstate)
        )
        self._namespace_list.SetSelection(0)
        self._set_base_name()

    def _update_base_name(self, evt):
        self._set_base_name()
        evt.Skip()

    def _set_base_name(self):
        version = self._translation_manager.get_version(self.platform, self.version)
        self._base_name_list.SetItems(
            version.block.base_names(self.namespace, self.force_blockstate)
        )
        self._base_name_list.SetSelection(0)
        self._set_properties()

    def _update_properties(self, evt):
        self._set_properties()
        evt.Skip()

    def _set_properties(self):
        pass


class BlockDefine(BlockSelect):
    def __init__(self, parent, translation_manager: PyMCTranslate.TranslationManager):
        self._properties: List[SimplePanel] = []
        self._properties_panel: Optional[SimplePanel] = None
        super().__init__(parent, translation_manager)

    def _setup_ui(self):
        super()._setup_ui()
        self._properties_panel = SimplePanel(self, wx.VERTICAL)
        self.add_object(self._properties_panel, 0)

    @property
    def properties(self) -> dict:
        return {
            prop.GetChildren()[0].GetLabel(): prop.GetChildren()[1].GetString(prop.GetChildren()[1].GetSelection())
            for prop in self._properties
        }

    @property
    def block(self) -> Block:
        return Block(
            self.namespace,
            self.base_name,
            {key: amulet_nbt.from_snbt(value) for key, value in self.properties.items()}
        )

    def _clear_properties(self):
        for prop in self._properties:
            prop.Destroy()
        self._properties.clear()
        self._properties_panel.Layout()

    def _add_property(self, property_name: str, property_values: List[str]):
        prop_panel = SimplePanel(self._properties_panel, wx.HORIZONTAL)
        self._properties.append(prop_panel)
        self._properties_panel.add_object(prop_panel, 0)
        name_text = SimpleText(prop_panel, property_name)
        prop_panel.add_object(name_text, 0, wx.CENTER | wx.ALL)
        name_list = SimpleChoice(prop_panel)
        prop_panel.add_object(name_list, 0, wx.CENTER | wx.ALL)
        name_list.SetItems(property_values)
        name_list.SetSelection(0)

    def _set_properties(self):
        self._clear_properties()
        specification = self._translation_manager.get_version(
            self.platform, self.version
        ).block.get_specification(
            self.namespace, self.base_name, self.force_blockstate
        )
        if 'properties' in specification:
            for prop, options in specification['properties'].items():
                self._add_property(prop, options)
        self._properties_panel.Layout()
        self._properties_panel.Fit()
        self.Fit()
