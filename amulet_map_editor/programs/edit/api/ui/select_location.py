import wx
from typing import Callable, Type, Any, TYPE_CHECKING
import math

from amulet.api.level import BaseLevel
from amulet.api.data_types import BlockCoordinates, Dimension
from amulet_map_editor.api.wx.ui.simple import SimplePanel
from amulet_map_editor.api.wx.util.validators import IntValidator
from amulet_map_editor.programs.edit.api.edit_canvas_container import (
    EditCanvasContainer,
)
from amulet_map_editor.programs.edit.api.events import (
    EVT_CURSOR_BOX_MOVE,
    EVT_BOX_CLICK,
)
from amulet_map_editor.api import config

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class SelectLocationUI(SimplePanel, EditCanvasContainer):
    """A UI element that can be dropped into the EditCanvas and let the user pick a location for a structure.
    This UI does not allow for rotation.
    Will send EVT_SELECT_CONFIRM when the user confirms the selection."""

    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        structure: BaseLevel,
        dimension: Dimension,
        confirm_callback: Callable[[], None],
    ):
        SimplePanel.__init__(self, parent)
        EditCanvasContainer.__init__(self, canvas)

        self._structure = structure
        self._dimension = dimension
        self.canvas.renderer.fake_levels.clear()
        self.canvas.renderer.fake_levels.append(
            structure, dimension, (0, 0, 0), (1, 1, 1), (0, 0, 0)
        )

        self._setup_ui()

        self._confirm = wx.Button(self, label="Confirm")
        self.sizer.Add(
            self._confirm, flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, border=5
        )

        self._confirm.Bind(wx.EVT_BUTTON, lambda evt: confirm_callback())
        self._clicked = False
        self.canvas.Bind(EVT_CURSOR_BOX_MOVE, self._cursor_move)
        self.canvas.Bind(EVT_BOX_CLICK, self._box_click)

    def _add_row(self, label: str, wx_object: Type[wx.Object], **kwargs) -> Any:
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.add_object(sizer, 0, wx.ALIGN_CENTER_HORIZONTAL)
        name_text = wx.StaticText(self, label=label)
        sizer.Add(name_text, flag=wx.CENTER | wx.ALL | wx.EXPAND, border=5)
        obj = wx_object(self, **kwargs)
        sizer.Add(obj, flag=wx.CENTER | wx.ALL, border=5)
        return obj

    def _setup_ui(self):
        self._x: wx.SpinCtrl = self._add_row(
            "x", wx.SpinCtrl, min=-30000000, max=30000000
        )
        self._y: wx.SpinCtrl = self._add_row(
            "y", wx.SpinCtrl, min=-30000000, max=30000000
        )
        self._z: wx.SpinCtrl = self._add_row(
            "z", wx.SpinCtrl, min=-30000000, max=30000000
        )
        for ui in (self._x, self._y, self._z):
            ui.SetValidator(IntValidator())

        self._copy_air: wx.CheckBox = self._add_row("Copy Air", wx.CheckBox)
        copy_air = config.get("edit_select_location", {}).get("copy_air", False)
        self._copy_air.SetValue(copy_air)
        self._copy_air.Bind(wx.EVT_CHECKBOX, self._save_config)

        self._copy_water: wx.CheckBox = self._add_row("Copy Water", wx.CheckBox)
        copy_water = config.get("edit_select_location", {}).get("copy_water", True)
        self._copy_water.SetValue(copy_water)
        self._copy_water.Bind(wx.EVT_CHECKBOX, self._save_config)

        self._copy_lava: wx.CheckBox = self._add_row("Copy Lava", wx.CheckBox)
        copy_lava = config.get("edit_select_location", {}).get("copy_lava", True)
        self._copy_lava.SetValue(copy_lava)
        self._copy_lava.Bind(wx.EVT_CHECKBOX, self._save_config)

        self._x.Bind(wx.EVT_SPINCTRL, self._on_transform_change)
        self._y.Bind(wx.EVT_SPINCTRL, self._on_transform_change)
        self._z.Bind(wx.EVT_SPINCTRL, self._on_transform_change)

    @property
    def location(self) -> BlockCoordinates:
        return self._x.GetValue(), self._y.GetValue(), self._z.GetValue()

    @property
    def copy_air(self) -> bool:
        return self._copy_air.GetValue()

    @property
    def copy_water(self) -> bool:
        return self._copy_water.GetValue()

    @property
    def copy_lava(self) -> bool:
        return self._copy_lava.GetValue()

    @property
    def structure(self) -> BaseLevel:
        return self._structure

    @property
    def dimension(self) -> Dimension:
        return self._dimension

    def _save_config(self, evt):
        select_config = config.get("edit_select_location", {})
        select_config["copy_air"] = self.copy_air
        select_config["copy_water"] = self.copy_water
        select_config["copy_lava"] = self.copy_lava
        config.put("edit_select_location", select_config)

    def _on_transform_change(self, evt):
        location, scale, rotation = self.canvas.renderer.fake_levels.active_transform
        self.canvas.renderer.fake_levels.active_transform = (
            self.location,
            scale,
            rotation,
        )

    def _cursor_move(self, evt):
        if not self._clicked:
            x, y, z = evt.location
            self._x.SetValue(x)
            self._y.SetValue(y)
            self._z.SetValue(z)
            self._on_transform_change(None)
        evt.Skip()

    def _box_click(self, evt):
        self._clicked = True
        evt.Skip()


class SelectTransformUI(SelectLocationUI):
    """A UI element that can be dropped into the EditCanvas and let the user pick the transform for a structure.
    Will send EVT_SELECT_CONFIRM when the user confirms the selection."""

    def _setup_ui(self):
        super()._setup_ui()
        # self._sx: wx.SpinCtrl = self._add_row('sx', wx.SpinCtrlDouble, min=-100, max=100, initial=1)
        # self._sy: wx.SpinCtrl = self._add_row('sy', wx.SpinCtrlDouble, min=-100, max=100, initial=1)
        # self._sz: wx.SpinCtrl = self._add_row('sz', wx.SpinCtrlDouble, min=-100, max=100, initial=1)
        # self._sx.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_transform_change)
        # self._sy.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_transform_change)
        # self._sz.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_transform_change)

        self._rx: wx.SpinCtrl = self._add_row(
            "rx",
            wx.SpinCtrlDouble,
            min=-30000000,
            max=30000000,
            inc=90,
            style=wx.SP_ARROW_KEYS | wx.SP_WRAP,
        )
        self._ry: wx.SpinCtrl = self._add_row(
            "ry",
            wx.SpinCtrlDouble,
            min=-30000000,
            max=30000000,
            inc=90,
            style=wx.SP_ARROW_KEYS | wx.SP_WRAP,
        )
        self._rz: wx.SpinCtrl = self._add_row(
            "rz",
            wx.SpinCtrlDouble,
            min=-30000000,
            max=30000000,
            inc=90,
            style=wx.SP_ARROW_KEYS | wx.SP_WRAP,
        )
        self._rx.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_transform_change)
        self._ry.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_transform_change)
        self._rz.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_transform_change)

    @property
    def scale(self) -> BlockCoordinates:
        return 1, 1, 1
        # return self._sx.GetValue(), self._sy.GetValue(), self._sz.GetValue()

    @property
    def rotation(self) -> BlockCoordinates:
        return self._rx.GetValue(), self._ry.GetValue(), self._rz.GetValue()

    def _on_transform_change(self, evt):
        for ctrl in (self._rx, self._ry, self._rz):
            ctrl.SetValue(
                round((ctrl.GetValue() % 360) / 90) * 90
            )  # TODO: change this if smaller increments are allowed
        self.canvas.renderer.fake_levels.active_transform = (
            self.location,
            self.scale,
            tuple(math.radians(r) for r in self.rotation),
        )
