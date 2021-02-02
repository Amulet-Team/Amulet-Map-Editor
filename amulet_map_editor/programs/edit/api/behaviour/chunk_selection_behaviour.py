from typing import TYPE_CHECKING, Tuple
import numpy
import time

from amulet.api.data_types import PointCoordinatesAny
from amulet.api.selection import SelectionGroup, SelectionBox
from .pointer_behaviour import PointerBehaviour
from amulet_map_editor.api.opengl.mesh.selection import RenderSelectionGroup
from ..events import (
    InputPressEvent,
    EVT_INPUT_PRESS,
    InputReleaseEvent,
    EVT_INPUT_RELEASE,
    EVT_SELECTION_CHANGE,
)
from amulet_map_editor.api.opengl.camera import Projection

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class ChunkSelectionBehaviour(PointerBehaviour):
    """Adds the behaviour for a chunk based selection."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
        self._selection = RenderSelectionGroup(
            self.canvas.context_identifier,
            self.canvas.renderer.opengl_resource_pack,
        )
        self._editing = False
        self._press_time = 0
        self._start_box = None
        self._add_box = False

    def bind_events(self):
        super().bind_events()
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)
        self.canvas.Bind(EVT_INPUT_RELEASE, self._on_input_release)
        self.canvas.Bind(EVT_SELECTION_CHANGE, self._on_selection_change)

    def _create_undo(self):
        """Write the current state to the global selection triggering an undo point."""
        self.canvas.selection.selection_group = self._selection.selection_group

    def enable(self):
        self._selection.selection_group = self.canvas.selection.selection_group

    def _on_selection_change(self, evt):
        self._selection.selection_group = self.canvas.selection.selection_group
        evt.Skip()

    # def _push_selection(self, evt):
    #     self.canvas.selection.selection_corners = self._selection.all_selection_corners
    #     evt.Skip()

    def _on_input_press(self, evt: InputPressEvent):
        if evt.action_id == "box click":
            if not self._editing:
                self._press_time = time.time()
                self._editing = True
                self._add_box = (
                    "add box modifier" in self.canvas.buttons.pressed_actions
                )
                self._start_box = self._pointer.bounds
        elif evt.action_id == "deselect boxes":
            self._selection.selection_group = SelectionGroup()
            self._create_undo()
        elif evt.action_id == "remove box":
            if "deselect boxes" not in self.canvas.buttons.pressed_actions:
                self._selection.selection_group = SelectionGroup()
                self._create_undo()
        evt.Skip()

    def _on_input_release(self, evt: InputReleaseEvent):
        if evt.action_id == "box click":
            if self._editing and time.time() - self._press_time > 0.1:
                self._editing = False
                points = numpy.concatenate([self._start_box, self._pointer.bounds], 0)
                self._selection.selection_group = SelectionGroup(
                    self._selection.selection_group.selection_boxes
                    + [SelectionBox(numpy.min(points, 0), numpy.max(points, 0))]
                )
                self._create_undo()
        evt.Skip()

    def _get_pointer_location(self) -> Tuple[PointCoordinatesAny, PointCoordinatesAny]:
        if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            x, z = self.get_2d_mouse_location()
            location = numpy.array([x, 0, z])
        else:
            camera_location = self.canvas.camera.location
            look_vector = self.look_vector()
            (
                box,
                max_distance,
            ) = self._selection.selection_group.closest_vector_intersection(
                camera_location, look_vector
            )
            location, hit = self.box_location_closest(min(max_distance, 100))

        chunk_size = self.canvas.world.sub_chunk_size
        location_min: numpy.ndarray = (location // chunk_size) * chunk_size
        location_max = location_min + chunk_size
        location_min[1] = self.canvas.world.selection_bounds.min[1]
        location_max[1] = self.canvas.world.selection_bounds.max[1]
        return location_min, location_max

    def draw(self):
        self._selection.draw(
            self.canvas.camera.transformation_matrix, self.canvas.camera.location
        )
        super().draw()
