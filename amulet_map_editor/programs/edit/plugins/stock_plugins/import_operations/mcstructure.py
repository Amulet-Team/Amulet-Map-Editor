from typing import TYPE_CHECKING
import wx

import os
from amulet_map_editor.amulet_wx.ui.simple import SimpleDialog
from amulet.api.block import BlockManager
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import Dimension
from amulet.api.structure import Structure
from amulet.structure_interface.mcstructure import MCStructureFormatWrapper
from amulet.operations.paste import paste

if TYPE_CHECKING:
    from amulet.api.world import World


def show_ui(parent, world: "World", options: dict) -> dict:
    dialog = SimpleDialog(parent, 'Import Bedrock .mcstructure')
    file_picker = wx.FilePickerCtrl(
        dialog,
        path=options.get('path', ''),
        wildcard="Bedrock mcstructure file (*.mcstructure)|*.mcstructure",
        style=wx.FLP_USE_TEXTCTRL | wx.FLP_OPEN
    )
    dialog.sizer.Add(file_picker, 0, wx.ALL, 5)
    dialog.Fit()

    if dialog.ShowModal() == wx.ID_OK:
        options = {
            "path": file_picker.GetPath()
        }
    return options


def import_schematic(
    world: "World",
    dimension: Dimension,
    options: dict
) -> Structure:
    path = options.get('path', None)
    if isinstance(path, str) and path.endswith('.mcstructure') and os.path.isfile(path):
        wrapper = MCStructureFormatWrapper(path, 'r')
        wrapper.translation_manager = world.translation_manager
        wrapper.open()
        selection = wrapper.selection

        global_palette = BlockManager()
        chunks = {}
        for (cx, cz) in wrapper.all_chunk_coords():
            try:
                chunks[(cx, cz)] = wrapper.load_chunk(cx, cz, global_palette)
            except ChunkLoadError:
                pass

        wrapper.close()
        return Structure(
            chunks,
            global_palette,
            selection
        )
    else:
        raise Exception('Please specify a mcstructure file in the options before running.')


export = {
    "v": 1,  # a version 1 plugin
    "name": "Import Bedrock .mcstructure",  # the name of the plugin
    "features": ["src_selection", "wxoptions", "dst_location_absolute"],
    "structure_callable_inputs": ["options"],  # the inputs to give to the plugin
    "structure_callable": import_schematic,
    "inputs": ["structure", "options"],  # the inputs to give to the plugin
    "operation": paste,  # the actual function to call when running the plugin
    "wxoptions": show_ui
}
