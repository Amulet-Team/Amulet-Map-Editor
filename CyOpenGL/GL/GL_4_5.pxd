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

cdef GLenum GL_BACK
cdef GLenum GL_CLIP_DEPTH_MODE
cdef GLenum GL_CLIP_ORIGIN
cdef GLenum GL_COLOR_TABLE
cdef GLenum GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT
cdef GLenum GL_CONTEXT_LOST
cdef GLenum GL_CONTEXT_RELEASE_BEHAVIOR
cdef GLenum GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH
cdef GLenum GL_CONVOLUTION_1D
cdef GLenum GL_CONVOLUTION_2D
cdef GLenum GL_GUILTY_CONTEXT_RESET
cdef GLenum GL_HISTOGRAM
cdef GLenum GL_INNOCENT_CONTEXT_RESET
cdef GLenum GL_LOSE_CONTEXT_ON_RESET
cdef GLenum GL_LOWER_LEFT
cdef GLenum GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES
cdef GLenum GL_MAX_CULL_DISTANCES
cdef GLenum GL_MINMAX
cdef GLenum GL_NEGATIVE_ONE_TO_ONE
cdef GLenum GL_NONE
cdef GLenum GL_NO_ERROR
cdef GLenum GL_NO_RESET_NOTIFICATION
cdef GLenum GL_POST_COLOR_MATRIX_COLOR_TABLE
cdef GLenum GL_POST_CONVOLUTION_COLOR_TABLE
cdef GLenum GL_PROXY_COLOR_TABLE
cdef GLenum GL_PROXY_HISTOGRAM
cdef GLenum GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE
cdef GLenum GL_PROXY_POST_CONVOLUTION_COLOR_TABLE
cdef GLenum GL_QUERY_BY_REGION_NO_WAIT_INVERTED
cdef GLenum GL_QUERY_BY_REGION_WAIT_INVERTED
cdef GLenum GL_QUERY_NO_WAIT_INVERTED
cdef GLenum GL_QUERY_TARGET
cdef GLenum GL_QUERY_WAIT_INVERTED
cdef GLenum GL_RESET_NOTIFICATION_STRATEGY
cdef GLenum GL_SEPARABLE_2D
cdef GLenum GL_TEXTURE_BINDING_1D
cdef GLenum GL_TEXTURE_BINDING_1D_ARRAY
cdef GLenum GL_TEXTURE_BINDING_2D
cdef GLenum GL_TEXTURE_BINDING_2D_ARRAY
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY
cdef GLenum GL_TEXTURE_BINDING_3D
cdef GLenum GL_TEXTURE_BINDING_BUFFER
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP_ARRAY
cdef GLenum GL_TEXTURE_BINDING_RECTANGLE
cdef GLenum GL_TEXTURE_TARGET
cdef GLenum GL_UNKNOWN_CONTEXT_RESET
cdef GLenum GL_UPPER_LEFT
cdef GLenum GL_ZERO_TO_ONE
cdef void glBindTextureUnit(GLuint unit, GLuint texture)
cdef void glBlitNamedFramebuffer(GLuint readFramebuffer, GLuint drawFramebuffer, GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
cdef GLenum glCheckNamedFramebufferStatus(GLuint framebuffer, GLenum target)
cdef void glClearNamedBufferData(GLuint buffer, GLenum internalformat, GLenum format, GLenum type, const void *data)
cdef void glClearNamedBufferSubData(GLuint buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data)
cdef void glClearNamedFramebufferfi(GLuint framebuffer, GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil)
cdef void glClearNamedFramebufferfv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat *value)
cdef void glClearNamedFramebufferiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLint *value)
cdef void glClearNamedFramebufferuiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLuint *value)
cdef void glClipControl(GLenum origin, GLenum depth)
cdef void glCompressedTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data)
cdef void glCompressedTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data)
cdef void glCompressedTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data)
cdef void glCopyNamedBufferSubData(GLuint readBuffer, GLuint writeBuffer, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size)
cdef void glCopyTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
cdef void glCopyTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
cdef void glCopyTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height)
cdef void glCreateBuffers(GLsizei n, GLuint *buffers)
cdef void glCreateFramebuffers(GLsizei n, GLuint *framebuffers)
cdef void glCreateProgramPipelines(GLsizei n, GLuint *pipelines)
cdef void glCreateQueries(GLenum target, GLsizei n, GLuint *ids)
cdef void glCreateRenderbuffers(GLsizei n, GLuint *renderbuffers)
cdef void glCreateSamplers(GLsizei n, GLuint *samplers)
cdef void glCreateTextures(GLenum target, GLsizei n, GLuint *textures)
cdef void glCreateTransformFeedbacks(GLsizei n, GLuint *ids)
cdef void glCreateVertexArrays(GLsizei n, GLuint *arrays)
cdef void glDisableVertexArrayAttrib(GLuint vaobj, GLuint index)
cdef void glEnableVertexArrayAttrib(GLuint vaobj, GLuint index)
cdef void glFlushMappedNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length)
cdef void glGenerateTextureMipmap(GLuint texture)
cdef void glGetCompressedTextureImage(GLuint texture, GLint level, GLsizei bufSize, void *pixels)
cdef void glGetCompressedTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei bufSize, void *pixels)
cdef GLenum glGetGraphicsResetStatus()
cdef void glGetNamedBufferParameteri64v(GLuint buffer, GLenum pname, GLint64 *params)
cdef void glGetNamedBufferParameteriv(GLuint buffer, GLenum pname, GLint *params)
cdef void glGetNamedBufferPointerv(GLuint buffer, GLenum pname, void **params)
cdef void glGetNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, void *data)
cdef void glGetNamedFramebufferAttachmentParameteriv(GLuint framebuffer, GLenum attachment, GLenum pname, GLint *params)
cdef void glGetNamedFramebufferParameteriv(GLuint framebuffer, GLenum pname, GLint *param)
cdef void glGetNamedRenderbufferParameteriv(GLuint renderbuffer, GLenum pname, GLint *params)
cdef void glGetQueryBufferObjecti64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
cdef void glGetQueryBufferObjectiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
cdef void glGetQueryBufferObjectui64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
cdef void glGetQueryBufferObjectuiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
cdef void glGetTextureImage(GLuint texture, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
cdef void glGetTextureLevelParameterfv(GLuint texture, GLint level, GLenum pname, GLfloat *params)
cdef void glGetTextureLevelParameteriv(GLuint texture, GLint level, GLenum pname, GLint *params)
cdef void glGetTextureParameterIiv(GLuint texture, GLenum pname, GLint *params)
cdef void glGetTextureParameterIuiv(GLuint texture, GLenum pname, GLuint *params)
cdef void glGetTextureParameterfv(GLuint texture, GLenum pname, GLfloat *params)
cdef void glGetTextureParameteriv(GLuint texture, GLenum pname, GLint *params)
cdef void glGetTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
cdef void glGetTransformFeedbacki64_v(GLuint xfb, GLenum pname, GLuint index, GLint64 *param)
cdef void glGetTransformFeedbacki_v(GLuint xfb, GLenum pname, GLuint index, GLint *param)
cdef void glGetTransformFeedbackiv(GLuint xfb, GLenum pname, GLint *param)
cdef void glGetVertexArrayIndexed64iv(GLuint vaobj, GLuint index, GLenum pname, GLint64 *param)
cdef void glGetVertexArrayIndexediv(GLuint vaobj, GLuint index, GLenum pname, GLint *param)
cdef void glGetVertexArrayiv(GLuint vaobj, GLenum pname, GLint *param)
cdef void glGetnColorTable(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *table)
cdef void glGetnCompressedTexImage(GLenum target, GLint lod, GLsizei bufSize, void *pixels)
cdef void glGetnConvolutionFilter(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *image)
cdef void glGetnHistogram(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values)
cdef void glGetnMapdv(GLenum target, GLenum query, GLsizei bufSize, GLdouble *v)
cdef void glGetnMapfv(GLenum target, GLenum query, GLsizei bufSize, GLfloat *v)
cdef void glGetnMapiv(GLenum target, GLenum query, GLsizei bufSize, GLint *v)
cdef void glGetnMinmax(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values)
cdef void glGetnPixelMapfv(GLenum map, GLsizei bufSize, GLfloat *values)
cdef void glGetnPixelMapuiv(GLenum map, GLsizei bufSize, GLuint *values)
cdef void glGetnPixelMapusv(GLenum map, GLsizei bufSize, GLushort *values)
cdef void glGetnPolygonStipple(GLsizei bufSize, GLubyte *pattern)
cdef void glGetnSeparableFilter(GLenum target, GLenum format, GLenum type, GLsizei rowBufSize, void *row, GLsizei columnBufSize, void *column, void *span)
cdef void glGetnTexImage(GLenum target, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
cdef void glGetnUniformdv(GLuint program, GLint location, GLsizei bufSize, GLdouble *params)
cdef void glGetnUniformfv(GLuint program, GLint location, GLsizei bufSize, GLfloat *params)
cdef void glGetnUniformiv(GLuint program, GLint location, GLsizei bufSize, GLint *params)
cdef void glGetnUniformuiv(GLuint program, GLint location, GLsizei bufSize, GLuint *params)
cdef void glInvalidateNamedFramebufferData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments)
cdef void glInvalidateNamedFramebufferSubData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height)
cdef void *glMapNamedBuffer(GLuint buffer, GLenum access)
cdef void *glMapNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length, GLbitfield access)
cdef void glMemoryBarrierByRegion(GLbitfield barriers)
cdef void glNamedBufferData(GLuint buffer, GLsizeiptr size, const void *data, GLenum usage)
cdef void glNamedBufferStorage(GLuint buffer, GLsizeiptr size, const void *data, GLbitfield flags)
cdef void glNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, const void *data)
cdef void glNamedFramebufferDrawBuffer(GLuint framebuffer, GLenum buf)
cdef void glNamedFramebufferDrawBuffers(GLuint framebuffer, GLsizei n, const GLenum *bufs)
cdef void glNamedFramebufferParameteri(GLuint framebuffer, GLenum pname, GLint param)
cdef void glNamedFramebufferReadBuffer(GLuint framebuffer, GLenum src)
cdef void glNamedFramebufferRenderbuffer(GLuint framebuffer, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
cdef void glNamedFramebufferTexture(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level)
cdef void glNamedFramebufferTextureLayer(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level, GLint layer)
cdef void glNamedRenderbufferStorage(GLuint renderbuffer, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glNamedRenderbufferStorageMultisample(GLuint renderbuffer, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glReadnPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei bufSize, void *data)
cdef void glTextureBarrier()
cdef void glTextureBuffer(GLuint texture, GLenum internalformat, GLuint buffer)
cdef void glTextureBufferRange(GLuint texture, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size)
cdef void glTextureParameterIiv(GLuint texture, GLenum pname, const GLint *params)
cdef void glTextureParameterIuiv(GLuint texture, GLenum pname, const GLuint *params)
cdef void glTextureParameterf(GLuint texture, GLenum pname, GLfloat param)
cdef void glTextureParameterfv(GLuint texture, GLenum pname, const GLfloat *param)
cdef void glTextureParameteri(GLuint texture, GLenum pname, GLint param)
cdef void glTextureParameteriv(GLuint texture, GLenum pname, const GLint *param)
cdef void glTextureStorage1D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width)
cdef void glTextureStorage2D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glTextureStorage2DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
cdef void glTextureStorage3D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth)
cdef void glTextureStorage3DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
cdef void glTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels)
cdef void glTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
cdef void glTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels)
cdef void glTransformFeedbackBufferBase(GLuint xfb, GLuint index, GLuint buffer)
cdef void glTransformFeedbackBufferRange(GLuint xfb, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
cdef GLboolean glUnmapNamedBuffer(GLuint buffer)
cdef void glVertexArrayAttribBinding(GLuint vaobj, GLuint attribindex, GLuint bindingindex)
cdef void glVertexArrayAttribFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset)
cdef void glVertexArrayAttribIFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
cdef void glVertexArrayAttribLFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
cdef void glVertexArrayBindingDivisor(GLuint vaobj, GLuint bindingindex, GLuint divisor)
cdef void glVertexArrayElementBuffer(GLuint vaobj, GLuint buffer)
cdef void glVertexArrayVertexBuffer(GLuint vaobj, GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)
cdef void glVertexArrayVertexBuffers(GLuint vaobj, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides)
