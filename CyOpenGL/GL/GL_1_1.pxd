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
ctypedef void ( *GLDEBUGPROC)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,const void *userParam)
ctypedef void ( *GLDEBUGPROCARB)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,const void *userParam)
ctypedef void ( *GLDEBUGPROCKHR)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,const void *userParam)
ctypedef void ( *GLDEBUGPROCAMD)(GLuint id,GLenum category,GLenum severity,GLsizei length,const GLchar *message,void *userParam)
ctypedef unsigned short GLhalfNV
ctypedef GLintptr GLvdpauSurfaceNV
ctypedef void ( *GLVULKANPROCNV)()
cdef void glDrawArrays(GLenum mode, GLint first, GLsizei count)
cdef void glColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer)
cdef void glPopClientAttrib()
cdef void glBindTexture(GLenum target, GLuint texture)
cdef void glIndexubv(const GLubyte *c)
cdef void glCopyTexImage1D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
cdef void glInterleavedArrays(GLenum format, GLsizei stride, const void *pointer)
cdef GLboolean glAreTexturesResident(GLsizei n, const GLuint *textures, GLboolean *residences)
cdef void glCopyTexImage2D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border)
cdef void glPushClientAttrib(GLbitfield mask)
cdef void glTexCoordPointer(GLint size, GLenum type, GLsizei stride, const void *pointer)
cdef void glDrawElements(GLenum mode, GLsizei count, GLenum type, const void *indices)
cdef void glArrayElement(GLint i)
cdef void glDeleteTextures(GLsizei n, const GLuint *textures)
cdef void glCopyTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
cdef void glGenTextures(GLsizei n, GLuint *textures)
cdef void glVertexPointer(GLint size, GLenum type, GLsizei stride, const void *pointer)
cdef void glEdgeFlagPointer(GLsizei stride, const void *pointer)
cdef void glEnableClientState(GLenum array)
cdef void glGetPointerv(GLenum pname, void **params)
cdef GLboolean glIsTexture(GLuint texture)
cdef void glCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
cdef void glDisableClientState(GLenum array)
cdef void glIndexub(GLubyte c)
cdef void glIndexPointer(GLenum type, GLsizei stride, const void *pointer)
cdef void glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
cdef void glNormalPointer(GLenum type, GLsizei stride, const void *pointer)
cdef void glPrioritizeTextures(GLsizei n, const GLuint *textures, const GLfloat *priorities)
cdef void glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels)
cdef void glPolygonOffset(GLfloat factor, GLfloat units)
