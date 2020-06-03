from typing import TYPE_CHECKING

from amulet.api.structure import structure_buffer, Structure
from amulet.api.data_types import Dimension
from amulet.api.selection import SelectionGroup
from amulet_map_editor.programs.edit.plugins.api.errors import OperationSilentAbort

if TYPE_CHECKING:
    from amulet.api.world import World


def copy(
    world: "World",
    dimension: Dimension,
    selection: SelectionGroup
):
    structure = Structure.from_world(
        world, selection, dimension
    )
    structure_buffer.append(structure)
    raise OperationSilentAbort
