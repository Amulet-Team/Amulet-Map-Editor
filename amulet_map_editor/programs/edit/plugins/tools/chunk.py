from typing import TYPE_CHECKING, Dict, Tuple
import wx
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
    GL_DEPTH_TEST,
    glEnable,
    glDisable,
    glGetBoolean,
)

from amulet_map_editor import lang
from amulet_map_editor.api.opengl.camera import Projection, EVT_CAMERA_MOVED
from amulet_map_editor.programs.edit.api.ui.tool import DefaultBaseToolUI
from amulet_map_editor.programs.edit.api.behaviour import ChunkSelectionBehaviour
from amulet.operations.delete_chunk import delete_chunk
from amulet.api.data_types import Dimension
from amulet_map_editor.programs.edit.plugins.operations.stock_plugins.internal_operations.prune_chunks import (
    prune_chunks,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class ChunkTool(wx.BoxSizer, DefaultBaseToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        DefaultBaseToolUI.__init__(self, canvas)

        self._selection = ChunkSelectionBehaviour(self.canvas)

        self._button_panel = wx.Panel(canvas)
        button_sizer = wx.BoxSizer(wx.VERTICAL)
        self._button_panel.SetSizer(button_sizer)

        y_sizer = wx.FlexGridSizer(2, 5, 5)
        button_sizer.Add(y_sizer, flag=wx.ALL, border=5)
        min_y_label = wx.StaticText(
            self._button_panel, label=lang.get("program_3d_edit.chunk_tool.min_y")
        )
        y_sizer.Add(min_y_label, flag=wx.ALIGN_CENTER)
        self._min_y = wx.SpinCtrl(
            self._button_panel,
            min=-30_000_000,
            max=30_000_000,
            initial=256,
        )
        self._min_y.SetToolTip(lang.get("program_3d_edit.chunk_tool.min_y_tooltip"))
        y_sizer.Add(self._min_y, flag=wx.ALIGN_CENTER)
        self._min_y.Bind(wx.EVT_SPINCTRL, self._on_update_clipping)

        max_y_label = wx.StaticText(
            self._button_panel, label=lang.get("program_3d_edit.chunk_tool.max_y")
        )
        y_sizer.Add(max_y_label, flag=wx.ALIGN_CENTER)
        self._max_y = wx.SpinCtrl(
            self._button_panel,
            min=-30_000_000,
            max=30_000_000,
            initial=0,
        )
        self._max_y.SetToolTip(lang.get("program_3d_edit.chunk_tool.max_y_tooltip"))
        y_sizer.Add(self._max_y, flag=wx.ALIGN_CENTER)
        self._max_y.Bind(wx.EVT_SPINCTRL, self._on_update_clipping)
        self._dimensions: Dict[Dimension, Tuple[int, int]] = {}

        delete_button = wx.Button(
            self._button_panel,
            label=lang.get("program_3d_edit.chunk_tool.delete_chunks"),
        )
        delete_button.SetToolTip(
            lang.get("program_3d_edit.chunk_tool.delete_chunks_tooltip")
        )
        button_sizer.Add(
            delete_button, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT | wx.EXPAND, 5
        )
        delete_button.Bind(wx.EVT_BUTTON, self._delete_chunks)

        prune_button = wx.Button(
            self._button_panel,
            label=lang.get("program_3d_edit.chunk_tool.prune_chunks"),
        )
        prune_button.SetToolTip(
            lang.get("program_3d_edit.chunk_tool.prune_chunks_tooltip")
        )
        button_sizer.Add(prune_button, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT | wx.EXPAND, 5)
        prune_button.Bind(wx.EVT_BUTTON, self._prune_chunks)

        self.Add(self._button_panel, 0, wx.ALIGN_CENTER_VERTICAL)

    @property
    def name(self) -> str:
        return "Chunk"

    def bind_events(self):
        super().bind_events()
        self._selection.bind_events()
        self.canvas.Bind(EVT_CAMERA_MOVED, self._on_update_clipping)

    def enable(self):
        self.Layout()
        self.canvas.camera.projection_mode = Projection.TOP_DOWN
        self._selection.enable()
        self._update_clipping()

        dimension = self.canvas.dimension
        if dimension not in self._dimensions:
            self._dimensions[dimension] = (
                min(
                    30_000_000,
                    max(-30_000_000, self.canvas.world.bounds(dimension).min[1]),
                ),
                min(
                    30_000_000,
                    max(-30_000_000, self.canvas.world.bounds(dimension).max[1]),
                ),
            )
        miny, maxy = self._dimensions[dimension]
        self._min_y.SetValue(miny)
        self._max_y.SetValue(maxy)
        self._update_clipping()

    def disable(self):
        super().disable()
        self.canvas.camera.orthographic_clipping = -(10 ** 5), 10 ** 5

    def _on_update_clipping(self, evt):
        self._update_clipping()
        evt.Skip()

    def _update_clipping(self):
        y = self.canvas.camera.location[1]
        self.canvas.camera.orthographic_clipping = (
            y - self._max_y.GetValue() - 1,
            y - self._min_y.GetValue() + 1,
        )

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
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self._selection.draw()
        else:
            depth_state = glGetBoolean(GL_DEPTH_TEST)
            if depth_state:
                glDisable(GL_DEPTH_TEST)
            clip = self.canvas.camera.orthographic_clipping
            self.canvas.camera.orthographic_clipping = -(10 ** 5), 10 ** 5
            self._selection.draw()
            self.canvas.camera.orthographic_clipping = clip
            if depth_state:
                glEnable(GL_DEPTH_TEST)
        self.canvas.renderer.end_draw()
