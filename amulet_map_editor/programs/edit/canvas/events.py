from wx.lib import newevent

CameraMoveEvent, EVT_CAMERA_MOVE = newevent.NewEvent()
CameraRotateEvent, EVT_CAMERA_ROTATE = newevent.NewEvent()
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

# the block highlighted by the cursor changed position.
SelectionPointChangeEvent, EVT_SELECTION_POINT_CHANGE = newevent.NewEvent()

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
