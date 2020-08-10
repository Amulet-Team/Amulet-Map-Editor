import wx
import os
from typing import TYPE_CHECKING

from amulet.api.registry import BlockManager
from amulet.api.structure import Structure
from amulet.api.selection import SelectionGroup
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import Dimension
from amulet.structure_interface.mcstructure import MCStructureFormatWrapper

from amulet_map_editor.programs.edit.plugins.api.simple_operation_panel import (
    SimpleOperationPanel,
)
from amulet_map_editor.programs.edit.plugins.api.errors import OperationError

if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class ImportMCStructure(SimpleOperationPanel):
    def __init__(
        self, parent: wx.Window, canvas: "EditCanvas", world: "World", options_path: str
    ):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)

        options = self._load_options({})

        self._file_picker = wx.FilePickerCtrl(
            self,
            path=options.get("path", ""),
            wildcard="Bedrock mcstructure file (*.mcstructure)|*.mcstructure",
            style=wx.FLP_USE_TEXTCTRL | wx.FLP_OPEN,
        )
        self._sizer.Add(self._file_picker, 0, wx.ALL | wx.CENTER, 5)
        self._add_run_button("Load")
        self.Layout()

    def unload(self):
        self._save_options({"path": self._file_picker.GetPath()})

    def _operation(
        self, world: "World", dimension: Dimension, selection: SelectionGroup
    ):
        path = self._file_picker.GetPath()

        if (
            isinstance(path, str)
            and path.endswith(".mcstructure")
            and os.path.isfile(path)
        ):
            wrapper = MCStructureFormatWrapper(path, "r")
            wrapper.translation_manager = world.translation_manager
            wrapper.open()
            selection = wrapper.selection

            global_palette = BlockManager()
            chunks = {}
            chunk_count = len(list(wrapper.all_chunk_coords()))
            yield 0, f"Importing {os.path.basename(path)}"
            for chunk_index, (cx, cz) in enumerate(wrapper.all_chunk_coords()):
                try:
                    chunk = chunks[(cx, cz)] = wrapper.load_chunk(cx, cz)
                    chunk.block_palette = global_palette
                except ChunkLoadError:
                    pass
                yield (chunk_index + 1) / chunk_count

            wrapper.close()
            self.canvas.paste(Structure(chunks, global_palette, selection))
        else:
            raise OperationError(
                "Please specify a mcstructure file in the options before running."
            )


export = {
    "name": "Import Bedrock .mcstructure",  # the name of the plugin
    "operation": ImportMCStructure,  # the UI class to display
}
