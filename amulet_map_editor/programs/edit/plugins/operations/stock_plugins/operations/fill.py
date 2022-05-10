"""
This license applies to this file only.
-- begin license --
MIT License
Copyright (c) 2021 Amulet-Team
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-- end license --
"""

from typing import TYPE_CHECKING, Tuple
import wx

from amulet.operations.fill import fill

from amulet_map_editor.api.wx.ui.base_select import EVT_PICK
from amulet_map_editor.api.wx.ui.block_select import BlockDefine
from amulet_map_editor.programs.edit.api.operations import DefaultOperationUI

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class Fill(wx.Panel, DefaultOperationUI):
    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        wx.Panel.__init__(self, parent)
        DefaultOperationUI.__init__(self, parent, canvas, world, options_path)
        self.Freeze()
        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        options = self._load_options({})

        self._block_define = BlockDefine(
            self,
            world.translation_manager,
            wx.VERTICAL,
            *(options.get("fill_block_options", []) or [world.level_wrapper.platform]),
            show_pick_block=True
        )
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

    def _on_pick_block_button(self, evt):
        """Set up listening for the block click"""
        self._show_pointer = True

    def _on_box_click(self):
        if self._show_pointer:
            self._show_pointer = False
            x, y, z = self._pointer.pointer_base
            self._block_define.universal_block = (
                self.world.get_block(x, y, z, self.canvas.dimension),
                None,
            )

    def _get_fill_block(self):
        return self._block_define.universal_block[0]

    def disable(self):
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
                self.canvas.selection.selection_group,
                self._get_fill_block(),
            )
        )


export = {
    "name": "Fill",  # the name of the plugin
    "operation": Fill,  # the actual function to call when running the plugin
}
