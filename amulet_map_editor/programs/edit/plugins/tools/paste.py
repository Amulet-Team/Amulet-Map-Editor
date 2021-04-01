import wx
from typing import TYPE_CHECKING, Tuple, Union, Type
from OpenGL.GL import (
    glClear,
    GL_DEPTH_BUFFER_BIT,
)
import math

from amulet.operations.paste import paste_iter

from amulet_map_editor.api.opengl.camera import Projection
from amulet_map_editor.api.opengl.mesh.level import RenderLevel

from amulet_map_editor.programs.edit.api.ui.tool import DefaultBaseToolUI
from amulet_map_editor.programs.edit.api.events import EVT_PASTE
from amulet_map_editor.programs.edit.api.ui.select_location import (
    TransformChangeEvent,
)

from amulet_map_editor.programs.edit.api.behaviour import StaticSelectionBehaviour
from amulet_map_editor.programs.edit.api.behaviour.pointer_behaviour import (
    PointerBehaviour,
    EVT_POINT_CHANGE,
    PointChangeEvent,
)
from amulet_map_editor.programs.edit.api.events import (
    InputPressEvent,
    EVT_INPUT_PRESS,
)
from amulet_map_editor.programs.edit.api.key_config import ACT_BOX_CLICK

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class TupleInput(wx.FlexGridSizer):
    WindowCls: Union[Type[wx.SpinCtrl], Type[wx.SpinCtrlDouble]] = None

    def __init__(
        self,
        parent: wx.Window,
        x_str: str,
        y_str: str,
        z_str: str,
        min_value: int = -30_000_000,
        max_value: int = 30_000_000,
        start_value: int = 0,
        style=wx.SP_ARROW_KEYS,
    ):
        super().__init__(3, 2, 5, 5)

        x_label = wx.StaticText(parent, label=x_str)
        self.Add(x_label, 0, wx.ALIGN_CENTER, 5)
        self.x = self.WindowCls(
            parent, min=min_value, max=max_value, initial=start_value, style=style
        )
        self.Add(self.x, 0, wx.ALIGN_CENTER, 5)

        y_label = wx.StaticText(parent, label=y_str)
        self.Add(y_label, 0, wx.ALIGN_CENTER, 5)
        self.y = self.WindowCls(
            parent, min=min_value, max=max_value, initial=start_value, style=style
        )
        self.Add(self.y, 0, wx.ALIGN_CENTER, 0)

        z_label = wx.StaticText(parent, label=z_str)
        self.Add(z_label, 0, wx.ALIGN_CENTER, 5)
        self.z = self.WindowCls(
            parent, min=min_value, max=max_value, initial=start_value, style=style
        )
        self.Add(self.z, 0, wx.ALIGN_CENTER, 0)

    @property
    def value(self):
        return self.x.GetValue(), self.y.GetValue(), self.z.GetValue()

    @value.setter
    def value(self, value):
        self.x.SetValue(value[0])
        self.y.SetValue(value[1])
        self.z.SetValue(value[2])


class TupleIntInput(TupleInput):
    WindowCls = wx.SpinCtrl

    @property
    def value(self) -> Tuple[int, int, int]:
        return self.x.GetValue(), self.y.GetValue(), self.z.GetValue()

    @value.setter
    def value(self, value: Tuple[int, int, int]):
        self.x.SetValue(value[0])
        self.y.SetValue(value[1])
        self.z.SetValue(value[2])


class TupleFloatInput(TupleInput):
    WindowCls = wx.SpinCtrlDouble

    @property
    def value(self) -> Tuple[float, float, float]:
        return self.x.GetValue(), self.y.GetValue(), self.z.GetValue()

    @value.setter
    def value(self, value: Tuple[float, float, float]):
        self.x.SetValue(value[0])
        self.y.SetValue(value[1])
        self.z.SetValue(value[2])


class RotationTupleInput(TupleFloatInput):
    def __init__(
        self,
        parent: wx.Window,
        x_str: str,
        y_str: str,
        z_str: str,
        increment=90,
    ):
        super().__init__(
            parent, x_str, y_str, z_str, -180, 180, style=wx.SP_ARROW_KEYS | wx.SP_WRAP
        )
        self.increment = increment
        self.x.Bind(wx.EVT_MOUSEWHEEL, self._on_wheel)
        self.y.Bind(wx.EVT_MOUSEWHEEL, self._on_wheel)
        self.z.Bind(wx.EVT_MOUSEWHEEL, self._on_wheel)
        self.x.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_change)
        self.y.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_change)
        self.z.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_change)

    @property
    def rotation_radians(self) -> Tuple[float, float, float]:
        return (
            math.radians(self.x.GetValue()),
            math.radians(self.y.GetValue()),
            math.radians(self.z.GetValue()),
        )

    @property
    def increment(self) -> int:
        return self.x.GetIncrement()

    @increment.setter
    def increment(self, increment: int):
        assert isinstance(increment, int) and increment >= 1
        self.x.SetIncrement(increment)
        self.y.SetIncrement(increment)
        self.z.SetIncrement(increment)
        self._round_values()

    def _on_wheel(self, evt: wx.MouseEvent):
        rotation = evt.GetWheelRotation()
        ctrl = evt.GetEventObject()
        if rotation > 0:
            ctrl.SetValue(ctrl.GetValue() + ctrl.GetIncrement())
            self._changed(ctrl)
        elif rotation < 0:
            ctrl.SetValue(ctrl.GetValue() - ctrl.GetIncrement())
            self._changed(ctrl)

    def _on_change(self, evt: wx.SpinDoubleEvent):
        ctrl = evt.GetEventObject()
        ctrl.SetValue(
            int(round(ctrl.GetValue() / ctrl.GetIncrement())) * ctrl.GetIncrement()
        )
        evt.SetValue(ctrl.GetValue())
        evt.Skip()

    def _changed(self, ctrl: wx.SpinCtrlDouble):
        evt = wx.SpinDoubleEvent(wx.wxEVT_SPINCTRLDOUBLE, ctrl.GetId(), ctrl.GetValue())
        evt.SetEventObject(ctrl)
        wx.PostEvent(ctrl, evt)

    def _round_value(self, ctrl: wx.SpinCtrlDouble):
        ctrl.SetValue(
            int(round(ctrl.GetValue() / ctrl.GetIncrement())) * ctrl.GetIncrement()
        )
        self._changed(ctrl)

    def _round_values(self):
        self._round_value(self.x)
        self._round_value(self.y)
        self._round_value(self.z)


class PasteTool(wx.BoxSizer, DefaultBaseToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.HORIZONTAL)
        DefaultBaseToolUI.__init__(self, canvas)

        self._selection = StaticSelectionBehaviour(self.canvas)
        self._cursor = PointerBehaviour(self.canvas)
        self._moving = False

        self._paste_panel = wx.Panel(canvas)
        self._paste_sizer = wx.BoxSizer(wx.VERTICAL)
        self._paste_panel.SetSizer(self._paste_sizer)
        self.Add(self._paste_panel, 0, wx.ALIGN_CENTER_VERTICAL)

        self._copy_air = wx.CheckBox(
            self._paste_panel, label="Copy Air", style=wx.ALIGN_RIGHT
        )
        self._paste_sizer.Add(self._copy_air, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self._copy_water = wx.CheckBox(
            self._paste_panel, label="Copy Water", style=wx.ALIGN_RIGHT
        )
        self._paste_sizer.Add(
            self._copy_water,
            flag=wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT,
            border=5,
        )

        self._copy_lava = wx.CheckBox(
            self._paste_panel, label="Copy Lava", style=wx.ALIGN_RIGHT
        )
        self._paste_sizer.Add(
            self._copy_lava,
            flag=wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT,
            border=5,
        )

        self._location = TupleIntInput(self._paste_panel, "x", "y", "z")
        self._paste_sizer.Add(
            self._location,
            flag=wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT,
            border=5,
        )

        self._free_rotation = wx.CheckBox(
            self._paste_panel, label="Free Rotation", style=wx.ALIGN_RIGHT
        )
        self._paste_sizer.Add(
            self._free_rotation,
            flag=wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT,
            border=5,
        )

        self._rotation = RotationTupleInput(self._paste_panel, "rx", "ry", "rz")
        self._paste_sizer.Add(
            self._rotation,
            flag=wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT,
            border=5,
        )
        self._free_rotation.Bind(wx.EVT_CHECKBOX, self._on_free_rotation_change)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        self._paste_sizer.Add(
            sizer_6, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT, 5
        )

        self.button_3 = wx.Button(self._paste_panel, label="a")
        self.button_3.SetMinSize((30, 30))
        sizer_6.Add(self.button_3, 0, 0, 0)

        self.button_4 = wx.Button(self._paste_panel, label="a")
        self.button_4.SetMinSize((30, 30))
        sizer_6.Add(self.button_4, 0, 0, 0)

        self._scale = TupleFloatInput(
            self._paste_panel, "sx", "sy", "sz", start_value=1
        )
        self._paste_sizer.Add(
            self._scale,
            flag=wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT,
            border=5,
        )

        self._paste_panel.Bind(wx.EVT_SPINCTRL, self._on_transform_change)
        self._paste_panel.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_transform_change)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        self._paste_sizer.Add(
            sizer_5, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM | wx.LEFT | wx.RIGHT, 5
        )

        self.button_1 = wx.Button(self._paste_panel, label="a")
        self.button_1.SetMinSize((30, 30))
        sizer_5.Add(self.button_1, 0, 0, 0)

        self.button_2 = wx.Button(self._paste_panel, label="a")
        self.button_2.SetMinSize((30, 30))
        sizer_5.Add(self.button_2, 0, 0, 0)

        confirm_button = wx.Button(self._paste_panel, label="Confirm")
        self._paste_sizer.Add(
            confirm_button, 0, wx.BOTTOM | wx.LEFT | wx.RIGHT | wx.EXPAND, 5
        )
        confirm_button.Bind(wx.EVT_BUTTON, self._paste_confirm)

        self._paste_panel.Disable()
        self.Layout()

    @property
    def name(self) -> str:
        return "Paste"

    def bind_events(self):
        super().bind_events()
        self._selection.bind_events()
        self.canvas.Bind(EVT_PASTE, self._paste)
        self._cursor.bind_events()
        self.canvas.Bind(EVT_POINT_CHANGE, self._on_pointer_change)
        self.canvas.Bind(EVT_INPUT_PRESS, self._on_input_press)

    def enable(self):
        super().enable()
        self._selection.update_selection()
        self._moving = False

    def disable(self):
        super().disable()
        self._paste_panel.Disable()
        self.canvas.renderer.fake_levels.clear()

    def _on_free_rotation_change(self, evt):
        if self._free_rotation.GetValue():
            self._rotation.increment = 1
        else:
            self._rotation.increment = 90

    def _rotation_radians(self) -> Tuple[float, float, float]:
        return tuple(math.radians(v) for v in self._rotation.value)

    def _on_pointer_change(self, evt: PointChangeEvent):
        if self._moving:
            self.canvas.renderer.fake_levels.active_transform = (
                evt.point,
                self._scale.value,
                self._rotation_radians(),
            )
            self._location.value = evt.point
        evt.Skip()

    def _on_transform_change(self, evt: TransformChangeEvent):
        self.canvas.renderer.fake_levels.active_transform = (
            self._location.value,
            self._scale.value,
            self._rotation_radians(),
        )
        evt.Skip()

    def _on_input_press(self, evt: InputPressEvent):
        if evt.action_id == ACT_BOX_CLICK:
            self._moving = not self._moving
            if self._moving:
                self.canvas.renderer.fake_levels.active_transform = (
                    self._location.value,
                    self._scale.value,
                    self._rotation_radians(),
                )
        evt.Skip()

    def _paste(self, evt):
        self._paste_panel.Enable()
        structure = evt.structure
        dimension = evt.dimension
        self.canvas.renderer.fake_levels.clear()
        self.canvas.renderer.fake_levels.append(
            structure, dimension, (0, 0, 0), (1, 1, 1), (0, 0, 0)
        )
        self._moving = True

    def _paste_confirm(self, evt):
        fake_levels = self.canvas.renderer.fake_levels
        level_index: int = fake_levels.active_level_index
        if level_index is not None:
            render_level: RenderLevel = fake_levels.render_levels[level_index]
            self.canvas.run_operation(
                lambda: paste_iter(
                    self.canvas.world,
                    self.canvas.dimension,
                    render_level.level,
                    render_level.dimension,
                    self._location.value,
                    self._scale.value,
                    self._rotation.value,
                    self._copy_air.GetValue(),
                    self._copy_water.GetValue(),
                    self._copy_lava.GetValue(),
                )
            )

    def _on_draw(self, evt):
        self.canvas.renderer.start_draw()
        if self.canvas.camera.projection_mode == Projection.PERSPECTIVE:
            self.canvas.renderer.draw_sky_box()
            glClear(GL_DEPTH_BUFFER_BIT)
        self.canvas.renderer.draw_level()
        self.canvas.renderer.draw_fake_levels()
        self._selection.draw()
        self.canvas.renderer.end_draw()
