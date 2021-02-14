import wx
from typing import Union
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.programs.edit.api.edit_canvas_container import (
    EditCanvasContainer,
)
from amulet_map_editor.programs.edit.api.events import EVT_DRAW

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]


class BaseToolUI(EditCanvasContainer):
    @property
    def name(self) -> str:
        raise NotImplementedError

    def enable(self):
        """Bind any required events and start the tool."""
        self.canvas.camera.projection_mode = Projection.PERSPECTIVE

    def disable(self):
        """Stop the tool. All events on the canvas will be automatically removed."""
        pass

    def bind_events(self):
        self.canvas.Bind(EVT_DRAW, self._on_draw)

    def _on_draw(self, evt):
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.canvas.renderer.draw_level()
        self.canvas.renderer.end_draw()
