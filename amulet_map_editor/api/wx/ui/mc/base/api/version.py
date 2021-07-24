from typing import Optional
import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple
from .platform import BaseMCPlatformAPI, BaseMCPlatform


class BaseMCVersionAPI(BaseMCPlatformAPI):
    @property
    def version_number(self) -> VersionNumberTuple:
        """The active version tuple."""
        raise NotImplementedError

    @version_number.setter
    def version_number(self, version_number: VersionNumberTuple):
        """
        Set the active version tuple.
        Changes will propagate to the end of this UI.
        No events will be created.

        :param version_number: The version number to set.
        """
        raise NotImplementedError

    def set_version_number(self, version_number: Optional[VersionNumberTuple]):
        """
        Set the active version tuple.
        Changes will not propagate.
        :meth:`update` must be called once all desired states are set.

        :param version_number: The version number to set.
        """
        raise NotImplementedError

    @property
    def force_blockstate(self) -> bool:
        """
        Is the block format native (False) or blockstate (True)
        Note in cases where the native is blockstate this option does nothing.
        """
        raise NotImplementedError

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        """
        Set if blockstate is forced.
        Changes will propagate to the end of this UI.
        No events will be created.

        :param force_blockstate: False for the native format, True for the blockstate format.
        """
        raise NotImplementedError

    def set_force_blockstate(self, force_blockstate: Optional[bool]):
        """
        Set if blockstate is forced.
        Changes will not propagate.
        :meth:`update` must be called once all desired states are set.

        :param force_blockstate: False for the native format, True for the blockstate format.
        """
        raise NotImplementedError


class BaseMCVersion(BaseMCPlatform, BaseMCVersionAPI):
    """A class to store the state of the platform, version tuple and force blockstate."""

    def __init__(
        self,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = False,
    ):
        super().__init__(translation_manager, platform)
        self._version_number = None
        self.set_version_number(version_number)
        self._force_blockstate = None
        self.set_force_blockstate(force_blockstate)

    @property
    def version_number(self) -> VersionNumberTuple:
        return self._version_number

    @version_number.setter
    def version_number(self, version_number: VersionNumberTuple):
        self.set_version_number(version_number)
        self.push()

    def set_version_number(self, version_number: Optional[VersionNumberTuple]):
        v = None
        if version_number is not None:
            if version_number in self._translation_manager.version_numbers(
                self.platform
            ):
                self._version_number = v = version_number
            else:
                try:
                    self._version_number = v = self._translation_manager.get_version(
                        self.platform, version_number
                    ).version_number
                except KeyError:
                    pass
        if v is None:
            self._version_number = self._translation_manager.version_numbers(
                self.platform
            )[-1]

    @property
    def force_blockstate(self) -> bool:
        return self._force_blockstate

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        self.set_force_blockstate(force_blockstate)
        self.push()

    def set_force_blockstate(self, force_blockstate: Optional[bool]):
        self._force_blockstate = bool(force_blockstate)
