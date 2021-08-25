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
cdef GLboolean glIsRenderbuffer(GLuint renderbuffer)
cdef void glVertexAttribI4i(GLuint index, GLint x, GLint y, GLint z, GLint w)
cdef void glGetRenderbufferParameteriv(GLenum target, GLenum pname, GLint *params)
cdef void glVertexAttribI4sv(GLuint index, const GLshort *v)
cdef void glUniform3uiv(GLint location, GLsizei count, const GLuint *value)
cdef void glEnablei(GLenum target, GLuint index)
cdef void glTransformFeedbackVaryings(GLuint program, GLsizei count, const GLchar **varyings, GLenum bufferMode)
cdef GLboolean glIsEnabledi(GLenum target, GLuint index)
cdef void glTexParameterIuiv(GLenum target, GLenum pname, const GLuint *params)
cdef void glUniform2uiv(GLint location, GLsizei count, const GLuint *value)
cdef void glClearBufferfv(GLenum buffer, GLint drawbuffer, const GLfloat *value)
cdef void glVertexAttribI2i(GLuint index, GLint x, GLint y)
cdef void glFramebufferTexture2D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level)
cdef void glVertexAttribI1iv(GLuint index, const GLint *v)
cdef void glVertexAttribIPointer(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer)
cdef void glFramebufferTextureLayer(GLenum target, GLenum attachment, GLuint texture, GLint level, GLint layer)
cdef void glVertexAttribI4bv(GLuint index, const GLbyte *v)
cdef void glVertexAttribI4iv(GLuint index, const GLint *v)
cdef void glGetFramebufferAttachmentParameteriv(GLenum target, GLenum attachment, GLenum pname, GLint *params)
cdef void glGenVertexArrays(GLsizei n, GLuint *arrays)
cdef void glVertexAttribI3ui(GLuint index, GLuint x, GLuint y, GLuint z)
cdef void glGenRenderbuffers(GLsizei n, GLuint *renderbuffers)
cdef GLint glGetFragDataLocation(GLuint program, const GLchar *name)
cdef void glFramebufferTexture1D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level)
cdef void glVertexAttribI3iv(GLuint index, const GLint *v)
cdef void glVertexAttribI1i(GLuint index, GLint x)
cdef void glEndConditionalRender()
cdef const GLubyte *glGetStringi(GLenum name, GLuint index)
cdef void glDeleteVertexArrays(GLsizei n, const GLuint *arrays)
cdef void glBlitFramebuffer(GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
cdef void *glMapBufferRange(GLenum target, GLintptr offset, GLsizeiptr length, GLbitfield access)
cdef void glFramebufferTexture3D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level, GLint zoffset)
cdef void glUniform4ui(GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
cdef GLboolean glIsFramebuffer(GLuint framebuffer)
cdef void glDeleteRenderbuffers(GLsizei n, const GLuint *renderbuffers)
cdef void glVertexAttribI4ubv(GLuint index, const GLubyte *v)
cdef void glUniform4uiv(GLint location, GLsizei count, const GLuint *value)
cdef void glBindVertexArray(GLuint array)
cdef void glGetTexParameterIuiv(GLenum target, GLenum pname, GLuint *params)
cdef void glRenderbufferStorage(GLenum target, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glVertexAttribI2uiv(GLuint index, const GLuint *v)
cdef void glBindFragDataLocation(GLuint program, GLuint color, const GLchar *name)
cdef void glVertexAttribI3uiv(GLuint index, const GLuint *v)
cdef void glGetTransformFeedbackVarying(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum *type, GLchar *name)
cdef void glVertexAttribI4ui(GLuint index, GLuint x, GLuint y, GLuint z, GLuint w)
cdef void glGetUniformuiv(GLuint program, GLint location, GLuint *params)
cdef void glBindBufferRange(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
cdef void glBeginTransformFeedback(GLenum primitiveMode)
cdef void glClearBufferfi(GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil)
cdef void glGetTexParameterIiv(GLenum target, GLenum pname, GLint *params)
cdef void glUniform2ui(GLint location, GLuint v0, GLuint v1)
cdef void glBindFramebuffer(GLenum target, GLuint framebuffer)
cdef void glRenderbufferStorageMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height)
cdef void glDisablei(GLenum target, GLuint index)
cdef void glDeleteFramebuffers(GLsizei n, const GLuint *framebuffers)
cdef void glVertexAttribI4usv(GLuint index, const GLushort *v)
cdef void glVertexAttribI2iv(GLuint index, const GLint *v)
cdef void glUniform1ui(GLint location, GLuint v0)
cdef void glClearBufferiv(GLenum buffer, GLint drawbuffer, const GLint *value)
cdef void glClampColor(GLenum target, GLenum clamp)
cdef void glBindBufferBase(GLenum target, GLuint index, GLuint buffer)
cdef void glEndTransformFeedback()
cdef void glVertexAttribI3i(GLuint index, GLint x, GLint y, GLint z)
cdef void glGenerateMipmap(GLenum target)
cdef void glFlushMappedBufferRange(GLenum target, GLintptr offset, GLsizeiptr length)
cdef void glGetVertexAttribIiv(GLuint index, GLenum pname, GLint *params)
cdef void glUniform1uiv(GLint location, GLsizei count, const GLuint *value)
cdef void glTexParameterIiv(GLenum target, GLenum pname, const GLint *params)
cdef void glBindRenderbuffer(GLenum target, GLuint renderbuffer)
cdef void glVertexAttribI4uiv(GLuint index, const GLuint *v)
cdef GLenum glCheckFramebufferStatus(GLenum target)
cdef void glFramebufferRenderbuffer(GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
cdef void glVertexAttribI1ui(GLuint index, GLuint x)
cdef void glUniform3ui(GLint location, GLuint v0, GLuint v1, GLuint v2)
cdef void glGenFramebuffers(GLsizei n, GLuint *framebuffers)
cdef void glBeginConditionalRender(GLuint id, GLenum mode)
cdef void glVertexAttribI1uiv(GLuint index, const GLuint *v)
cdef void glGetIntegeri_v(GLenum target, GLuint index, GLint *data)
cdef void glColorMaski(GLuint index, GLboolean r, GLboolean g, GLboolean b, GLboolean a)
cdef GLboolean glIsVertexArray(GLuint array)
cdef void glVertexAttribI2ui(GLuint index, GLuint x, GLuint y)
cdef void glClearBufferuiv(GLenum buffer, GLint drawbuffer, const GLuint *value)
cdef void glGetBooleani_v(GLenum target, GLuint index, GLboolean *data)
cdef void glGetVertexAttribIuiv(GLuint index, GLenum pname, GLuint *params)
