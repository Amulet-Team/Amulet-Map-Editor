from typing import TYPE_CHECKING
import wx

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.programs.edit.api.ui.tool import CameraToolUI

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class ChunkTool(wx.BoxSizer, CameraToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        CameraToolUI.__init__(self, canvas)

    @property
    def name(self) -> str:
        return "Chunk"

    def enable(self):
        self.Layout()
        self.canvas.camera.projection_mode = Projection.TOP_DOWN

    def disable(self):
        super().disable()
