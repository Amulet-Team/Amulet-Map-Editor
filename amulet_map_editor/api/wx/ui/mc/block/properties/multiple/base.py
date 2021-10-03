import wx

from amulet.api.block import PropertyTypeMultiple
from amulet_map_editor.api.wx.ui.mc.state import StateHolder, BlockState, State


class BaseMultipleProperty(wx.Panel, StateHolder):
    """
    A UI from which a user can choose zero or more values for each property.

    This is base class for both flavours of multiple property selection UIs.
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

    def _get_ui_properties_multiple(self) -> PropertyTypeMultiple:
        raise NotImplementedError

    def _if_do_state_change(self) -> bool:
        raise NotImplementedError

    def _on_state_change(self):
        if self._if_do_state_change():
            if self.state.is_changed(State.BaseName):
                self._rebuild_properties()
            elif self.state.is_changed(State.PropertiesMultiple):
                if self.state.properties_multiple != self._get_ui_properties_multiple():
                    self._update_properties()

    def _on_property_change(self):
        properties_multiple = self._get_ui_properties_multiple()
        if properties_multiple != self.state.properties_multiple:
            with self.state as state:
                state.properties_multiple = properties_multiple
