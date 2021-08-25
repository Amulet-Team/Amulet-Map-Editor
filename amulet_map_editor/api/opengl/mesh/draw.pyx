# distutils: libraries = opengl32

import numpy
cimport numpy
from CyOpenGL.GL cimport (
    GL_FALSE,
    GL_TEXTURE0,
    GL_TEXTURE_2D,
    GLuint,
    GLint,
    GLfloat,
    GLsizei,
    GLenum,
    glUseProgram,
    glUniformMatrix4fv,
    glUniform1i,
    glBindVertexArray,
    glActiveTexture,
    glBindTexture,
    glDrawArrays,
)

cpdef draw(self, transformation_matrix: numpy.ndarray):
    cdef float[::1] np_transform = numpy.ascontiguousarray(transformation_matrix.T.ravel(), dtype=numpy.float32)
    cdef float *transform = &np_transform[0]
    cdef GLenum mode = self.draw_mode
    cdef GLint first = self.draw_start
    cdef GLsizei count = self.draw_count
    cdef GLuint shader = self._shader
    cdef GLint transform_location = self._transform_location
    cdef GLint texture_location = self._texture_location
    cdef GLuint texture = self._texture
    cdef GLuint vao = self._vao
    glUseProgram(shader)
    glUniformMatrix4fv(
        transform_location,
        1,
        GL_FALSE,
        transform,
    )
    glUniform1i(texture_location, 0)
    glBindVertexArray(vao)
    glActiveTexture(GL_TEXTURE0)
    glBindTexture(GL_TEXTURE_2D, texture)
    glDrawArrays(mode, first, count)
    glBindVertexArray(0)
    glUseProgram(0)
