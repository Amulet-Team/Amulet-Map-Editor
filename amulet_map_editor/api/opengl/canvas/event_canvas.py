import wx
from typing import List, Tuple, Any
import logging

from amulet_map_editor.api.opengl.canvas import BaseCanvas

log = logging.getLogger(__name__)


class EventCanvas(BaseCanvas):
    """A modification of the normal canvas to make it easier to add and remove events."""

    def __init__(self, parent: wx.Window):
        self._bound_events: List[Tuple[wx.PyEventBinder, Any, Any]] = []
        super().__init__(parent)

    def reset_bound_events(self):
        """Unbind all events and re-bind the default events.
        We are allowing users to bind custom events so we should have a way to reset what is bound.
        """
        self.tear_down_events()
        self.bind_events()

    def tear_down_events(self):
        """Unbind all events.
        We are allowing users to bind custom events so we should have a way to reset what is bound.
        """
        for event, handler, source in self._bound_events:
            if source is None:
                while super().Unbind(event):
                    pass
            else:
                if not self.Unbind(event, source, handler=handler):
                    log.error(f"Failed to unbind {event}, {handler}, {source}")
        self._bound_events.clear()

    def bind_events(self):
        """Set up all events required to run.
        Note this will also bind subclass events."""
        raise NotImplementedError

    def Bind(self, event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY):
        """Bind an event to the canvas."""
        self._bound_events.append((event, handler, source))
        super().Bind(event, handler, source, id, id2)

    def Unbind(
        self, event, source=None, id=wx.ID_ANY, id2=wx.ID_ANY, handler=None
    ) -> bool:
        """Unbind an event from the canvas."""
        key = (event, handler, source)
        if key in self._bound_events:
            self._bound_events.remove(key)
        return super().Unbind(event, source=source, id=id, id2=id2, handler=handler)
