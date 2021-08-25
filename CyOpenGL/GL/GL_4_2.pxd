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

cdef GLenum GL_ACTIVE_ATOMIC_COUNTER_BUFFERS
cdef GLenum GL_ALL_BARRIER_BITS
cdef GLenum GL_ATOMIC_COUNTER_BARRIER_BIT
cdef GLenum GL_ATOMIC_COUNTER_BUFFER
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_BINDING
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_SIZE
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_START
cdef GLenum GL_BUFFER_UPDATE_BARRIER_BIT
cdef GLenum GL_COMMAND_BARRIER_BIT
cdef GLenum GL_COMPRESSED_RGBA_BPTC_UNORM
cdef GLenum GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT
cdef GLenum GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT
cdef GLenum GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM
cdef GLenum GL_COPY_READ_BUFFER_BINDING
cdef GLenum GL_COPY_WRITE_BUFFER_BINDING
cdef GLenum GL_ELEMENT_ARRAY_BARRIER_BIT
cdef GLenum GL_FRAMEBUFFER_BARRIER_BIT
cdef GLenum GL_IMAGE_1D
cdef GLenum GL_IMAGE_1D_ARRAY
cdef GLenum GL_IMAGE_2D
cdef GLenum GL_IMAGE_2D_ARRAY
cdef GLenum GL_IMAGE_2D_MULTISAMPLE
cdef GLenum GL_IMAGE_2D_MULTISAMPLE_ARRAY
cdef GLenum GL_IMAGE_2D_RECT
cdef GLenum GL_IMAGE_3D
cdef GLenum GL_IMAGE_BINDING_ACCESS
cdef GLenum GL_IMAGE_BINDING_FORMAT
cdef GLenum GL_IMAGE_BINDING_LAYER
cdef GLenum GL_IMAGE_BINDING_LAYERED
cdef GLenum GL_IMAGE_BINDING_LEVEL
cdef GLenum GL_IMAGE_BINDING_NAME
cdef GLenum GL_IMAGE_BUFFER
cdef GLenum GL_IMAGE_CUBE
cdef GLenum GL_IMAGE_CUBE_MAP_ARRAY
cdef GLenum GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS
cdef GLenum GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE
cdef GLenum GL_IMAGE_FORMAT_COMPATIBILITY_TYPE
cdef GLenum GL_INT_IMAGE_1D
cdef GLenum GL_INT_IMAGE_1D_ARRAY
cdef GLenum GL_INT_IMAGE_2D
cdef GLenum GL_INT_IMAGE_2D_ARRAY
cdef GLenum GL_INT_IMAGE_2D_MULTISAMPLE
cdef GLenum GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY
cdef GLenum GL_INT_IMAGE_2D_RECT
cdef GLenum GL_INT_IMAGE_3D
cdef GLenum GL_INT_IMAGE_BUFFER
cdef GLenum GL_INT_IMAGE_CUBE
cdef GLenum GL_INT_IMAGE_CUBE_MAP_ARRAY
cdef GLenum GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS
cdef GLenum GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE
cdef GLenum GL_MAX_COMBINED_ATOMIC_COUNTERS
cdef GLenum GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS
cdef GLenum GL_MAX_COMBINED_IMAGE_UNIFORMS
cdef GLenum GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS
cdef GLenum GL_MAX_FRAGMENT_ATOMIC_COUNTERS
cdef GLenum GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS
cdef GLenum GL_MAX_FRAGMENT_IMAGE_UNIFORMS
cdef GLenum GL_MAX_GEOMETRY_ATOMIC_COUNTERS
cdef GLenum GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS
cdef GLenum GL_MAX_GEOMETRY_IMAGE_UNIFORMS
cdef GLenum GL_MAX_IMAGE_SAMPLES
cdef GLenum GL_MAX_IMAGE_UNITS
cdef GLenum GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS
cdef GLenum GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS
cdef GLenum GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS
cdef GLenum GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS
cdef GLenum GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS
cdef GLenum GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS
cdef GLenum GL_MAX_VERTEX_ATOMIC_COUNTERS
cdef GLenum GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS
cdef GLenum GL_MAX_VERTEX_IMAGE_UNIFORMS
cdef GLenum GL_MIN_MAP_BUFFER_ALIGNMENT
cdef GLenum GL_NUM_SAMPLE_COUNTS
cdef GLenum GL_PACK_COMPRESSED_BLOCK_DEPTH
cdef GLenum GL_PACK_COMPRESSED_BLOCK_HEIGHT
cdef GLenum GL_PACK_COMPRESSED_BLOCK_SIZE
cdef GLenum GL_PACK_COMPRESSED_BLOCK_WIDTH
cdef GLenum GL_PIXEL_BUFFER_BARRIER_BIT
cdef GLenum GL_SHADER_IMAGE_ACCESS_BARRIER_BIT
cdef GLenum GL_TEXTURE_FETCH_BARRIER_BIT
cdef GLenum GL_TEXTURE_IMMUTABLE_FORMAT
cdef GLenum GL_TEXTURE_UPDATE_BARRIER_BIT
cdef GLenum GL_TRANSFORM_FEEDBACK_ACTIVE
cdef GLenum GL_TRANSFORM_FEEDBACK_BARRIER_BIT
cdef GLenum GL_TRANSFORM_FEEDBACK_PAUSED
cdef GLenum GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX
cdef GLenum GL_UNIFORM_BARRIER_BIT
cdef GLenum GL_UNPACK_COMPRESSED_BLOCK_DEPTH
cdef GLenum GL_UNPACK_COMPRESSED_BLOCK_HEIGHT
cdef GLenum GL_UNPACK_COMPRESSED_BLOCK_SIZE
cdef GLenum GL_UNPACK_COMPRESSED_BLOCK_WIDTH
cdef GLenum GL_UNSIGNED_INT_ATOMIC_COUNTER
cdef GLenum GL_UNSIGNED_INT_IMAGE_1D
cdef GLenum GL_UNSIGNED_INT_IMAGE_1D_ARRAY
cdef GLenum GL_UNSIGNED_INT_IMAGE_2D
cdef GLenum GL_UNSIGNED_INT_IMAGE_2D_ARRAY
cdef GLenum GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE
cdef GLenum GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY
cdef GLenum GL_UNSIGNED_INT_IMAGE_2D_RECT
cdef GLenum GL_UNSIGNED_INT_IMAGE_3D
cdef GLenum GL_UNSIGNED_INT_IMAGE_BUFFER
cdef GLenum GL_UNSIGNED_INT_IMAGE_CUBE
cdef GLenum GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT
cdef void glBindImageTexture(GLuint unit, GLuint texture, GLint level, GLboolean layered, GLint layer, GLenum access, GLenum format)
cdef void glDrawArraysInstancedBaseInstance(GLenum mode, GLint first, GLsizei count, GLsizei instancecount, GLuint baseinstance)
cdef void glDrawElementsInstancedBaseInstance(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLuint baseinstance)
cdef void glDrawElementsInstancedBaseVertexBaseInstance(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex, GLuint baseinstance)
cdef void glDrawTransformFeedbackInstanced(GLenum mode, GLuint id, GLsizei instancecount)
cdef void glDrawTransformFeedbackStreamInstanced(GLenum mode, GLuint id, GLuint stream, GLsizei instancecount)
cdef void glGetActiveAtomicCounterBufferiv(GLuint program, GLuint bufferIndex, GLenum pname, GLint *params)
cdef void glGetInternalformativ(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint *params)
cdef void glMemoryBarrier(GLbitfield barriers)
cdef void glTexStorage1D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width)
cdef void glTexStorage2D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glTexStorage3D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth)
