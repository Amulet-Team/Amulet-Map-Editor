from typing import TYPE_CHECKING

from amulet.api.block import Block
from amulet.api.data_types import Dimension, OperationReturnType
from amulet.api.selection import SelectionGroup
from amulet.operations.fill import fill

if TYPE_CHECKING:
    from amulet.api.world import World


def delete(
    world: "World", dimension: Dimension, selection: SelectionGroup
) -> OperationReturnType:
    yield from fill(
        world,
        dimension,
        selection,
        world.translation_manager.get_version("java", (1, 15, 2)).block.to_universal(
            Block("minecraft", "air")
        )[0],
    )
