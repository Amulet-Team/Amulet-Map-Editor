from typing import TYPE_CHECKING

from amulet.api.structure import structure_buffer, Structure
from amulet.api.data_types import Dimension
from amulet.api.selection import SelectionGroup

if TYPE_CHECKING:
    from amulet.api.world import World


def copy_selection(
    world: "World",
    dimension: Dimension,
    selection: SelectionGroup
):
    structure = Structure.from_world(
        world, selection, dimension
    )
    structure_buffer.append(structure)
    return True


export = {
    "v": 1,  # a version 1 plugin
    "name": "Copy",  # the name of the plugin
    "features": ["src_selection"],
    "inputs": ["src_selection"],  # the inputs to give to the plugin
    "operation": copy_selection  # the actual function to call when running the plugin
}
