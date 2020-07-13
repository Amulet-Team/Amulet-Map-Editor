from amulet.operations.delete_chunk import delete_chunk


def delete_chunk_wrapper(world, dimension, selection, _):
    return delete_chunk(world, dimension, selection)


export = {
    "name": "Delete Chunks",  # the name of the plugin
    "operation": delete_chunk_wrapper,  # the actual function to call when running the plugin
}
