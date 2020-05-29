from wx.lib import newevent


CameraMoveEvent, EVT_CAMERA_MOVE = newevent.NewEvent()
CameraRotateEvent, EVT_CAMERA_ROTATE = newevent.NewEvent()
DimensionChangeEvent, EVT_DIMENSION_CHANGE = newevent.NewEvent()

ToolChangeEvent, EVT_TOOL_CHANGE = newevent.NewEvent()

UndoEvent, EVT_UNDO = newevent.NewEvent()
RedoEvent, EVT_REDO = newevent.NewEvent()
CreateUndoEvent, EVT_CREATE_UNDO = newevent.NewEvent()
SaveEvent, EVT_SAVE = newevent.NewEvent()
EditCloseEvent, EVT_EDIT_CLOSE = newevent.NewEvent()

BoxGreenCornerChangeEvent, EVT_BOX_GREEN_CORNER_CHANGE = newevent.NewEvent()
BoxBlueCornerChangeEvent, EVT_BOX_BLUE_CORNER_CHANGE = newevent.NewEvent()

BoxCoordsEnableEvent, EVT_BOX_COORDS_ENABLE = newevent.NewEvent()
