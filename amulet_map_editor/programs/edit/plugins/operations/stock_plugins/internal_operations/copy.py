from typing import TYPE_CHECKING

from amulet.api.structure import structure_cache
from amulet.api.data_types import Dimension
from amulet.api.selection import SelectionGroup
from amulet_map_editor.programs.edit.api.operations import (
    OperationSilentAbort,
    OperationError,
)
from amulet.api.data_types import OperationReturnType

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel


def copy(
    world: "BaseLevel", dimension: Dimension, selection: SelectionGroup
) -> OperationReturnType:
    if selection:
        yield 0, "Copying"
        structure = yield from world.extract_structure_iter(selection, dimension)
        structure_cache.add_structure(structure, structure.dimensions[0])
        raise OperationSilentAbort
    else:
        raise OperationError(
            "At least one selection is required for the copy operation."
        )
