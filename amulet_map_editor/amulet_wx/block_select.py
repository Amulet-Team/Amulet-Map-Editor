from amulet_map_editor.amulet_wx.simple import SimplePanel, SimpleText, SimpleChoice, SimpleChoiceAny
import wx
import PyMCTranslate
import amulet_nbt
from typing import Tuple, List, Optional, Type, Dict, Any
from amulet.api.block import Block


class BaseSelect(SimplePanel):
    def __init__(self, parent):
        super().__init__(parent)

    def _add_ui_element(self, label: str, obj: Type[wx.Control], **kwargs) -> Any:
        panel = SimplePanel(self, wx.HORIZONTAL)
        self.add_object(panel, 0)
        text = SimpleText(panel, label)
        panel.add_object(text, 0, wx.CENTER | wx.ALL)
        wx_obj = obj(panel, **kwargs)
        panel.add_object(wx_obj, 0, wx.CENTER | wx.ALL)
        return wx_obj


class PlatformSelect(BaseSelect):
    def __init__(
            self,
            parent: wx.Window,
            translation_manager: PyMCTranslate.TranslationManager,
            platform: str = None
    ):
        super().__init__(parent)
        self._translation_manager = translation_manager
        self._platform_list: SimpleChoice = self._add_ui_element("Platform", SimpleChoice)
        self._set_platform(platform)

    @property
    def options(self) -> str:
        return self.platform

    @property
    def platform(self) -> str:
        return self._platform_list.GetCurrentString()

    def _set_platform(self, platform: str = None):
        platforms = self._translation_manager.platforms()
        self._platform_list.SetItems(
            platforms
        )
        if platform and platform in platforms:
            self._platform_list.SetSelection(platforms.index(platform))
        else:
            self._platform_list.SetSelection(0)

    def _set_platform_recursive(self, platform: str = None, **kwargs):
        self._set_platform(platform)
        self._set_version_recursive(**kwargs)

    def _set_version_recursive(self, version: Tuple[int, int, int] = None, **kwargs):
        pass


class VersionSelect(PlatformSelect):
    def __init__(
            self,
            parent: wx.Window,
            translation_manager: PyMCTranslate.TranslationManager,
            platform: str = None,
            version: Tuple[int, int, int] = None
    ):
        super().__init__(parent, translation_manager, platform)
        self._version_list: Optional[SimpleChoiceAny] = self._add_ui_element("Version", SimpleChoiceAny, reverse=True)
        self._platform_list.Bind(wx.EVT_CHOICE, self._on_platform_change)
        self._set_version(version)

    @property
    def options(self) -> Tuple[str, Tuple[int, int, int]]:
        return self.platform, self.version

    @property
    def version(self) -> Tuple[int, int, int]:
        return self._version_list.GetAny()

    def _set_version(self, version: Tuple[int, int, int] = None):
        self._version_list.SetItems(
            self._translation_manager.version_numbers(self.platform)
        )
        versions = self._version_list.values
        if version and version in versions:
            self._version_list.SetSelection(versions.index(version))

    def _on_platform_change(self, evt):
        self._set_version_recursive()
        evt.Skip()

    def _set_version_recursive(self, version: Tuple[int, int, int] = None, **kwargs):
        self._set_version(version)
        self._set_blockstate_recursive(**kwargs)

    def _set_blockstate_recursive(self, blockstate: bool = None, **kwargs):
        pass


class SubVersionSelect(VersionSelect):
    def __init__(
            self,
            parent: wx.Window,
            translation_manager: PyMCTranslate.TranslationManager,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            blockstate: bool = None
    ):
        super().__init__(parent, translation_manager, platform, version)
        self._blockstate_button: Optional[wx.CheckBox] = self._add_ui_element("Force Blockstate", wx.CheckBox)
        self._version_list.Bind(wx.EVT_CHOICE, self._on_version_change)
        self._set_blockstate(blockstate)

    @property
    def options(self) -> Tuple[str, Tuple[int, int, int], bool]:
        return self.platform, self.version, self.force_blockstate

    @property
    def force_blockstate(self) -> bool:
        return self._blockstate_button.GetValue()

    def _set_blockstate(self, blockstate: bool = None):
        if self._translation_manager.get_version(self.platform, self.version).has_abstract_format:
            self._blockstate_button.Enable()
            if blockstate is not None:
                self._blockstate_button.SetValue(blockstate)
        else:
            self._blockstate_button.Disable()

    def _on_version_change(self, evt):
        self._set_blockstate_recursive()
        evt.Skip()

    def _set_blockstate_recursive(self, blockstate: bool = None, **kwargs):
        self._set_blockstate(blockstate)
        self._set_namespace_recursive(**kwargs)

    def _set_namespace_recursive(self, namespace: str = None, **kwargs):
        pass


class BlockSelect(SubVersionSelect):
    def __init__(
            self,
            parent,
            translation_manager: PyMCTranslate.TranslationManager,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            blockstate: bool = None,
            namespace: str = None,
            base_name: str = None
    ):
        super().__init__(
            parent,
            translation_manager,
            platform,
            version,
            blockstate
        )
        self._namespace_list: Optional[SimpleChoice] = self._add_ui_element("Namespace", SimpleChoice)
        self._base_name_list: Optional[SimpleChoice] = self._add_ui_element("Base name", SimpleChoice)
        self._blockstate_button.Bind(wx.EVT_CHECKBOX, self._on_sub_version_change)
        self._set_namespace(namespace)
        self._namespace_list.Bind(wx.EVT_CHOICE, self._on_namespace_change)
        self._set_base_name(base_name)

    @property
    def options(self) -> Tuple[str, Tuple[int, int, int], bool, str, str]:
        return self.platform, self.version, self.force_blockstate, self.namespace, self.base_name

    @property
    def namespace(self) -> str:
        return self._namespace_list.GetCurrentString()

    @property
    def base_name(self) -> str:
        return self._base_name_list.GetCurrentString()

    def _on_sub_version_change(self, evt):
        self._set_namespace_recursive()
        evt.Skip()

    def _set_namespace(self, namespace: str = None):
        version = self._translation_manager.get_version(self.platform, self.version)
        namespaces = version.block.namespaces(self.force_blockstate)
        self._namespace_list.SetItems(
            namespaces
        )
        if namespace and namespace in namespaces:
            self._namespace_list.SetSelection(namespaces.index(namespace))
        else:
            self._namespace_list.SetSelection(0)

    def _set_namespace_recursive(self, namespace: str = None, **kwargs):
        self._set_namespace(namespace)
        self._set_base_name_recursive(**kwargs)

    def _on_namespace_change(self, evt):
        self._set_base_name_recursive()
        evt.Skip()

    def _set_base_name(self, base_name: str = None):
        version = self._translation_manager.get_version(self.platform, self.version)
        base_names = version.block.base_names(self.namespace, self.force_blockstate)
        self._base_name_list.SetItems(
            base_names
        )
        if base_name and base_name in base_names:
            self._base_name_list.SetSelection(base_names.index(base_name))
        else:
            self._base_name_list.SetSelection(0)

    def _set_base_name_recursive(self, base_name: str = None, **kwargs):
        self._set_base_name(base_name)
        self._set_properties(**kwargs)

    def _set_properties(self, properties: Dict[str, str] = None):
        pass


class BlockDefine(BlockSelect):
    def __init__(
            self,
            parent,
            translation_manager: PyMCTranslate.TranslationManager,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            blockstate: bool = None,
            namespace: str = None,
            base_name: str = None,
            properties: Dict[str, str] = None,
            wildcard: bool = False
    ):
        super().__init__(
            parent,
            translation_manager,
            platform,
            version,
            blockstate,
            namespace,
            base_name
        )
        self._properties: List[SimplePanel] = []
        self._wildcard = wildcard
        self._base_name_list.Bind(wx.EVT_CHOICE, self._on_base_name_change)
        self._properties_panel: Optional[SimplePanel] = SimplePanel(self, wx.VERTICAL)
        self.add_object(self._properties_panel, 0)
        self._set_properties(properties)

    @property
    def options(self) -> Tuple[str, Tuple[int, int, int], bool, str, str, Dict[str, str]]:
        return self.platform, self.version, self.force_blockstate, self.namespace, self.base_name, self.properties

    @property
    def properties(self) -> Dict[str, str]:
        return {
            prop.GetChildren()[0].GetLabel(): prop.GetChildren()[1].GetString(prop.GetChildren()[1].GetSelection())
            for prop in self._properties
        }

    @property
    def block(self) -> Block:
        if self._wildcard:
            raise Exception('block property cannot be used when BlockDefine is in wildcard mode')
        else:
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

    def _add_property(self, property_name: str, property_values: List[str], default: str = None):
        prop_panel = SimplePanel(self._properties_panel, wx.HORIZONTAL)
        self._properties.append(prop_panel)
        self._properties_panel.add_object(prop_panel, 0)
        name_text = SimpleText(prop_panel, property_name)
        prop_panel.add_object(name_text, 0, wx.CENTER | wx.ALL)
        name_list = SimpleChoice(prop_panel)
        prop_panel.add_object(name_list, 0, wx.CENTER | wx.ALL)

        if self._wildcard:
            property_values.insert(0, "*")
        name_list.SetItems(property_values)
        if default and default in property_values:
            name_list.SetSelection(property_values.index(default))
        else:
            name_list.SetSelection(0)

    def _on_base_name_change(self, evt):
        self._set_properties()
        evt.Skip()

    def _set_properties(self, properties: Dict[str, str] = None):
        self._clear_properties()
        specification = self._translation_manager.get_version(
            self.platform, self.version
        ).block.get_specification(
            self.namespace, self.base_name, self.force_blockstate
        )
        if properties is None:
            properties = {}
        if 'properties' in specification:
            for prop, options in specification['properties'].items():
                self._add_property(prop, options, properties.get(prop, None))
        self.Fit()
        self.Layout()
        self.GetTopLevelParent().Fit()
