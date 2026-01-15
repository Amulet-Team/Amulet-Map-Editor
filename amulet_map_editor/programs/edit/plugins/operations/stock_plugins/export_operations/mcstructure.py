from typing import TYPE_CHECKING
import wx
import os

from amulet.api.selection import SelectionGroup
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import Dimension, OperationReturnType
from amulet.level.formats.mcstructure import MCStructureFormatWrapper

from amulet_map_editor.api.wx.ui.version_select import VersionSelect
from amulet_map_editor.programs.edit.api.operations import (
    SimpleOperationPanel,
    OperationError,
)

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class ExportMCStructure(SimpleOperationPanel):
    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)

        options = self._load_options({})

        self._path = options.get("path", "")

        self._version_define = VersionSelect(
            self,
            world.translation_manager,
            options.get("platform", None) or world.level_wrapper.platform,
            allowed_platforms=("bedrock",),
            allow_numerical=False,
        )
        self._sizer.Add(self._version_define, 0, wx.ALL | wx.EXPAND, 5)

        self._add_run_button("Export")
        self.Layout()

    def disable(self):
        self._save_options(
            {
                "path": self._path,
                "version": self._version_define.version_number,
            }
        )

    def _pre_operation(self) -> bool:
        try:
            path = os.path.realpath(self._path)
            fname = os.path.basename(path)
            fdir = os.path.dirname(path)
        except:
            fname = ""
            fdir = ""
        with wx.FileDialog(
            self,
            "Select Save Location",
            defaultDir=fdir,
            defaultFile=fname,
            wildcard="mcstructure file (*.mcstructure)|*.mcstructure",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
        ) as file_dialog:
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return False
            self._path = file_dialog.GetPath()
        return True

    def _operation(
        self, world: "BaseLevel", dimension: Dimension, selection: SelectionGroup
    ) -> OperationReturnType:
        if len(selection.selection_boxes) == 0:
            raise OperationError("No selection was given to export.")
        elif len(selection.selection_boxes) != 1:
            raise OperationError(
                "The mcstructure format only supports a single selection box."
            )

        path = self._path
        version = self._version_define.version_number
        if isinstance(path, str):
            wrapper = MCStructureFormatWrapper(path)
            wrapper.create_and_open("bedrock", version, selection, True)
            wrapper.translation_manager = world.translation_manager
            wrapper_dimension = wrapper.dimensions[0]
            chunk_count = len(list(selection.chunk_locations()))
            yield 0, f"Exporting {os.path.basename(path)}"
            for chunk_index, (cx, cz) in enumerate(selection.chunk_locations()):
                try:
                    chunk = world.get_chunk(cx, cz, dimension)
                    wrapper.commit_chunk(chunk, wrapper_dimension)
                except ChunkLoadError:
                    continue
                yield (chunk_index + 1) / chunk_count
            wrapper.save()
            wrapper.close()
        else:
            raise OperationError(
                "Please specify a save location and version in the options before running."
            )


export = {
    "name": "Export Bedrock .mcstructure",  # the name of the plugin
    "operation": ExportMCStructure,  # the UI class to display
}
