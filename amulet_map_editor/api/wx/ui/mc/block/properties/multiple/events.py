import wx
from amulet.api.block import PropertyTypeMultiple

_MultiplePropertiesChangeEventType = wx.NewEventType()
EVT_MULTIPLE_PROPERTIES_CHANGE = wx.PyEventBinder(_MultiplePropertiesChangeEventType)


class MultiplePropertiesChangeEvent(wx.PyCommandEvent):
    """
    Run when the properties UI changes.
    """

    def __init__(self, selected_properties: PropertyTypeMultiple):
        wx.PyCommandEvent.__init__(self, eventType=_MultiplePropertiesChangeEventType)
        self._selected_properties = selected_properties

    @property
    def selected_properties(self) -> PropertyTypeMultiple:
        return self._selected_properties
