from typing import TYPE_CHECKING
import wx

from amulet.api.selection import SelectionGroup
from amulet.api.data_types import Dimension, OperationReturnType

from amulet_map_editor.programs.edit.api.operations import (
    SimpleOperationPanel,
    OperationSilentAbort,
)

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class Clone(SimpleOperationPanel):
    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)
        self._add_run_button()
        self.Layout()

    def _operation(
        self, world: "BaseLevel", dimension: Dimension, selection: SelectionGroup
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
