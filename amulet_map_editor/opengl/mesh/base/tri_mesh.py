from OpenGL.GL import *
import numpy
from amulet_map_editor.opengl.mesh import new_empty_verts
from amulet_map_editor.opengl.shaders import get_shader


class TriMesh:
    """The base class for a triangular face mesh.
    Implements the base logic to set up and unload OpenGL."""
    _vertex_attrs = (
        3,  # vertex attribute pointers
        2,  # texture coords attribute pointers
        4,  # texture coords attribute pointers
        3,  # tint value (also shading)
    )
    _vert_len = sum(_vertex_attrs)

    def __init__(self, context_identifier: str):
        """Create a new TriMesh.
        The object can be created from another thread so OpenGL
        variables cannot be set from here"""
        self.context_identifier = context_identifier  # a string identifier unique to the context
        self._vao = None  # vertex array object
        self._vbo = None  # vertex buffer object
        self._shader = None  # the shader program
        self._trm_mat_loc = None  # the reference within the shader program of the transformation matrix
        self.verts = new_empty_verts()  # the vertices to draw
        self.draw_start = 0
        self.draw_count = 0  # the number of vertices to draw

    @property
    def vertex_usage(self):
        return GL_STATIC_DRAW

    @property
    def draw_mode(self):
        return GL_TRIANGLES

    @property
    def shader(self):
        if self._shader is None:
            self._shader = get_shader(self.context_identifier, 'render_chunk')
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
            self.change_verts()
            self._setup_opengl_attrs()
            glBindVertexArray(0)

    def _setup_opengl_attrs(self):
        """Set up OpenGL vertex attributes"""
        attr_start = 0
        for index, attr_count in enumerate(self._vertex_attrs):
            glVertexAttribPointer(index, attr_count, GL_FLOAT, GL_FALSE, self._vert_len * 4, ctypes.c_void_p(attr_start * 4))
            glEnableVertexAttribArray(index)
            attr_start += attr_count

    def change_verts(self, verts=None):
        """Modify the vertices in OpenGL"""
        glBindVertexArray(self._vao)
        glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
        if verts is not None:
            glBufferData(GL_ARRAY_BUFFER, verts.size * 4, verts, self.vertex_usage)
        else:
            glBufferData(GL_ARRAY_BUFFER, self.verts.size * 4, self.verts, self.vertex_usage)

    def unload(self):
        """Unload all opengl data"""
        if self._vao is not None:
            glDeleteVertexArrays(1, self._vao)
            glDeleteBuffers(1, self._vbo)
            self._vao = None
            self._vbo = None

    def draw(self, transformation_matrix: numpy.ndarray):
        self._setup()
        self._draw(transformation_matrix)

    def _draw(self, transformation_matrix: numpy.ndarray):
        glUseProgram(self.shader)
        glUniformMatrix4fv(self.transform_location, 1, GL_FALSE, transformation_matrix)
        glBindVertexArray(self._vao)
        glDrawArrays(self.draw_mode, self.draw_start, self.draw_count)
