from amulet_map_editor.api.wx.ui.simple import SimpleChoice
import wx
import PyMCTranslate
from typing import Tuple, Type, Any, Dict

from amulet.api.data_types import PlatformType
from .events import PlatformChangeEvent
from amulet_map_editor.api.wx.ui.mc.base.api.platform import BaseMCPlatform


class PlatformSelect(wx.Panel, BaseMCPlatform):
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
        state: Dict[str, Any] = None,
        style: Dict[str, Any] = None,
    ):
        """
        Construct a :class:`PlatformSelect` UI.

        :param parent: The parent window.
        :param translation_manager: The translation manager to populate from.
        :param platform: The default platform (optional)
        :param allow_universal: If True the universal format will be included.
        :param allow_vanilla: If True the vanilla formats will be included.
        :param allowed_platforms: A whitelist of platforms.
        :param state: A dictionary containing kwargs passed to the state manager.
        :param style: Dictionary of keyword args to be given to the Panel.
        """
        state = state or {}
        state.setdefault("translation_manager", translation_manager)
        state.setdefault("platform", platform)
        # This is the init call to the class that stores the internal state of the data.
        # This needs to be at the start to ensure that the internal state is set up before anything else is done.
        # It is not a direct call to init so that subclasses of this class can substitute in which state subclass is used.
        self._init_state(state)

        # Init the panel
        style = style or {}
        style.setdefault("style", wx.BORDER_SIMPLE)
        wx.Panel.__init__(self, parent, **style)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self._sizer = wx.FlexGridSizer(2, 5, 5)
        sizer.Add(self._sizer, 1, wx.ALL | wx.EXPAND, 5)

        self._sizer.AddGrowableCol(0)
        self._sizer.AddGrowableCol(1)

        self._allow_universal = allow_universal
        self._allow_vanilla = allow_vanilla
        self._allowed_platforms = allowed_platforms
        self._platform_choice: SimpleChoice = self._add_ui_element(
            "Platform:", SimpleChoice
        )
        self._populate_platform()
        self._push_platform()
        self._platform_choice.Bind(
            wx.EVT_CHOICE,
            self._on_platform_change,
        )

    def _init_state(self, state: Dict[str, Any]):
        """
        Call the init method of the state manager.
        This is here so that nested classes do not have to init the state managers multiple times.
        """
        BaseMCPlatform.__init__(self, **state)

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

    def _populate_platform(self):
        """Update the UI with the valid platforms."""
        platforms = self._translation_manager.platforms()
        if self._allowed_platforms is not None:
            platforms = [p for p in platforms if p in self._allowed_platforms]
        if not self._allow_universal:
            platforms = [p for p in platforms if p != "universal"]
        if not self._allow_vanilla:
            platforms = [p for p in platforms if p == "universal"]
        self._platform_choice.SetItems(platforms)

    def _push_platform(self):
        """Push the internal platform state to the UI."""
        self._platform_choice.SetSelection(
            self._platform_choice.GetItems().index(self.platform)
        )

    def _on_platform_change(self, evt):
        """The event run when the platform choice is changed by a user."""
        old_platform = self.platform
        new_platform = self._platform_choice.GetCurrentString()
        # write the changes back to the internal state
        self._set_platform(new_platform)
        wx.PostEvent(self, PlatformChangeEvent(new_platform, old_platform))

    def _on_push(self):
        if self.platform != self._platform_choice.GetCurrentString():
            self._push_platform()
            return True
        return False


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
    sizer.Add(
        PlatformSelect(dialog, translation_manager, "java"),
        1,
        wx.ALL | wx.EXPAND,
        5,
    )
    dialog.Bind(wx.EVT_CLOSE, lambda evt: dialog.Destroy())
    dialog.Show()
    dialog.Fit()
