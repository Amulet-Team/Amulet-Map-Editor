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

from typing import TYPE_CHECKING
import wx

from amulet.api.selection import SelectionGroup
from amulet.api.data_types import Dimension, OperationReturnType

from amulet_map_editor.programs.edit.api.operations import (
    SimpleOperationPanel,
    OperationSilentAbort,
)

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class Clone(SimpleOperationPanel):
    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)
        self._add_run_button()
        self.Layout()

    def _operation(
        self, world: "BaseLevel", dimension: Dimension, selection: SelectionGroup
    ) -> OperationReturnType:
        structure = world.extract_structure(selection, dimension)
        self.canvas.paste(structure, structure.dimensions[0])
        raise OperationSilentAbort


export = {
    "name": "Clone",  # the name of the plugin
    "operation": Clone,  # the actual function to call when running the plugin
}
