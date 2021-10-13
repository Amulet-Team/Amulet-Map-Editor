from typing import List, Dict, Any
import wx

from amulet_map_editor.api.wx.ui.events import ChildSizeEvent
from .block_entry import BaseBlockEntry, EVT_BLOCK_CLOSE
from .block_entry.custom_fill_button import SrcBlockState
from amulet_map_editor.api.wx.ui.mc.state import StateHolder


class BaseBlockContainer(wx.Panel, StateHolder):
    """This is a UI element that contains one or more block buttons."""

    _blocks: List[BaseBlockEntry]
    state: SrcBlockState

    def __init__(self, parent: wx.Window, default_state: SrcBlockState):
        StateHolder.__init__(self, default_state)
        wx.Panel.__init__(self, parent)
        self._expert = False
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(top_sizer, 0, wx.EXPAND, 5)

        self._add_button = wx.Button(self, label="➕")
        self._add_button.Bind(wx.EVT_BUTTON, lambda evt: self._add_block())
        self._add_button.SetMinSize((28, 28))
        self._add_button.Show(self._expert)
        top_sizer.Add(self._add_button)

        label = wx.StaticText(self, label=self.name, style=wx.ALIGN_CENTER_HORIZONTAL)
        top_sizer.Add(label, 1, wx.ALIGN_CENTER_VERTICAL)

        self._block_sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self._block_sizer, 0, wx.EXPAND, 0)

        self._blocks = []
        self._add_block()

    def _post_change_size(self):
        """Call this when the size changes to notify parent elements."""
        wx.PostEvent(self, ChildSizeEvent(0))

    @property
    def name(self) -> str:
        raise NotImplementedError

    def set_expert(self, expert: bool):
        self._expert = expert
        self._add_button.Show(expert)
        for block in self._blocks:
            block.show_close(expert)
        if not expert:
            while len(self._blocks) > 1:
                self._do_destroy_block_entry(self._blocks[-1])

    def _create_block(self) -> BaseBlockEntry:
        raise NotImplementedError

    def _add_block(self):
        self._do_add_block()
        self._post_change_size()

    def _do_add_block(self):
        block = self._create_block()
        block.Bind(EVT_BLOCK_CLOSE, self._on_block_entry_close)
        self._block_sizer.Add(block, 0, wx.EXPAND | wx.TOP, 5)
        self._blocks.append(block)
        if len(self._blocks) == 1:
            # if there is only one block it cannot be removed.
            self._blocks[-1].enable_close(False)
        else:
            if len(self._blocks) == 2:
                # if this is the second block that was added enable the first
                self._blocks[0].enable_close()
            # enable the block that was just added
            self._blocks[-1].enable_close()
        block.show_close(self._expert)

    def _on_block_entry_close(self, evt):
        window = evt.GetEventObject()
        if isinstance(window, BaseBlockEntry):
            self._destroy_block_entry(window)

    def _destroy_block_entry(self, window: BaseBlockEntry):
        self._do_destroy_block_entry(window)
        self._post_change_size()

    def _do_destroy_block_entry(self, window: BaseBlockEntry):
        if window in self._blocks:
            self._blocks.remove(window)
            window.Destroy()
            if len(self._blocks) == 1:
                block = self._blocks[-1]
                block.enable_close(False)

    @property
    def states(self) -> List[SrcBlockState]:
        return [block.state for block in self._blocks]

    @states.setter
    def states(self, states: List[SrcBlockState]):
        while len(states) > len(self._blocks):
            self._do_add_block()
        while len(states) < len(self._blocks):
            self._do_destroy_block_entry(self._blocks[-1])
        for state, block in zip(states, self._blocks):
            block.state = state
        self._post_change_size()
