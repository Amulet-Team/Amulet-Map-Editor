from OpenGL.GL import *
import numpy
from typing import TYPE_CHECKING, Dict, Tuple, Generator, Union
import math
import itertools

from amulet_renderer import shaders

from amulet.api.errors import ChunkDoesNotExist
if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet.api.chunk import Chunk
import minecraft_model_reader


class RenderWorld:
    def __init__(self, world: 'World', resource_pack: minecraft_model_reader.JavaRPHandler):
        self.world = world
        self.projection = [45.0, 4/3, 0.1, 1000.0]
        self.camera_location = [1, 0, 0]
        self.camera_rotation = [0, 0]
        self.render_distance = 10
        self._loaded_render_chunks: Dict[Tuple[int, int], Union['RenderChunk', None]] = {}
        self.shaders = {
            'render_chunk': shaders.load_shader('render_chunk')
        }
        self.resource_pack = resource_pack
        self.block_models = []
        self.resource_pack_translator = self.world.world_wrapper.translation_manager.get_sub_version('java', (1, 13, 2), force_blockstate=True)

    def get_model(self, pallete_index: int):
        if len(self.world.palette) > len(self.block_models):
            for block_index in range(len(self.block_models), len(self.world.palette)):
                self.block_models.append(
                    self.resource_pack.get_model(
                        self.resource_pack_translator.from_universal(
                            self.world.palette[block_index]
                        )[0]
                    )
                )

        return self.block_models[pallete_index]

    @property
    def transformation_matrix(self) -> numpy.ndarray:
        # camera translation
        transformation_matrix = numpy.eye(4, dtype=numpy.float64)
        transformation_matrix[3, :3] = numpy.array(self.camera_location) * -1

        theta = math.radians(self.camera_rotation[1])
        c = math.cos(theta)
        s = math.sin(theta)

        y_rot = numpy.array(
            [
                [c, 0, -s, 0],
                [0, 1, 0, 0],
                [s, 0, c, 0],
                [0, 0, 0, 1]
            ],
            dtype=numpy.float64
        )

        transformation_matrix = numpy.matmul(transformation_matrix, y_rot)

        # rotations
        theta = math.radians(self.camera_rotation[0])
        c = math.cos(theta)
        s = math.sin(theta)

        x_rot = numpy.array(
            [
                [1, 0, 0, 0],
                [0, c, s, 0],
                [0, -s, c, 0],
                [0, 0, 0, 1]
            ],
            dtype=numpy.float64
        )

        transformation_matrix = numpy.matmul(transformation_matrix, x_rot)

        # camera projection
        fovy, aspect, z_near, z_far = self.projection
        fovy = math.radians(fovy)
        f = 1 / math.tan(fovy / 2)
        projection = numpy.array(
            [
                [f/aspect, 0, 0, 0],
                [0, f, 0, 0],
                [0, 0, (z_far+z_near)/(z_near-z_far), -1],
                [0, 0, (2*z_far*z_near)/(z_near-z_far), 0]
            ],
            dtype=numpy.float64
        )

        transformation_matrix = numpy.matmul(transformation_matrix, projection)

        return transformation_matrix

    def _get_render_chunk(self, chunk_coords: Tuple[int, int]) -> Union['RenderChunk', None]:
        if chunk_coords not in self._loaded_render_chunks:
            try:
                chunk = self.world.get_chunk(*chunk_coords)
            except ChunkDoesNotExist:
                self._loaded_render_chunks[chunk_coords] = None
            else:
                self._loaded_render_chunks[chunk_coords] = RenderChunk(self, chunk_coords, chunk)  # TODO: get the chunk data from the world
        return self._loaded_render_chunks[chunk_coords]

    def chunk_coords(self) -> Generator[Tuple[int, int], None, None]:
        """Get all of the chunks to draw/load"""
        x, z = self.camera_location[0] // 16, self.camera_location[2] // 16
        chunks = itertools.product(
            range(x-self.render_distance, x+self.render_distance),
            range(z-self.render_distance, z+self.render_distance)
        )

        for chunk in sorted(chunks, key=lambda c: (c[0]-x)**2 + (c[1]-x)**2):
            yield chunk

    def draw(self, transformation_matrix):
        # draw all chunks within render distance
        load_chunks = []
        for chunk_coords in self.chunk_coords():
            if chunk_coords in self._loaded_render_chunks:
                chunk = self._loaded_render_chunks[chunk_coords]
                if chunk is None:
                    continue
                chunk.draw(transformation_matrix)
            else:
                load_chunks.append(chunk_coords)

        # generate chunks
        if load_chunks:
            self._get_render_chunk(load_chunks[0])


class RenderChunk:
    def __init__(self, render_world: RenderWorld, chunk_coords: Tuple[int, int], chunk: 'Chunk'):
        # the chunk geometry is stored in chunk space (floating point)
        # at shader time it is transformed by the players transform
        self.render_world = render_world
        self.coords = chunk_coords
        self.chunk = chunk
        self.vao = glGenVertexArrays(1)
        self.chunk_verts: numpy.ndarray = None
        self.chunk_faces: numpy.ndarray = None

        self.create_lod0()
        self.create_geometry()

    @property
    def cx(self):
        return self.coords[0]

    @property
    def cz(self):
        return self.coords[1]

    def create_lod0(self):
        world = self.render_world.world

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

            except:
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

        show_map = {'up': show_up, 'down': show_down, 'north': show_north, 'south': show_south, 'east': show_east, 'west': show_west}

        chunk_verts = []
        chunk_faces = []
        vert_offset = 0

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
                verts = model.verts[cull_dir]
                # duplicate the vertices for each block
                vert_list_ = numpy.tile(verts, (block_count, 1))
                # offset the model verts to chunk space TODO: there might be a better way to do this
                for axis in range(3):
                    vert_list_[:, axis::3] += block_offsets[:, axis].reshape((-1, 1))

                vert_table = numpy.hstack((
                    vert_list_.reshape((-1, 3)),
                    numpy.tile(
                        model.texture_coords[cull_dir].reshape((-1, 2)),
                        (block_count, 1)
                    )
                )).astype(numpy.float32)
                chunk_verts.append(vert_table)
                for _ in range(block_count):
                    chunk_faces.append(
                        model.faces[cull_dir].reshape((-1, 3)) + vert_offset
                    )
                    vert_offset += verts.size // 3

        if len(chunk_faces) == 0:
            self.chunk_verts = numpy.zeros((0, 5), dtype=numpy.float32)
            self.chunk_faces = numpy.zeros((0, 3), dtype=numpy.uint32)
        else:
            self.chunk_verts = numpy.concatenate(chunk_verts, 0).ravel()
            self.chunk_faces = numpy.concatenate(chunk_faces, 0).ravel()


                # texture = model.texture_index[cull_dir]
                # TODO: not all faces in the same model have the same texture
                # cur_texture = model.textures[texture[0]]
                # if not self.render_world.texture_exists(cur_texture):
                #     self.queue.put(("texture", (self.cx, self.cz), self.render_id, cur_texture))
                #     self.render_world.queued_textures.append(cur_texture)
                # self.queue.put((
                #     "vertices",
                #     (self.cx, self.cz),
                #     self.render_id,
                #     cur_texture,
                #     vert_list_,
                #     block_count,
                #     model.texture_coords[cull_dir][0::2],
                #     model.texture_coords[cull_dir][1::2]
                # ))

    def create_geometry(self):
        glBindVertexArray(self.vao)
        vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, self.chunk_verts.size * 4, self.chunk_verts, GL_STATIC_DRAW)
        # vertex attribute pointers
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        # texture coords attribute pointers
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 20, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)

        ivbo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ivbo)
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, self.chunk_faces.size * 4, self.chunk_faces, GL_STATIC_DRAW)

        glBindVertexArray(0)


    def create_geometry_(self):
        # geometry will include
        # vertex coords (in chunk space)
        # texture coords
        # perhaps in the future (if face merging is added) a way to specify texture bounds
        # normals

        # triangle   vertices      colors
        triangle = [
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
            -0.5 + 0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
            -0.5 + 0.0, 0.5, 0.0, 0.0, 0.0, 1.0
        ]

        triangle = numpy.array(triangle, dtype=numpy.float32)

        glBindVertexArray(self.vao)
        vbo = glGenBuffers(1)


        glBindBuffer(GL_ARRAY_BUFFER, vbo)
        glBufferData(GL_ARRAY_BUFFER, len(triangle) * 4, triangle, GL_STATIC_DRAW)

        # vertex attribute pointers
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        # color attribute pointers
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)
        glBindVertexArray(0)

    def draw(self, transformation_matrix: numpy.ndarray):
        shader = self.render_world.shaders['render_chunk']
        glUseProgram(shader)

        chunk_translation = numpy.eye(4, dtype=numpy.float64)
        chunk_translation[3, [0, 2]] = numpy.array(self.coords) * 16

        transformation_matrix = numpy.matmul(chunk_translation, transformation_matrix)

        trm_mat_loc = glGetUniformLocation(shader, "transformation_matrix")
        glUniformMatrix4fv(trm_mat_loc, 1, GL_FALSE, transformation_matrix.astype(numpy.float32))

        glBindVertexArray(self.vao)
        glDrawElements(GL_TRIANGLES, self.chunk_faces.size, GL_UNSIGNED_INT, ctypes.c_void_p(0))

