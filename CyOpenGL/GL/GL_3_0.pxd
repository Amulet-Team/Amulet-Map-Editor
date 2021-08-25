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

cdef GLenum GL_ALPHA_INTEGER
cdef GLenum GL_BGRA_INTEGER
cdef GLenum GL_BGR_INTEGER
cdef GLenum GL_BLUE_INTEGER
cdef GLenum GL_BUFFER_ACCESS_FLAGS
cdef GLenum GL_BUFFER_MAP_LENGTH
cdef GLenum GL_BUFFER_MAP_OFFSET
cdef GLenum GL_CLAMP_FRAGMENT_COLOR
cdef GLenum GL_CLAMP_READ_COLOR
cdef GLenum GL_CLAMP_VERTEX_COLOR
cdef GLenum GL_CLIP_DISTANCE0
cdef GLenum GL_CLIP_DISTANCE1
cdef GLenum GL_CLIP_DISTANCE2
cdef GLenum GL_CLIP_DISTANCE3
cdef GLenum GL_CLIP_DISTANCE4
cdef GLenum GL_CLIP_DISTANCE5
cdef GLenum GL_CLIP_DISTANCE6
cdef GLenum GL_CLIP_DISTANCE7
cdef GLenum GL_COLOR_ATTACHMENT0
cdef GLenum GL_COLOR_ATTACHMENT1
cdef GLenum GL_COLOR_ATTACHMENT10
cdef GLenum GL_COLOR_ATTACHMENT11
cdef GLenum GL_COLOR_ATTACHMENT12
cdef GLenum GL_COLOR_ATTACHMENT13
cdef GLenum GL_COLOR_ATTACHMENT14
cdef GLenum GL_COLOR_ATTACHMENT15
cdef GLenum GL_COLOR_ATTACHMENT16
cdef GLenum GL_COLOR_ATTACHMENT17
cdef GLenum GL_COLOR_ATTACHMENT18
cdef GLenum GL_COLOR_ATTACHMENT19
cdef GLenum GL_COLOR_ATTACHMENT2
cdef GLenum GL_COLOR_ATTACHMENT20
cdef GLenum GL_COLOR_ATTACHMENT21
cdef GLenum GL_COLOR_ATTACHMENT22
cdef GLenum GL_COLOR_ATTACHMENT23
cdef GLenum GL_COLOR_ATTACHMENT24
cdef GLenum GL_COLOR_ATTACHMENT25
cdef GLenum GL_COLOR_ATTACHMENT26
cdef GLenum GL_COLOR_ATTACHMENT27
cdef GLenum GL_COLOR_ATTACHMENT28
cdef GLenum GL_COLOR_ATTACHMENT29
cdef GLenum GL_COLOR_ATTACHMENT3
cdef GLenum GL_COLOR_ATTACHMENT30
cdef GLenum GL_COLOR_ATTACHMENT31
cdef GLenum GL_COLOR_ATTACHMENT4
cdef GLenum GL_COLOR_ATTACHMENT5
cdef GLenum GL_COLOR_ATTACHMENT6
cdef GLenum GL_COLOR_ATTACHMENT7
cdef GLenum GL_COLOR_ATTACHMENT8
cdef GLenum GL_COLOR_ATTACHMENT9
cdef GLenum GL_COMPARE_REF_TO_TEXTURE
cdef GLenum GL_COMPRESSED_RED
cdef GLenum GL_COMPRESSED_RED_RGTC1
cdef GLenum GL_COMPRESSED_RG
cdef GLenum GL_COMPRESSED_RG_RGTC2
cdef GLenum GL_COMPRESSED_SIGNED_RED_RGTC1
cdef GLenum GL_COMPRESSED_SIGNED_RG_RGTC2
cdef GLenum GL_CONTEXT_FLAGS
cdef GLenum GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT
cdef GLenum GL_DEPTH24_STENCIL8
cdef GLenum GL_DEPTH32F_STENCIL8
cdef GLenum GL_DEPTH_ATTACHMENT
cdef GLenum GL_DEPTH_COMPONENT32F
cdef GLenum GL_DEPTH_STENCIL
cdef GLenum GL_DEPTH_STENCIL_ATTACHMENT
cdef GLenum GL_DRAW_FRAMEBUFFER
cdef GLenum GL_DRAW_FRAMEBUFFER_BINDING
cdef GLenum GL_FIXED_ONLY
cdef GLenum GL_FLOAT_32_UNSIGNED_INT_24_8_REV
cdef GLenum GL_FRAMEBUFFER
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL
cdef GLenum GL_FRAMEBUFFER_BINDING
cdef GLenum GL_FRAMEBUFFER_COMPLETE
cdef GLenum GL_FRAMEBUFFER_DEFAULT
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER
cdef GLenum GL_FRAMEBUFFER_SRGB
cdef GLenum GL_FRAMEBUFFER_UNDEFINED
cdef GLenum GL_FRAMEBUFFER_UNSUPPORTED
cdef GLenum GL_GREEN_INTEGER
cdef GLenum GL_HALF_FLOAT
cdef GLenum GL_INDEX
cdef GLenum GL_INTERLEAVED_ATTRIBS
cdef GLenum GL_INT_SAMPLER_1D
cdef GLenum GL_INT_SAMPLER_1D_ARRAY
cdef GLenum GL_INT_SAMPLER_2D
cdef GLenum GL_INT_SAMPLER_2D_ARRAY
cdef GLenum GL_INT_SAMPLER_3D
cdef GLenum GL_INT_SAMPLER_CUBE
cdef GLenum GL_INVALID_FRAMEBUFFER_OPERATION
cdef GLenum GL_MAJOR_VERSION
cdef GLenum GL_MAP_FLUSH_EXPLICIT_BIT
cdef GLenum GL_MAP_INVALIDATE_BUFFER_BIT
cdef GLenum GL_MAP_INVALIDATE_RANGE_BIT
cdef GLenum GL_MAP_READ_BIT
cdef GLenum GL_MAP_UNSYNCHRONIZED_BIT
cdef GLenum GL_MAP_WRITE_BIT
cdef GLenum GL_MAX_ARRAY_TEXTURE_LAYERS
cdef GLenum GL_MAX_CLIP_DISTANCES
cdef GLenum GL_MAX_COLOR_ATTACHMENTS
cdef GLenum GL_MAX_PROGRAM_TEXEL_OFFSET
cdef GLenum GL_MAX_RENDERBUFFER_SIZE
cdef GLenum GL_MAX_SAMPLES
cdef GLenum GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS
cdef GLenum GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS
cdef GLenum GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS
cdef GLenum GL_MAX_VARYING_COMPONENTS
cdef GLenum GL_MINOR_VERSION
cdef GLenum GL_MIN_PROGRAM_TEXEL_OFFSET
cdef GLenum GL_NUM_EXTENSIONS
cdef GLenum GL_PRIMITIVES_GENERATED
cdef GLenum GL_PROXY_TEXTURE_1D_ARRAY
cdef GLenum GL_PROXY_TEXTURE_2D_ARRAY
cdef GLenum GL_QUERY_BY_REGION_NO_WAIT
cdef GLenum GL_QUERY_BY_REGION_WAIT
cdef GLenum GL_QUERY_NO_WAIT
cdef GLenum GL_QUERY_WAIT
cdef GLenum GL_R11F_G11F_B10F
cdef GLenum GL_R16
cdef GLenum GL_R16F
cdef GLenum GL_R16I
cdef GLenum GL_R16UI
cdef GLenum GL_R32F
cdef GLenum GL_R32I
cdef GLenum GL_R32UI
cdef GLenum GL_R8
cdef GLenum GL_R8I
cdef GLenum GL_R8UI
cdef GLenum GL_RASTERIZER_DISCARD
cdef GLenum GL_READ_FRAMEBUFFER
cdef GLenum GL_READ_FRAMEBUFFER_BINDING
cdef GLenum GL_RED_INTEGER
cdef GLenum GL_RENDERBUFFER
cdef GLenum GL_RENDERBUFFER_ALPHA_SIZE
cdef GLenum GL_RENDERBUFFER_BINDING
cdef GLenum GL_RENDERBUFFER_BLUE_SIZE
cdef GLenum GL_RENDERBUFFER_DEPTH_SIZE
cdef GLenum GL_RENDERBUFFER_GREEN_SIZE
cdef GLenum GL_RENDERBUFFER_HEIGHT
cdef GLenum GL_RENDERBUFFER_INTERNAL_FORMAT
cdef GLenum GL_RENDERBUFFER_RED_SIZE
cdef GLenum GL_RENDERBUFFER_SAMPLES
cdef GLenum GL_RENDERBUFFER_STENCIL_SIZE
cdef GLenum GL_RENDERBUFFER_WIDTH
cdef GLenum GL_RG
cdef GLenum GL_RG16
cdef GLenum GL_RG16F
cdef GLenum GL_RG16I
cdef GLenum GL_RG16UI
cdef GLenum GL_RG32F
cdef GLenum GL_RG32I
cdef GLenum GL_RG32UI
cdef GLenum GL_RG8
cdef GLenum GL_RG8I
cdef GLenum GL_RG8UI
cdef GLenum GL_RGB16F
cdef GLenum GL_RGB16I
cdef GLenum GL_RGB16UI
cdef GLenum GL_RGB32F
cdef GLenum GL_RGB32I
cdef GLenum GL_RGB32UI
cdef GLenum GL_RGB8I
cdef GLenum GL_RGB8UI
cdef GLenum GL_RGB9_E5
cdef GLenum GL_RGBA16F
cdef GLenum GL_RGBA16I
cdef GLenum GL_RGBA16UI
cdef GLenum GL_RGBA32F
cdef GLenum GL_RGBA32I
cdef GLenum GL_RGBA32UI
cdef GLenum GL_RGBA8I
cdef GLenum GL_RGBA8UI
cdef GLenum GL_RGBA_INTEGER
cdef GLenum GL_RGB_INTEGER
cdef GLenum GL_RG_INTEGER
cdef GLenum GL_SAMPLER_1D_ARRAY
cdef GLenum GL_SAMPLER_1D_ARRAY_SHADOW
cdef GLenum GL_SAMPLER_2D_ARRAY
cdef GLenum GL_SAMPLER_2D_ARRAY_SHADOW
cdef GLenum GL_SAMPLER_CUBE_SHADOW
cdef GLenum GL_SEPARATE_ATTRIBS
cdef GLenum GL_STENCIL_ATTACHMENT
cdef GLenum GL_STENCIL_INDEX1
cdef GLenum GL_STENCIL_INDEX16
cdef GLenum GL_STENCIL_INDEX4
cdef GLenum GL_STENCIL_INDEX8
cdef GLenum GL_TEXTURE_1D_ARRAY
cdef GLenum GL_TEXTURE_2D_ARRAY
cdef GLenum GL_TEXTURE_ALPHA_TYPE
cdef GLenum GL_TEXTURE_BINDING_1D_ARRAY
cdef GLenum GL_TEXTURE_BINDING_2D_ARRAY
cdef GLenum GL_TEXTURE_BLUE_TYPE
cdef GLenum GL_TEXTURE_DEPTH_TYPE
cdef GLenum GL_TEXTURE_GREEN_TYPE
cdef GLenum GL_TEXTURE_INTENSITY_TYPE
cdef GLenum GL_TEXTURE_LUMINANCE_TYPE
cdef GLenum GL_TEXTURE_RED_TYPE
cdef GLenum GL_TEXTURE_SHARED_SIZE
cdef GLenum GL_TEXTURE_STENCIL_SIZE
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_BINDING
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_MODE
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_SIZE
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_START
cdef GLenum GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN
cdef GLenum GL_TRANSFORM_FEEDBACK_VARYINGS
cdef GLenum GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH
cdef GLenum GL_UNSIGNED_INT_10F_11F_11F_REV
cdef GLenum GL_UNSIGNED_INT_24_8
cdef GLenum GL_UNSIGNED_INT_5_9_9_9_REV
cdef GLenum GL_UNSIGNED_INT_SAMPLER_1D
cdef GLenum GL_UNSIGNED_INT_SAMPLER_1D_ARRAY
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_ARRAY
cdef GLenum GL_UNSIGNED_INT_SAMPLER_3D
cdef GLenum GL_UNSIGNED_INT_SAMPLER_CUBE
cdef GLenum GL_UNSIGNED_INT_VEC2
cdef GLenum GL_UNSIGNED_INT_VEC3
cdef GLenum GL_UNSIGNED_INT_VEC4
cdef GLenum GL_UNSIGNED_NORMALIZED
cdef GLenum GL_VERTEX_ARRAY_BINDING
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_INTEGER
cdef void glBeginConditionalRender(GLuint id, GLenum mode)
cdef void glBeginTransformFeedback(GLenum primitiveMode)
cdef void glBindBufferBase(GLenum target, GLuint index, GLuint buffer)
cdef void glBindBufferRange(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
cdef void glBindFragDataLocation(GLuint program, GLuint color, const GLchar *name)
cdef void glBindFramebuffer(GLenum target, GLuint framebuffer)
cdef void glBindRenderbuffer(GLenum target, GLuint renderbuffer)
cdef void glBindVertexArray(GLuint array)
cdef void glBlitFramebuffer(GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
cdef GLenum glCheckFramebufferStatus(GLenum target)
cdef void glClampColor(GLenum target, GLenum clamp)
cdef void glClearBufferfi(GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil)
cdef void glClearBufferfv(GLenum buffer, GLint drawbuffer, const GLfloat *value)
cdef void glClearBufferiv(GLenum buffer, GLint drawbuffer, const GLint *value)
cdef void glClearBufferuiv(GLenum buffer, GLint drawbuffer, const GLuint *value)
cdef void glColorMaski(GLuint index, GLboolean r, GLboolean g, GLboolean b, GLboolean a)
cdef void glDeleteFramebuffers(GLsizei n, const GLuint *framebuffers)
cdef void glDeleteRenderbuffers(GLsizei n, const GLuint *renderbuffers)
cdef void glDeleteVertexArrays(GLsizei n, const GLuint *arrays)
cdef void glDisablei(GLenum target, GLuint index)
cdef void glEnablei(GLenum target, GLuint index)
cdef void glEndConditionalRender()
cdef void glEndTransformFeedback()
cdef void glFlushMappedBufferRange(GLenum target, GLintptr offset, GLsizeiptr length)
cdef void glFramebufferRenderbuffer(GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
cdef void glFramebufferTexture1D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level)
cdef void glFramebufferTexture2D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level)
cdef void glFramebufferTexture3D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level, GLint zoffset)
cdef void glFramebufferTextureLayer(GLenum target, GLenum attachment, GLuint texture, GLint level, GLint layer)
cdef void glGenFramebuffers(GLsizei n, GLuint *framebuffers)
cdef void glGenRenderbuffers(GLsizei n, GLuint *renderbuffers)
cdef void glGenVertexArrays(GLsizei n, GLuint *arrays)
cdef void glGenerateMipmap(GLenum target)
cdef void glGetBooleani_v(GLenum target, GLuint index, GLboolean *data)
cdef GLint glGetFragDataLocation(GLuint program, const GLchar *name)
cdef void glGetFramebufferAttachmentParameteriv(GLenum target, GLenum attachment, GLenum pname, GLint *params)
cdef void glGetIntegeri_v(GLenum target, GLuint index, GLint *data)
cdef void glGetRenderbufferParameteriv(GLenum target, GLenum pname, GLint *params)
cdef const GLubyte *glGetStringi(GLenum name, GLuint index)
cdef void glGetTexParameterIiv(GLenum target, GLenum pname, GLint *params)
cdef void glGetTexParameterIuiv(GLenum target, GLenum pname, GLuint *params)
cdef void glGetTransformFeedbackVarying(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum *type, GLchar *name)
cdef void glGetUniformuiv(GLuint program, GLint location, GLuint *params)
cdef void glGetVertexAttribIiv(GLuint index, GLenum pname, GLint *params)
cdef void glGetVertexAttribIuiv(GLuint index, GLenum pname, GLuint *params)
cdef GLboolean glIsEnabledi(GLenum target, GLuint index)
cdef GLboolean glIsFramebuffer(GLuint framebuffer)
cdef GLboolean glIsRenderbuffer(GLuint renderbuffer)
cdef GLboolean glIsVertexArray(GLuint array)
cdef void *glMapBufferRange(GLenum target, GLintptr offset, GLsizeiptr length, GLbitfield access)
cdef void glRenderbufferStorage(GLenum target, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glRenderbufferStorageMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glTexParameterIiv(GLenum target, GLenum pname, const GLint *params)
cdef void glTexParameterIuiv(GLenum target, GLenum pname, const GLuint *params)
cdef void glTransformFeedbackVaryings(GLuint program, GLsizei count, const GLchar **varyings, GLenum bufferMode)
cdef void glUniform1ui(GLint location, GLuint v0)
cdef void glUniform1uiv(GLint location, GLsizei count, const GLuint *value)
cdef void glUniform2ui(GLint location, GLuint v0, GLuint v1)
cdef void glUniform2uiv(GLint location, GLsizei count, const GLuint *value)
cdef void glUniform3ui(GLint location, GLuint v0, GLuint v1, GLuint v2)
cdef void glUniform3uiv(GLint location, GLsizei count, const GLuint *value)
cdef void glUniform4ui(GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
cdef void glUniform4uiv(GLint location, GLsizei count, const GLuint *value)
cdef void glVertexAttribI1i(GLuint index, GLint x)
cdef void glVertexAttribI1iv(GLuint index, const GLint *v)
cdef void glVertexAttribI1ui(GLuint index, GLuint x)
cdef void glVertexAttribI1uiv(GLuint index, const GLuint *v)
cdef void glVertexAttribI2i(GLuint index, GLint x, GLint y)
cdef void glVertexAttribI2iv(GLuint index, const GLint *v)
cdef void glVertexAttribI2ui(GLuint index, GLuint x, GLuint y)
cdef void glVertexAttribI2uiv(GLuint index, const GLuint *v)
cdef void glVertexAttribI3i(GLuint index, GLint x, GLint y, GLint z)
cdef void glVertexAttribI3iv(GLuint index, const GLint *v)
cdef void glVertexAttribI3ui(GLuint index, GLuint x, GLuint y, GLuint z)
cdef void glVertexAttribI3uiv(GLuint index, const GLuint *v)
cdef void glVertexAttribI4bv(GLuint index, const GLbyte *v)
cdef void glVertexAttribI4i(GLuint index, GLint x, GLint y, GLint z, GLint w)
cdef void glVertexAttribI4iv(GLuint index, const GLint *v)
cdef void glVertexAttribI4sv(GLuint index, const GLshort *v)
cdef void glVertexAttribI4ubv(GLuint index, const GLubyte *v)
cdef void glVertexAttribI4ui(GLuint index, GLuint x, GLuint y, GLuint z, GLuint w)
cdef void glVertexAttribI4uiv(GLuint index, const GLuint *v)
cdef void glVertexAttribI4usv(GLuint index, const GLushort *v)
cdef void glVertexAttribIPointer(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer)
