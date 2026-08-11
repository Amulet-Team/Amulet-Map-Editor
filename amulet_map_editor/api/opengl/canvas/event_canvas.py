import wx
from typing import Any
import logging

from amulet_map_editor.api.opengl.canvas import BaseCanvas

log = logging.getLogger(__name__)


class EventCanvas(BaseCanvas):
    """A modification of the normal canvas to make it easier to add and remove events."""

    def __init__(self, parent: wx.Window):
        self._bound_events: dict[wx.PyEventBinder, list[tuple[Any, Any]]] = {}
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
        # Disconnect all handlers
        for event, data in self._bound_events.items():
            for handler, source in data:
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
        # Store the event handler and source
        event_group = self._bound_events.setdefault(event, [])
        event_group.append((handler, source))

        if event == wx.EVT_KEY_DOWN:
            # If this is the first key down handler, bind the key down event
            if len(event_group) == 1:
                super().Bind(wx.EVT_KEY_DOWN, self._on_key_down)
        else:
            super().Bind(event, handler, source, id, id2)

    def Unbind(
        self, event, source=None, id=wx.ID_ANY, id2=wx.ID_ANY, handler=None
    ) -> bool:
        """Unbind an event from the canvas."""
        try:
            # Try and remove the event handler and source
            event_group = self._bound_events[event]
            event_group.remove((handler, source))
        except (KeyError, ValueError):
            pass
        else:
            # If there are no more handlers for the key down event, unbind it
            if event == wx.EVT_KEY_DOWN and not event_group:
                super().Unbind(wx.EVT_KEY_DOWN, self._on_key_down)
                return True

        # Remove the handler
        return super().Unbind(event, source=source, id=id, id2=id2, handler=handler)

    def _on_key_down(self, evt: wx.KeyEvent) -> None:
        # On macOS if no handler claims the key down event, an alert sound will play.
        # To get around this, we must have one handler and skip if no handler claims the event.
        handled = False
        for handler, source in self._bound_events.get(wx.EVT_KEY_DOWN, []):
            if source is not None and source != evt.GetEventObject():
                continue
            evt.Skip(False)
            try:
                handler(evt)
            except Exception as e:
                log.exception(f"Failed to handle key down event: {e}")
            if not evt.GetSkipped():
                handled = True
        evt.Skip(not handled)
