import wx
from typing import Optional

from amulet.api.data_types import PlatformType, VersionNumberTuple
from amulet_map_editor.api.wx.ui.mc.api import BaseMCBlockIdentifierAPI
from amulet_map_editor.api.wx.ui.mc.block.define import BaseBlockDefine


class BaseBlockDefineButton(wx.Button, BaseMCBlockIdentifierAPI):
    def __init__(
        self,
        parent: wx.Window,
    ):
        super().__init__(parent)
        self._dialog: Optional[wx.Dialog] = None
        self._block_widget: Optional[BaseBlockDefine] = None
        self.Bind(wx.EVT_BUTTON, self._on_press)

    def _on_press(self, evt):
        self._dialog.Fit()
        if self._dialog.ShowModal() == wx.ID_OK:
            self.update_button()
        # TODO: There is currently a bug if the user clicks cancel and clicks the button again the UI will not get reset.
        #  In order to fix this, this class will need to store the state outside of the UI.
        #  This should probably be done for all the UI elements

    def update_button(self):
        """Update the text on the button from the internal state."""
        raise NotImplementedError

    @property
    def platform(self) -> PlatformType:
        return self._block_widget.platform

    @platform.setter
    def platform(self, platform: PlatformType):
        self._set_platform(platform)
        self.update_button()

    def _set_platform(self, platform: PlatformType):
        self._block_widget.platform = platform

    @property
    def version_number(self) -> VersionNumberTuple:
        return self._block_widget.version_number

    @version_number.setter
    def version_number(self, version_number: VersionNumberTuple):
        self._set_version_number(version_number)
        self.update_button()

    def _set_version_number(self, version_number: VersionNumberTuple):
        self._block_widget.version_number = version_number

    @property
    def namespace(self) -> str:
        return self._block_widget.namespace

    @namespace.setter
    def namespace(self, namespace: str):
        self._set_namespace(namespace)
        self.update_button()

    def _set_namespace(self, namespace: str):
        self._block_widget.namespace = namespace

    @property
    def force_blockstate(self) -> bool:
        return self._block_widget.force_blockstate

    @force_blockstate.setter
    def force_blockstate(self, force_blockstate: bool):
        self._set_force_blockstate(force_blockstate)
        self.update_button()

    def _set_force_blockstate(self, force_blockstate: bool):
        self._block_widget.force_blockstate = force_blockstate

    @property
    def block_name(self) -> str:
        return self._block_widget.block_name

    @block_name.setter
    def block_name(self, block_name: str):
        self.set_block_name(block_name)
        self.update_button()

    def set_block_name(self, block_name: str):
        self._block_widget.block_name = block_name
