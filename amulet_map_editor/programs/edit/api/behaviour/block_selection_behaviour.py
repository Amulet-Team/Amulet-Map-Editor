from typing import TYPE_CHECKING, Tuple, Optional
import time
import numpy
import wx

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

NPArray2x3 = numpy.ndarray
NPVector3 = numpy.ndarray


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
        self._start_point_1: NPArray2x3 = numpy.zeros((2, 3))  # the state of the cursor when editing starts
        self._start_point_2: NPArray2x3 = numpy.zeros((2, 3))  # the state of the cursor when editing starts
        self._highlight = False  # is a box being highlighted
        self._initial_box: Optional[NPArray2x3] = None  # the state of the box when editing started
        self._pointer_mask: NPArray2x3 = numpy.zeros((2, 3), dtype=numpy.bool)

    def _load_active_selection(self):
        """Create the active selection if it does not exist."""
        if self._active_selection is None:
            self._active_selection = RenderSelectionEditable(
                self.canvas.context_identifier,
                self.canvas.renderer.opengl_resource_pack,
            )

    def _unload_active_selection(self):
        """Unload the active selection if it exists."""
        if self._active_selection is not None:
            self._active_selection.unload()
            self._active_selection = None

    def bind_events(self):
        super().bind_events()
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)
        self.canvas.Bind(EVT_INPUT_RELEASE, self._on_input_release)
        self.canvas.Bind(EVT_SELECTION_CHANGE, self._on_selection_change)
        self.canvas.Bind(wx.EVT_KEY_DOWN, self._on_key_press)

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
                default_create = True

                if "add box modifier" in self.canvas.buttons.pressed_actions:
                    # create a new box
                    if self._active_selection is not None:
                        # move the existing active to the inactive
                        self._selection.selection_group = self._selection.selection_group + self._active_selection.selection_group

                elif self._highlight:
                    # edit the highlighted box
                    box_index, faces = self._get_box_faces()
                    if box_index is None:
                        # this shouldn't happen but just to be safe.
                        self._selection.selection_group = SelectionGroup()
                    else:
                        if box_index == len(self._selection):
                            # the active selection is highlighted
                            self._press_time = time.time()
                            self._editing = True
                            self._start_point_1, self._start_point_2 = self._get_active_points()
                            self._active_selection.set_highlight_edges(faces)
                            self._pointer_mask = faces
                            self._active_selection.locked = False
                            self._initial_box = None
                        else:
                            # a static selection box is highlighted
                            selection_group = self.selection_group
                            self._selection.selection_group = selection_group[:box_index] + selection_group[box_index+1:]
                            self._active_selection.selection_box = selection_group[box_index]

                        default_create = False
                        self._initial_box = self._active_selection.points
                else:
                    # clear the selection
                    self._selection.selection_group = SelectionGroup()

                self._load_active_selection()
                if default_create:
                    self._press_time = time.time()
                    self._editing = True
                    self._start_point_1 = self._pointer.bounds
                    self._pointer_mask = numpy.array([[False]*3, [True]*3], dtype=numpy.bool)
                    self._active_selection.set_highlight_edges(self._pointer_mask)
                    self._active_selection.locked = False
                    self._initial_box = None

        elif evt.action_id == "deselect boxes":
            self.selection_group = SelectionGroup()
            self._push_selection()
        elif evt.action_id == "remove box":
            if "deselect boxes" not in self.canvas.buttons.pressed_actions:
                self.selection_group = self.selection_group[:-1]
                self._push_selection()
        evt.Skip()

    def _on_key_press(self, evt: wx.KeyEvent):
        key = evt.GetUnicodeKey() or evt.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            self._escape()
        evt.Skip()

    def _escape(self):
        """Reset the state to how it was before editing."""
        if self._editing:
            if self._initial_box is None:
                # there was no initial box
                if self._selection:
                    # static selection exists. Load the last into the active.
                    self._load_active_selection()
                    selection_group = self.selection_group
                    self._selection.selection_group = selection_group[:-1]
                    self._active_selection.selection_box = selection_group[-1]
                    self._active_selection.locked = True
                else:
                    self._unload_active_selection()
            else:
                # there was an initial box
                self._load_active_selection()
                self._active_selection.points = self._initial_box
                self._active_selection.locked = True
            self._editing = False

    def _get_active_points(self) -> Tuple[NPArray2x3, NPArray2x3]:
        """Get the 1x1x1 box coords for the active selection."""
        p1, p2 = numpy.zeros((2, 3)), numpy.zeros((2, 3))
        if self._active_selection is not None:
            p1[0], p2[0] = self._active_selection.points
            p1[1] = p1[0] + 1
            p2[1] = p2[0] + 1
            mult = p1[0] < p2[0]
            p1 -= 1 * numpy.logical_not(mult)
            p2 -= 1 * mult
        return p1, p2

    @property
    def active_block_positions(self) -> Tuple[Tuple[int, int, int], Tuple[int, int, int]]:
        """Get the active box positions.
        The coordinates for the maximum point of the box will be one less because this is the block position."""
        if self._active_selection is None:
            return (0, 0, 0), (0, 0, 0)
        else:
            p1, p2 = self._get_active_points()
            return tuple(p1.tolist()), tuple(p2.tolist())

    @active_block_positions.setter
    def active_block_positions(self, positions: Tuple[Tuple[int, int, int], Tuple[int, int, int]]):
        """Set the active box positions.
        This should only be used when not editing.
        The coordinates for the maximum point of the box will be one greater because this is the block position."""
        if self._active_selection is not None and not self._editing:
            self._pointer_mask[:] = False
            self._start_point_1[:] = positions[0]
            self._start_point_2[:] = positions[1]
            self._start_point_1[1] += 1
            self._start_point_2[1] += 1
            (
                self._active_selection.point1,
                self._active_selection.point2,
            ) = self._get_editing_selection()
            self._push_selection()

    def _get_editing_selection(self) -> Tuple[NPVector3, NPVector3]:
        """Get the minimum and maximum points of the editing selection.
        This is based on the stored starting pointer and the current pointer."""
        start_point_1 = self._start_point_1.copy()
        start_point_2 = self._start_point_2.copy()
        pointer = self._pointer.bounds.copy()
        start_point_1[:, self._pointer_mask[0]] = pointer[:, self._pointer_mask[0]]
        start_point_2[:, self._pointer_mask[1]] = pointer[:, self._pointer_mask[1]]
        start_1, start_2 = start_point_1
        point_1, point_2 = start_point_2
        start = start_1
        point = point_1
        mask = numpy.abs(start - point_1) < numpy.abs(start - point_2)
        point[mask] = point_2[mask]
        mask = numpy.abs(point - start_1) < numpy.abs(point - start_2)
        start[mask] = start_2[mask]
        return start, point

    def _on_input_release(self, evt: InputReleaseEvent):
        if evt.action_id == "box click":
            if self._editing and time.time() - self._press_time > 0.1:
                self._editing = False
                self._active_selection.locked = True
                self._push_selection()
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
                self._highlight = False
                if self._active_selection is not None:
                    self._active_selection.reset_highlight_edges()
            else:
                self._highlight = True
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
                self._unload_active_selection()

        if len(selection_group) <= 1:
            # unload the selection group
            self._selection.selection_group = SelectionGroup()

        if len(selection_group) >= 1:
            # load the active selection
            self._load_active_selection()
            self._active_selection.selection_box = selection_group[-1]

        if len(selection_group) >= 2:
            # load the selection group
            self._selection.selection_group = selection_group[:-1]

    def _get_box_faces(self) -> Tuple[Optional[int], NPArray2x3]:
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
        if not self._highlight and not self._editing:
            super().draw()
