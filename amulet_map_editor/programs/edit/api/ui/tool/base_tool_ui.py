import wx
from typing import Union, TYPE_CHECKING

from amulet_map_editor.programs.edit.api.edit_canvas_container import (
    EditCanvasContainer,
)
from ..canvas_toggle_element import CanvasToggleElement

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class BaseToolUI(EditCanvasContainer, CanvasToggleElement):
    """The abstract base class for all tools that are to be loaded into the canvas."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
        self._is_setup = False

    @property
    def is_setup(self) -> bool:
        return self._is_setup

    def setup(self):
        """
        Behaviour run before showing the tool for the first time.
        This is useful so tools only need creating when they are first used.
        Reduces the delay when first loading.
        """
        self._is_setup = True

    @property
    def name(self) -> str:
        """The name of the tool."""
        raise NotImplementedError

    def enable(self):
        """Set the state of the tool for being enabled.
        Do not bind events to the canvas here because they will get removed. Do this in bind_events."""
        pass

    def bind_events(self):
        """Bind all required events to the canvas.
        All events on the canvas will be automatically removed after the tool is disabled.
        """
        pass

    def disable(self):
        """Stop the tool. Unload any excessive data. May get resumed again with a call to enable.
        All events bound to the canvas will be automatically removed after this is run."""
        pass
