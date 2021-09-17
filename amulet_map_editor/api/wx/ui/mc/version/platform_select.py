from amulet_map_editor.api.wx.ui.simple import SimpleChoice
import wx
import PyMCTranslate
from typing import Tuple, Type, Any, Dict

from amulet.api.data_types import PlatformType
from .events import PlatformChangeEvent, EVT_PLATFORM_CHANGE
from amulet_map_editor.api.wx.ui.mc.state import PlatformState, StateHolder, State


class PlatformSelect(wx.Panel, StateHolder):
    """
    A UI element that allows you to pick between the platforms in the translator.
    """

    state: PlatformState

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        state: PlatformState = None,
        platform: PlatformType = None,
        allow_universal: bool = True,
        allow_vanilla: bool = True,
        allowed_platforms: Tuple[PlatformType, ...] = None,
        style: Dict[str, Any] = None,
    ):
        """
        Construct a :class:`PlatformSelect` UI.

        :param parent: The parent window.
        :param translation_manager: The translation manager to populate from.
        :param state: optional PlatformSelect instance holding the state of the platform.
        :param platform: The default platform (optional). If state is defined this will not be used.
        :param allow_universal: If True the universal format will be included.
        :param allow_vanilla: If True the vanilla formats will be included.
        :param allowed_platforms: A whitelist of platforms.
        :param style: Dictionary of keyword args to be given to the Panel.
        """
        # init the state
        if not isinstance(state, PlatformState):
            state = PlatformState(translation_manager, platform=platform)
        StateHolder.__init__(self, state)

        # init the panel
        style = style or {}
        style.setdefault("style", wx.BORDER_SIMPLE)
        wx.Panel.__init__(self, parent, **style)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self._sizer = wx.FlexGridSizer(2, 5, 5)
        sizer.Add(self._sizer, 1, wx.ALL | wx.EXPAND, 5)

        self._sizer.AddGrowableCol(0)
        self._sizer.AddGrowableCol(1)

        # self._allow_universal = allow_universal
        # self._allow_vanilla = allow_vanilla
        # self._allowed_platforms = allowed_platforms
        self._platform_choice: SimpleChoice = self._add_ui_element(
            "Platform:", SimpleChoice
        )
        self._update_platform()
        self._platform_choice.Bind(
            wx.EVT_CHOICE,
            self._on_platform_change,
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

    # def _populate_platform(self):
    #     """Update the UI with the valid platforms."""
        # TODO
        # platforms = self._translation_manager.platforms()
        # if self._allowed_platforms is not None:
        #     platforms = [p for p in platforms if p in self._allowed_platforms]
        # if not self._allow_universal:
        #     platforms = [p for p in platforms if p != "universal"]
        # if not self._allow_vanilla:
        #     platforms = [p for p in platforms if p == "universal"]
        # self._platform_choice.SetItems(self.state.valid_platforms)

    def _update_platform(self):
        """Push the internal platform state to the UI."""
        self._platform_choice.SetItems(self.state.valid_platforms)
        self._platform_choice.SetSelection(
            self._platform_choice.GetItems().index(self.state.platform)
        )

    def _on_state_change(self):
        if self.state.is_changed(State.Platform):
            self._update_platform()

    def _on_platform_change(self, evt):
        """The event run when the platform choice is changed by a user."""
        platform = self._platform_choice.GetCurrentString()
        if platform != self.state.platform:
            with self.state as state:
                state.platform = platform
            wx.PostEvent(self, PlatformChangeEvent(self.state.platform))


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    dialog = wx.Dialog(
        None,
        title="PlatformSelect",
        style=wx.DEFAULT_DIALOG_STYLE | wx.DIALOG_NO_PARENT,
    )
    sizer = wx.BoxSizer()
    dialog.SetSizer(sizer)
    obj = PlatformSelect(dialog, translation_manager, platform="java")
    sizer.Add(
        obj,
        1,
        wx.ALL | wx.EXPAND,
        5,
    )

    def set_data(platform: str):
        with obj.state as state:
            state.platform = platform

    wx.CallLater(1000, set_data, "bedrock")

    def on_change(evt: PlatformChangeEvent):
        print(evt.platform)

    obj.Bind(EVT_PLATFORM_CHANGE, on_change)
    dialog.Bind(wx.EVT_CLOSE, lambda evt: dialog.Destroy())
    dialog.Show()
    dialog.Fit()
