import wx
from amulet.api.block import PropertyType

_SinglePropertiesChangeEventType = wx.NewEventType()
EVT_SINGLE_PROPERTIES_CHANGE = wx.PyEventBinder(_SinglePropertiesChangeEventType)


class SinglePropertiesChangeEvent(wx.PyEvent):
    """
    Run when the properties UI changes.
    """

    def __init__(self, properties: PropertyType):
        wx.PyEvent.__init__(self, eventType=_SinglePropertiesChangeEventType)
        self._properties = properties

    @property
    def properties(self) -> PropertyType:
        return self._properties
