from wx.lib import newevent


CameraMoveEvent, EVT_CAMERA_MOVE = newevent.NewEvent()
CameraRotateEvent, EVT_CAMERA_ROTATE = newevent.NewEvent()

ToolChangeEvent, EVT_TOOL_CHANGE = newevent.NewEvent()

SelectToolEnabledEvent, EVT_SELECT_TOOL_ENABLED = newevent.NewEvent()
OperationToolEnabledEvent, EVT_OPERATION_TOOL_ENABLED = newevent.NewEvent()
ImportToolEnabledEvent, EVT_IMPORT_TOOL_ENABLED = newevent.NewEvent()
ExportToolEnabledEvent, EVT_EXPORT_TOOL_ENABLED = newevent.NewEvent()

BoxGreenCornerChangeEvent, EVT_BOX_GREEN_CORNER_CHANGE = newevent.NewEvent()
BoxBlueCornerChangeEvent, EVT_BOX_BLUE_CORNER_CHANGE = newevent.NewEvent()

BoxCoordsEnableEvent, EVT_BOX_COORDS_ENABLE = newevent.NewEvent()
