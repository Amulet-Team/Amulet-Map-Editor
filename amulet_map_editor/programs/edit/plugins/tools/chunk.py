from typing import TYPE_CHECKING, Dict, Tuple, Optional
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
from amulet.api.level import BaseLevel
from amulet.api.selection import SelectionGroup
from amulet.api.chunk import Chunk
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

        create_button = wx.Button(
            self._button_panel,
            label=lang.get("program_3d_edit.chunk_tool.create_chunks"),
        )
        create_button.SetToolTip(
            lang.get("program_3d_edit.chunk_tool.create_chunks_tooltip")
        )
        button_sizer.Add(
            create_button, 0, wx.LEFT | wx.BOTTOM | wx.RIGHT | wx.EXPAND, 5
        )
        create_button.Bind(wx.EVT_BUTTON, self._create_chunks)

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
        self.canvas.camera.orthographic_clipping = -(10**5), 10**5

    def _on_update_clipping(self, evt):
        self._update_clipping()
        evt.Skip()

    def _update_clipping(self):
        y = self.canvas.camera.location[1]
        self.canvas.camera.orthographic_clipping = (
            y - self._max_y.GetValue() - 1,
            y - self._min_y.GetValue() + 1,
        )

    def _ask_delete_chunks(self) -> Optional[bool]:
        class DeleteChunksDialog(wx.Dialog):
            def __init__(self, *args, **kwds):
                kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
                wx.Dialog.__init__(self, *args, **kwds)
                self.SetTitle("Do you want to load the original chunk state?")

                sizer_1 = wx.BoxSizer(wx.VERTICAL)

                label_1 = wx.StaticText(
                    self,
                    wx.ID_ANY,
                    "Do you want to load the original chunk state?\n\n"
                    'Clicking "Yes" will allow you to undo this operation but the operation will take a while to process.\n\n'
                    'Clicking "No" will mean this operation cannot be undone.\n\n'
                    "Changes will not be made to the world until you save so closing before saving will not actually delete the chunks.",
                    style=wx.ALIGN_CENTER_HORIZONTAL,
                )
                label_1.Wrap(500)
                sizer_1.Add(label_1, 0, wx.ALL, 5)

                sizer_2 = wx.StdDialogButtonSizer()
                sizer_1.Add(sizer_2, 0, wx.ALIGN_RIGHT | wx.ALL, 4)

                self.button_YES = wx.Button(self, wx.ID_YES, "")
                self.button_YES.SetDefault()
                sizer_2.AddButton(self.button_YES)

                self.button_NO = wx.Button(self, wx.ID_NO, "")
                self.button_NO.Bind(wx.EVT_BUTTON, self._on_no)
                sizer_2.AddButton(self.button_NO)

                self.button_CANCEL = wx.Button(self, wx.ID_CANCEL, "")
                sizer_2.AddButton(self.button_CANCEL)

                sizer_2.Realize()

                self.SetSizer(sizer_1)
                sizer_1.Fit(self)

                self.SetAffirmativeId(self.button_YES.GetId())
                self.SetEscapeId(self.button_CANCEL.GetId())

                self.Layout()

            def _on_no(self, evt):
                self.EndModal(wx.ID_NO)

        d = DeleteChunksDialog(self.canvas)
        response = d.ShowModal()
        if response == wx.ID_YES:
            return True
        elif response == wx.ID_NO:
            return False
        return None

    def _create_chunks(self, evt):
        def create_chunks(
            world: BaseLevel,
            dimension: Dimension,
            selection: SelectionGroup,
        ):
            for cx, cz in selection.chunk_locations():
                if not world.has_chunk(cx, cz, dimension):
                    world.put_chunk(Chunk(cx, cz), dimension)

        self.canvas.run_operation(
            lambda: create_chunks(
                self.canvas.world,
                self.canvas.dimension,
                self.canvas.selection.selection_group,
            )
        )

    def _delete_chunks(self, evt):
        load_original = self._ask_delete_chunks()
        if load_original is not None:
            self.canvas.run_operation(
                lambda: delete_chunk(
                    self.canvas.world,
                    self.canvas.dimension,
                    self.canvas.selection.selection_group,
                    load_original,
                )
            )

    def _prune_chunks(self, evt):
        load_original = self._ask_delete_chunks()
        if load_original is not None:
            self.canvas.run_operation(
                lambda: prune_chunks(
                    self.canvas.world,
                    self.canvas.dimension,
                    self.canvas.selection.selection_group,
                    load_original,
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
            self.canvas.camera.orthographic_clipping = -(10**5), 10**5
            self._selection.draw()
            self.canvas.camera.orthographic_clipping = clip
            if depth_state:
                glEnable(GL_DEPTH_TEST)
        self.canvas.renderer.end_draw()
