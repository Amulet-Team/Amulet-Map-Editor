import wx
from typing import Union
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)
import traceback
import os

import amulet
from amulet.api.errors import LoaderNoneMatched
from amulet_map_editor import log

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
        self.canvas.DragAcceptFiles(True)
        self.canvas.Bind(wx.EVT_DROP_FILES, self._on_drop_files)

    def _on_draw(self, evt):
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.canvas.renderer.draw_level()
        self.canvas.renderer.end_draw()

    def _on_drop_files(self, evt: wx.DropFilesEvent):
        paths = evt.GetFiles()
        if paths:
            pathname = paths[0]
            if os.path.isfile(pathname):
                # TODO: if importing worlds get supported fix this
                try:
                    level = amulet.load_level(pathname)
                except LoaderNoneMatched:
                    wx.MessageBox(f"Could not find a matching loader for {pathname}.")
                    log.error(f"Could not find a matching loader for {pathname}.")
                except Exception as e:
                    log.error(
                        f"Could not open {pathname}. Check the console for more details.\n{traceback.format_exc()}"
                    )
                    wx.MessageBox(
                        f"Could not open {pathname}. Check the console for more details.\n{e}"
                    )
                else:
                    self.canvas.paste(level, level.dimensions[0])
        evt.Skip()
