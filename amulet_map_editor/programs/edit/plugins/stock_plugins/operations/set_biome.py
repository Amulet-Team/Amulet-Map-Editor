from typing import TYPE_CHECKING

import numpy
import wx

from amulet import block_coords_to_chunk_coords
from amulet_map_editor.api.wx.ui.base_select import EVT_PICK
from amulet_map_editor.api.wx.ui.biome_select import BiomeDefine
from amulet_map_editor.programs.edit.canvas.events import EVT_BOX_CLICK
from amulet_map_editor.programs.edit.plugins.api.simple_operation_panel import (
    SimpleOperationPanel,
)

if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas
    from amulet import SelectionGroup
    from amulet.api.data_types import Dimension, OperationReturnType


MODES = {
    "Selection Only": "Set the biomes for only the blocks in the selection and not the chunks.",
    "Whole Chunks": "Set the biomes for the full chunks for all the chunks in the selection.",
}


class SetBiome(SimpleOperationPanel):
    def __init__(
        self, parent: wx.Window, canvas: "EditCanvas", world: "World", options_path: str
    ):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)
        self.Freeze()
        options = self._load_options({})

        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        self._sizer.Add(top_sizer, 0, wx.EXPAND | wx.ALL, 5)

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

        self._biome_choice = BiomeDefine(
            self,
            world.world_wrapper.translation_manager,
            wx.VERTICAL,
            *(
                options.get("original_block_options", [])
                or [world.world_wrapper.platform]
            ),
            wildcard_properties=True,
            show_pick_biome=True,
        )
        self._biome_click_registered = False
        self._biome_choice.Bind(EVT_PICK, self._on_pick_biome_button)
        self._sizer.Add(self._biome_choice, 1, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self._add_run_button()

        self.Thaw()

    def _on_mode_change(self, evt):
        self._mode_description.SetLabel(
            MODES[self._mode.GetString(self._mode.GetSelection())]
        )
        self._mode_description.Fit()
        self.Layout()
        evt.Skip()

    def unload(self):
        pass

    def _on_pick_biome_button(self, evt):
        """Set up listening for the biome click"""
        if not self._biome_click_registered:
            self.canvas.Bind(EVT_BOX_CLICK, self._on_pick_biome)
            self._biome_click_registered = True
        evt.Skip()

    def _on_pick_biome(self, evt):
        self.canvas.Unbind(EVT_BOX_CLICK, handler=self._on_pick_biome)
        self._biome_click_registered = False
        x, y, z = self.canvas.cursor_location

        # TODO: replace with "get_biome(x, y, z)" if it'll be created
        cx, cz = block_coords_to_chunk_coords(x, z, chunk_size=self.world.chunk_size[0])
        offset_x, offset_z = x - 16 * cx, z - 16 * cz
        chunk = self.world.get_chunk(cx, cz, self.canvas.dimension)

        if chunk.biomes.dimension == 3:
            biome = chunk.biomes[offset_x//4, y//4, offset_z//4]
        elif chunk.biomes.dimension == 2:
            biome = chunk.biomes[offset_x, offset_z]
        else:
            return

        self._biome_choice.universal_biome = chunk.biome_palette[biome]

    def _operation(
        self, world: "World", dimension: "Dimension", selection: "SelectionGroup"
    ) -> "OperationReturnType":
        mode = self._mode.GetString(self._mode.GetSelection())
        world = self.world
        selection = self.canvas.selection_group
        dimension = self.canvas.dimension

        iter_count = len(list(world.get_chunk_slices(selection, dimension, True)))
        count = 0
        for chunk, slices, _ in world.get_chunk_slices(selection, dimension, True):
            original_blocks = chunk.blocks[slices]
            palette, blocks = numpy.unique(original_blocks, return_inverse=True)
            blocks = blocks.reshape(original_blocks.shape)
            if mode == "Selection Only":
                pass
            elif mode == "Whole Chunks":
                pass
            else:
                raise ValueError(
                    f"mode {mode} doesn't exist for the Set Biome operation."
                )

            chunk.changed = True
            count += 1
            yield count / iter_count


export = {
    "name": "Set Biome",  # the name of the plugin
    "operation": SetBiome,  # the actual function to call when running the plugin
}
