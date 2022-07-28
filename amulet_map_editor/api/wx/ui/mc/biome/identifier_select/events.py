import wx
from ...base.base_identifier_select import BaseIDChangeEvent

_BiomeIDChangeEventType = wx.NewEventType()
EVT_BIOME_ID_CHANGE = wx.PyEventBinder(_BiomeIDChangeEventType)


class BiomeIDChangeEvent(BaseIDChangeEvent):
    """
    Run when the biome resource identifier changes.
    """

    def __init__(
        self,
        namespace: str,
        base_name: str,
    ):
        super().__init__(namespace, base_name)
        self.SetEventType(_BiomeIDChangeEventType)
