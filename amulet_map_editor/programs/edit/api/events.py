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


DimensionChangeEvent, EVT_DIMENSION_CHANGE = newevent.NewEvent()

# the active tool changed
ToolChangeEvent, EVT_TOOL_CHANGE = newevent.NewEvent()
PasteEvent, EVT_PASTE = newevent.NewEvent()

UndoEvent, EVT_UNDO = newevent.NewEvent()
RedoEvent, EVT_REDO = newevent.NewEvent()
CreateUndoEvent, EVT_CREATE_UNDO = newevent.NewEvent()
SaveEvent, EVT_SAVE = newevent.NewEvent()
EditCloseEvent, EVT_EDIT_CLOSE = newevent.NewEvent()
EditEscapeEvent, EVT_EDIT_ESCAPE = newevent.NewEvent()  # the escape key was pressed

# This event is created for each frame that the mouse cursor has moved.
# It should be used to update the cursor box and selection box.
CursorMoveEvent, EVT_CURSOR_MOVE = newevent.NewEvent()

# This event is created each time the cursor box moves
# Used to notify the UI that the cursor box has moved.
CursorBoxMoveEvent, EVT_CURSOR_BOX_MOVE = newevent.NewEvent()

# events fired when the active selection box changes.  TODO: reimplement these
(
    BoxChangeEvent,
    EVT_BOX_CHANGE,
) = newevent.NewEvent()  # one or more of the box coordinates have changed

(
    BoxDisableInputsEvent,
    EVT_BOX_DISABLE_INPUTS,
) = newevent.NewEvent()  # the box starts being edited
(
    BoxEnableInputsEvent,
    EVT_BOX_ENABLE_INPUTS,
) = newevent.NewEvent()  # the box stops being edited
(
    BoxChangeConfirmEvent,
    EVT_BOX_CHANGE_CONFIRM,
) = newevent.NewEvent()  # the coordinates of the box are confirmed

# The button to select the box was clicked. (Usually left mouse) Note based on the state the box may be unchanged.
BoxClickEvent, EVT_BOX_CLICK = newevent.NewEvent()
