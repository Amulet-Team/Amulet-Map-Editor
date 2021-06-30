import wx
from typing import Tuple

import PyMCTranslate


class BasePropertySelect(wx.Panel):
    def __init__(
        self,
        parent: wx.Window,
        translation_manager: PyMCTranslate.TranslationManager,
        platform: str,
        version_number: Tuple[int, int, int],
        force_blockstate: bool,
        namespace: str,
        block_name: str,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        self._translation_manager = translation_manager

        self._platform: str = platform
        self._version_number: Tuple[int, int, int] = version_number
        self._force_blockstate: bool = force_blockstate
        self._namespace: str = namespace
        self._block_name: str = block_name

        self._set_version_block(
            (platform, version_number, force_blockstate, namespace, block_name)
        )

    @property
    def version_block(self) -> Tuple[str, Tuple[int, int, int], bool, str, str]:
        """The version and block these properties relate to."""
        return (
            self._platform,
            self._version_number,
            self._force_blockstate,
            self._namespace,
            self._block_name,
        )

    @version_block.setter
    def version_block(
        self, version_block: Tuple[str, Tuple[int, int, int], bool, str, str]
    ):
        """Set the version and block and update the UI."""
        self._set_version_block(version_block)
        self._rebuild_ui()

    def _set_version_block(
        self, version_block: Tuple[str, Tuple[int, int, int], bool, str, str]
    ):
        """
        Set the version and block these properties relate to.

        :param version_block: The platform, version number, format, namespace and block name
        """
        version = version_block[:3]
        assert (
            version[0] in self._translation_manager.platforms()
            and version[1] in self._translation_manager.version_numbers(version[0])
            and isinstance(version[2], bool)
        ), f"{version} is not a valid version"
        self._platform, self._version_number, self._force_blockstate = version
        block = version_block[3:5]
        assert isinstance(block[0], str) and isinstance(
            block[1], str
        ), "The block namespace and block name must be strings"
        self._namespace, self._block_name = block

    def _rebuild_ui(self):
        """
        Rebuild the UI.
        Run when the version or block is changed.
        """
        raise NotImplementedError
