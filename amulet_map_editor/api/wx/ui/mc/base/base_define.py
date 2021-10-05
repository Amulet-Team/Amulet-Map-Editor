import wx
import wx.lib.scrolledpanel

import PyMCTranslate

from amulet_map_editor.api.wx.ui.mc.base.base_identifier_select import (
    BaseIdentifierSelect,
)
from amulet_map_editor.api.wx.ui.mc.version import (
    VersionSelect,
)
from amulet_map_editor.api.wx.ui.mc.state import BaseResourceIDState, StateHolder


class BaseDefine(wx.Panel, StateHolder):
    _version_picker: VersionSelect
    _identifier_select: BaseIdentifierSelect
    state: BaseResourceIDState

    def __init__(
        self,
        parent,
        translation_manager: PyMCTranslate.TranslationManager,
        *,
        state: BaseResourceIDState = None,
        orientation=wx.VERTICAL,
    ):
        assert isinstance(state, BaseResourceIDState)
        StateHolder.__init__(self, state)
        wx.Panel.__init__(self, parent)

        self._orientation = orientation
        self._sizer = wx.BoxSizer(orientation)
        self.SetSizer(self._sizer)

        self._top_sizer = wx.BoxSizer(wx.VERTICAL)
        if orientation == wx.HORIZONTAL:
            self._sizer.Add(self._top_sizer, 1, wx.EXPAND)
        else:
            self._sizer.Add(self._top_sizer, 0, wx.EXPAND)

        self._version_picker = VersionSelect(
            self, translation_manager, state=self.state
        )
        self._top_sizer.Add(self._version_picker, 0, wx.EXPAND)

        self.Layout()
