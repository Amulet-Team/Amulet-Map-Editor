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

cdef GLenum GL_ARRAY_BUFFER
cdef GLenum GL_ARRAY_BUFFER_BINDING
cdef GLenum GL_BUFFER_ACCESS
cdef GLenum GL_BUFFER_MAPPED
cdef GLenum GL_BUFFER_MAP_POINTER
cdef GLenum GL_BUFFER_SIZE
cdef GLenum GL_BUFFER_USAGE
cdef GLenum GL_COLOR_ARRAY_BUFFER_BINDING
cdef GLenum GL_CURRENT_FOG_COORD
cdef GLenum GL_CURRENT_QUERY
cdef GLenum GL_DYNAMIC_COPY
cdef GLenum GL_DYNAMIC_DRAW
cdef GLenum GL_DYNAMIC_READ
cdef GLenum GL_EDGE_FLAG_ARRAY_BUFFER_BINDING
cdef GLenum GL_ELEMENT_ARRAY_BUFFER
cdef GLenum GL_ELEMENT_ARRAY_BUFFER_BINDING
cdef GLenum GL_FOG_COORD
cdef GLenum GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING
cdef GLenum GL_FOG_COORD_ARRAY
cdef GLenum GL_FOG_COORD_ARRAY_BUFFER_BINDING
cdef GLenum GL_FOG_COORD_ARRAY_POINTER
cdef GLenum GL_FOG_COORD_ARRAY_STRIDE
cdef GLenum GL_FOG_COORD_ARRAY_TYPE
cdef GLenum GL_FOG_COORD_SRC
cdef GLenum GL_INDEX_ARRAY_BUFFER_BINDING
cdef GLenum GL_NORMAL_ARRAY_BUFFER_BINDING
cdef GLenum GL_QUERY_COUNTER_BITS
cdef GLenum GL_QUERY_RESULT
cdef GLenum GL_QUERY_RESULT_AVAILABLE
cdef GLenum GL_READ_ONLY
cdef GLenum GL_READ_WRITE
cdef GLenum GL_SAMPLES_PASSED
cdef GLenum GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING
cdef GLenum GL_SRC0_ALPHA
cdef GLenum GL_SRC0_RGB
cdef GLenum GL_SRC1_ALPHA
cdef GLenum GL_SRC1_RGB
cdef GLenum GL_SRC2_ALPHA
cdef GLenum GL_SRC2_RGB
cdef GLenum GL_STATIC_COPY
cdef GLenum GL_STATIC_DRAW
cdef GLenum GL_STATIC_READ
cdef GLenum GL_STREAM_COPY
cdef GLenum GL_STREAM_DRAW
cdef GLenum GL_STREAM_READ
cdef GLenum GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING
cdef GLenum GL_VERTEX_ARRAY_BUFFER_BINDING
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING
cdef GLenum GL_WEIGHT_ARRAY_BUFFER_BINDING
cdef GLenum GL_WRITE_ONLY
cdef void glBeginQuery(GLenum target, GLuint id)
cdef void glBindBuffer(GLenum target, GLuint buffer)
cdef void glBufferData(GLenum target, GLsizeiptr size, const void *data, GLenum usage)
cdef void glBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, const void *data)
cdef void glDeleteBuffers(GLsizei n, const GLuint *buffers)
cdef void glDeleteQueries(GLsizei n, const GLuint *ids)
cdef void glEndQuery(GLenum target)
cdef void glGenBuffers(GLsizei n, GLuint *buffers)
cdef void glGenQueries(GLsizei n, GLuint *ids)
cdef void glGetBufferParameteriv(GLenum target, GLenum pname, GLint *params)
cdef void glGetBufferPointerv(GLenum target, GLenum pname, void **params)
cdef void glGetBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, void *data)
cdef void glGetQueryObjectiv(GLuint id, GLenum pname, GLint *params)
cdef void glGetQueryObjectuiv(GLuint id, GLenum pname, GLuint *params)
cdef void glGetQueryiv(GLenum target, GLenum pname, GLint *params)
cdef GLboolean glIsBuffer(GLuint buffer)
cdef GLboolean glIsQuery(GLuint id)
cdef void *glMapBuffer(GLenum target, GLenum access)
cdef GLboolean glUnmapBuffer(GLenum target)
