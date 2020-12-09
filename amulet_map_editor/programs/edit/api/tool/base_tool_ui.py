import wx
from typing import Union

from amulet_map_editor.api.opengl.canvas import Perspective
from amulet_map_editor.programs.edit.api.base_ui import BaseUI
from amulet_map_editor.programs.edit.api.ui.canvas.events import EVT_DRAW
from amulet_map_editor.programs.edit.api.ui.canvas import BlockSelectionMode

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]


class BaseToolUI(BaseUI):
    @property
    def name(self) -> str:
        raise NotImplementedError

    def enable(self):
        self.canvas.selection_mode = BlockSelectionMode
        self.canvas.projection_mode = Perspective

    def disable(self):
        pass

    def bind_events(self):
        self.canvas.Bind(EVT_DRAW, self._on_draw)

    def _on_draw(self, evt):
        self.canvas.start_draw()
        if self.canvas.projection_mode == Perspective:
            self.canvas.draw_sky_box()
        self.canvas.draw_level()
        self.canvas.draw_selection()
        self.canvas.end_draw()
