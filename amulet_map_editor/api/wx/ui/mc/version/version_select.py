from amulet_map_editor.api.wx.ui.simple import SimpleChoice, ChoiceRaw
import wx
import PyMCTranslate
from typing import Optional, Dict, Any, Tuple

from amulet.api.data_types import VersionNumberTuple, PlatformType
from .platform_select import PlatformSelect
from amulet_map_editor.api.wx.ui.mc.state import VersionState, State
from .events import VersionChangeEvent, EVT_VERSION_CHANGE


class VersionSelect(PlatformSelect):
    """
    A UI element that allows you to pick between the platforms and versions in the translator.
    """

    state: VersionState

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        state: VersionState = None,
        platform: PlatformType = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        allow_universal: bool = True,
        allow_vanilla: bool = True,
        allowed_platforms: Tuple[PlatformType, ...] = None,
        show_force_blockstate: bool = True,
        allow_numerical: bool = True,
        allow_blockstate: bool = True,
        style: Dict[str, Any] = None,
    ):
        """
        Construct a :class:`VersionSelect` UI.

        :param parent: The parent window.
        :param translation_manager: The translation manager to populate from.
        :param state: optional VersionSelect instance holding the state of the platform and version.
        :param platform: The default platform (optional). If state is defined this will not be used.
        :param version_number: The default version number (optional). If state is defined this will not be used.
        :param force_blockstate: If True and the native format is numerical will use the custom blockstate format. Else will use the native format. If state is defined this will not be used.
        :param allow_universal: If True the universal format will be included.
        :param allow_vanilla: If True the vanilla formats will be included.
        :param allowed_platforms: A whitelist of platforms.
        :param show_force_blockstate: Should the format selection be shown to the user.
        :param allow_numerical: Should the numerical versions be shown to the user.
        :param allow_blockstate: Should the blockstate versions be shown to the user.
        :param style: Dictionary of keyword args to be given to the Panel.
        """
        # init the state
        if not isinstance(state, VersionState):
            state = VersionState(
                translation_manager,
                platform=platform,
                version_number=version_number,
                force_blockstate=force_blockstate,
            )

        super().__init__(
            parent,
            translation_manager,
            state=state,
            allow_universal=allow_universal,
            allow_vanilla=allow_vanilla,
            allowed_platforms=allowed_platforms,
            style=style,
        )
        self._allow_numerical = allow_numerical
        self._allow_blockstate = allow_blockstate

        self._version_choice: Optional[ChoiceRaw] = self._add_ui_element(
            "Version:", ChoiceRaw, reverse=True
        )
        self._update_version_number()
        self._version_choice.Bind(
            wx.EVT_CHOICE,
            self._on_version_number_change,
        )

        self._blockstate_choice: Optional[SimpleChoice] = self._add_ui_element(
            "Format:", SimpleChoice, shown=show_force_blockstate
        )
        self._blockstate_choice.SetItems(["native", "blockstate"])
        self._update_force_blockstate()
        self._blockstate_choice.Bind(wx.EVT_CHOICE, self._on_blockstate_change)

    # def _populate_version(self):
    #     """Populate the version UI element"""
        # TODO
        # versions = self._translation_manager.version_numbers(self.platform)
        # if not self._allow_blockstate:
        #     versions = [v for v in versions if v < (1, 13, 0)]
        # if not self._allow_numerical:
        #     versions = [v for v in versions if v >= (1, 13, 0)]
        # self._version_choice.SetItems(versions)

    def _update_version_number(self):
        """Push the internal version number state to the UI."""
        self._version_choice.SetItems(self.state.valid_version_numbers)
        self._version_choice.SetSelection(
            self._version_choice.values.index(self.state.version_number)
        )

    def _update_force_blockstate(self):
        """Push the internal block format state to the UI."""
        self._blockstate_choice.Enable(self.state.has_abstract_format)
        self._blockstate_choice.SetSelection(int(self.state.force_blockstate))

    def _on_state_change(self):
        super()._on_state_change()
        if self.state.is_changed(State.VersionNumber):
            self._update_version_number()
        if self.state.is_changed(State.ForceBlockstate):
            self._update_force_blockstate()

    def _post_version_change(self):
        wx.PostEvent(
            self,
            VersionChangeEvent(
                self.state.platform,
                self.state.version_number,
                self.state.force_blockstate,
            ),
        )

    def _on_version_number_change(self, evt):
        version = self._version_choice.GetCurrentObject()
        if version != self.state.version_number:
            with self.state as state:
                state.version_number = version
            self._post_version_change()

    def _on_blockstate_change(self, evt):
        force_blockstate = bool(self._version_choice.GetCurrentSelection())
        if force_blockstate != self.state.force_blockstate:
            with self.state as state:
                state.force_blockstate = force_blockstate
            self._post_version_change()


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
        select: VersionSelect = cls(dialog, translation_manager)
        sizer.Add(select, 0, wx.ALL, 5)
        dialog.Show()
        dialog.Fit()

        def on_change(evt: VersionChangeEvent):
            print(
                evt.platform,
                evt.version_number,
                evt.force_blockstate,
            )

        select.Bind(EVT_VERSION_CHANGE, on_change)

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
            with obj.state as state:
                state.platform = platform
                state.version_number = version
                state.force_blockstate = force_blockstate

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
            with obj.state as state:
                state.force_blockstate = force_blockstate
                state.version_number = version
                state.platform = platform

        wx.CallLater(interval * 5, set_version2, select, "java", (1, 15, 0), False)
        wx.CallLater(interval * 6, set_version2, select, "java", (1, 17, 0), False)
        wx.CallLater(interval * 7, set_version2, select, "bedrock", (1, 15, 0), False)
        wx.CallLater(interval * 8, set_version2, select, "bedrock", (1, 17, 0), False)

        def set_platform(obj: VersionSelect, platform: PlatformType):
            obj.platform = platform

        wx.CallLater(interval * 9, set_platform, select, "java")
        wx.CallLater(interval * 10, set_platform, select, "bedrock")
