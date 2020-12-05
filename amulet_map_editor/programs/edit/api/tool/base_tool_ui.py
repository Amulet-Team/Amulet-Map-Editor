import wx
from typing import Union, TYPE_CHECKING
from OpenGL.GL import (
    glClear,
    GL_COLOR_BUFFER_BIT,
    GL_DEPTH_BUFFER_BIT,
)

from amulet_map_editor.programs.edit.api.base_ui import BaseUI
from amulet_map_editor.programs.edit.api.ui.canvas.events import EVT_DRAW

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.ui.canvas.edit_canvas import EditCanvas

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]


class BaseToolUI(BaseUI):
    @property
    def name(self) -> str:
        raise NotImplementedError

    def enable(self):
        pass

    def disable(self):
        pass

    def bind_events(self):
        self.canvas.Bind(EVT_DRAW, self._on_draw)

    def _on_draw(self, evt):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.canvas.draw_sky_box()
        self.canvas.draw_level()
        self.canvas.SwapBuffers()
