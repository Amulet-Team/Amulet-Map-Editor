from typing import TYPE_CHECKING
from .raycast_behaviour import RaycastBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class PointerBehaviour(RaycastBehaviour):
    """Adds the behaviour of the selection pointer."""
    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
