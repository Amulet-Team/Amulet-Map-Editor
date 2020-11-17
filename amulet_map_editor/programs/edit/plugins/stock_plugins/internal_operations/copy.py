from typing import TYPE_CHECKING

from amulet.api.structure import structure_cache, Structure
from amulet.api.data_types import Dimension
from amulet.api.selection import SelectionGroup
from amulet_map_editor.programs.edit.plugins.api.errors import (
    OperationSilentAbort,
    OperationError,
)

if TYPE_CHECKING:
    from amulet.api.world import World


def copy(world: "World", dimension: Dimension, selection: SelectionGroup):
    if selection:
        structure = Structure.from_world(world, selection, dimension)
        structure_cache.add_structure(structure)
        raise OperationSilentAbort
    else:
        raise OperationError(
            "At least one selection is required for the copy operation."
        )
