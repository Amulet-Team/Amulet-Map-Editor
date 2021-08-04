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
        old_platform: str,
        old_version_number: VersionNumberTuple,
        old_force_blockstate: bool,
        old_namespace: str,
        old_base_name: str,
    ):
        self._platform = platform
        self._version_number = version_number
        self._force_blockstate = force_blockstate
        self._namespace = namespace
        self._base_name = base_name
        self._old_platform = old_platform
        self._old_version_number = old_version_number
        self._old_force_blockstate = old_force_blockstate
        self._old_namespace = old_namespace
        self._old_base_name = old_base_name

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

    @property
    def old_platform(self) -> str:
        return self._old_platform

    @property
    def old_version_number(self) -> VersionNumberTuple:
        return self._old_version_number

    @property
    def old_force_blockstate(self) -> bool:
        return self._old_force_blockstate

    @property
    def old_namespace(self) -> str:
        return self._old_namespace

    @property
    def old_base_name(self) -> str:
        return self._old_base_name


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
        old_platform: str,
        old_version_number: VersionNumberTuple,
        old_force_blockstate: bool,
        old_namespace: str,
        old_base_name: str,
        old_properties: PropertyType,
    ):
        wx.PyEvent.__init__(self, eventType=_BlockChangeEventType)
        BaseBlockChangeEvent.__init__(
            self,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
            old_platform,
            old_version_number,
            old_force_blockstate,
            old_namespace,
            old_base_name,
        )
        self._properties = properties
        self._old_properties = old_properties

    @property
    def properties(self) -> PropertyType:
        return self._properties

    @property
    def old_properties(self) -> PropertyType:
        return self._old_properties


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
        old_platform: str,
        old_version_number: VersionNumberTuple,
        old_force_blockstate: bool,
        old_namespace: str,
        old_base_name: str,
        old_selected_properties: PropertyTypeMultiple,
    ):
        wx.PyEvent.__init__(self, eventType=_WildcardBlockChangeEventType)
        BaseBlockChangeEvent.__init__(
            self,
            platform,
            version_number,
            force_blockstate,
            namespace,
            base_name,
            old_platform,
            old_version_number,
            old_force_blockstate,
            old_namespace,
            old_base_name,
        )
        self._selected_properties = selected_properties
        self._old_selected_properties = old_selected_properties

    @property
    def selected_properties(self) -> PropertyTypeMultiple:
        return self._selected_properties

    @property
    def old_selected_properties(self) -> PropertyTypeMultiple:
        return self._old_selected_properties
