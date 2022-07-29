import logging
import wx
from typing import TYPE_CHECKING
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)
import traceback
import os

import amulet
from amulet.api.errors import LoaderNoneMatched

from amulet_map_editor.api.wx.ui.traceback_dialog import TracebackDialog
from amulet_map_editor.api.opengl.camera import Projection
from .base_tool_ui import BaseToolUI
from amulet_map_editor.programs.edit.api.events import EVT_DRAW
from amulet_map_editor.programs.edit.api.behaviour import CameraBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

log = logging.getLogger(__name__)


class DefaultBaseToolUI(BaseToolUI):
    """A base class for tools that adds a render loop, camera behaviour and file dropping logic."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
        self._camera_behaviour = CameraBehaviour(self.canvas)

    @property
    def name(self) -> str:
        """The name of the tool."""
        raise NotImplementedError

    def enable(self):
        """Set the state of the tool for being enabled."""
        self.canvas.camera.projection_mode = Projection.PERSPECTIVE

    def bind_events(self):
        """Bind all required events to the canvas.
        All events on the canvas will be automatically removed after the tool is disabled.
        """
        self.canvas.Bind(EVT_DRAW, self._on_draw)
        self.canvas.SetDropTarget(None)  # fixes #239
        self.canvas.DragAcceptFiles(True)
        self.canvas.Bind(wx.EVT_DROP_FILES, self._on_drop_files)
        self._camera_behaviour.bind_events()

    def _on_draw(self, evt):
        """The render loop for this tool."""
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.canvas.renderer.draw_level()
        self.canvas.renderer.end_draw()

    def _on_drop_files(self, evt: wx.DropFilesEvent):
        """Logic to run when a file is dropped into the canvas."""
        paths = evt.GetFiles()
        if paths:
            pathname = paths[0]
            if os.path.isfile(pathname):
                # TODO: if importing worlds get supported fix this
                try:
                    level = amulet.load_level(pathname)
                except LoaderNoneMatched:
                    msg = f"Could not find a matching loader for {pathname}."
                    wx.MessageBox(msg)
                    log.error(msg)
                except Exception as e:
                    log.error(f"Could not open {pathname}.", exc_info=True)
                    dialog = TracebackDialog(
                        self.canvas,
                        f"Could not open {pathname}.",
                        str(e),
                        traceback.format_exc(),
                    )
                    dialog.ShowModal()
                    dialog.Destroy()
                else:
                    self.canvas.paste(level, level.dimensions[0])
        evt.Skip()
