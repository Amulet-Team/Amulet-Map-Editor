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


class RenderWorld:
    def __init__(self, world: 'World'):
        self.world = world
        self.projection = [45.0, 4/3, 0.1, 1000.0]
        self.camera_location = [1, 0, 0]
        self.camera_rotation = [0, 0]
        self.render_distance = 10
        self._loaded_render_chunks: Dict[Tuple[int, int], Union['RenderChunk', None]] = {}
        self.shaders = {
            'render_chunk': shaders.load_shader('render_chunk')
        }

    @property
    def transformation_matrix(self) -> numpy.ndarray:
        # camera translation
        transformation_matrix = numpy.eye(4, dtype=numpy.float64)
        transformation_matrix[3, :3] = numpy.array(self.camera_location) * -1

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
        self.create_geometry()

    def create_geometry(self):
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
        glDrawArrays(GL_TRIANGLES, 0, 3)

