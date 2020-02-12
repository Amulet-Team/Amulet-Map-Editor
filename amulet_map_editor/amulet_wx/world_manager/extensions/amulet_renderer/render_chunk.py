from OpenGL.GL import *
import numpy
from typing import TYPE_CHECKING, Tuple, Dict
import minecraft_model_reader
if TYPE_CHECKING:
    from .render_world import RenderWorld
    from amulet.api.errors import ChunkLoadError
    from amulet.api.chunk import Chunk


class RenderChunk:
    def __init__(self, render_world: RenderWorld, chunk_coords: Tuple[int, int], chunk: 'Chunk'):
        # the chunk geometry is stored in chunk space (floating point)
        # at shader time it is transformed by the players transform
        self.render_world = render_world
        self.coords = chunk_coords
        self.chunk_transform = numpy.eye(4, dtype=numpy.float32)
        self.chunk_transform[3, [0, 2]] = numpy.array(self.coords) * 16
        self.chunk = chunk
        self._shader = None
        self._trm_mat_loc = None
        self.vao = None
        self.chunk_verts: numpy.ndarray = None
        self._draw_count = 0
        self.create_lod0()

    def _setup(self):
        """Set up the opengl data which cannot be set up in another thread"""
        if self.vao is None:
            self.vao = glGenVertexArrays(1)
            self.create_geometry()

    @property
    def cx(self):
        return self.coords[0]

    @property
    def cz(self):
        return self.coords[1]

    def create_lod0(self):
        print(f'Creating geometry for chunk {self.cx} {self.cz}')
        world = self.render_world._world

        blocks: numpy.ndarray = self.chunk.blocks
        blocks_ = numpy.zeros(blocks.shape + numpy.array((2, 0, 2)), blocks.dtype)
        blocks_[1:-1, :, 1:-1] = blocks

        for dx, dz in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            try:
                blocks_temp: numpy.ndarray = world.get_chunk(self.cx + dx, self.cz + dz).blocks
                if (dx, dz) == (-1, 0):
                    blocks_[0, :, 1:-1] = blocks_temp[-1, :, :]
                elif (dx, dz) == (1, 0):
                    blocks_[-1, :, 1:-1] = blocks_temp[0, :, :]
                elif (dx, dz) == (0, -1):
                    blocks_[1:-1, :, 0] = blocks_temp[:, :, -1]
                elif (dx, dz) == (0, 1):
                    blocks_[1:-1, :, -1] = blocks_temp[:, :, 0]

            except ChunkLoadError:
                continue

        models: Dict[int, minecraft_model_reader.MinecraftMesh] = {
            block_temp_id: self.render_world.get_model(block_temp_id) for block_temp_id in numpy.unique(blocks_)
        }
        is_transparrent = [block_temp_id for block_temp_id, model in models.items() if not model.is_opaque]
        is_transparrent_array = numpy.isin(blocks_, is_transparrent)

        show_up = numpy.ones(blocks.shape, dtype=numpy.bool)
        show_down = numpy.ones(blocks.shape, dtype=numpy.bool)
        show_up[:, :-1, :] = is_transparrent_array[1:-1, 1:, 1:-1]
        show_down[:, 1:, :] = is_transparrent_array[1:-1, :-1, 1:-1]
        show_north = is_transparrent_array[1:-1, :, :-2]
        show_south = is_transparrent_array[1:-1, :, 2:]
        show_east = is_transparrent_array[2:, :, 1:-1]
        show_west = is_transparrent_array[:-2, :, 1:-1]

        show_map = {
            'up': show_up,
            'down': show_down,
            'north': show_north,
            'south': show_south,
            'east': show_east,
            'west': show_west
        }

        chunk_verts = []

        for block_temp_id in numpy.unique(blocks):
            # for each unique blockstate in the chunk
            # get the model and the locations of the blocks
            model: minecraft_model_reader.MinecraftMesh = models[block_temp_id]
            all_block_locations = numpy.argwhere(blocks == block_temp_id)
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
                    if len(block_locations) == 0:
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
                vert_table = numpy.zeros((block_count, faces.size, 9), dtype=numpy.float32)
                vert_table[:, :, :3] = verts[faces] + block_offsets[:, :].reshape((-1, 1, 3))
                vert_table[:, :, 3:5] = tverts[faces]

                vert_index = 0
                for texture_index in model.texture_index[cull_dir]:
                    tex_bounds = self.render_world.get_texture_bounds(
                        model.textures[texture_index]
                    )

                    vert_table[:, vert_index:vert_index+3, 5:9] = tex_bounds
                    vert_index += 3

                chunk_verts.append(vert_table.ravel())

        if len(chunk_verts) == 0:
            self.chunk_verts = numpy.zeros((0, 9), dtype=numpy.float32)
            self._draw_count = 0
        else:
            self.chunk_verts = numpy.concatenate(chunk_verts, 0).ravel()
            self._draw_count = int(self.chunk_verts.size // 9)
        print(f'Finished creating geometry for chunk {self.cx} {self.cz}')

    def create_geometry(self):
        print(f'Setting up opengl for chunk {self.cx} {self.cz}')
        glBindVertexArray(self.vao)
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, self.chunk_verts.size * 4, self.chunk_verts, GL_STATIC_DRAW)
        # vertex attribute pointers
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 36, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        # texture coords attribute pointers
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 36, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)
        # texture coords attribute pointers
        glVertexAttribPointer(2, 4, GL_FLOAT, GL_FALSE, 36, ctypes.c_void_p(20))
        glEnableVertexAttribArray(2)

        glBindVertexArray(0)

        self._shader = self.render_world.shaders['render_chunk']
        self._trm_mat_loc = glGetUniformLocation(self._shader, "transformation_matrix")
        print(f'Finished setting up opengl for chunk {self.cx} {self.cz}')

    def draw(self, transformation_matrix: numpy.ndarray):
        self._setup()
        glUseProgram(self._shader)
        transformation_matrix = numpy.matmul(self.chunk_transform, transformation_matrix)
        glUniformMatrix4fv(self._trm_mat_loc, 1, GL_FALSE, transformation_matrix)
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, self._draw_count)

    def delete(self):
        if self.vao is not None:
            glDeleteVertexArrays(1, self.vao)
            self.vao = None
