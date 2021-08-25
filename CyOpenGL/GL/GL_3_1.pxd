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

cdef GLenum GL_ACTIVE_UNIFORM_BLOCKS
cdef GLenum GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH
cdef GLenum GL_COPY_READ_BUFFER
cdef GLenum GL_COPY_WRITE_BUFFER
cdef GLenum GL_INT_SAMPLER_2D_RECT
cdef GLenum GL_INT_SAMPLER_BUFFER
cdef GLenum GL_INVALID_INDEX
cdef GLenum GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS
cdef GLenum GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS
cdef GLenum GL_MAX_COMBINED_UNIFORM_BLOCKS
cdef GLenum GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS
cdef GLenum GL_MAX_FRAGMENT_UNIFORM_BLOCKS
cdef GLenum GL_MAX_GEOMETRY_UNIFORM_BLOCKS
cdef GLenum GL_MAX_RECTANGLE_TEXTURE_SIZE
cdef GLenum GL_MAX_TEXTURE_BUFFER_SIZE
cdef GLenum GL_MAX_UNIFORM_BLOCK_SIZE
cdef GLenum GL_MAX_UNIFORM_BUFFER_BINDINGS
cdef GLenum GL_MAX_VERTEX_UNIFORM_BLOCKS
cdef GLenum GL_PRIMITIVE_RESTART
cdef GLenum GL_PRIMITIVE_RESTART_INDEX
cdef GLenum GL_PROXY_TEXTURE_RECTANGLE
cdef GLenum GL_R16_SNORM
cdef GLenum GL_R8_SNORM
cdef GLenum GL_RG16_SNORM
cdef GLenum GL_RG8_SNORM
cdef GLenum GL_RGB16_SNORM
cdef GLenum GL_RGB8_SNORM
cdef GLenum GL_RGBA16_SNORM
cdef GLenum GL_RGBA8_SNORM
cdef GLenum GL_SAMPLER_2D_RECT
cdef GLenum GL_SAMPLER_2D_RECT_SHADOW
cdef GLenum GL_SAMPLER_BUFFER
cdef GLenum GL_SIGNED_NORMALIZED
cdef GLenum GL_TEXTURE_BINDING_BUFFER
cdef GLenum GL_TEXTURE_BINDING_RECTANGLE
cdef GLenum GL_TEXTURE_BUFFER
cdef GLenum GL_TEXTURE_BUFFER_DATA_STORE_BINDING
cdef GLenum GL_TEXTURE_RECTANGLE
cdef GLenum GL_UNIFORM_ARRAY_STRIDE
cdef GLenum GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS
cdef GLenum GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES
cdef GLenum GL_UNIFORM_BLOCK_BINDING
cdef GLenum GL_UNIFORM_BLOCK_DATA_SIZE
cdef GLenum GL_UNIFORM_BLOCK_INDEX
cdef GLenum GL_UNIFORM_BLOCK_NAME_LENGTH
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER
cdef GLenum GL_UNIFORM_BUFFER
cdef GLenum GL_UNIFORM_BUFFER_BINDING
cdef GLenum GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT
cdef GLenum GL_UNIFORM_BUFFER_SIZE
cdef GLenum GL_UNIFORM_BUFFER_START
cdef GLenum GL_UNIFORM_IS_ROW_MAJOR
cdef GLenum GL_UNIFORM_MATRIX_STRIDE
cdef GLenum GL_UNIFORM_NAME_LENGTH
cdef GLenum GL_UNIFORM_OFFSET
cdef GLenum GL_UNIFORM_SIZE
cdef GLenum GL_UNIFORM_TYPE
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_RECT
cdef GLenum GL_UNSIGNED_INT_SAMPLER_BUFFER
cdef void glBindBufferBase(GLenum target, GLuint index, GLuint buffer)
cdef void glBindBufferRange(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
cdef void glCopyBufferSubData(GLenum readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size)
cdef void glDrawArraysInstanced(GLenum mode, GLint first, GLsizei count, GLsizei instancecount)
cdef void glDrawElementsInstanced(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount)
cdef void glGetActiveUniformBlockName(GLuint program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformBlockName)
cdef void glGetActiveUniformBlockiv(GLuint program, GLuint uniformBlockIndex, GLenum pname, GLint *params)
cdef void glGetActiveUniformName(GLuint program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformName)
cdef void glGetActiveUniformsiv(GLuint program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint *params)
cdef void glGetIntegeri_v(GLenum target, GLuint index, GLint *data)
cdef GLuint glGetUniformBlockIndex(GLuint program, const GLchar *uniformBlockName)
cdef void glGetUniformIndices(GLuint program, GLsizei uniformCount, const GLchar **uniformNames, GLuint *uniformIndices)
cdef void glPrimitiveRestartIndex(GLuint index)
cdef void glTexBuffer(GLenum target, GLenum internalformat, GLuint buffer)
cdef void glUniformBlockBinding(GLuint program, GLuint uniformBlockIndex, GLuint uniformBlockBinding)
