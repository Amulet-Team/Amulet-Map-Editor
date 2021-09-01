import wx

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple
from amulet_map_editor import lang
from .block_container import FillBlockContainer, FindBlockContainer


class ReplaceOperationWidget(wx.Panel):
    """A widget containing a single Fill and optional Find widget."""

    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        **kwargs,
    ):
        kwargs["style"] = kwargs.get("style", 0) | wx.BORDER_SIMPLE
        super().__init__(parent, **kwargs)
        self._replace = False

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        self._find = FindBlockContainer(
            self, translation_manager, platform, version_number, force_blockstate
        )
        self._find.Hide()
        sizer.Add(self._find, 0, wx.EXPAND | wx.ALL, 5)

        self._swap_button = wx.Button(
            self, wx.ID_ANY, lang.get("program_3d_edit.fill_tool.swap")
        )
        self._swap_button.Bind(wx.EVT_BUTTON, self._swap_blocks)
        self._swap_button.Hide()
        sizer.Add(self._swap_button, 0, wx.EXPAND | wx.ALL, 5)

        self._fill = FillBlockContainer(
            self, translation_manager, platform, version_number, force_blockstate
        )
        sizer.Add(self._fill, 0, wx.EXPAND | wx.ALL, 5)

        self.Layout()

    def _swap_blocks(self, evt):
        self.Freeze()
        self._find.states, self._fill.states = self._fill.states, self._find.states
        self.GetTopLevelParent().Layout()
        self.Thaw()

    def set_replace(self, replace: bool):
        self._find.Show(replace)
        self._swap_button.Show(replace)

    def set_expert(self, expert: bool):
        self._find.set_expert(expert)
        self._fill.set_expert(expert)
