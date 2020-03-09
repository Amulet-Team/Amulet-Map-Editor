from OpenGL.GL import *
import numpy
from typing import TYPE_CHECKING, Tuple, Dict
import weakref

import minecraft_model_reader
from amulet.api.errors import ChunkLoadError, ChunkDoesNotExist
from amulet_map_editor.opengl import shaders

if TYPE_CHECKING:
    from .render_world import RenderWorld
    from amulet.api.chunk import Chunk


def new_empty_verts() -> numpy.ndarray:
    return numpy.zeros(0, dtype=numpy.float32)


class RenderChunk:
    def __init__(self, render_world: 'RenderWorld', region_size: int, chunk_coords: Tuple[int, int], dimension: int):
        # the chunk geometry is stored in chunk space (floating point)
        # at shader time it is transformed by the players transform
        self._render_world = weakref.ref(render_world)
        self._region_size = region_size
        self._coords = chunk_coords
        self._dimension = dimension
        self._chunk_state = 0  # 0 = chunk does not exist, 1 = chunk exists but failed to load, 2 = chunk exists
        self._changed_time = 0
        self._shader = None
        self._trm_mat_loc = None
        self._vao = None
        self._rebuild = True
        self.chunk_lod0: numpy.ndarray = new_empty_verts()
        self.chunk_lod0_translucent = 0  # the offset into the above from which the faces can be translucent
        self.chunk_lod1: numpy.ndarray = new_empty_verts()
        self._draw_count = 0

    def __repr__(self):
        return f'RenderChunk({self._coords[0]}, {self._coords[1]})'

    def _setup(self):
        """Set up the opengl data which cannot be set up in another thread"""
        if self._vao is None:
            self._vao = glGenVertexArrays(1)
        if self._rebuild:
            self._setup_opengl()
            self._rebuild = False

    @property
    def dimension(self) -> int:
        return self._dimension

    @property
    def cx(self) -> int:
        return self._coords[0]

    @property
    def cz(self) -> int:
        return self._coords[1]

    @property
    def coords(self) -> Tuple[int, int]:
        return self._coords

    @property
    def chunk(self) -> "Chunk":
        return self._render_world().world.get_chunk(*self._coords, self._dimension)

    @property
    def chunk_state(self) -> int:
        return self._chunk_state

    def needs_rebuild(self):
        """has the chunk data changed since the last rebuild"""
        try:
            chunk = self.chunk
        except ChunkDoesNotExist:
            chunk_state = 0
        except ChunkLoadError:
            chunk_state = 1
        else:
            chunk_state = 2
            if chunk.changed_time != self._changed_time:
                return True
        return chunk_state != self._chunk_state

    def _get_block_data(self, chunk: "Chunk") -> Tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]:
        """Given a Chunk object will return the chunk arrays needed to generate geometry
        :returns: block array of the chunk, block array one block larger than the chunk, array of unique blocks"""
        blocks: numpy.ndarray = chunk.blocks
        larger_blocks = numpy.zeros(blocks.shape + numpy.array((2, 0, 2)), blocks.dtype)
        larger_blocks[1:-1, :, 1:-1] = blocks

        for dx, dz in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            try:
                blocks_temp: numpy.ndarray = self._render_world().world.get_chunk(self.cx + dx, self.cz + dz).blocks
                if (dx, dz) == (-1, 0):
                    larger_blocks[0, :, 1:-1] = blocks_temp[-1, :, :]
                elif (dx, dz) == (1, 0):
                    larger_blocks[-1, :, 1:-1] = blocks_temp[0, :, :]
                elif (dx, dz) == (0, -1):
                    larger_blocks[1:-1, :, 0] = blocks_temp[:, :, -1]
                elif (dx, dz) == (0, 1):
                    larger_blocks[1:-1, :, -1] = blocks_temp[:, :, 0]

            except ChunkLoadError:
                continue

        unique_blocks = numpy.unique(larger_blocks)
        return blocks, larger_blocks, unique_blocks

    def create_geometry(self):
        try:
            chunk = self.chunk
        except ChunkDoesNotExist:
            self._create_empty_geometry()
            self._chunk_state = 0
        except ChunkLoadError:
            # log.info(f'Error loading chunk {chunk_coords}', exc_info=True)
            self._create_error_geometry()
            self._chunk_state = 1
        else:
            self._changed_time = chunk.changed_time
            self._chunk_state = 2
            blocks, larger_blocks, unique_blocks = self._get_block_data(chunk)
            self._create_lod0(blocks, larger_blocks, unique_blocks)
        self._rebuild = True

    def _create_empty_geometry(self):
        self.chunk_lod0: numpy.ndarray = new_empty_verts()
        self.chunk_lod1: numpy.ndarray = new_empty_verts()

    def _create_error_geometry(self):
        # TODO
        self.chunk_lod0: numpy.ndarray = new_empty_verts()
        self.chunk_lod1: numpy.ndarray = new_empty_verts()

    def _create_lod0(self, blocks: numpy.ndarray, larger_blocks: numpy.ndarray, unique_blocks: numpy.ndarray):
        transparent_array = numpy.zeros(larger_blocks.shape, dtype=numpy.uint8)
        models: Dict[int, minecraft_model_reader.MinecraftMesh] = {}
        for block_temp_id in unique_blocks:
            model = models[block_temp_id] = self._render_world().get_model(block_temp_id)
            transparent_array[larger_blocks == block_temp_id] = model.is_transparent

        def get_transparent_array(offset_transparent_array, transparent_array):
            return numpy.logical_and(
                offset_transparent_array,  # if the next block is transparent
                numpy.logical_not(  # but is not the same block with transparency mode 1
                    (offset_transparent_array == 1) * (offset_transparent_array == transparent_array)
                )
            )

        show_up = numpy.ones(blocks.shape, dtype=numpy.bool)
        show_down = numpy.ones(blocks.shape, dtype=numpy.bool)
        show_up[:, :-1, :] = get_transparent_array(transparent_array[1:-1, 1:, 1:-1], transparent_array[1:-1, :-1, 1:-1])
        show_down[:, 1:, :] = get_transparent_array(transparent_array[1:-1, :-1, 1:-1], transparent_array[1:-1, 1:, 1:-1])
        show_north = get_transparent_array(transparent_array[1:-1, :, :-2], transparent_array[1:-1, :, 1:-1])
        show_south = get_transparent_array(transparent_array[1:-1, :, 2:], transparent_array[1:-1, :, 1:-1])
        show_east = get_transparent_array(transparent_array[2:, :, 1:-1], transparent_array[1:-1, :, 1:-1])
        show_west = get_transparent_array(transparent_array[:-2, :, 1:-1], transparent_array[1:-1, :, 1:-1])

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
                vert_table[:, :, :3] = verts[faces] + \
                                       block_offsets[:, :].reshape((-1, 1, 3)) + \
                                       16 * (numpy.array([self._coords[0], 0, self._coords[1]]) % self._region_size)
                vert_table[:, :, 3:5] = tverts[faces]

                vert_index = 0
                for texture_index in model.texture_index[cull_dir]:
                    tex_bounds = self._render_world().get_texture_bounds(
                        model.textures[texture_index]
                    )

                    vert_table[:, vert_index:vert_index+3, 5:9] = tex_bounds
                    vert_index += 3

                vert_table[:, :, 9] = model.tint_verts[cull_dir][faces]

                if model.is_transparent == 1:
                    chunk_verts_translucent.append(vert_table.ravel())
                else:
                    chunk_verts.append(vert_table.ravel())

        if chunk_verts:
            self.chunk_lod0 = numpy.concatenate(chunk_verts, 0)
            self._draw_count = int(self.chunk_lod0.size // 10)
            self.chunk_lod0_translucent = self.chunk_lod0.size
        else:
            self.chunk_lod0 = new_empty_verts()
            self._draw_count = 0

        if chunk_verts_translucent:
            chunk_verts_translucent.insert(0, self.chunk_lod0)
            self.chunk_lod0 = numpy.concatenate(chunk_verts_translucent, 0)
            self._draw_count = int(self.chunk_lod0.size // 10)

    def _create_lod1(self, blocks: numpy.ndarray, larger_blocks: numpy.ndarray, unique_blocks: numpy.ndarray):
        # TODO
        self.chunk_lod0: numpy.ndarray = new_empty_verts()
        self.chunk_lod1: numpy.ndarray = new_empty_verts()

    def _setup_opengl(self):
        glBindVertexArray(self._vao)
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, self.chunk_lod0.size * 4, self.chunk_lod0, GL_STATIC_DRAW)
        # vertex attribute pointers
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        # texture coords attribute pointers
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)
        # texture coords attribute pointers
        glVertexAttribPointer(2, 4, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(20))
        glEnableVertexAttribArray(2)
        # tint value
        glVertexAttribPointer(3, 1, GL_FLOAT, GL_FALSE, 40, ctypes.c_void_p(36))
        glEnableVertexAttribArray(3)

        glBindVertexArray(0)

        self._shader = shaders.get_shader(self._render_world().identifier, 'render_chunk')
        self._trm_mat_loc = glGetUniformLocation(self._shader, "transformation_matrix")

    def draw(self, transformation_matrix: numpy.ndarray):
        self._setup()
        glUseProgram(self._shader)
        glUniformMatrix4fv(self._trm_mat_loc, 1, GL_FALSE, transformation_matrix)
        glBindVertexArray(self._vao)
        glDrawArrays(GL_TRIANGLES, 0, self._draw_count)

    def unload(self):
        if self._vao is not None:
            glDeleteVertexArrays(1, self._vao)
            self._vao = None
