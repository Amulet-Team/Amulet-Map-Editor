from typing import TYPE_CHECKING
import wx
import numpy

from amulet.api.block import Block
from amulet_map_editor.amulet_wx.ui.select_block import BlockDefine
from amulet_map_editor.programs.edit.plugins import OperationUI
from amulet_map_editor.amulet_wx.ui.simple import SimpleScrollablePanel

if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class Replace(SimpleScrollablePanel, OperationUI):
    def __init__(
            self,
            parent: wx.Window,
            canvas: "EditCanvas",
            world: "World",
            options_path: str
    ):
        SimpleScrollablePanel.__init__(self, parent)
        OperationUI.__init__(self, parent, canvas, world, options_path)

        options = self._load_options({})

        self._original_block = BlockDefine(
            self,
            world.world_wrapper.translation_manager,
            *(options.get("original_block_options", []) or [world.world_wrapper.platform]),
            wildcard=True,
            style=wx.BORDER_SIMPLE,
            properties_style=wx.BORDER_SIMPLE
        )
        self._sizer.Add(self._original_block, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)
        self._replacement_block = BlockDefine(
            self,
            world.world_wrapper.translation_manager,
            *(options.get("replacement_block_options", []) or [world.world_wrapper.platform]),
            style=wx.BORDER_SIMPLE,
            properties_style=wx.BORDER_SIMPLE
        )
        self._sizer.Add(self._replacement_block, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self._run_button = wx.Button(self, label="Run Operation")
        self._run_button.Bind(wx.EVT_BUTTON, self._run_operation)
        self._sizer.Add(self._run_button, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self.Layout()

    def _get_replacement_block(self) -> Block:
        return self.world.translation_manager.get_version(
            self._replacement_block.platform,
            self._replacement_block.version
        ).block.to_universal(
            self._replacement_block.block,
            force_blockstate=self._replacement_block.force_blockstate
        )[0]

    def unload(self):
        self._save_options({
            "original_block_options": self._original_block.options,
            "replacement_block": self._get_replacement_block(),
            "replacement_block_options": self._replacement_block.options,
        })

    def _run_operation(self, _):
        self.canvas.run_operation(
            lambda: self._replace()
        )

    def _replace(self):
        world = self.world
        selection = self.canvas.selection_group
        dimension = self.canvas.dimension

        original_platform, original_version, original_blockstate, original_namespace, original_base_name, original_properties = self._original_block.options
        replacement_block = self._get_replacement_block()

        replacement_block_id = world.palette.get_add_block(replacement_block)

        original_block_matches = []
        universal_block_count = 0

        iter_count = len(list(world.get_chunk_slices(selection, dimension)))
        count = 0

        for chunk, slices, _ in world.get_chunk_slices(selection, dimension):
            if universal_block_count < len(world.palette):
                for universal_block_id in range(universal_block_count, len(world.palette)):
                    version_block = world.translation_manager.get_version(
                        original_platform,
                        original_version
                    ).block.from_universal(
                        world.palette[universal_block_id],
                        force_blockstate=original_blockstate
                    )[0]
                    if version_block.namespace == original_namespace and \
                            version_block.base_name == original_base_name \
                            and all(original_properties.get(prop) in ['*', val.to_snbt()] for prop, val in version_block.properties.items()):
                        original_block_matches.append(universal_block_id)

                universal_block_count = len(world.palette)
            blocks = chunk.blocks[slices]
            blocks[numpy.isin(blocks, original_block_matches)] = replacement_block_id
            chunk.blocks[slices] = blocks
            chunk.changed = True

            count += 1
            yield 100 * count / iter_count

    def DoGetBestClientSize(self):
        sizer = self.GetSizer()
        if sizer is None:
            return -1, -1
        else:
            sx, sy = self.GetSizer().CalcMin()
            return sx + wx.SystemSettings.GetMetric(wx.SYS_VSCROLL_X), sy + wx.SystemSettings.GetMetric(wx.SYS_HSCROLL_Y)


export = {
    "name": "Replace",  # the name of the plugin
    "operation": Replace,  # the actual function to call when running the plugin
}
