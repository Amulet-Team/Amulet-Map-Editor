from wx.lib import newevent

from amulet_map_editor.api.opengl.camera import (
    CameraMovedEvent,
    EVT_CAMERA_MOVED,
    ProjectionChangedEvent,
    EVT_PROJECTION_CHANGED,
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
ToolChangeEvent, EVT_TOOL_CHANGE = newevent.NewEvent()
PasteEvent, EVT_PASTE = newevent.NewEvent()

UndoEvent, EVT_UNDO = newevent.NewEvent()
RedoEvent, EVT_REDO = newevent.NewEvent()
CreateUndoEvent, EVT_CREATE_UNDO = newevent.NewEvent()
SaveEvent, EVT_SAVE = newevent.NewEvent()
EditCloseEvent, EVT_EDIT_CLOSE = newevent.NewEvent()

# This event is created each time the cursor box moves
# Used to notify the UI that the cursor box has moved.
# TODO: remove this
CursorBoxMoveEvent, EVT_CURSOR_BOX_MOVE = newevent.NewEvent()

# The button to select the box was clicked. (Usually left mouse) Note based on the state the box may be unchanged.
# TODO: remove this
BoxClickEvent, EVT_BOX_CLICK = newevent.NewEvent()
