from wx.lib import newevent

(
    WidgetSizeChangeEvent,
    EVT_WIDGET_SIZE_CHANGED,
) = (
    newevent.NewCommandEvent()
)  # Emitted when a widget's size changed in a way that the parent needs to be aware of.
