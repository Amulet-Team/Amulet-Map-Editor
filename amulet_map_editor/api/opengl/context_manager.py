class ContextManager:
    """Store the uuid of the context this data applies to."""

    def __init__(self, context_identifier: str):
        self._context_identifier = context_identifier

    @property
    def context_identifier(self) -> str:
        return self._context_identifier
