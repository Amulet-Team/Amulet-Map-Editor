from typing import TYPE_CHECKING
from amulet_map_editor.api.opengl.canvas_container import CanvasContainer

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class EditCanvasContainer(CanvasContainer):
    """A helper class to store a reference to the canvas.
    This ensures there are no memory leaks due to circular references."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)

    @property
    def canvas(self) -> "EditCanvas":
        return self._canvas()
