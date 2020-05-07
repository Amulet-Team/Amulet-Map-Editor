from typing import TYPE_CHECKING
import wx
import numpy

from amulet.api.selection import SelectionGroup
from amulet.api.block import Block
from amulet.api.data_types import Dimension
from amulet_map_editor.amulet_wx.block_select import BlockDefine
from amulet_map_editor.amulet_wx.simple import SimpleDialog

if TYPE_CHECKING:
    from amulet.api.world import World


def waterlog(
    world: "World",
    dimension: Dimension,
    selection: SelectionGroup,
    options: dict
):
    waterlog_block = options.get("fill_block", None)
    waterlog_block: Block
    if isinstance(waterlog_block, Block):
        iter_count = len(list(world.get_chunk_slices(selection, dimension, True)))
        count = 0
        for chunk, slices, _ in world.get_chunk_slices(selection, dimension, True):
            original_blocks = chunk.blocks[slices]
            palette, blocks = numpy.unique(original_blocks, return_inverse=True)
            blocks = blocks.reshape(original_blocks.shape)
            lut = numpy.array(
                [
                    world.palette.get_add_block(
                        world.palette[block_id] + waterlog_block  # get the Block object for that id and add the user specified block
                    )  # register the new block / get the numerical id if it was already registered
                    for block_id in palette
                ]  # add the new id to the palette
            )

            chunk.blocks[slices] = lut[blocks]

            chunk.changed = True
            count += 1
            yield 100 * count / iter_count
    else:
        raise Exception('Please specify a block before running the waterlog operation')


def show_ui(parent, world: "World", options: dict) -> dict:
    dialog = SimpleDialog(parent, 'Waterlog')
    block_define = BlockDefine(
        dialog.custom_panel,
        world.world_wrapper.translation_manager,
        *(options.get("fill_block_options", []) or [world.world_wrapper.platform])
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
    "name": "Waterlog",  # the name of the plugin
    "features": ["src_selection", "wxoptions"],
    "inputs": ["src_selection", "options"],  # the inputs to give to the plugin
    "operation": waterlog,  # the actual function to call when running the plugin
    "wxoptions": show_ui
}
