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
cdef void glDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect)
cdef void glBindTransformFeedback(GLenum target, GLuint id)
cdef GLboolean glIsTransformFeedback(GLuint id)
cdef void glUniform4dv(GLint location, GLsizei count, const GLdouble *value)
cdef void glUniform3d(GLint location, GLdouble x, GLdouble y, GLdouble z)
cdef void glUniformMatrix2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef GLuint glGetSubroutineIndex(GLuint program, GLenum shadertype, const GLchar *name)
cdef void glGetProgramStageiv(GLuint program, GLenum shadertype, GLenum pname, GLint *values)
cdef void glDrawTransformFeedback(GLenum mode, GLuint id)
cdef void glMinSampleShading(GLfloat value)
cdef void glUniformMatrix3x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glGetUniformSubroutineuiv(GLenum shadertype, GLint location, GLuint *params)
cdef void glPatchParameterfv(GLenum pname, const GLfloat *values)
cdef void glBlendFunci(GLuint buf, GLenum src, GLenum dst)
cdef void glUniform2d(GLint location, GLdouble x, GLdouble y)
cdef void glBlendEquationi(GLuint buf, GLenum mode)
cdef void glUniformMatrix3x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glGetActiveSubroutineName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
cdef void glGetQueryIndexediv(GLenum target, GLuint index, GLenum pname, GLint *params)
cdef void glUniform4d(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
cdef void glBlendEquationSeparatei(GLuint buf, GLenum modeRGB, GLenum modeAlpha)
cdef GLint glGetSubroutineUniformLocation(GLuint program, GLenum shadertype, const GLchar *name)
cdef void glDeleteTransformFeedbacks(GLsizei n, const GLuint *ids)
cdef void glUniform1dv(GLint location, GLsizei count, const GLdouble *value)
cdef void glGetActiveSubroutineUniformName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
cdef void glEndQueryIndexed(GLenum target, GLuint index)
cdef void glBlendFuncSeparatei(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
cdef void glUniform3dv(GLint location, GLsizei count, const GLdouble *value)
cdef void glUniformMatrix3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformMatrix2x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformMatrix2x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glDrawTransformFeedbackStream(GLenum mode, GLuint id, GLuint stream)
cdef void glUniformMatrix4x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glResumeTransformFeedback()
cdef void glUniformMatrix4x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glPauseTransformFeedback()
cdef void glUniformMatrix4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glBeginQueryIndexed(GLenum target, GLuint index, GLuint id)
cdef void glDrawArraysIndirect(GLenum mode, const void *indirect)
cdef void glPatchParameteri(GLenum pname, GLint value)
cdef void glUniformSubroutinesuiv(GLenum shadertype, GLsizei count, const GLuint *indices)
cdef void glGenTransformFeedbacks(GLsizei n, GLuint *ids)
cdef void glUniform1d(GLint location, GLdouble x)
cdef void glUniform2dv(GLint location, GLsizei count, const GLdouble *value)
cdef void glGetActiveSubroutineUniformiv(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values)
cdef void glGetUniformdv(GLuint program, GLint location, GLdouble *params)
