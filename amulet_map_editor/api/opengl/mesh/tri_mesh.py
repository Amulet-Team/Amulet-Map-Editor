from OpenGL.GL import (
    glBindTexture,
    GL_TEXTURE_2D,
    GL_TRIANGLES,
    glBindVertexArray,
    glBindBuffer,
    GL_ARRAY_BUFFER,
    GL_STATIC_DRAW,
    glUseProgram,
    glGetUniformLocation,
    glGenVertexArrays,
    glGenBuffers,
    glVertexAttribPointer,
    GL_FLOAT,
    GL_FALSE,
    glEnableVertexAttribArray,
    glBufferData,
    glDeleteBuffers,
    glDeleteVertexArrays,
    glUniformMatrix4fv,
    glUniform1i,
    glActiveTexture,
    GL_TEXTURE0,
    glDrawArrays,
)
from OpenGL.error import GLError
import ctypes
import numpy
from amulet_map_editor.api.opengl.shaders import get_shader
from amulet_map_editor.api.opengl import Drawable, ContextManager
from amulet_map_editor import log


class TriMesh(Drawable, ContextManager):
    """The base class for a triangular face mesh.
    Implements the base logic to set up and unload OpenGL."""

    _vertex_attrs = (
        3,  # vertex attribute pointers
        2,  # texture coords attribute pointers
        4,  # texture coords attribute pointers
        3,  # tint value (also shading)
    )
    _vert_len = sum(_vertex_attrs)

    def __init__(self, context_identifier: str, texture: int):
        """Create a new TriMesh.
        The object can be created from another thread so OpenGL
        variables cannot be set from here"""
        ContextManager.__init__(self, context_identifier)
        self._vao = None  # vertex array object
        self._vbo = None  # vertex buffer object
        self._shader = None  # the shader program
        self._transform_location = (
            None  # the reference within the shader program of the transformation matrix
        )
        self._texture_location = None  # the location of the texture in the shader
        self._texture = texture
        self.verts = self.new_empty_verts()  # the vertices to draw
        self.draw_start = 0
        self.draw_count = 0  # the number of vertices to draw

    @staticmethod
    def new_empty_verts() -> numpy.ndarray:
        return numpy.zeros(0, dtype=numpy.float32)

    @property
    def vertex_usage(self):
        return GL_STATIC_DRAW

    @property
    def draw_mode(self):
        return GL_TRIANGLES

    @property
    def shader_name(self) -> str:
        return "render_chunk"

    def _setup(self):
        """Setup OpenGL attributes if required"""
        if self._vao is None:  # if the opengl state has not been set
            self._shader = get_shader(self.context_identifier, self.shader_name)
            glUseProgram(self._shader)
            self._transform_location = glGetUniformLocation(
                self._shader, "transformation_matrix"
            )
            self._texture_location = glGetUniformLocation(self._shader, "image")
            self._vao = glGenVertexArrays(1)  # create the array
            glBindVertexArray(self._vao)
            self._vbo = glGenBuffers(1)  # and the buffer
            glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
            self._setup_opengl_attrs()
            self._change_verts()
            glBindVertexArray(0)
            glBindBuffer(GL_ARRAY_BUFFER, 0)
            glUseProgram(0)

    def _setup_opengl_attrs(self):
        """Set up OpenGL vertex attributes"""
        attr_start = 0
        for index, attr_count in enumerate(self._vertex_attrs):
            glVertexAttribPointer(
                index,
                attr_count,
                GL_FLOAT,
                GL_FALSE,
                self._vert_len * 4,
                ctypes.c_void_p(attr_start * 4),
            )
            glEnableVertexAttribArray(index)
            attr_start += attr_count

    def change_verts(self, verts=None):
        """Modify the vertices in OpenGL."""
        log.debug(f"change_verts {self}")
        try:
            glBindVertexArray(self._vao)
            glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
        except GLError:  # There seems to be errors randomly when binding the VBO
            log.debug(
                f"Failed binding the OpenGL state for {self}. Trying to reload it."
            )
            self.unload()
            self._setup()
            if verts is None:
                return
            glBindVertexArray(self._vao)
            glBindBuffer(GL_ARRAY_BUFFER, self._vbo)
        self._change_verts(verts)
        glBindVertexArray(0)
        glBindBuffer(GL_ARRAY_BUFFER, 0)

    def _change_verts(self, verts=None):
        """Modify the vertices in OpenGL. Requires binding and unbinding."""
        if verts is not None:
            glBufferData(GL_ARRAY_BUFFER, verts.size * 4, verts, self.vertex_usage)
        else:
            glBufferData(
                GL_ARRAY_BUFFER, self.verts.size * 4, self.verts, self.vertex_usage
            )

    def unload(self):
        """Unload all opengl data"""
        log.debug(f"unload {self}")
        if self._vbo is not None:
            glDeleteBuffers(1, int(self._vbo))
            self._vbo = None
        if self._vao is not None:
            glDeleteVertexArrays(1, int(self._vao))
            self._vao = None

    def draw(self, transformation_matrix: numpy.ndarray):
        self._setup()
        self._draw(transformation_matrix)

    def _draw(self, transformation_matrix: numpy.ndarray):
        glUseProgram(self._shader)
        glUniformMatrix4fv(
            self._transform_location,
            1,
            GL_FALSE,
            transformation_matrix.T.astype(numpy.float32),
        )
        glUniform1i(self._texture_location, 0)
        try:
            glBindVertexArray(self._vao)
        except GLError:  # There seems to be errors randomly when binding the VBO
            log.debug(
                f"Failed binding the OpenGL state for {self}. Trying to reload it."
            )
            self.unload()
            self._setup()
            glBindVertexArray(self._vao)
        glActiveTexture(GL_TEXTURE0)
        glBindTexture(GL_TEXTURE_2D, self._texture)

        glDrawArrays(self.draw_mode, self.draw_start, self.draw_count)

        glBindVertexArray(0)
        glUseProgram(0)
