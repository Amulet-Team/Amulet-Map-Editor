from amulet_map_editor.api.wx.ui.simple import SimpleChoice, SimpleChoiceAny
import wx
from wx.lib import newevent
import PyMCTranslate
from typing import Tuple, Optional, Type, Any

from amulet.api.data_types import VersionNumberTuple, PlatformType

(
    PlatformChangeEvent,
    EVT_PLATFORM_CHANGE,
) = newevent.NewCommandEvent()  # the platform entry changed
(
    VersionNumberChangeEvent,
    EVT_VERSION_NUMBER_CHANGE,
) = newevent.NewCommandEvent()  # the version number entry changed
(
    FormatChangeEvent,
    EVT_FORMAT_CHANGE,
) = (
    newevent.NewCommandEvent()
)  # the format entry changed (is fired even if the entry isn't visible)
(
    VersionChangeEvent,
    EVT_VERSION_CHANGE,
) = (
    newevent.NewCommandEvent()
)  # one of the above changed. Fired after EVT_FORMAT_CHANGE


class PlatformSelect(wx.Panel):
    """
    A UI element that allows you to pick between the platforms in the translator.
    """
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: PlatformType = None,
        allow_universal: bool = True,
        allow_vanilla: bool = True,
        allowed_platforms: Tuple[PlatformType, ...] = None,
        **kwargs
    ):
        """
        Construct a :class:`PlatformSelect` UI.

        :param parent: The parent window.
        :param translation_manager: The translation manager to populate from.
        :param platform: The default platform (optional)
        :param allow_universal: If True the universal format will be included.
        :param allow_vanilla: If True the vanilla formats will be included.
        :param allowed_platforms: A whitelist of platforms.
        :param kwargs: Keyword args to be given to the Panel.
        """
        super().__init__(parent, style=wx.BORDER_SIMPLE)
        sizer = wx.BoxSizer()
        self.SetSizer(sizer)
        self._sizer = wx.FlexGridSizer(2, 5, 5)
        sizer.Add(self._sizer, 0, wx.ALL, 5)

        self._translation_manager = translation_manager
        self._allow_universal = allow_universal
        self._allow_vanilla = allow_vanilla
        self._allowed_platforms = allowed_platforms
        self._platform_choice: SimpleChoice = self._add_ui_element(
            "Platform:", SimpleChoice
        )
        self._populate_platform()
        self._set_platform(platform)
        self._platform_choice.Bind(
            wx.EVT_CHOICE,
            lambda evt: wx.PostEvent(
                self, PlatformChangeEvent(self.GetId(), platform=self.platform)
            ),
        )

    def _add_ui_element(
        self, label: str, obj: Type[wx.Control], shown=True, **kwargs
    ) -> Any:
        text = wx.StaticText(self, label=label, style=wx.ALIGN_CENTER)
        self._sizer.Add(text, 0, wx.ALIGN_CENTER)
        wx_obj = obj(self, **kwargs)
        self._sizer.Add(wx_obj, 0, wx.EXPAND)
        if not shown:
            text.Hide()
            wx_obj.Hide()
        return wx_obj

    @property
    def platform(self) -> PlatformType:
        return self._platform_choice.GetCurrentString()

    @platform.setter
    def platform(self, platform: PlatformType):
        self._set_platform(platform)
        wx.PostEvent(self, PlatformChangeEvent(self.GetId(), platform=self.platform))

    def _set_platform(self, platform: PlatformType):
        if platform and platform in self._platform_choice.GetItems():
            self._platform_choice.SetSelection(
                self._platform_choice.GetItems().index(platform)
            )
        else:
            self._platform_choice.SetSelection(0)

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
    """
    A UI element that allows you to pick between the platforms and versions in the translator.
    """
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: PlatformType = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        show_force_blockstate: bool = True,
        allow_numerical: bool = True,
        allow_blockstate: bool = True,
        **kwargs
    ):
        """
        Construct a :class:`VersionSelect` UI.

        :param parent: The parent window.
        :param translation_manager: The translation manager to populate from.
        :param platform: The default platform (optional)
        :param version_number: The default version number (optional)
        :param force_blockstate: If True and the native format is numerical will use the custom blockstate format. Else will use the native format.
        :param show_force_blockstate: Should the format selection be shown to the user.
        :param allow_numerical: Should the numerical versions be shown to the user.
        :param allow_blockstate: Should the blockstate versions be shown to the user.
        :param kwargs: Keyword args to be given to the :class:`PlatformSelect` and Panel.
        """
        super().__init__(parent, translation_manager, platform, **kwargs)
        self._allow_numerical = allow_numerical
        self._allow_blockstate = allow_blockstate

        self.Bind(EVT_PLATFORM_CHANGE, self._on_platform_change)

        self._version_choice: Optional[SimpleChoiceAny] = self._add_ui_element(
            "Version:", SimpleChoiceAny, reverse=True
        )
        self._populate_version()
        self._set_version_number(version_number)
        self._version_choice.Bind(
            wx.EVT_CHOICE,
            lambda evt: wx.PostEvent(
                self,
                VersionNumberChangeEvent(
                    self.GetId(), version_number=self.version_number
                ),
            ),
        )

        self.Bind(EVT_VERSION_NUMBER_CHANGE, self._on_version_number_change)
        self._blockstate_choice: Optional[SimpleChoice] = self._add_ui_element(
            "Format:", SimpleChoice, shown=show_force_blockstate
        )
        self._blockstate_choice.SetItems(["native", "blockstate"])
        self._blockstate_choice.SetSelection(0)
        self._populate_blockstate()
        self._set_force_blockstate(force_blockstate)
        self._blockstate_choice.Bind(
            wx.EVT_CHOICE, lambda evt: self._post_version_change()
        )

    def _post_version_change(self):
        wx.PostEvent(
            self,
            FormatChangeEvent(self.GetId(), force_blockstate=self.force_blockstate),
        ),
        wx.PostEvent(
            self,
            VersionChangeEvent(
                self.GetId(),
                platform=self.platform,
                version_number=self.version_number,
                force_blockstate=self.force_blockstate,
            ),
        )

    @property
    def version_number(self) -> VersionNumberTuple:
        return self._version_choice.GetCurrentObject()

    @version_number.setter
    def version_number(self, version_number: VersionNumberTuple):
        self._set_version_number(version_number)
        wx.PostEvent(
            self,
            VersionNumberChangeEvent(self.GetId(), version_number=self.version_number),
        )

    def _set_version_number(self, version_number: VersionNumberTuple):
        if version_number and version_number in self._version_choice.values:
            self._version_choice.SetSelection(
                self._version_choice.values.index(version_number)
            )
        else:
            self._version_choice.SetSelection(0)

    @property
    def force_blockstate(self) -> bool:
        return self._blockstate_choice.GetCurrentString() == "blockstate"

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        self._set_force_blockstate(force_blockstate)
        self._post_version_change()

    def _set_force_blockstate(self, force_blockstate: bool):
        if force_blockstate is not None:
            self._blockstate_choice.SetSelection(int(force_blockstate))

    @property
    def version(self) -> Tuple[PlatformType, VersionNumberTuple, bool]:
        return self.platform, self.version_number, self.force_blockstate

    @version.setter
    def version(self, version: Tuple[PlatformType, VersionNumberTuple, bool]):
        platform, version_number, force_blockstate = version
        self._set_platform(platform)
        self._set_version_number(version_number)
        self.force_blockstate = force_blockstate

    def _populate_version(self):
        versions = self._translation_manager.version_numbers(self.platform)
        if not self._allow_blockstate:
            versions = [v for v in versions if v < (1, 13, 0)]
        if not self._allow_numerical:
            versions = [v for v in versions if v >= (1, 13, 0)]
        self._version_choice.SetItems(versions)

    def _populate_blockstate(self):
        if self._translation_manager.get_version(
            self.platform, self.version_number
        ).has_abstract_format:
            self._blockstate_choice.Enable()
        else:
            self._blockstate_choice.Disable()

    def _on_platform_change(self, evt):
        self._populate_version()
        self.version_number = None
        evt.Skip()

    def _on_version_number_change(self, evt):
        self._populate_blockstate()
        self.force_blockstate = None
        evt.Skip()


if __name__ == "__main__":

    def main():
        translation_manager = PyMCTranslate.new_translation_manager()
        app = wx.App()
        for cls in (
            PlatformSelect,
            lambda *args: VersionSelect(*args, show_force_blockstate=False),
            VersionSelect,
        ):
            dialog = wx.Dialog(None)
            sizer = wx.BoxSizer()
            dialog.SetSizer(sizer)
            sizer.Add(cls(dialog, translation_manager), 0, wx.ALL, 5)
            dialog.Show()
            dialog.Fit()

            def get_on_close(dialog_):
                def on_close(evt):
                    dialog_.Destroy()
                return on_close
            dialog.Bind(wx.EVT_CLOSE, get_on_close(dialog))
        app.MainLoop()

    main()
