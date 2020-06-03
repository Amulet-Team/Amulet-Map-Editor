from typing import TYPE_CHECKING

from amulet.api.structure import structure_buffer, Structure
from amulet.api.data_types import Dimension, OperationReturnType
from amulet.api.selection import SelectionGroup
from amulet_map_editor.programs.edit.plugins.stock_plugins.internal_operations.delete import delete

if TYPE_CHECKING:
    from amulet.api.world import World


def cut(
    world: "World",
    dimension: Dimension,
    selection: SelectionGroup
) -> OperationReturnType:
    structure = Structure.from_world(
        world, selection, dimension
    )
    structure_buffer.append(structure)
    yield from delete(
        world,
        dimension,
        selection,
    )
