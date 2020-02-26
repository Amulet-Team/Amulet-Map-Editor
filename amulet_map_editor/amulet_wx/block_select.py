from .wx_util import SimplePanel, SimpleText, SimpleChoice, SimpleChoiceAny
import wx
import PyMCTranslate
from typing import Tuple, List


class VersionSelect(SimplePanel):
    def __init__(self, parent, translation_manager: PyMCTranslate.TranslationManager):
        super().__init__(parent)
        self._translation_manager = translation_manager

        self._platform_panel = SimplePanel(self, wx.HORIZONTAL)
        self._version_panel = SimplePanel(self, wx.HORIZONTAL)
        self._blockstate_panel = SimplePanel(self, wx.HORIZONTAL)
        self.add_object(self._platform_panel, 0)
        self.add_object(self._version_panel, 0)
        self.add_object(self._blockstate_panel, 0)

        self._platform_text = SimpleText(self._platform_panel, "Platform")
        self._version_text = SimpleText(self._version_panel, "Version")
        self._blockstate_text = SimpleText(self._blockstate_panel, "Force Blockstate")

        self._platform_panel.add_object(self._platform_text, 0, wx.CENTER | wx.ALL)
        self._version_panel.add_object(self._version_text, 0, wx.CENTER | wx.ALL)
        self._blockstate_panel.add_object(self._blockstate_text, 0, wx.CENTER | wx.ALL)

        self._platform_list = SimpleChoice(self._platform_panel)
        self._version_list = SimpleChoiceAny(self._version_panel)
        self._blockstate_button = wx.CheckBox(self._blockstate_panel)

        self._platform_panel.add_object(self._platform_list, 0, wx.CENTER | wx.ALL)
        self._version_panel.add_object(self._version_list, 0, wx.CENTER | wx.ALL)
        self._blockstate_panel.add_object(self._blockstate_button, 0, wx.CENTER | wx.ALL)

        self._platform_list.Bind(wx.EVT_CHOICE, self._update_version)
        self._version_list.Bind(wx.EVT_CHOICE, self._update_blockstate)
        self._blockstate_button.Bind(wx.EVT_CHECKBOX, self._update_namespace)

    def populate(self):
        self._set_platforms()

    @property
    def platform(self) -> str:
        return self._platform_list.GetString(self._platform_list.GetSelection())

    @property
    def version(self) -> Tuple[int, int, int]:
        return self._version_list.GetAny()

    @property
    def force_blockstate(self) -> bool:
        return self._blockstate_button.GetValue()

    def _set_platforms(self):
        self._platform_list.SetItems(
            self._translation_manager.platforms()
        )
        self._platform_list.SetSelection(0)
        self._set_versions()

    def _set_versions(self):
        self._version_list.SetItems(
            self._translation_manager.version_numbers(self.platform)
        )
        self._set_blockstate()

    def _update_version(self, evt):
        self._set_versions()
        evt.Skip()

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

    def _set_namespace(self):
        pass


class BlockSelect(VersionSelect):
    def __init__(self, parent, translation_manager: PyMCTranslate.TranslationManager):
        super().__init__(parent, translation_manager)

        self._namespace_panel = SimplePanel(self, wx.HORIZONTAL)
        self._base_name_panel = SimplePanel(self, wx.HORIZONTAL)
        self.add_object(self._namespace_panel, 0)
        self.add_object(self._base_name_panel, 0)

        self._namespace_text = SimpleText(self._namespace_panel, "Namespace")
        self._base_name_text = SimpleText(self._base_name_panel, "Base name")

        self._namespace_panel.add_object(self._namespace_text, 0, wx.CENTER | wx.ALL)
        self._base_name_panel.add_object(self._base_name_text, 0, wx.CENTER | wx.ALL)

        self._namespace_list = SimpleChoice(self._namespace_panel)
        self._base_name_list = SimpleChoice(self._base_name_panel)

        self._namespace_panel.add_object(self._namespace_list, 0, wx.CENTER | wx.ALL)
        self._base_name_panel.add_object(self._base_name_list, 0, wx.CENTER | wx.ALL)

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
        super().__init__(parent, translation_manager)
        self._properties = []
        self._properties_panel = SimplePanel(self, wx.VERTICAL)
        self.add_object(self._properties_panel, 0)

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
        self.Fit()
