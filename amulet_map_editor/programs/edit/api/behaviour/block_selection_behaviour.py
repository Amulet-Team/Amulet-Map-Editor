from typing import TYPE_CHECKING, Tuple
import wx
import time
import weakref

from amulet_map_editor.api.opengl.mesh.selection import RenderSelectionGroupEditable
from ..events import (
    BoxChangeEvent,
    BoxDisableInputsEvent,
    BoxEnableInputsEvent,
    BoxChangeConfirmEvent,
    InputPressEvent,
    EVT_INPUT_PRESS,
    InputReleaseEvent,
    EVT_INPUT_RELEASE,
    EVT_SELECTION_CHANGE,
    EVT_BOX_CHANGE_CONFIRM,
)
from amulet_map_editor.api.opengl.resource_pack import OpenGLResourcePack
from amulet.api.history import Changeable
from amulet.api.data_types import PointCoordinatesAny
from amulet_map_editor.api.opengl.camera import Projection

from .pointer_behaviour import PointerBehaviour


if TYPE_CHECKING:
    from ..canvas import EditCanvas


class EditProgramRenderSelectionGroup(RenderSelectionGroupEditable, Changeable):
    def __init__(
        self,
        canvas: "EditCanvas",
        context_identifier: str,
        resource_pack: OpenGLResourcePack,
    ):
        RenderSelectionGroupEditable.__init__(self, context_identifier, resource_pack)
        Changeable.__init__(self)
        self._canvas = weakref.ref(canvas)

    @property
    def canvas(self) -> "EditCanvas":
        return self._canvas()

    def _box_change_event(self):
        wx.PostEvent(self.canvas, BoxChangeEvent(corners=self.active_selection_corners))

    def _enable_inputs_event(self):
        super()._enable_inputs_event()
        wx.PostEvent(self.canvas, BoxEnableInputsEvent())

    def _disable_inputs_event(self):
        super()._disable_inputs_event()
        wx.PostEvent(self.canvas, BoxDisableInputsEvent())

    def _confirm_change_event(self):
        self.changed = True
        wx.PostEvent(self.canvas, BoxChangeConfirmEvent())


class BlockSelectionBehaviour(PointerBehaviour):
    """Adds the behaviour for a block based selection."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
        self._active_selection = None
        self._selection = EditProgramRenderSelectionGroup(
            self.canvas,
            self.canvas.context_identifier,
            self.canvas.renderer.opengl_resource_pack,
        )
        self._editing = False
        self._press_time = 0

    def bind_events(self):
        super().bind_events()
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)
        self.canvas.Bind(EVT_INPUT_RELEASE, self._on_input_release)
        self.canvas.Bind(EVT_SELECTION_CHANGE, self._on_selection_change)
        self.canvas.Bind(EVT_BOX_CHANGE_CONFIRM, self._push_selection)

    def enable(self):
        self._selection.all_selection_corners = self.canvas.selection.selection_corners

    def _on_selection_change(self, evt):
        self._selection.set_all_selection_corners(
            list(self.canvas.selection.selection_corners)
        )
        evt.Skip()

    def _push_selection(self, evt):
        self.canvas.selection.selection_corners = self._selection.all_selection_corners
        evt.Skip()

    def _on_input_press(self, evt: InputPressEvent):
        if evt.action_id == "box click":
            if not self._editing:
                self._press_time = time.time()
                self._editing = True
                self._selection.box_select_toggle(
                    "add box modifier" in self.canvas.buttons.pressed_actions
                )
        elif evt.action_id == "deselect boxes":
            self._selection.deselect_all()
        elif evt.action_id == "remove box":
            if "deselect boxes" not in self.canvas.buttons.pressed_actions:
                self._selection.deselect_active()
        evt.Skip()

    def _on_input_release(self, evt: InputReleaseEvent):
        if evt.action_id == "box click":
            if time.time() - self._press_time > 0.1:
                self._editing = False
                self._selection.box_select_toggle()
        evt.Skip()

    def _move_pointer(self, evt):
        super()._move_pointer(evt)
        self._selection.cursor_position = self._pointer.point1

    def _get_pointer_location(self) -> Tuple[PointCoordinatesAny, PointCoordinatesAny]:
        if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            location = self.closest_block_2d()[0]
        else:
            camera_location = self.canvas.camera.location
            look_vector = self.look_vector()
            (
                box,
                max_distance,
            ) = self._selection.selection_group.closest_vector_intersection(
                camera_location, look_vector
            )
            location, hit = self.closest_block_3d(min(max_distance, 100))
            if box is not None and not hit and max_distance < 100:
                for loc in self.collision_locations(
                    2, camera_location + look_vector * max_distance, look_vector
                ):
                    if self._selection[box].in_boundary(loc):
                        location = loc
                        self._selection.set_box_index(box)
                        break

        return location, location + 1

    def draw(self):
        if self.canvas.camera.projection_mode == Projection.TOP_DOWN:
            camera = None
        else:
            camera = self.canvas.camera.location
        self._selection.draw(self.canvas.camera.transformation_matrix, camera)
        super().draw()
