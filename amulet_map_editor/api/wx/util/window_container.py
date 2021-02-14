import weakref
import wx


class WindowContainer:
    """A helper class to store a reference to a wx.Window.
    If a window is hard referenced there may be cyclic references leading to memory leaks.
    Subclass this class if you intend to store a reference to a window."""

    def __init__(self, window: wx.Window):
        self._window = weakref.ref(window)

    @property
    def window(self) -> wx.Window:
        return self._window()
