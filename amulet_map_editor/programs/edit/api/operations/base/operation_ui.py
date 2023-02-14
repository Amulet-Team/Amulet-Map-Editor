import pickle
from typing import Any, TYPE_CHECKING, Union, Tuple
import os
import wx
import weakref
import warnings

from amulet_map_editor.programs.edit.api.edit_canvas_container import (
    EditCanvasContainer,
)
from amulet_map_editor.programs.edit.api.ui.canvas_toggle_element import (
    CanvasToggleElement,
)

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas
    from amulet.api.level import BaseLevel

OperationUIType = Union[wx.Window, wx.Sizer, "OperationUI"]


class OperationUI(EditCanvasContainer, CanvasToggleElement):
    """The base class that all operations must inherit from."""

    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        super().__init__(canvas)
        self._parent = weakref.ref(parent)
        self._world = weakref.ref(world)
        self._options_path = options_path

    @property
    def parent(self) -> wx.Window:
        """The UI element that contains this operation."""
        return self._parent()

    @property
    def world(self) -> "BaseLevel":
        """The world to operate on."""
        return self._world()

    @property
    def wx_add_options(self) -> Tuple[int, ...]:
        """The options used to put the UI element into a vertical BoxSizer covering the whole canvas.
        Override if these options do not work for your UI."""
        if isinstance(self, wx.Window):
            return ()
        elif isinstance(self, wx.Sizer):
            return 1, wx.EXPAND
        return ()

    def enable(self):
        """Set the state of the UI for being enabled.
        Do not bind events to the canvas here because they will get removed. Do this in bind_events.
        """
        pass

    def bind_events(self):
        """Bind all required events to the canvas.
        All events on the canvas will be automatically removed after the UI is disabled.
        """
        pass

    def disable(self):
        """Stop the UI and make it safe to be destroyed.
        Unload any excessive data. May get resumed again with a call to enable.
        All events bound to the canvas will be automatically removed after this is run.
        """
        if hasattr(self, "unload") and callable(self.unload):
            warnings.warn(
                "OperationUI.unload is depreciated and will be removed in the future. Please used OperationUI.disable instead",
                DeprecationWarning,
            )
            self.unload()

    def _load_options(self, default=None) -> Any:
        """Load previously saved options from disk or return the default options."""
        try:
            with open(self._options_path, "rb") as f:
                return pickle.load(f)
        except:
            return default

    def _save_options(self, options: Any):
        """Save the given options to disk so that they persist in the next session."""
        os.makedirs(os.path.dirname(self._options_path), exist_ok=True)
        with open(self._options_path, "wb") as f:
            return pickle.dump(options, f)
