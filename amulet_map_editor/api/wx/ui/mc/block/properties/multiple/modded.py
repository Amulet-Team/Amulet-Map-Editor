import wx
from collections import namedtuple

from amulet_map_editor.api.wx.ui.mc.state import BlockState
from ..single.modded import BaseModdedSingleProperty

PropertyStorage = namedtuple(
    "PropertyStorage", ("sizer", "key_entry", "value_entry", "snbt_text")
)


class BaseModdedMultipleProperty(BaseModdedSingleProperty):
    """
    A UI from which a user can choose zero or more values for each property.

    This is used when the block is not know so the user can define the properties themselves.
    """

    # TODO: This currently only allows on value to be defined.
    state: BlockState

    def _on_property_change(self):
        properties = self._get_ui_properties()
        if properties != self.state.properties:
            with self.state as state:
                state.properties = properties
                state.properties_multiple = {
                    key: (val,) for key, val in properties.items()
                }


class ModdedMultipleProperty(BaseModdedMultipleProperty):
    def __init__(self, parent: wx.Window, state: BlockState):
        super().__init__(parent, state)
        self._rebuild_properties()
