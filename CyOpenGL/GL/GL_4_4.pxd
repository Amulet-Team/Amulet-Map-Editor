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

cdef GLenum GL_BUFFER_IMMUTABLE_STORAGE
cdef GLenum GL_BUFFER_STORAGE_FLAGS
cdef GLenum GL_CLEAR_TEXTURE
cdef GLenum GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT
cdef GLenum GL_CLIENT_STORAGE_BIT
cdef GLenum GL_DYNAMIC_STORAGE_BIT
cdef GLenum GL_LOCATION_COMPONENT
cdef GLenum GL_MAP_COHERENT_BIT
cdef GLenum GL_MAP_PERSISTENT_BIT
cdef GLenum GL_MAP_READ_BIT
cdef GLenum GL_MAP_WRITE_BIT
cdef GLenum GL_MAX_VERTEX_ATTRIB_STRIDE
cdef GLenum GL_MIRROR_CLAMP_TO_EDGE
cdef GLenum GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED
cdef GLenum GL_QUERY_BUFFER
cdef GLenum GL_QUERY_BUFFER_BARRIER_BIT
cdef GLenum GL_QUERY_BUFFER_BINDING
cdef GLenum GL_QUERY_RESULT_NO_WAIT
cdef GLenum GL_STENCIL_INDEX
cdef GLenum GL_STENCIL_INDEX8
cdef GLenum GL_TEXTURE_BUFFER_BINDING
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_INDEX
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_STRIDE
cdef GLenum GL_UNSIGNED_INT_10F_11F_11F_REV
cdef void glBindBuffersBase(GLenum target, GLuint first, GLsizei count, const GLuint *buffers)
cdef void glBindBuffersRange(GLenum target, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizeiptr *sizes)
cdef void glBindImageTextures(GLuint first, GLsizei count, const GLuint *textures)
cdef void glBindSamplers(GLuint first, GLsizei count, const GLuint *samplers)
cdef void glBindTextures(GLuint first, GLsizei count, const GLuint *textures)
cdef void glBindVertexBuffers(GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides)
cdef void glBufferStorage(GLenum target, GLsizeiptr size, const void *data, GLbitfield flags)
cdef void glClearTexImage(GLuint texture, GLint level, GLenum format, GLenum type, const void *data)
cdef void glClearTexSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *data)
