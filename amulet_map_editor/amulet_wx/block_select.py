from .wx_util import SimplePanel, SimpleText, SimpleChoice
import wx
import PyMCTranslate
from typing import Tuple


class VersionSelect(SimplePanel):
    def __init__(self, parent, translation_manager: PyMCTranslate.TranslationManager):
        super().__init__(parent)
        self._translation_manager = translation_manager
        self._registered_updates = []
        self._versions = []

        for platform in translation_manager.platforms():
            for version in translation_manager.version_numbers(platform):
                print(platform, version, self._translation_manager.get_version(platform, version).has_abstract_format)

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

        platforms = translation_manager.platforms()
        self._platform_list = SimpleChoice(self._platform_panel, platforms)
        self._version_list = SimpleChoice(self._version_panel)
        self._set_versions()
        self._blockstate_button = wx.CheckBox(self._blockstate_panel)

        self._platform_panel.add_object(self._platform_list, 0, wx.CENTER | wx.ALL)
        self._version_panel.add_object(self._version_list, 0, wx.CENTER | wx.ALL)
        self._blockstate_panel.add_object(self._blockstate_button, 0, wx.CENTER | wx.ALL)

        self._platform_list.Bind(wx.EVT_CHOICE, self._update_version)
        self._version_list.Bind(wx.EVT_CHOICE, self._update_blockstate)

    @property
    def platform(self) -> str:
        return self._platform_list.GetString(self._platform_list.GetSelection())

    @property
    def version(self) -> Tuple[int, int, int]:
        return self._versions[self._version_list.GetSelection()]

    def _set_versions(self):
        versions = self._translation_manager.version_numbers(self.platform)
        self._versions = sorted(versions)
        self._version_list.SetItems([str(v) for v in sorted(versions)])
        self._version_list.SetSelection(0)

    @property
    def force_blockstate(self) -> bool:
        return self._platform_list.GetStringSelection()

    def _update_version(self, evt):
        self._set_versions()
        self._update_blockstate_()
        evt.Skip()

    def _update_blockstate(self, evt):
        self._update_blockstate_()
        evt.Skip()

    def _update_blockstate_(self):
        if self._translation_manager.get_version(self.platform, self.version).has_abstract_format:
            self._blockstate_button.Enable()
        else:
            self._blockstate_button.Disable()
        for callback in self._registered_updates:
            callback()

    def register_on_update(self, callback):
        self._registered_updates.append(callback)


class BlockSelect:
    pass


class BlockDefine:
    pass
