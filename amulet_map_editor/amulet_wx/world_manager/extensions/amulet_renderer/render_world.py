from OpenGL.GL import *
import numpy
from typing import TYPE_CHECKING, Tuple, Generator, Union, Optional
import math
from concurrent.futures import ThreadPoolExecutor, Future
import time
import uuid
import weakref

from amulet_map_editor import log
from ..amulet_renderer import shaders

import minecraft_model_reader
from ..amulet_renderer import textureatlas
from .render_chunk import RenderChunk
from .render_region import ChunkManager
if TYPE_CHECKING:
    from amulet.api.world import World


def sin(theta: Union[int, float]) -> float:
    return math.sin(math.radians(theta))


def cos(theta: Union[int, float]) -> float:
    return math.cos(math.radians(theta))


class ChunkGenerator(ThreadPoolExecutor):
    def __init__(self, render_world: 'RenderWorld'):
        super().__init__(max_workers=1)
        self._render_world = weakref.ref(render_world)
        self._region_size = render_world.chunk_manager.region_size
        self._enabled = False
        self._generator: Optional[Future] = None

    def start(self):
        if self._enabled:
            raise Exception('ChunkGenerator started more than once')
        else:
            self._enabled = True
            self._generator = self.submit(self._generate_chunks)

    def stop(self):
        if self._enabled:
            self._enabled = False
            self._generator.result()

    def _generate_chunks(self):
        while self._enabled:
            chunk_coords = next(
                (
                    c for c in self._render_world().chunk_coords() if
                    c not in self._render_world().chunk_manager or
                    self._render_world().chunk_manager.render_chunk_needs_rebuild(c)
                ),
                None
            )
            if chunk_coords is None:
                time.sleep(1 / 30)
            else:
                chunk = RenderChunk(
                    self._render_world(),
                    self._region_size,
                    chunk_coords,
                    self._render_world().dimension
                )

                try:
                    chunk.create_geometry()
                except Exception as e:
                    log.error(f'Failed generating chunk geometry for chunk {chunk_coords}', exc_info=True)

                self._render_world().chunk_manager.add_render_chunk(
                    chunk
                )


class RenderWorld:
    def __init__(self, world: 'World', resource_pack: minecraft_model_reader.JavaRPHandler):
        self.identifier = str(uuid.uuid4())
        self._world = world
        self._projection = [70.0, 4 / 3, 0.1, 1000.0]
        self._camera = [0, 300, 0, 90, 0]
        self._dimension = 0
        self._camera_move_speed = 5
        self._camera_rotate_speed = 2

        self._render_distance = 10
        self._garbage_distance = 20
        # self._loaded_render_chunks: Dict[Tuple[int, int], Union[RenderChunk, None]] = {}
        self._chunk_manager = ChunkManager(self.identifier)
        self._resource_pack = resource_pack
        self._block_models = {}
        self._texture_bounds = {}
        self._resource_pack_translator = self._world.world_wrapper.translation_manager.get_version('java', (1, 15, 2))
        self._texture_atlas = None
        self._gl_texture_atlas = glGenTextures(1)
        self._create_atlas()
        self._chunk_generator = ChunkGenerator(self)

    @property
    def world(self) -> 'World':
        return self._world

    @property
    def chunk_manager(self) -> ChunkManager:
        return self._chunk_manager

    def is_closeable(self):
        return True

    def enable(self):
        self._chunk_generator.start()

    def disable(self):
        self._chunk_generator.stop()
        self.run_garbage_collector(True)

    def close(self):
        self.disable()
        glDeleteTextures([self._gl_texture_atlas])

    def _create_atlas(self):
        # filename = str(hash(tuple(self._resource_pack.pack_paths)))
        # ext = 'png'

        self._texture_atlas, self._texture_bounds, width, height = textureatlas.create_atlas(self._resource_pack.textures)

        glBindTexture(GL_TEXTURE_2D, self._gl_texture_atlas)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)

        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, self._texture_atlas)

        shader = shaders.get_shader(self.identifier, 'render_chunk')
        glUseProgram(shader)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self._gl_texture_atlas)
        glUniform1i(glGetUniformLocation(shader, 'image'), 0)

        log.info('Finished setting up texture atlas in OpenGL')

    def move_camera(self, forward, up, right, pitch, yaw):
        if (forward, up, right, pitch, yaw) == (0, 0, 0, 0, 0):
            return
        self._camera[0] += self._camera_move_speed * (cos(self._camera[4]) * right + sin(self._camera[4]) * forward)
        self._camera[1] += self._camera_move_speed * up
        self._camera[2] += self._camera_move_speed * (sin(self._camera[4]) * right - cos(self._camera[4]) * forward)

        self._camera[3] += self._camera_rotate_speed * pitch
        if not -90 <= self._camera[3] <= 90:
            self._camera[3] = max(min(self._camera[3], 90), -90)
        self._camera[4] += self._camera_rotate_speed * yaw

    @property
    def dimension(self) -> int:
        return self._dimension

    @dimension.setter
    def dimension(self, dimension: int):
        self._chunk_generator.stop()
        self._dimension = dimension
        self.run_garbage_collector(True)
        self._chunk_generator.start()

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
        transformation_matrix = numpy.eye(4, dtype=numpy.float32)
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
            dtype=numpy.float32
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
            dtype=numpy.float32
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
            dtype=numpy.float32
        )

        transformation_matrix = numpy.matmul(transformation_matrix, projection)

        return transformation_matrix

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
        self._chunk_manager.draw(self.transformation_matrix)

    def run_garbage_collector(self, remove_all=False):
        if remove_all:
            self._chunk_manager.unload()
            self._world.unload()
        else:
            safe_area = (
                self._dimension,
                self._camera[0]//16 - self.garbage_distance,
                self._camera[2]//16 - self.garbage_distance,
                self._camera[0]//16 + self.garbage_distance,
                self._camera[2]//16 + self.garbage_distance
            )
            self._chunk_manager.unload(safe_area[1:])
            self._world.unload(safe_area)
