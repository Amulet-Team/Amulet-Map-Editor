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

cdef GLenum GL_ACTIVE_RESOURCES
cdef GLenum GL_ACTIVE_VARIABLES
cdef GLenum GL_ANY_SAMPLES_PASSED_CONSERVATIVE
cdef GLenum GL_ARRAY_SIZE
cdef GLenum GL_ARRAY_STRIDE
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_INDEX
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER
cdef GLenum GL_AUTO_GENERATE_MIPMAP
cdef GLenum GL_BLOCK_INDEX
cdef GLenum GL_BUFFER
cdef GLenum GL_BUFFER_BINDING
cdef GLenum GL_BUFFER_DATA_SIZE
cdef GLenum GL_BUFFER_VARIABLE
cdef GLenum GL_CAVEAT_SUPPORT
cdef GLenum GL_CLEAR_BUFFER
cdef GLenum GL_COLOR_COMPONENTS
cdef GLenum GL_COLOR_ENCODING
cdef GLenum GL_COLOR_RENDERABLE
cdef GLenum GL_COMPRESSED_R11_EAC
cdef GLenum GL_COMPRESSED_RG11_EAC
cdef GLenum GL_COMPRESSED_RGB8_ETC2
cdef GLenum GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2
cdef GLenum GL_COMPRESSED_RGBA8_ETC2_EAC
cdef GLenum GL_COMPRESSED_SIGNED_R11_EAC
cdef GLenum GL_COMPRESSED_SIGNED_RG11_EAC
cdef GLenum GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC
cdef GLenum GL_COMPRESSED_SRGB8_ETC2
cdef GLenum GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2
cdef GLenum GL_COMPUTE_SHADER
cdef GLenum GL_COMPUTE_SHADER_BIT
cdef GLenum GL_COMPUTE_SUBROUTINE
cdef GLenum GL_COMPUTE_SUBROUTINE_UNIFORM
cdef GLenum GL_COMPUTE_TEXTURE
cdef GLenum GL_COMPUTE_WORK_GROUP_SIZE
cdef GLenum GL_CONTEXT_FLAG_DEBUG_BIT
cdef GLenum GL_DEBUG_CALLBACK_FUNCTION
cdef GLenum GL_DEBUG_CALLBACK_USER_PARAM
cdef GLenum GL_DEBUG_GROUP_STACK_DEPTH
cdef GLenum GL_DEBUG_LOGGED_MESSAGES
cdef GLenum GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH
cdef GLenum GL_DEBUG_OUTPUT
cdef GLenum GL_DEBUG_OUTPUT_SYNCHRONOUS
cdef GLenum GL_DEBUG_SEVERITY_HIGH
cdef GLenum GL_DEBUG_SEVERITY_LOW
cdef GLenum GL_DEBUG_SEVERITY_MEDIUM
cdef GLenum GL_DEBUG_SEVERITY_NOTIFICATION
cdef GLenum GL_DEBUG_SOURCE_API
cdef GLenum GL_DEBUG_SOURCE_APPLICATION
cdef GLenum GL_DEBUG_SOURCE_OTHER
cdef GLenum GL_DEBUG_SOURCE_SHADER_COMPILER
cdef GLenum GL_DEBUG_SOURCE_THIRD_PARTY
cdef GLenum GL_DEBUG_SOURCE_WINDOW_SYSTEM
cdef GLenum GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR
cdef GLenum GL_DEBUG_TYPE_ERROR
cdef GLenum GL_DEBUG_TYPE_MARKER
cdef GLenum GL_DEBUG_TYPE_OTHER
cdef GLenum GL_DEBUG_TYPE_PERFORMANCE
cdef GLenum GL_DEBUG_TYPE_POP_GROUP
cdef GLenum GL_DEBUG_TYPE_PORTABILITY
cdef GLenum GL_DEBUG_TYPE_PUSH_GROUP
cdef GLenum GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR
cdef GLenum GL_DEPTH_COMPONENTS
cdef GLenum GL_DEPTH_RENDERABLE
cdef GLenum GL_DEPTH_STENCIL_TEXTURE_MODE
cdef GLenum GL_DISPATCH_INDIRECT_BUFFER
cdef GLenum GL_DISPATCH_INDIRECT_BUFFER_BINDING
cdef GLenum GL_DISPLAY_LIST
cdef GLenum GL_FILTER
cdef GLenum GL_FRAGMENT_SUBROUTINE
cdef GLenum GL_FRAGMENT_SUBROUTINE_UNIFORM
cdef GLenum GL_FRAGMENT_TEXTURE
cdef GLenum GL_FRAMEBUFFER_BLEND
cdef GLenum GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS
cdef GLenum GL_FRAMEBUFFER_DEFAULT_HEIGHT
cdef GLenum GL_FRAMEBUFFER_DEFAULT_LAYERS
cdef GLenum GL_FRAMEBUFFER_DEFAULT_SAMPLES
cdef GLenum GL_FRAMEBUFFER_DEFAULT_WIDTH
cdef GLenum GL_FRAMEBUFFER_RENDERABLE
cdef GLenum GL_FRAMEBUFFER_RENDERABLE_LAYERED
cdef GLenum GL_FULL_SUPPORT
cdef GLenum GL_GEOMETRY_SUBROUTINE
cdef GLenum GL_GEOMETRY_SUBROUTINE_UNIFORM
cdef GLenum GL_GEOMETRY_TEXTURE
cdef GLenum GL_GET_TEXTURE_IMAGE_FORMAT
cdef GLenum GL_GET_TEXTURE_IMAGE_TYPE
cdef GLenum GL_IMAGE_CLASS_10_10_10_2
cdef GLenum GL_IMAGE_CLASS_11_11_10
cdef GLenum GL_IMAGE_CLASS_1_X_16
cdef GLenum GL_IMAGE_CLASS_1_X_32
cdef GLenum GL_IMAGE_CLASS_1_X_8
cdef GLenum GL_IMAGE_CLASS_2_X_16
cdef GLenum GL_IMAGE_CLASS_2_X_32
cdef GLenum GL_IMAGE_CLASS_2_X_8
cdef GLenum GL_IMAGE_CLASS_4_X_16
cdef GLenum GL_IMAGE_CLASS_4_X_32
cdef GLenum GL_IMAGE_CLASS_4_X_8
cdef GLenum GL_IMAGE_COMPATIBILITY_CLASS
cdef GLenum GL_IMAGE_PIXEL_FORMAT
cdef GLenum GL_IMAGE_PIXEL_TYPE
cdef GLenum GL_IMAGE_TEXEL_SIZE
cdef GLenum GL_INTERNALFORMAT_ALPHA_SIZE
cdef GLenum GL_INTERNALFORMAT_ALPHA_TYPE
cdef GLenum GL_INTERNALFORMAT_BLUE_SIZE
cdef GLenum GL_INTERNALFORMAT_BLUE_TYPE
cdef GLenum GL_INTERNALFORMAT_DEPTH_SIZE
cdef GLenum GL_INTERNALFORMAT_DEPTH_TYPE
cdef GLenum GL_INTERNALFORMAT_GREEN_SIZE
cdef GLenum GL_INTERNALFORMAT_GREEN_TYPE
cdef GLenum GL_INTERNALFORMAT_PREFERRED
cdef GLenum GL_INTERNALFORMAT_RED_SIZE
cdef GLenum GL_INTERNALFORMAT_RED_TYPE
cdef GLenum GL_INTERNALFORMAT_SHARED_SIZE
cdef GLenum GL_INTERNALFORMAT_STENCIL_SIZE
cdef GLenum GL_INTERNALFORMAT_STENCIL_TYPE
cdef GLenum GL_INTERNALFORMAT_SUPPORTED
cdef GLenum GL_IS_PER_PATCH
cdef GLenum GL_IS_ROW_MAJOR
cdef GLenum GL_LOCATION
cdef GLenum GL_LOCATION_INDEX
cdef GLenum GL_MANUAL_GENERATE_MIPMAP
cdef GLenum GL_MATRIX_STRIDE
cdef GLenum GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS
cdef GLenum GL_MAX_COMBINED_DIMENSIONS
cdef GLenum GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES
cdef GLenum GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS
cdef GLenum GL_MAX_COMPUTE_ATOMIC_COUNTERS
cdef GLenum GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS
cdef GLenum GL_MAX_COMPUTE_IMAGE_UNIFORMS
cdef GLenum GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS
cdef GLenum GL_MAX_COMPUTE_SHARED_MEMORY_SIZE
cdef GLenum GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS
cdef GLenum GL_MAX_COMPUTE_UNIFORM_BLOCKS
cdef GLenum GL_MAX_COMPUTE_UNIFORM_COMPONENTS
cdef GLenum GL_MAX_COMPUTE_WORK_GROUP_COUNT
cdef GLenum GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS
cdef GLenum GL_MAX_COMPUTE_WORK_GROUP_SIZE
cdef GLenum GL_MAX_DEBUG_GROUP_STACK_DEPTH
cdef GLenum GL_MAX_DEBUG_LOGGED_MESSAGES
cdef GLenum GL_MAX_DEBUG_MESSAGE_LENGTH
cdef GLenum GL_MAX_DEPTH
cdef GLenum GL_MAX_ELEMENT_INDEX
cdef GLenum GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS
cdef GLenum GL_MAX_FRAMEBUFFER_HEIGHT
cdef GLenum GL_MAX_FRAMEBUFFER_LAYERS
cdef GLenum GL_MAX_FRAMEBUFFER_SAMPLES
cdef GLenum GL_MAX_FRAMEBUFFER_WIDTH
cdef GLenum GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS
cdef GLenum GL_MAX_HEIGHT
cdef GLenum GL_MAX_LABEL_LENGTH
cdef GLenum GL_MAX_LAYERS
cdef GLenum GL_MAX_NAME_LENGTH
cdef GLenum GL_MAX_NUM_ACTIVE_VARIABLES
cdef GLenum GL_MAX_NUM_COMPATIBLE_SUBROUTINES
cdef GLenum GL_MAX_SHADER_STORAGE_BLOCK_SIZE
cdef GLenum GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS
cdef GLenum GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS
cdef GLenum GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS
cdef GLenum GL_MAX_UNIFORM_LOCATIONS
cdef GLenum GL_MAX_VERTEX_ATTRIB_BINDINGS
cdef GLenum GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET
cdef GLenum GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS
cdef GLenum GL_MAX_WIDTH
cdef GLenum GL_MIPMAP
cdef GLenum GL_NAME_LENGTH
cdef GLenum GL_NUM_ACTIVE_VARIABLES
cdef GLenum GL_NUM_SHADING_LANGUAGE_VERSIONS
cdef GLenum GL_OFFSET
cdef GLenum GL_PRIMITIVE_RESTART_FIXED_INDEX
cdef GLenum GL_PROGRAM
cdef GLenum GL_PROGRAM_INPUT
cdef GLenum GL_PROGRAM_OUTPUT
cdef GLenum GL_PROGRAM_PIPELINE
cdef GLenum GL_QUERY
cdef GLenum GL_READ_PIXELS
cdef GLenum GL_READ_PIXELS_FORMAT
cdef GLenum GL_READ_PIXELS_TYPE
cdef GLenum GL_REFERENCED_BY_COMPUTE_SHADER
cdef GLenum GL_REFERENCED_BY_FRAGMENT_SHADER
cdef GLenum GL_REFERENCED_BY_GEOMETRY_SHADER
cdef GLenum GL_REFERENCED_BY_TESS_CONTROL_SHADER
cdef GLenum GL_REFERENCED_BY_TESS_EVALUATION_SHADER
cdef GLenum GL_REFERENCED_BY_VERTEX_SHADER
cdef GLenum GL_SAMPLER
cdef GLenum GL_SHADER
cdef GLenum GL_SHADER_IMAGE_ATOMIC
cdef GLenum GL_SHADER_IMAGE_LOAD
cdef GLenum GL_SHADER_IMAGE_STORE
cdef GLenum GL_SHADER_STORAGE_BARRIER_BIT
cdef GLenum GL_SHADER_STORAGE_BLOCK
cdef GLenum GL_SHADER_STORAGE_BUFFER
cdef GLenum GL_SHADER_STORAGE_BUFFER_BINDING
cdef GLenum GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT
cdef GLenum GL_SHADER_STORAGE_BUFFER_SIZE
cdef GLenum GL_SHADER_STORAGE_BUFFER_START
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE
cdef GLenum GL_SRGB_READ
cdef GLenum GL_SRGB_WRITE
cdef GLenum GL_STACK_OVERFLOW
cdef GLenum GL_STACK_UNDERFLOW
cdef GLenum GL_STENCIL_COMPONENTS
cdef GLenum GL_STENCIL_RENDERABLE
cdef GLenum GL_TESS_CONTROL_SUBROUTINE
cdef GLenum GL_TESS_CONTROL_SUBROUTINE_UNIFORM
cdef GLenum GL_TESS_CONTROL_TEXTURE
cdef GLenum GL_TESS_EVALUATION_SUBROUTINE
cdef GLenum GL_TESS_EVALUATION_SUBROUTINE_UNIFORM
cdef GLenum GL_TESS_EVALUATION_TEXTURE
cdef GLenum GL_TEXTURE_BUFFER_OFFSET
cdef GLenum GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT
cdef GLenum GL_TEXTURE_BUFFER_SIZE
cdef GLenum GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT
cdef GLenum GL_TEXTURE_COMPRESSED_BLOCK_SIZE
cdef GLenum GL_TEXTURE_COMPRESSED_BLOCK_WIDTH
cdef GLenum GL_TEXTURE_GATHER
cdef GLenum GL_TEXTURE_GATHER_SHADOW
cdef GLenum GL_TEXTURE_IMAGE_FORMAT
cdef GLenum GL_TEXTURE_IMAGE_TYPE
cdef GLenum GL_TEXTURE_IMMUTABLE_LEVELS
cdef GLenum GL_TEXTURE_SHADOW
cdef GLenum GL_TEXTURE_VIEW
cdef GLenum GL_TEXTURE_VIEW_MIN_LAYER
cdef GLenum GL_TEXTURE_VIEW_MIN_LEVEL
cdef GLenum GL_TEXTURE_VIEW_NUM_LAYERS
cdef GLenum GL_TEXTURE_VIEW_NUM_LEVELS
cdef GLenum GL_TOP_LEVEL_ARRAY_SIZE
cdef GLenum GL_TOP_LEVEL_ARRAY_STRIDE
cdef GLenum GL_TRANSFORM_FEEDBACK_VARYING
cdef GLenum GL_TYPE
cdef GLenum GL_UNIFORM
cdef GLenum GL_UNIFORM_BLOCK
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER
cdef GLenum GL_VERTEX_ARRAY
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_LONG
cdef GLenum GL_VERTEX_ATTRIB_BINDING
cdef GLenum GL_VERTEX_ATTRIB_RELATIVE_OFFSET
cdef GLenum GL_VERTEX_BINDING_BUFFER
cdef GLenum GL_VERTEX_BINDING_DIVISOR
cdef GLenum GL_VERTEX_BINDING_OFFSET
cdef GLenum GL_VERTEX_BINDING_STRIDE
cdef GLenum GL_VERTEX_SUBROUTINE
cdef GLenum GL_VERTEX_SUBROUTINE_UNIFORM
cdef GLenum GL_VERTEX_TEXTURE
cdef GLenum GL_VIEW_CLASS_128_BITS
cdef GLenum GL_VIEW_CLASS_16_BITS
cdef GLenum GL_VIEW_CLASS_24_BITS
cdef GLenum GL_VIEW_CLASS_32_BITS
cdef GLenum GL_VIEW_CLASS_48_BITS
cdef GLenum GL_VIEW_CLASS_64_BITS
cdef GLenum GL_VIEW_CLASS_8_BITS
cdef GLenum GL_VIEW_CLASS_96_BITS
cdef GLenum GL_VIEW_CLASS_BPTC_FLOAT
cdef GLenum GL_VIEW_CLASS_BPTC_UNORM
cdef GLenum GL_VIEW_CLASS_RGTC1_RED
cdef GLenum GL_VIEW_CLASS_RGTC2_RG
cdef GLenum GL_VIEW_CLASS_S3TC_DXT1_RGB
cdef GLenum GL_VIEW_CLASS_S3TC_DXT1_RGBA
cdef GLenum GL_VIEW_CLASS_S3TC_DXT3_RGBA
cdef GLenum GL_VIEW_CLASS_S3TC_DXT5_RGBA
cdef GLenum GL_VIEW_COMPATIBILITY_CLASS
cdef void glBindVertexBuffer(GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)
cdef void glClearBufferData(GLenum target, GLenum internalformat, GLenum format, GLenum type, const void *data)
cdef void glClearBufferSubData(GLenum target, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data)
cdef void glCopyImageSubData(GLuint srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei srcDepth)
cdef void glDebugMessageCallback(GLDEBUGPROC callback, const void *userParam)
cdef void glDebugMessageControl(GLenum source, GLenum type, GLenum severity, GLsizei count, const GLuint *ids, GLboolean enabled)
cdef void glDebugMessageInsert(GLenum source, GLenum type, GLuint id, GLenum severity, GLsizei length, const GLchar *buf)
cdef void glDispatchCompute(GLuint num_groups_x, GLuint num_groups_y, GLuint num_groups_z)
cdef void glDispatchComputeIndirect(GLintptr indirect)
cdef void glFramebufferParameteri(GLenum target, GLenum pname, GLint param)
cdef GLuint glGetDebugMessageLog(GLuint count, GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids, GLenum *severities, GLsizei *lengths, GLchar *messageLog)
cdef void glGetFramebufferParameteriv(GLenum target, GLenum pname, GLint *params)
cdef void glGetInternalformati64v(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint64 *params)
cdef void glGetObjectLabel(GLenum identifier, GLuint name, GLsizei bufSize, GLsizei *length, GLchar *label)
cdef void glGetObjectPtrLabel(const void *ptr, GLsizei bufSize, GLsizei *length, GLchar *label)
cdef void glGetPointerv(GLenum pname, void **params)
cdef void glGetProgramInterfaceiv(GLuint program, GLenum programInterface, GLenum pname, GLint *params)
cdef GLuint glGetProgramResourceIndex(GLuint program, GLenum programInterface, const GLchar *name)
cdef GLint glGetProgramResourceLocation(GLuint program, GLenum programInterface, const GLchar *name)
cdef GLint glGetProgramResourceLocationIndex(GLuint program, GLenum programInterface, const GLchar *name)
cdef void glGetProgramResourceName(GLuint program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
cdef void glGetProgramResourceiv(GLuint program, GLenum programInterface, GLuint index, GLsizei propCount, const GLenum *props, GLsizei count, GLsizei *length, GLint *params)
cdef void glInvalidateBufferData(GLuint buffer)
cdef void glInvalidateBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr length)
cdef void glInvalidateFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments)
cdef void glInvalidateSubFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height)
cdef void glInvalidateTexImage(GLuint texture, GLint level)
cdef void glInvalidateTexSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth)
cdef void glMultiDrawArraysIndirect(GLenum mode, const void *indirect, GLsizei drawcount, GLsizei stride)
cdef void glMultiDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei stride)
cdef void glObjectLabel(GLenum identifier, GLuint name, GLsizei length, const GLchar *label)
cdef void glObjectPtrLabel(const void *ptr, GLsizei length, const GLchar *label)
cdef void glPopDebugGroup()
cdef void glPushDebugGroup(GLenum source, GLuint id, GLsizei length, const GLchar *message)
cdef void glShaderStorageBlockBinding(GLuint program, GLuint storageBlockIndex, GLuint storageBlockBinding)
cdef void glTexBufferRange(GLenum target, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size)
cdef void glTexStorage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
cdef void glTexStorage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
cdef void glTextureView(GLuint texture, GLenum target, GLuint origtexture, GLenum internalformat, GLuint minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers)
cdef void glVertexAttribBinding(GLuint attribindex, GLuint bindingindex)
cdef void glVertexAttribFormat(GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset)
cdef void glVertexAttribIFormat(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
cdef void glVertexAttribLFormat(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
cdef void glVertexBindingDivisor(GLuint bindingindex, GLuint divisor)
