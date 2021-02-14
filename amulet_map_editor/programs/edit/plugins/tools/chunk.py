from typing import TYPE_CHECKING
import wx
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.programs.edit.api.ui.tool import CameraToolUI
from amulet_map_editor.programs.edit.api.behaviour import ChunkSelectionBehaviour
from amulet.operations.delete_chunk import delete_chunk
from amulet_map_editor.programs.edit.plugins.operations.stock_plugins.internal_operations.prune_chunks import (
    prune_chunks,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class ChunkTool(wx.BoxSizer, CameraToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        CameraToolUI.__init__(self, canvas)

        self._selection = ChunkSelectionBehaviour(self.canvas)

        self._button_panel = wx.Panel(canvas)
        button_sizer = wx.BoxSizer(wx.VERTICAL)
        self._button_panel.SetSizer(button_sizer)

        delete_button = wx.Button(self._button_panel, label="Delete Chunks")
        button_sizer.Add(delete_button, 0, wx.ALL | wx.EXPAND, 5)
        delete_button.Bind(wx.EVT_BUTTON, self._delete_chunks)

        prune_button = wx.Button(self._button_panel, label="Prune Chunks")
        button_sizer.Add(prune_button, 0, wx.ALL | wx.EXPAND, 5)
        prune_button.Bind(wx.EVT_BUTTON, self._prune_chunks)

        self.Add(self._button_panel, 0, wx.ALIGN_CENTER_VERTICAL)

    @property
    def name(self) -> str:
        return "Chunk"

    def bind_events(self):
        super().bind_events()
        self._selection.bind_events()

    def enable(self):
        self.Layout()
        self.canvas.camera.projection_mode = Projection.TOP_DOWN
        self._selection.enable()

    def disable(self):
        super().disable()

    def _delete_chunks(self, evt):
        self.canvas.run_operation(
            lambda: delete_chunk(
                self.canvas.world,
                self.canvas.dimension,
                self.canvas.selection.selection_group,
            )
        )

    def _prune_chunks(self, evt):
        self.canvas.run_operation(
            lambda: prune_chunks(
                self.canvas.world,
                self.canvas.dimension,
                self.canvas.selection.selection_group,
            )
        )

    def _on_draw(self, evt):
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.canvas.renderer.draw_level()
        self._selection.draw()
        self.canvas.renderer.end_draw()
