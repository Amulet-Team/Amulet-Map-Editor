from OpenGL.GL import *
import numpy
from typing import TYPE_CHECKING, Dict, Tuple, Generator, Union
import math
from concurrent.futures import ThreadPoolExecutor

from ..amulet_renderer import shaders

from amulet.api.errors import ChunkLoadError
if TYPE_CHECKING:
    from amulet.api.world import World
    from amulet.api.chunk import Chunk
import minecraft_model_reader
from ..amulet_renderer import textureatlas


def sin(theta: Union[int, float]) -> float:
    return math.sin(math.radians(theta))


def cos(theta: Union[int, float]) -> float:
    return math.cos(math.radians(theta))


class ChunkGenerator(ThreadPoolExecutor):
    def __init__(self):
        super().__init__(max_workers=1)
        self._count = 0  # the number of chunks being generated
        self._max_count = 4

    def _gen_chunk(self, method, chunk):
        method(chunk)
        self._count -= 1

    def submit_chunk(self, method, chunk):
        if self._count < self._max_count:
            self._count += 1
            self.submit(self._gen_chunk, method, chunk)


class RenderWorld:
    def __init__(self, world: 'World', resource_pack: minecraft_model_reader.JavaRPHandler):
        self._world = world
        self._projection = [70.0, 4 / 3, 0.1, 1000.0]
        self._camera = [0, 300, 0, 90, 0]
        self._camera_move_speed = 5
        self._camera_rotate_speed = 2

        self._render_distance = 10
        self._garbage_distance = 20
        self._loaded_render_chunks: Dict[Tuple[int, int], Union['RenderChunk', None]] = {}
        self._chunk_generator = ChunkGenerator()
        self._shaders = {
            'render_chunk': shaders.load_shader('render_chunk')
        }
        self._resource_pack = resource_pack
        self._block_models = {}
        self._texture_bounds = {}
        self._resource_pack_translator = self._world.world_wrapper.translation_manager.get_version('java', (1, 15, 2))
        self._texture_atlas = None
        self._gl_texture_atlas = glGenTextures(1)
        self._create_atlas()

    def is_closeable(self):
        return True

    def close(self):
        self.run_garbage_collector(True)

    def _create_atlas(self):
        print('Creating texture atlas')
        # filename = str(hash(tuple(self._resource_pack.pack_paths)))
        # ext = 'png'

        self._texture_atlas, self._texture_bounds, width, height = textureatlas.create_atlas(self._resource_pack.textures)

        glBindTexture(GL_TEXTURE_2D, self._gl_texture_atlas)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, self._texture_atlas)

        print('Finished creating texture atlas')

    def move_camera(self, forward, up, right, pitch, yaw):
        self._camera[0] += self._camera_move_speed * (cos(self._camera[4]) * right + cos(self._camera[3]) * sin(self._camera[4]) * forward)
        self._camera[1] += self._camera_move_speed * (up - sin(self._camera[3]) * forward)
        self._camera[2] += self._camera_move_speed * (sin(self._camera[4]) * right - cos(self._camera[3]) * cos(self._camera[4]) * forward)

        self._camera[3] += self._camera_rotate_speed * pitch
        if not -90 <= self._camera[3] <= 90:
            self._camera[3] = max(min(self._camera[3], 90), -90)
        self._camera[4] += self._camera_rotate_speed * yaw

    @property
    def camera_move_speed(self) -> float:
        """The speed that the camera moves at"""
        return self._camera_move_speed

    @camera_move_speed.setter
    def camera_move_speed(self, val: float):
        self._camera_move_speed = val

    @property
    def camera_rotate_speed(self) -> float:
        """The speed that the camera rotates at"""
        return self._camera_rotate_speed

    @camera_rotate_speed.setter
    def camera_rotate_speed(self, val: float):
        self._camera_rotate_speed = val

    @property
    def render_distance(self) -> int:
        """The distance to render chunks around the camera"""
        return self._render_distance

    @render_distance.setter
    def render_distance(self, val: int):
        assert isinstance(val, int), 'Render distance must be an int'
        self._render_distance = val

    @property
    def garbage_distance(self) -> int:
        """The distance outside which chunks should be unloaded"""
        return self._garbage_distance

    @garbage_distance.setter
    def garbage_distance(self, val: int):
        assert isinstance(val, int), 'garbage distance must be an int'
        self._garbage_distance = val

    @property
    def resource_pack(self) -> minecraft_model_reader.JavaRPHandler:
        """The resource pack being used by the renderer"""
        return self._resource_pack

    @resource_pack.setter
    def resource_pack(self, val: minecraft_model_reader.JavaRPHandler):
        raise NotImplementedError
        # TODO: implement a way to reload all chunks with a new resource pack
        # self._resource_pack = val

    @property
    def fov(self) -> float:
        return self._projection[0]

    @fov.setter
    def fov(self, fov: float):
        self._projection[0] = fov

    @property
    def aspect_ratio(self) -> float:
        return self._projection[1]

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio: float):
        self._projection[1] = aspect_ratio

    def get_texture_bounds(self, texture):
        if texture not in self._texture_bounds:
            texture = ('minecraft', 'missing_no')
        return self._texture_bounds[texture]

    def get_model(self, pallete_index: int):
        if pallete_index not in self._block_models:
            self._block_models[pallete_index] = self._resource_pack.get_model(
                self._resource_pack_translator.block.from_universal(
                    self._world.palette[pallete_index]
                )[0]
            )

        return self._block_models[pallete_index]

    @property
    def transformation_matrix(self) -> numpy.ndarray:
        # camera translation
        transformation_matrix = numpy.eye(4, dtype=numpy.float64)
        transformation_matrix[3, :3] = numpy.array(self._camera[:3]) * -1

        theta = math.radians(self._camera[4])
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
        theta = math.radians(self._camera[3])
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
        fovy, aspect, z_near, z_far = self._projection
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
                chunk = self._world.get_chunk(*chunk_coords)
            except ChunkLoadError:
                self._loaded_render_chunks[chunk_coords] = None
            else:
                self._loaded_render_chunks[chunk_coords] = RenderChunk(self, chunk_coords, chunk)
        return self._loaded_render_chunks[chunk_coords]

    def chunk_coords(self) -> Generator[Tuple[int, int], None, None]:
        """Get all of the chunks to draw/load"""
        cx, cz = int(self._camera[0]) >> 4, int(self._camera[2]) >> 4

        sign = 1
        length = 1
        for _ in range(self.render_distance*2+1):
            for _ in range(length):
                yield cx, cz
                cx += sign
            for _ in range(length):
                yield cx, cz
                cz += sign
            sign *= -1
            length += 1

    def draw(self):
        transformation_matrix = self.transformation_matrix
        # draw all chunks within render distance
        gen_chunks = []
        for chunk_coords in self.chunk_coords():
            if chunk_coords in self._loaded_render_chunks:
                chunk = self._loaded_render_chunks[chunk_coords]
                if chunk is None:
                    continue
                chunk.draw(transformation_matrix)
            else:
                gen_chunks.append(chunk_coords)

        for chunk_coords in gen_chunks:
            self._chunk_generator.submit_chunk(self._get_render_chunk, chunk_coords)

    def run_garbage_collector(self, remove_all=False):
        camx, camz = self._camera[0]//16, self._camera[2]//16
        remove = []
        for (cx, cz), chunk in list(self._loaded_render_chunks.items()):
            if remove_all or max(abs(cx-camx), abs(cz-camz)) > self.garbage_distance:
                if chunk is not None:
                    chunk.delete()
                    remove.append((cx, cz))
        for coord in remove:
            del self._loaded_render_chunks[coord]


class RenderChunk:
    def __init__(self, render_world: RenderWorld, chunk_coords: Tuple[int, int], chunk: 'Chunk'):
        # the chunk geometry is stored in chunk space (floating point)
        # at shader time it is transformed by the players transform
        self.render_world = render_world
        self.coords = chunk_coords
        self.chunk = chunk
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

    def create_geometry(self):
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

    def draw(self, transformation_matrix: numpy.ndarray):
        self._setup()
        shader = self.render_world._shaders['render_chunk']

        glUseProgram(shader)

        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self.render_world._gl_texture_atlas)
        glUniform1i(glGetUniformLocation(shader, 'image'), 0)

        chunk_translation = numpy.eye(4, dtype=numpy.float64)
        chunk_translation[3, [0, 2]] = numpy.array(self.coords) * 16

        transformation_matrix = numpy.matmul(chunk_translation, transformation_matrix)

        trm_mat_loc = glGetUniformLocation(shader, "transformation_matrix")
        glUniformMatrix4fv(trm_mat_loc, 1, GL_FALSE, transformation_matrix.astype(numpy.float32))

        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, self._draw_count)

    def delete(self):
        if self.vao is not None:
            glDeleteVertexArrays(1, self.vao)
            self.vao = None

