import numpy
from typing import Tuple, Dict, List, Union

import minecraft_model_reader
from amulet.api.chunk import Chunk
from amulet.api.registry import BlockManager

from amulet_map_editor.api.opengl.mesh import TriMesh
from amulet_map_editor.api.opengl.resource_pack import (
    OpenGLResourcePackManagerStatic,
    OpenGLResourcePack,
)

_brightness_step = 0.15
_brightness_multiplier = {
    None: (1,) * 3,
    "up": (1,) * 3,
    "north": (1 - _brightness_step,) * 3,
    "south": (1 - _brightness_step,) * 3,
    "east": (1 - _brightness_step * 2,) * 3,
    "west": (1 - _brightness_step * 2,) * 3,
    "down": (1 - _brightness_step * 3,) * 3,
}


def py_create_lod0_sub_chunk(
    larger_blocks: numpy.ndarray,
    models: Tuple[minecraft_model_reader.BlockMesh],
    texture_bounds: Dict[str, Tuple[float, float, float, float]],
    vert_len: int,
    chunk_offset: numpy.ndarray,
    sub_chunk_y_offset: int,
) -> Tuple[List[numpy.ndarray], List[numpy.ndarray]]:
    """
    Create chunk geometry for a given sub-chunk.
    Creates a numpy array for opaque geometry and a numpy array for translucent geometry.

    :param larger_blocks: A numpy array for the sub-chunk that extends by one block in each direction.
    :param models: A tuple of block models. Indices match the larger_blocks array.
    :param texture_bounds: A dictionary mapping texture id to the bounds of the texture in the atlas.
    :param vert_len: The number of float32 values per vertex.
    :param chunk_offset: The offset of the chunk in the world.
    :param sub_chunk_y_offset: The offset of the sub-chunk relative to the chunk.
    :return:
    """
    sub_chunk_offset = (0, sub_chunk_y_offset, 0)
    blocks = larger_blocks[1:-1, 1:-1, 1:-1]
    transparent_array = numpy.array(
        [model.is_transparent for model in models], dtype=numpy.uint8
    )[larger_blocks]

    def get_transparent_array(offset_transparent_array, transparent_array_):
        return numpy.logical_and(
            offset_transparent_array,  # if the next block is transparent
            numpy.logical_not(  # but is not the same block with transparency mode 1
                (offset_transparent_array == 1)
                * (offset_transparent_array == transparent_array_)
            ),
        )

    middle_transparent_array = transparent_array[1:-1, 1:-1, 1:-1]
    show_up = get_transparent_array(
        transparent_array[1:-1, 2:, 1:-1], middle_transparent_array
    )
    show_down = get_transparent_array(
        transparent_array[1:-1, :-2, 1:-1], middle_transparent_array
    )
    show_north = get_transparent_array(
        transparent_array[1:-1, 1:-1, :-2], middle_transparent_array
    )
    show_south = get_transparent_array(
        transparent_array[1:-1, 1:-1, 2:], middle_transparent_array
    )
    show_east = get_transparent_array(
        transparent_array[2:, 1:-1, 1:-1], middle_transparent_array
    )
    show_west = get_transparent_array(
        transparent_array[:-2, 1:-1, 1:-1], middle_transparent_array
    )

    show_map = {
        "up": show_up,
        "down": show_down,
        "north": show_north,
        "south": show_south,
        "east": show_east,
        "west": show_west,
    }

    chunk_verts = []
    chunk_verts_translucent = []

    x, y, z = blocks.shape
    block_locations = numpy.transpose(numpy.mgrid[0:x, 0:y, 0:z], (1, 2, 3, 0)).reshape(
        (-1, 3)
    )
    unique_blocks, inverse, counts = numpy.unique(
        blocks, return_inverse=True, return_counts=True
    )
    block_indexes = numpy.argsort(inverse)
    block_locations = numpy.split(
        block_locations[block_indexes], numpy.cumsum(counts)[:-1]
    )

    for block_temp_id, all_block_locations in zip(unique_blocks, block_locations):
        model = models[block_temp_id]
        # for each unique blockstate in the chunk
        # get the model and the locations of the blocks
        # if not all_block_locations.size:
        #     continue
        where = None
        for cull_dir in model.faces.keys():
            # iterate through each cull direction
            # narrow down the blocks to what should be created for that cull direction
            if cull_dir is None:
                block_locations = all_block_locations
            elif cull_dir in show_map:
                if where is None:
                    where = tuple(all_block_locations.T)
                block_locations = all_block_locations[show_map[cull_dir][where]]
                if not block_locations.size:
                    continue
            else:
                continue

            # the number of blocks and their offsets in chunk space
            block_count = len(block_locations)
            block_offsets = block_locations

            # the vertices in model space
            verts = model.verts[cull_dir].reshape((-1, 3))
            tverts = model.texture_coords[cull_dir].reshape((-1, 2))
            faces = model.faces[cull_dir]

            # each slice in the first axis is a new block, each slice in the second is a new vertex
            vert_table = numpy.zeros(
                (block_count, faces.size, vert_len), dtype=numpy.float32
            )
            vert_table[:, :, :3] = (
                verts[faces]
                + block_offsets[:, :].reshape((-1, 1, 3))
                + chunk_offset
                + sub_chunk_offset
            )
            vert_table[:, :, 3:5] = tverts[faces]

            vert_index = 0
            for texture_index in model.texture_index[cull_dir]:
                tex_bounds = texture_bounds[model.textures[texture_index]]

                vert_table[:, vert_index : vert_index + 3, 5:9] = tex_bounds
                vert_index += 3

            vert_table[:, :, 9:12] = (
                model.tint_verts[cull_dir].reshape((-1, 3))[faces]
                * _brightness_multiplier[cull_dir]
            )
            vert_table[:, :, 9:12] *= 0.9 + 0.2 * numpy.abs(
                (numpy.remainder(vert_table[:, :, 1:2] / 32, 2) - 1)
            )

            if model.is_transparent == 1:
                chunk_verts_translucent.append(vert_table.ravel())
            else:
                chunk_verts.append(vert_table.ravel())

    return chunk_verts, chunk_verts_translucent


def py_create_lod0_chunk(
    resource_pack: OpenGLResourcePack,
    chunk_offset: numpy.ndarray,
    blocks: List[Tuple[numpy.ndarray, int]],
    block_palette: BlockManager,
    vert_len: int,
):
    chunk_verts = []
    chunk_verts_translucent = []

    for block_array, sub_chunk_y in blocks:
        # unique blocks per sub-chunk
        unique_sub_chunk_blocks, inverse_block_array = numpy.unique(
            block_array, return_inverse=True
        )

        models: Tuple[minecraft_model_reader.BlockMesh] = tuple(
            resource_pack.get_block_model(block_palette[block_temp_id])
            for block_temp_id in unique_sub_chunk_blocks
        )
        texture_bounds: Dict[str, Tuple[float, float, float, float]] = {
            texture_path: resource_pack.texture_bounds(texture_path)
            for model in models
            for texture_path in model.textures
        }
        chunk_verts_, chunk_verts_translucent_ = py_create_lod0_sub_chunk(
            inverse_block_array.reshape(block_array.shape),
            models,
            texture_bounds,
            vert_len,
            chunk_offset,
            sub_chunk_y,
        )
        chunk_verts += chunk_verts_
        chunk_verts_translucent += chunk_verts_translucent_

    return chunk_verts, chunk_verts_translucent


try:
    from .chunk_builder_cy import create_lod0_chunk

    print("Using cython chunk generator")
except:
    print("Using python chunk generator")
    create_lod0_chunk = py_create_lod0_chunk


class RenderChunkBuilder(TriMesh, OpenGLResourcePackManagerStatic):
    """A class to define the logic to generate geometry from a block array"""

    def __init__(self, context_identifier: str, resource_pack: OpenGLResourcePack):
        texture = resource_pack.get_atlas_id(context_identifier)
        TriMesh.__init__(self, context_identifier, texture)
        OpenGLResourcePackManagerStatic.__init__(self, resource_pack)

    @property
    def chunk(self) -> Chunk:
        raise NotImplementedError

    @property
    def offset(self) -> numpy.ndarray:
        raise NotImplementedError

    @staticmethod
    def _get_block_data(blocks: numpy.ndarray) -> Tuple[numpy.ndarray, numpy.ndarray]:
        """Given a Chunk object will return the chunk arrays needed to generate geometry
        :returns: block array of the chunk, block array one block larger than the chunk, array of unique blocks"""
        larger_blocks = numpy.zeros(blocks.shape + numpy.array((2, 2, 2)), blocks.dtype)
        larger_blocks[1:-1, 1:-1, 1:-1] = blocks
        unique_blocks = numpy.unique(larger_blocks)
        return larger_blocks, unique_blocks

    def create_geometry(self):
        raise NotImplementedError

    def _set_verts(
        self,
        chunk_verts: List[numpy.ndarray],
        chunk_verts_translucent: List[numpy.ndarray],
    ):
        if chunk_verts:
            self.verts = numpy.concatenate(chunk_verts, None)
            self.verts_translucent = self.verts.size
        else:
            self.verts = self.new_empty_verts()

        if chunk_verts_translucent:
            chunk_verts_translucent.insert(0, self.verts)
            self.verts = numpy.concatenate(chunk_verts_translucent, None)

        self.draw_count = int(self.verts.size // self._vert_len)

    def _create_lod0_multi(
        self, blocks: List[Tuple[numpy.ndarray, int]]
    ) -> Tuple[List[numpy.ndarray], List[numpy.ndarray]]:
        """Create LOD0 geometry data for every sub-chunk in a given chunk.

        :param blocks: A list of tuples containing block arrays extending one block outside the sub-chunk in each direction.
        :return: Opaque block vertices, translucent block vertices.
        """
        return create_lod0_chunk(
            self.resource_pack,
            self.offset,
            blocks,
            self.chunk.block_palette,
            self._vert_len,
        )
