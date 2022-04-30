import wx
from wx.lib import newevent

from amulet_map_editor.api.opengl.camera import (
    CameraMovedEvent,
    EVT_CAMERA_MOVED,
    ProjectionChangedEvent,
    EVT_PROJECTION_CHANGED,
    SpeedChangedEvent,
    EVT_SPEED_CHANGED,
)

from amulet_map_editor.api.opengl.events import (
    PreDrawEvent,
    EVT_PRE_DRAW,
    DrawEvent,
    EVT_DRAW,
    PostDrawEvent,
    EVT_POST_DRAW,
)

from amulet_map_editor.api.wx.util.button_input import (
    InputPressEvent,
    InputHeldEvent,
    InputReleaseEvent,
    EVT_INPUT_PRESS,
    EVT_INPUT_HELD,
    EVT_INPUT_RELEASE,
)

from .selection import SelectionChangeEvent, EVT_SELECTION_CHANGE


DimensionChangeEvent, EVT_DIMENSION_CHANGE = newevent.NewEvent()

# the active tool changed
_ToolChangeEventType = wx.NewEventType()
EVT_TOOL_CHANGE = wx.PyEventBinder(_ToolChangeEventType)


class ToolChangeEvent(wx.PyEvent):
    """Run when the camera has moved or rotated."""

    def __init__(self, tool: str, state=None):
        wx.PyEvent.__init__(self, eventType=_ToolChangeEventType)
        self.tool = tool
        self.state = state


UndoEvent, EVT_UNDO = newevent.NewEvent()
RedoEvent, EVT_REDO = newevent.NewEvent()
CreateUndoEvent, EVT_CREATE_UNDO = newevent.NewEvent()
SaveEvent, EVT_SAVE = newevent.NewEvent()
EditCloseEvent, EVT_EDIT_CLOSE = newevent.NewEvent()
