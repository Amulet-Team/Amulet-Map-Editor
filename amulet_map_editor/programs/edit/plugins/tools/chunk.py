from typing import TYPE_CHECKING
import wx

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.programs.edit.api.ui.tool import BaseToolUI
# from amulet_map_editor.programs.edit.api.ui.canvas_old import ChunkSelectionMode

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class ChunkTool(wx.BoxSizer, BaseToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        BaseToolUI.__init__(self, canvas)

    @property
    def name(self) -> str:
        return "Chunk"

    def enable(self):
        self.Layout()
        # self.canvas.selection_editable = True
        # self.canvas.selection_mode = ChunkSelectionMode
        self.canvas.camera.projection_mode = Projection.TOP_DOWN

    def disable(self):
        super().disable()
