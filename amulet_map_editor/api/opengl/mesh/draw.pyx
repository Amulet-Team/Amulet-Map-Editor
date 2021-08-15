import numpy
cimport numpy
from cyopengl cimport (
    # GL_FALSE,
    # GL_TEXTURE0,
    # GL_TEXTURE_2D,
    # glUseProgram,
    # glUniformMatrix4fv,
    # glUniform1i,
    # glBindVertexArray,
    # glActiveTexture,
    glBindTexture,
    glDrawArrays,
)

cpdef draw(self, transformation_matrix: numpy.ndarray):
    # cdef array.array transform_array = array.array("f", transformation_matrix.T.astype(numpy.float32).ravel())
    # cdef float* transform = &transform_array.data.as_floats[0]
    # glUseProgram(self._shader)
    # glUniformMatrix4fv(
    #     self._transform_location,
    #     1,
    #     GL_FALSE,
    #     transform,
    # )
    # glUniform1i(self._texture_location, 0)
    # glBindVertexArray(self._vao)
    # glActiveTexture(GL_TEXTURE0)
    cdef int texture = self._texture
    glBindTexture(0x0DE1, texture)

    cdef unsigned int mode = self.draw_mode
    cdef int first = self.draw_start
    cdef int count = self.draw_count
    glDrawArrays(mode, first, count)

    # glBindVertexArray(0)
    # glUseProgram(0)
