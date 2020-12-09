from typing import TYPE_CHECKING
import wx

from amulet_map_editor.api.opengl.canvas import Orthographic
from amulet_map_editor.programs.edit.api.tool import BaseToolUI
from amulet_map_editor.programs.edit.api.ui.canvas import ChunkSelectionMode

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.ui.canvas.edit_canvas import EditCanvas


class ChunkTool(wx.BoxSizer, BaseToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        BaseToolUI.__init__(self, canvas)

    @property
    def name(self) -> str:
        return "Chunk"

    def enable(self):
        self.Layout()
        self.canvas.selection_editable = True
        self.canvas.selection_mode = ChunkSelectionMode
        self.canvas.projection_mode = Orthographic

    def disable(self):
        super().disable()
