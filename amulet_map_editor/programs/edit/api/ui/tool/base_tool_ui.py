import wx
from typing import Union, Any

from amulet_map_editor.programs.edit.api.edit_canvas_container import (
    EditCanvasContainer,
)
from ..canvas_toggle_element import CanvasToggleElement

BaseToolUIType = Union[wx.Window, wx.Sizer, "BaseToolUI"]


class BaseToolUI(EditCanvasContainer, CanvasToggleElement):
    """The abstract base class for all tools that are to be loaded into the canvas."""

    @property
    def name(self) -> str:
        """The name of the tool."""
        raise NotImplementedError

    def enable(self):
        """Set the state of the tool for being enabled.
        Do not bind events to the canvas here because they will get removed. Do this in bind_events.
        """
        pass

    def bind_events(self):
        """Bind all required events to the canvas.
        All events on the canvas will be automatically removed after the tool is disabled.
        """
        pass

    def set_state(self, state: Any):
        """
        Set any state data.
        In some cases one tool might bounce to another and want to do more than just starting it.
        This will get called after enabling the tool.

        :param state: The state to set. Validate that this data is correct because it may come from anywhere.
        """
        pass

    def disable(self):
        """Stop the tool. Unload any excessive data. May get resumed again with a call to enable.
        All events bound to the canvas will be automatically removed after this is run.
        """
        pass
