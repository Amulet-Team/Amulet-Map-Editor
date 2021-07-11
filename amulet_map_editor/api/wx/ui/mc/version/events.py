import wx
from typing import Tuple

_PlatformEventType = wx.NewEventType()
EVT_PLATFORM_CHANGE = wx.PyEventBinder(_PlatformEventType)


class PlatformChangeEvent(wx.PyEvent):
    """
    Event run when the platform input is changed.
    Is run when the user or code changes the platform.
    """

    def __init__(self, platform: str, old_platform: str):
        wx.PyEvent.__init__(self, eventType=_PlatformEventType)
        self._platform = platform
        self._old_platform = old_platform

    @property
    def platform(self) -> str:
        """The platform that the selection was changed to."""
        return self._platform

    @property
    def old_platform(self) -> str:
        """The platform that was selected before it was changed."""
        return self._old_platform


_VersionChangeEventType = wx.NewEventType()
EVT_VERSION_CHANGE = wx.PyEventBinder(_VersionChangeEventType)


class VersionChangeEvent(wx.PyEvent):
    """
    Event is run at the same time as :class:`FormatChangeEvent` but holds all the information about the version.
    """

    def __init__(
        self,
        platform: str,
        version_number: Tuple[int, ...],
        force_blockstate: bool,
        old_platform: str,
        old_version_number: Tuple[int, ...],
        old_force_blockstate: bool,
    ):
        wx.PyEvent.__init__(self, eventType=_VersionChangeEventType)
        self._platform = platform
        self._version_number = version_number
        self._force_blockstate = force_blockstate
        self._old_platform = old_platform
        self._old_version_number = old_version_number
        self._old_force_blockstate = old_force_blockstate

    @property
    def platform(self) -> str:
        """The platform that the selection was changed to."""
        return self._platform

    @property
    def version_number(self) -> Tuple[int, ...]:
        """The version_number that the selection was changed to."""
        return self._version_number

    @property
    def force_blockstate(self) -> bool:
        """
        True if the format is force blockstate, False otherwise.
        """
        return self._force_blockstate

    @property
    def old_platform(self) -> str:
        """The platform that was selected before it was changed."""
        return self._old_platform

    @property
    def old_version_number(self) -> Tuple[int, ...]:
        """The version_number that was selected before it was changed."""
        return self._old_version_number

    @property
    def old_force_blockstate(self) -> bool:
        """
        True if the format was force blockstate, False otherwise.
        """
        return self._old_force_blockstate
