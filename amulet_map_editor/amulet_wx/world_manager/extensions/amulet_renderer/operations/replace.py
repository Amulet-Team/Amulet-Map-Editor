from typing import TYPE_CHECKING
import wx

from amulet.api.block import Block
from amulet.api.selection import Selection
from amulet.operations.replace import replace
from amulet_map_editor.amulet_wx.block_select import BlockDefine
from amulet_map_editor.amulet_wx.wx_util import SimpleDialog, SimplePanel

if TYPE_CHECKING:
    from amulet.api.world import World


def replace_(
    world: "World",
    selection_box: Selection,
    options: dict
):
    if all(  # verify that the options are actually given
        isinstance(options.get(key), list) and
        all(
            isinstance(b, Block) for b in options.get(key)
        ) for key in ['original_blocks', 'replacement_blocks']
    ):
        replace(world, selection_box, options)
    else:
        wx.MessageBox('Please specify the blocks before running the replace operation')


def show_ui(parent, world: "World", options: dict) -> dict:
    dialog = SimpleDialog(parent, 'Replace')
    horizontal_panel = SimplePanel(dialog.custom_panel, wx.HORIZONTAL)
    dialog.custom_panel.add_object(horizontal_panel)

    original_blocks = BlockDefine(horizontal_panel, world.world_wrapper.translation_manager)
    replacement_blocks = BlockDefine(horizontal_panel, world.world_wrapper.translation_manager)
    horizontal_panel.add_object(original_blocks)
    horizontal_panel.add_object(replacement_blocks)

    if dialog.ShowModal() == wx.ID_OK:
        options = {
            'original_blocks': [world.world_wrapper.translation_manager.get_version(
                original_blocks.platform,
                original_blocks.version
            ).block.to_universal(
                original_blocks.block
            )[0]],
            'replacement_blocks': [world.world_wrapper.translation_manager.get_version(
                replacement_blocks.platform,
                replacement_blocks.version
            ).block.to_universal(
                replacement_blocks.block
            )[0]]
        }
    return options


export = {
    "v": 1,  # a version 1 plugin
    "name": "Replace",  # the name of the plugin
    "operation": replace_,  # the actual function to call when running the plugin
    "inputs": ["src_box", "wxoptions"],  # the inputs to give to the plugin
    "wxoptions": show_ui
}
