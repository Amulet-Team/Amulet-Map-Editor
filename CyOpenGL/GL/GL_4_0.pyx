# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP_ARRAY = 0x900A
cdef GLenum GL_MIN_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5B
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH = 0x8E49
cdef GLenum GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS = 0x8DE8
cdef GLenum GL_DOUBLE_MAT3 = 0x8F47
cdef GLenum GL_DOUBLE_VEC3 = 0x8FFD
cdef GLenum GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E1E
cdef GLenum GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E1F
cdef GLenum GL_PATCH_VERTICES = 0x8E72
cdef GLenum GL_TESS_CONTROL_OUTPUT_VERTICES = 0x8E75
cdef GLenum GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS = 0x8E86
cdef GLenum GL_FRACTIONAL_EVEN = 0x8E7C
cdef GLenum GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS = 0x8E85
cdef GLenum GL_DOUBLE_VEC2 = 0x8FFC
cdef GLenum GL_FRAGMENT_INTERPOLATION_OFFSET_BITS = 0x8E5D
cdef GLenum GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900F
cdef GLenum GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E80
cdef GLenum GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW = 0x900D
cdef GLenum GL_NUM_COMPATIBLE_SUBROUTINES = 0x8E4A
cdef GLenum GL_TRANSFORM_FEEDBACK = 0x8E22
cdef GLenum GL_QUADS = 0x0007
cdef GLenum GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS = 0x8E82
cdef GLenum GL_TEXTURE_CUBE_MAP_ARRAY = 0x9009
cdef GLenum GL_TESS_GEN_POINT_MODE = 0x8E79
cdef GLenum GL_GEOMETRY_SHADER_INVOCATIONS = 0x887F
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS = 0x8E47
cdef GLenum GL_DOUBLE_MAT2 = 0x8F46
cdef GLenum GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS = 0x886D
cdef GLenum GL_PROXY_TEXTURE_CUBE_MAP_ARRAY = 0x900B
cdef GLenum GL_TESS_GEN_MODE = 0x8E76
cdef GLenum GL_TESS_GEN_VERTEX_ORDER = 0x8E78
cdef GLenum GL_TESS_GEN_SPACING = 0x8E77
cdef GLenum GL_MAX_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5C
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORMS = 0x8DE6
cdef GLenum GL_PATCH_DEFAULT_OUTER_LEVEL = 0x8E74
cdef GLenum GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS = 0x8E83
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x84F1
cdef GLenum GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS = 0x8E81
cdef GLenum GL_TRANSFORM_FEEDBACK_BINDING = 0x8E25
cdef GLenum GL_DOUBLE_MAT4x2 = 0x8F4D
cdef GLenum GL_DOUBLE_MAT3x4 = 0x8F4C
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE = 0x8E24
cdef GLenum GL_MAX_SUBROUTINES = 0x8DE7
cdef GLenum GL_PATCH_DEFAULT_INNER_LEVEL = 0x8E73
cdef GLenum GL_DOUBLE_VEC4 = 0x8FFE
cdef GLenum GL_DRAW_INDIRECT_BUFFER_BINDING = 0x8F43
cdef GLenum GL_ACTIVE_SUBROUTINE_MAX_LENGTH = 0x8E48
cdef GLenum GL_MAX_VERTEX_STREAMS = 0x8E71
cdef GLenum GL_MAX_TESS_GEN_LEVEL = 0x8E7E
cdef GLenum GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5F
cdef GLenum GL_DOUBLE_MAT2x4 = 0x8F4A
cdef GLenum GL_ISOLINES = 0x8E7A
cdef GLenum GL_DRAW_INDIRECT_BUFFER = 0x8F3F
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER = 0x84F0
cdef GLenum GL_MAX_TRANSFORM_FEEDBACK_BUFFERS = 0x8E70
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED = 0x8E23
cdef GLenum GL_MIN_SAMPLE_SHADING_VALUE = 0x8C37
cdef GLenum GL_MAX_PATCH_VERTICES = 0x8E7D
cdef GLenum GL_MAX_TESS_PATCH_COMPONENTS = 0x8E84
cdef GLenum GL_ACTIVE_SUBROUTINES = 0x8DE5
cdef GLenum GL_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900E
cdef GLenum GL_PATCHES = 0x000E
cdef GLenum GL_DOUBLE_MAT4 = 0x8F48
cdef GLenum GL_TESS_EVALUATION_SHADER = 0x8E87
cdef GLenum GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5E
cdef GLenum GL_SAMPLE_SHADING = 0x8C36
cdef GLenum GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E7F
cdef GLenum GL_TESS_CONTROL_SHADER = 0x8E88
cdef GLenum GL_DOUBLE_MAT2x3 = 0x8F49
cdef GLenum GL_DOUBLE_MAT4x3 = 0x8F4E
cdef GLenum GL_COMPATIBLE_SUBROUTINES = 0x8E4B
cdef GLenum GL_MAX_TESS_CONTROL_INPUT_COMPONENTS = 0x886C
cdef GLenum GL_DOUBLE_MAT3x2 = 0x8F4B
cdef GLenum GL_FRACTIONAL_ODD = 0x8E7B
cdef GLenum GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS = 0x8E89
cdef GLenum GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS = 0x8E8A
cdef GLenum GL_MAX_GEOMETRY_SHADER_INVOCATIONS = 0x8E5A
cdef GLenum GL_SAMPLER_CUBE_MAP_ARRAY = 0x900C

ctypedef void (*PFNGLDRAWELEMENTSINDIRECTPROC)(GLenum mode, GLenum type, const void *indirect)
ctypedef void (*PFNGLBINDTRANSFORMFEEDBACKPROC)(GLenum target, GLuint id)
ctypedef GLboolean (*PFNGLISTRANSFORMFEEDBACKPROC)(GLuint id)
ctypedef void (*PFNGLUNIFORM4DVPROC)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLUNIFORM3DPROC)(GLint location, GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*PFNGLUNIFORMMATRIX2DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef GLuint (*PFNGLGETSUBROUTINEINDEXPROC)(GLuint program, GLenum shadertype, const GLchar *name)
ctypedef void (*PFNGLGETPROGRAMSTAGEIVPROC)(GLuint program, GLenum shadertype, GLenum pname, GLint *values)
ctypedef void (*PFNGLDRAWTRANSFORMFEEDBACKPROC)(GLenum mode, GLuint id)
ctypedef void (*PFNGLMINSAMPLESHADINGPROC)(GLfloat value)
ctypedef void (*PFNGLUNIFORMMATRIX3X2DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLGETUNIFORMSUBROUTINEUIVPROC)(GLenum shadertype, GLint location, GLuint *params)
ctypedef void (*PFNGLPATCHPARAMETERFVPROC)(GLenum pname, const GLfloat *values)
ctypedef void (*PFNGLBLENDFUNCIPROC)(GLuint buf, GLenum src, GLenum dst)
ctypedef void (*PFNGLUNIFORM2DPROC)(GLint location, GLdouble x, GLdouble y)
ctypedef void (*PFNGLBLENDEQUATIONIPROC)(GLuint buf, GLenum mode)
ctypedef void (*PFNGLUNIFORMMATRIX3X4DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLGETACTIVESUBROUTINENAMEPROC)(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
ctypedef void (*PFNGLGETQUERYINDEXEDIVPROC)(GLenum target, GLuint index, GLenum pname, GLint *params)
ctypedef void (*PFNGLUNIFORM4DPROC)(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*PFNGLBLENDEQUATIONSEPARATEIPROC)(GLuint buf, GLenum modeRGB, GLenum modeAlpha)
ctypedef GLint (*PFNGLGETSUBROUTINEUNIFORMLOCATIONPROC)(GLuint program, GLenum shadertype, const GLchar *name)
ctypedef void (*PFNGLDELETETRANSFORMFEEDBACKSPROC)(GLsizei n, const GLuint *ids)
ctypedef void (*PFNGLUNIFORM1DVPROC)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLGETACTIVESUBROUTINEUNIFORMNAMEPROC)(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
ctypedef void (*PFNGLENDQUERYINDEXEDPROC)(GLenum target, GLuint index)
ctypedef void (*PFNGLBLENDFUNCSEPARATEIPROC)(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
ctypedef void (*PFNGLUNIFORM3DVPROC)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX3DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX2X3DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX2X4DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLDRAWTRANSFORMFEEDBACKSTREAMPROC)(GLenum mode, GLuint id, GLuint stream)
ctypedef void (*PFNGLUNIFORMMATRIX4X2DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLRESUMETRANSFORMFEEDBACKPROC)()
ctypedef void (*PFNGLUNIFORMMATRIX4X3DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLPAUSETRANSFORMFEEDBACKPROC)()
ctypedef void (*PFNGLUNIFORMMATRIX4DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLBEGINQUERYINDEXEDPROC)(GLenum target, GLuint index, GLuint id)
ctypedef void (*PFNGLDRAWARRAYSINDIRECTPROC)(GLenum mode, const void *indirect)
ctypedef void (*PFNGLPATCHPARAMETERIPROC)(GLenum pname, GLint value)
ctypedef void (*PFNGLUNIFORMSUBROUTINESUIVPROC)(GLenum shadertype, GLsizei count, const GLuint *indices)
ctypedef void (*PFNGLGENTRANSFORMFEEDBACKSPROC)(GLsizei n, GLuint *ids)
ctypedef void (*PFNGLUNIFORM1DPROC)(GLint location, GLdouble x)
ctypedef void (*PFNGLUNIFORM2DVPROC)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLGETACTIVESUBROUTINEUNIFORMIVPROC)(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values)
ctypedef void (*PFNGLGETUNIFORMDVPROC)(GLuint program, GLint location, GLdouble *params)

cdef PFNGLDRAWELEMENTSINDIRECTPROC cglDrawElementsIndirect = NULL
cdef PFNGLBINDTRANSFORMFEEDBACKPROC cglBindTransformFeedback = NULL
cdef PFNGLISTRANSFORMFEEDBACKPROC cglIsTransformFeedback = NULL
cdef PFNGLUNIFORM4DVPROC cglUniform4dv = NULL
cdef PFNGLUNIFORM3DPROC cglUniform3d = NULL
cdef PFNGLUNIFORMMATRIX2DVPROC cglUniformMatrix2dv = NULL
cdef PFNGLGETSUBROUTINEINDEXPROC cglGetSubroutineIndex = NULL
cdef PFNGLGETPROGRAMSTAGEIVPROC cglGetProgramStageiv = NULL
cdef PFNGLDRAWTRANSFORMFEEDBACKPROC cglDrawTransformFeedback = NULL
cdef PFNGLMINSAMPLESHADINGPROC cglMinSampleShading = NULL
cdef PFNGLUNIFORMMATRIX3X2DVPROC cglUniformMatrix3x2dv = NULL
cdef PFNGLGETUNIFORMSUBROUTINEUIVPROC cglGetUniformSubroutineuiv = NULL
cdef PFNGLPATCHPARAMETERFVPROC cglPatchParameterfv = NULL
cdef PFNGLBLENDFUNCIPROC cglBlendFunci = NULL
cdef PFNGLUNIFORM2DPROC cglUniform2d = NULL
cdef PFNGLBLENDEQUATIONIPROC cglBlendEquationi = NULL
cdef PFNGLUNIFORMMATRIX3X4DVPROC cglUniformMatrix3x4dv = NULL
cdef PFNGLGETACTIVESUBROUTINENAMEPROC cglGetActiveSubroutineName = NULL
cdef PFNGLGETQUERYINDEXEDIVPROC cglGetQueryIndexediv = NULL
cdef PFNGLUNIFORM4DPROC cglUniform4d = NULL
cdef PFNGLBLENDEQUATIONSEPARATEIPROC cglBlendEquationSeparatei = NULL
cdef PFNGLGETSUBROUTINEUNIFORMLOCATIONPROC cglGetSubroutineUniformLocation = NULL
cdef PFNGLDELETETRANSFORMFEEDBACKSPROC cglDeleteTransformFeedbacks = NULL
cdef PFNGLUNIFORM1DVPROC cglUniform1dv = NULL
cdef PFNGLGETACTIVESUBROUTINEUNIFORMNAMEPROC cglGetActiveSubroutineUniformName = NULL
cdef PFNGLENDQUERYINDEXEDPROC cglEndQueryIndexed = NULL
cdef PFNGLBLENDFUNCSEPARATEIPROC cglBlendFuncSeparatei = NULL
cdef PFNGLUNIFORM3DVPROC cglUniform3dv = NULL
cdef PFNGLUNIFORMMATRIX3DVPROC cglUniformMatrix3dv = NULL
cdef PFNGLUNIFORMMATRIX2X3DVPROC cglUniformMatrix2x3dv = NULL
cdef PFNGLUNIFORMMATRIX2X4DVPROC cglUniformMatrix2x4dv = NULL
cdef PFNGLDRAWTRANSFORMFEEDBACKSTREAMPROC cglDrawTransformFeedbackStream = NULL
cdef PFNGLUNIFORMMATRIX4X2DVPROC cglUniformMatrix4x2dv = NULL
cdef PFNGLRESUMETRANSFORMFEEDBACKPROC cglResumeTransformFeedback = NULL
cdef PFNGLUNIFORMMATRIX4X3DVPROC cglUniformMatrix4x3dv = NULL
cdef PFNGLPAUSETRANSFORMFEEDBACKPROC cglPauseTransformFeedback = NULL
cdef PFNGLUNIFORMMATRIX4DVPROC cglUniformMatrix4dv = NULL
cdef PFNGLBEGINQUERYINDEXEDPROC cglBeginQueryIndexed = NULL
cdef PFNGLDRAWARRAYSINDIRECTPROC cglDrawArraysIndirect = NULL
cdef PFNGLPATCHPARAMETERIPROC cglPatchParameteri = NULL
cdef PFNGLUNIFORMSUBROUTINESUIVPROC cglUniformSubroutinesuiv = NULL
cdef PFNGLGENTRANSFORMFEEDBACKSPROC cglGenTransformFeedbacks = NULL
cdef PFNGLUNIFORM1DPROC cglUniform1d = NULL
cdef PFNGLUNIFORM2DVPROC cglUniform2dv = NULL
cdef PFNGLGETACTIVESUBROUTINEUNIFORMIVPROC cglGetActiveSubroutineUniformiv = NULL
cdef PFNGLGETUNIFORMDVPROC cglGetUniformdv = NULL


cdef void GetglDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect):
    global cglDrawElementsIndirect
    cglDrawElementsIndirect = <PFNGLDRAWELEMENTSINDIRECTPROC>getFunction(b"glDrawElementsIndirect")
    cglDrawElementsIndirect(mode, type, indirect)

cdef void GetglBindTransformFeedback(GLenum target, GLuint id):
    global cglBindTransformFeedback
    cglBindTransformFeedback = <PFNGLBINDTRANSFORMFEEDBACKPROC>getFunction(b"glBindTransformFeedback")
    cglBindTransformFeedback(target, id)

cdef GLboolean GetglIsTransformFeedback(GLuint id):
    global cglIsTransformFeedback
    cglIsTransformFeedback = <PFNGLISTRANSFORMFEEDBACKPROC>getFunction(b"glIsTransformFeedback")
    cglIsTransformFeedback(id)

cdef void GetglUniform4dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform4dv
    cglUniform4dv = <PFNGLUNIFORM4DVPROC>getFunction(b"glUniform4dv")
    cglUniform4dv(location, count, value)

cdef void GetglUniform3d(GLint location, GLdouble x, GLdouble y, GLdouble z):
    global cglUniform3d
    cglUniform3d = <PFNGLUNIFORM3DPROC>getFunction(b"glUniform3d")
    cglUniform3d(location, x, y, z)

cdef void GetglUniformMatrix2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix2dv
    cglUniformMatrix2dv = <PFNGLUNIFORMMATRIX2DVPROC>getFunction(b"glUniformMatrix2dv")
    cglUniformMatrix2dv(location, count, transpose, value)

cdef GLuint GetglGetSubroutineIndex(GLuint program, GLenum shadertype, const GLchar *name):
    global cglGetSubroutineIndex
    cglGetSubroutineIndex = <PFNGLGETSUBROUTINEINDEXPROC>getFunction(b"glGetSubroutineIndex")
    cglGetSubroutineIndex(program, shadertype, name)

cdef void GetglGetProgramStageiv(GLuint program, GLenum shadertype, GLenum pname, GLint *values):
    global cglGetProgramStageiv
    cglGetProgramStageiv = <PFNGLGETPROGRAMSTAGEIVPROC>getFunction(b"glGetProgramStageiv")
    cglGetProgramStageiv(program, shadertype, pname, values)

cdef void GetglDrawTransformFeedback(GLenum mode, GLuint id):
    global cglDrawTransformFeedback
    cglDrawTransformFeedback = <PFNGLDRAWTRANSFORMFEEDBACKPROC>getFunction(b"glDrawTransformFeedback")
    cglDrawTransformFeedback(mode, id)

cdef void GetglMinSampleShading(GLfloat value):
    global cglMinSampleShading
    cglMinSampleShading = <PFNGLMINSAMPLESHADINGPROC>getFunction(b"glMinSampleShading")
    cglMinSampleShading(value)

cdef void GetglUniformMatrix3x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix3x2dv
    cglUniformMatrix3x2dv = <PFNGLUNIFORMMATRIX3X2DVPROC>getFunction(b"glUniformMatrix3x2dv")
    cglUniformMatrix3x2dv(location, count, transpose, value)

cdef void GetglGetUniformSubroutineuiv(GLenum shadertype, GLint location, GLuint *params):
    global cglGetUniformSubroutineuiv
    cglGetUniformSubroutineuiv = <PFNGLGETUNIFORMSUBROUTINEUIVPROC>getFunction(b"glGetUniformSubroutineuiv")
    cglGetUniformSubroutineuiv(shadertype, location, params)

cdef void GetglPatchParameterfv(GLenum pname, const GLfloat *values):
    global cglPatchParameterfv
    cglPatchParameterfv = <PFNGLPATCHPARAMETERFVPROC>getFunction(b"glPatchParameterfv")
    cglPatchParameterfv(pname, values)

cdef void GetglBlendFunci(GLuint buf, GLenum src, GLenum dst):
    global cglBlendFunci
    cglBlendFunci = <PFNGLBLENDFUNCIPROC>getFunction(b"glBlendFunci")
    cglBlendFunci(buf, src, dst)

cdef void GetglUniform2d(GLint location, GLdouble x, GLdouble y):
    global cglUniform2d
    cglUniform2d = <PFNGLUNIFORM2DPROC>getFunction(b"glUniform2d")
    cglUniform2d(location, x, y)

cdef void GetglBlendEquationi(GLuint buf, GLenum mode):
    global cglBlendEquationi
    cglBlendEquationi = <PFNGLBLENDEQUATIONIPROC>getFunction(b"glBlendEquationi")
    cglBlendEquationi(buf, mode)

cdef void GetglUniformMatrix3x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix3x4dv
    cglUniformMatrix3x4dv = <PFNGLUNIFORMMATRIX3X4DVPROC>getFunction(b"glUniformMatrix3x4dv")
    cglUniformMatrix3x4dv(location, count, transpose, value)

cdef void GetglGetActiveSubroutineName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    global cglGetActiveSubroutineName
    cglGetActiveSubroutineName = <PFNGLGETACTIVESUBROUTINENAMEPROC>getFunction(b"glGetActiveSubroutineName")
    cglGetActiveSubroutineName(program, shadertype, index, bufSize, length, name)

cdef void GetglGetQueryIndexediv(GLenum target, GLuint index, GLenum pname, GLint *params):
    global cglGetQueryIndexediv
    cglGetQueryIndexediv = <PFNGLGETQUERYINDEXEDIVPROC>getFunction(b"glGetQueryIndexediv")
    cglGetQueryIndexediv(target, index, pname, params)

cdef void GetglUniform4d(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglUniform4d
    cglUniform4d = <PFNGLUNIFORM4DPROC>getFunction(b"glUniform4d")
    cglUniform4d(location, x, y, z, w)

cdef void GetglBlendEquationSeparatei(GLuint buf, GLenum modeRGB, GLenum modeAlpha):
    global cglBlendEquationSeparatei
    cglBlendEquationSeparatei = <PFNGLBLENDEQUATIONSEPARATEIPROC>getFunction(b"glBlendEquationSeparatei")
    cglBlendEquationSeparatei(buf, modeRGB, modeAlpha)

cdef GLint GetglGetSubroutineUniformLocation(GLuint program, GLenum shadertype, const GLchar *name):
    global cglGetSubroutineUniformLocation
    cglGetSubroutineUniformLocation = <PFNGLGETSUBROUTINEUNIFORMLOCATIONPROC>getFunction(b"glGetSubroutineUniformLocation")
    cglGetSubroutineUniformLocation(program, shadertype, name)

cdef void GetglDeleteTransformFeedbacks(GLsizei n, const GLuint *ids):
    global cglDeleteTransformFeedbacks
    cglDeleteTransformFeedbacks = <PFNGLDELETETRANSFORMFEEDBACKSPROC>getFunction(b"glDeleteTransformFeedbacks")
    cglDeleteTransformFeedbacks(n, ids)

cdef void GetglUniform1dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform1dv
    cglUniform1dv = <PFNGLUNIFORM1DVPROC>getFunction(b"glUniform1dv")
    cglUniform1dv(location, count, value)

cdef void GetglGetActiveSubroutineUniformName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    global cglGetActiveSubroutineUniformName
    cglGetActiveSubroutineUniformName = <PFNGLGETACTIVESUBROUTINEUNIFORMNAMEPROC>getFunction(b"glGetActiveSubroutineUniformName")
    cglGetActiveSubroutineUniformName(program, shadertype, index, bufSize, length, name)

cdef void GetglEndQueryIndexed(GLenum target, GLuint index):
    global cglEndQueryIndexed
    cglEndQueryIndexed = <PFNGLENDQUERYINDEXEDPROC>getFunction(b"glEndQueryIndexed")
    cglEndQueryIndexed(target, index)

cdef void GetglBlendFuncSeparatei(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha):
    global cglBlendFuncSeparatei
    cglBlendFuncSeparatei = <PFNGLBLENDFUNCSEPARATEIPROC>getFunction(b"glBlendFuncSeparatei")
    cglBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha)

cdef void GetglUniform3dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform3dv
    cglUniform3dv = <PFNGLUNIFORM3DVPROC>getFunction(b"glUniform3dv")
    cglUniform3dv(location, count, value)

cdef void GetglUniformMatrix3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix3dv
    cglUniformMatrix3dv = <PFNGLUNIFORMMATRIX3DVPROC>getFunction(b"glUniformMatrix3dv")
    cglUniformMatrix3dv(location, count, transpose, value)

cdef void GetglUniformMatrix2x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix2x3dv
    cglUniformMatrix2x3dv = <PFNGLUNIFORMMATRIX2X3DVPROC>getFunction(b"glUniformMatrix2x3dv")
    cglUniformMatrix2x3dv(location, count, transpose, value)

cdef void GetglUniformMatrix2x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix2x4dv
    cglUniformMatrix2x4dv = <PFNGLUNIFORMMATRIX2X4DVPROC>getFunction(b"glUniformMatrix2x4dv")
    cglUniformMatrix2x4dv(location, count, transpose, value)

cdef void GetglDrawTransformFeedbackStream(GLenum mode, GLuint id, GLuint stream):
    global cglDrawTransformFeedbackStream
    cglDrawTransformFeedbackStream = <PFNGLDRAWTRANSFORMFEEDBACKSTREAMPROC>getFunction(b"glDrawTransformFeedbackStream")
    cglDrawTransformFeedbackStream(mode, id, stream)

cdef void GetglUniformMatrix4x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix4x2dv
    cglUniformMatrix4x2dv = <PFNGLUNIFORMMATRIX4X2DVPROC>getFunction(b"glUniformMatrix4x2dv")
    cglUniformMatrix4x2dv(location, count, transpose, value)

cdef void GetglResumeTransformFeedback():
    global cglResumeTransformFeedback
    cglResumeTransformFeedback = <PFNGLRESUMETRANSFORMFEEDBACKPROC>getFunction(b"glResumeTransformFeedback")
    cglResumeTransformFeedback()

cdef void GetglUniformMatrix4x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix4x3dv
    cglUniformMatrix4x3dv = <PFNGLUNIFORMMATRIX4X3DVPROC>getFunction(b"glUniformMatrix4x3dv")
    cglUniformMatrix4x3dv(location, count, transpose, value)

cdef void GetglPauseTransformFeedback():
    global cglPauseTransformFeedback
    cglPauseTransformFeedback = <PFNGLPAUSETRANSFORMFEEDBACKPROC>getFunction(b"glPauseTransformFeedback")
    cglPauseTransformFeedback()

cdef void GetglUniformMatrix4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix4dv
    cglUniformMatrix4dv = <PFNGLUNIFORMMATRIX4DVPROC>getFunction(b"glUniformMatrix4dv")
    cglUniformMatrix4dv(location, count, transpose, value)

cdef void GetglBeginQueryIndexed(GLenum target, GLuint index, GLuint id):
    global cglBeginQueryIndexed
    cglBeginQueryIndexed = <PFNGLBEGINQUERYINDEXEDPROC>getFunction(b"glBeginQueryIndexed")
    cglBeginQueryIndexed(target, index, id)

cdef void GetglDrawArraysIndirect(GLenum mode, const void *indirect):
    global cglDrawArraysIndirect
    cglDrawArraysIndirect = <PFNGLDRAWARRAYSINDIRECTPROC>getFunction(b"glDrawArraysIndirect")
    cglDrawArraysIndirect(mode, indirect)

cdef void GetglPatchParameteri(GLenum pname, GLint value):
    global cglPatchParameteri
    cglPatchParameteri = <PFNGLPATCHPARAMETERIPROC>getFunction(b"glPatchParameteri")
    cglPatchParameteri(pname, value)

cdef void GetglUniformSubroutinesuiv(GLenum shadertype, GLsizei count, const GLuint *indices):
    global cglUniformSubroutinesuiv
    cglUniformSubroutinesuiv = <PFNGLUNIFORMSUBROUTINESUIVPROC>getFunction(b"glUniformSubroutinesuiv")
    cglUniformSubroutinesuiv(shadertype, count, indices)

cdef void GetglGenTransformFeedbacks(GLsizei n, GLuint *ids):
    global cglGenTransformFeedbacks
    cglGenTransformFeedbacks = <PFNGLGENTRANSFORMFEEDBACKSPROC>getFunction(b"glGenTransformFeedbacks")
    cglGenTransformFeedbacks(n, ids)

cdef void GetglUniform1d(GLint location, GLdouble x):
    global cglUniform1d
    cglUniform1d = <PFNGLUNIFORM1DPROC>getFunction(b"glUniform1d")
    cglUniform1d(location, x)

cdef void GetglUniform2dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform2dv
    cglUniform2dv = <PFNGLUNIFORM2DVPROC>getFunction(b"glUniform2dv")
    cglUniform2dv(location, count, value)

cdef void GetglGetActiveSubroutineUniformiv(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values):
    global cglGetActiveSubroutineUniformiv
    cglGetActiveSubroutineUniformiv = <PFNGLGETACTIVESUBROUTINEUNIFORMIVPROC>getFunction(b"glGetActiveSubroutineUniformiv")
    cglGetActiveSubroutineUniformiv(program, shadertype, index, pname, values)

cdef void GetglGetUniformdv(GLuint program, GLint location, GLdouble *params):
    global cglGetUniformdv
    cglGetUniformdv = <PFNGLGETUNIFORMDVPROC>getFunction(b"glGetUniformdv")
    cglGetUniformdv(program, location, params)

cglDrawElementsIndirect = GetglDrawElementsIndirect
cglBindTransformFeedback = GetglBindTransformFeedback
cglIsTransformFeedback = GetglIsTransformFeedback
cglUniform4dv = GetglUniform4dv
cglUniform3d = GetglUniform3d
cglUniformMatrix2dv = GetglUniformMatrix2dv
cglGetSubroutineIndex = GetglGetSubroutineIndex
cglGetProgramStageiv = GetglGetProgramStageiv
cglDrawTransformFeedback = GetglDrawTransformFeedback
cglMinSampleShading = GetglMinSampleShading
cglUniformMatrix3x2dv = GetglUniformMatrix3x2dv
cglGetUniformSubroutineuiv = GetglGetUniformSubroutineuiv
cglPatchParameterfv = GetglPatchParameterfv
cglBlendFunci = GetglBlendFunci
cglUniform2d = GetglUniform2d
cglBlendEquationi = GetglBlendEquationi
cglUniformMatrix3x4dv = GetglUniformMatrix3x4dv
cglGetActiveSubroutineName = GetglGetActiveSubroutineName
cglGetQueryIndexediv = GetglGetQueryIndexediv
cglUniform4d = GetglUniform4d
cglBlendEquationSeparatei = GetglBlendEquationSeparatei
cglGetSubroutineUniformLocation = GetglGetSubroutineUniformLocation
cglDeleteTransformFeedbacks = GetglDeleteTransformFeedbacks
cglUniform1dv = GetglUniform1dv
cglGetActiveSubroutineUniformName = GetglGetActiveSubroutineUniformName
cglEndQueryIndexed = GetglEndQueryIndexed
cglBlendFuncSeparatei = GetglBlendFuncSeparatei
cglUniform3dv = GetglUniform3dv
cglUniformMatrix3dv = GetglUniformMatrix3dv
cglUniformMatrix2x3dv = GetglUniformMatrix2x3dv
cglUniformMatrix2x4dv = GetglUniformMatrix2x4dv
cglDrawTransformFeedbackStream = GetglDrawTransformFeedbackStream
cglUniformMatrix4x2dv = GetglUniformMatrix4x2dv
cglResumeTransformFeedback = GetglResumeTransformFeedback
cglUniformMatrix4x3dv = GetglUniformMatrix4x3dv
cglPauseTransformFeedback = GetglPauseTransformFeedback
cglUniformMatrix4dv = GetglUniformMatrix4dv
cglBeginQueryIndexed = GetglBeginQueryIndexed
cglDrawArraysIndirect = GetglDrawArraysIndirect
cglPatchParameteri = GetglPatchParameteri
cglUniformSubroutinesuiv = GetglUniformSubroutinesuiv
cglGenTransformFeedbacks = GetglGenTransformFeedbacks
cglUniform1d = GetglUniform1d
cglUniform2dv = GetglUniform2dv
cglGetActiveSubroutineUniformiv = GetglGetActiveSubroutineUniformiv
cglGetUniformdv = GetglGetUniformdv


cdef void glDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect):
    cglDrawElementsIndirect(mode, type, indirect)

cdef void glBindTransformFeedback(GLenum target, GLuint id):
    cglBindTransformFeedback(target, id)

cdef GLboolean glIsTransformFeedback(GLuint id):
    cglIsTransformFeedback(id)

cdef void glUniform4dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform4dv(location, count, value)

cdef void glUniform3d(GLint location, GLdouble x, GLdouble y, GLdouble z):
    cglUniform3d(location, x, y, z)

cdef void glUniformMatrix2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix2dv(location, count, transpose, value)

cdef GLuint glGetSubroutineIndex(GLuint program, GLenum shadertype, const GLchar *name):
    cglGetSubroutineIndex(program, shadertype, name)

cdef void glGetProgramStageiv(GLuint program, GLenum shadertype, GLenum pname, GLint *values):
    cglGetProgramStageiv(program, shadertype, pname, values)

cdef void glDrawTransformFeedback(GLenum mode, GLuint id):
    cglDrawTransformFeedback(mode, id)

cdef void glMinSampleShading(GLfloat value):
    cglMinSampleShading(value)

cdef void glUniformMatrix3x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix3x2dv(location, count, transpose, value)

cdef void glGetUniformSubroutineuiv(GLenum shadertype, GLint location, GLuint *params):
    cglGetUniformSubroutineuiv(shadertype, location, params)

cdef void glPatchParameterfv(GLenum pname, const GLfloat *values):
    cglPatchParameterfv(pname, values)

cdef void glBlendFunci(GLuint buf, GLenum src, GLenum dst):
    cglBlendFunci(buf, src, dst)

cdef void glUniform2d(GLint location, GLdouble x, GLdouble y):
    cglUniform2d(location, x, y)

cdef void glBlendEquationi(GLuint buf, GLenum mode):
    cglBlendEquationi(buf, mode)

cdef void glUniformMatrix3x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix3x4dv(location, count, transpose, value)

cdef void glGetActiveSubroutineName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    cglGetActiveSubroutineName(program, shadertype, index, bufSize, length, name)

cdef void glGetQueryIndexediv(GLenum target, GLuint index, GLenum pname, GLint *params):
    cglGetQueryIndexediv(target, index, pname, params)

cdef void glUniform4d(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglUniform4d(location, x, y, z, w)

cdef void glBlendEquationSeparatei(GLuint buf, GLenum modeRGB, GLenum modeAlpha):
    cglBlendEquationSeparatei(buf, modeRGB, modeAlpha)

cdef GLint glGetSubroutineUniformLocation(GLuint program, GLenum shadertype, const GLchar *name):
    cglGetSubroutineUniformLocation(program, shadertype, name)

cdef void glDeleteTransformFeedbacks(GLsizei n, const GLuint *ids):
    cglDeleteTransformFeedbacks(n, ids)

cdef void glUniform1dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform1dv(location, count, value)

cdef void glGetActiveSubroutineUniformName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    cglGetActiveSubroutineUniformName(program, shadertype, index, bufSize, length, name)

cdef void glEndQueryIndexed(GLenum target, GLuint index):
    cglEndQueryIndexed(target, index)

cdef void glBlendFuncSeparatei(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha):
    cglBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha)

cdef void glUniform3dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform3dv(location, count, value)

cdef void glUniformMatrix3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix3dv(location, count, transpose, value)

cdef void glUniformMatrix2x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix2x3dv(location, count, transpose, value)

cdef void glUniformMatrix2x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix2x4dv(location, count, transpose, value)

cdef void glDrawTransformFeedbackStream(GLenum mode, GLuint id, GLuint stream):
    cglDrawTransformFeedbackStream(mode, id, stream)

cdef void glUniformMatrix4x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix4x2dv(location, count, transpose, value)

cdef void glResumeTransformFeedback():
    cglResumeTransformFeedback()

cdef void glUniformMatrix4x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix4x3dv(location, count, transpose, value)

cdef void glPauseTransformFeedback():
    cglPauseTransformFeedback()

cdef void glUniformMatrix4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix4dv(location, count, transpose, value)

cdef void glBeginQueryIndexed(GLenum target, GLuint index, GLuint id):
    cglBeginQueryIndexed(target, index, id)

cdef void glDrawArraysIndirect(GLenum mode, const void *indirect):
    cglDrawArraysIndirect(mode, indirect)

cdef void glPatchParameteri(GLenum pname, GLint value):
    cglPatchParameteri(pname, value)

cdef void glUniformSubroutinesuiv(GLenum shadertype, GLsizei count, const GLuint *indices):
    cglUniformSubroutinesuiv(shadertype, count, indices)

cdef void glGenTransformFeedbacks(GLsizei n, GLuint *ids):
    cglGenTransformFeedbacks(n, ids)

cdef void glUniform1d(GLint location, GLdouble x):
    cglUniform1d(location, x)

cdef void glUniform2dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform2dv(location, count, value)

cdef void glGetActiveSubroutineUniformiv(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values):
    cglGetActiveSubroutineUniformiv(program, shadertype, index, pname, values)

cdef void glGetUniformdv(GLuint program, GLint location, GLdouble *params):
    cglGetUniformdv(program, location, params)
