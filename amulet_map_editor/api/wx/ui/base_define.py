import wx
import wx.lib.scrolledpanel
from typing import Tuple, Type

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple, PlatformType

from amulet_map_editor.api.wx.ui.base_select import EVT_ITEM_CHANGE, BaseSelect
from amulet_map_editor.api.wx.ui.version_select import (
    VersionSelect,
    EVT_VERSION_CHANGE,
)


class BaseDefine(wx.Panel):
    def __init__(
        self,
        parent,
        translation_manager: PyMCTranslate.TranslationManager,
        select_type: Type[BaseSelect],
        orientation=wx.VERTICAL,
        platform: str = None,
        version_number: Tuple[int, int, int] = None,
        namespace: str = None,
        default_name: str = None,
        show_pick: bool = False,
        **kwargs,
    ):
        super().__init__(parent)

        self._translation_manager = translation_manager
        self._orientation = orientation
        self._sizer = wx.BoxSizer(orientation)
        left_sizer = wx.BoxSizer(wx.VERTICAL)
        if orientation == wx.HORIZONTAL:
            self._sizer.Add(left_sizer, 1, wx.EXPAND)
        else:
            self._sizer.Add(left_sizer, 2, wx.EXPAND)

        self._version_picker = VersionSelect(
            self,
            translation_manager,
            platform,
            version_number,
            **kwargs,
        )
        left_sizer.Add(self._version_picker, 0, wx.EXPAND)
        self._version_picker.Bind(EVT_VERSION_CHANGE, self._on_version_change)

        self._picker = select_type(
            self,
            translation_manager,
            self._version_picker.platform,
            self._version_picker.version_number,
            self._version_picker.force_blockstate,
            namespace,
            default_name,
            show_pick,
        )
        left_sizer.Add(self._picker, 1, wx.EXPAND | wx.TOP, 5)
        self._picker.Bind(EVT_ITEM_CHANGE, self._on_picker_change)

        self.SetSizerAndFit(self._sizer)
        self.Layout()

    def _on_picker_change(self, evt):
        raise NotImplementedError("This method should be overridden in child classes.")

    def _on_version_change(self, evt):
        self._picker.version = (
            evt.platform,
            evt.version_number,
            evt.force_blockstate,
        )
        evt.Skip()

    @property
    def platform(self) -> PlatformType:
        return self._version_picker.platform

    @platform.setter
    def platform(self, platform: PlatformType):
        self._version_picker.platform = platform

    @property
    def version_number(self) -> VersionNumberTuple:
        return self._version_picker.version_number

    @version_number.setter
    def version_number(self, version_number: VersionNumberTuple):
        self._version_picker.version_number = version_number

    @property
    def version(self) -> Tuple[PlatformType, VersionNumberTuple, bool]:
        return self._version_picker.version

    @version.setter
    def version(self, version: Tuple[PlatformType, VersionNumberTuple, bool]):
        self._version_picker.version = version

    @property
    def namespace(self) -> str:
        return self._picker.namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self._picker.namespace = namespace
