from OpenGL.GL import *
from amulet_renderer import shaders
import numpy
from typing import TYPE_CHECKING, Dict, Tuple
if TYPE_CHECKING:
    from amulet.api.world import World
import random


class RenderWorld:
    def __init__(self, world: 'World'):
        self.world = world
        self.camera_matrix = None
        self.loaded_render_chunks: Dict[Tuple[int, int], 'RenderChunk'] = {
            (0, 0): RenderChunk(),
            (0, 1): RenderChunk()
        }

    def draw(self):
        # draw all chunks within render distance
        for chunk in self.loaded_render_chunks.values():
            chunk.draw()

        # generate chunks


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

