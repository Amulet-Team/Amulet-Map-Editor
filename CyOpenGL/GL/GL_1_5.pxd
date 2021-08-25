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
cdef GLboolean glIsQuery(GLuint id)
cdef void glDeleteQueries(GLsizei n, const GLuint *ids)
cdef void glBeginQuery(GLenum target, GLuint id)
cdef void glBufferData(GLenum target, GLsizeiptr size, const void *data, GLenum usage)
cdef void glGetBufferPointerv(GLenum target, GLenum pname, void **params)
cdef void glGetQueryiv(GLenum target, GLenum pname, GLint *params)
cdef void glGetBufferParameteriv(GLenum target, GLenum pname, GLint *params)
cdef GLboolean glIsBuffer(GLuint buffer)
cdef void glGetBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, void *data)
cdef void glGetQueryObjectuiv(GLuint id, GLenum pname, GLuint *params)
cdef void glBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, const void *data)
cdef GLboolean glUnmapBuffer(GLenum target)
cdef void glBindBuffer(GLenum target, GLuint buffer)
cdef void glGenBuffers(GLsizei n, GLuint *buffers)
cdef void glDeleteBuffers(GLsizei n, const GLuint *buffers)
cdef void glGetQueryObjectiv(GLuint id, GLenum pname, GLint *params)
cdef void *glMapBuffer(GLenum target, GLenum access)
cdef void glGenQueries(GLsizei n, GLuint *ids)
cdef void glEndQuery(GLenum target)
