from enum import Enum
from typing import List, Optional

import wx

import PyMCTranslate

from amulet.api.data_types import VersionGroupType
from amulet_map_editor import lang
from amulet_map_editor.api.wx.ui.simple import SimpleChoiceAny, SimpleScrollablePanel
from amulet_map_editor.api.wx.ui.mc.version import (
    VersionSelect,
    VersionChangeEvent,
    EVT_VERSION_CHANGE,
)

from .replace_widget import ReplaceOperationWidget


class ReplaceMode(Enum):
    Single = 0
    Sequence = 1
    Map = 2


class FillReplaceWidget(wx.Panel):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        default_version: Optional[VersionGroupType] = None,
        **kwargs
    ):
        super().__init__(parent, **kwargs)
        self._translation_manager = translation_manager
        if default_version is None:
            default_version = (
                "java",
                max(translation_manager.version_numbers("java")),
                False,
            )
        self._default_version = default_version

        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(top_sizer, 0, wx.BOTTOM | wx.EXPAND, 5)

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
            self._replace_mode, 1, wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 5
        )

        self._operation_panel = SimpleScrollablePanel(self)
        sizer.Add(self._operation_panel, 1, wx.EXPAND)
        self._operation_sizer = wx.BoxSizer(wx.VERTICAL)
        self._operation_panel.SetSizer(self._operation_sizer)

        self._operations: List[ReplaceOperationWidget] = []
        self._add_operation()

        self.Layout()

    def _add_operation(self):
        replace_operation = ReplaceOperationWidget(
            self._operation_panel,
            self._translation_manager,
            *self._default_version,
        )
        replace_operation.set_expert(self.is_expert)
        replace_operation.set_replace(self.is_replace)
        self._operations.append(replace_operation)
        self._operation_sizer.Add(replace_operation, 0, wx.EXPAND | wx.BOTTOM, 5)

    def _update_buttons(self):
        self._pull_source.Show(self.is_expert)
        # TODO: when multiple support is added uncomment this
        # self._multiple.Show(self.is_expert)
        # self._replace_mode.Show(self.is_expert and self._multiple.GetValue())
        for operation in self._operations:
            operation.set_replace(self.is_replace)
            operation.set_expert(self.is_expert)
        self.GetTopLevelParent().Layout()

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
