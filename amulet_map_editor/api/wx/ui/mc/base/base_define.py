import wx
import wx.lib.scrolledpanel
from typing import Optional, Dict, Any

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple, PlatformType

from amulet_map_editor.api.wx.ui.mc.base.base_identifier_select import (
    BaseIdentifierSelect,
)
from amulet_map_editor.api.wx.ui.mc import version as mc_version
from amulet_map_editor.api.wx.ui.mc.base.api import BaseMCVersion


class BaseDefine(wx.Panel, BaseMCVersion):
    def __init__(
        self,
        parent,
        translation_manager: PyMCTranslate.TranslationManager,
        orientation=wx.VERTICAL,
        platform: PlatformType = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = False,
        state: Dict[str, Any] = None,
        style: Dict[str, Any] = None,
        **kwargs,
    ):
        state = state or {}
        state.setdefault("translation_manager", translation_manager)
        state.setdefault("platform", platform)
        state.setdefault("version_number", version_number)
        state.setdefault("force_blockstate", force_blockstate)
        # This is the init call to the class that stores the internal state of the data.
        # This needs to be at the start to ensure that the internal state is set up before anything else is done.
        # It is not a direct call to init so that subclasses of this class can substitute in which state subclass is used.
        self._init_state(state)
        wx.Panel.__init__(self, parent)

        self._orientation = orientation
        self._sizer = wx.BoxSizer(orientation)
        self.SetSizer(self._sizer)

        self._top_sizer = wx.BoxSizer(wx.VERTICAL)
        if orientation == wx.HORIZONTAL:
            self._sizer.Add(self._top_sizer, 1, wx.EXPAND)
        else:
            self._sizer.Add(self._top_sizer, 2, wx.EXPAND)

        self._version_picker = mc_version.VersionSelect(
            self,
            translation_manager,
            platform,
            version_number,
            force_blockstate,
            style=style,
            **kwargs,
        )
        self._top_sizer.Add(self._version_picker, 0, wx.EXPAND)
        self._version_picker.Bind(
            mc_version.EVT_VERSION_CHANGE, self._on_version_change
        )

        self._picker: Optional[BaseIdentifierSelect] = None

        self.Layout()

    def _init_state(self, state: Dict[str, Any]):
        """
        Call the init method of the state manager.
        This is here so that nested classes do not have to init the state managers multiple times.
        """
        BaseMCVersion.__init__(self, **state)

    def _on_version_change(self, evt: mc_version.VersionChangeEvent):
        raise NotImplementedError

    def push(self) -> bool:
        self.set_platform(self.platform)
        self.set_version_number(self.version_number)
        self.set_force_blockstate(self.force_blockstate)
        if (
            self.platform != self._version_picker.platform
            or self.version_number != self._version_picker.version_number
            or self.force_blockstate != self._version_picker.force_blockstate
        ):
            self._version_picker.set_platform(self.platform)
            self._version_picker.set_version_number(self.version_number)
            self._version_picker.set_force_blockstate(self.force_blockstate)
            self._version_picker.push()
            return True
        return False
