from typing import Tuple
import wx

import weakref
import numpy
import math

from amulet_map_editor.api.opengl.camera import Camera
from amulet_map_editor.api.opengl.matrix import rotation_matrix_xy
from amulet_map_editor.programs.edit.api.key_config import (
    KeybindGroup,
    ACT_MOVE_UP,
    ACT_MOVE_DOWN,
    ACT_MOVE_FORWARDS,
    ACT_MOVE_BACKWARDS,
    ACT_MOVE_LEFT,
    ACT_MOVE_RIGHT,
    ACT_BOX_CLICK,
)
from amulet_map_editor.api.wx.util.button_input import (
    ButtonInput,
    InputPressEvent,
    EVT_INPUT_PRESS,
    InputReleaseEvent,
    EVT_INPUT_RELEASE,
    InputHeldEvent,
    EVT_INPUT_HELD,
)


_MoveActions = {
    ACT_MOVE_UP,
    ACT_MOVE_DOWN,
    ACT_MOVE_FORWARDS,
    ACT_MOVE_BACKWARDS,
    ACT_MOVE_LEFT,
    ACT_MOVE_RIGHT,
}


class NudgeButton(wx.Button):
    """A button that catches actions when pressed."""

    def __init__(
        self,
        parent: wx.Window,
        camera: Camera,
        keybinds: KeybindGroup,
        label: str,
        tooltip: str,
    ):
        super().__init__(parent, label=label, style=wx.WANTS_CHARS)
        self.SetToolTip(tooltip)
        self._camera = weakref.ref(camera)
        self._buttons = ButtonInput(self)
        self._buttons.register_actions(keybinds)
        self._buttons.bind_events()  # this is fine here because we are binding to a custom button not the canvas.
        self.Bind(EVT_INPUT_PRESS, self._on_down)
        self.Bind(EVT_INPUT_RELEASE, self._on_up)
        self.Bind(EVT_INPUT_HELD, self._on_held)
        self._listen = False
        self._timeout = 10

    @property
    def camera(self) -> Camera:
        return self._camera()

    def enable(self):
        self._buttons.enable()

    def disable(self):
        self._buttons.disable()

    def _on_down(self, evt: InputPressEvent):
        if evt.action_id == ACT_BOX_CLICK:
            self._listen = True
        elif evt.action_id in _MoveActions:
            self._timeout = 10

    def _on_up(self, evt: InputReleaseEvent):
        if evt.action_id == ACT_BOX_CLICK:
            self._listen = False

    def _on_held(self, evt: InputHeldEvent):
        if self._listen:
            if self._timeout == 0 or self._timeout == 10:
                x = y = z = 0
                if ACT_MOVE_LEFT in evt.action_ids:
                    x += 1
                if ACT_MOVE_RIGHT in evt.action_ids:
                    x -= 1
                if ACT_MOVE_UP in evt.action_ids:
                    y += 1
                if ACT_MOVE_DOWN in evt.action_ids:
                    y -= 1
                if ACT_MOVE_FORWARDS in evt.action_ids:
                    z += 1
                if ACT_MOVE_BACKWARDS in evt.action_ids:
                    z -= 1
                if any((x, y, z)):
                    self._move(self._rotate((x, y, z)))
            if self._timeout:
                self._timeout -= 1

    def _rotate(self, offset: Tuple[int, int, int]) -> Tuple[int, int, int]:
        x, y, z = offset
        ry = self.camera.rotation[0]
        x, y, z, _ = (
            numpy.round(
                numpy.matmul(
                    rotation_matrix_xy(0, -math.radians(round(ry / 90) * 90)),
                    (x, y, z, 0),
                )
            )
            .astype(int)
            .tolist()
        )
        return x, y, z

    def _move(self, offset: Tuple[int, int, int]):
        pass
