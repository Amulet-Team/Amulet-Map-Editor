from typing import TYPE_CHECKING, Tuple
import wx
import numpy

from amulet.api.block import Block

from amulet_map_editor.api.wx.ui.mc.base.base_identifier_select import EVT_PICK
from amulet_map_editor.api.wx.ui.mc.block import BlockDefine
from amulet_map_editor.api.wx.ui.simple import SimpleScrollablePanel
from amulet_map_editor.programs.edit.api.operations import DefaultOperationUI

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class Replace(SimpleScrollablePanel, DefaultOperationUI):
    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        SimpleScrollablePanel.__init__(self, parent)
        DefaultOperationUI.__init__(self, parent, canvas, world, options_path)
        self.Freeze()
        options = self._load_options({})

        self._original_block = BlockDefine.from_data(
            self,
            world.level_wrapper.translation_manager,
            orientation=wx.VERTICAL,
            *(
                options.get("original_block_options", [])
                or [world.level_wrapper.platform]
            ),
            wildcard_properties=True,
            show_pick_block=True
        )
        self._sizer.Add(self._original_block, 1, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)
        self._original_block.Bind(EVT_PICK, lambda evt: self._on_pick_block_button(1))
        self._replacement_block = BlockDefine.from_data(
            self,
            world.level_wrapper.translation_manager,
            orientation=wx.VERTICAL,
            *(
                options.get("replacement_block_options", [])
                or [world.level_wrapper.platform]
            ),
            show_pick_block=True
        )
        self._sizer.Add(
            self._replacement_block, 1, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5
        )
        self._replacement_block.Bind(
            EVT_PICK, lambda evt: self._on_pick_block_button(2)
        )

        self._run_button = wx.Button(self, label="Run Operation")
        self._run_button.Bind(wx.EVT_BUTTON, self._run_operation)
        self._sizer.Add(self._run_button, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self.Layout()
        self.Thaw()

    @property
    def wx_add_options(self) -> Tuple[int, ...]:
        return (1,)

    def _on_pick_block_button(self, code):
        """Set up listening for the block click"""
        self._show_pointer = code

    def _on_box_click(self):
        if self._show_pointer:
            x, y, z = self._pointer.pointer_base
            if self._show_pointer == 1:
                self._original_block.universal_block = (
                    self.world.get_block(x, y, z, self.canvas.dimension),
                    None,
                )
            elif self._show_pointer == 2:
                self._replacement_block.universal_block = (
                    self.world.get_block(x, y, z, self.canvas.dimension),
                    None,
                )
            self._show_pointer = False

    def _get_replacement_block(self) -> Block:
        return self._replacement_block.universal_block[0]

    def disable(self):
        self._save_options(
            {
                "original_block_options": (
                    self._original_block.platform,
                    self._original_block.version_number,
                    self._original_block.force_blockstate,
                    self._original_block.namespace,
                    self._original_block.block_name,
                    self._original_block.str_properties,
                ),
                "replacement_block": self._get_replacement_block(),
                "replacement_block_options": (
                    self._replacement_block.platform,
                    self._replacement_block.version_number,
                    self._replacement_block.force_blockstate,
                    self._replacement_block.namespace,
                    self._replacement_block.block_name,
                    self._replacement_block.str_properties,
                ),
            }
        )

    def _run_operation(self, _):
        self.canvas.run_operation(lambda: self._replace())

    def _replace(self):
        world = self.world
        selection = self.canvas.selection.selection_group
        dimension = self.canvas.dimension

        (
            original_platform,
            original_version,
            original_blockstate,
            original_namespace,
            original_base_name,
            original_properties,
        ) = (
            self._original_block.platform,
            self._original_block.version_number,
            self._original_block.force_blockstate,
            self._original_block.namespace,
            self._original_block.block_name,
            self._original_block.str_properties,
        )
        replacement_block = self._get_replacement_block()

        replacement_block_id = world.block_palette.get_add_block(replacement_block)

        original_block_matches = []
        universal_block_count = 0

        iter_count = len(list(world.get_coord_box(dimension, selection)))
        count = 0

        for chunk, slices, _ in world.get_chunk_slice_box(dimension, selection):
            if universal_block_count < len(world.block_palette):
                for universal_block_id in range(
                    universal_block_count, len(world.block_palette)
                ):
                    version_block = world.translation_manager.get_version(
                        original_platform, original_version
                    ).block.from_universal(
                        world.block_palette[universal_block_id],
                        force_blockstate=original_blockstate,
                    )[
                        0
                    ]
                    if (
                        version_block.namespace == original_namespace
                        and version_block.base_name == original_base_name
                        and all(
                            original_properties.get(prop) in ["*", val.to_snbt()]
                            for prop, val in version_block.properties.items()
                        )
                    ):
                        original_block_matches.append(universal_block_id)

                universal_block_count = len(world.block_palette)
            blocks = chunk.blocks[slices]
            blocks[numpy.isin(blocks, original_block_matches)] = replacement_block_id
            chunk.blocks[slices] = blocks
            chunk.changed = True

            count += 1
            yield count / iter_count


export = {
    "name": "Replace",  # the name of the plugin
    "operation": Replace,  # the actual function to call when running the plugin
}
