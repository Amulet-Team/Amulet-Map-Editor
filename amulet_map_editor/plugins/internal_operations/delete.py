from typing import TYPE_CHECKING

from amulet.operations.fill import fill
from amulet.api.selection import SelectionGroup
from amulet.api.block import Block
from amulet.api.data_types import Dimension

if TYPE_CHECKING:
    from amulet.api.world import World


def delete(
    world: "World",
    dimension: Dimension,
    selection_box: SelectionGroup
):
    yield from fill(
        world,
        dimension,
        selection_box,
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
    "name": "Delete",  # the name of the plugin
    "features": ["src_selection"],
    "inputs": ["src_selection"],  # the inputs to give to the plugin
    "operation": delete,  # the actual function to call when running the plugin
}
