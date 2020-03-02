from typing import TYPE_CHECKING
import wx

from amulet.api.block import Block
from amulet.operations.replace import replace
from amulet_map_editor.amulet_wx.block_select import BlockDefine
from amulet_map_editor.amulet_wx.wx_util import SimpleDialog, SimplePanel

if TYPE_CHECKING:
    from amulet.api.world import World


def show_ui(parent, world: World, options: dict) -> dict:
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
                Block(
                    original_blocks.namespace,
                    original_blocks.base_name,
                    original_blocks.properties
                )
            )],
            'replacement_blocks': [world.world_wrapper.translation_manager.get_version(
                replacement_blocks.platform,
                replacement_blocks.version
            ).block.to_universal(
                Block(
                    replacement_blocks.namespace,
                    replacement_blocks.base_name,
                    replacement_blocks.properties
                )
            )]
        }
    return options


export = {
    "v": 1,  # a version 1 plugin
    "name": "Replace",  # the name of the plugin
    "operation": replace,  # the actual function to call when running the plugin
    "inputs": ["src_box", "wxoptions"],  # the inputs to give to the plugin
    "wxoptions": show_ui
}
