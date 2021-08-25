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
cdef GLsync glFenceSync(GLenum condition, GLbitfield flags)
cdef void glDrawElementsInstancedBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex)
cdef GLboolean glIsSync(GLsync sync)
cdef void glGetInteger64v(GLenum pname, GLint64 *data)
cdef void glDrawElementsBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLint basevertex)
cdef GLenum glClientWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout)
cdef void glGetBufferParameteri64v(GLenum target, GLenum pname, GLint64 *params)
cdef void glFramebufferTexture(GLenum target, GLenum attachment, GLuint texture, GLint level)
cdef void glMultiDrawElementsBaseVertex(GLenum mode, const GLsizei *count, GLenum type, const void **indices, GLsizei drawcount, const GLint *basevertex)
cdef void glProvokingVertex(GLenum mode)
cdef void glWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout)
cdef void glGetInteger64i_v(GLenum target, GLuint index, GLint64 *data)
cdef void glDeleteSync(GLsync sync)
cdef void glDrawRangeElementsBaseVertex(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices, GLint basevertex)
cdef void glSampleMaski(GLuint maskNumber, GLbitfield mask)
cdef void glTexImage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
cdef void glGetMultisamplefv(GLenum pname, GLuint index, GLfloat *val)
cdef void glTexImage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
cdef void glGetSynciv(GLsync sync, GLenum pname, GLsizei count, GLsizei *length, GLint *values)
