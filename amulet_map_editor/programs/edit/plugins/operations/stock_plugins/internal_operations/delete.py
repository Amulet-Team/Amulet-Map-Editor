from typing import TYPE_CHECKING

from amulet.operations.fill import fill
from amulet.api.selection import SelectionGroup
from amulet.api.block import UniversalAirBlock
from amulet.api.data_types import Dimension, OperationReturnType

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel


def delete(
    world: "BaseLevel", dimension: Dimension, selection: SelectionGroup
) -> OperationReturnType:
    yield from fill(
        world,
        dimension,
        selection,
        UniversalAirBlock,
    )
