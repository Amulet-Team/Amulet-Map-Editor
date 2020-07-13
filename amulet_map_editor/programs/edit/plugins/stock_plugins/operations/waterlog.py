import numpy
from typing import TYPE_CHECKING
import wx

from amulet_map_editor.amulet_wx.ui.select_block import BlockDefine
from amulet_map_editor.programs.edit.plugins import OperationUI

if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class Waterlog(wx.Panel, OperationUI):
    def __init__(
        self, parent: wx.Window, canvas: "EditCanvas", world: "World", options_path: str
    ):
        wx.Panel.__init__(self, parent)
        OperationUI.__init__(self, parent, canvas, world, options_path)

        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        options = self._load_options({})

        self._block_define = BlockDefine(
            self,
            world.world_wrapper.translation_manager,
            *(options.get("fill_block_options", []) or [world.world_wrapper.platform]),
            style=wx.BORDER_SIMPLE,
            properties_style=wx.BORDER_SIMPLE
        )
        self._sizer.Add(self._block_define, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self._run_button = wx.Button(self, label="Run Operation")
        self._run_button.Bind(wx.EVT_BUTTON, self._run_operation)
        self._sizer.Add(self._run_button, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self.Layout()

    def _get_fill_block(self):
        return self.world.world_wrapper.translation_manager.get_version(
            self._block_define.platform, self._block_define.version
        ).block.to_universal(
            self._block_define.block,
            force_blockstate=self._block_define.force_blockstate,
        )[
            0
        ]

    def unload(self):
        self._save_options(
            {
                "fill_block": self._get_fill_block(),
                "fill_block_options": self._block_define.options,
            }
        )

    def _run_operation(self, _):
        self.canvas.run_operation(lambda: self._waterlog())

    def _waterlog(self):
        waterlog_block = self._get_fill_block()
        world = self.world
        selection = self.canvas.selection_group
        dimension = self.canvas.dimension
        iter_count = len(list(world.get_chunk_slices(selection, dimension, True)))
        count = 0
        for chunk, slices, _ in world.get_chunk_slices(selection, dimension, True):
            original_blocks = chunk.blocks[slices]
            palette, blocks = numpy.unique(original_blocks, return_inverse=True)
            blocks = blocks.reshape(original_blocks.shape)
            lut = numpy.array(
                [
                    world.palette.get_add_block(
                        world.palette[block_id]
                        + waterlog_block  # get the Block object for that id and add the user specified block
                    )  # register the new block / get the numerical id if it was already registered
                    for block_id in palette
                ]  # add the new id to the palette
            )

            chunk.blocks[slices] = lut[blocks]

            chunk.changed = True
            count += 1
            yield count / iter_count


export = {
    "name": "Waterlog",  # the name of the plugin
    "operation": Waterlog,  # the actual function to call when running the plugin
}
