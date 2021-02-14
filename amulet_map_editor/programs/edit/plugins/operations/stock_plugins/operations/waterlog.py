import numpy
from typing import TYPE_CHECKING, Tuple
import wx

from amulet_map_editor.api.wx.ui.base_select import EVT_PICK
from amulet_map_editor.api.wx.ui.simple import SimpleDialog
from amulet_map_editor.api.wx.ui.block_select import BlockDefine
from amulet_map_editor.programs.edit.api.operations import OperationUI
from amulet_map_editor.programs.edit.api.events import EVT_BOX_CLICK
from amulet_map_editor.api import image

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

MODES = {
    "Overlay": "Overlay the block on the existing. If the first block is air it replaces the first block otherwise it sets the second block.",
    "Underlay": "Underlay the block on the existing. If the first block is not air it moves the first block to the second block. It then replaces the first block.",
    "Normal Fill": "Replace all selected blocks with the chosen block.",
    "Game Fill": "Fill like in game. Moves water blocks to the second block and replaces the first block. Useful for setting blocks in existing water.",
    "Set First": "Set the first block leaving the second block as it was. If you want to change the first block without modifying the second block.",
    "Set Second": 'Set the second block leaving the first block as it was. This can cause issues if the first block is air. You might prefer "Overlay"',
}


class Waterlog(wx.Panel, OperationUI):
    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        wx.Panel.__init__(self, parent)
        OperationUI.__init__(self, parent, canvas, world, options_path)
        self.Freeze()

        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        options = self._load_options({})

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._sizer.Add(top_sizer, 0, wx.EXPAND | wx.ALL, 5)

        help_button = wx.BitmapButton(
            self, bitmap=image.icon.tablericons.help.bitmap(22, 22)
        )
        top_sizer.Add(help_button)

        def on_button(evt):
            dialog = SimpleDialog(self, "Extra block help.")
            text = wx.TextCtrl(
                dialog,
                value="Blocks in the newer versions of Minecraft support having two blocks in the same location.\n"
                "This is how the game is able to have water and blocks like fences at the same location.\n"
                "In the example of waterlogged fences the fence is the first block and the water is the second. Unless it is water the second block is usually just visual.\n"
                "In Java currently the second block is strictly water but in Bedrock there is no limit on what the second block can be.\n"
                "It is not possible to set non-water second blocks in the game but this operation enables the use of that feature.\n"
                "There are a number of different modes which can be selected at the top. A description of how it works will appear.",
                style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_BESTWRAP,
            )
            dialog.sizer.Add(text, 1, wx.EXPAND)
            dialog.ShowModal()
            evt.Skip()

        help_button.Bind(wx.EVT_BUTTON, on_button)

        self._mode = wx.Choice(self, choices=list(MODES.keys()))
        self._mode.SetSelection(0)
        top_sizer.Add(self._mode, 1, wx.EXPAND | wx.LEFT, 5)
        self._mode.Bind(wx.EVT_CHOICE, self._on_mode_change)

        self._mode_description = wx.TextCtrl(
            self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_BESTWRAP
        )
        self._sizer.Add(self._mode_description, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)

        self._mode_description.SetLabel(
            MODES[self._mode.GetString(self._mode.GetSelection())]
        )
        self._mode_description.Fit()

        self._block_define = BlockDefine(
            self,
            world.level_wrapper.translation_manager,
            wx.VERTICAL,
            *(options.get("fill_block_options", []) or [world.level_wrapper.platform]),
            show_pick_block=True
        )
        self._block_click_registered = False
        self._block_define.Bind(EVT_PICK, self._on_pick_block_button)
        self._sizer.Add(self._block_define, 1, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self._run_button = wx.Button(self, label="Run Operation")
        self._run_button.Bind(wx.EVT_BUTTON, self._run_operation)
        self._sizer.Add(self._run_button, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self.Layout()
        self.Thaw()

    @property
    def wx_add_options(self) -> Tuple[int, ...]:
        return (1,)

    def _on_mode_change(self, evt):
        self._mode_description.SetLabel(
            MODES[self._mode.GetString(self._mode.GetSelection())]
        )
        self._mode_description.Fit()
        self.Layout()
        evt.Skip()

    def _on_pick_block_button(self, evt):
        """Set up listening for the block click"""
        if not self._block_click_registered:
            self.canvas.Bind(EVT_BOX_CLICK, self._on_pick_block)
            self._block_click_registered = True
        evt.Skip()

    def _on_pick_block(self, evt):
        self.canvas.Unbind(EVT_BOX_CLICK, handler=self._on_pick_block)
        self._block_click_registered = False
        x, y, z = self.canvas.cursor_location
        self._block_define.universal_block = (
            self.world.get_block(x, y, z, self.canvas.dimension),
            None,
        )

    def _get_fill_block(self):
        return self._block_define.universal_block[0]

    def unload(self):
        self._save_options(
            {
                "fill_block": self._get_fill_block(),
                "fill_block_options": (
                    self._block_define.platform,
                    self._block_define.version_number,
                    self._block_define.force_blockstate,
                    self._block_define.namespace,
                    self._block_define.block_name,
                    self._block_define.properties,
                ),
            }
        )

    def _run_operation(self, _):
        self.canvas.run_operation(lambda: self._waterlog())

    def _waterlog(self):
        mode = self._mode.GetString(self._mode.GetSelection())
        waterlog_block = self._get_fill_block().base_block
        world = self.world
        selection = self.canvas.selection.selection_group
        dimension = self.canvas.dimension
        iter_count = len(list(world.get_chunk_slice_box(dimension, selection, True)))
        count = 0
        for chunk, slices, _ in world.get_chunk_slice_box(dimension, selection, True):
            original_blocks = chunk.blocks[slices]
            palette, blocks = numpy.unique(original_blocks, return_inverse=True)
            blocks = blocks.reshape(original_blocks.shape)
            if mode == "Overlay":
                lut = numpy.array(
                    [
                        world.block_palette.get_add_block(
                            waterlog_block
                            if world.block_palette[block_id].namespaced_name
                            == "universal_minecraft:air"
                            else world.block_palette[block_id].base_block
                            + waterlog_block  # get the Block object for that id and add the user specified block
                        )  # register the new block / get the numerical id if it was already registered
                        for block_id in palette
                    ]  # add the new id to the palette
                )
            elif mode == "Underlay":
                lut = numpy.array(
                    [
                        world.block_palette.get_add_block(
                            waterlog_block
                            if world.block_palette[block_id].namespaced_name
                            == "universal_minecraft:air"
                            else waterlog_block
                            + world.block_palette[  # get the Block object for that id and add the user specified block
                                block_id
                            ].base_block
                        )  # register the new block / get the numerical id if it was already registered
                        for block_id in palette
                    ]  # add the new id to the palette
                )
            elif mode == "Normal Fill":
                lut = numpy.array(
                    [
                        world.block_palette.get_add_block(
                            waterlog_block
                        )  # register the new block / get the numerical id if it was already registered
                    ]
                    * len(palette)  # add the new id to the palette
                )
            elif mode == "Game Fill":
                lut = numpy.array(
                    [
                        world.block_palette.get_add_block(
                            waterlog_block + world.block_palette[block_id].base_block
                            if world.block_palette[block_id].namespaced_name
                            == "universal_minecraft:water"
                            else waterlog_block
                        )  # register the new block / get the numerical id if it was already registered
                        for block_id in palette
                    ]  # add the new id to the palette
                )
            elif mode == "Set First":
                lut = numpy.array(
                    [
                        world.block_palette.get_add_block(
                            waterlog_block
                            + world.block_palette[block_id].extra_blocks[0]
                            if world.block_palette[block_id].extra_blocks
                            else waterlog_block
                        )  # register the new block / get the numerical id if it was already registered
                        for block_id in palette
                    ]  # add the new id to the palette
                )
            elif mode == "Set Second":
                lut = numpy.array(
                    [
                        world.block_palette.get_add_block(
                            world.block_palette[block_id].base_block + waterlog_block
                        )  # register the new block / get the numerical id if it was already registered
                        for block_id in palette
                    ]  # add the new id to the palette
                )
            else:
                raise Exception("hello")

            chunk.blocks[slices] = lut[blocks]

            chunk.changed = True
            count += 1
            yield count / iter_count


export = {
    "name": "Waterlog",  # the name of the plugin
    "operation": Waterlog,  # the actual function to call when running the plugin
}
