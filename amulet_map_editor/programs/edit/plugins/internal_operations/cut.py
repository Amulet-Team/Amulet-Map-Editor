from typing import TYPE_CHECKING

from amulet.api.structure import structure_buffer, Structure
from amulet.api.data_types import Dimension
from amulet.api.selection import SelectionGroup
from amulet.operations.fill import fill
from amulet.api.block import Block

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
    yield from fill(
        world,
        dimension,
        selection,
        {
            "fill_block": world.translation_manager.get_version(
                'java', (1, 15, 2)
            ).block.to_universal(
                Block("minecraft", "air")
            )[0]
        }
    )


export = {
    "v": 1,  # a version 1 plugin
    "name": "Copy",  # the name of the plugin
    "features": ["src_selection"],
    "inputs": ["src_selection"],  # the inputs to give to the plugin
    "operation": copy_selection  # the actual function to call when running the plugin
}
