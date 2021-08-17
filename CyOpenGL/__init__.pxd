IF UNAME_SYSNAME == "Windows":
    cdef extern from "<windows.h>":
        ctypedef void *PVOID
        ctypedef PVOID HANDLE
        ctypedef HANDLE HINSTANCE
        ctypedef HINSTANCE HMODULE
        ctypedef char *LPCSTR

cdef extern from "<gl/gl.h>":
    ctypedef unsigned int GLenum
    ctypedef unsigned char GLboolean
    ctypedef unsigned int GLbitfield
    ctypedef void GLvoid
    ctypedef signed char GLbyte
    ctypedef short GLshort
    ctypedef int GLint
    ctypedef int GLclampx
    ctypedef unsigned char GLubyte
    ctypedef unsigned short GLushort
    ctypedef unsigned int GLuint
    ctypedef int GLsizei
    ctypedef float GLfloat
    ctypedef float GLclampf
    ctypedef double GLdouble
    ctypedef double GLclampd
    ctypedef void *GLeglClientBufferEXT
    ctypedef void *GLeglImageOES
    ctypedef char GLchar
    ctypedef char GLcharARB
    ctypedef int GLhandleARB
    ctypedef unsigned short GLhalfARB
    ctypedef unsigned short GLhalf
    ctypedef GLint GLfixed
    ctypedef int * GLintptr
    ctypedef int GLsizeiptr
    ctypedef int GLint64
    ctypedef int GLuint64
    ctypedef ptrdiff_t GLintptrARB
    ctypedef ptrdiff_t GLsizeiptrARB
    ctypedef int GLint64EXT
    ctypedef int GLuint64EXT
    ctypedef int *GLsync
    unsigned int GL_FALSE
    unsigned int GL_TEXTURE0
    unsigned int GL_TEXTURE_2D
    # void glUseProgram(GLuint program)
    # void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
    # void glUniform1i(GLint location, GLint v0)
    # void glBindVertexArray(GLuint array)
    # void glActiveTexture(GLenum texture)
    void glBindTexture(GLenum target, GLuint texture)
    void glDrawArrays(GLenum mode, GLint first, GLsizei count)
    void* wglGetProcAddress(LPCSTR lpszProc)

cpdef void glUseProgram(GLuint program)
cpdef void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat[:] value)
cpdef void glUniform1i(GLint location, GLint v0)
cpdef void glBindVertexArray(GLuint array)
cpdef void glActiveTexture(GLenum texture)
