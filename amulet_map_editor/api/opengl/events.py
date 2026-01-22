from wx.lib import newevent

from .camera import (
    CameraMovedEvent,
    EVT_CAMERA_MOVED,
    ProjectionChangedEvent,
    EVT_PROJECTION_CHANGED,
)

PreDrawEvent, EVT_PRE_DRAW = newevent.NewEvent()
