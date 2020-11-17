from typing import TYPE_CHECKING
import wx
import os

from amulet.api.selection import SelectionGroup
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import Dimension, OperationReturnType
from amulet.structure_interface.schematic import SchematicFormatWrapper

from amulet_map_editor.api.wx.ui.version_select import PlatformSelect
from amulet_map_editor.programs.edit.plugins.api.simple_operation_panel import (
    SimpleOperationPanel,
)
from amulet_map_editor.programs.edit.plugins.api.errors import OperationError

if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas

WarningMsg = """The Schematic format is a
legacy format that can only
save data in the numerical
format. Anything that was
added to the game in version
1.13 or after will not be
saved in the schematic file.

We suggest using the Construction
file format instead."""


class ExportSchematic(SimpleOperationPanel):
    def __init__(
        self, parent: wx.Window, canvas: "EditCanvas", world: "World", options_path: str
    ):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)

        options = self._load_options({})

        self._file_picker = wx.FilePickerCtrl(
            self,
            path=options.get("path", ""),
            wildcard="Schematic file (*.schematic)|*.schematic",
            style=wx.FLP_USE_TEXTCTRL | wx.FLP_SAVE | wx.FLP_OVERWRITE_PROMPT,
        )
        self._sizer.Add(self._file_picker, 0, wx.ALL | wx.CENTER, 5)
        self._platform_define = PlatformSelect(
            self,
            world.translation_manager,
            options.get("platform", None) or world.world_wrapper.platform,
            allow_universal=False,
        )
        self._sizer.Add(self._platform_define, 0, wx.CENTRE, 5)
        self._sizer.Add(
            wx.StaticText(self, label=WarningMsg, style=wx.ALIGN_CENTRE_HORIZONTAL),
            0,
            wx.ALL | wx.CENTER,
            5,
        )
        self._add_run_button("Export")
        self.Layout()

    def unload(self):
        self._save_options(
            {
                "path": self._file_picker.GetPath(),
                "platform": self._platform_define.platform,
            }
        )

    def _operation(
        self, world: "World", dimension: Dimension, selection: SelectionGroup
    ) -> OperationReturnType:
        if len(selection.selection_boxes) == 0:
            raise OperationError("No selection was given to export.")
        elif len(selection.selection_boxes) != 1:
            raise OperationError(
                "The schematic format only supports a single selection box."
            )

        path = self._file_picker.GetPath()
        platform = self._platform_define.platform
        if isinstance(path, str) and path.endswith(".schematic") and platform:
            wrapper = SchematicFormatWrapper(path, "w")
            wrapper.platform = platform
            wrapper.selection = selection
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
                "Please specify a save location and platform in the options before running."
            )


export = {
    "name": "Export Schematic (legacy)",  # the name of the plugin
    "operation": ExportSchematic,  # the UI class to display
}
