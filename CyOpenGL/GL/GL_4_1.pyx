# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
cdef GLenum GL_SHADER_BINARY_FORMATS = 0x8DF8
cdef GLenum GL_NUM_PROGRAM_BINARY_FORMATS = 0x87FE
cdef GLenum GL_HIGH_FLOAT = 0x8DF2
cdef GLenum GL_VIEWPORT_SUBPIXEL_BITS = 0x825C
cdef GLenum GL_LOW_FLOAT = 0x8DF0
cdef GLenum GL_PROGRAM_BINARY_FORMATS = 0x87FF
cdef GLenum GL_ALL_SHADER_BITS = 0xFFFFFFFF
cdef GLenum GL_PROGRAM_PIPELINE_BINDING = 0x825A
cdef GLenum GL_MEDIUM_INT = 0x8DF4
cdef GLenum GL_LOW_INT = 0x8DF3
cdef GLenum GL_LAYER_PROVOKING_VERTEX = 0x825E
cdef GLenum GL_TESS_EVALUATION_SHADER_BIT = 0x00000010
cdef GLenum GL_PROGRAM_BINARY_RETRIEVABLE_HINT = 0x8257
cdef GLenum GL_MEDIUM_FLOAT = 0x8DF1
cdef GLenum GL_NUM_SHADER_BINARY_FORMATS = 0x8DF9
cdef GLenum GL_MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
cdef GLenum GL_FRAGMENT_SHADER_BIT = 0x00000002
cdef GLenum GL_IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
cdef GLenum GL_PROGRAM_SEPARABLE = 0x8258
cdef GLenum GL_UNDEFINED_VERTEX = 0x8260
cdef GLenum GL_RGB565 = 0x8D62
cdef GLenum GL_MAX_VIEWPORTS = 0x825B
cdef GLenum GL_MAX_VARYING_VECTORS = 0x8DFC
cdef GLenum GL_GEOMETRY_SHADER_BIT = 0x00000004
cdef GLenum GL_FIXED = 0x140C
cdef GLenum GL_SHADER_COMPILER = 0x8DFA
cdef GLenum GL_ACTIVE_PROGRAM = 0x8259
cdef GLenum GL_HIGH_INT = 0x8DF5
cdef GLenum GL_PROGRAM_BINARY_LENGTH = 0x8741
cdef GLenum GL_VIEWPORT_INDEX_PROVOKING_VERTEX = 0x825F
cdef GLenum GL_TESS_CONTROL_SHADER_BIT = 0x00000008
cdef GLenum GL_VIEWPORT_BOUNDS_RANGE = 0x825D
cdef GLenum GL_VERTEX_SHADER_BIT = 0x00000001
cdef GLenum GL_IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B

ctypedef void (*PFNGLSHADERBINARYPROC)(GLsizei count, const GLuint *shaders, GLenum binaryFormat, const void *binary, GLsizei length)
ctypedef void (*PFNGLPROGRAMBINARYPROC)(GLuint program, GLenum binaryFormat, const void *binary, GLsizei length)
ctypedef void (*PFNGLGETPROGRAMBINARYPROC)(GLuint program, GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, void *binary)
ctypedef GLboolean (*PFNGLISPROGRAMPIPELINEPROC)(GLuint pipeline)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX3X2FVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLVERTEXATTRIBL2DPROC)(GLuint index, GLdouble x, GLdouble y)
ctypedef void (*PFNGLPROGRAMUNIFORM2IPROC)(GLuint program, GLint location, GLint v0, GLint v1)
ctypedef void (*PFNGLPROGRAMUNIFORM1FVPROC)(GLuint program, GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*PFNGLPROGRAMUNIFORM1FPROC)(GLuint program, GLint location, GLfloat v0)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX4X3DVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLVERTEXATTRIBL1DVPROC)(GLuint index, const GLdouble *v)
ctypedef void (*PFNGLPROGRAMUNIFORM1UIPROC)(GLuint program, GLint location, GLuint v0)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX2X4FVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX2FVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLDEPTHRANGEINDEXEDPROC)(GLuint index, GLdouble n, GLdouble f)
ctypedef void (*PFNGLVERTEXATTRIBLPOINTERPROC)(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*PFNGLVERTEXATTRIBL4DVPROC)(GLuint index, const GLdouble *v)
ctypedef void (*PFNGLGETPROGRAMPIPELINEIVPROC)(GLuint pipeline, GLenum pname, GLint *params)
ctypedef void (*PFNGLPROGRAMUNIFORM2UIPROC)(GLuint program, GLint location, GLuint v0, GLuint v1)
ctypedef void (*PFNGLPROGRAMUNIFORM3FPROC)(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2)
ctypedef GLuint (*PFNGLCREATESHADERPROGRAMVPROC)(GLenum type, GLsizei count, const GLchar **strings)
ctypedef void (*PFNGLGETSHADERPRECISIONFORMATPROC)(GLenum shadertype, GLenum precisiontype, GLint *range, GLint *precision)
ctypedef void (*PFNGLVIEWPORTINDEXEDFVPROC)(GLuint index, const GLfloat *v)
ctypedef void (*PFNGLPROGRAMUNIFORM3IVPROC)(GLuint program, GLint location, GLsizei count, const GLint *value)
ctypedef void (*PFNGLPROGRAMUNIFORM2IVPROC)(GLuint program, GLint location, GLsizei count, const GLint *value)
ctypedef void (*PFNGLVALIDATEPROGRAMPIPELINEPROC)(GLuint pipeline)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX2X4DVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLVERTEXATTRIBL1DPROC)(GLuint index, GLdouble x)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX3FVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLVERTEXATTRIBL4DPROC)(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX4DVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX3X4DVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLDEPTHRANGEARRAYVPROC)(GLuint first, GLsizei count, const GLdouble *v)
ctypedef void (*PFNGLPROGRAMUNIFORM4UIPROC)(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX4X2FVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLPROGRAMUNIFORM4IPROC)(GLuint program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX2DVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLVIEWPORTINDEXEDFPROC)(GLuint index, GLfloat x, GLfloat y, GLfloat w, GLfloat h)
ctypedef void (*PFNGLVERTEXATTRIBL2DVPROC)(GLuint index, const GLdouble *v)
ctypedef void (*PFNGLRELEASESHADERCOMPILERPROC)()
ctypedef void (*PFNGLDEPTHRANGEFPROC)(GLfloat n, GLfloat f)
ctypedef void (*PFNGLPROGRAMUNIFORM4UIVPROC)(GLuint program, GLint location, GLsizei count, const GLuint *value)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX2X3FVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLPROGRAMUNIFORM4IVPROC)(GLuint program, GLint location, GLsizei count, const GLint *value)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX3DVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLPROGRAMUNIFORM1IVPROC)(GLuint program, GLint location, GLsizei count, const GLint *value)
ctypedef void (*PFNGLPROGRAMPARAMETERIPROC)(GLuint program, GLenum pname, GLint value)
ctypedef void (*PFNGLPROGRAMUNIFORM2FPROC)(GLuint program, GLint location, GLfloat v0, GLfloat v1)
ctypedef void (*PFNGLVIEWPORTARRAYVPROC)(GLuint first, GLsizei count, const GLfloat *v)
ctypedef void (*PFNGLPROGRAMUNIFORM3FVPROC)(GLuint program, GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*PFNGLCLEARDEPTHFPROC)(GLfloat d)
ctypedef void (*PFNGLPROGRAMUNIFORM4DVPROC)(GLuint program, GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLPROGRAMUNIFORM4FPROC)(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX4FVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLPROGRAMUNIFORM2UIVPROC)(GLuint program, GLint location, GLsizei count, const GLuint *value)
ctypedef void (*PFNGLVERTEXATTRIBL3DPROC)(GLuint index, GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*PFNGLGETVERTEXATTRIBLDVPROC)(GLuint index, GLenum pname, GLdouble *params)
ctypedef void (*PFNGLSCISSORARRAYVPROC)(GLuint first, GLsizei count, const GLint *v)
ctypedef void (*PFNGLSCISSORINDEXEDVPROC)(GLuint index, const GLint *v)
ctypedef void (*PFNGLPROGRAMUNIFORM1IPROC)(GLuint program, GLint location, GLint v0)
ctypedef void (*PFNGLGETFLOATI_VPROC)(GLenum target, GLuint index, GLfloat *data)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX4X3FVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLSCISSORINDEXEDPROC)(GLuint index, GLint left, GLint bottom, GLsizei width, GLsizei height)
ctypedef void (*PFNGLPROGRAMUNIFORM2DPROC)(GLuint program, GLint location, GLdouble v0, GLdouble v1)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX4X2DVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLPROGRAMUNIFORM3DVPROC)(GLuint program, GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLPROGRAMUNIFORM3UIPROC)(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2)
ctypedef void (*PFNGLBINDPROGRAMPIPELINEPROC)(GLuint pipeline)
ctypedef void (*PFNGLGETDOUBLEI_VPROC)(GLenum target, GLuint index, GLdouble *data)
ctypedef void (*PFNGLVERTEXATTRIBL3DVPROC)(GLuint index, const GLdouble *v)
ctypedef void (*PFNGLPROGRAMUNIFORM1DVPROC)(GLuint program, GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLUSEPROGRAMSTAGESPROC)(GLuint pipeline, GLbitfield stages, GLuint program)
ctypedef void (*PFNGLPROGRAMUNIFORM1UIVPROC)(GLuint program, GLint location, GLsizei count, const GLuint *value)
ctypedef void (*PFNGLGENPROGRAMPIPELINESPROC)(GLsizei n, GLuint *pipelines)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX3X4FVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLPROGRAMUNIFORM1DPROC)(GLuint program, GLint location, GLdouble v0)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX3X2DVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLDELETEPROGRAMPIPELINESPROC)(GLsizei n, const GLuint *pipelines)
ctypedef void (*PFNGLACTIVESHADERPROGRAMPROC)(GLuint pipeline, GLuint program)
ctypedef void (*PFNGLGETPROGRAMPIPELINEINFOLOGPROC)(GLuint pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
ctypedef void (*PFNGLPROGRAMUNIFORM2FVPROC)(GLuint program, GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*PFNGLPROGRAMUNIFORM3IPROC)(GLuint program, GLint location, GLint v0, GLint v1, GLint v2)
ctypedef void (*PFNGLPROGRAMUNIFORM3DPROC)(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2)
ctypedef void (*PFNGLPROGRAMUNIFORM4FVPROC)(GLuint program, GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*PFNGLPROGRAMUNIFORMMATRIX2X3DVPROC)(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLPROGRAMUNIFORM4DPROC)(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3)
ctypedef void (*PFNGLPROGRAMUNIFORM3UIVPROC)(GLuint program, GLint location, GLsizei count, const GLuint *value)
ctypedef void (*PFNGLPROGRAMUNIFORM2DVPROC)(GLuint program, GLint location, GLsizei count, const GLdouble *value)

cdef PFNGLSHADERBINARYPROC cglShaderBinary = NULL
cdef PFNGLPROGRAMBINARYPROC cglProgramBinary = NULL
cdef PFNGLGETPROGRAMBINARYPROC cglGetProgramBinary = NULL
cdef PFNGLISPROGRAMPIPELINEPROC cglIsProgramPipeline = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX3X2FVPROC cglProgramUniformMatrix3x2fv = NULL
cdef PFNGLVERTEXATTRIBL2DPROC cglVertexAttribL2d = NULL
cdef PFNGLPROGRAMUNIFORM2IPROC cglProgramUniform2i = NULL
cdef PFNGLPROGRAMUNIFORM1FVPROC cglProgramUniform1fv = NULL
cdef PFNGLPROGRAMUNIFORM1FPROC cglProgramUniform1f = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX4X3DVPROC cglProgramUniformMatrix4x3dv = NULL
cdef PFNGLVERTEXATTRIBL1DVPROC cglVertexAttribL1dv = NULL
cdef PFNGLPROGRAMUNIFORM1UIPROC cglProgramUniform1ui = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX2X4FVPROC cglProgramUniformMatrix2x4fv = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX2FVPROC cglProgramUniformMatrix2fv = NULL
cdef PFNGLDEPTHRANGEINDEXEDPROC cglDepthRangeIndexed = NULL
cdef PFNGLVERTEXATTRIBLPOINTERPROC cglVertexAttribLPointer = NULL
cdef PFNGLVERTEXATTRIBL4DVPROC cglVertexAttribL4dv = NULL
cdef PFNGLGETPROGRAMPIPELINEIVPROC cglGetProgramPipelineiv = NULL
cdef PFNGLPROGRAMUNIFORM2UIPROC cglProgramUniform2ui = NULL
cdef PFNGLPROGRAMUNIFORM3FPROC cglProgramUniform3f = NULL
cdef PFNGLCREATESHADERPROGRAMVPROC cglCreateShaderProgramv = NULL
cdef PFNGLGETSHADERPRECISIONFORMATPROC cglGetShaderPrecisionFormat = NULL
cdef PFNGLVIEWPORTINDEXEDFVPROC cglViewportIndexedfv = NULL
cdef PFNGLPROGRAMUNIFORM3IVPROC cglProgramUniform3iv = NULL
cdef PFNGLPROGRAMUNIFORM2IVPROC cglProgramUniform2iv = NULL
cdef PFNGLVALIDATEPROGRAMPIPELINEPROC cglValidateProgramPipeline = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX2X4DVPROC cglProgramUniformMatrix2x4dv = NULL
cdef PFNGLVERTEXATTRIBL1DPROC cglVertexAttribL1d = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX3FVPROC cglProgramUniformMatrix3fv = NULL
cdef PFNGLVERTEXATTRIBL4DPROC cglVertexAttribL4d = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX4DVPROC cglProgramUniformMatrix4dv = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX3X4DVPROC cglProgramUniformMatrix3x4dv = NULL
cdef PFNGLDEPTHRANGEARRAYVPROC cglDepthRangeArrayv = NULL
cdef PFNGLPROGRAMUNIFORM4UIPROC cglProgramUniform4ui = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX4X2FVPROC cglProgramUniformMatrix4x2fv = NULL
cdef PFNGLPROGRAMUNIFORM4IPROC cglProgramUniform4i = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX2DVPROC cglProgramUniformMatrix2dv = NULL
cdef PFNGLVIEWPORTINDEXEDFPROC cglViewportIndexedf = NULL
cdef PFNGLVERTEXATTRIBL2DVPROC cglVertexAttribL2dv = NULL
cdef PFNGLRELEASESHADERCOMPILERPROC cglReleaseShaderCompiler = NULL
cdef PFNGLDEPTHRANGEFPROC cglDepthRangef = NULL
cdef PFNGLPROGRAMUNIFORM4UIVPROC cglProgramUniform4uiv = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX2X3FVPROC cglProgramUniformMatrix2x3fv = NULL
cdef PFNGLPROGRAMUNIFORM4IVPROC cglProgramUniform4iv = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX3DVPROC cglProgramUniformMatrix3dv = NULL
cdef PFNGLPROGRAMUNIFORM1IVPROC cglProgramUniform1iv = NULL
cdef PFNGLPROGRAMPARAMETERIPROC cglProgramParameteri = NULL
cdef PFNGLPROGRAMUNIFORM2FPROC cglProgramUniform2f = NULL
cdef PFNGLVIEWPORTARRAYVPROC cglViewportArrayv = NULL
cdef PFNGLPROGRAMUNIFORM3FVPROC cglProgramUniform3fv = NULL
cdef PFNGLCLEARDEPTHFPROC cglClearDepthf = NULL
cdef PFNGLPROGRAMUNIFORM4DVPROC cglProgramUniform4dv = NULL
cdef PFNGLPROGRAMUNIFORM4FPROC cglProgramUniform4f = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX4FVPROC cglProgramUniformMatrix4fv = NULL
cdef PFNGLPROGRAMUNIFORM2UIVPROC cglProgramUniform2uiv = NULL
cdef PFNGLVERTEXATTRIBL3DPROC cglVertexAttribL3d = NULL
cdef PFNGLGETVERTEXATTRIBLDVPROC cglGetVertexAttribLdv = NULL
cdef PFNGLSCISSORARRAYVPROC cglScissorArrayv = NULL
cdef PFNGLSCISSORINDEXEDVPROC cglScissorIndexedv = NULL
cdef PFNGLPROGRAMUNIFORM1IPROC cglProgramUniform1i = NULL
cdef PFNGLGETFLOATI_VPROC cglGetFloati_v = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX4X3FVPROC cglProgramUniformMatrix4x3fv = NULL
cdef PFNGLSCISSORINDEXEDPROC cglScissorIndexed = NULL
cdef PFNGLPROGRAMUNIFORM2DPROC cglProgramUniform2d = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX4X2DVPROC cglProgramUniformMatrix4x2dv = NULL
cdef PFNGLPROGRAMUNIFORM3DVPROC cglProgramUniform3dv = NULL
cdef PFNGLPROGRAMUNIFORM3UIPROC cglProgramUniform3ui = NULL
cdef PFNGLBINDPROGRAMPIPELINEPROC cglBindProgramPipeline = NULL
cdef PFNGLGETDOUBLEI_VPROC cglGetDoublei_v = NULL
cdef PFNGLVERTEXATTRIBL3DVPROC cglVertexAttribL3dv = NULL
cdef PFNGLPROGRAMUNIFORM1DVPROC cglProgramUniform1dv = NULL
cdef PFNGLUSEPROGRAMSTAGESPROC cglUseProgramStages = NULL
cdef PFNGLPROGRAMUNIFORM1UIVPROC cglProgramUniform1uiv = NULL
cdef PFNGLGENPROGRAMPIPELINESPROC cglGenProgramPipelines = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX3X4FVPROC cglProgramUniformMatrix3x4fv = NULL
cdef PFNGLPROGRAMUNIFORM1DPROC cglProgramUniform1d = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX3X2DVPROC cglProgramUniformMatrix3x2dv = NULL
cdef PFNGLDELETEPROGRAMPIPELINESPROC cglDeleteProgramPipelines = NULL
cdef PFNGLACTIVESHADERPROGRAMPROC cglActiveShaderProgram = NULL
cdef PFNGLGETPROGRAMPIPELINEINFOLOGPROC cglGetProgramPipelineInfoLog = NULL
cdef PFNGLPROGRAMUNIFORM2FVPROC cglProgramUniform2fv = NULL
cdef PFNGLPROGRAMUNIFORM3IPROC cglProgramUniform3i = NULL
cdef PFNGLPROGRAMUNIFORM3DPROC cglProgramUniform3d = NULL
cdef PFNGLPROGRAMUNIFORM4FVPROC cglProgramUniform4fv = NULL
cdef PFNGLPROGRAMUNIFORMMATRIX2X3DVPROC cglProgramUniformMatrix2x3dv = NULL
cdef PFNGLPROGRAMUNIFORM4DPROC cglProgramUniform4d = NULL
cdef PFNGLPROGRAMUNIFORM3UIVPROC cglProgramUniform3uiv = NULL
cdef PFNGLPROGRAMUNIFORM2DVPROC cglProgramUniform2dv = NULL


cdef void GetglShaderBinary(GLsizei count, const GLuint *shaders, GLenum binaryFormat, const void *binary, GLsizei length):
    global cglShaderBinary
    cglShaderBinary = <PFNGLSHADERBINARYPROC>getFunction(b"glShaderBinary")
    cglShaderBinary(count, shaders, binaryFormat, binary, length)

cdef void GetglProgramBinary(GLuint program, GLenum binaryFormat, const void *binary, GLsizei length):
    global cglProgramBinary
    cglProgramBinary = <PFNGLPROGRAMBINARYPROC>getFunction(b"glProgramBinary")
    cglProgramBinary(program, binaryFormat, binary, length)

cdef void GetglGetProgramBinary(GLuint program, GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, void *binary):
    global cglGetProgramBinary
    cglGetProgramBinary = <PFNGLGETPROGRAMBINARYPROC>getFunction(b"glGetProgramBinary")
    cglGetProgramBinary(program, bufSize, length, binaryFormat, binary)

cdef GLboolean GetglIsProgramPipeline(GLuint pipeline):
    global cglIsProgramPipeline
    cglIsProgramPipeline = <PFNGLISPROGRAMPIPELINEPROC>getFunction(b"glIsProgramPipeline")
    cglIsProgramPipeline(pipeline)

cdef void GetglProgramUniformMatrix3x2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix3x2fv
    cglProgramUniformMatrix3x2fv = <PFNGLPROGRAMUNIFORMMATRIX3X2FVPROC>getFunction(b"glProgramUniformMatrix3x2fv")
    cglProgramUniformMatrix3x2fv(program, location, count, transpose, value)

cdef void GetglVertexAttribL2d(GLuint index, GLdouble x, GLdouble y):
    global cglVertexAttribL2d
    cglVertexAttribL2d = <PFNGLVERTEXATTRIBL2DPROC>getFunction(b"glVertexAttribL2d")
    cglVertexAttribL2d(index, x, y)

cdef void GetglProgramUniform2i(GLuint program, GLint location, GLint v0, GLint v1):
    global cglProgramUniform2i
    cglProgramUniform2i = <PFNGLPROGRAMUNIFORM2IPROC>getFunction(b"glProgramUniform2i")
    cglProgramUniform2i(program, location, v0, v1)

cdef void GetglProgramUniform1fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    global cglProgramUniform1fv
    cglProgramUniform1fv = <PFNGLPROGRAMUNIFORM1FVPROC>getFunction(b"glProgramUniform1fv")
    cglProgramUniform1fv(program, location, count, value)

cdef void GetglProgramUniform1f(GLuint program, GLint location, GLfloat v0):
    global cglProgramUniform1f
    cglProgramUniform1f = <PFNGLPROGRAMUNIFORM1FPROC>getFunction(b"glProgramUniform1f")
    cglProgramUniform1f(program, location, v0)

cdef void GetglProgramUniformMatrix4x3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix4x3dv
    cglProgramUniformMatrix4x3dv = <PFNGLPROGRAMUNIFORMMATRIX4X3DVPROC>getFunction(b"glProgramUniformMatrix4x3dv")
    cglProgramUniformMatrix4x3dv(program, location, count, transpose, value)

cdef void GetglVertexAttribL1dv(GLuint index, const GLdouble *v):
    global cglVertexAttribL1dv
    cglVertexAttribL1dv = <PFNGLVERTEXATTRIBL1DVPROC>getFunction(b"glVertexAttribL1dv")
    cglVertexAttribL1dv(index, v)

cdef void GetglProgramUniform1ui(GLuint program, GLint location, GLuint v0):
    global cglProgramUniform1ui
    cglProgramUniform1ui = <PFNGLPROGRAMUNIFORM1UIPROC>getFunction(b"glProgramUniform1ui")
    cglProgramUniform1ui(program, location, v0)

cdef void GetglProgramUniformMatrix2x4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix2x4fv
    cglProgramUniformMatrix2x4fv = <PFNGLPROGRAMUNIFORMMATRIX2X4FVPROC>getFunction(b"glProgramUniformMatrix2x4fv")
    cglProgramUniformMatrix2x4fv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix2fv
    cglProgramUniformMatrix2fv = <PFNGLPROGRAMUNIFORMMATRIX2FVPROC>getFunction(b"glProgramUniformMatrix2fv")
    cglProgramUniformMatrix2fv(program, location, count, transpose, value)

cdef void GetglDepthRangeIndexed(GLuint index, GLdouble n, GLdouble f):
    global cglDepthRangeIndexed
    cglDepthRangeIndexed = <PFNGLDEPTHRANGEINDEXEDPROC>getFunction(b"glDepthRangeIndexed")
    cglDepthRangeIndexed(index, n, f)

cdef void GetglVertexAttribLPointer(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglVertexAttribLPointer
    cglVertexAttribLPointer = <PFNGLVERTEXATTRIBLPOINTERPROC>getFunction(b"glVertexAttribLPointer")
    cglVertexAttribLPointer(index, size, type, stride, pointer)

cdef void GetglVertexAttribL4dv(GLuint index, const GLdouble *v):
    global cglVertexAttribL4dv
    cglVertexAttribL4dv = <PFNGLVERTEXATTRIBL4DVPROC>getFunction(b"glVertexAttribL4dv")
    cglVertexAttribL4dv(index, v)

cdef void GetglGetProgramPipelineiv(GLuint pipeline, GLenum pname, GLint *params):
    global cglGetProgramPipelineiv
    cglGetProgramPipelineiv = <PFNGLGETPROGRAMPIPELINEIVPROC>getFunction(b"glGetProgramPipelineiv")
    cglGetProgramPipelineiv(pipeline, pname, params)

cdef void GetglProgramUniform2ui(GLuint program, GLint location, GLuint v0, GLuint v1):
    global cglProgramUniform2ui
    cglProgramUniform2ui = <PFNGLPROGRAMUNIFORM2UIPROC>getFunction(b"glProgramUniform2ui")
    cglProgramUniform2ui(program, location, v0, v1)

cdef void GetglProgramUniform3f(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2):
    global cglProgramUniform3f
    cglProgramUniform3f = <PFNGLPROGRAMUNIFORM3FPROC>getFunction(b"glProgramUniform3f")
    cglProgramUniform3f(program, location, v0, v1, v2)

cdef GLuint GetglCreateShaderProgramv(GLenum type, GLsizei count, const GLchar **strings):
    global cglCreateShaderProgramv
    cglCreateShaderProgramv = <PFNGLCREATESHADERPROGRAMVPROC>getFunction(b"glCreateShaderProgramv")
    cglCreateShaderProgramv(type, count, strings)

cdef void GetglGetShaderPrecisionFormat(GLenum shadertype, GLenum precisiontype, GLint *range, GLint *precision):
    global cglGetShaderPrecisionFormat
    cglGetShaderPrecisionFormat = <PFNGLGETSHADERPRECISIONFORMATPROC>getFunction(b"glGetShaderPrecisionFormat")
    cglGetShaderPrecisionFormat(shadertype, precisiontype, range, precision)

cdef void GetglViewportIndexedfv(GLuint index, const GLfloat *v):
    global cglViewportIndexedfv
    cglViewportIndexedfv = <PFNGLVIEWPORTINDEXEDFVPROC>getFunction(b"glViewportIndexedfv")
    cglViewportIndexedfv(index, v)

cdef void GetglProgramUniform3iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    global cglProgramUniform3iv
    cglProgramUniform3iv = <PFNGLPROGRAMUNIFORM3IVPROC>getFunction(b"glProgramUniform3iv")
    cglProgramUniform3iv(program, location, count, value)

cdef void GetglProgramUniform2iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    global cglProgramUniform2iv
    cglProgramUniform2iv = <PFNGLPROGRAMUNIFORM2IVPROC>getFunction(b"glProgramUniform2iv")
    cglProgramUniform2iv(program, location, count, value)

cdef void GetglValidateProgramPipeline(GLuint pipeline):
    global cglValidateProgramPipeline
    cglValidateProgramPipeline = <PFNGLVALIDATEPROGRAMPIPELINEPROC>getFunction(b"glValidateProgramPipeline")
    cglValidateProgramPipeline(pipeline)

cdef void GetglProgramUniformMatrix2x4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix2x4dv
    cglProgramUniformMatrix2x4dv = <PFNGLPROGRAMUNIFORMMATRIX2X4DVPROC>getFunction(b"glProgramUniformMatrix2x4dv")
    cglProgramUniformMatrix2x4dv(program, location, count, transpose, value)

cdef void GetglVertexAttribL1d(GLuint index, GLdouble x):
    global cglVertexAttribL1d
    cglVertexAttribL1d = <PFNGLVERTEXATTRIBL1DPROC>getFunction(b"glVertexAttribL1d")
    cglVertexAttribL1d(index, x)

cdef void GetglProgramUniformMatrix3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix3fv
    cglProgramUniformMatrix3fv = <PFNGLPROGRAMUNIFORMMATRIX3FVPROC>getFunction(b"glProgramUniformMatrix3fv")
    cglProgramUniformMatrix3fv(program, location, count, transpose, value)

cdef void GetglVertexAttribL4d(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglVertexAttribL4d
    cglVertexAttribL4d = <PFNGLVERTEXATTRIBL4DPROC>getFunction(b"glVertexAttribL4d")
    cglVertexAttribL4d(index, x, y, z, w)

cdef void GetglProgramUniformMatrix4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix4dv
    cglProgramUniformMatrix4dv = <PFNGLPROGRAMUNIFORMMATRIX4DVPROC>getFunction(b"glProgramUniformMatrix4dv")
    cglProgramUniformMatrix4dv(program, location, count, transpose, value)

cdef void GetglProgramUniformMatrix3x4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix3x4dv
    cglProgramUniformMatrix3x4dv = <PFNGLPROGRAMUNIFORMMATRIX3X4DVPROC>getFunction(b"glProgramUniformMatrix3x4dv")
    cglProgramUniformMatrix3x4dv(program, location, count, transpose, value)

cdef void GetglDepthRangeArrayv(GLuint first, GLsizei count, const GLdouble *v):
    global cglDepthRangeArrayv
    cglDepthRangeArrayv = <PFNGLDEPTHRANGEARRAYVPROC>getFunction(b"glDepthRangeArrayv")
    cglDepthRangeArrayv(first, count, v)

cdef void GetglProgramUniform4ui(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3):
    global cglProgramUniform4ui
    cglProgramUniform4ui = <PFNGLPROGRAMUNIFORM4UIPROC>getFunction(b"glProgramUniform4ui")
    cglProgramUniform4ui(program, location, v0, v1, v2, v3)

cdef void GetglProgramUniformMatrix4x2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix4x2fv
    cglProgramUniformMatrix4x2fv = <PFNGLPROGRAMUNIFORMMATRIX4X2FVPROC>getFunction(b"glProgramUniformMatrix4x2fv")
    cglProgramUniformMatrix4x2fv(program, location, count, transpose, value)

cdef void GetglProgramUniform4i(GLuint program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3):
    global cglProgramUniform4i
    cglProgramUniform4i = <PFNGLPROGRAMUNIFORM4IPROC>getFunction(b"glProgramUniform4i")
    cglProgramUniform4i(program, location, v0, v1, v2, v3)

cdef void GetglProgramUniformMatrix2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix2dv
    cglProgramUniformMatrix2dv = <PFNGLPROGRAMUNIFORMMATRIX2DVPROC>getFunction(b"glProgramUniformMatrix2dv")
    cglProgramUniformMatrix2dv(program, location, count, transpose, value)

cdef void GetglViewportIndexedf(GLuint index, GLfloat x, GLfloat y, GLfloat w, GLfloat h):
    global cglViewportIndexedf
    cglViewportIndexedf = <PFNGLVIEWPORTINDEXEDFPROC>getFunction(b"glViewportIndexedf")
    cglViewportIndexedf(index, x, y, w, h)

cdef void GetglVertexAttribL2dv(GLuint index, const GLdouble *v):
    global cglVertexAttribL2dv
    cglVertexAttribL2dv = <PFNGLVERTEXATTRIBL2DVPROC>getFunction(b"glVertexAttribL2dv")
    cglVertexAttribL2dv(index, v)

cdef void GetglReleaseShaderCompiler():
    global cglReleaseShaderCompiler
    cglReleaseShaderCompiler = <PFNGLRELEASESHADERCOMPILERPROC>getFunction(b"glReleaseShaderCompiler")
    cglReleaseShaderCompiler()

cdef void GetglDepthRangef(GLfloat n, GLfloat f):
    global cglDepthRangef
    cglDepthRangef = <PFNGLDEPTHRANGEFPROC>getFunction(b"glDepthRangef")
    cglDepthRangef(n, f)

cdef void GetglProgramUniform4uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    global cglProgramUniform4uiv
    cglProgramUniform4uiv = <PFNGLPROGRAMUNIFORM4UIVPROC>getFunction(b"glProgramUniform4uiv")
    cglProgramUniform4uiv(program, location, count, value)

cdef void GetglProgramUniformMatrix2x3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix2x3fv
    cglProgramUniformMatrix2x3fv = <PFNGLPROGRAMUNIFORMMATRIX2X3FVPROC>getFunction(b"glProgramUniformMatrix2x3fv")
    cglProgramUniformMatrix2x3fv(program, location, count, transpose, value)

cdef void GetglProgramUniform4iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    global cglProgramUniform4iv
    cglProgramUniform4iv = <PFNGLPROGRAMUNIFORM4IVPROC>getFunction(b"glProgramUniform4iv")
    cglProgramUniform4iv(program, location, count, value)

cdef void GetglProgramUniformMatrix3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix3dv
    cglProgramUniformMatrix3dv = <PFNGLPROGRAMUNIFORMMATRIX3DVPROC>getFunction(b"glProgramUniformMatrix3dv")
    cglProgramUniformMatrix3dv(program, location, count, transpose, value)

cdef void GetglProgramUniform1iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    global cglProgramUniform1iv
    cglProgramUniform1iv = <PFNGLPROGRAMUNIFORM1IVPROC>getFunction(b"glProgramUniform1iv")
    cglProgramUniform1iv(program, location, count, value)

cdef void GetglProgramParameteri(GLuint program, GLenum pname, GLint value):
    global cglProgramParameteri
    cglProgramParameteri = <PFNGLPROGRAMPARAMETERIPROC>getFunction(b"glProgramParameteri")
    cglProgramParameteri(program, pname, value)

cdef void GetglProgramUniform2f(GLuint program, GLint location, GLfloat v0, GLfloat v1):
    global cglProgramUniform2f
    cglProgramUniform2f = <PFNGLPROGRAMUNIFORM2FPROC>getFunction(b"glProgramUniform2f")
    cglProgramUniform2f(program, location, v0, v1)

cdef void GetglViewportArrayv(GLuint first, GLsizei count, const GLfloat *v):
    global cglViewportArrayv
    cglViewportArrayv = <PFNGLVIEWPORTARRAYVPROC>getFunction(b"glViewportArrayv")
    cglViewportArrayv(first, count, v)

cdef void GetglProgramUniform3fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    global cglProgramUniform3fv
    cglProgramUniform3fv = <PFNGLPROGRAMUNIFORM3FVPROC>getFunction(b"glProgramUniform3fv")
    cglProgramUniform3fv(program, location, count, value)

cdef void GetglClearDepthf(GLfloat d):
    global cglClearDepthf
    cglClearDepthf = <PFNGLCLEARDEPTHFPROC>getFunction(b"glClearDepthf")
    cglClearDepthf(d)

cdef void GetglProgramUniform4dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    global cglProgramUniform4dv
    cglProgramUniform4dv = <PFNGLPROGRAMUNIFORM4DVPROC>getFunction(b"glProgramUniform4dv")
    cglProgramUniform4dv(program, location, count, value)

cdef void GetglProgramUniform4f(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3):
    global cglProgramUniform4f
    cglProgramUniform4f = <PFNGLPROGRAMUNIFORM4FPROC>getFunction(b"glProgramUniform4f")
    cglProgramUniform4f(program, location, v0, v1, v2, v3)

cdef void GetglProgramUniformMatrix4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix4fv
    cglProgramUniformMatrix4fv = <PFNGLPROGRAMUNIFORMMATRIX4FVPROC>getFunction(b"glProgramUniformMatrix4fv")
    cglProgramUniformMatrix4fv(program, location, count, transpose, value)

cdef void GetglProgramUniform2uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    global cglProgramUniform2uiv
    cglProgramUniform2uiv = <PFNGLPROGRAMUNIFORM2UIVPROC>getFunction(b"glProgramUniform2uiv")
    cglProgramUniform2uiv(program, location, count, value)

cdef void GetglVertexAttribL3d(GLuint index, GLdouble x, GLdouble y, GLdouble z):
    global cglVertexAttribL3d
    cglVertexAttribL3d = <PFNGLVERTEXATTRIBL3DPROC>getFunction(b"glVertexAttribL3d")
    cglVertexAttribL3d(index, x, y, z)

cdef void GetglGetVertexAttribLdv(GLuint index, GLenum pname, GLdouble *params):
    global cglGetVertexAttribLdv
    cglGetVertexAttribLdv = <PFNGLGETVERTEXATTRIBLDVPROC>getFunction(b"glGetVertexAttribLdv")
    cglGetVertexAttribLdv(index, pname, params)

cdef void GetglScissorArrayv(GLuint first, GLsizei count, const GLint *v):
    global cglScissorArrayv
    cglScissorArrayv = <PFNGLSCISSORARRAYVPROC>getFunction(b"glScissorArrayv")
    cglScissorArrayv(first, count, v)

cdef void GetglScissorIndexedv(GLuint index, const GLint *v):
    global cglScissorIndexedv
    cglScissorIndexedv = <PFNGLSCISSORINDEXEDVPROC>getFunction(b"glScissorIndexedv")
    cglScissorIndexedv(index, v)

cdef void GetglProgramUniform1i(GLuint program, GLint location, GLint v0):
    global cglProgramUniform1i
    cglProgramUniform1i = <PFNGLPROGRAMUNIFORM1IPROC>getFunction(b"glProgramUniform1i")
    cglProgramUniform1i(program, location, v0)

cdef void GetglGetFloati_v(GLenum target, GLuint index, GLfloat *data):
    global cglGetFloati_v
    cglGetFloati_v = <PFNGLGETFLOATI_VPROC>getFunction(b"glGetFloati_v")
    cglGetFloati_v(target, index, data)

cdef void GetglProgramUniformMatrix4x3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix4x3fv
    cglProgramUniformMatrix4x3fv = <PFNGLPROGRAMUNIFORMMATRIX4X3FVPROC>getFunction(b"glProgramUniformMatrix4x3fv")
    cglProgramUniformMatrix4x3fv(program, location, count, transpose, value)

cdef void GetglScissorIndexed(GLuint index, GLint left, GLint bottom, GLsizei width, GLsizei height):
    global cglScissorIndexed
    cglScissorIndexed = <PFNGLSCISSORINDEXEDPROC>getFunction(b"glScissorIndexed")
    cglScissorIndexed(index, left, bottom, width, height)

cdef void GetglProgramUniform2d(GLuint program, GLint location, GLdouble v0, GLdouble v1):
    global cglProgramUniform2d
    cglProgramUniform2d = <PFNGLPROGRAMUNIFORM2DPROC>getFunction(b"glProgramUniform2d")
    cglProgramUniform2d(program, location, v0, v1)

cdef void GetglProgramUniformMatrix4x2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix4x2dv
    cglProgramUniformMatrix4x2dv = <PFNGLPROGRAMUNIFORMMATRIX4X2DVPROC>getFunction(b"glProgramUniformMatrix4x2dv")
    cglProgramUniformMatrix4x2dv(program, location, count, transpose, value)

cdef void GetglProgramUniform3dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    global cglProgramUniform3dv
    cglProgramUniform3dv = <PFNGLPROGRAMUNIFORM3DVPROC>getFunction(b"glProgramUniform3dv")
    cglProgramUniform3dv(program, location, count, value)

cdef void GetglProgramUniform3ui(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2):
    global cglProgramUniform3ui
    cglProgramUniform3ui = <PFNGLPROGRAMUNIFORM3UIPROC>getFunction(b"glProgramUniform3ui")
    cglProgramUniform3ui(program, location, v0, v1, v2)

cdef void GetglBindProgramPipeline(GLuint pipeline):
    global cglBindProgramPipeline
    cglBindProgramPipeline = <PFNGLBINDPROGRAMPIPELINEPROC>getFunction(b"glBindProgramPipeline")
    cglBindProgramPipeline(pipeline)

cdef void GetglGetDoublei_v(GLenum target, GLuint index, GLdouble *data):
    global cglGetDoublei_v
    cglGetDoublei_v = <PFNGLGETDOUBLEI_VPROC>getFunction(b"glGetDoublei_v")
    cglGetDoublei_v(target, index, data)

cdef void GetglVertexAttribL3dv(GLuint index, const GLdouble *v):
    global cglVertexAttribL3dv
    cglVertexAttribL3dv = <PFNGLVERTEXATTRIBL3DVPROC>getFunction(b"glVertexAttribL3dv")
    cglVertexAttribL3dv(index, v)

cdef void GetglProgramUniform1dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    global cglProgramUniform1dv
    cglProgramUniform1dv = <PFNGLPROGRAMUNIFORM1DVPROC>getFunction(b"glProgramUniform1dv")
    cglProgramUniform1dv(program, location, count, value)

cdef void GetglUseProgramStages(GLuint pipeline, GLbitfield stages, GLuint program):
    global cglUseProgramStages
    cglUseProgramStages = <PFNGLUSEPROGRAMSTAGESPROC>getFunction(b"glUseProgramStages")
    cglUseProgramStages(pipeline, stages, program)

cdef void GetglProgramUniform1uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    global cglProgramUniform1uiv
    cglProgramUniform1uiv = <PFNGLPROGRAMUNIFORM1UIVPROC>getFunction(b"glProgramUniform1uiv")
    cglProgramUniform1uiv(program, location, count, value)

cdef void GetglGenProgramPipelines(GLsizei n, GLuint *pipelines):
    global cglGenProgramPipelines
    cglGenProgramPipelines = <PFNGLGENPROGRAMPIPELINESPROC>getFunction(b"glGenProgramPipelines")
    cglGenProgramPipelines(n, pipelines)

cdef void GetglProgramUniformMatrix3x4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglProgramUniformMatrix3x4fv
    cglProgramUniformMatrix3x4fv = <PFNGLPROGRAMUNIFORMMATRIX3X4FVPROC>getFunction(b"glProgramUniformMatrix3x4fv")
    cglProgramUniformMatrix3x4fv(program, location, count, transpose, value)

cdef void GetglProgramUniform1d(GLuint program, GLint location, GLdouble v0):
    global cglProgramUniform1d
    cglProgramUniform1d = <PFNGLPROGRAMUNIFORM1DPROC>getFunction(b"glProgramUniform1d")
    cglProgramUniform1d(program, location, v0)

cdef void GetglProgramUniformMatrix3x2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix3x2dv
    cglProgramUniformMatrix3x2dv = <PFNGLPROGRAMUNIFORMMATRIX3X2DVPROC>getFunction(b"glProgramUniformMatrix3x2dv")
    cglProgramUniformMatrix3x2dv(program, location, count, transpose, value)

cdef void GetglDeleteProgramPipelines(GLsizei n, const GLuint *pipelines):
    global cglDeleteProgramPipelines
    cglDeleteProgramPipelines = <PFNGLDELETEPROGRAMPIPELINESPROC>getFunction(b"glDeleteProgramPipelines")
    cglDeleteProgramPipelines(n, pipelines)

cdef void GetglActiveShaderProgram(GLuint pipeline, GLuint program):
    global cglActiveShaderProgram
    cglActiveShaderProgram = <PFNGLACTIVESHADERPROGRAMPROC>getFunction(b"glActiveShaderProgram")
    cglActiveShaderProgram(pipeline, program)

cdef void GetglGetProgramPipelineInfoLog(GLuint pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    global cglGetProgramPipelineInfoLog
    cglGetProgramPipelineInfoLog = <PFNGLGETPROGRAMPIPELINEINFOLOGPROC>getFunction(b"glGetProgramPipelineInfoLog")
    cglGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog)

cdef void GetglProgramUniform2fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    global cglProgramUniform2fv
    cglProgramUniform2fv = <PFNGLPROGRAMUNIFORM2FVPROC>getFunction(b"glProgramUniform2fv")
    cglProgramUniform2fv(program, location, count, value)

cdef void GetglProgramUniform3i(GLuint program, GLint location, GLint v0, GLint v1, GLint v2):
    global cglProgramUniform3i
    cglProgramUniform3i = <PFNGLPROGRAMUNIFORM3IPROC>getFunction(b"glProgramUniform3i")
    cglProgramUniform3i(program, location, v0, v1, v2)

cdef void GetglProgramUniform3d(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2):
    global cglProgramUniform3d
    cglProgramUniform3d = <PFNGLPROGRAMUNIFORM3DPROC>getFunction(b"glProgramUniform3d")
    cglProgramUniform3d(program, location, v0, v1, v2)

cdef void GetglProgramUniform4fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    global cglProgramUniform4fv
    cglProgramUniform4fv = <PFNGLPROGRAMUNIFORM4FVPROC>getFunction(b"glProgramUniform4fv")
    cglProgramUniform4fv(program, location, count, value)

cdef void GetglProgramUniformMatrix2x3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglProgramUniformMatrix2x3dv
    cglProgramUniformMatrix2x3dv = <PFNGLPROGRAMUNIFORMMATRIX2X3DVPROC>getFunction(b"glProgramUniformMatrix2x3dv")
    cglProgramUniformMatrix2x3dv(program, location, count, transpose, value)

cdef void GetglProgramUniform4d(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3):
    global cglProgramUniform4d
    cglProgramUniform4d = <PFNGLPROGRAMUNIFORM4DPROC>getFunction(b"glProgramUniform4d")
    cglProgramUniform4d(program, location, v0, v1, v2, v3)

cdef void GetglProgramUniform3uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    global cglProgramUniform3uiv
    cglProgramUniform3uiv = <PFNGLPROGRAMUNIFORM3UIVPROC>getFunction(b"glProgramUniform3uiv")
    cglProgramUniform3uiv(program, location, count, value)

cdef void GetglProgramUniform2dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    global cglProgramUniform2dv
    cglProgramUniform2dv = <PFNGLPROGRAMUNIFORM2DVPROC>getFunction(b"glProgramUniform2dv")
    cglProgramUniform2dv(program, location, count, value)

cglShaderBinary = GetglShaderBinary
cglProgramBinary = GetglProgramBinary
cglGetProgramBinary = GetglGetProgramBinary
cglIsProgramPipeline = GetglIsProgramPipeline
cglProgramUniformMatrix3x2fv = GetglProgramUniformMatrix3x2fv
cglVertexAttribL2d = GetglVertexAttribL2d
cglProgramUniform2i = GetglProgramUniform2i
cglProgramUniform1fv = GetglProgramUniform1fv
cglProgramUniform1f = GetglProgramUniform1f
cglProgramUniformMatrix4x3dv = GetglProgramUniformMatrix4x3dv
cglVertexAttribL1dv = GetglVertexAttribL1dv
cglProgramUniform1ui = GetglProgramUniform1ui
cglProgramUniformMatrix2x4fv = GetglProgramUniformMatrix2x4fv
cglProgramUniformMatrix2fv = GetglProgramUniformMatrix2fv
cglDepthRangeIndexed = GetglDepthRangeIndexed
cglVertexAttribLPointer = GetglVertexAttribLPointer
cglVertexAttribL4dv = GetglVertexAttribL4dv
cglGetProgramPipelineiv = GetglGetProgramPipelineiv
cglProgramUniform2ui = GetglProgramUniform2ui
cglProgramUniform3f = GetglProgramUniform3f
cglCreateShaderProgramv = GetglCreateShaderProgramv
cglGetShaderPrecisionFormat = GetglGetShaderPrecisionFormat
cglViewportIndexedfv = GetglViewportIndexedfv
cglProgramUniform3iv = GetglProgramUniform3iv
cglProgramUniform2iv = GetglProgramUniform2iv
cglValidateProgramPipeline = GetglValidateProgramPipeline
cglProgramUniformMatrix2x4dv = GetglProgramUniformMatrix2x4dv
cglVertexAttribL1d = GetglVertexAttribL1d
cglProgramUniformMatrix3fv = GetglProgramUniformMatrix3fv
cglVertexAttribL4d = GetglVertexAttribL4d
cglProgramUniformMatrix4dv = GetglProgramUniformMatrix4dv
cglProgramUniformMatrix3x4dv = GetglProgramUniformMatrix3x4dv
cglDepthRangeArrayv = GetglDepthRangeArrayv
cglProgramUniform4ui = GetglProgramUniform4ui
cglProgramUniformMatrix4x2fv = GetglProgramUniformMatrix4x2fv
cglProgramUniform4i = GetglProgramUniform4i
cglProgramUniformMatrix2dv = GetglProgramUniformMatrix2dv
cglViewportIndexedf = GetglViewportIndexedf
cglVertexAttribL2dv = GetglVertexAttribL2dv
cglReleaseShaderCompiler = GetglReleaseShaderCompiler
cglDepthRangef = GetglDepthRangef
cglProgramUniform4uiv = GetglProgramUniform4uiv
cglProgramUniformMatrix2x3fv = GetglProgramUniformMatrix2x3fv
cglProgramUniform4iv = GetglProgramUniform4iv
cglProgramUniformMatrix3dv = GetglProgramUniformMatrix3dv
cglProgramUniform1iv = GetglProgramUniform1iv
cglProgramParameteri = GetglProgramParameteri
cglProgramUniform2f = GetglProgramUniform2f
cglViewportArrayv = GetglViewportArrayv
cglProgramUniform3fv = GetglProgramUniform3fv
cglClearDepthf = GetglClearDepthf
cglProgramUniform4dv = GetglProgramUniform4dv
cglProgramUniform4f = GetglProgramUniform4f
cglProgramUniformMatrix4fv = GetglProgramUniformMatrix4fv
cglProgramUniform2uiv = GetglProgramUniform2uiv
cglVertexAttribL3d = GetglVertexAttribL3d
cglGetVertexAttribLdv = GetglGetVertexAttribLdv
cglScissorArrayv = GetglScissorArrayv
cglScissorIndexedv = GetglScissorIndexedv
cglProgramUniform1i = GetglProgramUniform1i
cglGetFloati_v = GetglGetFloati_v
cglProgramUniformMatrix4x3fv = GetglProgramUniformMatrix4x3fv
cglScissorIndexed = GetglScissorIndexed
cglProgramUniform2d = GetglProgramUniform2d
cglProgramUniformMatrix4x2dv = GetglProgramUniformMatrix4x2dv
cglProgramUniform3dv = GetglProgramUniform3dv
cglProgramUniform3ui = GetglProgramUniform3ui
cglBindProgramPipeline = GetglBindProgramPipeline
cglGetDoublei_v = GetglGetDoublei_v
cglVertexAttribL3dv = GetglVertexAttribL3dv
cglProgramUniform1dv = GetglProgramUniform1dv
cglUseProgramStages = GetglUseProgramStages
cglProgramUniform1uiv = GetglProgramUniform1uiv
cglGenProgramPipelines = GetglGenProgramPipelines
cglProgramUniformMatrix3x4fv = GetglProgramUniformMatrix3x4fv
cglProgramUniform1d = GetglProgramUniform1d
cglProgramUniformMatrix3x2dv = GetglProgramUniformMatrix3x2dv
cglDeleteProgramPipelines = GetglDeleteProgramPipelines
cglActiveShaderProgram = GetglActiveShaderProgram
cglGetProgramPipelineInfoLog = GetglGetProgramPipelineInfoLog
cglProgramUniform2fv = GetglProgramUniform2fv
cglProgramUniform3i = GetglProgramUniform3i
cglProgramUniform3d = GetglProgramUniform3d
cglProgramUniform4fv = GetglProgramUniform4fv
cglProgramUniformMatrix2x3dv = GetglProgramUniformMatrix2x3dv
cglProgramUniform4d = GetglProgramUniform4d
cglProgramUniform3uiv = GetglProgramUniform3uiv
cglProgramUniform2dv = GetglProgramUniform2dv


cdef void glShaderBinary(GLsizei count, const GLuint *shaders, GLenum binaryFormat, const void *binary, GLsizei length):
    cglShaderBinary(count, shaders, binaryFormat, binary, length)

cdef void glProgramBinary(GLuint program, GLenum binaryFormat, const void *binary, GLsizei length):
    cglProgramBinary(program, binaryFormat, binary, length)

cdef void glGetProgramBinary(GLuint program, GLsizei bufSize, GLsizei *length, GLenum *binaryFormat, void *binary):
    cglGetProgramBinary(program, bufSize, length, binaryFormat, binary)

cdef GLboolean glIsProgramPipeline(GLuint pipeline):
    cglIsProgramPipeline(pipeline)

cdef void glProgramUniformMatrix3x2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix3x2fv(program, location, count, transpose, value)

cdef void glVertexAttribL2d(GLuint index, GLdouble x, GLdouble y):
    cglVertexAttribL2d(index, x, y)

cdef void glProgramUniform2i(GLuint program, GLint location, GLint v0, GLint v1):
    cglProgramUniform2i(program, location, v0, v1)

cdef void glProgramUniform1fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    cglProgramUniform1fv(program, location, count, value)

cdef void glProgramUniform1f(GLuint program, GLint location, GLfloat v0):
    cglProgramUniform1f(program, location, v0)

cdef void glProgramUniformMatrix4x3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix4x3dv(program, location, count, transpose, value)

cdef void glVertexAttribL1dv(GLuint index, const GLdouble *v):
    cglVertexAttribL1dv(index, v)

cdef void glProgramUniform1ui(GLuint program, GLint location, GLuint v0):
    cglProgramUniform1ui(program, location, v0)

cdef void glProgramUniformMatrix2x4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix2x4fv(program, location, count, transpose, value)

cdef void glProgramUniformMatrix2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix2fv(program, location, count, transpose, value)

cdef void glDepthRangeIndexed(GLuint index, GLdouble n, GLdouble f):
    cglDepthRangeIndexed(index, n, f)

cdef void glVertexAttribLPointer(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglVertexAttribLPointer(index, size, type, stride, pointer)

cdef void glVertexAttribL4dv(GLuint index, const GLdouble *v):
    cglVertexAttribL4dv(index, v)

cdef void glGetProgramPipelineiv(GLuint pipeline, GLenum pname, GLint *params):
    cglGetProgramPipelineiv(pipeline, pname, params)

cdef void glProgramUniform2ui(GLuint program, GLint location, GLuint v0, GLuint v1):
    cglProgramUniform2ui(program, location, v0, v1)

cdef void glProgramUniform3f(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2):
    cglProgramUniform3f(program, location, v0, v1, v2)

cdef GLuint glCreateShaderProgramv(GLenum type, GLsizei count, const GLchar **strings):
    cglCreateShaderProgramv(type, count, strings)

cdef void glGetShaderPrecisionFormat(GLenum shadertype, GLenum precisiontype, GLint *range, GLint *precision):
    cglGetShaderPrecisionFormat(shadertype, precisiontype, range, precision)

cdef void glViewportIndexedfv(GLuint index, const GLfloat *v):
    cglViewportIndexedfv(index, v)

cdef void glProgramUniform3iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    cglProgramUniform3iv(program, location, count, value)

cdef void glProgramUniform2iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    cglProgramUniform2iv(program, location, count, value)

cdef void glValidateProgramPipeline(GLuint pipeline):
    cglValidateProgramPipeline(pipeline)

cdef void glProgramUniformMatrix2x4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix2x4dv(program, location, count, transpose, value)

cdef void glVertexAttribL1d(GLuint index, GLdouble x):
    cglVertexAttribL1d(index, x)

cdef void glProgramUniformMatrix3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix3fv(program, location, count, transpose, value)

cdef void glVertexAttribL4d(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglVertexAttribL4d(index, x, y, z, w)

cdef void glProgramUniformMatrix4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix4dv(program, location, count, transpose, value)

cdef void glProgramUniformMatrix3x4dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix3x4dv(program, location, count, transpose, value)

cdef void glDepthRangeArrayv(GLuint first, GLsizei count, const GLdouble *v):
    cglDepthRangeArrayv(first, count, v)

cdef void glProgramUniform4ui(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3):
    cglProgramUniform4ui(program, location, v0, v1, v2, v3)

cdef void glProgramUniformMatrix4x2fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix4x2fv(program, location, count, transpose, value)

cdef void glProgramUniform4i(GLuint program, GLint location, GLint v0, GLint v1, GLint v2, GLint v3):
    cglProgramUniform4i(program, location, v0, v1, v2, v3)

cdef void glProgramUniformMatrix2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix2dv(program, location, count, transpose, value)

cdef void glViewportIndexedf(GLuint index, GLfloat x, GLfloat y, GLfloat w, GLfloat h):
    cglViewportIndexedf(index, x, y, w, h)

cdef void glVertexAttribL2dv(GLuint index, const GLdouble *v):
    cglVertexAttribL2dv(index, v)

cdef void glReleaseShaderCompiler():
    cglReleaseShaderCompiler()

cdef void glDepthRangef(GLfloat n, GLfloat f):
    cglDepthRangef(n, f)

cdef void glProgramUniform4uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    cglProgramUniform4uiv(program, location, count, value)

cdef void glProgramUniformMatrix2x3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix2x3fv(program, location, count, transpose, value)

cdef void glProgramUniform4iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    cglProgramUniform4iv(program, location, count, value)

cdef void glProgramUniformMatrix3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix3dv(program, location, count, transpose, value)

cdef void glProgramUniform1iv(GLuint program, GLint location, GLsizei count, const GLint *value):
    cglProgramUniform1iv(program, location, count, value)

cdef void glProgramParameteri(GLuint program, GLenum pname, GLint value):
    cglProgramParameteri(program, pname, value)

cdef void glProgramUniform2f(GLuint program, GLint location, GLfloat v0, GLfloat v1):
    cglProgramUniform2f(program, location, v0, v1)

cdef void glViewportArrayv(GLuint first, GLsizei count, const GLfloat *v):
    cglViewportArrayv(first, count, v)

cdef void glProgramUniform3fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    cglProgramUniform3fv(program, location, count, value)

cdef void glClearDepthf(GLfloat d):
    cglClearDepthf(d)

cdef void glProgramUniform4dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    cglProgramUniform4dv(program, location, count, value)

cdef void glProgramUniform4f(GLuint program, GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3):
    cglProgramUniform4f(program, location, v0, v1, v2, v3)

cdef void glProgramUniformMatrix4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix4fv(program, location, count, transpose, value)

cdef void glProgramUniform2uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    cglProgramUniform2uiv(program, location, count, value)

cdef void glVertexAttribL3d(GLuint index, GLdouble x, GLdouble y, GLdouble z):
    cglVertexAttribL3d(index, x, y, z)

cdef void glGetVertexAttribLdv(GLuint index, GLenum pname, GLdouble *params):
    cglGetVertexAttribLdv(index, pname, params)

cdef void glScissorArrayv(GLuint first, GLsizei count, const GLint *v):
    cglScissorArrayv(first, count, v)

cdef void glScissorIndexedv(GLuint index, const GLint *v):
    cglScissorIndexedv(index, v)

cdef void glProgramUniform1i(GLuint program, GLint location, GLint v0):
    cglProgramUniform1i(program, location, v0)

cdef void glGetFloati_v(GLenum target, GLuint index, GLfloat *data):
    cglGetFloati_v(target, index, data)

cdef void glProgramUniformMatrix4x3fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix4x3fv(program, location, count, transpose, value)

cdef void glScissorIndexed(GLuint index, GLint left, GLint bottom, GLsizei width, GLsizei height):
    cglScissorIndexed(index, left, bottom, width, height)

cdef void glProgramUniform2d(GLuint program, GLint location, GLdouble v0, GLdouble v1):
    cglProgramUniform2d(program, location, v0, v1)

cdef void glProgramUniformMatrix4x2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix4x2dv(program, location, count, transpose, value)

cdef void glProgramUniform3dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    cglProgramUniform3dv(program, location, count, value)

cdef void glProgramUniform3ui(GLuint program, GLint location, GLuint v0, GLuint v1, GLuint v2):
    cglProgramUniform3ui(program, location, v0, v1, v2)

cdef void glBindProgramPipeline(GLuint pipeline):
    cglBindProgramPipeline(pipeline)

cdef void glGetDoublei_v(GLenum target, GLuint index, GLdouble *data):
    cglGetDoublei_v(target, index, data)

cdef void glVertexAttribL3dv(GLuint index, const GLdouble *v):
    cglVertexAttribL3dv(index, v)

cdef void glProgramUniform1dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    cglProgramUniform1dv(program, location, count, value)

cdef void glUseProgramStages(GLuint pipeline, GLbitfield stages, GLuint program):
    cglUseProgramStages(pipeline, stages, program)

cdef void glProgramUniform1uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    cglProgramUniform1uiv(program, location, count, value)

cdef void glGenProgramPipelines(GLsizei n, GLuint *pipelines):
    cglGenProgramPipelines(n, pipelines)

cdef void glProgramUniformMatrix3x4fv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglProgramUniformMatrix3x4fv(program, location, count, transpose, value)

cdef void glProgramUniform1d(GLuint program, GLint location, GLdouble v0):
    cglProgramUniform1d(program, location, v0)

cdef void glProgramUniformMatrix3x2dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix3x2dv(program, location, count, transpose, value)

cdef void glDeleteProgramPipelines(GLsizei n, const GLuint *pipelines):
    cglDeleteProgramPipelines(n, pipelines)

cdef void glActiveShaderProgram(GLuint pipeline, GLuint program):
    cglActiveShaderProgram(pipeline, program)

cdef void glGetProgramPipelineInfoLog(GLuint pipeline, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    cglGetProgramPipelineInfoLog(pipeline, bufSize, length, infoLog)

cdef void glProgramUniform2fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    cglProgramUniform2fv(program, location, count, value)

cdef void glProgramUniform3i(GLuint program, GLint location, GLint v0, GLint v1, GLint v2):
    cglProgramUniform3i(program, location, v0, v1, v2)

cdef void glProgramUniform3d(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2):
    cglProgramUniform3d(program, location, v0, v1, v2)

cdef void glProgramUniform4fv(GLuint program, GLint location, GLsizei count, const GLfloat *value):
    cglProgramUniform4fv(program, location, count, value)

cdef void glProgramUniformMatrix2x3dv(GLuint program, GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglProgramUniformMatrix2x3dv(program, location, count, transpose, value)

cdef void glProgramUniform4d(GLuint program, GLint location, GLdouble v0, GLdouble v1, GLdouble v2, GLdouble v3):
    cglProgramUniform4d(program, location, v0, v1, v2, v3)

cdef void glProgramUniform3uiv(GLuint program, GLint location, GLsizei count, const GLuint *value):
    cglProgramUniform3uiv(program, location, count, value)

cdef void glProgramUniform2dv(GLuint program, GLint location, GLsizei count, const GLdouble *value):
    cglProgramUniform2dv(program, location, count, value)
