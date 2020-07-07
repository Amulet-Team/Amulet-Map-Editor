import numpy
from typing import Tuple, Dict, Any, List, Union

from amulet_map_editor.opengl.mesh.base.tri_mesh import Drawable
from amulet.api.selection import SelectionGroup, SelectionBox
from amulet.api.data_types import BlockCoordinatesAny, PointCoordinatesAny
from .render_selection import RenderSelection


class RenderSelectionGroup(Drawable):
    """A group of selection boxes to be drawn"""

    def __init__(
        self,
        context_identifier: str,
        texture_bounds: Dict[Any, Tuple[float, float, float, float]],
        texture: int,
        selection: SelectionGroup = None,
    ):
        self._context_identifier = context_identifier
        self._texture_bounds = texture_bounds
        self._texture = texture

        self._boxes: List[RenderSelection] = []

        if selection:
            for box in selection.selection_boxes:
                render_box = self._new_render_selection()
                render_box.point1 = numpy.array(box.min) - selection.min
                render_box.point2 = numpy.array(box.max) - selection.min - 1
                self._boxes.append(render_box)

    def _new_render_selection(self):
        return RenderSelection(
            self._context_identifier, self._texture_bounds, self._texture
        )

    def __iter__(self):
        yield from self._boxes

    def __contains__(self, position: Union[BlockCoordinatesAny, PointCoordinatesAny]):
        return any(position in box for box in self._boxes)

    def __getitem__(self, index: int) -> "RenderSelection":
        return self._boxes[index]

    def create_selection_group(self) -> SelectionGroup:
        return SelectionGroup([SelectionBox(box.min, box.max) for box in self._boxes])

    def draw(
        self, camera_matrix: numpy.ndarray, camera_position: PointCoordinatesAny = None
    ):
        for box in self._boxes:
            box.draw(camera_matrix, camera_position)
