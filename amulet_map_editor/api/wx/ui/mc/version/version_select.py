from amulet_map_editor.api.wx.ui.simple import SimpleChoice, SimpleChoiceAny
import wx
import PyMCTranslate
from typing import Optional, Dict, Any, Tuple

from amulet.api.data_types import VersionNumberTuple, PlatformType
from .platform_select import PlatformSelect
from amulet_map_editor.api.wx.ui.mc.base.api.version import BaseMCVersion
from .events import (
    VersionChangeEvent,
)


class VersionSelect(PlatformSelect, BaseMCVersion):
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
        allow_universal: bool = True,
        allow_vanilla: bool = True,
        allowed_platforms: Tuple[PlatformType, ...] = None,
        show_force_blockstate: bool = True,
        allow_numerical: bool = True,
        allow_blockstate: bool = True,
        state: Dict[str, Any] = None,
        **kwargs,
    ):
        """
        Construct a :class:`VersionSelect` UI.

        :param parent: The parent window.
        :param translation_manager: The translation manager to populate from.
        :param platform: The default platform (optional)
        :param version_number: The default version number (optional)
        :param force_blockstate: If True and the native format is numerical will use the custom blockstate format. Else will use the native format.
        :param allow_universal: If True the universal format will be included.
        :param allow_vanilla: If True the vanilla formats will be included.
        :param allowed_platforms: A whitelist of platforms.
        :param show_force_blockstate: Should the format selection be shown to the user.
        :param allow_numerical: Should the numerical versions be shown to the user.
        :param allow_blockstate: Should the blockstate versions be shown to the user.
        :param state: A dictionary containing kwargs passed to the state manager.
        :param kwargs: Keyword args to be given to the :class:`PlatformSelect` and Panel.
        """
        state = state or {}
        state.setdefault("version_number", version_number)
        state.setdefault("force_blockstate", force_blockstate)
        super().__init__(
            parent,
            translation_manager,
            platform,
            allow_universal=allow_universal,
            allow_vanilla=allow_vanilla,
            allowed_platforms=allowed_platforms,
            state=state,
            **kwargs,
        )
        self._allow_numerical = allow_numerical
        self._allow_blockstate = allow_blockstate

        self._version_choice: Optional[SimpleChoiceAny] = self._add_ui_element(
            "Version:", SimpleChoiceAny, reverse=True
        )
        self._populate_version()
        self._push_version_number()
        self._version_choice.Bind(
            wx.EVT_CHOICE,
            self._on_version_number_change,
        )

        self._blockstate_choice: Optional[SimpleChoice] = self._add_ui_element(
            "Format:", SimpleChoice, shown=show_force_blockstate
        )
        self._blockstate_choice.SetItems(["native", "blockstate"])
        self._blockstate_choice.SetSelection(0)
        self._populate_blockstate()
        self._push_force_blockstate()
        self._blockstate_choice.Bind(wx.EVT_CHOICE, self._on_blockstate_change)

    def _init_state(self, state: Dict[str, Any]):
        """
        Call the init method of the state manager.
        This is here so that nested classes do not have to init the state managers multiple times.
        """
        BaseMCVersion.__init__(self, **state)

    def _populate_version(self):
        """Populate the version UI element"""
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

    def _push_version_number(self):
        """Push the internal version number state to the UI."""
        self._version_choice.SetSelection(
            self._version_choice.values.index(self.version_number)
        )

    def _push_force_blockstate(self):
        """Push the internal block format state to the UI."""
        self._blockstate_choice.SetSelection(int(self.force_blockstate))

    def _on_change(self, changed: int):
        """
        Handle the UI changes and create an event.

        :param changed: 1=platform, 2=version, 3=blockstate
        :return:
        """
        old_platform = self.platform
        old_version = self.version_number
        old_force_blockstate = self.force_blockstate

        if changed <= 1:
            # write the changes back to the internal state
            new_platform = self._platform_choice.GetCurrentString()
            self.set_platform(new_platform)
        else:
            new_platform = old_platform

        if changed <= 2:
            if changed < 2:
                self._populate_version()
                self._version_choice.SetSelection(0)
            new_version = self._version_choice.GetCurrentObject()
            self.set_version_number(new_version)
        else:
            new_version = old_version

        if changed < 3:
            self._populate_blockstate()
            self._blockstate_choice.SetSelection(0)
        new_force_blockstate = (
            self._blockstate_choice.GetCurrentString() == "blockstate"
        )
        self.set_force_blockstate(new_force_blockstate)

        wx.PostEvent(
            self,
            VersionChangeEvent(
                new_platform,
                new_version,
                new_force_blockstate,
                old_platform,
                old_version,
                old_force_blockstate,
            ),
        )

    def _on_platform_change(self, evt):
        self._on_change(1)

    def _on_version_number_change(self, evt):
        self._on_change(2)

    def _on_blockstate_change(self, evt):
        self._on_change(3)

    def update(self) -> bool:
        update = super().update()
        # If the user set these out of order they may be messed up.
        # This should fix that.
        self.set_version_number(self.version_number)
        self.set_force_blockstate(self.force_blockstate)

        if update:
            self._populate_version()
        if update or self.version_number != self._version_choice.GetCurrentObject():
            self._push_version_number()
            update = True
        if update:
            self._populate_blockstate()
        if update or self.force_blockstate != (
            self._blockstate_choice.GetCurrentString() == "blockstate"
        ):
            self._push_force_blockstate()
            update = True
        return update


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    for cls, title in (
        (
            lambda *args: VersionSelect(*args, show_force_blockstate=False),
            "VersionSelect without format choice",
        ),
        (VersionSelect, "VersionSelect with format choice"),
    ):
        dialog = wx.Dialog(
            None, title=title, style=wx.DEFAULT_DIALOG_STYLE | wx.DIALOG_NO_PARENT
        )
        sizer = wx.BoxSizer()
        dialog.SetSizer(sizer)
        select = cls(dialog, translation_manager)
        sizer.Add(select, 0, wx.ALL, 5)
        dialog.Show()
        dialog.Fit()

        def get_on_close(dialog_):
            def on_close(evt):
                dialog_.Destroy()

            return on_close

        dialog.Bind(wx.EVT_CLOSE, get_on_close(dialog))

        def set_version(
            obj: VersionSelect,
            platform: PlatformType,
            version: VersionNumberTuple,
            force_blockstate: bool,
        ):
            obj.set_platform(platform)
            obj.set_version_number(version)
            obj.set_force_blockstate(force_blockstate)
            obj.update()

        interval = 1_000

        wx.CallLater(interval * 1, set_version, select, "java", (1, 15, 0), False)
        wx.CallLater(interval * 2, set_version, select, "java", (1, 17, 0), False)
        wx.CallLater(interval * 3, set_version, select, "bedrock", (1, 15, 0), False)
        wx.CallLater(interval * 4, set_version, select, "bedrock", (1, 17, 0), False)

        def set_version2(
            obj: VersionSelect,
            platform: PlatformType,
            version: VersionNumberTuple,
            force_blockstate: bool,
        ):
            obj.set_force_blockstate(force_blockstate)
            obj.set_version_number(version)
            obj.set_platform(platform)
            obj.update()

        wx.CallLater(interval * 5, set_version2, select, "java", (1, 15, 0), False)
        wx.CallLater(interval * 6, set_version2, select, "java", (1, 17, 0), False)
        wx.CallLater(interval * 7, set_version2, select, "bedrock", (1, 15, 0), False)
        wx.CallLater(interval * 8, set_version2, select, "bedrock", (1, 17, 0), False)

        def set_platform(obj: VersionSelect, platform: PlatformType):
            obj.platform = platform

        wx.CallLater(interval * 9, set_platform, select, "java")
        wx.CallLater(interval * 10, set_platform, select, "bedrock")
