import wx
from wx.lib import newevent

(
    PickEvent,
    EVT_PICK,
) = newevent.NewCommandEvent()  # The pick button was pressed


class BaseIDChangeEvent(wx.PyEvent):
    """
    Run when the identifier changes.
    """

    def __init__(
        self,
        namespace: str,
        base_name: str,
        old_namespace: str,
        old_base_name: str,
    ):
        wx.PyEvent.__init__(self)
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
