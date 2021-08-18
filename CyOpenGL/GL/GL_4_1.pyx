# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_FIXED = 0x140C
cdef GLenum GL_IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
cdef GLenum GL_IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B
cdef GLenum GL_LOW_FLOAT = 0x8DF0
cdef GLenum GL_MEDIUM_FLOAT = 0x8DF1
cdef GLenum GL_HIGH_FLOAT = 0x8DF2
cdef GLenum GL_LOW_INT = 0x8DF3
cdef GLenum GL_MEDIUM_INT = 0x8DF4
cdef GLenum GL_HIGH_INT = 0x8DF5
cdef GLenum GL_SHADER_COMPILER = 0x8DFA
cdef GLenum GL_SHADER_BINARY_FORMATS = 0x8DF8
cdef GLenum GL_NUM_SHADER_BINARY_FORMATS = 0x8DF9
cdef GLenum GL_MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
cdef GLenum GL_MAX_VARYING_VECTORS = 0x8DFC
cdef GLenum GL_MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
cdef GLenum GL_RGB565 = 0x8D62
cdef GLenum GL_PROGRAM_BINARY_RETRIEVABLE_HINT = 0x8257
cdef GLenum GL_PROGRAM_BINARY_LENGTH = 0x8741
cdef GLenum GL_NUM_PROGRAM_BINARY_FORMATS = 0x87FE
cdef GLenum GL_PROGRAM_BINARY_FORMATS = 0x87FF
cdef GLenum GL_VERTEX_SHADER_BIT = 0x00000001
cdef GLenum GL_FRAGMENT_SHADER_BIT = 0x00000002
cdef GLenum GL_GEOMETRY_SHADER_BIT = 0x00000004
cdef GLenum GL_TESS_CONTROL_SHADER_BIT = 0x00000008
cdef GLenum GL_TESS_EVALUATION_SHADER_BIT = 0x00000010
cdef GLenum GL_ALL_SHADER_BITS = 0xFFFFFFFF
cdef GLenum GL_PROGRAM_SEPARABLE = 0x8258
cdef GLenum GL_ACTIVE_PROGRAM = 0x8259
cdef GLenum GL_PROGRAM_PIPELINE_BINDING = 0x825A
cdef GLenum GL_MAX_VIEWPORTS = 0x825B
cdef GLenum GL_VIEWPORT_SUBPIXEL_BITS = 0x825C
cdef GLenum GL_VIEWPORT_BOUNDS_RANGE = 0x825D
cdef GLenum GL_LAYER_PROVOKING_VERTEX = 0x825E
cdef GLenum GL_VIEWPORT_INDEX_PROVOKING_VERTEX = 0x825F
cdef GLenum GL_UNDEFINED_VERTEX = 0x8260

ctypedef void (*GL_RELEASE_SHADER_COMPILER)()
ctypedef void (*GL_SHADER_BINARY)(GLsizei count, const GLuint *shaders, GLenum binaryFormat, const void *binary, GLsizei length)
ctypedef void (*GL_GET_SHADER_PRECISION_FORMAT)(GLenum shadertype, GLenum precisiontype, GLint *range, GLint *precision)
ctypedef void (*GL_DEPTH_RANGEF)(GLfloat n, GLfloat f)
ctypedef void (*GL_CLEAR_DEPTHF)(GLfloat d)
ctypedef void (*GL_GET_PROGRAM_BINARY)(GLuint program, GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, void *binary)
ctypedef void (*GL_PROGRAM_BINARY)(GLuint program, GLenum binaryFormat, const void *binary, GLsizei length)
ctypedef void (*GL_PROGRAM_PARAMETERI)(GLuint program, GLenum pname, GLint value)
ctypedef void (*GL_USE_PROGRAM_STAGES)(GLuint pipeline, GLbitfield stages, GLuint program)
ctypedef void (*GL_ACTIVE_SHADER_PROGRAM)(GLuint pipeline, GLuint program)
ctypedef GLuint (*GL_CREATE_SHADER_PROGRAMV)(GLenum type, GLsizei count, const GLchar *const*strings)
ctypedef void (*GL_BIND_PROGRAM_PIPELINE)(GLuint pipeline)
ctypedef void (*GL_DELETE_PROGRAM_PIPELINES)(GLsizei n, const GLuint *pipelines)
ctypedef void (*GL_GEN_PROGRAM_PIPELINES)(GLsizei n, GLuint *pipelines)
ctypedef GLboolean (*GL_IS_PROGRAM_PIPELINE)(GLuint pipeline)
ctypedef void (*GL_GET_PROGRAM_PIPELINEIV)(GLuint pipeline, GLenum pname, GLint *params)
ctypedef void (*GL_PROGRAM_PARAMETERI)(GLuint program, GLenum pname, GLint value)
ctypedef void (*GL_PROGRAM_UNIFORM1I)(GLuint program, GLint location, GLint v0)
ctypedef void (*GL_PROGRAM_UNIFORM1IV)(GLuint program, GLint location, GLsizei count, const GLint *value)
ctypedef void (*GL_PROGRAM_UNIFORM1F)(GLuint program, GLint location, GLfloat v0)
ctypedef void (*GL_PROGRAM_UNIFORM1FV)(GLuint program, GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM1D)(GLuint program, GLint location, GLdouble v0)
ctypedef void (*GL_PROGRAM_UNIFORM1DV)(GLuint program, GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM1UI)(GLuint program, GLint location, GLuint v0)
ctypedef void (*GL_PROGRAM_UNIFORM1UIV)(GLuint program, GLint location, GLsizei count, const GLuint *value)
ctypedef void (*GL_PROGRAM_UNIFORM2I)(GLuint program, GLint location, GLint v0, GLint v1)
ctypedef void (*GL_PROGRAM_UNIFORM2IV)(GLuint program, GLint location, GLsizei count, const GLint *value)
ctypedef void (*GL_PROGRAM_UNIFORM2F)(GLuint program, GLint location, GLfloat v0, GLfloat v1)
ctypedef void (*GL_PROGRAM_UNIFORM2FV)(GLuint program, GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM2D)(GLuint program, GLint location, GLdouble v0, GLdouble v1)
ctypedef void (*GL_PROGRAM_UNIFORM2DV)(GLuint program, GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM2UI)(GLuint program, GLint location, GLuint v0, GLuint v1)
ctypedef void (*GL_PROGRAM_UNIFORM2UIV)(GLuint program, GLint location, GLsizei count, const GLuint *value)
ctypedef void (*GL_PROGRAM_UNIFORM3I)(GLuint program, GLint location, GLint v0, GLint v1, GLint v2)
ctypedef void (*GL_PROGRAM_UNIFORM3IV)(GLuint program, GLint location, GLsizei count, const GLint *value)
ctypedef void (*GL_PROGRAM_UNIFORM3F)(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2)
ctypedef void (*GL_PROGRAM_UNIFORM3FV)(GLuint program, GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM3D)(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2)
ctypedef void (*GL_PROGRAM_UNIFORM3DV)(GLuint program, GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM3UI)(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2)
ctypedef void (*GL_PROGRAM_UNIFORM3UIV)(GLuint program, GLint location, GLsizei count, const GLuint *value)
ctypedef void (*GL_PROGRAM_UNIFORM4I)(GLuint program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3)
ctypedef void (*GL_PROGRAM_UNIFORM4IV)(GLuint program, GLint location, GLsizei count, const GLint *value)
ctypedef void (*GL_PROGRAM_UNIFORM4F)(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
ctypedef void (*GL_PROGRAM_UNIFORM4FV)(GLuint program, GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM4D)(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3)
ctypedef void (*GL_PROGRAM_UNIFORM4DV)(GLuint program, GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM4UI)(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
ctypedef void (*GL_PROGRAM_UNIFORM4UIV)(GLuint program, GLint location, GLsizei count, const GLuint *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX2FV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX3FV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX4FV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX2DV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX3DV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX4DV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX2X3FV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX3X2FV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX2X4FV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX4X2FV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX3X4FV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX4X3FV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX2X3DV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX3X2DV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX2X4DV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX4X2DV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX3X4DV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_PROGRAM_UNIFORM_MATRIX4X3DV)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_VALIDATE_PROGRAM_PIPELINE)(GLuint pipeline)
ctypedef void (*GL_GET_PROGRAM_PIPELINE_INFO_LOG)(GLuint pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
ctypedef void (*GL_VERTEX_ATTRIB_L1D)(GLuint index, GLdouble x)
ctypedef void (*GL_VERTEX_ATTRIB_L2D)(GLuint index, GLdouble x, GLdouble y)
ctypedef void (*GL_VERTEX_ATTRIB_L3D)(GLuint index, GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*GL_VERTEX_ATTRIB_L4D)(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*GL_VERTEX_ATTRIB_L1DV)(GLuint index, const GLdouble *v)
ctypedef void (*GL_VERTEX_ATTRIB_L2DV)(GLuint index, const GLdouble *v)
ctypedef void (*GL_VERTEX_ATTRIB_L3DV)(GLuint index, const GLdouble *v)
ctypedef void (*GL_VERTEX_ATTRIB_L4DV)(GLuint index, const GLdouble *v)
ctypedef void (*GL_VERTEX_ATTRIB_L_POINTER)(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*GL_GET_VERTEX_ATTRIB_LDV)(GLuint index, GLenum pname, GLdouble *params)
ctypedef void (*GL_VIEWPORT_ARRAYV)(GLuint first, GLsizei count, const GLfloat *v)
ctypedef void (*GL_VIEWPORT_INDEXEDF)(GLuint index, GLfloat x, GLfloat y, GLfloat w, GLfloat h)
ctypedef void (*GL_VIEWPORT_INDEXEDFV)(GLuint index, const GLfloat *v)
ctypedef void (*GL_SCISSOR_ARRAYV)(GLuint first, GLsizei count, const GLint *v)
ctypedef void (*GL_SCISSOR_INDEXED)(GLuint index, GLint left, GLint bottom, GLsizei width, GLsizei height)
ctypedef void (*GL_SCISSOR_INDEXEDV)(GLuint index, const GLint *v)
ctypedef void (*GL_DEPTH_RANGE_ARRAYV)(GLuint first, GLsizei count, const GLdouble *v)
ctypedef void (*GL_DEPTH_RANGE_INDEXED)(GLuint index, GLdouble n, GLdouble f)
ctypedef void (*GL_GET_FLOATI_V)(GLenum target, GLuint index, GLfloat *data)
ctypedef void (*GL_GET_DOUBLEI_V)(GLenum target, GLuint index, GLdouble *data)

cdef GL_RELEASE_SHADER_COMPILER cglReleaseShaderCompiler = NULL
cdef GL_SHADER_BINARY cglShaderBinary = NULL
cdef GL_GET_SHADER_PRECISION_FORMAT cglGetShaderPrecisionFormat = NULL
cdef GL_DEPTH_RANGEF cglDepthRangef = NULL
cdef GL_CLEAR_DEPTHF cglClearDepthf = NULL
cdef GL_GET_PROGRAM_BINARY cglGetProgramBinary = NULL
cdef GL_PROGRAM_BINARY cglProgramBinary = NULL
cdef GL_PROGRAM_PARAMETERI cglProgramParameteri = NULL
cdef GL_USE_PROGRAM_STAGES cglUseProgramStages = NULL
cdef GL_ACTIVE_SHADER_PROGRAM cglActiveShaderProgram = NULL
cdef GL_CREATE_SHADER_PROGRAMV cglCreateShaderProgramv = NULL
cdef GL_BIND_PROGRAM_PIPELINE cglBindProgramPipeline = NULL
cdef GL_DELETE_PROGRAM_PIPELINES cglDeleteProgramPipelines = NULL
cdef GL_GEN_PROGRAM_PIPELINES cglGenProgramPipelines = NULL
cdef GL_IS_PROGRAM_PIPELINE cglIsProgramPipeline = NULL
cdef GL_GET_PROGRAM_PIPELINEIV cglGetProgramPipelineiv = NULL
cdef GL_PROGRAM_PARAMETERI cglProgramParameteri = NULL
cdef GL_PROGRAM_UNIFORM1I cglProgramUniform1i = NULL
cdef GL_PROGRAM_UNIFORM1IV cglProgramUniform1iv = NULL
cdef GL_PROGRAM_UNIFORM1F cglProgramUniform1f = NULL
cdef GL_PROGRAM_UNIFORM1FV cglProgramUniform1fv = NULL
cdef GL_PROGRAM_UNIFORM1D cglProgramUniform1d = NULL
cdef GL_PROGRAM_UNIFORM1DV cglProgramUniform1dv = NULL
cdef GL_PROGRAM_UNIFORM1UI cglProgramUniform1ui = NULL
cdef GL_PROGRAM_UNIFORM1UIV cglProgramUniform1uiv = NULL
cdef GL_PROGRAM_UNIFORM2I cglProgramUniform2i = NULL
cdef GL_PROGRAM_UNIFORM2IV cglProgramUniform2iv = NULL
cdef GL_PROGRAM_UNIFORM2F cglProgramUniform2f = NULL
cdef GL_PROGRAM_UNIFORM2FV cglProgramUniform2fv = NULL
cdef GL_PROGRAM_UNIFORM2D cglProgramUniform2d = NULL
cdef GL_PROGRAM_UNIFORM2DV cglProgramUniform2dv = NULL
cdef GL_PROGRAM_UNIFORM2UI cglProgramUniform2ui = NULL
cdef GL_PROGRAM_UNIFORM2UIV cglProgramUniform2uiv = NULL
cdef GL_PROGRAM_UNIFORM3I cglProgramUniform3i = NULL
cdef GL_PROGRAM_UNIFORM3IV cglProgramUniform3iv = NULL
cdef GL_PROGRAM_UNIFORM3F cglProgramUniform3f = NULL
cdef GL_PROGRAM_UNIFORM3FV cglProgramUniform3fv = NULL
cdef GL_PROGRAM_UNIFORM3D cglProgramUniform3d = NULL
cdef GL_PROGRAM_UNIFORM3DV cglProgramUniform3dv = NULL
cdef GL_PROGRAM_UNIFORM3UI cglProgramUniform3ui = NULL
cdef GL_PROGRAM_UNIFORM3UIV cglProgramUniform3uiv = NULL
cdef GL_PROGRAM_UNIFORM4I cglProgramUniform4i = NULL
cdef GL_PROGRAM_UNIFORM4IV cglProgramUniform4iv = NULL
cdef GL_PROGRAM_UNIFORM4F cglProgramUniform4f = NULL
cdef GL_PROGRAM_UNIFORM4FV cglProgramUniform4fv = NULL
cdef GL_PROGRAM_UNIFORM4D cglProgramUniform4d = NULL
cdef GL_PROGRAM_UNIFORM4DV cglProgramUniform4dv = NULL
cdef GL_PROGRAM_UNIFORM4UI cglProgramUniform4ui = NULL
cdef GL_PROGRAM_UNIFORM4UIV cglProgramUniform4uiv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX2FV cglProgramUniformMatrix2fv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX3FV cglProgramUniformMatrix3fv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX4FV cglProgramUniformMatrix4fv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX2DV cglProgramUniformMatrix2dv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX3DV cglProgramUniformMatrix3dv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX4DV cglProgramUniformMatrix4dv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX2X3FV cglProgramUniformMatrix2x3fv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX3X2FV cglProgramUniformMatrix3x2fv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX2X4FV cglProgramUniformMatrix2x4fv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX4X2FV cglProgramUniformMatrix4x2fv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX3X4FV cglProgramUniformMatrix3x4fv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX4X3FV cglProgramUniformMatrix4x3fv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX2X3DV cglProgramUniformMatrix2x3dv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX3X2DV cglProgramUniformMatrix3x2dv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX2X4DV cglProgramUniformMatrix2x4dv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX4X2DV cglProgramUniformMatrix4x2dv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX3X4DV cglProgramUniformMatrix3x4dv = NULL
cdef GL_PROGRAM_UNIFORM_MATRIX4X3DV cglProgramUniformMatrix4x3dv = NULL
cdef GL_VALIDATE_PROGRAM_PIPELINE cglValidateProgramPipeline = NULL
cdef GL_GET_PROGRAM_PIPELINE_INFO_LOG cglGetProgramPipelineInfoLog = NULL
cdef GL_VERTEX_ATTRIB_L1D cglVertexAttribL1d = NULL
cdef GL_VERTEX_ATTRIB_L2D cglVertexAttribL2d = NULL
cdef GL_VERTEX_ATTRIB_L3D cglVertexAttribL3d = NULL
cdef GL_VERTEX_ATTRIB_L4D cglVertexAttribL4d = NULL
cdef GL_VERTEX_ATTRIB_L1DV cglVertexAttribL1dv = NULL
cdef GL_VERTEX_ATTRIB_L2DV cglVertexAttribL2dv = NULL
cdef GL_VERTEX_ATTRIB_L3DV cglVertexAttribL3dv = NULL
cdef GL_VERTEX_ATTRIB_L4DV cglVertexAttribL4dv = NULL
cdef GL_VERTEX_ATTRIB_L_POINTER cglVertexAttribLPointer = NULL
cdef GL_GET_VERTEX_ATTRIB_LDV cglGetVertexAttribLdv = NULL
cdef GL_VIEWPORT_ARRAYV cglViewportArrayv = NULL
cdef GL_VIEWPORT_INDEXEDF cglViewportIndexedf = NULL
cdef GL_VIEWPORT_INDEXEDFV cglViewportIndexedfv = NULL
cdef GL_SCISSOR_ARRAYV cglScissorArrayv = NULL
cdef GL_SCISSOR_INDEXED cglScissorIndexed = NULL
cdef GL_SCISSOR_INDEXEDV cglScissorIndexedv = NULL
cdef GL_DEPTH_RANGE_ARRAYV cglDepthRangeArrayv = NULL
cdef GL_DEPTH_RANGE_INDEXED cglDepthRangeIndexed = NULL
cdef GL_GET_FLOATI_V cglGetFloati_v = NULL
cdef GL_GET_DOUBLEI_V cglGetDoublei_v = NULL


cdef void GetglReleaseShaderCompiler():
    global cglReleaseShaderCompiler
    cglReleaseShaderCompiler = <GL_RELEASE_SHADER_COMPILER>getFunction(b"glReleaseShaderCompiler")
    cglReleaseShaderCompiler()

cdef void GetglShaderBinary(GLsizei count, const GLuint *shaders, GLenum binaryFormat, const void *binary, GLsizei length):
    global cglShaderBinary
    cglShaderBinary = <GL_SHADER_BINARY>getFunction(b"glShaderBinary")
    cglShaderBinary(count, shaders, binaryFormat, binary, length)

cdef void GetglGetShaderPrecisionFormat(GLenum shadertype, GLenum precisiontype, GLint *range, GLint *precision):
    global cglGetShaderPrecisionFormat
    cglGetShaderPrecisionFormat = <GL_GET_SHADER_PRECISION_FORMAT>getFunction(b"glGetShaderPrecisionFormat")
    cglGetShaderPrecisionFormat(shadertype, precisiontype, range, precision)

cdef void GetglDepthRangef(GLfloat n, GLfloat f):
    global cglDepthRangef
    cglDepthRangef = <GL_DEPTH_RANGEF>getFunction(b"glDepthRangef")
    cglDepthRangef(n, f)

cdef void GetglClearDepthf(GLfloat d):
    global cglClearDepthf
    cglClearDepthf = <GL_CLEAR_DEPTHF>getFunction(b"glClearDepthf")
    cglClearDepthf(d)

cdef void GetglGetProgramBinary(GLuint program, GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, void *binary):
    global cglGetProgramBinary
    cglGetProgramBinary = <GL_GET_PROGRAM_BINARY>getFunction(b"glGetProgramBinary")
    cglGetProgramBinary(program, bufSize, length, binaryFormat, binary)

cdef void GetglProgramBinary(GLuint program, GLenum binaryFormat, const void *binary, GLsizei length):
    global cglProgramBinary
    cglProgramBinary = <GL_PROGRAM_BINARY>getFunction(b"glProgramBinary")
    cglProgramBinary(program, binaryFormat, binary, length)

cdef void GetglProgramParameteri(GLuint program, GLenum pname, GLint value):
    global cglProgramParameteri
    cglProgramParameteri = <GL_PROGRAM_PARAMETERI>getFunction(b"glProgramParameteri")
    cglProgramParameteri(program, pname, value)

cdef void GetglUseProgramStages(GLuint pipeline, GLbitfield stages, GLuint program):
    global cglUseProgramStages
    cglUseProgramStages = <GL_USE_PROGRAM_STAGES>getFunction(b"glUseProgramStages")
    cglUseProgramStages(pipeline, stages, program)

cdef void GetglActiveShaderProgram(GLuint pipeline, GLuint program):
    global cglActiveShaderProgram
    cglActiveShaderProgram = <GL_ACTIVE_SHADER_PROGRAM>getFunction(b"glActiveShaderProgram")
    cglActiveShaderProgram(pipeline, program)

cdef GLuint GetglCreateShaderProgramv(GLenum type, GLsizei count, const GLchar *const*strings):
    global cglCreateShaderProgramv
    cglCreateShaderProgramv = <GL_CREATE_SHADER_PROGRAMV>getFunction(b"glCreateShaderProgramv")
    cglCreateShaderProgramv(type, count, strings)

cdef void GetglBindProgramPipeline(GLuint pipeline):
    global cglBindProgramPipeline
    cglBindProgramPipeline = <GL_BIND_PROGRAM_PIPELINE>getFunction(b"glBindProgramPipeline")
    cglBindProgramPipeline(pipeline)

cdef void GetglDeleteProgramPipelines(GLsizei n, const GLuint *pipelines):
    global cglDeleteProgramPipelines
    cglDeleteProgramPipelines = <GL_DELETE_PROGRAM_PIPELINES>getFunction(b"glDeleteProgramPipelines")
    cglDeleteProgramPipelines(n, pipelines)

cdef void GetglGenProgramPipelines(GLsizei n, GLuint *pipelines):
    global cglGenProgramPipelines
    cglGenProgramPipelines = <GL_GEN_PROGRAM_PIPELINES>getFunction(b"glGenProgramPipelines")
    cglGenProgramPipelines(n, pipelines)

cdef GLboolean GetglIsProgramPipeline(GLuint pipeline):
    global cglIsProgramPipeline
    cglIsProgramPipeline = <GL_IS_PROGRAM_PIPELINE>getFunction(b"glIsProgramPipeline")
    cglIsProgramPipeline(pipeline)

cdef void GetglGetProgramPipelineiv(GLuint pipeline, GLenum pname, GLint *params):
    global cglGetProgramPipelineiv
    cglGetProgramPipelineiv = <GL_GET_PROGRAM_PIPELINEIV>getFunction(b"glGetProgramPipelineiv")
    cglGetProgramPipelineiv(pipeline, pname, params)

cdef void GetglProgramParameteri(GLuint program, GLenum pname, GLint value):
    global cglProgramParameteri
    cglProgramParameteri = <GL_PROGRAM_PARAMETERI>getFunction(b"glProgramParameteri")
    cglProgramParameteri(program, pname, value)

cdef void GetglProgramUniform1i(GLuint program, GLint location, GLint v0):
    global cglProgramUniform1i
    cglProgramUniform1i = <GL_PROGRAM_UNIFORM1I>getFunction(b"glProgramUniform1i")
    cglProgramUniform1i(program, location, v0)

cdef void GetglProgramUniform1iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    global cglProgramUniform1iv
    cglProgramUniform1iv = <GL_PROGRAM_UNIFORM1IV>getFunction(b"glProgramUniform1iv")
    cglProgramUniform1iv(program, location, count, value)

cdef void GetglProgramUniform1f(GLuint program, GLint location, GLfloat v0):
    global cglProgramUniform1f
    cglProgramUniform1f = <GL_PROGRAM_UNIFORM1F>getFunction(b"glProgramUniform1f")
    cglProgramUniform1f(program, location, v0)

cdef void GetglProgramUniform1fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    global cglProgramUniform1fv
    cglProgramUniform1fv = <GL_PROGRAM_UNIFORM1FV>getFunction(b"glProgramUniform1fv")
    cglProgramUniform1fv(program, location, count, value)

cdef void GetglProgramUniform1d(GLuint program, GLint location, GLdouble v0):
    global cglProgramUniform1d
    cglProgramUniform1d = <GL_PROGRAM_UNIFORM1D>getFunction(b"glProgramUniform1d")
    cglProgramUniform1d(program, location, v0)

cdef void GetglProgramUniform1dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    global cglProgramUniform1dv
    cglProgramUniform1dv = <GL_PROGRAM_UNIFORM1DV>getFunction(b"glProgramUniform1dv")
    cglProgramUniform1dv(program, location, count, value)

cdef void GetglProgramUniform1ui(GLuint program, GLint location, GLuint v0):
    global cglProgramUniform1ui
    cglProgramUniform1ui = <GL_PROGRAM_UNIFORM1UI>getFunction(b"glProgramUniform1ui")
    cglProgramUniform1ui(program, location, v0)

cdef void GetglProgramUniform1uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    global cglProgramUniform1uiv
    cglProgramUniform1uiv = <GL_PROGRAM_UNIFORM1UIV>getFunction(b"glProgramUniform1uiv")
    cglProgramUniform1uiv(program, location, count, value)

cdef void GetglProgramUniform2i(GLuint program, GLint location, GLint v0, GLint v1):
    global cglProgramUniform2i
    cglProgramUniform2i = <GL_PROGRAM_UNIFORM2I>getFunction(b"glProgramUniform2i")
    cglProgramUniform2i(program, location, v0, v1)

cdef void GetglProgramUniform2iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    global cglProgramUniform2iv
    cglProgramUniform2iv = <GL_PROGRAM_UNIFORM2IV>getFunction(b"glProgramUniform2iv")
    cglProgramUniform2iv(program, location, count, value)

cdef void GetglProgramUniform2f(GLuint program, GLint location, GLfloat v0, GLfloat v1):
    global cglProgramUniform2f
    cglProgramUniform2f = <GL_PROGRAM_UNIFORM2F>getFunction(b"glProgramUniform2f")
    cglProgramUniform2f(program, location, v0, v1)

cdef void GetglProgramUniform2fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    global cglProgramUniform2fv
    cglProgramUniform2fv = <GL_PROGRAM_UNIFORM2FV>getFunction(b"glProgramUniform2fv")
    cglProgramUniform2fv(program, location, count, value)

cdef void GetglProgramUniform2d(GLuint program, GLint location, GLdouble v0, GLdouble v1):
    global cglProgramUniform2d
    cglProgramUniform2d = <GL_PROGRAM_UNIFORM2D>getFunction(b"glProgramUniform2d")
    cglProgramUniform2d(program, location, v0, v1)

cdef void GetglProgramUniform2dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    global cglProgramUniform2dv
    cglProgramUniform2dv = <GL_PROGRAM_UNIFORM2DV>getFunction(b"glProgramUniform2dv")
    cglProgramUniform2dv(program, location, count, value)

cdef void GetglProgramUniform2ui(GLuint program, GLint location, GLuint v0, GLuint v1):
    global cglProgramUniform2ui
    cglProgramUniform2ui = <GL_PROGRAM_UNIFORM2UI>getFunction(b"glProgramUniform2ui")
    cglProgramUniform2ui(program, location, v0, v1)

cdef void GetglProgramUniform2uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    global cglProgramUniform2uiv
    cglProgramUniform2uiv = <GL_PROGRAM_UNIFORM2UIV>getFunction(b"glProgramUniform2uiv")
    cglProgramUniform2uiv(program, location, count, value)

cdef void GetglProgramUniform3i(GLuint program, GLint location, GLint v0, GLint v1, GLint v2):
    global cglProgramUniform3i
    cglProgramUniform3i = <GL_PROGRAM_UNIFORM3I>getFunction(b"glProgramUniform3i")
    cglProgramUniform3i(program, location, v0, v1, v2)

cdef void GetglProgramUniform3iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    global cglProgramUniform3iv
    cglProgramUniform3iv = <GL_PROGRAM_UNIFORM3IV>getFunction(b"glProgramUniform3iv")
    cglProgramUniform3iv(program, location, count, value)

cdef void GetglProgramUniform3f(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2):
    global cglProgramUniform3f
    cglProgramUniform3f = <GL_PROGRAM_UNIFORM3F>getFunction(b"glProgramUniform3f")
    cglProgramUniform3f(program, location, v0, v1, v2)

cdef void GetglProgramUniform3fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    global cglProgramUniform3fv
    cglProgramUniform3fv = <GL_PROGRAM_UNIFORM3FV>getFunction(b"glProgramUniform3fv")
    cglProgramUniform3fv(program, location, count, value)

cdef void GetglProgramUniform3d(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2):
    global cglProgramUniform3d
    cglProgramUniform3d = <GL_PROGRAM_UNIFORM3D>getFunction(b"glProgramUniform3d")
    cglProgramUniform3d(program, location, v0, v1, v2)

cdef void GetglProgramUniform3dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    global cglProgramUniform3dv
    cglProgramUniform3dv = <GL_PROGRAM_UNIFORM3DV>getFunction(b"glProgramUniform3dv")
    cglProgramUniform3dv(program, location, count, value)

cdef void GetglProgramUniform3ui(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2):
    global cglProgramUniform3ui
    cglProgramUniform3ui = <GL_PROGRAM_UNIFORM3UI>getFunction(b"glProgramUniform3ui")
    cglProgramUniform3ui(program, location, v0, v1, v2)

cdef void GetglProgramUniform3uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    global cglProgramUniform3uiv
    cglProgramUniform3uiv = <GL_PROGRAM_UNIFORM3UIV>getFunction(b"glProgramUniform3uiv")
    cglProgramUniform3uiv(program, location, count, value)

cdef void GetglProgramUniform4i(GLuint program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3):
    global cglProgramUniform4i
    cglProgramUniform4i = <GL_PROGRAM_UNIFORM4I>getFunction(b"glProgramUniform4i")
    cglProgramUniform4i(program, location, v0, v1, v2, v3)

cdef void GetglProgramUniform4iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    global cglProgramUniform4iv
    cglProgramUniform4iv = <GL_PROGRAM_UNIFORM4IV>getFunction(b"glProgramUniform4iv")
    cglProgramUniform4iv(program, location, count, value)

cdef void GetglProgramUniform4f(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3):
    global cglProgramUniform4f
    cglProgramUniform4f = <GL_PROGRAM_UNIFORM4F>getFunction(b"glProgramUniform4f")
    cglProgramUniform4f(program, location, v0, v1, v2, v3)

cdef void GetglProgramUniform4fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    global cglProgramUniform4fv
    cglProgramUniform4fv = <GL_PROGRAM_UNIFORM4FV>getFunction(b"glProgramUniform4fv")
    cglProgramUniform4fv(program, location, count, value)

cdef void GetglProgramUniform4d(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3):
    global cglProgramUniform4d
    cglProgramUniform4d = <GL_PROGRAM_UNIFORM4D>getFunction(b"glProgramUniform4d")
    cglProgramUniform4d(program, location, v0, v1, v2, v3)

cdef void GetglProgramUniform4dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    global cglProgramUniform4dv
    cglProgramUniform4dv = <GL_PROGRAM_UNIFORM4DV>getFunction(b"glProgramUniform4dv")
    cglProgramUniform4dv(program, location, count, value)

cdef void GetglProgramUniform4ui(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3):
    global cglProgramUniform4ui
    cglProgramUniform4ui = <GL_PROGRAM_UNIFORM4UI>getFunction(b"glProgramUniform4ui")
    cglProgramUniform4ui(program, location, v0, v1, v2, v3)

cdef void GetglProgramUniform4uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    global cglProgramUniform4uiv
    cglProgramUniform4uiv = <GL_PROGRAM_UNIFORM4UIV>getFunction(b"glProgramUniform4uiv")
    cglProgramUniform4uiv(program, location, count, value)

cdef void GetglProgramUniformMatrix2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix2fv
    cglProgramUniformMatrix2fv = <GL_PROGRAM_UNIFORM_MATRIX2FV>getFunction(b"glProgramUniformMatrix2fv")
    cglProgramUniformMatrix2fv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix3fv
    cglProgramUniformMatrix3fv = <GL_PROGRAM_UNIFORM_MATRIX3FV>getFunction(b"glProgramUniformMatrix3fv")
    cglProgramUniformMatrix3fv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix4fv
    cglProgramUniformMatrix4fv = <GL_PROGRAM_UNIFORM_MATRIX4FV>getFunction(b"glProgramUniformMatrix4fv")
    cglProgramUniformMatrix4fv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix2dv
    cglProgramUniformMatrix2dv = <GL_PROGRAM_UNIFORM_MATRIX2DV>getFunction(b"glProgramUniformMatrix2dv")
    cglProgramUniformMatrix2dv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix3dv
    cglProgramUniformMatrix3dv = <GL_PROGRAM_UNIFORM_MATRIX3DV>getFunction(b"glProgramUniformMatrix3dv")
    cglProgramUniformMatrix3dv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix4dv
    cglProgramUniformMatrix4dv = <GL_PROGRAM_UNIFORM_MATRIX4DV>getFunction(b"glProgramUniformMatrix4dv")
    cglProgramUniformMatrix4dv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix2x3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix2x3fv
    cglProgramUniformMatrix2x3fv = <GL_PROGRAM_UNIFORM_MATRIX2X3FV>getFunction(b"glProgramUniformMatrix2x3fv")
    cglProgramUniformMatrix2x3fv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix3x2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix3x2fv
    cglProgramUniformMatrix3x2fv = <GL_PROGRAM_UNIFORM_MATRIX3X2FV>getFunction(b"glProgramUniformMatrix3x2fv")
    cglProgramUniformMatrix3x2fv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix2x4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix2x4fv
    cglProgramUniformMatrix2x4fv = <GL_PROGRAM_UNIFORM_MATRIX2X4FV>getFunction(b"glProgramUniformMatrix2x4fv")
    cglProgramUniformMatrix2x4fv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix4x2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix4x2fv
    cglProgramUniformMatrix4x2fv = <GL_PROGRAM_UNIFORM_MATRIX4X2FV>getFunction(b"glProgramUniformMatrix4x2fv")
    cglProgramUniformMatrix4x2fv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix3x4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix3x4fv
    cglProgramUniformMatrix3x4fv = <GL_PROGRAM_UNIFORM_MATRIX3X4FV>getFunction(b"glProgramUniformMatrix3x4fv")
    cglProgramUniformMatrix3x4fv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix4x3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix4x3fv
    cglProgramUniformMatrix4x3fv = <GL_PROGRAM_UNIFORM_MATRIX4X3FV>getFunction(b"glProgramUniformMatrix4x3fv")
    cglProgramUniformMatrix4x3fv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix2x3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix2x3dv
    cglProgramUniformMatrix2x3dv = <GL_PROGRAM_UNIFORM_MATRIX2X3DV>getFunction(b"glProgramUniformMatrix2x3dv")
    cglProgramUniformMatrix2x3dv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix3x2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix3x2dv
    cglProgramUniformMatrix3x2dv = <GL_PROGRAM_UNIFORM_MATRIX3X2DV>getFunction(b"glProgramUniformMatrix3x2dv")
    cglProgramUniformMatrix3x2dv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix2x4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix2x4dv
    cglProgramUniformMatrix2x4dv = <GL_PROGRAM_UNIFORM_MATRIX2X4DV>getFunction(b"glProgramUniformMatrix2x4dv")
    cglProgramUniformMatrix2x4dv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix4x2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix4x2dv
    cglProgramUniformMatrix4x2dv = <GL_PROGRAM_UNIFORM_MATRIX4X2DV>getFunction(b"glProgramUniformMatrix4x2dv")
    cglProgramUniformMatrix4x2dv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix3x4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix3x4dv
    cglProgramUniformMatrix3x4dv = <GL_PROGRAM_UNIFORM_MATRIX3X4DV>getFunction(b"glProgramUniformMatrix3x4dv")
    cglProgramUniformMatrix3x4dv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix4x3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix4x3dv
    cglProgramUniformMatrix4x3dv = <GL_PROGRAM_UNIFORM_MATRIX4X3DV>getFunction(b"glProgramUniformMatrix4x3dv")
    cglProgramUniformMatrix4x3dv(program, location, count, transpose, value)

cdef void GetglValidateProgramPipeline(GLuint pipeline):
    global cglValidateProgramPipeline
    cglValidateProgramPipeline = <GL_VALIDATE_PROGRAM_PIPELINE>getFunction(b"glValidateProgramPipeline")
    cglValidateProgramPipeline(pipeline)

cdef void GetglGetProgramPipelineInfoLog(GLuint pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    global cglGetProgramPipelineInfoLog
    cglGetProgramPipelineInfoLog = <GL_GET_PROGRAM_PIPELINE_INFO_LOG>getFunction(b"glGetProgramPipelineInfoLog")
    cglGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog)

cdef void GetglVertexAttribL1d(GLuint index, GLdouble x):
    global cglVertexAttribL1d
    cglVertexAttribL1d = <GL_VERTEX_ATTRIB_L1D>getFunction(b"glVertexAttribL1d")
    cglVertexAttribL1d(index, x)

cdef void GetglVertexAttribL2d(GLuint index, GLdouble x, GLdouble y):
    global cglVertexAttribL2d
    cglVertexAttribL2d = <GL_VERTEX_ATTRIB_L2D>getFunction(b"glVertexAttribL2d")
    cglVertexAttribL2d(index, x, y)

cdef void GetglVertexAttribL3d(GLuint index, GLdouble x, GLdouble y, GLdouble z):
    global cglVertexAttribL3d
    cglVertexAttribL3d = <GL_VERTEX_ATTRIB_L3D>getFunction(b"glVertexAttribL3d")
    cglVertexAttribL3d(index, x, y, z)

cdef void GetglVertexAttribL4d(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglVertexAttribL4d
    cglVertexAttribL4d = <GL_VERTEX_ATTRIB_L4D>getFunction(b"glVertexAttribL4d")
    cglVertexAttribL4d(index, x, y, z, w)

cdef void GetglVertexAttribL1dv(GLuint index, const GLdouble *v):
    global cglVertexAttribL1dv
    cglVertexAttribL1dv = <GL_VERTEX_ATTRIB_L1DV>getFunction(b"glVertexAttribL1dv")
    cglVertexAttribL1dv(index, v)

cdef void GetglVertexAttribL2dv(GLuint index, const GLdouble *v):
    global cglVertexAttribL2dv
    cglVertexAttribL2dv = <GL_VERTEX_ATTRIB_L2DV>getFunction(b"glVertexAttribL2dv")
    cglVertexAttribL2dv(index, v)

cdef void GetglVertexAttribL3dv(GLuint index, const GLdouble *v):
    global cglVertexAttribL3dv
    cglVertexAttribL3dv = <GL_VERTEX_ATTRIB_L3DV>getFunction(b"glVertexAttribL3dv")
    cglVertexAttribL3dv(index, v)

cdef void GetglVertexAttribL4dv(GLuint index, const GLdouble *v):
    global cglVertexAttribL4dv
    cglVertexAttribL4dv = <GL_VERTEX_ATTRIB_L4DV>getFunction(b"glVertexAttribL4dv")
    cglVertexAttribL4dv(index, v)

cdef void GetglVertexAttribLPointer(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglVertexAttribLPointer
    cglVertexAttribLPointer = <GL_VERTEX_ATTRIB_L_POINTER>getFunction(b"glVertexAttribLPointer")
    cglVertexAttribLPointer(index, size, type, stride, pointer)

cdef void GetglGetVertexAttribLdv(GLuint index, GLenum pname, GLdouble *params):
    global cglGetVertexAttribLdv
    cglGetVertexAttribLdv = <GL_GET_VERTEX_ATTRIB_LDV>getFunction(b"glGetVertexAttribLdv")
    cglGetVertexAttribLdv(index, pname, params)

cdef void GetglViewportArrayv(GLuint first, GLsizei count, const GLfloat *v):
    global cglViewportArrayv
    cglViewportArrayv = <GL_VIEWPORT_ARRAYV>getFunction(b"glViewportArrayv")
    cglViewportArrayv(first, count, v)

cdef void GetglViewportIndexedf(GLuint index, GLfloat x, GLfloat y, GLfloat w, GLfloat h):
    global cglViewportIndexedf
    cglViewportIndexedf = <GL_VIEWPORT_INDEXEDF>getFunction(b"glViewportIndexedf")
    cglViewportIndexedf(index, x, y, w, h)

cdef void GetglViewportIndexedfv(GLuint index, const GLfloat *v):
    global cglViewportIndexedfv
    cglViewportIndexedfv = <GL_VIEWPORT_INDEXEDFV>getFunction(b"glViewportIndexedfv")
    cglViewportIndexedfv(index, v)

cdef void GetglScissorArrayv(GLuint first, GLsizei count, const GLint *v):
    global cglScissorArrayv
    cglScissorArrayv = <GL_SCISSOR_ARRAYV>getFunction(b"glScissorArrayv")
    cglScissorArrayv(first, count, v)

cdef void GetglScissorIndexed(GLuint index, GLint left, GLint bottom, GLsizei width, GLsizei height):
    global cglScissorIndexed
    cglScissorIndexed = <GL_SCISSOR_INDEXED>getFunction(b"glScissorIndexed")
    cglScissorIndexed(index, left, bottom, width, height)

cdef void GetglScissorIndexedv(GLuint index, const GLint *v):
    global cglScissorIndexedv
    cglScissorIndexedv = <GL_SCISSOR_INDEXEDV>getFunction(b"glScissorIndexedv")
    cglScissorIndexedv(index, v)

cdef void GetglDepthRangeArrayv(GLuint first, GLsizei count, const GLdouble *v):
    global cglDepthRangeArrayv
    cglDepthRangeArrayv = <GL_DEPTH_RANGE_ARRAYV>getFunction(b"glDepthRangeArrayv")
    cglDepthRangeArrayv(first, count, v)

cdef void GetglDepthRangeIndexed(GLuint index, GLdouble n, GLdouble f):
    global cglDepthRangeIndexed
    cglDepthRangeIndexed = <GL_DEPTH_RANGE_INDEXED>getFunction(b"glDepthRangeIndexed")
    cglDepthRangeIndexed(index, n, f)

cdef void GetglGetFloati_v(GLenum target, GLuint index, GLfloat *data):
    global cglGetFloati_v
    cglGetFloati_v = <GL_GET_FLOATI_V>getFunction(b"glGetFloati_v")
    cglGetFloati_v(target, index, data)

cdef void GetglGetDoublei_v(GLenum target, GLuint index, GLdouble *data):
    global cglGetDoublei_v
    cglGetDoublei_v = <GL_GET_DOUBLEI_V>getFunction(b"glGetDoublei_v")
    cglGetDoublei_v(target, index, data)

cglReleaseShaderCompiler = GetglReleaseShaderCompiler
cglShaderBinary = GetglShaderBinary
cglGetShaderPrecisionFormat = GetglGetShaderPrecisionFormat
cglDepthRangef = GetglDepthRangef
cglClearDepthf = GetglClearDepthf
cglGetProgramBinary = GetglGetProgramBinary
cglProgramBinary = GetglProgramBinary
cglProgramParameteri = GetglProgramParameteri
cglUseProgramStages = GetglUseProgramStages
cglActiveShaderProgram = GetglActiveShaderProgram
cglCreateShaderProgramv = GetglCreateShaderProgramv
cglBindProgramPipeline = GetglBindProgramPipeline
cglDeleteProgramPipelines = GetglDeleteProgramPipelines
cglGenProgramPipelines = GetglGenProgramPipelines
cglIsProgramPipeline = GetglIsProgramPipeline
cglGetProgramPipelineiv = GetglGetProgramPipelineiv
cglProgramParameteri = GetglProgramParameteri
cglProgramUniform1i = GetglProgramUniform1i
cglProgramUniform1iv = GetglProgramUniform1iv
cglProgramUniform1f = GetglProgramUniform1f
cglProgramUniform1fv = GetglProgramUniform1fv
cglProgramUniform1d = GetglProgramUniform1d
cglProgramUniform1dv = GetglProgramUniform1dv
cglProgramUniform1ui = GetglProgramUniform1ui
cglProgramUniform1uiv = GetglProgramUniform1uiv
cglProgramUniform2i = GetglProgramUniform2i
cglProgramUniform2iv = GetglProgramUniform2iv
cglProgramUniform2f = GetglProgramUniform2f
cglProgramUniform2fv = GetglProgramUniform2fv
cglProgramUniform2d = GetglProgramUniform2d
cglProgramUniform2dv = GetglProgramUniform2dv
cglProgramUniform2ui = GetglProgramUniform2ui
cglProgramUniform2uiv = GetglProgramUniform2uiv
cglProgramUniform3i = GetglProgramUniform3i
cglProgramUniform3iv = GetglProgramUniform3iv
cglProgramUniform3f = GetglProgramUniform3f
cglProgramUniform3fv = GetglProgramUniform3fv
cglProgramUniform3d = GetglProgramUniform3d
cglProgramUniform3dv = GetglProgramUniform3dv
cglProgramUniform3ui = GetglProgramUniform3ui
cglProgramUniform3uiv = GetglProgramUniform3uiv
cglProgramUniform4i = GetglProgramUniform4i
cglProgramUniform4iv = GetglProgramUniform4iv
cglProgramUniform4f = GetglProgramUniform4f
cglProgramUniform4fv = GetglProgramUniform4fv
cglProgramUniform4d = GetglProgramUniform4d
cglProgramUniform4dv = GetglProgramUniform4dv
cglProgramUniform4ui = GetglProgramUniform4ui
cglProgramUniform4uiv = GetglProgramUniform4uiv
cglProgramUniformMatrix2fv = GetglProgramUniformMatrix2fv
cglProgramUniformMatrix3fv = GetglProgramUniformMatrix3fv
cglProgramUniformMatrix4fv = GetglProgramUniformMatrix4fv
cglProgramUniformMatrix2dv = GetglProgramUniformMatrix2dv
cglProgramUniformMatrix3dv = GetglProgramUniformMatrix3dv
cglProgramUniformMatrix4dv = GetglProgramUniformMatrix4dv
cglProgramUniformMatrix2x3fv = GetglProgramUniformMatrix2x3fv
cglProgramUniformMatrix3x2fv = GetglProgramUniformMatrix3x2fv
cglProgramUniformMatrix2x4fv = GetglProgramUniformMatrix2x4fv
cglProgramUniformMatrix4x2fv = GetglProgramUniformMatrix4x2fv
cglProgramUniformMatrix3x4fv = GetglProgramUniformMatrix3x4fv
cglProgramUniformMatrix4x3fv = GetglProgramUniformMatrix4x3fv
cglProgramUniformMatrix2x3dv = GetglProgramUniformMatrix2x3dv
cglProgramUniformMatrix3x2dv = GetglProgramUniformMatrix3x2dv
cglProgramUniformMatrix2x4dv = GetglProgramUniformMatrix2x4dv
cglProgramUniformMatrix4x2dv = GetglProgramUniformMatrix4x2dv
cglProgramUniformMatrix3x4dv = GetglProgramUniformMatrix3x4dv
cglProgramUniformMatrix4x3dv = GetglProgramUniformMatrix4x3dv
cglValidateProgramPipeline = GetglValidateProgramPipeline
cglGetProgramPipelineInfoLog = GetglGetProgramPipelineInfoLog
cglVertexAttribL1d = GetglVertexAttribL1d
cglVertexAttribL2d = GetglVertexAttribL2d
cglVertexAttribL3d = GetglVertexAttribL3d
cglVertexAttribL4d = GetglVertexAttribL4d
cglVertexAttribL1dv = GetglVertexAttribL1dv
cglVertexAttribL2dv = GetglVertexAttribL2dv
cglVertexAttribL3dv = GetglVertexAttribL3dv
cglVertexAttribL4dv = GetglVertexAttribL4dv
cglVertexAttribLPointer = GetglVertexAttribLPointer
cglGetVertexAttribLdv = GetglGetVertexAttribLdv
cglViewportArrayv = GetglViewportArrayv
cglViewportIndexedf = GetglViewportIndexedf
cglViewportIndexedfv = GetglViewportIndexedfv
cglScissorArrayv = GetglScissorArrayv
cglScissorIndexed = GetglScissorIndexed
cglScissorIndexedv = GetglScissorIndexedv
cglDepthRangeArrayv = GetglDepthRangeArrayv
cglDepthRangeIndexed = GetglDepthRangeIndexed
cglGetFloati_v = GetglGetFloati_v
cglGetDoublei_v = GetglGetDoublei_v


cpdef void glReleaseShaderCompiler():
    cglReleaseShaderCompiler()

cpdef void glShaderBinary(GLsizei count, const GLuint *shaders, GLenum binaryFormat, const void *binary, GLsizei length):
    cglShaderBinary(count, shaders, binaryFormat, binary, length)

cpdef void glGetShaderPrecisionFormat(GLenum shadertype, GLenum precisiontype, GLint *range, GLint *precision):
    cglGetShaderPrecisionFormat(shadertype, precisiontype, range, precision)

cpdef void glDepthRangef(GLfloat n, GLfloat f):
    cglDepthRangef(n, f)

cpdef void glClearDepthf(GLfloat d):
    cglClearDepthf(d)

cpdef void glGetProgramBinary(GLuint program, GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, void *binary):
    cglGetProgramBinary(program, bufSize, length, binaryFormat, binary)

cpdef void glProgramBinary(GLuint program, GLenum binaryFormat, const void *binary, GLsizei length):
    cglProgramBinary(program, binaryFormat, binary, length)

cpdef void glProgramParameteri(GLuint program, GLenum pname, GLint value):
    cglProgramParameteri(program, pname, value)

cpdef void glUseProgramStages(GLuint pipeline, GLbitfield stages, GLuint program):
    cglUseProgramStages(pipeline, stages, program)

cpdef void glActiveShaderProgram(GLuint pipeline, GLuint program):
    cglActiveShaderProgram(pipeline, program)

cpdef GLuint glCreateShaderProgramv(GLenum type, GLsizei count, const GLchar *const*strings):
    cglCreateShaderProgramv(type, count, strings)

cpdef void glBindProgramPipeline(GLuint pipeline):
    cglBindProgramPipeline(pipeline)

cpdef void glDeleteProgramPipelines(GLsizei n, const GLuint *pipelines):
    cglDeleteProgramPipelines(n, pipelines)

cpdef void glGenProgramPipelines(GLsizei n, GLuint *pipelines):
    cglGenProgramPipelines(n, pipelines)

cpdef GLboolean glIsProgramPipeline(GLuint pipeline):
    cglIsProgramPipeline(pipeline)

cpdef void glGetProgramPipelineiv(GLuint pipeline, GLenum pname, GLint *params):
    cglGetProgramPipelineiv(pipeline, pname, params)

cpdef void glProgramParameteri(GLuint program, GLenum pname, GLint value):
    cglProgramParameteri(program, pname, value)

cpdef void glProgramUniform1i(GLuint program, GLint location, GLint v0):
    cglProgramUniform1i(program, location, v0)

cpdef void glProgramUniform1iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    cglProgramUniform1iv(program, location, count, value)

cpdef void glProgramUniform1f(GLuint program, GLint location, GLfloat v0):
    cglProgramUniform1f(program, location, v0)

cpdef void glProgramUniform1fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    cglProgramUniform1fv(program, location, count, value)

cpdef void glProgramUniform1d(GLuint program, GLint location, GLdouble v0):
    cglProgramUniform1d(program, location, v0)

cpdef void glProgramUniform1dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    cglProgramUniform1dv(program, location, count, value)

cpdef void glProgramUniform1ui(GLuint program, GLint location, GLuint v0):
    cglProgramUniform1ui(program, location, v0)

cpdef void glProgramUniform1uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    cglProgramUniform1uiv(program, location, count, value)

cpdef void glProgramUniform2i(GLuint program, GLint location, GLint v0, GLint v1):
    cglProgramUniform2i(program, location, v0, v1)

cpdef void glProgramUniform2iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    cglProgramUniform2iv(program, location, count, value)

cpdef void glProgramUniform2f(GLuint program, GLint location, GLfloat v0, GLfloat v1):
    cglProgramUniform2f(program, location, v0, v1)

cpdef void glProgramUniform2fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    cglProgramUniform2fv(program, location, count, value)

cpdef void glProgramUniform2d(GLuint program, GLint location, GLdouble v0, GLdouble v1):
    cglProgramUniform2d(program, location, v0, v1)

cpdef void glProgramUniform2dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    cglProgramUniform2dv(program, location, count, value)

cpdef void glProgramUniform2ui(GLuint program, GLint location, GLuint v0, GLuint v1):
    cglProgramUniform2ui(program, location, v0, v1)

cpdef void glProgramUniform2uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    cglProgramUniform2uiv(program, location, count, value)

cpdef void glProgramUniform3i(GLuint program, GLint location, GLint v0, GLint v1, GLint v2):
    cglProgramUniform3i(program, location, v0, v1, v2)

cpdef void glProgramUniform3iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    cglProgramUniform3iv(program, location, count, value)

cpdef void glProgramUniform3f(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2):
    cglProgramUniform3f(program, location, v0, v1, v2)

cpdef void glProgramUniform3fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    cglProgramUniform3fv(program, location, count, value)

cpdef void glProgramUniform3d(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2):
    cglProgramUniform3d(program, location, v0, v1, v2)

cpdef void glProgramUniform3dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    cglProgramUniform3dv(program, location, count, value)

cpdef void glProgramUniform3ui(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2):
    cglProgramUniform3ui(program, location, v0, v1, v2)

cpdef void glProgramUniform3uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    cglProgramUniform3uiv(program, location, count, value)

cpdef void glProgramUniform4i(GLuint program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3):
    cglProgramUniform4i(program, location, v0, v1, v2, v3)

cpdef void glProgramUniform4iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    cglProgramUniform4iv(program, location, count, value)

cpdef void glProgramUniform4f(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3):
    cglProgramUniform4f(program, location, v0, v1, v2, v3)

cpdef void glProgramUniform4fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    cglProgramUniform4fv(program, location, count, value)

cpdef void glProgramUniform4d(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3):
    cglProgramUniform4d(program, location, v0, v1, v2, v3)

cpdef void glProgramUniform4dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    cglProgramUniform4dv(program, location, count, value)

cpdef void glProgramUniform4ui(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3):
    cglProgramUniform4ui(program, location, v0, v1, v2, v3)

cpdef void glProgramUniform4uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    cglProgramUniform4uiv(program, location, count, value)

cpdef void glProgramUniformMatrix2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix2fv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix3fv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix4fv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix2dv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix3dv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix4dv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix2x3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix2x3fv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix3x2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix3x2fv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix2x4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix2x4fv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix4x2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix4x2fv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix3x4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix3x4fv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix4x3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix4x3fv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix2x3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix2x3dv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix3x2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix3x2dv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix2x4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix2x4dv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix4x2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix4x2dv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix3x4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix3x4dv(program, location, count, transpose, value)

cpdef void glProgramUniformMatrix4x3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix4x3dv(program, location, count, transpose, value)

cpdef void glValidateProgramPipeline(GLuint pipeline):
    cglValidateProgramPipeline(pipeline)

cpdef void glGetProgramPipelineInfoLog(GLuint pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    cglGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog)

cpdef void glVertexAttribL1d(GLuint index, GLdouble x):
    cglVertexAttribL1d(index, x)

cpdef void glVertexAttribL2d(GLuint index, GLdouble x, GLdouble y):
    cglVertexAttribL2d(index, x, y)

cpdef void glVertexAttribL3d(GLuint index, GLdouble x, GLdouble y, GLdouble z):
    cglVertexAttribL3d(index, x, y, z)

cpdef void glVertexAttribL4d(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglVertexAttribL4d(index, x, y, z, w)

cpdef void glVertexAttribL1dv(GLuint index, const GLdouble *v):
    cglVertexAttribL1dv(index, v)

cpdef void glVertexAttribL2dv(GLuint index, const GLdouble *v):
    cglVertexAttribL2dv(index, v)

cpdef void glVertexAttribL3dv(GLuint index, const GLdouble *v):
    cglVertexAttribL3dv(index, v)

cpdef void glVertexAttribL4dv(GLuint index, const GLdouble *v):
    cglVertexAttribL4dv(index, v)

cpdef void glVertexAttribLPointer(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglVertexAttribLPointer(index, size, type, stride, pointer)

cpdef void glGetVertexAttribLdv(GLuint index, GLenum pname, GLdouble *params):
    cglGetVertexAttribLdv(index, pname, params)

cpdef void glViewportArrayv(GLuint first, GLsizei count, const GLfloat *v):
    cglViewportArrayv(first, count, v)

cpdef void glViewportIndexedf(GLuint index, GLfloat x, GLfloat y, GLfloat w, GLfloat h):
    cglViewportIndexedf(index, x, y, w, h)

cpdef void glViewportIndexedfv(GLuint index, const GLfloat *v):
    cglViewportIndexedfv(index, v)

cpdef void glScissorArrayv(GLuint first, GLsizei count, const GLint *v):
    cglScissorArrayv(first, count, v)

cpdef void glScissorIndexed(GLuint index, GLint left, GLint bottom, GLsizei width, GLsizei height):
    cglScissorIndexed(index, left, bottom, width, height)

cpdef void glScissorIndexedv(GLuint index, const GLint *v):
    cglScissorIndexedv(index, v)

cpdef void glDepthRangeArrayv(GLuint first, GLsizei count, const GLdouble *v):
    cglDepthRangeArrayv(first, count, v)

cpdef void glDepthRangeIndexed(GLuint index, GLdouble n, GLdouble f):
    cglDepthRangeIndexed(index, n, f)

cpdef void glGetFloati_v(GLenum target, GLuint index, GLfloat *data):
    cglGetFloati_v(target, index, data)

cpdef void glGetDoublei_v(GLenum target, GLuint index, GLdouble *data):
    cglGetDoublei_v(target, index, data)
