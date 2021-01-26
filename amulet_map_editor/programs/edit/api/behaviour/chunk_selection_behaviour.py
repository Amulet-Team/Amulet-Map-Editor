from typing import TYPE_CHECKING
from .base_behaviour import BaseBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class ChunkSelectionBehaviour(BaseBehaviour):
    """Adds the behaviour for a chunk based selection."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
