import wx
import math

from amulet.api.data_types import BlockCoordinates, FloatTriplet

# The location changed
_ObjectLocationChangeEventType = wx.NewEventType()
EVT_LOCATION_CHANGE = wx.PyEventBinder(_ObjectLocationChangeEventType)


class LocationChangeEvent(wx.PyEvent):
    """Run when the camera has moved or rotated."""

    def __init__(self, location: BlockCoordinates):
        wx.PyEvent.__init__(self, eventType=_ObjectLocationChangeEventType)
        self._location = location

    @property
    def location(self) -> BlockCoordinates:
        """The location of the object. (x, y, z)"""
        return self._location


# The rotation changed
_ObjectRotationChangeEventType = wx.NewEventType()
EVT_ROTATION_CHANGE = wx.PyEventBinder(_ObjectRotationChangeEventType)


class RotationChangeEvent(wx.PyEvent):
    """Run when the camera has moved or rotated."""

    def __init__(self, rotation: FloatTriplet):
        wx.PyEvent.__init__(self, eventType=_ObjectRotationChangeEventType)
        self._rotation = rotation

    @property
    def rotation(self) -> FloatTriplet:
        """The rotation of the object. (x, y, z)."""
        return self._rotation

    @property
    def rotation_radians(self) -> FloatTriplet:
        """The rotation of the object. (x, y, z)."""
        return tuple(math.radians(r) for r in self._rotation)


# The scale changed
_ObjectScaleChangeEventType = wx.NewEventType()
EVT_SCALE_CHANGE = wx.PyEventBinder(_ObjectScaleChangeEventType)


class ScaleChangeEvent(wx.PyEvent):
    """Run when the camera has moved or rotated."""

    def __init__(self, scale: FloatTriplet):
        wx.PyEvent.__init__(self, eventType=_ObjectScaleChangeEventType)
        self._scale = scale

    @property
    def scale(self) -> FloatTriplet:
        """The scale of the object. (x, y, z)."""
        return self._scale


# The location, rotation or scale changed
_ObjectTransformEventType = wx.NewEventType()
EVT_TRANSFORM_CHANGE = wx.PyEventBinder(_ObjectTransformEventType)


class TransformChangeEvent(wx.PyEvent):
    """Run when the camera has moved or rotated."""

    def __init__(
        self, location: BlockCoordinates, rotation: FloatTriplet, scale: FloatTriplet
    ):
        wx.PyEvent.__init__(self, eventType=_ObjectTransformEventType)
        self._location = location
        self._rotation = rotation
        self._scale = scale

    @property
    def location(self) -> BlockCoordinates:
        """The location of the object. (x, y, z)"""
        return self._location

    @property
    def rotation(self) -> FloatTriplet:
        """The rotation of the object. (x, y, z)."""
        return self._rotation

    @property
    def rotation_radians(self) -> FloatTriplet:
        """The rotation of the object. (x, y, z)."""
        return tuple(math.radians(r) for r in self._rotation)

    @property
    def scale(self) -> FloatTriplet:
        """The scale of the object. (x, y, z)."""
        return self._scale
