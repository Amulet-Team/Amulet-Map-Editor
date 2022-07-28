from amulet_map_editor.api.wx.ui.simple import SimpleChoice
import wx
import PyMCTranslate
from typing import Type, Any

from amulet_map_editor import lang
from amulet_map_editor.api.wx.ui.mc.state import PlatformState, StateHolder, State
from .events import PlatformChangeEvent, EVT_PLATFORM_CHANGE


class PlatformSelect(wx.Panel, StateHolder):
    """
    A UI element that allows you to pick between the platforms in the translator.
    """

    state: PlatformState

    def __init__(
        self,
        parent: wx.Window,
        state: PlatformState,
        **kwargs,
    ):
        """
        Construct a :class:`PlatformSelect` UI.

        :param parent: The parent window.
        :param state: optional PlatformSelect instance holding the state of the platform.
        """
        # init the state
        StateHolder.__init__(self, state)

        # init the panel
        wx.Panel.__init__(self, parent, style=wx.BORDER_SIMPLE)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self._sizer = wx.FlexGridSizer(2, 5, 5)
        sizer.Add(self._sizer, 1, wx.ALL | wx.EXPAND, 5)

        self._sizer.AddGrowableCol(0)
        self._sizer.AddGrowableCol(1)

        self._platform_choice: SimpleChoice = self._add_ui_element(
            lang.get("widget.mc.platform"), SimpleChoice
        )
        self._update_platform()
        self._platform_choice.Bind(
            wx.EVT_CHOICE,
            self._on_platform_change,
        )

    @classmethod
    def from_data(
        cls,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        **kwargs,
    ):
        """
        :param parent: The parent window.
        :param translation_manager: The translation manager to populate from.
        """
        return cls(
            parent,
            PlatformState(
                translation_manager,
                **kwargs,
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

    def _update_platform(self):
        """Push the internal platform state to the UI."""
        self._platform_choice.SetItems(self.state.valid_platforms)
        self._platform_choice.SetSelection(
            self._platform_choice.GetItems().index(self.state.platform)
        )

    def _on_state_change(self):
        if self.state.is_changed(State.Platform):
            self._update_platform()

    def _post_change(self):
        wx.PostEvent(self, PlatformChangeEvent(self.state.platform))

    def _on_platform_change(self, evt):
        """The event run when the platform choice is changed by a user."""
        platform = self._platform_choice.GetCurrentString()
        if platform != self.state.platform:
            with self.state as state:
                state.platform = platform
            self._post_change()


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
    obj = PlatformSelect.from_data(dialog, translation_manager, platform="java")
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
