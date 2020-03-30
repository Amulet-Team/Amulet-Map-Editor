from typing import TYPE_CHECKING
import wx

from amulet.operations.fill import fill
from amulet.api.selection import Selection
from amulet.api.block import Block
from amulet_map_editor.amulet_wx.block_select import BlockDefine
from amulet_map_editor.amulet_wx.simple import SimpleDialog

if TYPE_CHECKING:
    from amulet.api.world import World


def fill_(
    world: "World",
    dimension: int,
    selection_box: Selection,
    options: dict
):
    if isinstance(options.get('fill_block'), Block):
        fill(world, dimension, selection_box, options)
    else:
        wx.MessageBox('Please specify a block before running the fill operation')


def show_ui(parent, world: "World", options: dict) -> dict:
    dialog = SimpleDialog(parent, 'Fill')
    block_define = BlockDefine(
        dialog.custom_panel,
        world.world_wrapper.translation_manager,
        *options.get("fill_block_options", [])
    )
    dialog.custom_panel.add_object(block_define)
    dialog.Fit()
    if dialog.ShowModal() == wx.ID_OK:
        options = {
            "fill_block": world.world_wrapper.translation_manager.get_version(
                block_define.platform,
                block_define.version
            ).block.to_universal(
                block_define.block,
                force_blockstate=block_define.force_blockstate
            )[0],
            "fill_block_options": block_define.options
        }
    return options


export = {
    "v": 1,  # a version 1 plugin
    "name": "Fill",  # the name of the plugin
    "features": ["src_selection", "wxoptions"],
    "inputs": ["src_selection", "options"],  # the inputs to give to the plugin
    "operation": fill_,  # the actual function to call when running the plugin
    "wxoptions": show_ui
}
