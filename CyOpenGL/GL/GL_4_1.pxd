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
cdef void glShaderBinary(GLsizei count, const GLuint *shaders, GLenum binaryFormat, const void *binary, GLsizei length)
cdef void glProgramBinary(GLuint program, GLenum binaryFormat, const void *binary, GLsizei length)
cdef void glGetProgramBinary(GLuint program, GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, void *binary)
cdef GLboolean glIsProgramPipeline(GLuint pipeline)
cdef void glProgramUniformMatrix3x2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glVertexAttribL2d(GLuint index, GLdouble x, GLdouble y)
cdef void glProgramUniform2i(GLuint program, GLint location, GLint v0, GLint v1)
cdef void glProgramUniform1fv(GLuint program, GLint location, GLsizei count, const GLfloat *value)
cdef void glProgramUniform1f(GLuint program, GLint location, GLfloat v0)
cdef void glProgramUniformMatrix4x3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glVertexAttribL1dv(GLuint index, const GLdouble *v)
cdef void glProgramUniform1ui(GLuint program, GLint location, GLuint v0)
cdef void glProgramUniformMatrix2x4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glProgramUniformMatrix2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glDepthRangeIndexed(GLuint index, GLdouble n, GLdouble f)
cdef void glVertexAttribLPointer(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer)
cdef void glVertexAttribL4dv(GLuint index, const GLdouble *v)
cdef void glGetProgramPipelineiv(GLuint pipeline, GLenum pname, GLint *params)
cdef void glProgramUniform2ui(GLuint program, GLint location, GLuint v0, GLuint v1)
cdef void glProgramUniform3f(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2)
cdef GLuint glCreateShaderProgramv(GLenum type, GLsizei count, const GLchar **strings)
cdef void glGetShaderPrecisionFormat(GLenum shadertype, GLenum precisiontype, GLint *range, GLint *precision)
cdef void glViewportIndexedfv(GLuint index, const GLfloat *v)
cdef void glProgramUniform3iv(GLuint program, GLint location, GLsizei count, const GLint *value)
cdef void glProgramUniform2iv(GLuint program, GLint location, GLsizei count, const GLint *value)
cdef void glValidateProgramPipeline(GLuint pipeline)
cdef void glProgramUniformMatrix2x4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glVertexAttribL1d(GLuint index, GLdouble x)
cdef void glProgramUniformMatrix3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glVertexAttribL4d(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
cdef void glProgramUniformMatrix4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glProgramUniformMatrix3x4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glDepthRangeArrayv(GLuint first, GLsizei count, const GLdouble *v)
cdef void glProgramUniform4ui(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
cdef void glProgramUniformMatrix4x2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glProgramUniform4i(GLuint program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3)
cdef void glProgramUniformMatrix2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glViewportIndexedf(GLuint index, GLfloat x, GLfloat y, GLfloat w, GLfloat h)
cdef void glVertexAttribL2dv(GLuint index, const GLdouble *v)
cdef void glReleaseShaderCompiler()
cdef void glDepthRangef(GLfloat n, GLfloat f)
cdef void glProgramUniform4uiv(GLuint program, GLint location, GLsizei count, const GLuint *value)
cdef void glProgramUniformMatrix2x3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glProgramUniform4iv(GLuint program, GLint location, GLsizei count, const GLint *value)
cdef void glProgramUniformMatrix3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glProgramUniform1iv(GLuint program, GLint location, GLsizei count, const GLint *value)
cdef void glProgramParameteri(GLuint program, GLenum pname, GLint value)
cdef void glProgramUniform2f(GLuint program, GLint location, GLfloat v0, GLfloat v1)
cdef void glViewportArrayv(GLuint first, GLsizei count, const GLfloat *v)
cdef void glProgramUniform3fv(GLuint program, GLint location, GLsizei count, const GLfloat *value)
cdef void glClearDepthf(GLfloat d)
cdef void glProgramUniform4dv(GLuint program, GLint location, GLsizei count, const GLdouble *value)
cdef void glProgramUniform4f(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
cdef void glProgramUniformMatrix4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glProgramUniform2uiv(GLuint program, GLint location, GLsizei count, const GLuint *value)
cdef void glVertexAttribL3d(GLuint index, GLdouble x, GLdouble y, GLdouble z)
cdef void glGetVertexAttribLdv(GLuint index, GLenum pname, GLdouble *params)
cdef void glScissorArrayv(GLuint first, GLsizei count, const GLint *v)
cdef void glScissorIndexedv(GLuint index, const GLint *v)
cdef void glProgramUniform1i(GLuint program, GLint location, GLint v0)
cdef void glGetFloati_v(GLenum target, GLuint index, GLfloat *data)
cdef void glProgramUniformMatrix4x3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glScissorIndexed(GLuint index, GLint left, GLint bottom, GLsizei width, GLsizei height)
cdef void glProgramUniform2d(GLuint program, GLint location, GLdouble v0, GLdouble v1)
cdef void glProgramUniformMatrix4x2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glProgramUniform3dv(GLuint program, GLint location, GLsizei count, const GLdouble *value)
cdef void glProgramUniform3ui(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2)
cdef void glBindProgramPipeline(GLuint pipeline)
cdef void glGetDoublei_v(GLenum target, GLuint index, GLdouble *data)
cdef void glVertexAttribL3dv(GLuint index, const GLdouble *v)
cdef void glProgramUniform1dv(GLuint program, GLint location, GLsizei count, const GLdouble *value)
cdef void glUseProgramStages(GLuint pipeline, GLbitfield stages, GLuint program)
cdef void glProgramUniform1uiv(GLuint program, GLint location, GLsizei count, const GLuint *value)
cdef void glGenProgramPipelines(GLsizei n, GLuint *pipelines)
cdef void glProgramUniformMatrix3x4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
cdef void glProgramUniform1d(GLuint program, GLint location, GLdouble v0)
cdef void glProgramUniformMatrix3x2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glDeleteProgramPipelines(GLsizei n, const GLuint *pipelines)
cdef void glActiveShaderProgram(GLuint pipeline, GLuint program)
cdef void glGetProgramPipelineInfoLog(GLuint pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
cdef void glProgramUniform2fv(GLuint program, GLint location, GLsizei count, const GLfloat *value)
cdef void glProgramUniform3i(GLuint program, GLint location, GLint v0, GLint v1, GLint v2)
cdef void glProgramUniform3d(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2)
cdef void glProgramUniform4fv(GLuint program, GLint location, GLsizei count, const GLfloat *value)
cdef void glProgramUniformMatrix2x3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glProgramUniform4d(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3)
cdef void glProgramUniform3uiv(GLuint program, GLint location, GLsizei count, const GLuint *value)
cdef void glProgramUniform2dv(GLuint program, GLint location, GLsizei count, const GLdouble *value)
