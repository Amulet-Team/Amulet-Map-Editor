import wx
from typing import Union

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.programs.edit.api.edit_canvas_container import (
    EditCanvasContainer,
)
from amulet_map_editor.programs.edit.api.events import EVT_DRAW
# from amulet_map_editor.programs.edit.api.ui.canvas_old import BlockSelectionMode

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]


class BaseToolUI(EditCanvasContainer):
    @property
    def name(self) -> str:
        raise NotImplementedError

    def enable(self):
        # self.canvas.selection_mode = BlockSelectionMode
        self.canvas.camera.projection_mode = Projection.PERSPECTIVE

    def disable(self):
        pass

    def bind_events(self):
        self.canvas.Bind(EVT_DRAW, self._on_draw)

    def _on_draw(self, evt):
        # self.canvas.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
        self.canvas.renderer.draw_level()
        self.canvas.renderer.draw_selection()
        # self.canvas.end_draw()
