from typing import TYPE_CHECKING
import weakref

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas.edit_canvas import EditCanvas


class BaseUI:
    def __init__(self, canvas: "EditCanvas"):
        self._canvas = weakref.ref(canvas)

    @property
    def canvas(self) -> "EditCanvas":
        return self._canvas()
