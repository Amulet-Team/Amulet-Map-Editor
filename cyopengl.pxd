IF UNAME_SYSNAME == "Windows":
    cdef extern from "<windows.h>":
        pass
cdef extern from "<GL/gl.h>":
    unsigned int GL_FALSE
    unsigned int GL_TEXTURE0
    unsigned int GL_TEXTURE_2D
    void glUseProgram(unsigned int program)
    void glUniformMatrix4fv(int location, int count, unsigned char transpose, const float *value)
    void glUniform1i(int location, int v0)
    void glBindVertexArray(unsigned int array)
    void glActiveTexture(unsigned int texture)
    void glBindTexture(unsigned int target, unsigned int texture)
    void glDrawArrays(unsigned int mode, int first, int count)
