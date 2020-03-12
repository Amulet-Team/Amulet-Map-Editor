import numpy
from typing import Tuple, Dict

import minecraft_model_reader
from amulet_map_editor.opengl.mesh import new_empty_verts, TriMesh


class BaseRenderChunk(TriMesh):
    """A class to define the logic to generate geometry from a block array"""

    def _get_model(self, block_temp_id: int) -> minecraft_model_reader.MinecraftMesh:
        raise NotImplementedError

    def _texture_bounds(self, texture):
        raise NotImplementedError

    @property
    def offset(self) -> numpy.ndarray:
        raise NotImplementedError

    def _get_block_data(self, blocks: numpy.ndarray) -> Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
        """Given a Chunk object will return the chunk arrays needed to generate geometry
        :returns: block array of the chunk, block array one block larger than the chunk, array of unique blocks"""
        larger_blocks = numpy.zeros(blocks.shape + numpy.array((2, 2, 2)), blocks.dtype)
        larger_blocks[1:-1, 1:-1, 1:-1] = blocks

        larger_blocks = self._fill_boundary_block_data(larger_blocks)

        unique_blocks = numpy.unique(larger_blocks)
        return blocks, larger_blocks, unique_blocks

    def _fill_boundary_block_data(self, larger_blocks: numpy.ndarray) -> numpy.ndarray:
        return larger_blocks

    def _create_lod0(self, blocks: numpy.ndarray, larger_blocks: numpy.ndarray, unique_blocks: numpy.ndarray):
        transparent_array = numpy.zeros(larger_blocks.shape, dtype=numpy.uint8)
        models: Dict[int, minecraft_model_reader.MinecraftMesh] = {}
        for block_temp_id in unique_blocks:
            model = models[block_temp_id] = self._get_model(block_temp_id)
            transparent_array[larger_blocks == block_temp_id] = model.is_transparent

        def get_transparent_array(offset_transparent_array, transparent_array_):
            return numpy.logical_and(
                offset_transparent_array,  # if the next block is transparent
                numpy.logical_not(  # but is not the same block with transparency mode 1
                    (offset_transparent_array == 1) * (offset_transparent_array == transparent_array_)
                )
            )

        middle_transparent_array = transparent_array[1:-1, 1:-1, 1:-1]
        show_up = get_transparent_array(transparent_array[1:-1, 2:, 1:-1], middle_transparent_array)
        show_down = get_transparent_array(transparent_array[1:-1, :-2, 1:-1], middle_transparent_array)
        show_north = get_transparent_array(transparent_array[1:-1, 1:-1, :-2], middle_transparent_array)
        show_south = get_transparent_array(transparent_array[1:-1, 1:-1, 2:], middle_transparent_array)
        show_east = get_transparent_array(transparent_array[2:, 1:-1, 1:-1], middle_transparent_array)
        show_west = get_transparent_array(transparent_array[:-2, 1:-1, 1:-1], middle_transparent_array)

        show_map = {
            'up': show_up,
            'down': show_down,
            'north': show_north,
            'south': show_south,
            'east': show_east,
            'west': show_west
        }

        chunk_verts = []
        chunk_verts_translucent = []

        for block_temp_id, model in models.items():
            # for each unique blockstate in the chunk
            # get the model and the locations of the blocks
            model: minecraft_model_reader.MinecraftMesh
            all_block_locations = numpy.argwhere(blocks == block_temp_id)
            if not all_block_locations.size:
                continue
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
                vert_table = numpy.zeros((block_count, faces.size, 10), dtype=numpy.float32)
                vert_table[:, :, :3] = verts[faces] + block_offsets[:, :].reshape((-1, 1, 3)) + self.offset
                vert_table[:, :, 3:5] = tverts[faces]

                vert_index = 0
                for texture_index in model.texture_index[cull_dir]:
                    tex_bounds = self._texture_bounds(model.textures[texture_index])

                    vert_table[:, vert_index:vert_index+3, 5:9] = tex_bounds
                    vert_index += 3

                vert_table[:, :, 9] = model.tint_verts[cull_dir][faces]

                if model.is_transparent == 1:
                    chunk_verts_translucent.append(vert_table.ravel())
                else:
                    chunk_verts.append(vert_table.ravel())

        if chunk_verts:
            self.verts = numpy.concatenate(chunk_verts, 0)
            self.draw_count = int(self.verts.size // 10)
            self.verts_translucent = self.verts.size
        else:
            self.verts = new_empty_verts()
            self.draw_count = 0

        if chunk_verts_translucent:
            chunk_verts_translucent.insert(0, self.verts)
            self.verts = numpy.concatenate(chunk_verts_translucent, 0)
            self.draw_count = int(self.verts.size // 10)
