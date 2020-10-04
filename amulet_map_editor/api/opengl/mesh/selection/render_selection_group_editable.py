import numpy
from typing import Tuple, Optional, List

from amulet.api.data_types import (
    BlockCoordinatesAny,
    BlockCoordinatesNDArray,
    PointCoordinatesAny,
    BlockCoordinates,
)
from .render_selection_group import RenderSelectionGroup
from .render_selection import RenderSelection
from .render_selection_highlightable import RenderSelectionHighlightable
from .render_selection_editable import RenderSelectionEditable

from amulet_map_editor.api.opengl.resource_pack import OpenGLResourcePack


class RenderSelectionGroupEditable(RenderSelectionGroup):
    """A group of selection boxes to be drawn with an added editable box."""

    def __init__(
        self, context_identifier: str, resource_pack: OpenGLResourcePack,
    ):
        super().__init__(context_identifier, resource_pack)
        # the block coordinate of the mouse pointer. This needs updating via `update_cursor_position` when the mouse moves
        self._cursor_position = numpy.array([0, 0, 0], dtype=numpy.int)

        # the drawable box to display where the mouse is selecting. Is not always drawn
        self._cursor = RenderSelection(context_identifier, resource_pack)

        # the list of all boxes in the selection
        self._boxes: List[RenderSelectionHighlightable] = []

        # the indexes into self._boxes that are currently active and was last active.
        # These can be None only if self._boxes is empty and thus there are no boxes to be active.
        self._active_box_index: Optional[int] = None
        self._last_active_box_index: Optional[
            int
        ] = None  # the last active box for use when deselecting or escaping a non-committed box

        # The box that is active (renders differently to the ones in self._boxes) may be None if no box is active.
        self._active_box: Optional[RenderSelectionEditable] = None

        self._hover_box_index: Optional[
            int
        ] = None  # the index of the box being hovered over
        self._last_highlighted_box_index: Optional[
            int
        ] = None  # the index of the box previously hovered over. Used to remove the highlight effect.

        self._editable = True  # Should the selection accept user interaction.

    @property
    def active_selection_corners(self) -> Tuple[BlockCoordinates, BlockCoordinates]:
        """Get the bounds of the selection box that is currently active.
        Will be all 0 if no selection box exists.
        The second value will be one less than the actual top edge.
        This is the same as box selection in game works and solves some other issues."""
        if self._active_box is None:
            return (0, 0, 0), (0, 0, 0)
        else:
            return tuple(self._active_box.point1), tuple(self._active_box.point2)

    @active_selection_corners.setter
    def active_selection_corners(
        self, box_corners: Tuple[BlockCoordinates, BlockCoordinates]
    ):
        if self._active_box is not None:
            self._active_box.point1, self._active_box.point2 = box_corners
        if self._active_box_index is not None:
            box = self._boxes[self._active_box_index]
            box.point1, box.point2 = box_corners
        self._enable_inputs_event()
        self._confirm_change_event()

    @property
    def all_selection_corners(
        self,
    ) -> Tuple[Tuple[BlockCoordinates, BlockCoordinates], ...]:
        """The corners of each selection box."""
        return tuple((tuple(box.point1), tuple(box.point2)) for box in self._boxes)

    @all_selection_corners.setter
    def all_selection_corners(
        self, corners: Tuple[Tuple[BlockCoordinates, BlockCoordinates], ...]
    ):
        """Set the selection corners."""
        if self.set_all_selection_corners(corners):
            self._confirm_change_event()

    def set_all_selection_corners(
        self, corners: Tuple[Tuple[BlockCoordinates, BlockCoordinates], ...]
    ) -> bool:
        """
        Set the selection corners. Will not run _confirm_change_event. You may prefer the all_selection_corners setter.
        :param corners: The block coordinates of each corner.
        :return: Has the selection changed.
        """
        if corners != self.all_selection_corners:
            if corners:
                active = self._active_box_index
                self._deselect_all()
                for point1, point2 in corners:
                    box = self._new_render_selection()
                    box.point1 = point1
                    box.point2 = point2
                    self._boxes.append(box)
                if isinstance(active, int) and active < len(corners):
                    self._active_box_index = active
                else:
                    self._active_box_index = 0
                self._create_active_box_from_existing()
            else:
                self._deselect_all()
            return True
        return False

    @property
    def active_box_index(self) -> Optional[int]:
        """The index of the active selection box."""
        return self._active_box_index

    @active_box_index.setter
    def active_box_index(self, index: Optional[int]):
        """Set index of the active selection box."""
        if isinstance(index, int):
            index = min(index, len(self._boxes) - 1)
            self._active_box_index = index
            self._create_active_box_from_existing()
        elif index is None:
            self._unload_active_box()
        else:
            raise Exception("index format is incorrect")

    def _new_render_selection(self):
        return RenderSelectionHighlightable(
            self._context_identifier, self.resource_pack
        )

    def _new_editable_render_selection(self):
        return RenderSelectionEditable(self._context_identifier, self.resource_pack)

    def _unload_active_box(self):
        if self._active_box is not None:
            self._active_box.unload()
            self._active_box = None

    def _create_active_box_from_cursor(self):
        # create from the cursor position
        self._unload_active_box()
        self._active_box = (
            self._new_editable_render_selection()
        )  # create a new render selection
        self._last_active_box_index = self._active_box_index
        self._active_box.point1, self._active_box.point2 = (
            self._cursor_position,
            self._cursor_position,
        )
        self._active_box_index = None
        self._disable_inputs_event()

    def _create_active_box_from_existing(self):
        self._unload_active_box()
        self._active_box = (
            self._new_editable_render_selection()
        )  # create a new render selection
        self._last_active_box_index = None
        active_box = self._boxes[self._active_box_index]
        self._active_box.point1, self._active_box.point2 = (
            active_box.point1,
            active_box.point2,
        )
        self._active_box.lock()
        self._enable_inputs_event()

    @property
    def editable(self) -> bool:
        """Is the selection open for editing. Useful to stop the selection being edited.
        This is not for if the box is being modified."""
        return self._editable

    @editable.setter
    def editable(self, editable: bool):
        """
        Set if the selection is able to be edited.
        :param editable: True for the selection to be editable for the user. False to ignore user interaction.
        :return:
        """
        self._editable = bool(editable)
        if editable and self._active_box_index is not None:
            self._create_active_box_from_existing()
        else:
            self._unload_active_box()
            self._disable_inputs_event()

    @property
    def editing(self) -> bool:
        """Is the selection being modified."""
        return self._active_box is not None and self._active_box.is_dynamic

    @property
    def reediting(self) -> bool:
        """Is the selection being modified after having been confirmed at least once."""
        return self._active_box is not None and self._active_box.being_resized

    def escape_event(self, evt):
        self.escape()
        evt.Skip()

    def escape(self):
        """If the selection box is being modified revert it"""
        if self._active_box_index is not None:
            self._create_active_box_from_existing()
        elif self._last_active_box_index is not None:
            self._active_box_index = self._last_active_box_index
            self._last_active_box_index = None
            self._create_active_box_from_existing()
        else:
            # if the box hasn't been committed yet
            self._unload_active_box()
            self._active_box_index = self._last_active_box_index = None
            self._disable_inputs_event()

    def deselect_all(self):
        """Destroy all selection boxes."""
        changed = bool(self._boxes)
        self._deselect_all()
        if changed:
            self._confirm_change_event()

    def _deselect_all(self):
        """Destroy all selection boxes. No events fired."""
        while self._boxes:
            box = self._boxes.pop()
            box.unload()
        self._active_box: Optional[RenderSelectionEditable] = None
        self._active_box_index = (
            self._last_active_box_index
        ) = self._last_highlighted_box_index = None
        self._disable_inputs_event()

    def deselect_active(self):
        """Destroy the active selection box."""
        if self._active_box_index is not None:
            # If the box already exists in the list
            box = self._boxes.pop(self._active_box_index)
            box.unload()
            if self._boxes:
                if self._active_box_index >= 1:
                    self._active_box_index -= 1
                if (
                    self._last_highlighted_box_index is not None
                    and self._last_highlighted_box_index >= 1
                ):
                    self._last_highlighted_box_index -= 1
                self._create_active_box_from_existing()
            else:
                self._unload_active_box()
                self._active_box_index = self._last_active_box_index = None
                self._disable_inputs_event()
            self._confirm_change_event()
        elif self._last_active_box_index is not None:
            self._active_box_index = self._last_active_box_index
            self._last_active_box_index = None
            self._create_active_box_from_existing()
        else:
            # if the box hasn't been committed yet
            self._unload_active_box()
            self._active_box_index = self._last_active_box_index = None
            self._disable_inputs_event()

    @property
    def cursor_position(self) -> BlockCoordinates:
        """The block coordinate of the cursor."""
        return tuple(self._cursor_position)

    def update_cursor_position(
        self, position: BlockCoordinatesAny, box_index: Optional[int]
    ):
        self._cursor_position[:] = position
        self._hover_box_index = box_index
        self._cursor.point1 = self._cursor.point2 = position
        if (
            self._last_highlighted_box_index is not None
            and self._last_highlighted_box_index != box_index
        ):
            self._boxes[self._last_highlighted_box_index].set_highlight_edges(False)
            self._last_highlighted_box_index = None
        if box_index is not None and self._active_box_index != box_index:
            self._boxes[box_index].set_active_point(position)
            self._last_highlighted_box_index = box_index

        if self._active_box:
            self._active_box.set_active_point(position)
            self._box_change_event()

    def _box_change_event(self):
        """The coordinates of the box have changed."""
        pass

    def _disable_inputs_event(self):
        """Disable external inputs. Generally called when box editing has started."""
        self._box_change_event()

    def _enable_inputs_event(self):
        """Enable external inputs. Generally called when box editing has finished."""
        self._box_change_event()

    def _confirm_change_event(self):
        """The changed coordinates have been confirmed as final."""
        pass

    def box_select_disable(self):
        """Lock the currently selected box in its current state."""
        if self._active_box is not None and self._active_box.is_dynamic:
            self._box_select_disable()

    def _box_select_disable(self):
        self._active_box.lock()
        if self._active_box_index is None:
            box = self._new_render_selection()
            self._active_box_index = len(self._boxes)
            self._boxes.append(box)
        else:
            box = self._boxes[self._active_box_index]
        box.point1, box.point2 = self._active_box.point1, self._active_box.point2
        self._enable_inputs_event()
        self._confirm_change_event()

    def box_select_toggle(
        self, add_modifier: bool = False
    ) -> Optional[BlockCoordinatesNDArray]:
        """Method called to activate or deactivate the active selection"""
        if self._active_box is None:  # if there is no active selection
            self._create_active_box_from_cursor()
        elif (
            self._active_box.is_static
        ):  # if there is an active selection that is static
            if (
                self._hover_box_index is not None
                and self._hover_box_index != self._active_box_index
            ):  # if hovering over a different selected box
                self._active_box_index = (
                    self._hover_box_index
                )  # activate that selection box
                self._create_active_box_from_existing()
                self._confirm_change_event()
            if (
                self._hover_box_index == self._active_box_index
            ):  # if the cursor was hovering over the current selection
                self._active_box.unlock(self._cursor_position)  # unlock it
                self._last_active_box_index = self._active_box_index
                self._disable_inputs_event()
                return self._cursor_position
            else:  # if no hovered selection box
                if not add_modifier:
                    self._deselect_all()
                self._create_active_box_from_cursor()
        else:  # if there is an active selection that is being edited
            self._box_select_disable()

    def draw(
        self,
        camera_matrix: numpy.ndarray,
        camera_position: PointCoordinatesAny = None,
        draw_selection=True,
        draw_cursor=True,
    ):
        if draw_selection:
            for index, box in enumerate(self._boxes):
                if not self.editable or index != self._active_box_index:
                    box.draw(camera_matrix, camera_position)
            if self._active_box is not None:
                self._active_box.draw(camera_matrix, camera_position)
        if draw_cursor and not self.editing:
            self._cursor.draw(camera_matrix)

    def closest_intersection(
        self, origin: PointCoordinatesAny, vector: PointCoordinatesAny
    ) -> Tuple[Optional[int], Optional["RenderSelectionHighlightable"]]:
        """
        Returns the index for the closest box in the look vector
        :param origin:
        :param vector:
        :return: Index for the closest box. None if no intersection.
        """
        multiplier = 999999999
        index_return = None
        box_return = None
        for index, box in enumerate(self._boxes):
            if (
                not self.editable
                or self._active_box is None
                or self._active_box.is_static
                or index != self._active_box_index
            ):
                mult = box.intersects_vector(origin, vector)
                if mult is not None and mult < multiplier:
                    multiplier = mult
                    index_return = index
                    box_return = box
        return index_return, box_return
