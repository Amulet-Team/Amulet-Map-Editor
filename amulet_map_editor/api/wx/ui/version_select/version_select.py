from amulet_map_editor.api.wx.ui.simple import SimpleChoice, SimpleChoiceAny
import wx
import PyMCTranslate
from typing import Tuple, Optional

from amulet.api.data_types import VersionNumberTuple, PlatformType
from .platform_select import PlatformSelect
from .events import (
    PlatformChangeEvent,
    EVT_PLATFORM_CHANGE,
    VersionNumberChangeEvent,
    EVT_VERSION_NUMBER_CHANGE,
    VersionChangeEvent,
)


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
                VersionNumberChangeEvent(self.version_number),
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
            VersionChangeEvent(
                self.platform,
                self.version_number,
                self.force_blockstate,
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
            VersionNumberChangeEvent(self.version_number),
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

    def _on_platform_change(self, evt: PlatformChangeEvent):
        self._populate_version()
        self.version_number = None
        evt.Skip()

    def _on_version_number_change(self, evt: VersionChangeEvent):
        self._populate_blockstate()
        self.force_blockstate = None
        evt.Skip()
