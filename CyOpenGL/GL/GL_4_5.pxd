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
cdef void glCreateSamplers(GLsizei n, GLuint *samplers)
cdef void glVertexArrayVertexBuffers(GLuint vaobj, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides)
cdef void glTextureParameterf(GLuint texture, GLenum pname, GLfloat param)
cdef void glClearNamedBufferData(GLuint buffer, GLenum internalformat, GLenum format, GLenum type, const void *data)
cdef void glVertexArrayAttribFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset)
cdef void glGetnConvolutionFilter(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *image)
cdef void glNamedFramebufferDrawBuffers(GLuint framebuffer, GLsizei n, const GLenum *bufs)
cdef void glNamedBufferData(GLuint buffer, GLsizeiptr size, const void *data, GLenum usage)
cdef void glBindTextureUnit(GLuint unit, GLuint texture)
cdef void glVertexArrayAttribBinding(GLuint vaobj, GLuint attribindex, GLuint bindingindex)
cdef void glTextureStorage2DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
cdef void glFlushMappedNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length)
cdef void glGetQueryBufferObjectui64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
cdef void glDisableVertexArrayAttrib(GLuint vaobj, GLuint index)
cdef void glGetTextureLevelParameterfv(GLuint texture, GLint level, GLenum pname, GLfloat *params)
cdef void glCreateTransformFeedbacks(GLsizei n, GLuint *ids)
cdef void glClearNamedFramebufferuiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLuint *value)
cdef void glGetnPixelMapfv(GLenum map, GLsizei bufSize, GLfloat *values)
cdef void glNamedFramebufferReadBuffer(GLuint framebuffer, GLenum src)
cdef void glCreateRenderbuffers(GLsizei n, GLuint *renderbuffers)
cdef void glCreateVertexArrays(GLsizei n, GLuint *arrays)
cdef void glGetNamedFramebufferAttachmentParameteriv(GLuint framebuffer, GLenum attachment, GLenum pname, GLint *params)
cdef void glNamedFramebufferDrawBuffer(GLuint framebuffer, GLenum buf)
cdef void glCreateBuffers(GLsizei n, GLuint *buffers)
cdef void glGetTextureParameterfv(GLuint texture, GLenum pname, GLfloat *params)
cdef void glCompressedTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data)
cdef void glTextureBufferRange(GLuint texture, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size)
cdef void glTextureBarrier()
cdef void glTextureParameterfv(GLuint texture, GLenum pname, const GLfloat *param)
cdef void glInvalidateNamedFramebufferSubData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height)
cdef void glTextureBuffer(GLuint texture, GLenum internalformat, GLuint buffer)
cdef void glTextureParameteri(GLuint texture, GLenum pname, GLint param)
cdef void glTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels)
cdef void glCompressedTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data)
cdef void glGetnCompressedTexImage(GLenum target, GLint lod, GLsizei bufSize, void *pixels)
cdef void glGetnTexImage(GLenum target, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
cdef GLenum glGetGraphicsResetStatus()
cdef void glCreateFramebuffers(GLsizei n, GLuint *framebuffers)
cdef void glCreateProgramPipelines(GLsizei n, GLuint *pipelines)
cdef void glTextureStorage2D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glNamedRenderbufferStorageMultisample(GLuint renderbuffer, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glVertexArrayBindingDivisor(GLuint vaobj, GLuint bindingindex, GLuint divisor)
cdef void glGetVertexArrayIndexediv(GLuint vaobj, GLuint index, GLenum pname, GLint *param)
cdef void glGetnSeparableFilter(GLenum target, GLenum format, GLenum type, GLsizei rowBufSize, void *row, GLsizei columnBufSize, void *column, void *span)
cdef void glGetnColorTable(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *table)
cdef void glGetTextureImage(GLuint texture, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
cdef GLenum glCheckNamedFramebufferStatus(GLuint framebuffer, GLenum target)
cdef void glClearNamedFramebufferfv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat *value)
cdef void glGetNamedFramebufferParameteriv(GLuint framebuffer, GLenum pname, GLint *param)
cdef void glVertexArrayElementBuffer(GLuint vaobj, GLuint buffer)
cdef void glTransformFeedbackBufferRange(GLuint xfb, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
cdef void glNamedFramebufferParameteri(GLuint framebuffer, GLenum pname, GLint param)
cdef void glMemoryBarrierByRegion(GLbitfield barriers)
cdef void glNamedBufferStorage(GLuint buffer, GLsizeiptr size, const void *data, GLbitfield flags)
cdef void glGetnPolygonStipple(GLsizei bufSize, GLubyte *pattern)
cdef void glTextureParameteriv(GLuint texture, GLenum pname, const GLint *param)
cdef void glGetCompressedTextureImage(GLuint texture, GLint level, GLsizei bufSize, void *pixels)
cdef void glTextureParameterIuiv(GLuint texture, GLenum pname, const GLuint *params)
cdef void glTextureStorage1D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width)
cdef void glGetnUniformiv(GLuint program, GLint location, GLsizei bufSize, GLint *params)
cdef void glGetTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
cdef void glBlitNamedFramebuffer(GLuint readFramebuffer, GLuint drawFramebuffer, GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
cdef void *glMapNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length, GLbitfield access)
cdef void glNamedRenderbufferStorage(GLuint renderbuffer, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glGetTextureLevelParameteriv(GLuint texture, GLint level, GLenum pname, GLint *params)
cdef void glGetCompressedTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei bufSize, void *pixels)
cdef void glCreateTextures(GLenum target, GLsizei n, GLuint *textures)
cdef void glGetNamedRenderbufferParameteriv(GLuint renderbuffer, GLenum pname, GLint *params)
cdef void glGetQueryBufferObjectiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
cdef void glGetnUniformuiv(GLuint program, GLint location, GLsizei bufSize, GLuint *params)
cdef void glClipControl(GLenum origin, GLenum depth)
cdef void glGetTransformFeedbacki_v(GLuint xfb, GLenum pname, GLuint index, GLint *param)
cdef GLboolean glUnmapNamedBuffer(GLuint buffer)
cdef void glCreateQueries(GLenum target, GLsizei n, GLuint *ids)
cdef void glTextureStorage3DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
cdef void glVertexArrayVertexBuffer(GLuint vaobj, GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)
cdef void glGetTextureParameterIuiv(GLuint texture, GLenum pname, GLuint *params)
cdef void glClearNamedBufferSubData(GLuint buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data)
cdef void glGetnMapiv(GLenum target, GLenum query, GLsizei bufSize, GLint *v)
cdef void glGetTextureParameteriv(GLuint texture, GLenum pname, GLint *params)
cdef void glGetTransformFeedbacki64_v(GLuint xfb, GLenum pname, GLuint index, GLint64 *param)
cdef void glVertexArrayAttribLFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
cdef void glTextureParameterIiv(GLuint texture, GLenum pname, const GLint *params)
cdef void glGetQueryBufferObjectuiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
cdef void glGetnUniformdv(GLuint program, GLint location, GLsizei bufSize, GLdouble *params)
cdef void glCopyTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height)
cdef void glTextureStorage3D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth)
cdef void glGetnMapdv(GLenum target, GLenum query, GLsizei bufSize, GLdouble *v)
cdef void glGetQueryBufferObjecti64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
cdef void glGetNamedBufferPointerv(GLuint buffer, GLenum pname, void **params)
cdef void glClearNamedFramebufferiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLint *value)
cdef void glTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
cdef void glGetVertexArrayIndexed64iv(GLuint vaobj, GLuint index, GLenum pname, GLint64 *param)
cdef void glClearNamedFramebufferfi(GLuint framebuffer, GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil)
cdef void glTransformFeedbackBufferBase(GLuint xfb, GLuint index, GLuint buffer)
cdef void glNamedFramebufferTextureLayer(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level, GLint layer)
cdef void glGetnMinmax(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values)
cdef void glCopyTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
cdef void glGetnUniformfv(GLuint program, GLint location, GLsizei bufSize, GLfloat *params)
cdef void glGetNamedBufferParameteri64v(GLuint buffer, GLenum pname, GLint64 *params)
cdef void glGetNamedBufferParameteriv(GLuint buffer, GLenum pname, GLint *params)
cdef void glGetVertexArrayiv(GLuint vaobj, GLenum pname, GLint *param)
cdef void glCopyTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
cdef void *glMapNamedBuffer(GLuint buffer, GLenum access)
cdef void glNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, const void *data)
cdef void glGetnHistogram(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values)
cdef void glNamedFramebufferRenderbuffer(GLuint framebuffer, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
cdef void glGetnPixelMapusv(GLenum map, GLsizei bufSize, GLushort *values)
cdef void glGetNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, void *data)
cdef void glReadnPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei bufSize, void *data)
cdef void glCompressedTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data)
cdef void glGetTextureParameterIiv(GLuint texture, GLenum pname, GLint *params)
cdef void glGetnMapfv(GLenum target, GLenum query, GLsizei bufSize, GLfloat *v)
cdef void glGetnPixelMapuiv(GLenum map, GLsizei bufSize, GLuint *values)
cdef void glCopyNamedBufferSubData(GLuint readBuffer, GLuint writeBuffer, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size)
cdef void glGenerateTextureMipmap(GLuint texture)
cdef void glTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels)
cdef void glGetTransformFeedbackiv(GLuint xfb, GLenum pname, GLint *param)
cdef void glEnableVertexArrayAttrib(GLuint vaobj, GLuint index)
cdef void glInvalidateNamedFramebufferData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments)
cdef void glVertexArrayAttribIFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
cdef void glNamedFramebufferTexture(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level)
