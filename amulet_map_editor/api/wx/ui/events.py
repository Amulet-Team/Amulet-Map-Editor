from wx.lib import newevent

# Sizers only propagate size changes downwards
# This event can be used to propagate those changes upwards so that parent elements know of the size change
ChildSizeEvent, EVT_CHILD_SIZE = newevent.NewCommandEvent()
