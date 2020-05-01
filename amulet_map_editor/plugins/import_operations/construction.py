from typing import TYPE_CHECKING
import wx

import os
from amulet_map_editor.amulet_wx.simple import SimpleDialog
from amulet.api.block import BlockManager
from amulet.api.data_types import Dimension
from amulet.api.structure import Structure
from amulet.structure_interface.construction import ConstructionFormatWrapper
from amulet.operations.paste import paste

if TYPE_CHECKING:
    from amulet.api.world import World


def show_ui(parent, world: "World", options: dict) -> dict:
    dialog = SimpleDialog(parent, 'Import Construction')
    file_picker = wx.FilePickerCtrl(
        dialog.custom_panel,
        path=options.get('path', ''),
        wildcard="Construction file (*.construction)|*.construction",
        style=wx.FLP_USE_TEXTCTRL | wx.FLP_OPEN
    )
    dialog.custom_panel.add_object(file_picker, 0)
    dialog.Fit()

    if dialog.ShowModal() == wx.ID_OK:
        options = {
            "path": file_picker.GetPath()
        }
    return options


def import_construction(
    world: "World",
    dimension: Dimension,
    options: dict
) -> Structure:
    path = options.get('path', None)
    if isinstance(path, str) and path.endswith('.construction') and os.path.isfile(path):
        wrapper = ConstructionFormatWrapper(path, 'r')
        wrapper.translation_manager = world.translation_manager
        wrapper.open()
        selection = wrapper.selection

        global_palette = BlockManager()
        chunks = {(cx, cz): wrapper.load_chunk(cx, cz, global_palette) for (cx, cz) in wrapper.all_chunk_coords()}

        wrapper.close()
        return Structure(
            chunks,
            global_palette,
            selection
        )
    else:
        raise Exception('Please specify a construction file in the options before running.')


export = {
    "v": 1,  # a version 1 plugin
    "name": "Import Construction",  # the name of the plugin
    "features": ["src_selection", "wxoptions", "dst_location_absolute"],
    "structure_callable_inputs": ["options"],  # the inputs to give to the plugin
    "structure_callable": import_construction,
    "inputs": ["structure", "options"],  # the inputs to give to the plugin
    "operation": paste,  # the actual function to call when running the plugin
    "wxoptions": show_ui
}
