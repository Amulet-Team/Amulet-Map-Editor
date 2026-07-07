from typing import Optional, Tuple
import wx

import time
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

# Wall-clock timings for the nudge repeat. These are kept time-based (rather
# than counting input ticks) so the feel is independent of the shared input
# timer's tick rate. The first nudge fires immediately, then repeats pause for
# the initial delay before continuing at the steady interval.
_INITIAL_DELAY = 0.33  # seconds before the held nudge starts repeating
_REPEAT_INTERVAL = 1 / 30  # seconds between repeats (~30 nudges/sec)


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
        # Wall-clock time at which the next repeat nudge is allowed. ``None``
        # means a fresh press: the next held event nudges immediately.
        self._next_nudge_time: Optional[float] = None

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
            # Fresh press: the next held event should nudge immediately.
            self._next_nudge_time = None

    def _on_up(self, evt: InputReleaseEvent):
        if evt.action_id == ACT_BOX_CLICK:
            self._listen = False

    def _on_held(self, evt: InputHeldEvent):
        if not self._listen:
            return
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
        if not any((x, y, z)):
            return
        now = time.time()
        if self._next_nudge_time is None:
            # First held event after a press: nudge immediately, then wait out
            # the initial delay before repeating.
            self._move(self._rotate((x, y, z)))
            self._next_nudge_time = now + _INITIAL_DELAY
        elif now >= self._next_nudge_time:
            self._move(self._rotate((x, y, z)))
            self._next_nudge_time = now + _REPEAT_INTERVAL

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
