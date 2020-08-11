from typing import TYPE_CHECKING
import wx
import os

from amulet.api.selection import SelectionGroup
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import Dimension, OperationReturnType
from amulet.structure_interface.mcstructure import MCStructureFormatWrapper

from amulet_map_editor.api.wx.ui.version_select import VersionSelect
from amulet_map_editor.programs.edit.plugins.api.simple_operation_panel import (
    SimpleOperationPanel,
)
from amulet_map_editor.programs.edit.plugins.api.errors import OperationError

if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class ExportMCStructure(SimpleOperationPanel):
    def __init__(
        self, parent: wx.Window, canvas: "EditCanvas", world: "World", options_path: str
    ):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)

        options = self._load_options({})

        self._file_picker = wx.FilePickerCtrl(
            self,
            path=options.get("path", ""),
            wildcard="mcstructure file (*.mcstructure)|*.mcstructure",
            style=wx.FLP_USE_TEXTCTRL | wx.FLP_SAVE | wx.FLP_OVERWRITE_PROMPT,
        )
        self._sizer.Add(self._file_picker, 0, wx.ALL | wx.CENTER, 5)
        self._version_define = VersionSelect(
            self,
            world.translation_manager,
            options.get("platform", None) or world.world_wrapper.platform,
            allowed_platforms=("bedrock",),
            allow_numerical=False,
        )
        self._sizer.Add(self._version_define, 0, wx.CENTRE, 5)
        self._add_run_button("Export")
        self.Layout()

    def unload(self):
        self._save_options(
            {
                "path": self._file_picker.GetPath(),
                "version": self._version_define.version_number,
            }
        )

    def _operation(
        self, world: "World", dimension: Dimension, selection: SelectionGroup
    ) -> OperationReturnType:
        if len(selection.selection_boxes) == 0:
            raise OperationError("No selection was given to export.")
        elif len(selection.selection_boxes) != 1:
            raise OperationError(
                "The mcstructure format only supports a single selection box."
            )

        path = self._file_picker.GetPath()
        version = self._version_define.version_number

        if isinstance(path, str) and path.endswith(".mcstructure") and version:
            wrapper = MCStructureFormatWrapper(path, "w")
            wrapper.selection = selection
            wrapper.version = version
            wrapper.translation_manager = world.translation_manager
            wrapper.open()
            chunk_count = len(list(selection.chunk_locations()))
            yield 0, f"Exporting {os.path.basename(path)}"
            for chunk_index, (cx, cz) in enumerate(selection.chunk_locations()):
                try:
                    chunk = world.get_chunk(cx, cz, dimension)
                    wrapper.commit_chunk(chunk, world.palette)
                except ChunkLoadError:
                    continue
                yield (chunk_index + 1) / chunk_count

            wrapper.close()
        else:
            raise OperationError(
                "Please specify a save location and version in the options before running."
            )


export = {
    "name": "Export Bedrock .mcstructure",  # the name of the plugin
    "operation": ExportMCStructure,  # the UI class to display
}
