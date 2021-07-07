from amulet.api.data_types import VersionNumberTuple
from .platform import BaseMCPlatformAPI


class BaseMCVersionAPI(BaseMCPlatformAPI):
    @property
    def version_number(self) -> VersionNumberTuple:
        raise NotImplementedError

    @version_number.setter
    def version_number(self, version_number: VersionNumberTuple):
        raise NotImplementedError

    @property
    def force_blockstate(self) -> bool:
        raise NotImplementedError

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        raise NotImplementedError

