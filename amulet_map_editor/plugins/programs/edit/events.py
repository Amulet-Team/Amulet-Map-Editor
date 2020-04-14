from wx.lib import newevent

CameraMoveEvent, EVT_CAMERA_MOVE = newevent.NewEvent()
SelectToolEnabledEvent, EVT_SELECT_TOOL_ENABLED = newevent.NewEvent()
OperationToolEnabledEvent, EVT_OPERATION_TOOL_ENABLED = newevent.NewEvent()
