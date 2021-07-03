from amulet.api.data_types import PlatformType, VersionNumberTuple


class BaseDefineAPI:
    @property
    def platform(self) -> PlatformType:
        raise NotImplementedError

    @platform.setter
    def platform(self, platform: PlatformType):
        raise NotImplementedError

    @property
    def version_number(self) -> VersionNumberTuple:
        raise NotImplementedError

    @version_number.setter
    def version_number(self, version_number: VersionNumberTuple):
        raise NotImplementedError

    @property
    def namespace(self) -> str:
        raise NotImplementedError

    @namespace.setter
    def namespace(self, namespace: str):
        raise NotImplementedError
