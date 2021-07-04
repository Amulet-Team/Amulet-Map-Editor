from typing import Optional
import PyMCTranslate
from amulet.api.data_types import PlatformType, VersionNumberTuple


class BaseMCPlatformAPI:
    @property
    def platform(self) -> PlatformType:
        raise NotImplementedError

    @platform.setter
    def platform(self, platform: PlatformType):
        raise NotImplementedError

    def set_platform(self, platform: PlatformType):
        raise NotImplementedError
