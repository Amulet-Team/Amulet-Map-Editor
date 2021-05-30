from amulet_map_editor.api.wx.ui.simple import SimpleChoice
import wx
import PyMCTranslate
from typing import Tuple, Type, Any

from amulet.api.data_types import PlatformType
from .events import PlatformChangeEvent


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
        kwargs.setdefault("style", wx.BORDER_SIMPLE)
        super().__init__(parent, **kwargs)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        self._sizer = wx.FlexGridSizer(2, 5, 5)
        sizer.Add(self._sizer, 1, wx.ALL | wx.EXPAND, 5)

        self._sizer.AddGrowableCol(0)
        self._sizer.AddGrowableCol(1)

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
            lambda evt: wx.PostEvent(self, PlatformChangeEvent(self.platform)),
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
        wx.PostEvent(self, PlatformChangeEvent(self.platform))

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


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    translation_manager = PyMCTranslate.new_translation_manager()
    dialog = wx.Dialog(None, title="PlatformSelect", style=wx.DEFAULT_DIALOG_STYLE | wx.DIALOG_NO_PARENT)
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
