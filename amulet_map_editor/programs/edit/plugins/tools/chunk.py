from typing import TYPE_CHECKING
import wx

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.programs.edit.api.ui.tool import CameraToolUI
from amulet.operations.delete_chunk import delete_chunk

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class ChunkTool(wx.BoxSizer, CameraToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        CameraToolUI.__init__(self, canvas)

        self._button_panel = wx.Panel(canvas)
        button_sizer = wx.BoxSizer(wx.VERTICAL)
        self._button_panel.SetSizer(button_sizer)

        delete_button = wx.Button(self._button_panel, label="Delete Chunks")
        button_sizer.Add(delete_button, 0, wx.ALL | wx.EXPAND, 5)
        delete_button.Bind(wx.EVT_BUTTON, self._delete_chunks)

        self.Add(self._button_panel, 0, wx.ALIGN_CENTER_VERTICAL)

    @property
    def name(self) -> str:
        return "Chunk"

    def enable(self):
        self.Layout()
        self.canvas.camera.projection_mode = Projection.TOP_DOWN

    def disable(self):
        super().disable()

    def _delete_chunks(self, evt):
        self.canvas.run_operation(
            lambda: delete_chunk(self.canvas.world, self.canvas.dimension, self.canvas.selection.selection_group)
        )
