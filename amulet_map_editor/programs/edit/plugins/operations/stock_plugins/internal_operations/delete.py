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

        chunk_x, chunk_z = chunk.coordinates
        chunk_x *= 16
        chunk_z *= 16
        x_min = chunk_x + slices[0].start
        y_min = slices[1].start
        z_min = chunk_z + slices[2].start
        x_max = chunk_x + slices[0].stop
        y_max = slices[1].stop
        z_max = chunk_z + slices[2].stop

        for x, y, z in list(chunk.block_entities.keys()):
            if x_min <= x < x_max and y_min <= y < y_max and z_min <= z < z_max:
                chunk.block_entities.pop((x, y, z))

        chunk.changed = True
        count += 1
        yield count / iter_count
