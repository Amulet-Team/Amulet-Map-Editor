from typing import TYPE_CHECKING
from .base_behaviour import BaseBehaviour

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class BlockSelectionBehaviour(BaseBehaviour):
    """Adds the behaviour for a block based selection."""
    def __init__(self, canvas: "EditCanvas"):
        super().__init__(canvas)
