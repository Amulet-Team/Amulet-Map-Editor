from amulet.api.level import BaseLevel
from amulet.api.data_types import Dimension
from amulet.api.selection import SelectionGroup
from amulet.api.chunk import Chunk


def prune_chunks(
    world: "BaseLevel",
    dimension: Dimension,
    selection: SelectionGroup,
    load_original: bool = True,
):
    chunks = world.all_chunk_coords(dimension).difference(selection.chunk_locations())
    iter_count = len(chunks)
    for count, (cx, cz) in enumerate(chunks):
        world.delete_chunk(cx, cz, dimension)

        if not load_original:
            # this part is kind of hacky.
            # Work out a propery API to do this.
            key = dimension, cx, cz
            if key not in world.chunks._history_database:
                world.chunks._register_original_entry(key, Chunk(cx, cz))

        yield (count + 1) / iter_count
