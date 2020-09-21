import numpy
from typing import List, Union

from amulet_map_editor.api.opengl.mesh.base.tri_mesh import Drawable, ContextManager
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePack,
    OpenGLResourcePackManagerStatic,
)
from amulet.api.selection import SelectionGroup, SelectionBox
from amulet.api.data_types import BlockCoordinatesAny, PointCoordinatesAny
from .render_selection import RenderSelection


class RenderSelectionGroup(Drawable, ContextManager, OpenGLResourcePackManagerStatic):
    """A group of selection boxes to be drawn"""

    def __init__(
        self,
        context_identifier: str,
        resource_pack: OpenGLResourcePack,
        selection: SelectionGroup = None,
    ):
        ContextManager.__init__(self, context_identifier)
        OpenGLResourcePackManagerStatic.__init__(self, resource_pack)

        self._boxes: List[RenderSelection] = []

        if selection:
            for box in selection.selection_boxes:
                render_box = self._new_render_selection()
                render_box.point1 = numpy.array(box.min) - selection.min
                render_box.point2 = numpy.array(box.max) - selection.min - 1
                self._boxes.append(render_box)

    def _new_render_selection(self):
        return RenderSelection(self.context_identifier, self.resource_pack)

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
