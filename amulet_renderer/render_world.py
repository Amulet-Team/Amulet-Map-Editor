from OpenGL.GL import *
import numpy
from typing import TYPE_CHECKING, Dict, Tuple, Generator
if TYPE_CHECKING:
    from amulet.api.world import World
import random
import itertools

from amulet_renderer import shaders


class RenderWorld:
    def __init__(self, world: 'World'):
        self.world = world
        self.camera_location = (0, 0, 0)
        self.render_distance = 10
        self._loaded_render_chunks: Dict[Tuple[int, int], 'RenderChunk'] = {}

    def _get_render_chunk(self, chunk_coords: Tuple[int, int]) -> 'RenderChunk':
        if not chunk_coords in self._loaded_render_chunks:
            self._loaded_render_chunks[chunk_coords] = RenderChunk()  # TODO: get the chunk data from the world
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

    def draw(self):
        # draw all chunks within render distance
        load_chunks = []
        for chunk_coords in self.chunk_coords():
            if chunk_coords in self._loaded_render_chunks:
                chunk = self._loaded_render_chunks[chunk_coords]
                chunk.draw()
            else:
                load_chunks.append(chunk_coords)

        # generate chunks
        if load_chunks:
            self._loaded_render_chunks[load_chunks[0]] = RenderChunk()


class RenderChunk:
    def __init__(self):
        # the chunk geometry is stored in chunk space (floating point)
        # at shader time it is transformed by the players transform

        self.main_shader = shaders.load_shader('render_chunk')
        self.vao = glGenVertexArrays(1)
        self.create_geometry()

    def create_geometry(self):
        # geometry will include
        # vertex coords (in chunk space)
        # texture coords
        # perhaps in the future (if face merging is added) a way to specify texture bounds
        # normals

        offset = random.random()
        print(offset)
        # triangle   vertices      colors
        triangle = [offset -0.5 + -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                    offset -0.5 + 0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                    offset -0.5 + 0.0, 0.5, 0.0, 0.0, 0.0, 1.0]

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

    def draw(self):
        glUseProgram(self.main_shader)
        glBindVertexArray(self.vao)
        glDrawArrays(GL_TRIANGLES, 0, 3)

