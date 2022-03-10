from __future__ import annotations

from typing import TYPE_CHECKING

from amulet.api.selection import SelectionGroup
from amulet.api.block import UniversalAirBlock
from amulet.api.data_types import Dimension, OperationReturnType

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel


def delete(
    world: "BaseLevel", dimension: Dimension, selection: SelectionGroup
) -> OperationReturnType:
    internal_id = world.block_palette.get_add_block(UniversalAirBlock)

    iter_count = len(list(world.get_coord_box(dimension, selection, False)))
    count = 0

    for chunk, slices, _ in world.get_chunk_slice_box(dimension, selection, False):
        chunk.blocks[slices] = internal_id
        chunk.changed = True
        count += 1
        yield count / iter_count
