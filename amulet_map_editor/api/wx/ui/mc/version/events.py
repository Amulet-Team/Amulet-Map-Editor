import wx
from typing import Tuple
from amulet.api.data_types import VersionNumberTuple

_PlatformEventType = wx.NewEventType()
EVT_PLATFORM_CHANGE = wx.PyEventBinder(_PlatformEventType)


class PlatformChangeEvent(wx.PyEvent):
    """
    Event run when the platform input is changed.
    Is run when the user or code changes the platform.
    """

    def __init__(self, platform: str):
        wx.PyEvent.__init__(self, eventType=_PlatformEventType)
        self._platform = platform

    @property
    def platform(self) -> str:
        """The platform that the selection was changed to."""
        return self._platform


_VersionChangeEventType = wx.NewEventType()
EVT_VERSION_CHANGE = wx.PyEventBinder(_VersionChangeEventType)


class VersionChangeEvent(wx.PyEvent):
    """
    Event is run at the same time as :class:`FormatChangeEvent` but holds all the information about the version.
    """

    def __init__(
        self,
        platform: str,
        version_number: VersionNumberTuple,
        force_blockstate: bool,
    ):
        wx.PyEvent.__init__(self, eventType=_VersionChangeEventType)
        self._platform = platform
        self._version_number = version_number
        self._force_blockstate = force_blockstate

    @property
    def platform(self) -> str:
        """The platform that the selection was changed to."""
        return self._platform

    @property
    def version_number(self) -> VersionNumberTuple:
        """The version_number that the selection was changed to."""
        return self._version_number

    @property
    def force_blockstate(self) -> bool:
        """
        True if the format is force blockstate, False otherwise.
        """
        return self._force_blockstate
