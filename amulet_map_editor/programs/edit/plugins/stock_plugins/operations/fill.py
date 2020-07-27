from typing import TYPE_CHECKING
import wx

from amulet.operations.fill import fill
from amulet_map_editor.amulet_wx.ui.block_select import BlockDefine
from amulet_map_editor.programs.edit.plugins import OperationUI

if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class Fill(wx.Panel, OperationUI):
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
            world.translation_manager,
            wx.VERTICAL,
            *(options.get("fill_block_options", []) or [world.world_wrapper.platform])
        )
        self._sizer.Add(self._block_define, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self._run_button = wx.Button(self, label="Run Operation")
        self._run_button.Bind(wx.EVT_BUTTON, self._run_operation)
        self._sizer.Add(self._run_button, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5)

        self.Layout()

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
        self.canvas.run_operation(
            lambda: fill(
                self.world,
                self.canvas.dimension,
                self.canvas.selection_group,
                self._get_fill_block(),
            )
        )


export = {
    "name": "Fill",  # the name of the plugin
    "operation": Fill,  # the actual function to call when running the plugin
}
