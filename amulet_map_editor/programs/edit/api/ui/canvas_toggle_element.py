class CanvasToggleElement:
    """This is a base class for any UI element that is dropped
    into the canvas and can be enabled and disabled."""

    def enable(self):
        """Set the state of the UI for being enabled.
        Do not bind events to the canvas here because they will get removed. Do this in bind_events.
        """
        raise NotImplementedError

    def bind_events(self):
        """Bind all required events to the canvas.
        All events on the canvas will be automatically removed after the UI is disabled.
        """
        raise NotImplementedError

    def disable(self):
        """Stop the UI. Unload any excessive data. May get resumed again with a call to enable.
        All events bound to the canvas will be automatically removed after this is run.
        """
        raise NotImplementedError
