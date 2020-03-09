from OpenGL.GL import *
import numpy
from . import new_empty_verts
from amulet_map_editor.opengl.shaders import get_shader


class TriMesh:
    """The base class for a triangular face mesh.
    Implements the base logic to set up and unload OpenGL."""
    def __init__(self, context_identifier: str):
        """Create a new TriMesh.
        The object can be created from another thread so OpenGL
        variables cannot be set from here"""
        self._context_identifier = context_identifier  # a string identifier unique to the context
        self._vao = None  # vertex array object
        self._vbo = None  # vertex buffer object
        self._shader = None  # the shader program
        self._trm_mat_loc = None  # the reference within the shader program of the transformation matrix
        self._verts = new_empty_verts()  # the vertices to draw
        self._draw_count = 0  # the number of vertices to draw

    @property
    def draw_mode(self):
        return GL_STATIC_DRAW

    @property
    def shader(self):
        if self._shader is None:
            self._shader = get_shader(self._context_identifier, 'render_chunk')
        return self._shader

    @property
    def transform_location(self):
        if self._trm_mat_loc is None:
            self._trm_mat_loc = glGetUniformLocation(self.shader, "transformation_matrix")
        return self._trm_mat_loc

    def _setup(self):
        """Setup OpenGL attributes if required"""
        if self._vao is None:  # if the opengl state has not been set
            self._vao = glGenVertexArrays(1)  # create the array
            self._vbo = glGenBuffers(1)  # and the buffer
            self._change_verts()
            self._setup_opengl_attrs()
            glBindVertexArray(0)

    def _setup_opengl_attrs(self):
        """Set up OpenGL vertex attributes"""
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

    def _change_verts(self):
        """Modify the vertices in OpenGL"""
        glBindVertexArray(self._vao)
        glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
        glBufferData(GL_ARRAY_BUFFER, self._verts.size * 4, self._verts, self.draw_mode)

    def unload(self):
        """Unload all opengl data"""
        if self._vao is not None:
            glDeleteVertexArrays(1, self._vao)
            glDeleteBuffers(1, self._vbo)
            self._vao = None
            self._vbo = None

    def draw(self, transformation_matrix: numpy.ndarray):
        self._setup()
        glUseProgram(self.shader)
        glUniformMatrix4fv(self.transform_location, 1, GL_FALSE, transformation_matrix)
        glBindVertexArray(self._vao)
        glDrawArrays(GL_TRIANGLES, 0, self._draw_count)
