from amulet.api.level import BaseLevel
from amulet.api.data_types import Dimension
from amulet.api.selection import SelectionGroup


def prune_chunks(world: "BaseLevel", dimension: Dimension, selection: SelectionGroup):
    chunks = world.all_chunk_coords(dimension).difference(selection.chunk_locations())
    for i, (cx, cz) in enumerate(chunks):
        world.delete_chunk(cx, cz, dimension)
        yield (i + 1) / len(chunks)
