import wx
from typing import Callable, Dict, Any, TYPE_CHECKING

from .operation_ui import OperationUI

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas.controllable_canvas import ControllableEditCanvas
    from amulet.api.world import World


class OperationError(Exception):
    """Error to raise if something went wrong when running the operation.
    Eg. if the operation requires something it is not given"""
    pass


class OperationSuccessful(Exception):
    """raise this if you want to exit the operation without creating an undo point.
    Any changes to the world since the last undo point will be reverted."""
    pass


class FixedFunctionUI(OperationUI):
    def __init__(self, parent: wx.Window, canvas: "ControllableEditCanvas", world: "World", options_path: str, operation: Callable, options: Dict[str, Any]):
        super().__init__(options_path)
        # TODO
