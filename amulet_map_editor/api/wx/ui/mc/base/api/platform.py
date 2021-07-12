from typing import Optional
import PyMCTranslate
from amulet.api.data_types import PlatformType


class BaseMCPlatformAPI:
    @property
    def platform(self) -> PlatformType:
        """The active platform."""
        raise NotImplementedError

    @platform.setter
    def platform(self, platform: PlatformType):
        """
        Set the active platform.
        Changes will propagate to the end of this UI.
        No events will be created.

        :param platform: The platform string to set.
        """
        raise NotImplementedError

    def set_platform(self, platform: Optional[PlatformType]):
        """
        Set the active platform.
        Changes will not propagate.
        :meth:`update` must be called once all desired states are set.

        :param platform: The platform string to set.
        """
        raise NotImplementedError


"""
update method should compare the internal state to the UI state and update as required. This should not create events.
Setter methods must change the set_x method and call the update logic to propagate the changes.
set_x methods should just change the internal state. Other code must call the update method
user changing the UI should propagate the changes and create one event at the end.
"""


class BaseMC:
    """A class to store the translation manager."""

    def __init__(
        self,
        translation_manager: PyMCTranslate.TranslationManager,
    ):
        self._translation_manager = translation_manager


class BaseMCPlatform(BaseMC, BaseMCPlatformAPI):
    """A class to store the state of the platform."""

    def __init__(
        self,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
    ):
        super().__init__(translation_manager)
        self._platform = None
        self.set_platform(platform)

    def update(self) -> bool:
        """
        Update the from the internal state.
        No events should be created when calling this method.

        :return: True if data was changed
        """
        raise NotImplementedError

    @property
    def platform(self) -> PlatformType:
        return self._platform

    @platform.setter
    def platform(self, platform: PlatformType):
        self.set_platform(platform)
        self.update()

    def set_platform(self, platform: Optional[PlatformType]):
        if platform is not None and platform in self._translation_manager.platforms():
            self._platform = platform
        else:
            self._platform = self._translation_manager.platforms()[0]
