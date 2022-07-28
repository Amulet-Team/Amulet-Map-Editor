import wx
from amulet.api.block import PropertyType, PropertyTypeMultiple
from amulet.api.data_types import VersionNumberTuple, PlatformType


class BaseBlockChangeEvent:
    def __init__(
        self,
        platform: PlatformType,
        version_number: VersionNumberTuple,
        force_blockstate: bool,
        namespace: str,
        base_name: str,
    ):
        self._platform = platform
        self._version_number = version_number
        self._force_blockstate = force_blockstate
        self._namespace = namespace
        self._base_name = base_name

    @property
    def platform(self) -> PlatformType:
        return self._platform

    @property
    def version_number(self) -> VersionNumberTuple:
        return self._version_number

    @property
    def force_blockstate(self) -> bool:
        return self._force_blockstate

    @property
    def namespace(self) -> str:
        return self._namespace

    @property
    def base_name(self) -> str:
        return self._base_name


_BlockChangeEventType = wx.NewEventType()
EVT_BLOCK_CHANGE = wx.PyEventBinder(_BlockChangeEventType)


class BlockChangeEvent(wx.PyEvent, BaseBlockChangeEvent):
    """
    Run when the block define UI changes.
    """

    def __init__(
        self,
        platform: PlatformType,
        version_number: VersionNumberTuple,
        force_blockstate: bool,
        namespace: str,
        base_name: str,
        properties: PropertyType,
    ):
        wx.PyEvent.__init__(self, eventType=_BlockChangeEventType)
        BaseBlockChangeEvent.__init__(
            self,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
        )
        self._properties = properties

    @property
    def properties(self) -> PropertyType:
        return self._properties


_WildcardBlockChangeEventType = wx.NewEventType()
EVT_WILDCARD_BLOCK_CHANGE = wx.PyEventBinder(_WildcardBlockChangeEventType)


class WildcardBlockChangeEvent(wx.PyEvent, BaseBlockChangeEvent):
    """
    Run when the wildcard block define UI changes.
    """

    def __init__(
        self,
        platform: PlatformType,
        version_number: VersionNumberTuple,
        force_blockstate: bool,
        namespace: str,
        base_name: str,
        selected_properties: PropertyTypeMultiple,
    ):
        wx.PyEvent.__init__(self, eventType=_WildcardBlockChangeEventType)
        BaseBlockChangeEvent.__init__(
            self,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
        )
        self._selected_properties = selected_properties

    @property
    def selected_properties(self) -> PropertyTypeMultiple:
        return self._selected_properties
