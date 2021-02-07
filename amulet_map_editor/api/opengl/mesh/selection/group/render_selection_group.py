import numpy
from typing import List

from amulet_map_editor.api.opengl import Drawable, ContextManager
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePack,
    OpenGLResourcePackManagerStatic,
)
from amulet.api.selection import SelectionGroup, SelectionBox
from amulet.api.data_types import PointCoordinatesAny
from amulet_map_editor.api.opengl.mesh.selection import RenderSelection


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
            self.selection_group = selection

    def __len__(self):
        return len(self._boxes)

    def __bool__(self):
        return bool(self._boxes)

    def _new_render_selection(self):
        return RenderSelection(self.context_identifier, self.resource_pack)

    @property
    def selection_group(self) -> SelectionGroup:
        return SelectionGroup(
            [SelectionBox(box.point1, box.point2) for box in self._boxes]
        )

    @selection_group.setter
    def selection_group(self, selection_group: SelectionGroup):
        if type(selection_group) is not SelectionGroup:
            raise TypeError("selection_group must be a SelectionGroup.")
        self.unload()
        for box in selection_group.selection_boxes:
            render_box = self._new_render_selection()
            render_box.point1 = numpy.array(box.point_1)
            render_box.point2 = numpy.array(box.point_2)
            self._boxes.append(render_box)

    def draw(
        self, camera_matrix: numpy.ndarray, camera_position: PointCoordinatesAny = None
    ):
        for box in self._boxes:
            box.draw(camera_matrix, camera_position)

    def unload(self):
        while self._boxes:
            box = self._boxes.pop()
            box.unload()
