from typing import TYPE_CHECKING
from ..edit_canvas_container import EditCanvasContainer

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class BaseBehaviour(EditCanvasContainer):
    """This class implements how the program actually works.
    It detects various inputs and sets the state of the program accordingly.
    This is just a shell of the class to implement the API."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)

    def bind_events(self):
        """Set up all events required to run."""
        pass
