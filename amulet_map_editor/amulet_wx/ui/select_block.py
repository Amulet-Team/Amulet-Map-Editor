from amulet_map_editor.amulet_wx.ui.simple import SimpleChoice, SimpleChoiceAny
import wx
import PyMCTranslate
import amulet_nbt
from typing import Tuple, List, Optional, Type, Dict, Any
from amulet.api.block import Block


class BaseSelect(wx.Panel):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

    def _add_ui_element(self, label: str, obj: Type[wx.Control], **kwargs) -> Any:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._sizer.Add(sizer, 0, wx.ALIGN_CENTER_HORIZONTAL)
        text = wx.StaticText(self, label=label)
        sizer.Add(text, 0, wx.CENTER | wx.LEFT | wx.RIGHT, 5)
        wx_obj = obj(self, **kwargs)
        sizer.Add(wx_obj, 0, wx.CENTER | wx.BOTTOM | wx.TOP | wx.RIGHT, 5)
        return wx_obj


class PlatformSelect(BaseSelect):
    def __init__(
            self,
            parent: wx.Window,
            translation_manager: PyMCTranslate.TranslationManager,
            platform: str = None,
            allow_universal: bool = True,
            allow_vanilla: bool = True,
            allowed_platforms: Tuple[str, ...] = None,
            **kwargs
    ):
        super().__init__(parent, **kwargs)
        self._translation_manager = translation_manager
        self._allow_universal = allow_universal
        self._allow_vanilla = allow_vanilla
        self._allowed_platforms = allowed_platforms
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
        if self._allowed_platforms is not None:
            platforms = [p for p in platforms if p in self._allowed_platforms]
        if not self._allow_universal:
            platforms = [p for p in platforms if p != "universal"]
        if not self._allow_vanilla:
            platforms = [p for p in platforms if p == "universal"]
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
            version: Tuple[int, int, int] = None,
            allow_numerical: bool = True,
            allow_blockstate: bool = True,
            **kwargs
    ):
        super().__init__(
            parent,
            translation_manager,
            platform,
            **kwargs
        )
        self._allow_numerical = allow_numerical
        self._allow_blockstate = allow_blockstate
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
        versions = self._translation_manager.version_numbers(self.platform)
        if not self._allow_blockstate:
            versions = [v for v in versions if v < (1, 13, 0)]
        if not self._allow_numerical:
            versions = [v for v in versions if v >= (1, 13, 0)]
        self._version_list.SetItems(
            versions
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
            blockstate: bool = None,
            **kwargs
    ):
        super().__init__(
            parent,
            translation_manager,
            platform,
            version,
            **kwargs
        )
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
            base_name: str = None,
            **kwargs
    ):
        super().__init__(
            parent,
            translation_manager,
            platform,
            version,
            blockstate,
            **kwargs
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
            wildcard: bool = False,
            properties_style=0,
            **kwargs
    ):
        super().__init__(
            parent,
            translation_manager,
            platform,
            version,
            blockstate,
            namespace,
            base_name,
            **kwargs
        )
        self._properties: Dict[str, SimpleChoice] = {}
        self._wildcard = wildcard
        self._base_name_list.Bind(wx.EVT_CHOICE, self._on_base_name_change)
        self._properties_panel: wx.Panel = wx.Panel(self, wx.VERTICAL, style=properties_style)
        properties_sizer = wx.BoxSizer(wx.VERTICAL)
        self._properties_panel.SetSizer(properties_sizer)
        self._sizer.Add(self._properties_panel, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 5)
        self._set_properties(properties)

    @property
    def options(self) -> Tuple[str, Tuple[int, int, int], bool, str, str, Dict[str, str]]:
        return self.platform, self.version, self.force_blockstate, self.namespace, self.base_name, self.properties

    @property
    def properties(self) -> Dict[str, str]:
        return {
            property_name: ui.GetString(ui.GetSelection())
            for property_name, ui in self._properties.items()
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
        for child in self._properties_panel.GetChildren():
            child.Destroy()
        self._properties.clear()
        self._properties_panel.Layout()

    def _add_property(self, property_name: str, property_values: List[str], default: str = None):
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._properties_panel.GetSizer().Add(sizer, 0, wx.ALL, 5)
        name_text = wx.StaticText(self._properties_panel, label=property_name)
        sizer.Add(name_text, 0, wx.CENTER | wx.RIGHT, 5)
        name_list = SimpleChoice(self._properties_panel)
        sizer.Add(name_list, 0, wx.CENTER, 5)

        self._properties[property_name] = name_list

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
        self.SetMinSize(self.GetSizer().CalcMin())
        parent = self.GetParent()  # there may be a better way to do this
        while parent is not None:
            parent.Layout()
            parent = parent.GetParent()
