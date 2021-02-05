from typing import TYPE_CHECKING, Tuple, Optional
import time
import numpy

from ..events import (
    InputPressEvent,
    EVT_INPUT_PRESS,
    InputReleaseEvent,
    EVT_INPUT_RELEASE,
    EVT_SELECTION_CHANGE,
)
from amulet.api.selection import SelectionGroup, SelectionBox
from amulet.api.data_types import PointCoordinatesAny
from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.api.opengl.mesh.selection import (
    RenderSelectionEditable,
    RenderSelectionGroupHighlightable,
)

from .pointer_behaviour import PointerBehaviour


if TYPE_CHECKING:
    from ..canvas import EditCanvas


class BlockSelectionBehaviour(PointerBehaviour):
    """Adds the behaviour for a block based selection."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
        self._selection: RenderSelectionGroupHighlightable = (
            RenderSelectionGroupHighlightable(
                self.canvas.context_identifier,
                self.canvas.renderer.opengl_resource_pack,
            )
        )

        self._active_selection: Optional[RenderSelectionEditable] = None
        self._editing = False  # is the active selection being created or resized
        self._press_time = 0  # the time when the last box edit started
        self._start_box = numpy.zeros((2, 3))
        self._highlight = False

    def bind_events(self):
        super().bind_events()
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)
        self.canvas.Bind(EVT_INPUT_RELEASE, self._on_input_release)
        self.canvas.Bind(EVT_SELECTION_CHANGE, self._on_selection_change)

    def enable(self):
        self._pull_selection()

    def _on_selection_change(self, evt):
        self._pull_selection()
        evt.Skip()

    def _push_selection(self):
        """Write the current state to the global selection triggering an undo point."""
        self.canvas.selection.selection_group = self.selection_group

    def _pull_selection(self):
        """Pull the selection from the canvas."""
        self.selection_group = self.canvas.selection.selection_group

    def _on_input_press(self, evt: InputPressEvent):
        if evt.action_id == "box click":
            if not self._editing:
                self._press_time = time.time()
                self._editing = True

                if self._active_selection is None:
                    self._active_selection = RenderSelectionEditable(
                        self.canvas.context_identifier,
                        self.canvas.renderer.opengl_resource_pack,
                    )
                self._start_box = self._pointer.bounds
                # self._selection.box_select_toggle(
                #     "add box modifier" in self.canvas.buttons.pressed_actions
                # )
        elif evt.action_id == "deselect boxes":
            self.selection_group = SelectionGroup()
            self._push_selection()
        elif evt.action_id == "remove box":
            if "deselect boxes" not in self.canvas.buttons.pressed_actions:
                self.selection_group = SelectionGroup()
                self._push_selection()
        evt.Skip()

    def _get_editing_selection(self) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Get the minimum and maximum points of the editing selection.
        This is based on the stored starting pointer and the current pointer."""
        points = numpy.concatenate([self._start_box, self._pointer.bounds], 0)
        return numpy.min(points, 0), numpy.max(points, 0)

    def _on_input_release(self, evt: InputReleaseEvent):
        if evt.action_id == "box click":
            if time.time() - self._press_time > 0.1:
                self._editing = False
                self._active_selection.locked = True
        evt.Skip()

    def _move_pointer(self, evt):
        super()._move_pointer(evt)
        if self._editing:
            (
                self._active_selection.point1,
                self._active_selection.point2,
            ) = self._get_editing_selection()
        else:
            box_index, faces = self._get_box_faces()
            self._selection.reset_highlight_edges()
            if box_index is None:
                if self._active_selection is not None:
                    self._active_selection.reset_highlight_edges()
            else:
                if box_index == len(self._selection):
                    self._active_selection.set_highlight_edges(faces)
                else:
                    self._selection.set_highlight_edges(box_index, faces)
                    self._active_selection.reset_highlight_edges()

    @property
    def selection_group(self) -> SelectionGroup:
        """The selection group of the static and active selection.
        If the active selection is being resized it will not be included in this."""
        selection_group = self._selection.selection_group
        if self._active_selection is not None and not self._editing:
            selection_group += self._active_selection.selection_group
        return selection_group

    @selection_group.setter
    def selection_group(self, selection_group: SelectionGroup):
        if len(selection_group) == 0:
            # unload the active selection
            if self._active_selection is not None:
                self._active_selection.unload()
                self._active_selection = None

        if len(selection_group) <= 1:
            # unload the selection group
            self._selection.selection_group = SelectionGroup()

        if len(selection_group) >= 1:
            # load the active selection
            if self._active_selection is None:
                self._active_selection = RenderSelectionEditable(
                    self.canvas.context_identifier,
                    self.canvas.renderer.opengl_resource_pack,
                )
            self._active_selection.selection_box = selection_group[-1]

        if len(selection_group) >= 2:
            # load the selection group
            self._selection.selection_group = SelectionGroup(selection_group[:-1])

    def _get_box_faces(self) -> Tuple[Optional[int], numpy.ndarray]:
        """Get a bool array of which faces the look vector hits.
        If the vector hits near an edge it will have two faces and three for a corner."""
        camera = self.canvas.camera.location
        look_vector = self.look_vector()
        selection_group = self.selection_group
        (box_index, max_distance) = selection_group.closest_vector_intersection(
            camera, look_vector
        )
        if box_index is None:
            # it doesn't hit any boxes
            return None, numpy.zeros((2, 3), dtype=numpy.bool)
        else:
            box: SelectionBox = selection_group[box_index]
            point = max_distance * look_vector + camera
            tol = numpy.min([numpy.array(box.shape) / 4, numpy.ones(3)], 0)
            return box_index, numpy.abs(box.points_array - point) < tol

    def _get_pointer_location(self) -> Tuple[PointCoordinatesAny, PointCoordinatesAny]:
        if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            location = self.closest_block_2d()[0]
        else:
            camera_location = self.canvas.camera.location
            look_vector = self.look_vector()
            selection_group = self.selection_group
            box_index, max_distance = selection_group.closest_vector_intersection(
                camera_location, look_vector
            )
            location, block_hit = self.closest_block_3d(min(max_distance, 100))
            # if box_index is not None and not block_hit and max_distance < 100:
            #     for loc in self.collision_locations(
            #         2, camera_location + look_vector * max_distance, look_vector
            #     ):
            #         if loc in selection_group[box_index]:
            #             location = loc
            #             self._selection.set_box_index(box_index)
            #             break

        return location, location + 1

    def draw(self):
        if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            camera = None
        else:
            camera = self.canvas.camera.location
        self._selection.draw(self.canvas.camera.transformation_matrix, camera)
        if self._active_selection is not None:
            self._active_selection.draw(
                self.canvas.camera.transformation_matrix, camera
            )
        super().draw()
