import wx
import math

from amulet.api.data_types import FloatTriplet
from .select_location import SelectLocationUI
from .events import RotationChangeEvent, ScaleChangeEvent, TransformChangeEvent


class SelectTransformUI(SelectLocationUI):
    """A UI element that can be dropped into the EditCanvas and let the user pick the transform for a structure."""

    def _setup_ui(self):
        super()._setup_ui()
        # self._sx: wx.SpinCtrl = self._add_row('sx', wx.SpinCtrlDouble, min=-100, max=100, initial=1)
        # self._sy: wx.SpinCtrl = self._add_row('sy', wx.SpinCtrlDouble, min=-100, max=100, initial=1)
        # self._sz: wx.SpinCtrl = self._add_row('sz', wx.SpinCtrlDouble, min=-100, max=100, initial=1)
        # self._sx.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_scale_change)
        # self._sy.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_scale_change)
        # self._sz.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_scale_change)

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
        self._rx.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_rotation_change)
        self._ry.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_rotation_change)
        self._rz.Bind(wx.EVT_SPINCTRLDOUBLE, self._on_rotation_change)

    @property
    def scale(self) -> FloatTriplet:
        return 1, 1, 1
        # return self._sx.GetValue(), self._sy.GetValue(), self._sz.GetValue()

    @property
    def rotation(self) -> FloatTriplet:
        return self._rx.GetValue(), self._ry.GetValue(), self._rz.GetValue()

    @property
    def rotation_radians(self) -> FloatTriplet:
        """The rotation of the object. (x, y, z)."""
        return tuple(math.radians(r) for r in self.rotation)

    def _on_rotation_change(self, evt):
        wx.PostEvent(self, RotationChangeEvent(self.rotation))
        self._on_transform_change()

    def _on_scale_change(self, evt):
        for ctrl in (self._rx, self._ry, self._rz):
            ctrl.SetValue(
                round((ctrl.GetValue() % 360) / 90) * 90
            )  # TODO: change this if smaller increments are allowed
        wx.PostEvent(self, ScaleChangeEvent(self.scale))
        self._on_transform_change()

    def _on_transform_change(self):
        wx.PostEvent(
            self, TransformChangeEvent(self.location, self.rotation, self.scale)
        )
