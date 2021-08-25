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

cdef GLenum GL_ACTIVE_SUBROUTINES
cdef GLenum GL_ACTIVE_SUBROUTINE_MAX_LENGTH
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORMS
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH
cdef GLenum GL_COMPATIBLE_SUBROUTINES
cdef GLenum GL_DOUBLE_MAT2
cdef GLenum GL_DOUBLE_MAT2x3
cdef GLenum GL_DOUBLE_MAT2x4
cdef GLenum GL_DOUBLE_MAT3
cdef GLenum GL_DOUBLE_MAT3x2
cdef GLenum GL_DOUBLE_MAT3x4
cdef GLenum GL_DOUBLE_MAT4
cdef GLenum GL_DOUBLE_MAT4x2
cdef GLenum GL_DOUBLE_MAT4x3
cdef GLenum GL_DOUBLE_VEC2
cdef GLenum GL_DOUBLE_VEC3
cdef GLenum GL_DOUBLE_VEC4
cdef GLenum GL_DRAW_INDIRECT_BUFFER
cdef GLenum GL_DRAW_INDIRECT_BUFFER_BINDING
cdef GLenum GL_FRACTIONAL_EVEN
cdef GLenum GL_FRACTIONAL_ODD
cdef GLenum GL_FRAGMENT_INTERPOLATION_OFFSET_BITS
cdef GLenum GL_GEOMETRY_SHADER_INVOCATIONS
cdef GLenum GL_INT_SAMPLER_CUBE_MAP_ARRAY
cdef GLenum GL_ISOLINES
cdef GLenum GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS
cdef GLenum GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS
cdef GLenum GL_MAX_FRAGMENT_INTERPOLATION_OFFSET
cdef GLenum GL_MAX_GEOMETRY_SHADER_INVOCATIONS
cdef GLenum GL_MAX_PATCH_VERTICES
cdef GLenum GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET
cdef GLenum GL_MAX_SUBROUTINES
cdef GLenum GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS
cdef GLenum GL_MAX_TESS_CONTROL_INPUT_COMPONENTS
cdef GLenum GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS
cdef GLenum GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS
cdef GLenum GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS
cdef GLenum GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS
cdef GLenum GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS
cdef GLenum GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS
cdef GLenum GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS
cdef GLenum GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS
cdef GLenum GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS
cdef GLenum GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS
cdef GLenum GL_MAX_TESS_GEN_LEVEL
cdef GLenum GL_MAX_TESS_PATCH_COMPONENTS
cdef GLenum GL_MAX_TRANSFORM_FEEDBACK_BUFFERS
cdef GLenum GL_MAX_VERTEX_STREAMS
cdef GLenum GL_MIN_FRAGMENT_INTERPOLATION_OFFSET
cdef GLenum GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET
cdef GLenum GL_MIN_SAMPLE_SHADING_VALUE
cdef GLenum GL_NUM_COMPATIBLE_SUBROUTINES
cdef GLenum GL_PATCHES
cdef GLenum GL_PATCH_DEFAULT_INNER_LEVEL
cdef GLenum GL_PATCH_DEFAULT_OUTER_LEVEL
cdef GLenum GL_PATCH_VERTICES
cdef GLenum GL_PROXY_TEXTURE_CUBE_MAP_ARRAY
cdef GLenum GL_QUADS
cdef GLenum GL_SAMPLER_CUBE_MAP_ARRAY
cdef GLenum GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW
cdef GLenum GL_SAMPLE_SHADING
cdef GLenum GL_TESS_CONTROL_OUTPUT_VERTICES
cdef GLenum GL_TESS_CONTROL_SHADER
cdef GLenum GL_TESS_EVALUATION_SHADER
cdef GLenum GL_TESS_GEN_MODE
cdef GLenum GL_TESS_GEN_POINT_MODE
cdef GLenum GL_TESS_GEN_SPACING
cdef GLenum GL_TESS_GEN_VERTEX_ORDER
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP_ARRAY
cdef GLenum GL_TEXTURE_CUBE_MAP_ARRAY
cdef GLenum GL_TRANSFORM_FEEDBACK
cdef GLenum GL_TRANSFORM_FEEDBACK_BINDING
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER
cdef GLenum GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY
cdef void glBeginQueryIndexed(GLenum target, GLuint index, GLuint id)
cdef void glBindTransformFeedback(GLenum target, GLuint id)
cdef void glBlendEquationSeparatei(GLuint buf, GLenum modeRGB, GLenum modeAlpha)
cdef void glBlendEquationi(GLuint buf, GLenum mode)
cdef void glBlendFuncSeparatei(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
cdef void glBlendFunci(GLuint buf, GLenum src, GLenum dst)
cdef void glDeleteTransformFeedbacks(GLsizei n, const GLuint *ids)
cdef void glDrawArraysIndirect(GLenum mode, const void *indirect)
cdef void glDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect)
cdef void glDrawTransformFeedback(GLenum mode, GLuint id)
cdef void glDrawTransformFeedbackStream(GLenum mode, GLuint id, GLuint stream)
cdef void glEndQueryIndexed(GLenum target, GLuint index)
cdef void glGenTransformFeedbacks(GLsizei n, GLuint *ids)
cdef void glGetActiveSubroutineName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
cdef void glGetActiveSubroutineUniformName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
cdef void glGetActiveSubroutineUniformiv(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values)
cdef void glGetProgramStageiv(GLuint program, GLenum shadertype, GLenum pname, GLint *values)
cdef void glGetQueryIndexediv(GLenum target, GLuint index, GLenum pname, GLint *params)
cdef GLuint glGetSubroutineIndex(GLuint program, GLenum shadertype, const GLchar *name)
cdef GLint glGetSubroutineUniformLocation(GLuint program, GLenum shadertype, const GLchar *name)
cdef void glGetUniformSubroutineuiv(GLenum shadertype, GLint location, GLuint *params)
cdef void glGetUniformdv(GLuint program, GLint location, GLdouble *params)
cdef GLboolean glIsTransformFeedback(GLuint id)
cdef void glMinSampleShading(GLfloat value)
cdef void glPatchParameterfv(GLenum pname, const GLfloat *values)
cdef void glPatchParameteri(GLenum pname, GLint value)
cdef void glPauseTransformFeedback()
cdef void glResumeTransformFeedback()
cdef void glUniform1d(GLint location, GLdouble x)
cdef void glUniform1dv(GLint location, GLsizei count, const GLdouble *value)
cdef void glUniform2d(GLint location, GLdouble x, GLdouble y)
cdef void glUniform2dv(GLint location, GLsizei count, const GLdouble *value)
cdef void glUniform3d(GLint location, GLdouble x, GLdouble y, GLdouble z)
cdef void glUniform3dv(GLint location, GLsizei count, const GLdouble *value)
cdef void glUniform4d(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
cdef void glUniform4dv(GLint location, GLsizei count, const GLdouble *value)
cdef void glUniformMatrix2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformMatrix2x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformMatrix2x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformMatrix3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformMatrix3x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformMatrix3x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformMatrix4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformMatrix4x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformMatrix4x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
cdef void glUniformSubroutinesuiv(GLenum shadertype, GLsizei count, const GLuint *indices)
