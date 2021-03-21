from typing import TYPE_CHECKING, Union
import wx
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)

from .operation_ui import OperationUI
from amulet_map_editor.programs.edit.api.behaviour import StaticSelectionBehaviour
from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.programs.edit.api.events import EVT_DRAW
from amulet_map_editor.programs.edit.api.behaviour import CameraBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas
    from amulet.api.level import BaseLevel

OperationUIType = Union[wx.Window, wx.Sizer, "OperationUI"]


class DefaultOperationUI(OperationUI):
    """An extension of the base OperationUI that adds camera, static selection and some other controls."""

    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        super().__init__(parent, canvas, world, options_path)
        self._selection = StaticSelectionBehaviour(self.canvas)
        self._camera_behaviour = CameraBehaviour(self.canvas)

    def enable(self):
        self._selection.update_selection()
        self.canvas.camera.projection_mode = Projection.PERSPECTIVE

    def bind_events(self):
        self._selection.bind_events()
        self.canvas.Bind(EVT_DRAW, self._on_draw)
        self._camera_behaviour.bind_events()

    def _on_draw(self, evt):
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.canvas.renderer.draw_level()
        self._selection.draw()
        self.canvas.renderer.end_draw()
