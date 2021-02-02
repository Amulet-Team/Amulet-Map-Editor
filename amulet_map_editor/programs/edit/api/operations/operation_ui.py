import pickle
from typing import Any, TYPE_CHECKING, Union, Tuple
import os
import wx
import weakref

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas
    from amulet.api.level import BaseLevel

OperationUIType = Union[wx.Window, wx.Sizer, "OperationUI"]


class OperationUI:
    """The base class that all operations must inherit from."""

    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        self._parent = weakref.ref(parent)
        self._canvas = weakref.ref(canvas)
        self._world = weakref.ref(world)
        self._options_path = options_path

    @property
    def parent(self) -> wx.Window:
        return self._parent()

    @property
    def canvas(self) -> "EditCanvas":
        return self._canvas()

    @property
    def world(self) -> "BaseLevel":
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

    def unload(self):
        """Unbind any events that have been set up and make safe to destroy the UI.
        The UI will be destroyed from externally."""
        raise NotImplementedError

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
