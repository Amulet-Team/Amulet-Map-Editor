from typing import TYPE_CHECKING, Optional
import wx
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.programs.edit.api.behaviour.block_selection_behaviour import (
    BlockSelectionBehaviour,
)
from amulet_map_editor.programs.edit.api.ui.tool import DefaultBaseToolUI
from .fill_replace_widget import FillReplaceWidget
from .block_container.block_entry.custom_fill_button import SrcBlockState

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

"""
FillReplaceTool(wx.BoxSizer)        A sizer containing the FillReplaceWidget.
    FillReplaceWidget(wx.Panel)     A panel containing mode buttons and one or more fill/replace operations
        OperationContainer(wx.lib.scrolledpanel.ScrolledPanel)  A ScrolledPanel containing one or more fill/replace operations.
            ReplaceOperationWidget
                FindBlockContainer
                    FindBlockEntry
                    ...
                FillBlockContainer
                    FillBlockEntry
                    ...
            ...
"""


class FillReplaceTool(wx.BoxSizer, DefaultBaseToolUI):
    """A sizer containing the FillReplaceWidget."""

    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        DefaultBaseToolUI.__init__(self, canvas)
        self._panel: Optional[wx.Panel] = None
        self._operations: Optional[FillReplaceWidget] = None
        self._button: Optional[wx.Button] = None
        self._selection: Optional[BlockSelectionBehaviour] = None

    def setup(self):
        super().setup()
        self._panel = wx.Panel(self.canvas)
        self.Add(self._panel)
        panel_sizer = wx.BoxSizer(wx.VERTICAL)
        self._panel.SetSizer(panel_sizer)

        find_state = SrcBlockState(
            self.canvas.world.translation_manager,
            platform="java",
            version_number=(1, 16, 0),
            namespace="minecraft",
            base_name="air",
        )
        fill_state = SrcBlockState(
            self.canvas.world.translation_manager,
            platform="java",
            version_number=(1, 16, 0),
            namespace="minecraft",
            base_name="stone",
        )
        for state_ in (find_state, fill_state):
            with state_ as state:
                state.platform = self.canvas.world.level_wrapper.platform
                state.version_number = self.canvas.world.level_wrapper.version

        self._operations = FillReplaceWidget(self._panel, find_state, fill_state)
        panel_sizer.Add(self._operations, 1, wx.LEFT | wx.TOP, 5)

        self._button = wx.Button(self._panel, label="Run Operation")
        panel_sizer.Add(
            self._button, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.TOP, 5
        )
        self._button.Bind(wx.EVT_BUTTON, self._operation)

        self._selection = BlockSelectionBehaviour(self.canvas)

    @property
    def name(self) -> str:
        return "Fill/Replace"

    def bind_events(self):
        super().bind_events()
        self._selection.bind_events()

    def enable(self):
        super().enable()
        self._selection.enable()

    def _on_draw(self, evt):
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.canvas.renderer.draw_level()
        self._selection.draw()
        self.canvas.renderer.end_draw()

    def _operation(self, evt):
        pass
