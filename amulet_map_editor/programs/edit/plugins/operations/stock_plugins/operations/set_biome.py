from typing import TYPE_CHECKING

import wx
import math

from amulet.utils import block_coords_to_chunk_coords
from amulet.api.chunk.biomes import BiomesShape
from amulet_map_editor.api.wx.ui.mc.base.base_identifier_select import EVT_PICK
from amulet_map_editor.api.wx.ui.mc.biome import BiomeDefine
from amulet_map_editor.programs.edit.api.operations import SimpleOperationPanel
from amulet_map_editor.api.wx.ui.simple import ChoiceRaw

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas
    from amulet.api.selection import SelectionGroup
    from amulet.api.data_types import Dimension, OperationReturnType


BoxMode = "box"
ColumnMode = "column"

lang = {
    ColumnMode: "Selected Column",
    BoxMode: "Selected Box",
}


MODES = {
    ColumnMode: "Set the biomes for the vertical column the selection intersects.",
    BoxMode: "Set the biomes for only the blocks in the selection.",
}

Border = wx.TOP | wx.LEFT | wx.RIGHT | wx.EXPAND


class SetBiome(SimpleOperationPanel):
    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)
        self.Freeze()
        options = self._load_options({})

        self._mode = ChoiceRaw(self)
        self._mode.SetItems({mode: lang[mode] for mode in MODES.keys()})
        self._sizer.Add(self._mode, 0, Border, 5)
        self._mode.Bind(wx.EVT_CHOICE, self._on_mode_change)

        self._mode_description = wx.TextCtrl(
            self, style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_BESTWRAP
        )
        self._sizer.Add(self._mode_description, 0, Border, 5)

        self._mode_description.SetLabel(MODES[self._mode.GetCurrentObject()])
        self._mode_description.Fit()

        self._biome_choice = BiomeDefine(
            self,
            world.level_wrapper.translation_manager,
            wx.VERTICAL,
            *(
                options.get("original_block_options", [])
                or [world.level_wrapper.platform]
            ),
            show_pick_biome=True,
        )
        self._biome_choice.Bind(EVT_PICK, self._on_pick_biome_button)
        self._sizer.Add(self._biome_choice, 1, Border, 5)

        self._add_run_button()

        self.Thaw()

    def _on_mode_change(self, evt):
        self._mode_description.SetLabel(MODES[self._mode.GetCurrentObject()])
        self._mode_description.Fit()
        self.Layout()
        evt.Skip()

    def _on_pick_biome_button(self, evt):
        """Set up listening for the biome click"""
        self._show_pointer = True

    def _on_box_click(self):
        if self._show_pointer:
            self._show_pointer = False
            x, y, z = self._pointer.pointer_base

            # TODO: replace with "get_biome(x, y, z)" if it'll be created
            cx, cz = block_coords_to_chunk_coords(
                x, z, sub_chunk_size=self.world.sub_chunk_size
            )
            offset_x, offset_z = x - 16 * cx, z - 16 * cz
            chunk = self.world.get_chunk(cx, cz, self.canvas.dimension)

            if chunk.biomes.dimension == BiomesShape.Shape3D:
                biome = chunk.biomes[offset_x // 4, y // 4, offset_z // 4]
            elif chunk.biomes.dimension == BiomesShape.Shape2D:
                biome = chunk.biomes[offset_x, offset_z]
            else:
                return

            self._biome_choice.universal_biome = chunk.biome_palette[biome]

    def _operation(
        self, world: "BaseLevel", dimension: "Dimension", selection: "SelectionGroup"
    ) -> "OperationReturnType":
        mode = self._mode.GetCurrentObject()

        iter_count = len(list(world.get_coord_box(dimension, selection, False)))
        for count, (chunk, slices, _) in enumerate(
            world.get_chunk_slice_box(dimension, selection, False)
        ):
            new_biome = chunk.biome_palette.get_add_biome(
                self._biome_choice.universal_biome
            )

            if mode == BoxMode:
                if chunk.biomes.dimension == BiomesShape.Shape3D:
                    slices = (
                        slice(slices[0].start // 4, math.ceil(slices[0].stop / 4)),
                        slice(slices[1].start // 4, math.ceil(slices[1].stop / 4)),
                        slice(slices[2].start // 4, math.ceil(slices[2].stop / 4)),
                    )
                elif chunk.biomes.dimension == BiomesShape.Shape2D:
                    slices = (slices[0], slices[2])
                else:
                    continue
            elif mode == ColumnMode:
                if chunk.biomes.dimension == BiomesShape.Shape3D:
                    slices = (
                        slice(slices[0].start // 4, math.ceil(slices[0].stop / 4)),
                        slice(None, None, None),
                        slice(slices[2].start // 4, math.ceil(slices[2].stop / 4)),
                    )
                elif chunk.biomes.dimension == BiomesShape.Shape2D:
                    slices = (slices[0], slices[2])
                else:
                    continue
            else:
                raise ValueError(
                    f"mode {mode} is not a valid mode for the Set Biome operation."
                )

            chunk.biomes[slices] = new_biome

            chunk.changed = True
            yield (count + 1) / iter_count


export = {
    "name": "Set Biome",  # the name of the plugin
    "operation": SetBiome,  # the actual function to call when running the plugin
}
