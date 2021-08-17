# ctypedef void (*PFNGLUSEPROGRAMPROC)(GLuint)
ctypedef void (*PFNGLUSEPROGRAMPROC)(GLuint program)
ctypedef void (*PFNGLUNIFORMMATRIX4FVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLUNIFORM1IPROC)(GLint location, GLint v0)
ctypedef void (*PFNGLBINDVERTEXARRAYPROC)(GLuint array)
ctypedef void (*PFNGLACTIVETEXTUREPROC)(GLenum texture)

cpdef void glUseProgram(GLuint program):
    cdef PFNGLUSEPROGRAMPROC fun = <PFNGLUSEPROGRAMPROC>wglGetProcAddress(b"glUseProgram")
    fun(program)

cpdef void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, GLfloat[:] value):
    cdef PFNGLUNIFORMMATRIX4FVPROC fun = <PFNGLUNIFORMMATRIX4FVPROC>wglGetProcAddress(b"glUniformMatrix4fv")
    fun(location, count, transpose, &value[0])

cpdef void glUniform1i(GLint location, GLint v0):
    cdef PFNGLUNIFORM1IPROC fun = <PFNGLUNIFORM1IPROC>wglGetProcAddress(b"glUniform1i")
    fun(location, v0)

cpdef void glBindVertexArray(GLuint array):
    cdef PFNGLBINDVERTEXARRAYPROC fun = <PFNGLBINDVERTEXARRAYPROC>wglGetProcAddress(b"glBindVertexArray")
    fun(array)

cpdef void glActiveTexture(GLenum texture):
    cdef PFNGLACTIVETEXTUREPROC fun = <PFNGLACTIVETEXTUREPROC>wglGetProcAddress(b"glActiveTexture")
    fun(texture)
