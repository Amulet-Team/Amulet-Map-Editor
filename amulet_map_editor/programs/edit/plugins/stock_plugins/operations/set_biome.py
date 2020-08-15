from typing import TYPE_CHECKING

import numpy
import wx

from amulet_map_editor.programs.edit.plugins.api.simple_operation_panel import (
    SimpleOperationPanel,
)

if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


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

        self._run_button = wx.Button(self, label="Run Operation")
        self._run_button.Bind(wx.EVT_BUTTON, self._run_operation)
        self._sizer.Add(self._run_button, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self.Layout()
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

    def _run_operation(self, _):
        self.canvas.run_operation(lambda: self._set_biome())

    def _set_biome(self):
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
                raise ValueError(f"mode {mode} doesn't exist for the Set Biome operation.")

            chunk.changed = True
            count += 1
            yield count / iter_count



export = {
    "name": "Set Biome",  # the name of the plugin
    "operation": SetBiome,  # the actual function to call when running the plugin
}
