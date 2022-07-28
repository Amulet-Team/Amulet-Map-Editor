from amulet_map_editor.api.wx.ui.simple import SimpleChoice, ChoiceRaw
import wx
import PyMCTranslate
from typing import Optional

from amulet.api.data_types import VersionNumberTuple, PlatformType
from amulet_map_editor import lang
from amulet_map_editor.api.wx.ui.mc.state import VersionState, State
from .platform_select import PlatformSelect
from .events import VersionChangeEvent, EVT_VERSION_CHANGE


class VersionSelect(PlatformSelect):
    """
    A UI element that allows you to pick between the platforms and versions in the translator.
    """

    state: VersionState

    def __init__(
        self,
        parent: wx.Window,
        state: VersionState,
        *,
        show_force_blockstate: bool = True,
        **kwargs,
    ):
        """
        Construct a :class:`VersionSelect` UI.

        :param parent: The parent window.
        :param state: optional VersionSelect instance holding the state of the platform and version.
        """
        super().__init__(parent, state, **kwargs)

        self._version_choice: Optional[ChoiceRaw] = self._add_ui_element(
            lang.get("widget.mc.version"), ChoiceRaw, reverse=True, sort=True
        )
        self._update_version_number()
        self._version_choice.Bind(
            wx.EVT_CHOICE,
            self._on_version_number_change,
        )

        self._blockstate_choice: Optional[SimpleChoice] = self._add_ui_element(
            lang.get("widget.mc.block_format"),
            SimpleChoice,
            shown=show_force_blockstate,
        )
        self._blockstate_choice.SetItems(
            [
                lang.get("widget.mc.block_format.native"),
                lang.get("widget.mc.block_format.blockstate"),
            ]
        )
        self._update_force_blockstate()
        self._blockstate_choice.Bind(wx.EVT_CHOICE, self._on_blockstate_change)

    @classmethod
    def from_data(
        cls,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        show_force_blockstate: bool = True,
        **kwargs,
    ):
        """
        :param parent: The parent window.
        :param translation_manager: The translation manager to populate from.
        :param show_force_blockstate: Should the format selection be shown to the user.
        """
        return cls(
            parent,
            VersionState(translation_manager, **kwargs),
            show_force_blockstate=show_force_blockstate,
        )

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

    def _post_change(self):
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
            self._post_change()

    def _on_blockstate_change(self, evt):
        force_blockstate = bool(self._version_choice.GetCurrentSelection())
        if force_blockstate != self.state.force_blockstate:
            with self.state as state:
                state.force_blockstate = force_blockstate
            self._post_change()


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    for cls, title in (
        (
            lambda *args: VersionSelect.from_data(*args, show_force_blockstate=False),
            "VersionSelect without format choice",
        ),
        (VersionSelect.from_data, "VersionSelect with format choice"),
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
