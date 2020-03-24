from amulet_map_editor.amulet_wx.simple import SimplePanel, SimpleText, SimpleChoice, SimpleChoiceAny
import wx
import PyMCTranslate
import amulet_nbt
from typing import Tuple, List, Optional, Type, Dict
from amulet.api.block import Block


class VersionSelect(SimplePanel):
    def __init__(
            self,
            parent,
            translation_manager: PyMCTranslate.TranslationManager,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            blockstate: bool = None
    ):
        super().__init__(parent)

        self._translation_manager = translation_manager
        self._platform_list: Optional[SimpleChoice] = None
        self._version_list: Optional[SimpleChoiceAny] = None
        self._blockstate_button: Optional[wx.CheckBox] = None
        self._setup_ui()
        self._populate_version(platform, version, blockstate)

    @property
    def options(self) -> Tuple[str, Tuple[int, int, int], bool]:
        return self.platform, self.version, self.force_blockstate

    def _populate_version(
            self,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            blockstate: bool = None
    ):
        self._set_platform(platform=platform, version=version, blockstate=blockstate)

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

    @property
    def platform(self) -> str:
        return self._platform_list.GetCurrentString()

    @property
    def version(self) -> Tuple[int, int, int]:
        return self._version_list.GetAny()

    @property
    def force_blockstate(self) -> bool:
        return self._blockstate_button.GetValue()

    def _set_platform(self, platform: str = None, **kwargs):
        platforms = self._translation_manager.platforms()
        self._platform_list.SetItems(
            platforms
        )
        if platform and platform in platforms:
            self._platform_list.SetSelection(platforms.index(platform))
        else:
            self._platform_list.SetSelection(0)
        self._set_version(**kwargs)

    def _update_version(self, evt):
        self._set_version()
        evt.Skip()

    def _set_version(self, version: Tuple[int, int, int] = None, **kwargs):
        self._version_list.SetItems(
            self._translation_manager.version_numbers(self.platform)
        )
        versions = self._version_list.values
        if version and version in versions:
            self._version_list.SetSelection(versions.index(version))
        self._set_blockstate(**kwargs)

    def _update_blockstate(self, evt):
        self._set_blockstate()
        evt.Skip()

    def _set_blockstate(self, blockstate: bool = None, **kwargs):
        if self._translation_manager.get_version(self.platform, self.version).has_abstract_format:
            self._blockstate_button.Enable()
            if blockstate is not None:
                self._blockstate_button.SetValue(blockstate)
        else:
            self._blockstate_button.Disable()
        self._set_namespace(**kwargs)

    def _set_namespace(self, namespace: str = None, **kwargs):
        pass


class BlockSelect(VersionSelect):
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
        self._namespace_list: Optional[SimpleChoice] = None
        self._base_name_list: Optional[SimpleChoice] = None
        super().__init__(
            parent,
            translation_manager,
            platform,
            version,
            blockstate
        )
        self._populate_block(platform, version, blockstate, namespace, base_name)

    @property
    def options(self) -> Tuple[str, Tuple[int, int, int], bool, str, str]:
        return self.platform, self.version, self.force_blockstate, self.namespace, self.base_name

    def _populate_version(
            self,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            blockstate: bool = None
    ):
        pass

    def _populate_block(
            self,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            blockstate: bool = None,
            namespace: str = None,
            base_name: str = None
    ):
        self._set_platform(platform=platform, version=version, blockstate=blockstate, namespace=namespace, base_name=base_name)

    def _setup_ui(self):
        super()._setup_ui()
        self._namespace_list = self._add_ui_element("Namespace", SimpleChoice)
        self._base_name_list = self._add_ui_element("Base name", SimpleChoice)

        self._blockstate_button.Bind(wx.EVT_CHECKBOX, self._update_namespace)
        self._namespace_list.Bind(wx.EVT_CHOICE, self._update_base_name)

    @property
    def namespace(self) -> str:
        return self._namespace_list.GetCurrentString()

    @property
    def base_name(self) -> str:
        return self._base_name_list.GetCurrentString()

    def _update_namespace(self, evt):
        self._set_namespace()
        evt.Skip()

    def _set_namespace(self, namespace: str = None, **kwargs):
        version = self._translation_manager.get_version(self.platform, self.version)
        namespaces = version.block.namespaces(self.force_blockstate)
        self._namespace_list.SetItems(
            namespaces
        )
        if namespace and namespace in namespaces:
            self._namespace_list.SetSelection(namespaces.index(namespace))
        else:
            self._namespace_list.SetSelection(0)
        self._set_base_name(**kwargs)

    def _update_base_name(self, evt):
        self._set_base_name()
        evt.Skip()

    def _set_base_name(self, base_name: str = None, **kwargs):
        version = self._translation_manager.get_version(self.platform, self.version)
        base_names = version.block.base_names(self.namespace, self.force_blockstate)
        self._base_name_list.SetItems(
            base_names
        )
        if base_name and base_name in base_names:
            self._base_name_list.SetSelection(base_names.index(base_name))
        else:
            self._base_name_list.SetSelection(0)
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
        self._properties: List[SimplePanel] = []
        self._wildcard = wildcard
        self._properties_panel: Optional[SimplePanel] = None
        super().__init__(
            parent,
            translation_manager,
            platform,
            version,
            blockstate,
            namespace,
            base_name
        )
        self._populate_properties(platform, version, blockstate, namespace, base_name, properties)

    @property
    def options(self) -> Tuple[str, Tuple[int, int, int], bool, str, str, Dict[str, str]]:
        return self.platform, self.version, self.force_blockstate, self.namespace, self.base_name, self.properties

    def _populate_version(
            self,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            blockstate: bool = None
    ):
        pass

    def _populate_block(
            self,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            blockstate: bool = None,
            namespace: str = None,
            base_name: str = None
    ):
        pass

    def _populate_properties(
            self,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            blockstate: bool = None,
            namespace: str = None,
            base_name: str = None,
            properties: Dict[str, str] = None
    ):
        self._set_platform(platform=platform, version=version, blockstate=blockstate, namespace=namespace, base_name=base_name, properties=properties)

    def _setup_ui(self):
        super()._setup_ui()
        self._base_name_list.Bind(wx.EVT_CHOICE, self._update_properties)
        self._properties_panel = SimplePanel(self, wx.VERTICAL)
        self.add_object(self._properties_panel, 0)

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

    def _update_properties(self, evt):
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
