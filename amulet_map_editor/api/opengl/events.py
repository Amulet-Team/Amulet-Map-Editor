from wx.lib import newevent

PreDrawEvent, EVT_PRE_DRAW = newevent.NewEvent()
DrawEvent, EVT_DRAW = newevent.NewEvent()
PostDrawEvent, EVT_POST_DRAW = newevent.NewEvent()
