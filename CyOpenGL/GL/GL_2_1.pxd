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

cdef GLenum GL_COMPRESSED_SLUMINANCE
cdef GLenum GL_COMPRESSED_SLUMINANCE_ALPHA
cdef GLenum GL_COMPRESSED_SRGB
cdef GLenum GL_COMPRESSED_SRGB_ALPHA
cdef GLenum GL_CURRENT_RASTER_SECONDARY_COLOR
cdef GLenum GL_FLOAT_MAT2x3
cdef GLenum GL_FLOAT_MAT2x4
cdef GLenum GL_FLOAT_MAT3x2
cdef GLenum GL_FLOAT_MAT3x4
cdef GLenum GL_FLOAT_MAT4x2
cdef GLenum GL_FLOAT_MAT4x3
cdef GLenum GL_PIXEL_PACK_BUFFER
cdef GLenum GL_PIXEL_PACK_BUFFER_BINDING
cdef GLenum GL_PIXEL_UNPACK_BUFFER
cdef GLenum GL_PIXEL_UNPACK_BUFFER_BINDING
cdef GLenum GL_SLUMINANCE
cdef GLenum GL_SLUMINANCE8
cdef GLenum GL_SLUMINANCE8_ALPHA8
cdef GLenum GL_SLUMINANCE_ALPHA
cdef GLenum GL_SRGB
cdef GLenum GL_SRGB8
cdef GLenum GL_SRGB8_ALPHA8
cdef GLenum GL_SRGB_ALPHA
cdef void glUniformMatrix2x3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glUniformMatrix2x4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glUniformMatrix3x2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glUniformMatrix3x4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glUniformMatrix4x2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glUniformMatrix4x3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
