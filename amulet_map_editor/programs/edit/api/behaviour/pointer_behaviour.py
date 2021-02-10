from typing import TYPE_CHECKING
import wx

from amulet_map_editor.api.opengl.mesh.selection import RenderSelection
from amulet_map_editor.api.opengl.camera import Projection
from amulet.api.data_types import BlockCoordinatesNDArray

from .raycast_behaviour import RaycastBehaviour
from ..events import (
    EVT_PRE_DRAW,
    EVT_CAMERA_MOVED,
    InputPressEvent,
    EVT_INPUT_PRESS,
)
from ..key_config import (
    ACT_INCR_SELECT_DISTANCE,
    ACT_DECR_SELECT_DISTANCE,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class PointerBehaviour(RaycastBehaviour):
    """Adds the behaviour of the selection pointer."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)

        # has the pointer moved
        self._pointer_moved = True

        # the distance between the camera and the pointer
        self._pointer_distance = 10

        # the pointer
        self._pointer = RenderSelection(
            self.canvas.context_identifier,
            self.canvas.renderer.opengl_resource_pack,
        )

    @property
    def pointer_base(self) -> BlockCoordinatesNDArray:
        return self._pointer.point1

    def bind_events(self):
        super().bind_events()
        self.canvas.Bind(EVT_PRE_DRAW, self._pre_draw)
        self.canvas.Bind(EVT_CAMERA_MOVED, self._invalidate_pointer)
        self.canvas.Bind(wx.EVT_MOTION, self._invalidate_pointer)
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)

    def _on_input_press(self, evt: InputPressEvent):
        if evt.action_id == ACT_INCR_SELECT_DISTANCE:
            self._pointer_distance += 1
            self._pointer_moved = True
        elif evt.action_id == ACT_DECR_SELECT_DISTANCE:
            self._pointer_distance -= 1
            self._pointer_moved = True
        evt.Skip()

    def _invalidate_pointer(self, evt):
        self._pointer_moved = True
        evt.Skip()

    def _pre_draw(self, evt):
        if self._pointer_moved:
            self._update_pointer()
            self._pointer_moved = False
        evt.Skip()

    def _update_pointer(self):
        """Update the pointer location."""
        if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            location = self.closest_block_2d()[0]
        else:
            if self.canvas.camera.rotating:
                location = self.distance_block_3d(self._pointer_distance)
            else:
                location = self.closest_block_3d()[0]

        self._pointer.point1, self._pointer.point2 = location, location + 1

    def draw(self):
        self._pointer.draw(self.canvas.camera.transformation_matrix)
