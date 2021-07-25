from typing import Optional

import PyMCTranslate
from amulet.api.data_types import VersionNumberTuple
from .version import BaseMCVersionAPI, BaseMCVersion


class BaseMCResourceIDAPI(BaseMCVersionAPI):
    @property
    def namespace(self) -> str:
        """The active namespace."""
        raise NotImplementedError

    @namespace.setter
    def namespace(self, namespace: str):
        """
        Set the active namespace.
        Changes will propagate to the end of this UI.
        No events will be created.

        :param namespace: The namespace to set.
        """
        raise NotImplementedError

    def _set_namespace(self, namespace: Optional[str]):
        """
        Set the active namespace.
        Changes will not propagate.
        :meth:`update` must be called once all desired states are set.

        :param namespace: The namespace to set.
        """
        raise NotImplementedError

    @property
    def base_name(self) -> str:
        """The active base name."""
        raise NotImplementedError

    @base_name.setter
    def base_name(self, base_name: str):
        """
        Set the active base name.
        Changes will propagate to the end of this UI.
        No events will be created.

        :param base_name: The base name to set.
        """
        raise NotImplementedError

    def _set_base_name(self, base_name: Optional[str]):
        """
        Set the active base name.
        Changes will not propagate.
        :meth:`update` must be called once all desired states are set.

        :param base_name: The base name to set.
        """
        raise NotImplementedError


class BaseMCResourceID(BaseMCVersion, BaseMCResourceIDAPI):
    def __init__(
        self,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str = None,
        version_number: VersionNumberTuple = None,
        force_blockstate: bool = False,
        namespace: str = None,
        base_name: str = None,
    ):
        super().__init__(
            translation_manager, platform, version_number, force_blockstate
        )
        self._namespace = None
        self._set_namespace(namespace)
        self._base_name = None
        self._set_base_name(base_name)

    @property
    def namespace(self) -> str:
        return self._namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self._set_namespace(namespace)
        self._schedule_push()

    def _set_namespace(self, namespace: Optional[str]):
        raise NotImplementedError

    @property
    def base_name(self) -> str:
        return self._base_name

    @base_name.setter
    def base_name(self, base_name: str):
        self._set_base_name(base_name)
        self._schedule_push()

    def _set_base_name(self, base_name: Optional[str]):
        raise NotImplementedError
