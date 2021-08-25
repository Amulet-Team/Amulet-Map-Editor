# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_ACTIVE_SUBROUTINES = 0x8DE5
cdef GLenum GL_ACTIVE_SUBROUTINE_MAX_LENGTH = 0x8E48
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORMS = 0x8DE6
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS = 0x8E47
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH = 0x8E49
cdef GLenum GL_COMPATIBLE_SUBROUTINES = 0x8E4B
cdef GLenum GL_DOUBLE_MAT2 = 0x8F46
cdef GLenum GL_DOUBLE_MAT2x3 = 0x8F49
cdef GLenum GL_DOUBLE_MAT2x4 = 0x8F4A
cdef GLenum GL_DOUBLE_MAT3 = 0x8F47
cdef GLenum GL_DOUBLE_MAT3x2 = 0x8F4B
cdef GLenum GL_DOUBLE_MAT3x4 = 0x8F4C
cdef GLenum GL_DOUBLE_MAT4 = 0x8F48
cdef GLenum GL_DOUBLE_MAT4x2 = 0x8F4D
cdef GLenum GL_DOUBLE_MAT4x3 = 0x8F4E
cdef GLenum GL_DOUBLE_VEC2 = 0x8FFC
cdef GLenum GL_DOUBLE_VEC3 = 0x8FFD
cdef GLenum GL_DOUBLE_VEC4 = 0x8FFE
cdef GLenum GL_DRAW_INDIRECT_BUFFER = 0x8F3F
cdef GLenum GL_DRAW_INDIRECT_BUFFER_BINDING = 0x8F43
cdef GLenum GL_FRACTIONAL_EVEN = 0x8E7C
cdef GLenum GL_FRACTIONAL_ODD = 0x8E7B
cdef GLenum GL_FRAGMENT_INTERPOLATION_OFFSET_BITS = 0x8E5D
cdef GLenum GL_GEOMETRY_SHADER_INVOCATIONS = 0x887F
cdef GLenum GL_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900E
cdef GLenum GL_ISOLINES = 0x8E7A
cdef GLenum GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E1E
cdef GLenum GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E1F
cdef GLenum GL_MAX_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5C
cdef GLenum GL_MAX_GEOMETRY_SHADER_INVOCATIONS = 0x8E5A
cdef GLenum GL_MAX_PATCH_VERTICES = 0x8E7D
cdef GLenum GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5F
cdef GLenum GL_MAX_SUBROUTINES = 0x8DE7
cdef GLenum GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS = 0x8DE8
cdef GLenum GL_MAX_TESS_CONTROL_INPUT_COMPONENTS = 0x886C
cdef GLenum GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS = 0x8E83
cdef GLenum GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS = 0x8E81
cdef GLenum GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS = 0x8E85
cdef GLenum GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS = 0x8E89
cdef GLenum GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E7F
cdef GLenum GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS = 0x886D
cdef GLenum GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS = 0x8E86
cdef GLenum GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS = 0x8E82
cdef GLenum GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS = 0x8E8A
cdef GLenum GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E80
cdef GLenum GL_MAX_TESS_GEN_LEVEL = 0x8E7E
cdef GLenum GL_MAX_TESS_PATCH_COMPONENTS = 0x8E84
cdef GLenum GL_MAX_TRANSFORM_FEEDBACK_BUFFERS = 0x8E70
cdef GLenum GL_MAX_VERTEX_STREAMS = 0x8E71
cdef GLenum GL_MIN_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5B
cdef GLenum GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5E
cdef GLenum GL_MIN_SAMPLE_SHADING_VALUE = 0x8C37
cdef GLenum GL_NUM_COMPATIBLE_SUBROUTINES = 0x8E4A
cdef GLenum GL_PATCHES = 0x000E
cdef GLenum GL_PATCH_DEFAULT_INNER_LEVEL = 0x8E73
cdef GLenum GL_PATCH_DEFAULT_OUTER_LEVEL = 0x8E74
cdef GLenum GL_PATCH_VERTICES = 0x8E72
cdef GLenum GL_PROXY_TEXTURE_CUBE_MAP_ARRAY = 0x900B
cdef GLenum GL_QUADS = 0x0007
cdef GLenum GL_SAMPLER_CUBE_MAP_ARRAY = 0x900C
cdef GLenum GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW = 0x900D
cdef GLenum GL_SAMPLE_SHADING = 0x8C36
cdef GLenum GL_TESS_CONTROL_OUTPUT_VERTICES = 0x8E75
cdef GLenum GL_TESS_CONTROL_SHADER = 0x8E88
cdef GLenum GL_TESS_EVALUATION_SHADER = 0x8E87
cdef GLenum GL_TESS_GEN_MODE = 0x8E76
cdef GLenum GL_TESS_GEN_POINT_MODE = 0x8E79
cdef GLenum GL_TESS_GEN_SPACING = 0x8E77
cdef GLenum GL_TESS_GEN_VERTEX_ORDER = 0x8E78
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP_ARRAY = 0x900A
cdef GLenum GL_TEXTURE_CUBE_MAP_ARRAY = 0x9009
cdef GLenum GL_TRANSFORM_FEEDBACK = 0x8E22
cdef GLenum GL_TRANSFORM_FEEDBACK_BINDING = 0x8E25
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE = 0x8E24
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED = 0x8E23
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER = 0x84F0
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x84F1
cdef GLenum GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900F

ctypedef void (*PFNGLBEGINQUERYINDEXEDPROC)(GLenum target, GLuint index, GLuint id)
ctypedef void (*PFNGLBINDTRANSFORMFEEDBACKPROC)(GLenum target, GLuint id)
ctypedef void (*PFNGLBLENDEQUATIONSEPARATEIPROC)(GLuint buf, GLenum modeRGB, GLenum modeAlpha)
ctypedef void (*PFNGLBLENDEQUATIONIPROC)(GLuint buf, GLenum mode)
ctypedef void (*PFNGLBLENDFUNCSEPARATEIPROC)(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
ctypedef void (*PFNGLBLENDFUNCIPROC)(GLuint buf, GLenum src, GLenum dst)
ctypedef void (*PFNGLDELETETRANSFORMFEEDBACKSPROC)(GLsizei n, const GLuint *ids)
ctypedef void (*PFNGLDRAWARRAYSINDIRECTPROC)(GLenum mode, const void *indirect)
ctypedef void (*PFNGLDRAWELEMENTSINDIRECTPROC)(GLenum mode, GLenum type, const void *indirect)
ctypedef void (*PFNGLDRAWTRANSFORMFEEDBACKPROC)(GLenum mode, GLuint id)
ctypedef void (*PFNGLDRAWTRANSFORMFEEDBACKSTREAMPROC)(GLenum mode, GLuint id, GLuint stream)
ctypedef void (*PFNGLENDQUERYINDEXEDPROC)(GLenum target, GLuint index)
ctypedef void (*PFNGLGENTRANSFORMFEEDBACKSPROC)(GLsizei n, GLuint *ids)
ctypedef void (*PFNGLGETACTIVESUBROUTINENAMEPROC)(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
ctypedef void (*PFNGLGETACTIVESUBROUTINEUNIFORMNAMEPROC)(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
ctypedef void (*PFNGLGETACTIVESUBROUTINEUNIFORMIVPROC)(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values)
ctypedef void (*PFNGLGETPROGRAMSTAGEIVPROC)(GLuint program, GLenum shadertype, GLenum pname, GLint *values)
ctypedef void (*PFNGLGETQUERYINDEXEDIVPROC)(GLenum target, GLuint index, GLenum pname, GLint *params)
ctypedef GLuint (*PFNGLGETSUBROUTINEINDEXPROC)(GLuint program, GLenum shadertype, const GLchar *name)
ctypedef GLint (*PFNGLGETSUBROUTINEUNIFORMLOCATIONPROC)(GLuint program, GLenum shadertype, const GLchar *name)
ctypedef void (*PFNGLGETUNIFORMSUBROUTINEUIVPROC)(GLenum shadertype, GLint location, GLuint *params)
ctypedef void (*PFNGLGETUNIFORMDVPROC)(GLuint program, GLint location, GLdouble *params)
ctypedef GLboolean (*PFNGLISTRANSFORMFEEDBACKPROC)(GLuint id)
ctypedef void (*PFNGLMINSAMPLESHADINGPROC)(GLfloat value)
ctypedef void (*PFNGLPATCHPARAMETERFVPROC)(GLenum pname, const GLfloat *values)
ctypedef void (*PFNGLPATCHPARAMETERIPROC)(GLenum pname, GLint value)
ctypedef void (*PFNGLPAUSETRANSFORMFEEDBACKPROC)()
ctypedef void (*PFNGLRESUMETRANSFORMFEEDBACKPROC)()
ctypedef void (*PFNGLUNIFORM1DPROC)(GLint location, GLdouble x)
ctypedef void (*PFNGLUNIFORM1DVPROC)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLUNIFORM2DPROC)(GLint location, GLdouble x, GLdouble y)
ctypedef void (*PFNGLUNIFORM2DVPROC)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLUNIFORM3DPROC)(GLint location, GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*PFNGLUNIFORM3DVPROC)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLUNIFORM4DPROC)(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*PFNGLUNIFORM4DVPROC)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX2DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX2X3DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX2X4DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX3DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX3X2DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX3X4DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX4DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX4X2DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMMATRIX4X3DVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*PFNGLUNIFORMSUBROUTINESUIVPROC)(GLenum shadertype, GLsizei count, const GLuint *indices)

cdef PFNGLBEGINQUERYINDEXEDPROC cglBeginQueryIndexed = NULL
cdef PFNGLBINDTRANSFORMFEEDBACKPROC cglBindTransformFeedback = NULL
cdef PFNGLBLENDEQUATIONSEPARATEIPROC cglBlendEquationSeparatei = NULL
cdef PFNGLBLENDEQUATIONIPROC cglBlendEquationi = NULL
cdef PFNGLBLENDFUNCSEPARATEIPROC cglBlendFuncSeparatei = NULL
cdef PFNGLBLENDFUNCIPROC cglBlendFunci = NULL
cdef PFNGLDELETETRANSFORMFEEDBACKSPROC cglDeleteTransformFeedbacks = NULL
cdef PFNGLDRAWARRAYSINDIRECTPROC cglDrawArraysIndirect = NULL
cdef PFNGLDRAWELEMENTSINDIRECTPROC cglDrawElementsIndirect = NULL
cdef PFNGLDRAWTRANSFORMFEEDBACKPROC cglDrawTransformFeedback = NULL
cdef PFNGLDRAWTRANSFORMFEEDBACKSTREAMPROC cglDrawTransformFeedbackStream = NULL
cdef PFNGLENDQUERYINDEXEDPROC cglEndQueryIndexed = NULL
cdef PFNGLGENTRANSFORMFEEDBACKSPROC cglGenTransformFeedbacks = NULL
cdef PFNGLGETACTIVESUBROUTINENAMEPROC cglGetActiveSubroutineName = NULL
cdef PFNGLGETACTIVESUBROUTINEUNIFORMNAMEPROC cglGetActiveSubroutineUniformName = NULL
cdef PFNGLGETACTIVESUBROUTINEUNIFORMIVPROC cglGetActiveSubroutineUniformiv = NULL
cdef PFNGLGETPROGRAMSTAGEIVPROC cglGetProgramStageiv = NULL
cdef PFNGLGETQUERYINDEXEDIVPROC cglGetQueryIndexediv = NULL
cdef PFNGLGETSUBROUTINEINDEXPROC cglGetSubroutineIndex = NULL
cdef PFNGLGETSUBROUTINEUNIFORMLOCATIONPROC cglGetSubroutineUniformLocation = NULL
cdef PFNGLGETUNIFORMSUBROUTINEUIVPROC cglGetUniformSubroutineuiv = NULL
cdef PFNGLGETUNIFORMDVPROC cglGetUniformdv = NULL
cdef PFNGLISTRANSFORMFEEDBACKPROC cglIsTransformFeedback = NULL
cdef PFNGLMINSAMPLESHADINGPROC cglMinSampleShading = NULL
cdef PFNGLPATCHPARAMETERFVPROC cglPatchParameterfv = NULL
cdef PFNGLPATCHPARAMETERIPROC cglPatchParameteri = NULL
cdef PFNGLPAUSETRANSFORMFEEDBACKPROC cglPauseTransformFeedback = NULL
cdef PFNGLRESUMETRANSFORMFEEDBACKPROC cglResumeTransformFeedback = NULL
cdef PFNGLUNIFORM1DPROC cglUniform1d = NULL
cdef PFNGLUNIFORM1DVPROC cglUniform1dv = NULL
cdef PFNGLUNIFORM2DPROC cglUniform2d = NULL
cdef PFNGLUNIFORM2DVPROC cglUniform2dv = NULL
cdef PFNGLUNIFORM3DPROC cglUniform3d = NULL
cdef PFNGLUNIFORM3DVPROC cglUniform3dv = NULL
cdef PFNGLUNIFORM4DPROC cglUniform4d = NULL
cdef PFNGLUNIFORM4DVPROC cglUniform4dv = NULL
cdef PFNGLUNIFORMMATRIX2DVPROC cglUniformMatrix2dv = NULL
cdef PFNGLUNIFORMMATRIX2X3DVPROC cglUniformMatrix2x3dv = NULL
cdef PFNGLUNIFORMMATRIX2X4DVPROC cglUniformMatrix2x4dv = NULL
cdef PFNGLUNIFORMMATRIX3DVPROC cglUniformMatrix3dv = NULL
cdef PFNGLUNIFORMMATRIX3X2DVPROC cglUniformMatrix3x2dv = NULL
cdef PFNGLUNIFORMMATRIX3X4DVPROC cglUniformMatrix3x4dv = NULL
cdef PFNGLUNIFORMMATRIX4DVPROC cglUniformMatrix4dv = NULL
cdef PFNGLUNIFORMMATRIX4X2DVPROC cglUniformMatrix4x2dv = NULL
cdef PFNGLUNIFORMMATRIX4X3DVPROC cglUniformMatrix4x3dv = NULL
cdef PFNGLUNIFORMSUBROUTINESUIVPROC cglUniformSubroutinesuiv = NULL


cdef void GetglBeginQueryIndexed(GLenum target, GLuint index, GLuint id):
    global cglBeginQueryIndexed
    cglBeginQueryIndexed = <PFNGLBEGINQUERYINDEXEDPROC>getFunction("glBeginQueryIndexed")
    cglBeginQueryIndexed(target, index, id)

cdef void GetglBindTransformFeedback(GLenum target, GLuint id):
    global cglBindTransformFeedback
    cglBindTransformFeedback = <PFNGLBINDTRANSFORMFEEDBACKPROC>getFunction("glBindTransformFeedback")
    cglBindTransformFeedback(target, id)

cdef void GetglBlendEquationSeparatei(GLuint buf, GLenum modeRGB, GLenum modeAlpha):
    global cglBlendEquationSeparatei
    cglBlendEquationSeparatei = <PFNGLBLENDEQUATIONSEPARATEIPROC>getFunction("glBlendEquationSeparatei")
    cglBlendEquationSeparatei(buf, modeRGB, modeAlpha)

cdef void GetglBlendEquationi(GLuint buf, GLenum mode):
    global cglBlendEquationi
    cglBlendEquationi = <PFNGLBLENDEQUATIONIPROC>getFunction("glBlendEquationi")
    cglBlendEquationi(buf, mode)

cdef void GetglBlendFuncSeparatei(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha):
    global cglBlendFuncSeparatei
    cglBlendFuncSeparatei = <PFNGLBLENDFUNCSEPARATEIPROC>getFunction("glBlendFuncSeparatei")
    cglBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha)

cdef void GetglBlendFunci(GLuint buf, GLenum src, GLenum dst):
    global cglBlendFunci
    cglBlendFunci = <PFNGLBLENDFUNCIPROC>getFunction("glBlendFunci")
    cglBlendFunci(buf, src, dst)

cdef void GetglDeleteTransformFeedbacks(GLsizei n, const GLuint *ids):
    global cglDeleteTransformFeedbacks
    cglDeleteTransformFeedbacks = <PFNGLDELETETRANSFORMFEEDBACKSPROC>getFunction("glDeleteTransformFeedbacks")
    cglDeleteTransformFeedbacks(n, ids)

cdef void GetglDrawArraysIndirect(GLenum mode, const void *indirect):
    global cglDrawArraysIndirect
    cglDrawArraysIndirect = <PFNGLDRAWARRAYSINDIRECTPROC>getFunction("glDrawArraysIndirect")
    cglDrawArraysIndirect(mode, indirect)

cdef void GetglDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect):
    global cglDrawElementsIndirect
    cglDrawElementsIndirect = <PFNGLDRAWELEMENTSINDIRECTPROC>getFunction("glDrawElementsIndirect")
    cglDrawElementsIndirect(mode, type, indirect)

cdef void GetglDrawTransformFeedback(GLenum mode, GLuint id):
    global cglDrawTransformFeedback
    cglDrawTransformFeedback = <PFNGLDRAWTRANSFORMFEEDBACKPROC>getFunction("glDrawTransformFeedback")
    cglDrawTransformFeedback(mode, id)

cdef void GetglDrawTransformFeedbackStream(GLenum mode, GLuint id, GLuint stream):
    global cglDrawTransformFeedbackStream
    cglDrawTransformFeedbackStream = <PFNGLDRAWTRANSFORMFEEDBACKSTREAMPROC>getFunction("glDrawTransformFeedbackStream")
    cglDrawTransformFeedbackStream(mode, id, stream)

cdef void GetglEndQueryIndexed(GLenum target, GLuint index):
    global cglEndQueryIndexed
    cglEndQueryIndexed = <PFNGLENDQUERYINDEXEDPROC>getFunction("glEndQueryIndexed")
    cglEndQueryIndexed(target, index)

cdef void GetglGenTransformFeedbacks(GLsizei n, GLuint *ids):
    global cglGenTransformFeedbacks
    cglGenTransformFeedbacks = <PFNGLGENTRANSFORMFEEDBACKSPROC>getFunction("glGenTransformFeedbacks")
    cglGenTransformFeedbacks(n, ids)

cdef void GetglGetActiveSubroutineName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    global cglGetActiveSubroutineName
    cglGetActiveSubroutineName = <PFNGLGETACTIVESUBROUTINENAMEPROC>getFunction("glGetActiveSubroutineName")
    cglGetActiveSubroutineName(program, shadertype, index, bufSize, length, name)

cdef void GetglGetActiveSubroutineUniformName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    global cglGetActiveSubroutineUniformName
    cglGetActiveSubroutineUniformName = <PFNGLGETACTIVESUBROUTINEUNIFORMNAMEPROC>getFunction("glGetActiveSubroutineUniformName")
    cglGetActiveSubroutineUniformName(program, shadertype, index, bufSize, length, name)

cdef void GetglGetActiveSubroutineUniformiv(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values):
    global cglGetActiveSubroutineUniformiv
    cglGetActiveSubroutineUniformiv = <PFNGLGETACTIVESUBROUTINEUNIFORMIVPROC>getFunction("glGetActiveSubroutineUniformiv")
    cglGetActiveSubroutineUniformiv(program, shadertype, index, pname, values)

cdef void GetglGetProgramStageiv(GLuint program, GLenum shadertype, GLenum pname, GLint *values):
    global cglGetProgramStageiv
    cglGetProgramStageiv = <PFNGLGETPROGRAMSTAGEIVPROC>getFunction("glGetProgramStageiv")
    cglGetProgramStageiv(program, shadertype, pname, values)

cdef void GetglGetQueryIndexediv(GLenum target, GLuint index, GLenum pname, GLint *params):
    global cglGetQueryIndexediv
    cglGetQueryIndexediv = <PFNGLGETQUERYINDEXEDIVPROC>getFunction("glGetQueryIndexediv")
    cglGetQueryIndexediv(target, index, pname, params)

cdef GLuint GetglGetSubroutineIndex(GLuint program, GLenum shadertype, const GLchar *name):
    global cglGetSubroutineIndex
    cglGetSubroutineIndex = <PFNGLGETSUBROUTINEINDEXPROC>getFunction("glGetSubroutineIndex")
    cglGetSubroutineIndex(program, shadertype, name)

cdef GLint GetglGetSubroutineUniformLocation(GLuint program, GLenum shadertype, const GLchar *name):
    global cglGetSubroutineUniformLocation
    cglGetSubroutineUniformLocation = <PFNGLGETSUBROUTINEUNIFORMLOCATIONPROC>getFunction("glGetSubroutineUniformLocation")
    cglGetSubroutineUniformLocation(program, shadertype, name)

cdef void GetglGetUniformSubroutineuiv(GLenum shadertype, GLint location, GLuint *params):
    global cglGetUniformSubroutineuiv
    cglGetUniformSubroutineuiv = <PFNGLGETUNIFORMSUBROUTINEUIVPROC>getFunction("glGetUniformSubroutineuiv")
    cglGetUniformSubroutineuiv(shadertype, location, params)

cdef void GetglGetUniformdv(GLuint program, GLint location, GLdouble *params):
    global cglGetUniformdv
    cglGetUniformdv = <PFNGLGETUNIFORMDVPROC>getFunction("glGetUniformdv")
    cglGetUniformdv(program, location, params)

cdef GLboolean GetglIsTransformFeedback(GLuint id):
    global cglIsTransformFeedback
    cglIsTransformFeedback = <PFNGLISTRANSFORMFEEDBACKPROC>getFunction("glIsTransformFeedback")
    cglIsTransformFeedback(id)

cdef void GetglMinSampleShading(GLfloat value):
    global cglMinSampleShading
    cglMinSampleShading = <PFNGLMINSAMPLESHADINGPROC>getFunction("glMinSampleShading")
    cglMinSampleShading(value)

cdef void GetglPatchParameterfv(GLenum pname, const GLfloat *values):
    global cglPatchParameterfv
    cglPatchParameterfv = <PFNGLPATCHPARAMETERFVPROC>getFunction("glPatchParameterfv")
    cglPatchParameterfv(pname, values)

cdef void GetglPatchParameteri(GLenum pname, GLint value):
    global cglPatchParameteri
    cglPatchParameteri = <PFNGLPATCHPARAMETERIPROC>getFunction("glPatchParameteri")
    cglPatchParameteri(pname, value)

cdef void GetglPauseTransformFeedback():
    global cglPauseTransformFeedback
    cglPauseTransformFeedback = <PFNGLPAUSETRANSFORMFEEDBACKPROC>getFunction("glPauseTransformFeedback")
    cglPauseTransformFeedback()

cdef void GetglResumeTransformFeedback():
    global cglResumeTransformFeedback
    cglResumeTransformFeedback = <PFNGLRESUMETRANSFORMFEEDBACKPROC>getFunction("glResumeTransformFeedback")
    cglResumeTransformFeedback()

cdef void GetglUniform1d(GLint location, GLdouble x):
    global cglUniform1d
    cglUniform1d = <PFNGLUNIFORM1DPROC>getFunction("glUniform1d")
    cglUniform1d(location, x)

cdef void GetglUniform1dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform1dv
    cglUniform1dv = <PFNGLUNIFORM1DVPROC>getFunction("glUniform1dv")
    cglUniform1dv(location, count, value)

cdef void GetglUniform2d(GLint location, GLdouble x, GLdouble y):
    global cglUniform2d
    cglUniform2d = <PFNGLUNIFORM2DPROC>getFunction("glUniform2d")
    cglUniform2d(location, x, y)

cdef void GetglUniform2dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform2dv
    cglUniform2dv = <PFNGLUNIFORM2DVPROC>getFunction("glUniform2dv")
    cglUniform2dv(location, count, value)

cdef void GetglUniform3d(GLint location, GLdouble x, GLdouble y, GLdouble z):
    global cglUniform3d
    cglUniform3d = <PFNGLUNIFORM3DPROC>getFunction("glUniform3d")
    cglUniform3d(location, x, y, z)

cdef void GetglUniform3dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform3dv
    cglUniform3dv = <PFNGLUNIFORM3DVPROC>getFunction("glUniform3dv")
    cglUniform3dv(location, count, value)

cdef void GetglUniform4d(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglUniform4d
    cglUniform4d = <PFNGLUNIFORM4DPROC>getFunction("glUniform4d")
    cglUniform4d(location, x, y, z, w)

cdef void GetglUniform4dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform4dv
    cglUniform4dv = <PFNGLUNIFORM4DVPROC>getFunction("glUniform4dv")
    cglUniform4dv(location, count, value)

cdef void GetglUniformMatrix2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix2dv
    cglUniformMatrix2dv = <PFNGLUNIFORMMATRIX2DVPROC>getFunction("glUniformMatrix2dv")
    cglUniformMatrix2dv(location, count, transpose, value)

cdef void GetglUniformMatrix2x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix2x3dv
    cglUniformMatrix2x3dv = <PFNGLUNIFORMMATRIX2X3DVPROC>getFunction("glUniformMatrix2x3dv")
    cglUniformMatrix2x3dv(location, count, transpose, value)

cdef void GetglUniformMatrix2x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix2x4dv
    cglUniformMatrix2x4dv = <PFNGLUNIFORMMATRIX2X4DVPROC>getFunction("glUniformMatrix2x4dv")
    cglUniformMatrix2x4dv(location, count, transpose, value)

cdef void GetglUniformMatrix3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix3dv
    cglUniformMatrix3dv = <PFNGLUNIFORMMATRIX3DVPROC>getFunction("glUniformMatrix3dv")
    cglUniformMatrix3dv(location, count, transpose, value)

cdef void GetglUniformMatrix3x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix3x2dv
    cglUniformMatrix3x2dv = <PFNGLUNIFORMMATRIX3X2DVPROC>getFunction("glUniformMatrix3x2dv")
    cglUniformMatrix3x2dv(location, count, transpose, value)

cdef void GetglUniformMatrix3x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix3x4dv
    cglUniformMatrix3x4dv = <PFNGLUNIFORMMATRIX3X4DVPROC>getFunction("glUniformMatrix3x4dv")
    cglUniformMatrix3x4dv(location, count, transpose, value)

cdef void GetglUniformMatrix4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix4dv
    cglUniformMatrix4dv = <PFNGLUNIFORMMATRIX4DVPROC>getFunction("glUniformMatrix4dv")
    cglUniformMatrix4dv(location, count, transpose, value)

cdef void GetglUniformMatrix4x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix4x2dv
    cglUniformMatrix4x2dv = <PFNGLUNIFORMMATRIX4X2DVPROC>getFunction("glUniformMatrix4x2dv")
    cglUniformMatrix4x2dv(location, count, transpose, value)

cdef void GetglUniformMatrix4x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix4x3dv
    cglUniformMatrix4x3dv = <PFNGLUNIFORMMATRIX4X3DVPROC>getFunction("glUniformMatrix4x3dv")
    cglUniformMatrix4x3dv(location, count, transpose, value)

cdef void GetglUniformSubroutinesuiv(GLenum shadertype, GLsizei count, const GLuint *indices):
    global cglUniformSubroutinesuiv
    cglUniformSubroutinesuiv = <PFNGLUNIFORMSUBROUTINESUIVPROC>getFunction("glUniformSubroutinesuiv")
    cglUniformSubroutinesuiv(shadertype, count, indices)

cglBeginQueryIndexed = GetglBeginQueryIndexed
cglBindTransformFeedback = GetglBindTransformFeedback
cglBlendEquationSeparatei = GetglBlendEquationSeparatei
cglBlendEquationi = GetglBlendEquationi
cglBlendFuncSeparatei = GetglBlendFuncSeparatei
cglBlendFunci = GetglBlendFunci
cglDeleteTransformFeedbacks = GetglDeleteTransformFeedbacks
cglDrawArraysIndirect = GetglDrawArraysIndirect
cglDrawElementsIndirect = GetglDrawElementsIndirect
cglDrawTransformFeedback = GetglDrawTransformFeedback
cglDrawTransformFeedbackStream = GetglDrawTransformFeedbackStream
cglEndQueryIndexed = GetglEndQueryIndexed
cglGenTransformFeedbacks = GetglGenTransformFeedbacks
cglGetActiveSubroutineName = GetglGetActiveSubroutineName
cglGetActiveSubroutineUniformName = GetglGetActiveSubroutineUniformName
cglGetActiveSubroutineUniformiv = GetglGetActiveSubroutineUniformiv
cglGetProgramStageiv = GetglGetProgramStageiv
cglGetQueryIndexediv = GetglGetQueryIndexediv
cglGetSubroutineIndex = GetglGetSubroutineIndex
cglGetSubroutineUniformLocation = GetglGetSubroutineUniformLocation
cglGetUniformSubroutineuiv = GetglGetUniformSubroutineuiv
cglGetUniformdv = GetglGetUniformdv
cglIsTransformFeedback = GetglIsTransformFeedback
cglMinSampleShading = GetglMinSampleShading
cglPatchParameterfv = GetglPatchParameterfv
cglPatchParameteri = GetglPatchParameteri
cglPauseTransformFeedback = GetglPauseTransformFeedback
cglResumeTransformFeedback = GetglResumeTransformFeedback
cglUniform1d = GetglUniform1d
cglUniform1dv = GetglUniform1dv
cglUniform2d = GetglUniform2d
cglUniform2dv = GetglUniform2dv
cglUniform3d = GetglUniform3d
cglUniform3dv = GetglUniform3dv
cglUniform4d = GetglUniform4d
cglUniform4dv = GetglUniform4dv
cglUniformMatrix2dv = GetglUniformMatrix2dv
cglUniformMatrix2x3dv = GetglUniformMatrix2x3dv
cglUniformMatrix2x4dv = GetglUniformMatrix2x4dv
cglUniformMatrix3dv = GetglUniformMatrix3dv
cglUniformMatrix3x2dv = GetglUniformMatrix3x2dv
cglUniformMatrix3x4dv = GetglUniformMatrix3x4dv
cglUniformMatrix4dv = GetglUniformMatrix4dv
cglUniformMatrix4x2dv = GetglUniformMatrix4x2dv
cglUniformMatrix4x3dv = GetglUniformMatrix4x3dv
cglUniformSubroutinesuiv = GetglUniformSubroutinesuiv


cdef void glBeginQueryIndexed(GLenum target, GLuint index, GLuint id):
    cglBeginQueryIndexed(target, index, id)

cdef void glBindTransformFeedback(GLenum target, GLuint id):
    cglBindTransformFeedback(target, id)

cdef void glBlendEquationSeparatei(GLuint buf, GLenum modeRGB, GLenum modeAlpha):
    cglBlendEquationSeparatei(buf, modeRGB, modeAlpha)

cdef void glBlendEquationi(GLuint buf, GLenum mode):
    cglBlendEquationi(buf, mode)

cdef void glBlendFuncSeparatei(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha):
    cglBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha)

cdef void glBlendFunci(GLuint buf, GLenum src, GLenum dst):
    cglBlendFunci(buf, src, dst)

cdef void glDeleteTransformFeedbacks(GLsizei n, const GLuint *ids):
    cglDeleteTransformFeedbacks(n, ids)

cdef void glDrawArraysIndirect(GLenum mode, const void *indirect):
    cglDrawArraysIndirect(mode, indirect)

cdef void glDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect):
    cglDrawElementsIndirect(mode, type, indirect)

cdef void glDrawTransformFeedback(GLenum mode, GLuint id):
    cglDrawTransformFeedback(mode, id)

cdef void glDrawTransformFeedbackStream(GLenum mode, GLuint id, GLuint stream):
    cglDrawTransformFeedbackStream(mode, id, stream)

cdef void glEndQueryIndexed(GLenum target, GLuint index):
    cglEndQueryIndexed(target, index)

cdef void glGenTransformFeedbacks(GLsizei n, GLuint *ids):
    cglGenTransformFeedbacks(n, ids)

cdef void glGetActiveSubroutineName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    cglGetActiveSubroutineName(program, shadertype, index, bufSize, length, name)

cdef void glGetActiveSubroutineUniformName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    cglGetActiveSubroutineUniformName(program, shadertype, index, bufSize, length, name)

cdef void glGetActiveSubroutineUniformiv(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values):
    cglGetActiveSubroutineUniformiv(program, shadertype, index, pname, values)

cdef void glGetProgramStageiv(GLuint program, GLenum shadertype, GLenum pname, GLint *values):
    cglGetProgramStageiv(program, shadertype, pname, values)

cdef void glGetQueryIndexediv(GLenum target, GLuint index, GLenum pname, GLint *params):
    cglGetQueryIndexediv(target, index, pname, params)

cdef GLuint glGetSubroutineIndex(GLuint program, GLenum shadertype, const GLchar *name):
    cglGetSubroutineIndex(program, shadertype, name)

cdef GLint glGetSubroutineUniformLocation(GLuint program, GLenum shadertype, const GLchar *name):
    cglGetSubroutineUniformLocation(program, shadertype, name)

cdef void glGetUniformSubroutineuiv(GLenum shadertype, GLint location, GLuint *params):
    cglGetUniformSubroutineuiv(shadertype, location, params)

cdef void glGetUniformdv(GLuint program, GLint location, GLdouble *params):
    cglGetUniformdv(program, location, params)

cdef GLboolean glIsTransformFeedback(GLuint id):
    cglIsTransformFeedback(id)

cdef void glMinSampleShading(GLfloat value):
    cglMinSampleShading(value)

cdef void glPatchParameterfv(GLenum pname, const GLfloat *values):
    cglPatchParameterfv(pname, values)

cdef void glPatchParameteri(GLenum pname, GLint value):
    cglPatchParameteri(pname, value)

cdef void glPauseTransformFeedback():
    cglPauseTransformFeedback()

cdef void glResumeTransformFeedback():
    cglResumeTransformFeedback()

cdef void glUniform1d(GLint location, GLdouble x):
    cglUniform1d(location, x)

cdef void glUniform1dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform1dv(location, count, value)

cdef void glUniform2d(GLint location, GLdouble x, GLdouble y):
    cglUniform2d(location, x, y)

cdef void glUniform2dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform2dv(location, count, value)

cdef void glUniform3d(GLint location, GLdouble x, GLdouble y, GLdouble z):
    cglUniform3d(location, x, y, z)

cdef void glUniform3dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform3dv(location, count, value)

cdef void glUniform4d(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglUniform4d(location, x, y, z, w)

cdef void glUniform4dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform4dv(location, count, value)

cdef void glUniformMatrix2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix2dv(location, count, transpose, value)

cdef void glUniformMatrix2x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix2x3dv(location, count, transpose, value)

cdef void glUniformMatrix2x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix2x4dv(location, count, transpose, value)

cdef void glUniformMatrix3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix3dv(location, count, transpose, value)

cdef void glUniformMatrix3x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix3x2dv(location, count, transpose, value)

cdef void glUniformMatrix3x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix3x4dv(location, count, transpose, value)

cdef void glUniformMatrix4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix4dv(location, count, transpose, value)

cdef void glUniformMatrix4x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix4x2dv(location, count, transpose, value)

cdef void glUniformMatrix4x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix4x3dv(location, count, transpose, value)

cdef void glUniformSubroutinesuiv(GLenum shadertype, GLsizei count, const GLuint *indices):
    cglUniformSubroutinesuiv(shadertype, count, indices)
