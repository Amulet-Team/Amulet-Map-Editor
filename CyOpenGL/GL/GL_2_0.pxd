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
cdef void glVertexAttribPointer(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void *pointer)
cdef void glVertexAttrib4ubv(GLuint index, const GLubyte *v)
cdef void glUniform2iv(GLint location, GLsizei count, const GLint *value)
cdef GLboolean glIsShader(GLuint shader)
cdef void glVertexAttrib4s(GLuint index, GLshort x, GLshort y, GLshort z, GLshort w)
cdef void glVertexAttrib4Nubv(GLuint index, const GLubyte *v)
cdef void glGetActiveUniform(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name)
cdef void glValidateProgram(GLuint program)
cdef void glVertexAttrib1fv(GLuint index, const GLfloat *v)
cdef void glVertexAttrib4dv(GLuint index, const GLdouble *v)
cdef void glUniform1iv(GLint location, GLsizei count, const GLint *value)
cdef void glVertexAttrib4usv(GLuint index, const GLushort *v)
cdef void glUniform1f(GLint location, GLfloat v0)
cdef void glVertexAttrib4sv(GLuint index, const GLshort *v)
cdef void glGetVertexAttribPointerv(GLuint index, GLenum pname, void **pointer)
cdef void glGetActiveAttrib(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name)
cdef void glGetShaderInfoLog(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
cdef void glUniform4f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
cdef void glVertexAttrib2dv(GLuint index, const GLdouble *v)
cdef void glBindAttribLocation(GLuint program, GLuint index, const GLchar *name)
cdef void glLinkProgram(GLuint program)
cdef void glVertexAttrib4bv(GLuint index, const GLbyte *v)
cdef void glVertexAttrib1d(GLuint index, GLdouble x)
cdef void glGetShaderSource(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *source)
cdef void glAttachShader(GLuint program, GLuint shader)
cdef void glVertexAttrib3sv(GLuint index, const GLshort *v)
cdef void glGetVertexAttribdv(GLuint index, GLenum pname, GLdouble *params)
cdef void glUniformMatrix2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glVertexAttrib1sv(GLuint index, const GLshort *v)
cdef void glVertexAttrib4Nsv(GLuint index, const GLshort *v)
cdef void glGetUniformiv(GLuint program, GLint location, GLint *params)
cdef void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glUniform4iv(GLint location, GLsizei count, const GLint *value)
cdef void glBlendEquationSeparate(GLenum modeRGB, GLenum modeAlpha)
cdef void glVertexAttrib4uiv(GLuint index, const GLuint *v)
cdef GLuint glCreateProgram()
cdef void glVertexAttrib3d(GLuint index, GLdouble x, GLdouble y, GLdouble z)
cdef void glStencilOpSeparate(GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass)
cdef void glUniform1fv(GLint location, GLsizei count, const GLfloat *value)
cdef void glUniform3i(GLint location, GLint v0, GLint v1, GLint v2)
cdef void glStencilMaskSeparate(GLenum face, GLuint mask)
cdef void glVertexAttrib2s(GLuint index, GLshort x, GLshort y)
cdef void glUniform2i(GLint location, GLint v0, GLint v1)
cdef void glDrawBuffers(GLsizei n, const GLenum *bufs)
cdef void glVertexAttrib3f(GLuint index, GLfloat x, GLfloat y, GLfloat z)
cdef void glEnableVertexAttribArray(GLuint index)
cdef void glVertexAttrib4Nbv(GLuint index, const GLbyte *v)
cdef void glUniform3fv(GLint location, GLsizei count, const GLfloat *value)
cdef void glStencilFuncSeparate(GLenum face, GLenum func, GLint ref, GLuint mask)
cdef void glVertexAttrib4f(GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w)
cdef void glDetachShader(GLuint program, GLuint shader)
cdef void glVertexAttrib1s(GLuint index, GLshort x)
cdef void glVertexAttrib4Nusv(GLuint index, const GLushort *v)
cdef GLboolean glIsProgram(GLuint program)
cdef void glVertexAttrib3s(GLuint index, GLshort x, GLshort y, GLshort z)
cdef void glVertexAttrib1dv(GLuint index, const GLdouble *v)
cdef void glGetProgramInfoLog(GLuint program, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
cdef void glUseProgram(GLuint program)
cdef void glVertexAttrib2d(GLuint index, GLdouble x, GLdouble y)
cdef GLint glGetUniformLocation(GLuint program, const GLchar *name)
cdef void glVertexAttrib1f(GLuint index, GLfloat x)
cdef void glGetUniformfv(GLuint program, GLint location, GLfloat *params)
cdef void glVertexAttrib4d(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
cdef void glVertexAttrib3fv(GLuint index, const GLfloat *v)
cdef void glUniformMatrix3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glVertexAttrib2fv(GLuint index, const GLfloat *v)
cdef void glVertexAttrib3dv(GLuint index, const GLdouble *v)
cdef void glUniform3iv(GLint location, GLsizei count, const GLint *value)
cdef void glUniform4fv(GLint location, GLsizei count, const GLfloat *value)
cdef void glVertexAttrib4Nuiv(GLuint index, const GLuint *v)
cdef void glDisableVertexAttribArray(GLuint index)
cdef void glDeleteShader(GLuint shader)
cdef void glGetShaderiv(GLuint shader, GLenum pname, GLint *params)
cdef void glUniform3f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2)
cdef void glCompileShader(GLuint shader)
cdef GLint glGetAttribLocation(GLuint program, const GLchar *name)
cdef void glGetProgramiv(GLuint program, GLenum pname, GLint *params)
cdef void glDeleteProgram(GLuint program)
cdef void glUniform2f(GLint location, GLfloat v0, GLfloat v1)
cdef GLuint glCreateShader(GLenum type)
cdef void glGetAttachedShaders(GLuint program, GLsizei maxCount, GLsizei *count, GLuint *shaders)
cdef void glVertexAttrib4Niv(GLuint index, const GLint *v)
cdef void glUniform1i(GLint location, GLint v0)
cdef void glVertexAttrib4Nub(GLuint index, GLubyte x, GLubyte y, GLubyte z, GLubyte w)
cdef void glGetVertexAttribfv(GLuint index, GLenum pname, GLfloat *params)
cdef void glShaderSource(GLuint shader, GLsizei count, const GLchar **string, const GLint *length)
cdef void glVertexAttrib4iv(GLuint index, const GLint *v)
cdef void glVertexAttrib2f(GLuint index, GLfloat x, GLfloat y)
cdef void glGetVertexAttribiv(GLuint index, GLenum pname, GLint *params)
cdef void glUniform2fv(GLint location, GLsizei count, const GLfloat *value)
cdef void glVertexAttrib2sv(GLuint index, const GLshort *v)
cdef void glVertexAttrib4fv(GLuint index, const GLfloat *v)
cdef void glUniform4i(GLint location, GLint v0, GLint v1, GLint v2, GLint v3)
