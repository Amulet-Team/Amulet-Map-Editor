import wx
from wx.lib import newevent

(
    PlatformChangeEvent,
    EVT_PLATFORM_CHANGE,
) = newevent.NewCommandEvent()  # the platform entry changed
(
    VersionNumberChangeEvent,
    EVT_VERSION_NUMBER_CHANGE,
) = newevent.NewCommandEvent()  # the version number entry changed
(
    FormatChangeEvent,
    EVT_FORMAT_CHANGE,
) = (
    newevent.NewCommandEvent()
)  # the format entry changed (is fired even if the entry isn't visible)
(
    VersionChangeEvent,
    EVT_VERSION_CHANGE,
) = (
    newevent.NewCommandEvent()
)  # one of the above changed. Fired after EVT_FORMAT_CHANGE
