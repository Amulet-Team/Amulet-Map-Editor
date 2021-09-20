import wx
from amulet_map_editor.api.wx.ui.mc.state import StateHolder, BlockState


class BaseSingleProperty(wx.Panel, StateHolder):
    """
    A UI from which a user can choose one value for each property.

    This is base class for both flavours of single property selection UIs.
    Subclasses must implement the logic.
    """

    state: BlockState

    def __init__(self, parent: wx.Window, state: BlockState):
        StateHolder.__init__(self, state)
        wx.Panel.__init__(self, parent)
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)
