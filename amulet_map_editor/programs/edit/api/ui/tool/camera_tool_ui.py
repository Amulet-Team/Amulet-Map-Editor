import wx
from typing import Union, TYPE_CHECKING

from amulet_map_editor.programs.edit.api.events import EVT_DRAW
from .base_tool_ui import BaseToolUI
from amulet_map_editor.programs.edit.api.behaviour import CameraBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]


class CameraToolUI(BaseToolUI):
    def __init__(self, canvas: EditCanvas):
        super().__init__(canvas)
        self._camera_behaviour = CameraBehaviour(self.canvas)

    @property
    def name(self) -> str:
        raise NotImplementedError

    def bind_events(self):
        self.canvas.Bind(EVT_DRAW, self._on_draw)
        self._camera_behaviour.set_up_events()
