import wx
from typing import Union, TYPE_CHECKING

from .base_tool_ui import BaseToolUI
from amulet_map_editor.programs.edit.api.behaviour import CameraBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]


class CameraToolUI(BaseToolUI):
    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
        self._camera_behaviour = CameraBehaviour(self.canvas)

    @property
    def name(self) -> str:
        raise NotImplementedError

    def bind_events(self):
        super().bind_events()
        self._camera_behaviour.bind_events()
