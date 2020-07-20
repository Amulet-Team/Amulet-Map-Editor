from amulet_map_editor.amulet_wx.ui.simple import SimpleChoice, SimpleChoiceAny
import wx
from wx.lib import newevent
import PyMCTranslate
from typing import Tuple, Optional, Type, Any

PlatformChangeEvent, EVT_PLATFORM_CHANGE = newevent.NewEvent()
VersionChangeEvent, EVT_VERSION_CHANGE = newevent.NewEvent()
FormatChangeEvent, EVT_FORMAT_CHANGE = newevent.NewEvent()


class PlatformSelect(wx.Panel):
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
        super().__init__(parent, style=wx.BORDER_SIMPLE)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        self._translation_manager = translation_manager
        self._allow_universal = allow_universal
        self._allow_vanilla = allow_vanilla
        self._allowed_platforms = allowed_platforms
        self._platform_choice: SimpleChoice = self._add_ui_element(
            "Platform:", SimpleChoice
        )
        self._populate_platform()
        self.platform = platform
        self._platform_choice.Bind(wx.EVT_CHOICE, lambda evt: wx.PostEvent(self, PlatformChangeEvent(platform=self.platform)))

    def _add_ui_element(self, label: str, obj: Type[wx.Control], **kwargs) -> Any:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._sizer.Add(sizer, 0, wx.EXPAND | wx.ALL, 5)
        text = wx.StaticText(self, label=label, style=wx.ALIGN_CENTER_VERTICAL)
        sizer.Add(text, 1, wx.ALIGN_CENTER_VERTICAL)
        wx_obj = obj(self, **kwargs)
        sizer.Add(wx_obj, 2)
        return wx_obj

    @property
    def platform(self) -> str:
        return self._platform_choice.GetCurrentString()

    @platform.setter
    def platform(self, platform: str):
        if platform and platform in self._platform_choice.GetItems():
            self._platform_choice.SetSelection(self._platform_choice.GetItems().index(platform))
        else:
            self._platform_choice.SetSelection(0)
        wx.PostEvent(self, PlatformChangeEvent(platform=self.platform))

    def _populate_platform(self):
        platforms = self._translation_manager.platforms()
        if self._allowed_platforms is not None:
            platforms = [p for p in platforms if p in self._allowed_platforms]
        if not self._allow_universal:
            platforms = [p for p in platforms if p != "universal"]
        if not self._allow_vanilla:
            platforms = [p for p in platforms if p == "universal"]
        self._platform_choice.SetItems(platforms)


class VersionSelect(PlatformSelect):
    def __init__(
            self,
            parent: wx.Window,
            translation_manager: PyMCTranslate.TranslationManager,
            platform: str = None,
            version: Tuple[int, int, int] = None,
            force_blockstate: bool = None,
            allow_numerical: bool = True,
            allow_blockstate: bool = True,
            **kwargs
    ):
        super().__init__(parent, translation_manager, platform, **kwargs)
        self._allow_numerical = allow_numerical
        self._allow_blockstate = allow_blockstate

        self.Bind(EVT_PLATFORM_CHANGE, self._on_platform_change)

        self._version_choice: Optional[SimpleChoiceAny] = self._add_ui_element(
            "Version:", SimpleChoiceAny, reverse=True
        )
        self._populate_version()
        self.version = version
        self._version_choice.Bind(wx.EVT_CHOICE, lambda evt: wx.PostEvent(self, VersionChangeEvent(version=self.version)))

        self.Bind(EVT_VERSION_CHANGE, self._on_version_change)
        self._blockstate_choice: Optional[SimpleChoice] = self._add_ui_element(
            "Format:", SimpleChoice
        )
        self._blockstate_choice.SetItems(["native", "blockstate"])
        self._blockstate_choice.SetSelection(0)
        self._populate_blockstate()
        self.force_blockstate = force_blockstate
        self._blockstate_choice.Bind(wx.EVT_CHOICE, lambda evt: wx.PostEvent(self, FormatChangeEvent(force_blockstate=self.force_blockstate)))

    @property
    def version(self) -> Tuple[int, int, int]:
        return self._version_choice.GetCurrentObject()

    @version.setter
    def version(self, version: Tuple[int, int, int]):
        if version and version in self._version_choice.values:
            self._version_choice.SetSelection(self._version_choice.values.index(version))
        else:
            self._version_choice.SetSelection(0)
        wx.PostEvent(self, VersionChangeEvent(version=self.version))

    @property
    def force_blockstate(self) -> bool:
        return self._blockstate_choice.GetCurrentString() == "blockstate"

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        if force_blockstate is not None:
            self._blockstate_choice.SetSelection(int(force_blockstate))
        wx.PostEvent(self, FormatChangeEvent(force_blockstate=self.force_blockstate))

    def _populate_version(self):
        versions = self._translation_manager.version_numbers(self.platform)
        if not self._allow_blockstate:
            versions = [v for v in versions if v < (1, 13, 0)]
        if not self._allow_numerical:
            versions = [v for v in versions if v >= (1, 13, 0)]
        self._version_choice.SetItems(versions)

    def _populate_blockstate(self):
        if self._translation_manager.get_version(
                self.platform, self.version
        ).has_abstract_format:
            self._blockstate_choice.Enable()
        else:
            self._blockstate_choice.Disable()

    def _on_platform_change(self, evt):
        self._populate_version()
        self.version = None
        evt.Skip()

    def _on_version_change(self, evt):
        self._populate_blockstate()
        self.force_blockstate = None
        evt.Skip()


if __name__ == '__main__':
    import PyMCTranslate
    translation_manager = PyMCTranslate.new_translation_manager()
    app = wx.App()
    for cls in (PlatformSelect, VersionSelect):
        dialog = wx.Dialog(None)
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        sizer.Add(cls(dialog, translation_manager))
        dialog.Show()
        dialog.Fit()
    app.MainLoop()
