from wx.lib import newevent

(
    ItemNamespaceChangeEvent,
    EVT_ITEM_NAMESPACE_CHANGE,
) = newevent.NewCommandEvent()  # the namespace entry changed
(
    ItemNameChangeEvent,
    EVT_ITEM_NAME_CHANGE,
) = newevent.NewCommandEvent()  # the name entry changed
(
    ItemChangeEvent,
    EVT_ITEM_CHANGE,
) = (
    newevent.NewCommandEvent()
)  # the name or namespace changed. Generated after EVT_ITEM_NAME_CHANGE
(
    PickEvent,
    EVT_PICK,
) = newevent.NewCommandEvent()  # The pick button was pressed
