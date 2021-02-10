from typing import TYPE_CHECKING, Tuple, Optional
import time
import numpy
import wx
from wx.lib import newevent

from ..events import (
    InputPressEvent,
    InputReleaseEvent,
    EVT_INPUT_RELEASE,
    EVT_SELECTION_CHANGE,
)
from amulet.api.selection import SelectionGroup, SelectionBox
from amulet.api.data_types import (
    PointCoordinates,
    BlockCoordinates,
)
from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.api.opengl.mesh.selection import (
    RenderSelectionEditable,
    RenderSelectionGroupHighlightable,
)

from .pointer_behaviour import PointerBehaviour
from ..key_config import (
    ACT_BOX_CLICK,
    ACT_BOX_CLICK_ADD,
    ACT_INCR_SELECT_DISTANCE,
    ACT_DECR_SELECT_DISTANCE,
    ACT_DESELECT_ALL_BOXES,
    ACT_DELESECT_BOX,
)

if TYPE_CHECKING:
    from ..canvas import EditCanvas

# the active selection was changed from local code. Not fired by active_block_positions.setter
_RenderBoxChangeEvent = wx.NewEventType()
EVT_RENDER_BOX_CHANGE = wx.PyEventBinder(_RenderBoxChangeEvent)


class RenderBoxChangeEvent(wx.PyEvent):
    """Run when the selection is changed by third party code."""

    def __init__(self, point1: BlockCoordinates, point2: BlockCoordinates):
        wx.PyEvent.__init__(self, eventType=_RenderBoxChangeEvent)
        self._point1 = point1
        self._point2 = point2

    @property
    def point1(self) -> BlockCoordinates:
        return self._point1

    @property
    def point2(self) -> BlockCoordinates:
        return self._point2

    @property
    def points(self) -> Tuple[BlockCoordinates, BlockCoordinates]:
        return self._point1, self._point2


# run when self._editing is set to True or the active selection is removed. Locks external editing
RenderBoxDisableInputsEvent, EVT_RENDER_BOX_DISABLE_INPUTS = newevent.NewEvent()

# run when self._editing is set to False and there is an active selection. Allows external editing
RenderBoxEnableInputsEvent, EVT_RENDER_BOX_ENABLE_INPUTS = newevent.NewEvent()

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
        self._start_point_1: NPArray2x3 = numpy.zeros(
            (2, 3)
        )  # the state of the cursor when editing starts
        self._start_point_2: NPArray2x3 = numpy.zeros(
            (2, 3)
        )  # the state of the cursor when editing starts
        self._highlight = False  # is a box being highlighted
        self._initial_box: Optional[
            NPArray2x3
        ] = None  # the state of the box when editing started
        self._pointer_mask: NPArray2x3 = numpy.zeros((2, 3), dtype=numpy.bool)
        self._resizing = False  # is a box being resized
        self._pointer_distance2 = 0  # the pointer distance used when resizing

    def _create_active_selection(self):
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
        self.canvas.Bind(EVT_INPUT_RELEASE, self._on_input_release)
        self.canvas.Bind(EVT_SELECTION_CHANGE, self._on_selection_change)
        self.canvas.Bind(wx.EVT_KEY_DOWN, self._on_key_press)

    def enable(self):
        self.pull_selection()

    def _on_selection_change(self, evt):
        self.pull_selection()
        evt.Skip()

    def push_selection(self):
        """Write the current state to the global selection triggering an undo point."""
        self.canvas.selection.selection_group = self.selection_group

    def pull_selection(self):
        """Pull the selection from the canvas."""
        selection = self.canvas.selection.selection_group
        self.selection_group = selection
        if selection:
            self._enable_inputs()
        else:
            self._disable_inputs()

    def _post_change_event(self):
        wx.PostEvent(self.canvas, RenderBoxChangeEvent(*self.active_block_positions))

    def _disable_inputs(self):
        wx.PostEvent(self.canvas, RenderBoxDisableInputsEvent())

    def _enable_inputs(self):
        wx.PostEvent(self.canvas, RenderBoxEnableInputsEvent())

    def _on_input_press(self, evt: InputPressEvent):
        if evt.action_id == ACT_INCR_SELECT_DISTANCE:
            if self._resizing:
                self._pointer_distance2 += 1
            else:
                self._pointer_distance += 1
            self._pointer_moved = True
        elif evt.action_id == ACT_DECR_SELECT_DISTANCE:
            if self._resizing:
                self._pointer_distance2 -= 1
            else:
                self._pointer_distance -= 1
            self._pointer_moved = True
        elif evt.action_id == ACT_BOX_CLICK:
            if not self._editing:
                default_create = True
                self._press_time = time.time()
                self._disable_inputs()

                if ACT_BOX_CLICK_ADD in self.canvas.buttons.pressed_actions:
                    # create a new box
                    if self._active_selection is not None:
                        # move the existing active to the inactive
                        self._selection.selection_group = (
                            self._selection.selection_group
                            + self._active_selection.selection_group
                        )

                elif self._highlight:
                    # edit the highlighted box
                    box_index, distance, faces = self._get_box_faces()
                    if box_index is None:
                        # this shouldn't happen but just to be safe.
                        self._selection.selection_group = SelectionGroup()
                    else:
                        if box_index < len(self._selection):
                            # a static selection box is highlighted
                            selection_group = self.selection_group
                            self._selection.selection_group = (
                                selection_group[:box_index]
                                + selection_group[box_index + 1 :]
                            )
                            self._active_selection.selection_box = selection_group[
                                box_index
                            ]
                            self._post_change_event()

                        (
                            self._start_point_1,
                            self._start_point_2,
                        ) = self._get_active_points()
                        self._pointer_distance2 = distance
                        self._pointer_mask = faces
                        self._active_selection.set_highlight_edges(faces)
                        self._initial_box = self._active_selection.points
                        self._resizing = True
                        default_create = False
                        self._pointer_moved = True
                else:
                    # clear the selection
                    self._selection.selection_group = SelectionGroup()

                self._create_active_selection()
                self._active_selection.locked = False
                self._editing = True
                if default_create:
                    self._start_point_1 = self._pointer.bounds
                    self._pointer_mask = numpy.array(
                        [[False] * 3, [True] * 3], dtype=numpy.bool
                    )
                    self._active_selection.set_highlight_edges(self._pointer_mask)
                    self._initial_box = None
                    self._resizing = False

        elif evt.action_id == ACT_DESELECT_ALL_BOXES:
            if self.selection_group:
                self.selection_group = SelectionGroup()
                self.push_selection()
                self._disable_inputs()
                self._post_change_event()
            else:
                self._escape()
        elif evt.action_id == ACT_DELESECT_BOX:
            if ACT_DESELECT_ALL_BOXES not in self.canvas.buttons.pressed_actions:
                selection_group = self.selection_group
                if selection_group:
                    self.selection_group = selection_group[:-1]
                    self.push_selection()
                    if self._active_selection is None:
                        self._disable_inputs()
                        self._post_change_event()
                else:
                    self._escape()
        evt.Skip()

    def _on_key_press(self, evt: wx.KeyEvent):
        key = evt.GetUnicodeKey() or evt.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            self._escape()
        evt.Skip()

    def _on_input_release(self, evt: InputReleaseEvent):
        if evt.action_id == ACT_BOX_CLICK:
            if self._editing and time.time() - self._press_time > 0.1:
                self._editing = self._resizing = False
                self._enable_inputs()
                self._active_selection.locked = True
                self.push_selection()
        evt.Skip()

    def _escape(self):
        """Reset the state to how it was before editing."""
        if self._editing:
            if self._initial_box is None:
                # there was no initial box
                if self._selection:
                    # static selection exists. Load the last into the active.
                    self._create_active_selection()
                    selection_group = self.selection_group
                    self._selection.selection_group = selection_group[:-1]
                    self._active_selection.selection_box = selection_group[-1]
                    self._active_selection.locked = True
                    self._enable_inputs()
                else:
                    self._unload_active_selection()
            else:
                # there was an initial box
                self._create_active_selection()
                self._active_selection.points = self._initial_box
                self._active_selection.locked = True
                self._enable_inputs()
            self._editing = self._resizing = False
            self._highlight = False
            self._post_change_event()

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
    def active_block_positions(
        self,
    ) -> Tuple[Tuple[int, int, int], Tuple[int, int, int]]:
        """Get the active box positions.
        The coordinates for the maximum point of the box will be one less because this is the block position."""
        if self._active_selection is None:
            return (0, 0, 0), (0, 0, 0)
        else:
            p1, p2 = self._get_active_points()
            return tuple(p1[0].tolist()), tuple(p2[0].tolist())

    @active_block_positions.setter
    def active_block_positions(
        self, positions: Tuple[Tuple[int, int, int], Tuple[int, int, int]]
    ):
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
            self.push_selection()
        else:
            self._disable_inputs()

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
        """Set the selection group of the static and active selection.
        This will only trigger a grapical change and will not update the global selection.
        A call to push_selection is required to push the updated selection to the global selection."""
        self._escape()
        if len(selection_group) == 0:
            # unload the active selection
            if self._active_selection is not None:
                self._unload_active_selection()

        if len(selection_group) <= 1:
            # unload the selection group
            self._selection.selection_group = SelectionGroup()

        if len(selection_group) >= 1:
            # load the active selection
            self._create_active_selection()
            self._active_selection.selection_box = selection_group[-1]

        if len(selection_group) >= 2:
            # load the selection group
            self._selection.selection_group = selection_group[:-1]

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

    def _update_pointer(self):
        # find the closest box position
        # check if there are any blocks up to that position

        # find the closest box position
        # find the closest box or block position
        if self._pointer_moved:
            if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
                camera = self.canvas.camera.location
                camera = (camera[0], 10 ** 9, camera[2])
                look_vector = self.look_vector()
                selection_group, box_index, max_distance = self._get_box_hit_data(
                    camera, look_vector
                )
                location, hit_block = self.closest_block_2d(
                    int(10 ** 9 - min(max_distance, 10 ** 9)) + 1
                )
            else:
                (
                    camera,
                    look_vector,
                    selection_group,
                    box_index,
                    max_distance,
                ) = self._get_default_box_hit_data()
                if self.canvas.camera.rotating:
                    if self._resizing:
                        location = self.distance_block_3d(self._pointer_distance2)
                    else:
                        location = self.distance_block_3d(self._pointer_distance)
                    hit_block = True
                else:
                    if self._resizing:
                        location = self.distance_block_3d(self._pointer_distance2)
                        hit_block = True
                    else:
                        location, hit_block = self.closest_block_3d(
                            min(max_distance, 100) - 0.3
                        )

            self._pointer.point1, self._pointer.point2 = location, location + 1
            self._pointer_moved = False
            if self._editing:
                (
                    self._active_selection.point1,
                    self._active_selection.point2,
                ) = self._get_editing_selection()
                self._post_change_event()
            else:
                self._selection.reset_highlight_edges()
                if box_index is None or hit_block:
                    # if no box was hit or a block was hit
                    self._highlight = False
                    if self._active_selection is not None:
                        self._active_selection.reset_highlight_edges()
                else:
                    self._highlight = True
                    faces_hit = self._get_box_faces_manual(
                        camera, look_vector, selection_group, box_index, max_distance
                    )
                    if box_index == len(self._selection):
                        self._active_selection.set_highlight_edges(faces_hit)
                    else:
                        self._selection.set_highlight_edges(box_index, faces_hit)
                        self._active_selection.reset_highlight_edges()

    def _get_default_box_hit_data(
        self,
    ) -> Tuple[PointCoordinates, NPVector3, SelectionGroup, Optional[int], float]:
        camera = self.canvas.camera.location
        look_vector = self.look_vector()
        return (camera, look_vector) + self._get_box_hit_data(camera, look_vector)

    def _get_box_hit_data(
        self, camera: PointCoordinates, look_vector: NPVector3
    ) -> Tuple[SelectionGroup, Optional[int], float]:
        selection_group = self.selection_group
        box_index, max_distance = selection_group.closest_vector_intersection(
            camera, look_vector
        )
        return selection_group, box_index, max_distance

    def _get_box_faces(self) -> Tuple[Optional[int], float, NPArray2x3]:
        """Get collision information between a vector and a selection group.
        If the vector intersects a box in the selection group it will return
            The index of the selection box in the selection group.
            A 2x3 bool array of the faces that were hit as corresponding to point1 and point2 x,y,z
        If the vector does not hit the selection the same structure applies but will look like this
            None
            2x3 False array"""
        (
            camera,
            look_vector,
            selection_group,
            box_index,
            max_distance,
        ) = self._get_default_box_hit_data()
        return (
            box_index,
            max_distance,
            self._get_box_faces_manual(
                camera, look_vector, selection_group, box_index, max_distance
            ),
        )

    @staticmethod
    def _get_box_faces_manual(
        camera: PointCoordinates,
        look_vector: NPVector3,
        selection_group: SelectionGroup,
        box_index: Optional[int],
        max_distance: float,
    ) -> NPArray2x3:
        """Get a 2x3 bool array of the faces the look vector first contacts.
        point1 (x y z), point2 (x y z)"""
        if box_index is None:
            # it doesn't hit any boxes
            return numpy.zeros((2, 3), dtype=numpy.bool)
        else:
            box: SelectionBox = selection_group[box_index]
            point = max_distance * look_vector + camera
            tol = numpy.min([numpy.array(box.shape) / 4, numpy.ones(3)], 0)
            return numpy.abs(box.points_array - point) < tol

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
