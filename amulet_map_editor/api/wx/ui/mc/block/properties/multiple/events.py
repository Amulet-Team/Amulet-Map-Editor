import wx
from typing import Dict, Tuple
from amulet.api.block import PropertyValueType

_MultiplePropertiesChangeEventType = wx.NewEventType()
EVT_MULTIPLE_PROPERTIES_CHANGE = wx.PyEventBinder(_MultiplePropertiesChangeEventType)


class MultiplePropertiesChangeEvent(wx.PyEvent):
    """
    Run when the properties UI changes.
    """

    def __init__(self, properties: Dict[str, Tuple[PropertyValueType, ...]]):
        wx.PyEvent.__init__(self, eventType=_MultiplePropertiesChangeEventType)
        self._properties = properties

    @property
    def properties(self) -> Dict[str, Tuple[PropertyValueType, ...]]:
        return self._properties
