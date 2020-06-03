from typing import TYPE_CHECKING
import wx

from amulet_map_editor.amulet_wx.select_block import PlatformSelect
from amulet_map_editor.amulet_wx.simple import SimpleDialog
from amulet.api.selection import SelectionGroup
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import Dimension
from amulet.structure_interface.schematic import SchematicFormatWrapper

if TYPE_CHECKING:
    from amulet.api.world import World


def export_schematic(
    world: "World",
    dimension: Dimension,
    selection: SelectionGroup,
    options: dict
):
    assert len(selection.selection_boxes) == 1, "The schematic format only supports a single selection box."
    path, platform = options.get('path', None), options.get('platform', None)
    if isinstance(path, str) and path.endswith('.schematic') and platform:
        wrapper = SchematicFormatWrapper(path, 'w')
        wrapper.platform = platform
        wrapper.selection = selection
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
    dialog = SimpleDialog(parent, 'Export Schematic (legacy)')
    file_picker = wx.FilePickerCtrl(
        dialog,
        path=options.get('path', ''),
        wildcard="Schematic file (*.schematic)|*.schematic",
        style=wx.FLP_USE_TEXTCTRL | wx.FLP_SAVE | wx.FLP_OVERWRITE_PROMPT
    )
    dialog.sizer.Add(file_picker, 0, wx.ALL | wx.CENTER, 5)
    platform_define = PlatformSelect(
        dialog,
        world.translation_manager,
        options.get("platform", None) or world.world_wrapper.platform,
        allow_universal=False
    )
    dialog.sizer.Add(platform_define, 0, wx.CENTER, 5)
    dialog.sizer.Add(
        wx.StaticText(
            dialog,
            label="""The Schematic format is a
legacy format that can only
save data in the numerical
format. Anything that was
added to the game in version
1.13 or after will not be
saved in the schematic file.

We suggest using the Construction
file format instead.""",
            style=wx.ALIGN_CENTRE_HORIZONTAL
        ), 0, wx.ALL | wx.CENTER, 5
    )
    dialog.Fit()

    if dialog.ShowModal() == wx.ID_OK:
        options = {
            "path": file_picker.GetPath(),
            "platform": platform_define.platform
        }
    return options


export = {
    "v": 1,  # a version 1 plugin
    "name": "Export Schematic (legacy)",  # the name of the plugin
    "features": ["src_selection", "wxoptions"],
    "inputs": ["src_selection", "options"],  # the inputs to give to the plugin
    "operation": export_schematic,  # the actual function to call when running the plugin
    "wxoptions": show_ui
}
