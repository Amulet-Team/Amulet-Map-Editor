import wx

_BlockIDChangeEventType = wx.NewEventType()
EVT_BLOCK_ID_CHANGE = wx.PyEventBinder(_BlockIDChangeEventType)


class BlockIDChangeEvent(wx.PyEvent):
    """
    Run when the block resource identifier changes.
    """

    def __init__(
            self,
            namespace: str,
            base_name: str,
            old_namespace: str,
            old_base_name: str,
    ):
        wx.PyEvent.__init__(self, eventType=_BlockIDChangeEventType)
        self._namespace = namespace
        self._base_name = base_name
        self._old_namespace = old_namespace
        self._old_base_name = old_base_name

    @property
    def namespace(self) -> str:
        return self._namespace

    @property
    def base_name(self) -> str:
        return self._base_name

    @property
    def old_namespace(self) -> str:
        return self._old_namespace

    @property
    def old_base_name(self) -> str:
        return self._old_base_name
