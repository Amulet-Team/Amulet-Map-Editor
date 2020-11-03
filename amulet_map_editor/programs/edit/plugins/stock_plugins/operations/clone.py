from typing import TYPE_CHECKING
import wx

from amulet.api.selection import SelectionGroup
from amulet.api.data_types import Dimension, OperationReturnType

from amulet_map_editor.programs.edit.plugins.api.simple_operation_panel import (
    SimpleOperationPanel,
)
from amulet_map_editor.programs.edit.plugins.api.errors import OperationSilentAbort

if TYPE_CHECKING:
    from amulet.api.level import World
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class Clone(SimpleOperationPanel):
    def __init__(
        self, parent: wx.Window, canvas: "EditCanvas", world: "World", options_path: str
    ):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)
        self._add_run_button()
        self.Layout()

    def _operation(
        self, world: "World", dimension: Dimension, selection: SelectionGroup
    ) -> OperationReturnType:
        structure = world.extract_structure(selection, dimension)
        self.canvas.paste(structure, structure.dimensions[0])
        raise OperationSilentAbort

    def unload(self):
        pass


export = {
    "name": "Clone",  # the name of the plugin
    "operation": Clone,  # the actual function to call when running the plugin
}
