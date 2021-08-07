import numpy
cimport numpy
cimport cython

cdef float _brightness_step = 0.15
cdef dict _brightness_multiplier = {
    None: (1,) * 3,
    "up": (1,) * 3,
    "north": (1 - _brightness_step,) * 3,
    "south": (1 - _brightness_step,) * 3,
    "east": (1 - _brightness_step * 2,) * 3,
    "west": (1 - _brightness_step * 2,) * 3,
    "down": (1 - _brightness_step * 3,) * 3,
}

CULL_STR_INDEX = {
    "up": 1,
    "down": 2,
    "north": 3,
    "east": 4,
    "south": 5,
    "west": 6,
}

cdef int CULL_MAP[7][3]
CULL_MAP[0][:] = (0, 0, 0)
CULL_MAP[1][:] = (0, 1, 0)
CULL_MAP[2][:] = (0, -1, 0)
CULL_MAP[3][:] = (0, 0, -1)
CULL_MAP[4][:] = (1, 0, 0)
CULL_MAP[5][:] = (0, 0, 1)
CULL_MAP[6][:] = (-1, 0, 0)

cdef int ARRAY_SIZE = 10_000

@cython.boundscheck(False)
@cython.wraparound(False)
cdef tuple create_lod0_sub_chunk(
    unsigned int[:, :, :] larger_blocks,
    char[:, :, :] transparent_array,
    tuple model_verts,
    char[:] is_transparent,
    long[:] sub_chunk_offset,
):
    cdef int x, y, z, x_, y_, z_, dx, dy, dz, vert_count, vert_end, cull_id, v
    cdef unsigned int block_id
    cdef tuple vert_map

    cdef float[:, :] vert_table = numpy.empty((ARRAY_SIZE, 12), dtype=numpy.float32)
    cdef float[:, :] trans_vert_table = numpy.empty((ARRAY_SIZE, 12), dtype=numpy.float32)
    cdef float[:, :] temp_vert_table

    cdef int size_x = larger_blocks.shape[0] - 2
    cdef int size_y = larger_blocks.shape[1] - 2
    cdef int size_z = larger_blocks.shape[2] - 2

    chunk_verts = []
    chunk_verts_translucent = []

    cdef int vert_id = 0
    cdef int trans_vert_id = 0
    for x in range(size_x):
        for y in range(size_y):
            for z in range(size_z):
                x_ = x + 1
                y_ = y + 1
                z_ = z + 1
                block_id = larger_blocks[x_, y_, z_]
                vert_map = model_verts[block_id]
                for cull_id in range(7):
                    if vert_map[cull_id] is not None:
                        # iterate through each cull direction
                        if cull_id:
                            dx = x_ + CULL_MAP[cull_id][0]
                            dy = y_ + CULL_MAP[cull_id][1]
                            dz = z_ + CULL_MAP[cull_id][2]
                            # If the next block is opaque or both blocks are full transparent blocks, do nothing
                            if transparent_array[dx, dy, dz] == 0 or transparent_array[dx, dy, dz] == transparent_array[x_, y_, z_] == 1:
                                continue

                        temp_vert_table = vert_map[cull_id]
                        vert_count = temp_vert_table.shape[0]

                        if is_transparent[block_id] == 1:
                            vert_end = trans_vert_id+vert_count
                            if vert_end > ARRAY_SIZE:
                                chunk_verts_translucent.append(trans_vert_table[:trans_vert_id].copy())
                                trans_vert_id = 0
                                vert_end = trans_vert_id+vert_count
                            trans_vert_table[trans_vert_id:vert_end, :] = temp_vert_table
                            for v in range(trans_vert_id, trans_vert_id + vert_count):
                                trans_vert_table[v, 0] += x + sub_chunk_offset[0]
                                trans_vert_table[v, 1] += y + sub_chunk_offset[1]
                                trans_vert_table[v, 2] += z + sub_chunk_offset[2]
                            trans_vert_id += vert_count
                        else:
                            vert_end = vert_id+vert_count
                            if vert_end > ARRAY_SIZE:
                                chunk_verts.append(vert_table[:vert_id].copy())
                                vert_id = 0
                                vert_end = vert_id+vert_count
                            vert_table[vert_id:vert_end, :] = temp_vert_table
                            for v in range(vert_id, vert_id + vert_count):
                                vert_table[v, 0] += x + sub_chunk_offset[0]
                                vert_table[v, 1] += y + sub_chunk_offset[1]
                                vert_table[v, 2] += z + sub_chunk_offset[2]
                            vert_id += vert_count

    if vert_id:
        chunk_verts.append(vert_table[:vert_id].copy())
    if trans_vert_id:
        chunk_verts_translucent.append(trans_vert_table[:trans_vert_id].copy())
    return chunk_verts, chunk_verts_translucent


def create_lod0_chunk(
    resource_pack,
    chunk_offset: numpy.ndarray,
    blocks,
    block_palette,
    vert_len,  # should be 12
):
    if not hasattr(resource_pack, "block_model_verts"):
        # TODO: set up a proper location for these
        resource_pack.block_model_verts = ()
    if not hasattr(resource_pack, "block_is_transparent"):
        resource_pack.block_is_transparent = numpy.zeros(0, dtype=numpy.uint8)
    model_verts = resource_pack.block_model_verts
    is_transparent = resource_pack.block_is_transparent

    state_count = len(block_palette)
    done_count = min(len(model_verts), len(is_transparent))

    if state_count != done_count:
        # more block states have been added

        model_verts = model_verts[:done_count]
        is_transparent = is_transparent[:done_count]

        models = tuple(
            resource_pack.get_block_model(
                block_palette[block_temp_id]
            )
            for block_temp_id in range(done_count, state_count)
        )
        resource_pack.block_is_transparent = is_transparent = numpy.concatenate(
            (
            is_transparent,
            numpy.array([model.is_transparent for model in models], dtype=numpy.uint8)
            ),
            None,
            dtype=numpy.uint8
        )
        texture_bounds = {
            texture_path: resource_pack.texture_bounds(texture_path)
            for model in models
            for texture_path in model.textures
        }
        block_model_verts_new = []
        for model in models:
            vert_map = [None]*7
            for py_cull_dir in model.faces.keys():
                if py_cull_dir is None:
                    cull_id = 0
                elif py_cull_dir in CULL_STR_INDEX:
                    cull_id = CULL_STR_INDEX[py_cull_dir]
                else:
                    continue
                # the vertices in model space
                verts = model.verts[py_cull_dir].reshape((-1, 3))
                tverts = model.texture_coords[py_cull_dir].reshape((-1, 2))
                faces = model.faces[py_cull_dir]

                py_vert_table = numpy.zeros(
                    (faces.size, vert_len), dtype=numpy.float32
                )
                py_vert_table[:, :3] = verts[faces]
                py_vert_table[:, 3:5] = tverts[faces]

                vert_index = 0
                for texture_index in model.texture_index[py_cull_dir]:
                    py_vert_table[vert_index : vert_index + 3, 5:9] = texture_bounds[model.textures[texture_index]]
                    vert_index += 3

                py_vert_table[:, 9:12] = (
                    model.tint_verts[py_cull_dir].reshape((-1, 3))[faces]
                    * _brightness_multiplier[py_cull_dir]
                )
                # py_vert_table[:, 9:12] *= 0.9 + 0.2 * numpy.abs(
                #     (numpy.remainder(py_vert_table[:, 1:2] / 32, 2) - 1)
                # )
                vert_map[cull_id] = py_vert_table
            block_model_verts_new.append(tuple(vert_map))

        resource_pack.block_model_verts = model_verts = model_verts + tuple(block_model_verts_new)

    chunk_verts = []
    chunk_verts_translucent = []

    for block_array, sub_chunk_y in blocks:
        sub_chunk_offset = chunk_offset.copy()
        sub_chunk_offset[1] += sub_chunk_y

        chunk_verts_, chunk_verts_translucent_ = create_lod0_sub_chunk(
            block_array,
            is_transparent[block_array],
            model_verts,
            is_transparent,
            sub_chunk_offset,
        )
        chunk_verts += chunk_verts_
        chunk_verts_translucent += chunk_verts_translucent_

    return chunk_verts, chunk_verts_translucent
