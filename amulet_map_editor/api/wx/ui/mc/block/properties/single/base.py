import wx

from amulet.api.block import PropertyType, PropertyValueType
from amulet_map_editor.api.wx.ui.mc.state import StateHolder, BlockState, State


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

    def _rebuild_properties(self):
        raise NotImplementedError

    def _tear_down_properties(self):
        raise NotImplementedError

    def _update_properties(self):
        raise NotImplementedError

    def _get_ui_properties(self) -> PropertyType:
        raise NotImplementedError

    def _if_do_state_change(self) -> bool:
        raise NotImplementedError

    def _on_state_change(self):
        if self._if_do_state_change():
            if self.state.is_changed(State.BaseName):
                self._rebuild_properties()
            elif self.state.is_changed(State.Properties):
                if self.state.properties != self._get_ui_properties():
                    self._update_properties()

    def _on_property_change(self):
        properties = self._get_ui_properties()
        if properties != self.state.properties:
            with self.state as state:
                state.properties = properties
