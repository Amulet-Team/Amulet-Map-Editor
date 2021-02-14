class Drawable:
    """A base class for all classes holding opengl data."""

    def draw(self, *args, **kwargs):
        """Draw the opengl data."""
        raise NotImplementedError

    def unload(self):
        """Unload the opengl data."""
        raise NotImplementedError
