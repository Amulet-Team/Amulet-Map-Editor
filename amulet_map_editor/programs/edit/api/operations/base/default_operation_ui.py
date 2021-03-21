from typing import TYPE_CHECKING
import wx
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)

from .operation_ui import OperationUI
from amulet_map_editor.programs.edit.api.behaviour import StaticSelectionBehaviour
from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.programs.edit.api.events import EVT_DRAW
from amulet_map_editor.programs.edit.api.behaviour import (
    CameraBehaviour,
    PointerBehaviour,
)
from amulet_map_editor.programs.edit.api.events import (
    InputPressEvent,
    EVT_INPUT_PRESS,
)
from amulet_map_editor.programs.edit.api.key_config import (
    ACT_BOX_CLICK,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas
    from amulet.api.level import BaseLevel


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
        self._pointer = PointerBehaviour(self.canvas)
        self._show_pointer = False

    def enable(self):
        self._selection.update_selection()
        self.canvas.camera.projection_mode = Projection.PERSPECTIVE

    def bind_events(self):
        self._selection.bind_events()
        self.canvas.Bind(EVT_DRAW, self._on_draw)
        self._camera_behaviour.bind_events()
        self._pointer.bind_events()
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)

    def _on_draw(self, evt):
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.canvas.renderer.draw_level()
        self._selection.draw()
        if self._show_pointer:
            self._pointer.draw()
        self.canvas.renderer.end_draw()

    def _on_input_press(self, evt: InputPressEvent):
        if evt.action_id == ACT_BOX_CLICK:
            self._on_box_click()
        evt.Skip()

    def _on_box_click(self):
        pass
