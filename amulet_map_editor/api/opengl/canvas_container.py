import weakref
from wx.glcanvas import GLCanvas


class CanvasContainer:
    """A helper class to store a reference to a canvas.
    If a canvas is hard referenced there may be cyclic references leading to memory leaks.
    Subclass this class if you intend to store a reference to the canvas."""

    def __init__(self, canvas: GLCanvas):
        self._canvas = weakref.ref(canvas)

    @property
    def canvas(self) -> GLCanvas:
        return self._canvas()
