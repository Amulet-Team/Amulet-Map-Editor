from enum import Enum
from typing import Tuple, List, Dict, Any
import wx
from wx.lib.scrolledpanel import ScrolledPanel

import PyMCTranslate

from amulet.api.data_types import VersionNumberTuple
from amulet_map_editor import lang
from amulet_map_editor.api.wx.ui.simple import SimpleChoiceAny
from amulet_map_editor.api.wx.ui.events import EVT_CHILD_SIZE, ChildSizeEvent
from .block_container import FillBlockContainer, FindBlockContainer


class ReplaceMode(Enum):
    Single = 0
    Sequence = 1
    Map = 2


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

    def _post_change_size(self):
        """Call this to resize and notify parent elements."""
        wx.PostEvent(self, ChildSizeEvent(0))

    def _swap_blocks(self, evt):
        self._find.states, self._fill.states = self._fill.states, self._find.states
        self._post_change_size()

    def set_replace(self, replace: bool):
        self._find.Show(replace)
        self._swap_button.Show(replace)

    def set_expert(self, expert: bool):
        self._find.set_expert(expert)
        self._fill.set_expert(expert)

    @property
    def operation(self) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        return self._find.states, self._fill.states


class OperationContainer(ScrolledPanel):
    def __init__(self, parent: wx.Window):
        super().__init__(parent)
        self._operations: List[ReplaceOperationWidget] = []
        self._operation_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._operation_sizer)
        self.SetupScrolling(scroll_x=False)
        self.FitInside()

    def DoGetBestSize(self):
        sizer = self.GetSizer()
        if sizer is None:
            return -1, -1
        else:
            sx, sy = sizer.CalcMin()
            return (
                sx + wx.SystemSettings.GetMetric(wx.SYS_VSCROLL_X),
                sy,
            )

    def __iter__(self):
        yield from self._operations

    def add_operation(self, replace_operation: ReplaceOperationWidget):
        self._operation_sizer.Add(replace_operation, 0, wx.TOP, 5)
        self._operations.append(replace_operation)


class FillReplaceWidget(wx.Panel):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = None,
        **kwargs
    ):
        super().__init__(parent, **kwargs)
        self._translation_manager = translation_manager
        self._platform = platform
        self._version_number = version_number
        self._force_blockstate = force_blockstate

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(top_sizer, 0, wx.EXPAND)

        self._replace = wx.CheckBox(
            self, wx.ID_ANY, lang.get("program_3d_edit.fill_tool.replace")
        )
        self._replace.Bind(wx.EVT_CHECKBOX, self._on_check_change)
        top_sizer.Add(self._replace, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)

        self._expert = wx.CheckBox(self, wx.ID_ANY, "Expert")
        self._expert.Bind(wx.EVT_CHECKBOX, self._on_check_change)
        top_sizer.Add(self._expert, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)

        self._pull_source = wx.CheckBox(self, wx.ID_ANY, "Pull From Source")
        self._pull_source.Hide()
        top_sizer.Add(self._pull_source, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)

        self._multiple = wx.CheckBox(self, wx.ID_ANY, "Multiple")
        self._multiple.Hide()
        self._multiple.Bind(wx.EVT_CHECKBOX, self._on_check_change)
        top_sizer.Add(self._multiple, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)

        self._replace_mode = SimpleChoiceAny(self, sort=False)
        self._replace_mode.Hide()
        self._replace_mode.SetItems(
            {
                ReplaceMode.Single: lang.get(
                    "program_3d_edit.fill_tool.replace_mode.single"
                ),
                ReplaceMode.Sequence: lang.get(
                    "program_3d_edit.fill_tool.replace_mode.sequence"
                ),
                ReplaceMode.Map: lang.get("program_3d_edit.fill_tool.replace_mode.map"),
            }
        )
        top_sizer.Add(
            self._replace_mode, 0, wx.LEFT, 5
        )

        self._operation_panel = OperationContainer(self)
        sizer.Add(self._operation_panel, 0)
        self._add_operation()

    def _post_change_size(self):
        """Call this to resize and notify parent elements."""
        wx.PostEvent(self, ChildSizeEvent(0))

    def _add_operation(self):
        replace_operation = ReplaceOperationWidget(
            self._operation_panel,
            self._translation_manager,
            self._platform,
            self._version_number,
            self._force_blockstate
        )
        replace_operation.set_expert(self.is_expert)
        replace_operation.set_replace(self.is_replace)
        self._operation_panel.add_operation(replace_operation)
        self._operation_panel.FitInside()

    def _update_buttons(self):
        self._pull_source.Show(self.is_expert)
        # TODO: when multiple support is added uncomment this
        # self._multiple.Show(self.is_expert)
        # self._replace_mode.Show(self.is_expert and self._multiple.GetValue())
        for operation in self._operation_panel:
            operation.set_replace(self.is_replace)
            operation.set_expert(self.is_expert)
        self._post_change_size()

    def _on_check_change(self, evt):
        self._update_buttons()

    @property
    def is_replace(self) -> bool:
        """Is the replace check box ticked."""
        return self._replace.GetValue()

    @property
    def is_expert(self) -> bool:
        return self._expert.GetValue()

    @property
    def replace_mode(self) -> ReplaceMode:
        return self._replace_mode.GetCurrentObject()

    @property
    def operations(self) -> List[Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]]:
        return [op.operation for op in self._operation_panel]
