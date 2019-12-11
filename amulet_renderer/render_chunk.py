from OpenGL.GL import *
from amulet_renderer import shaders
import numpy


class RenderChunk:
    def __init__(self):
        self.main_shader = shaders.load_shader('render_chunk')
        self.create_geometry()

    def create_geometry(self):
        # triangle   vertices      colors
        triangle = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                    0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                    0.0, 0.5, 0.0, 0.0, 0.0, 1.0]

        triangle = numpy.array(triangle, dtype=numpy.float32)

        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, len(triangle) * 4, triangle, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)

        glClearColor(0.1, 0.15, 0.1, 1.0)

        glUseProgram(self.main_shader)
