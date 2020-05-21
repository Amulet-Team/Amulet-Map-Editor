from typing import TYPE_CHECKING
import wx

from amulet_map_editor.amulet_wx.block_select import VersionSelect
from amulet_map_editor.amulet_wx.simple import SimpleDialog
from amulet.api.selection import SelectionGroup
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import Dimension
from amulet.structure_interface.mcstructure import MCStructureFormatWrapper

if TYPE_CHECKING:
    from amulet.api.world import World


def export_mcstructure(
    world: "World",
    dimension: Dimension,
    selection: SelectionGroup,
    options: dict
):
    assert len(selection.selection_boxes) == 1, "The mcstructure format only supports a single selection box."
    path, version = options.get('path', None), options.get('version', None)
    if isinstance(path, str) and path.endswith('.mcstructure') and version:
        wrapper = MCStructureFormatWrapper(path, 'w')
        wrapper.selection = selection
        wrapper.version = version
        wrapper.translation_manager = world.translation_manager
        wrapper.open()
        for cx, cz in wrapper.selection.chunk_locations():
            try:
                chunk = world.get_chunk(cx, cz, dimension)
                wrapper.commit_chunk(chunk, world.palette)
            except ChunkLoadError:
                continue

        wrapper.close()
    else:
        raise Exception('Please specify a save location and platform in the options before running.')


def show_ui(parent, world: "World", options: dict) -> dict:
    dialog = SimpleDialog(parent, 'Export Bedrock .mcstructure')
    file_picker = wx.FilePickerCtrl(
        dialog,
        path=options.get('path', ''),
        wildcard="mcstructure file (*.mcstructure)|*.mcstructure",
        style=wx.FLP_USE_TEXTCTRL | wx.FLP_SAVE | wx.FLP_OVERWRITE_PROMPT
    )
    dialog.sizer.Add(file_picker, 0, wx.ALL, 5)
    version_define = VersionSelect(
        dialog,
        world.translation_manager,
        options.get("platform", None) or world.world_wrapper.platform,
        allowed_platforms=("bedrock", ),
        allow_numerical=False
    )
    dialog.sizer.Add(version_define, 0)
    dialog.Fit()

    if dialog.ShowModal() == wx.ID_OK:
        options = {
            "path": file_picker.GetPath(),
            "version": version_define.version
        }
    return options


export = {
    "v": 1,  # a version 1 plugin
    "name": "Export Bedrock .mcstructure",  # the name of the plugin
    "features": ["src_selection", "wxoptions"],
    "inputs": ["src_selection", "options"],  # the inputs to give to the plugin
    "operation": export_mcstructure,  # the actual function to call when running the plugin
    "wxoptions": show_ui
}
