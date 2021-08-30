import wx
from typing import Optional, Dict, Any

from amulet_map_editor.api.wx.ui.mc.block import BaseBlockDefineButton
from .events import BlockCloseEvent


class BaseBlockEntry(wx.Panel):
    """A UI element that holds a block button, weight entry and close button"""

    _button_props = (
        "platform",
        "version_number",
        "force_blockstate",
        "namespace",
        "base_name",
    )

    def __init__(
        self,
        parent: wx.Window,
        **kwargs,
    ):
        super().__init__(parent, **kwargs)
        self._sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.SetSizer(self._sizer)
        self._block_button: Optional[BaseBlockDefineButton] = None
        self._close_button: Optional[wx.Button] = None

    def _init_close_button(self):
        self._close_button = wx.Button(self, label="❌")
        self._close_button.Bind(wx.EVT_BUTTON, self._on_close)
        self._close_button.SetMinSize((28, 28))
        self._sizer.Add(self._close_button)

    def _on_close(self, evt):
        evt2 = BlockCloseEvent()
        evt2.SetEventObject(self)
        wx.PostEvent(self, evt2)

    @property
    def block_button(self) -> BaseBlockDefineButton:
        raise NotImplementedError

    def show_close(self, show: bool = True):
        """Show or hide the close button."""
        self._close_button.Show(show)
        self.Layout()

    def enable_close(self, enable: bool = True):
        self._close_button.Enable(enable)

    @property
    def state(self) -> Dict[str, Any]:
        return {prop: getattr(self.block_button, prop) for prop in self._button_props}

    @state.setter
    def state(self, state: Dict[str, Any]):
        for prop in self._button_props:
            setattr(self.block_button, prop, state.get(prop, None))
