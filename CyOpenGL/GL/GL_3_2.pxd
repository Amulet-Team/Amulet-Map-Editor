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

cdef GLenum GL_ALREADY_SIGNALED
cdef GLenum GL_CONDITION_SATISFIED
cdef GLenum GL_CONTEXT_COMPATIBILITY_PROFILE_BIT
cdef GLenum GL_CONTEXT_CORE_PROFILE_BIT
cdef GLenum GL_CONTEXT_PROFILE_MASK
cdef GLenum GL_DEPTH_CLAMP
cdef GLenum GL_FIRST_VERTEX_CONVENTION
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_LAYERED
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS
cdef GLenum GL_GEOMETRY_INPUT_TYPE
cdef GLenum GL_GEOMETRY_OUTPUT_TYPE
cdef GLenum GL_GEOMETRY_SHADER
cdef GLenum GL_GEOMETRY_VERTICES_OUT
cdef GLenum GL_INT_SAMPLER_2D_MULTISAMPLE
cdef GLenum GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY
cdef GLenum GL_LAST_VERTEX_CONVENTION
cdef GLenum GL_LINES_ADJACENCY
cdef GLenum GL_LINE_STRIP_ADJACENCY
cdef GLenum GL_MAX_COLOR_TEXTURE_SAMPLES
cdef GLenum GL_MAX_DEPTH_TEXTURE_SAMPLES
cdef GLenum GL_MAX_FRAGMENT_INPUT_COMPONENTS
cdef GLenum GL_MAX_GEOMETRY_INPUT_COMPONENTS
cdef GLenum GL_MAX_GEOMETRY_OUTPUT_COMPONENTS
cdef GLenum GL_MAX_GEOMETRY_OUTPUT_VERTICES
cdef GLenum GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS
cdef GLenum GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS
cdef GLenum GL_MAX_GEOMETRY_UNIFORM_COMPONENTS
cdef GLenum GL_MAX_INTEGER_SAMPLES
cdef GLenum GL_MAX_SAMPLE_MASK_WORDS
cdef GLenum GL_MAX_SERVER_WAIT_TIMEOUT
cdef GLenum GL_MAX_VERTEX_OUTPUT_COMPONENTS
cdef GLenum GL_OBJECT_TYPE
cdef GLenum GL_PROGRAM_POINT_SIZE
cdef GLenum GL_PROVOKING_VERTEX
cdef GLenum GL_PROXY_TEXTURE_2D_MULTISAMPLE
cdef GLenum GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY
cdef GLenum GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION
cdef GLenum GL_SAMPLER_2D_MULTISAMPLE
cdef GLenum GL_SAMPLER_2D_MULTISAMPLE_ARRAY
cdef GLenum GL_SAMPLE_MASK
cdef GLenum GL_SAMPLE_MASK_VALUE
cdef GLenum GL_SAMPLE_POSITION
cdef GLenum GL_SIGNALED
cdef GLenum GL_SYNC_CONDITION
cdef GLenum GL_SYNC_FENCE
cdef GLenum GL_SYNC_FLAGS
cdef GLenum GL_SYNC_FLUSH_COMMANDS_BIT
cdef GLenum GL_SYNC_GPU_COMMANDS_COMPLETE
cdef GLenum GL_SYNC_STATUS
cdef GLenum GL_TEXTURE_2D_MULTISAMPLE
cdef GLenum GL_TEXTURE_2D_MULTISAMPLE_ARRAY
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY
cdef GLenum GL_TEXTURE_CUBE_MAP_SEAMLESS
cdef GLenum GL_TEXTURE_FIXED_SAMPLE_LOCATIONS
cdef GLenum GL_TEXTURE_SAMPLES
cdef GLenum GL_TIMEOUT_EXPIRED
cdef GLenum GL_TIMEOUT_IGNORED
cdef GLenum GL_TRIANGLES_ADJACENCY
cdef GLenum GL_TRIANGLE_STRIP_ADJACENCY
cdef GLenum GL_UNSIGNALED
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY
cdef GLenum GL_WAIT_FAILED
cdef GLenum glClientWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout)
cdef void glDeleteSync(GLsync sync)
cdef void glDrawElementsBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLint basevertex)
cdef void glDrawElementsInstancedBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex)
cdef void glDrawRangeElementsBaseVertex(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices, GLint basevertex)
cdef GLsync glFenceSync(GLenum condition, GLbitfield flags)
cdef void glFramebufferTexture(GLenum target, GLenum attachment, GLuint texture, GLint level)
cdef void glGetBufferParameteri64v(GLenum target, GLenum pname, GLint64 *params)
cdef void glGetInteger64i_v(GLenum target, GLuint index, GLint64 *data)
cdef void glGetInteger64v(GLenum pname, GLint64 *data)
cdef void glGetMultisamplefv(GLenum pname, GLuint index, GLfloat *val)
cdef void glGetSynciv(GLsync sync, GLenum pname, GLsizei count, GLsizei *length, GLint *values)
cdef GLboolean glIsSync(GLsync sync)
cdef void glMultiDrawElementsBaseVertex(GLenum mode, const GLsizei *count, GLenum type, const void **indices, GLsizei drawcount, const GLint *basevertex)
cdef void glProvokingVertex(GLenum mode)
cdef void glSampleMaski(GLuint maskNumber, GLbitfield mask)
cdef void glTexImage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
cdef void glTexImage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
cdef void glWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout)
