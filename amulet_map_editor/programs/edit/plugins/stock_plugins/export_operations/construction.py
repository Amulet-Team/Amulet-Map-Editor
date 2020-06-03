from typing import TYPE_CHECKING
import wx

from amulet_map_editor.amulet_wx.ui.select_block import VersionSelect
from amulet_map_editor.amulet_wx.ui.simple import SimpleDialog
from amulet.api.selection import SelectionGroup
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import Dimension
from amulet.structure_interface.construction import ConstructionFormatWrapper

if TYPE_CHECKING:
    from amulet.api.world import World


def export_construction(
    world: "World",
    dimension: Dimension,
    selection: SelectionGroup,
    options: dict
):
    path, platform, version = options.get('path', None), options.get('platform', None), options.get('version', None)
    if isinstance(path, str) and path.endswith('.construction') and platform and version:
        wrapper = ConstructionFormatWrapper(path, 'w')
        wrapper.platform = platform
        wrapper.version = version
        wrapper.selection = selection
        wrapper.translation_manager = world.translation_manager
        wrapper.open()
        for cx, cz in selection.chunk_locations():
            try:
                chunk = world.get_chunk(cx, cz, dimension)
                wrapper.commit_chunk(chunk, world.palette)
            except ChunkLoadError:
                continue

        wrapper.close()
    else:
        raise Exception('Please specify a save location and version in the options before running.')


def show_ui(parent, world: "World", options: dict) -> dict:
    dialog = SimpleDialog(parent, 'Export Construction')
    file_picker = wx.FilePickerCtrl(
        dialog,
        path=options.get('path', ''),
        wildcard="Construction file (*.construction)|*.construction",
        style=wx.FLP_USE_TEXTCTRL | wx.FLP_SAVE | wx.FLP_OVERWRITE_PROMPT
    )
    dialog.sizer.Add(file_picker, 0, wx.ALL, 5)
    version_define = VersionSelect(
        dialog,
        world.translation_manager,
        options.get("platform", None) or world.world_wrapper.platform,
        allow_universal=False
    )
    dialog.sizer.Add(version_define, 0)
    dialog.Fit()

    if dialog.ShowModal() == wx.ID_OK:
        options = {
            "path": file_picker.GetPath(),
            "platform": version_define.platform,
            "version": version_define.version
        }
    return options


export = {
    "v": 1,  # a version 1 plugin
    "name": "Export Construction",  # the name of the plugin
    "features": ["src_selection", "wxoptions"],
    "inputs": ["src_selection", "options"],  # the inputs to give to the plugin
    "operation": export_construction,  # the actual function to call when running the plugin
    "wxoptions": show_ui
}
