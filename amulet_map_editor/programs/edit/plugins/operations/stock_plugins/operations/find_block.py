from __future__ import annotations

from functools import reduce
from typing import TYPE_CHECKING

import numpy
import wx

from operator import add

from amulet_map_editor.api.wx.ui.block_select import BlockDefine
from amulet_map_editor.api.wx.ui.simple import SimpleDialog
from amulet_map_editor.programs.edit.api.operations import SimpleOperationPanel

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel
    from amulet.api.selection import SelectionGroup
    from amulet.api.data_types import Dimension


class ResultDialog(SimpleDialog):
    def __init__(self, parent, block_location_info):
        super(ResultDialog, self).__init__(parent, "Block Locations")

        self._block_location_info = block_location_info
        self.Freeze()

        self.sizer.Add(
            wx.StaticText(
                self, label=f"Block finding results:", style=wx.ALIGN_CENTRE_HORIZONTAL
            ),
            0,
            wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL,
            5,
        )
        self._tree = tree = wx.TreeCtrl(
            self, style=wx.TR_DEFAULT_STYLE | wx.TR_HIDE_ROOT
        )
        self._root = tree.AddRoot("__root__")

        self.sizer.Add(tree, 1, wx.ALL | wx.EXPAND, 5)

        self.Layout()
        self.Thaw()

    def build_results(self):
        count = 0
        iter_count = reduce(add, map(len, self._block_location_info.values()))

        for block in self._block_location_info:
            block_root = self._tree.AppendItem(
                self._root,
                f"{block} - {len(self._block_location_info[block])} locations",
            )

            for coordinates in self._block_location_info[block]:
                self._tree.AppendItem(block_root, str(coordinates))
                count += 1
                yield count / iter_count, "Building results dialog..."


class FindBlock(SimpleOperationPanel):
    def __init__(self, parent, canvas, world, options_path):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)
        self.Freeze()

        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        options = self._load_options({})

        self._block_define = BlockDefine(
            self,
            world.translation_manager,
            wx.VERTICAL,
            *(
                options.get("target_block_options", [])
                or [world.level_wrapper.platform]
            ),
            show_pick_block=True,
        )
        self._findSubTypes = wx.CheckBox(self, label="Find All Block Substates")
        self._findSubTypes.SetValue(options.get("find_substates", False))

        self._sizer.Add(self._block_define, 1, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)
        self._sizer.Add(self._findSubTypes, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self._add_run_button()

        self.Thaw()

    def _get_target_block(self):
        return self._block_define.universal_block[0]

    def _get_find_all_substates(self):
        return self._findSubTypes.GetValue()

    def disable(self):
        self._save_options(
            {
                "target_block": self._get_target_block(),
                "target_block_options": (
                    self._block_define.platform,
                    self._block_define.version_number,
                    self._block_define.force_blockstate,
                    self._block_define.namespace,
                    self._block_define.block_name,
                    self._block_define.properties,
                ),
                "find_substates": self._get_find_all_substates(),
            }
        )

    def _find_single_blockstate(self, world, dimension, selection):
        target = world.block_palette.get_add_block(self._get_target_block())

        iter_count = len(list(world.get_chunk_slice_box(dimension, selection, False)))
        count = 0

        block_locations = []

        for chunk, slices, _ in world.get_chunk_slice_box(dimension, selection, False):
            block_selection = chunk.blocks[slices]
            x_values, y_values, z_values = numpy.where(block_selection == target)
            for x, y, z in zip(x_values, y_values, z_values):
                block_locations.append(
                    (
                        block_selection.start_x + x,
                        block_selection.start_y + y,
                        block_selection.start_z + z,
                    )
                )
            count += 1
            yield count / iter_count, "Searching blocks..."

        result = {
            world.translation_manager.get_version(
                world.level_wrapper.platform, world.level_wrapper.version
            )
            .block.from_universal(world.block_palette[target])[0]
            .full_blockstate: block_locations
        }

        dialog = ResultDialog(self.parent, result)
        yield from dialog.build_results()
        dialog.Show()

    def _find_multiple_blockstates(
        self, world: "BaseLevel", dimension: "Dimension", selection: "SelectionGroup"
    ):
        blocks_to_find = set()
        block_translator = world.translation_manager.get_version(
            world.level_wrapper.platform, world.level_wrapper.version
        ).block
        versioned_block = block_translator.from_universal(self._get_target_block())[0]
        versioned_block_name = versioned_block.namespaced_name

        blocks_to_find.add(
            (
                world.block_palette.get_add_block(self._get_target_block()),
                versioned_block,
            )
        )

        # Technically, this is the correct way, since if a Block's substate doesn't exist in the
        # world, then it wouldn't be present in the block_palette and thus would be skipped
        # but to users this may not seem straightforward since it would look like the operation
        # is missing blockstates when the results window is shown
        blocks_to_find = blocks_to_find.union(
            filter(
                lambda b: b[1].namespaced_name == versioned_block_name,
                map(
                    lambda b: (b[0], block_translator.from_universal(b[1])[0]),
                    world.block_palette.items(),
                ),
            ),
        )

        chunk_slices = list(world.get_chunk_slice_box(dimension, selection, False))

        iter_count = len(chunk_slices)
        iter_count *= len(blocks_to_find)
        count = 0

        results = {block.full_blockstate: [] for _, block in blocks_to_find}

        for internal_id, block in blocks_to_find:
            extend_func = results[block.full_blockstate].extend
            for chunk, slices, _ in chunk_slices:
                block_selection = chunk.blocks[slices]
                x_values, y_values, z_values = numpy.where(
                    block_selection == internal_id
                )

                extend_func(
                    map(
                        lambda x, y, z: (
                            block_selection.start_x + x,
                            block_selection.start_y + y,
                            block_selection.start_z + z,
                        ),
                        x_values,
                        y_values,
                        z_values,
                    )
                )
                count += 1
                yield count / iter_count, "Searching blocks..."

        dialog = ResultDialog(self.parent, results)
        yield from dialog.build_results()
        dialog.Show()

    def _operation(
        self, world: "BaseLevel", dimension: "Dimension", selection: "SelectionGroup"
    ):
        if self._get_find_all_substates():
            yield from self._find_multiple_blockstates(world, dimension, selection)
        else:
            yield from self._find_single_blockstate(world, dimension, selection)


export = {"name": "Find Block", "operation": FindBlock}
