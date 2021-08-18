# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_SAMPLE_SHADING = 0x8C36
cdef GLenum GL_MIN_SAMPLE_SHADING_VALUE = 0x8C37
cdef GLenum GL_MIN_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5E
cdef GLenum GL_MAX_PROGRAM_TEXTURE_GATHER_OFFSET = 0x8E5F
cdef GLenum GL_TEXTURE_CUBE_MAP_ARRAY = 0x9009
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP_ARRAY = 0x900A
cdef GLenum GL_PROXY_TEXTURE_CUBE_MAP_ARRAY = 0x900B
cdef GLenum GL_SAMPLER_CUBE_MAP_ARRAY = 0x900C
cdef GLenum GL_SAMPLER_CUBE_MAP_ARRAY_SHADOW = 0x900D
cdef GLenum GL_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900E
cdef GLenum GL_UNSIGNED_INT_SAMPLER_CUBE_MAP_ARRAY = 0x900F
cdef GLenum GL_DRAW_INDIRECT_BUFFER = 0x8F3F
cdef GLenum GL_DRAW_INDIRECT_BUFFER_BINDING = 0x8F43
cdef GLenum GL_GEOMETRY_SHADER_INVOCATIONS = 0x887F
cdef GLenum GL_MAX_GEOMETRY_SHADER_INVOCATIONS = 0x8E5A
cdef GLenum GL_MIN_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5B
cdef GLenum GL_MAX_FRAGMENT_INTERPOLATION_OFFSET = 0x8E5C
cdef GLenum GL_FRAGMENT_INTERPOLATION_OFFSET_BITS = 0x8E5D
cdef GLenum GL_MAX_VERTEX_STREAMS = 0x8E71
cdef GLenum GL_DOUBLE_VEC2 = 0x8FFC
cdef GLenum GL_DOUBLE_VEC3 = 0x8FFD
cdef GLenum GL_DOUBLE_VEC4 = 0x8FFE
cdef GLenum GL_DOUBLE_MAT2 = 0x8F46
cdef GLenum GL_DOUBLE_MAT3 = 0x8F47
cdef GLenum GL_DOUBLE_MAT4 = 0x8F48
cdef GLenum GL_DOUBLE_MAT2x3 = 0x8F49
cdef GLenum GL_DOUBLE_MAT2x4 = 0x8F4A
cdef GLenum GL_DOUBLE_MAT3x2 = 0x8F4B
cdef GLenum GL_DOUBLE_MAT3x4 = 0x8F4C
cdef GLenum GL_DOUBLE_MAT4x2 = 0x8F4D
cdef GLenum GL_DOUBLE_MAT4x3 = 0x8F4E
cdef GLenum GL_ACTIVE_SUBROUTINES = 0x8DE5
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORMS = 0x8DE6
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORM_LOCATIONS = 0x8E47
cdef GLenum GL_ACTIVE_SUBROUTINE_MAX_LENGTH = 0x8E48
cdef GLenum GL_ACTIVE_SUBROUTINE_UNIFORM_MAX_LENGTH = 0x8E49
cdef GLenum GL_MAX_SUBROUTINES = 0x8DE7
cdef GLenum GL_MAX_SUBROUTINE_UNIFORM_LOCATIONS = 0x8DE8
cdef GLenum GL_NUM_COMPATIBLE_SUBROUTINES = 0x8E4A
cdef GLenum GL_COMPATIBLE_SUBROUTINES = 0x8E4B
cdef GLenum GL_PATCHES = 0x000E
cdef GLenum GL_PATCH_VERTICES = 0x8E72
cdef GLenum GL_PATCH_DEFAULT_INNER_LEVEL = 0x8E73
cdef GLenum GL_PATCH_DEFAULT_OUTER_LEVEL = 0x8E74
cdef GLenum GL_TESS_CONTROL_OUTPUT_VERTICES = 0x8E75
cdef GLenum GL_TESS_GEN_MODE = 0x8E76
cdef GLenum GL_TESS_GEN_SPACING = 0x8E77
cdef GLenum GL_TESS_GEN_VERTEX_ORDER = 0x8E78
cdef GLenum GL_TESS_GEN_POINT_MODE = 0x8E79
cdef GLenum GL_ISOLINES = 0x8E7A
cdef GLenum GL_QUADS = 0x0007
cdef GLenum GL_FRACTIONAL_ODD = 0x8E7B
cdef GLenum GL_FRACTIONAL_EVEN = 0x8E7C
cdef GLenum GL_MAX_PATCH_VERTICES = 0x8E7D
cdef GLenum GL_MAX_TESS_GEN_LEVEL = 0x8E7E
cdef GLenum GL_MAX_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E7F
cdef GLenum GL_MAX_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E80
cdef GLenum GL_MAX_TESS_CONTROL_TEXTURE_IMAGE_UNITS = 0x8E81
cdef GLenum GL_MAX_TESS_EVALUATION_TEXTURE_IMAGE_UNITS = 0x8E82
cdef GLenum GL_MAX_TESS_CONTROL_OUTPUT_COMPONENTS = 0x8E83
cdef GLenum GL_MAX_TESS_PATCH_COMPONENTS = 0x8E84
cdef GLenum GL_MAX_TESS_CONTROL_TOTAL_OUTPUT_COMPONENTS = 0x8E85
cdef GLenum GL_MAX_TESS_EVALUATION_OUTPUT_COMPONENTS = 0x8E86
cdef GLenum GL_MAX_TESS_CONTROL_UNIFORM_BLOCKS = 0x8E89
cdef GLenum GL_MAX_TESS_EVALUATION_UNIFORM_BLOCKS = 0x8E8A
cdef GLenum GL_MAX_TESS_CONTROL_INPUT_COMPONENTS = 0x886C
cdef GLenum GL_MAX_TESS_EVALUATION_INPUT_COMPONENTS = 0x886D
cdef GLenum GL_MAX_COMBINED_TESS_CONTROL_UNIFORM_COMPONENTS = 0x8E1E
cdef GLenum GL_MAX_COMBINED_TESS_EVALUATION_UNIFORM_COMPONENTS = 0x8E1F
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_CONTROL_SHADER = 0x84F0
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x84F1
cdef GLenum GL_TESS_EVALUATION_SHADER = 0x8E87
cdef GLenum GL_TESS_CONTROL_SHADER = 0x8E88
cdef GLenum GL_TRANSFORM_FEEDBACK = 0x8E22
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_PAUSED = 0x8E23
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_ACTIVE = 0x8E24
cdef GLenum GL_TRANSFORM_FEEDBACK_BINDING = 0x8E25
cdef GLenum GL_MAX_TRANSFORM_FEEDBACK_BUFFERS = 0x8E70
cdef GLenum GL_MAX_VERTEX_STREAMS = 0x8E71

ctypedef void (*GL_MIN_SAMPLE_SHADING)(GLfloat value)
ctypedef void (*GL_BLEND_EQUATIONI)(GLuint buf, GLenum mode)
ctypedef void (*GL_BLEND_EQUATION_SEPARATEI)(GLuint buf, GLenum modeRGB, GLenum modeAlpha)
ctypedef void (*GL_BLEND_FUNCI)(GLuint buf, GLenum src, GLenum dst)
ctypedef void (*GL_BLEND_FUNC_SEPARATEI)(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha)
ctypedef void (*GL_DRAW_ARRAYS_INDIRECT)(GLenum mode, const void *indirect)
ctypedef void (*GL_DRAW_ELEMENTS_INDIRECT)(GLenum mode, GLenum type, const void *indirect)
ctypedef void (*GL_UNIFORM1D)(GLint location, GLdouble x)
ctypedef void (*GL_UNIFORM2D)(GLint location, GLdouble x, GLdouble y)
ctypedef void (*GL_UNIFORM3D)(GLint location, GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*GL_UNIFORM4D)(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*GL_UNIFORM1DV)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*GL_UNIFORM2DV)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*GL_UNIFORM3DV)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*GL_UNIFORM4DV)(GLint location, GLsizei count, const GLdouble *value)
ctypedef void (*GL_UNIFORM_MATRIX2DV)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_UNIFORM_MATRIX3DV)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_UNIFORM_MATRIX4DV)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_UNIFORM_MATRIX2X3DV)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_UNIFORM_MATRIX2X4DV)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_UNIFORM_MATRIX3X2DV)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_UNIFORM_MATRIX3X4DV)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_UNIFORM_MATRIX4X2DV)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_UNIFORM_MATRIX4X3DV)(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value)
ctypedef void (*GL_GET_UNIFORMDV)(GLuint program, GLint location, GLdouble *params)
ctypedef GLint (*GL_GET_SUBROUTINE_UNIFORM_LOCATION)(GLuint program, GLenum shadertype, const GLchar *name)
ctypedef GLuint (*GL_GET_SUBROUTINE_INDEX)(GLuint program, GLenum shadertype, const GLchar *name)
ctypedef void (*GL_GET_ACTIVE_SUBROUTINE_UNIFORMIV)(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values)
ctypedef void (*GL_GET_ACTIVE_SUBROUTINE_UNIFORM_NAME)(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
ctypedef void (*GL_GET_ACTIVE_SUBROUTINE_NAME)(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
ctypedef void (*GL_UNIFORM_SUBROUTINESUIV)(GLenum shadertype, GLsizei count, const GLuint *indices)
ctypedef void (*GL_GET_UNIFORM_SUBROUTINEUIV)(GLenum shadertype, GLint location, GLuint *params)
ctypedef void (*GL_GET_PROGRAM_STAGEIV)(GLuint program, GLenum shadertype, GLenum pname, GLint *values)
ctypedef void (*GL_PATCH_PARAMETERI)(GLenum pname, GLint value)
ctypedef void (*GL_PATCH_PARAMETERFV)(GLenum pname, const GLfloat *values)
ctypedef void (*GL_BIND_TRANSFORM_FEEDBACK)(GLenum target, GLuint id)
ctypedef void (*GL_DELETE_TRANSFORM_FEEDBACKS)(GLsizei n, const GLuint *ids)
ctypedef void (*GL_GEN_TRANSFORM_FEEDBACKS)(GLsizei n, GLuint *ids)
ctypedef GLboolean (*GL_IS_TRANSFORM_FEEDBACK)(GLuint id)
ctypedef void (*GL_PAUSE_TRANSFORM_FEEDBACK)()
ctypedef void (*GL_RESUME_TRANSFORM_FEEDBACK)()
ctypedef void (*GL_DRAW_TRANSFORM_FEEDBACK)(GLenum mode, GLuint id)
ctypedef void (*GL_DRAW_TRANSFORM_FEEDBACK_STREAM)(GLenum mode, GLuint id, GLuint stream)
ctypedef void (*GL_BEGIN_QUERY_INDEXED)(GLenum target, GLuint index, GLuint id)
ctypedef void (*GL_END_QUERY_INDEXED)(GLenum target, GLuint index)
ctypedef void (*GL_GET_QUERY_INDEXEDIV)(GLenum target, GLuint index, GLenum pname, GLint *params)

cdef GL_MIN_SAMPLE_SHADING cglMinSampleShading = NULL
cdef GL_BLEND_EQUATIONI cglBlendEquationi = NULL
cdef GL_BLEND_EQUATION_SEPARATEI cglBlendEquationSeparatei = NULL
cdef GL_BLEND_FUNCI cglBlendFunci = NULL
cdef GL_BLEND_FUNC_SEPARATEI cglBlendFuncSeparatei = NULL
cdef GL_DRAW_ARRAYS_INDIRECT cglDrawArraysIndirect = NULL
cdef GL_DRAW_ELEMENTS_INDIRECT cglDrawElementsIndirect = NULL
cdef GL_UNIFORM1D cglUniform1d = NULL
cdef GL_UNIFORM2D cglUniform2d = NULL
cdef GL_UNIFORM3D cglUniform3d = NULL
cdef GL_UNIFORM4D cglUniform4d = NULL
cdef GL_UNIFORM1DV cglUniform1dv = NULL
cdef GL_UNIFORM2DV cglUniform2dv = NULL
cdef GL_UNIFORM3DV cglUniform3dv = NULL
cdef GL_UNIFORM4DV cglUniform4dv = NULL
cdef GL_UNIFORM_MATRIX2DV cglUniformMatrix2dv = NULL
cdef GL_UNIFORM_MATRIX3DV cglUniformMatrix3dv = NULL
cdef GL_UNIFORM_MATRIX4DV cglUniformMatrix4dv = NULL
cdef GL_UNIFORM_MATRIX2X3DV cglUniformMatrix2x3dv = NULL
cdef GL_UNIFORM_MATRIX2X4DV cglUniformMatrix2x4dv = NULL
cdef GL_UNIFORM_MATRIX3X2DV cglUniformMatrix3x2dv = NULL
cdef GL_UNIFORM_MATRIX3X4DV cglUniformMatrix3x4dv = NULL
cdef GL_UNIFORM_MATRIX4X2DV cglUniformMatrix4x2dv = NULL
cdef GL_UNIFORM_MATRIX4X3DV cglUniformMatrix4x3dv = NULL
cdef GL_GET_UNIFORMDV cglGetUniformdv = NULL
cdef GL_GET_SUBROUTINE_UNIFORM_LOCATION cglGetSubroutineUniformLocation = NULL
cdef GL_GET_SUBROUTINE_INDEX cglGetSubroutineIndex = NULL
cdef GL_GET_ACTIVE_SUBROUTINE_UNIFORMIV cglGetActiveSubroutineUniformiv = NULL
cdef GL_GET_ACTIVE_SUBROUTINE_UNIFORM_NAME cglGetActiveSubroutineUniformName = NULL
cdef GL_GET_ACTIVE_SUBROUTINE_NAME cglGetActiveSubroutineName = NULL
cdef GL_UNIFORM_SUBROUTINESUIV cglUniformSubroutinesuiv = NULL
cdef GL_GET_UNIFORM_SUBROUTINEUIV cglGetUniformSubroutineuiv = NULL
cdef GL_GET_PROGRAM_STAGEIV cglGetProgramStageiv = NULL
cdef GL_PATCH_PARAMETERI cglPatchParameteri = NULL
cdef GL_PATCH_PARAMETERFV cglPatchParameterfv = NULL
cdef GL_BIND_TRANSFORM_FEEDBACK cglBindTransformFeedback = NULL
cdef GL_DELETE_TRANSFORM_FEEDBACKS cglDeleteTransformFeedbacks = NULL
cdef GL_GEN_TRANSFORM_FEEDBACKS cglGenTransformFeedbacks = NULL
cdef GL_IS_TRANSFORM_FEEDBACK cglIsTransformFeedback = NULL
cdef GL_PAUSE_TRANSFORM_FEEDBACK cglPauseTransformFeedback = NULL
cdef GL_RESUME_TRANSFORM_FEEDBACK cglResumeTransformFeedback = NULL
cdef GL_DRAW_TRANSFORM_FEEDBACK cglDrawTransformFeedback = NULL
cdef GL_DRAW_TRANSFORM_FEEDBACK_STREAM cglDrawTransformFeedbackStream = NULL
cdef GL_BEGIN_QUERY_INDEXED cglBeginQueryIndexed = NULL
cdef GL_END_QUERY_INDEXED cglEndQueryIndexed = NULL
cdef GL_GET_QUERY_INDEXEDIV cglGetQueryIndexediv = NULL


cdef void GetglMinSampleShading(GLfloat value):
    global cglMinSampleShading
    cglMinSampleShading = <GL_MIN_SAMPLE_SHADING>getFunction(b"glMinSampleShading")
    cglMinSampleShading(value)

cdef void GetglBlendEquationi(GLuint buf, GLenum mode):
    global cglBlendEquationi
    cglBlendEquationi = <GL_BLEND_EQUATIONI>getFunction(b"glBlendEquationi")
    cglBlendEquationi(buf, mode)

cdef void GetglBlendEquationSeparatei(GLuint buf, GLenum modeRGB, GLenum modeAlpha):
    global cglBlendEquationSeparatei
    cglBlendEquationSeparatei = <GL_BLEND_EQUATION_SEPARATEI>getFunction(b"glBlendEquationSeparatei")
    cglBlendEquationSeparatei(buf, modeRGB, modeAlpha)

cdef void GetglBlendFunci(GLuint buf, GLenum src, GLenum dst):
    global cglBlendFunci
    cglBlendFunci = <GL_BLEND_FUNCI>getFunction(b"glBlendFunci")
    cglBlendFunci(buf, src, dst)

cdef void GetglBlendFuncSeparatei(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha):
    global cglBlendFuncSeparatei
    cglBlendFuncSeparatei = <GL_BLEND_FUNC_SEPARATEI>getFunction(b"glBlendFuncSeparatei")
    cglBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha)

cdef void GetglDrawArraysIndirect(GLenum mode, const void *indirect):
    global cglDrawArraysIndirect
    cglDrawArraysIndirect = <GL_DRAW_ARRAYS_INDIRECT>getFunction(b"glDrawArraysIndirect")
    cglDrawArraysIndirect(mode, indirect)

cdef void GetglDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect):
    global cglDrawElementsIndirect
    cglDrawElementsIndirect = <GL_DRAW_ELEMENTS_INDIRECT>getFunction(b"glDrawElementsIndirect")
    cglDrawElementsIndirect(mode, type, indirect)

cdef void GetglUniform1d(GLint location, GLdouble x):
    global cglUniform1d
    cglUniform1d = <GL_UNIFORM1D>getFunction(b"glUniform1d")
    cglUniform1d(location, x)

cdef void GetglUniform2d(GLint location, GLdouble x, GLdouble y):
    global cglUniform2d
    cglUniform2d = <GL_UNIFORM2D>getFunction(b"glUniform2d")
    cglUniform2d(location, x, y)

cdef void GetglUniform3d(GLint location, GLdouble x, GLdouble y, GLdouble z):
    global cglUniform3d
    cglUniform3d = <GL_UNIFORM3D>getFunction(b"glUniform3d")
    cglUniform3d(location, x, y, z)

cdef void GetglUniform4d(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglUniform4d
    cglUniform4d = <GL_UNIFORM4D>getFunction(b"glUniform4d")
    cglUniform4d(location, x, y, z, w)

cdef void GetglUniform1dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform1dv
    cglUniform1dv = <GL_UNIFORM1DV>getFunction(b"glUniform1dv")
    cglUniform1dv(location, count, value)

cdef void GetglUniform2dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform2dv
    cglUniform2dv = <GL_UNIFORM2DV>getFunction(b"glUniform2dv")
    cglUniform2dv(location, count, value)

cdef void GetglUniform3dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform3dv
    cglUniform3dv = <GL_UNIFORM3DV>getFunction(b"glUniform3dv")
    cglUniform3dv(location, count, value)

cdef void GetglUniform4dv(GLint location, GLsizei count, const GLdouble *value):
    global cglUniform4dv
    cglUniform4dv = <GL_UNIFORM4DV>getFunction(b"glUniform4dv")
    cglUniform4dv(location, count, value)

cdef void GetglUniformMatrix2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix2dv
    cglUniformMatrix2dv = <GL_UNIFORM_MATRIX2DV>getFunction(b"glUniformMatrix2dv")
    cglUniformMatrix2dv(location, count, transpose, value)

cdef void GetglUniformMatrix3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix3dv
    cglUniformMatrix3dv = <GL_UNIFORM_MATRIX3DV>getFunction(b"glUniformMatrix3dv")
    cglUniformMatrix3dv(location, count, transpose, value)

cdef void GetglUniformMatrix4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix4dv
    cglUniformMatrix4dv = <GL_UNIFORM_MATRIX4DV>getFunction(b"glUniformMatrix4dv")
    cglUniformMatrix4dv(location, count, transpose, value)

cdef void GetglUniformMatrix2x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix2x3dv
    cglUniformMatrix2x3dv = <GL_UNIFORM_MATRIX2X3DV>getFunction(b"glUniformMatrix2x3dv")
    cglUniformMatrix2x3dv(location, count, transpose, value)

cdef void GetglUniformMatrix2x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix2x4dv
    cglUniformMatrix2x4dv = <GL_UNIFORM_MATRIX2X4DV>getFunction(b"glUniformMatrix2x4dv")
    cglUniformMatrix2x4dv(location, count, transpose, value)

cdef void GetglUniformMatrix3x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix3x2dv
    cglUniformMatrix3x2dv = <GL_UNIFORM_MATRIX3X2DV>getFunction(b"glUniformMatrix3x2dv")
    cglUniformMatrix3x2dv(location, count, transpose, value)

cdef void GetglUniformMatrix3x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix3x4dv
    cglUniformMatrix3x4dv = <GL_UNIFORM_MATRIX3X4DV>getFunction(b"glUniformMatrix3x4dv")
    cglUniformMatrix3x4dv(location, count, transpose, value)

cdef void GetglUniformMatrix4x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix4x2dv
    cglUniformMatrix4x2dv = <GL_UNIFORM_MATRIX4X2DV>getFunction(b"glUniformMatrix4x2dv")
    cglUniformMatrix4x2dv(location, count, transpose, value)

cdef void GetglUniformMatrix4x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    global cglUniformMatrix4x3dv
    cglUniformMatrix4x3dv = <GL_UNIFORM_MATRIX4X3DV>getFunction(b"glUniformMatrix4x3dv")
    cglUniformMatrix4x3dv(location, count, transpose, value)

cdef void GetglGetUniformdv(GLuint program, GLint location, GLdouble *params):
    global cglGetUniformdv
    cglGetUniformdv = <GL_GET_UNIFORMDV>getFunction(b"glGetUniformdv")
    cglGetUniformdv(program, location, params)

cdef GLint GetglGetSubroutineUniformLocation(GLuint program, GLenum shadertype, const GLchar *name):
    global cglGetSubroutineUniformLocation
    cglGetSubroutineUniformLocation = <GL_GET_SUBROUTINE_UNIFORM_LOCATION>getFunction(b"glGetSubroutineUniformLocation")
    cglGetSubroutineUniformLocation(program, shadertype, name)

cdef GLuint GetglGetSubroutineIndex(GLuint program, GLenum shadertype, const GLchar *name):
    global cglGetSubroutineIndex
    cglGetSubroutineIndex = <GL_GET_SUBROUTINE_INDEX>getFunction(b"glGetSubroutineIndex")
    cglGetSubroutineIndex(program, shadertype, name)

cdef void GetglGetActiveSubroutineUniformiv(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values):
    global cglGetActiveSubroutineUniformiv
    cglGetActiveSubroutineUniformiv = <GL_GET_ACTIVE_SUBROUTINE_UNIFORMIV>getFunction(b"glGetActiveSubroutineUniformiv")
    cglGetActiveSubroutineUniformiv(program, shadertype, index, pname, values)

cdef void GetglGetActiveSubroutineUniformName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    global cglGetActiveSubroutineUniformName
    cglGetActiveSubroutineUniformName = <GL_GET_ACTIVE_SUBROUTINE_UNIFORM_NAME>getFunction(b"glGetActiveSubroutineUniformName")
    cglGetActiveSubroutineUniformName(program, shadertype, index, bufSize, length, name)

cdef void GetglGetActiveSubroutineName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    global cglGetActiveSubroutineName
    cglGetActiveSubroutineName = <GL_GET_ACTIVE_SUBROUTINE_NAME>getFunction(b"glGetActiveSubroutineName")
    cglGetActiveSubroutineName(program, shadertype, index, bufSize, length, name)

cdef void GetglUniformSubroutinesuiv(GLenum shadertype, GLsizei count, const GLuint *indices):
    global cglUniformSubroutinesuiv
    cglUniformSubroutinesuiv = <GL_UNIFORM_SUBROUTINESUIV>getFunction(b"glUniformSubroutinesuiv")
    cglUniformSubroutinesuiv(shadertype, count, indices)

cdef void GetglGetUniformSubroutineuiv(GLenum shadertype, GLint location, GLuint *params):
    global cglGetUniformSubroutineuiv
    cglGetUniformSubroutineuiv = <GL_GET_UNIFORM_SUBROUTINEUIV>getFunction(b"glGetUniformSubroutineuiv")
    cglGetUniformSubroutineuiv(shadertype, location, params)

cdef void GetglGetProgramStageiv(GLuint program, GLenum shadertype, GLenum pname, GLint *values):
    global cglGetProgramStageiv
    cglGetProgramStageiv = <GL_GET_PROGRAM_STAGEIV>getFunction(b"glGetProgramStageiv")
    cglGetProgramStageiv(program, shadertype, pname, values)

cdef void GetglPatchParameteri(GLenum pname, GLint value):
    global cglPatchParameteri
    cglPatchParameteri = <GL_PATCH_PARAMETERI>getFunction(b"glPatchParameteri")
    cglPatchParameteri(pname, value)

cdef void GetglPatchParameterfv(GLenum pname, const GLfloat *values):
    global cglPatchParameterfv
    cglPatchParameterfv = <GL_PATCH_PARAMETERFV>getFunction(b"glPatchParameterfv")
    cglPatchParameterfv(pname, values)

cdef void GetglBindTransformFeedback(GLenum target, GLuint id):
    global cglBindTransformFeedback
    cglBindTransformFeedback = <GL_BIND_TRANSFORM_FEEDBACK>getFunction(b"glBindTransformFeedback")
    cglBindTransformFeedback(target, id)

cdef void GetglDeleteTransformFeedbacks(GLsizei n, const GLuint *ids):
    global cglDeleteTransformFeedbacks
    cglDeleteTransformFeedbacks = <GL_DELETE_TRANSFORM_FEEDBACKS>getFunction(b"glDeleteTransformFeedbacks")
    cglDeleteTransformFeedbacks(n, ids)

cdef void GetglGenTransformFeedbacks(GLsizei n, GLuint *ids):
    global cglGenTransformFeedbacks
    cglGenTransformFeedbacks = <GL_GEN_TRANSFORM_FEEDBACKS>getFunction(b"glGenTransformFeedbacks")
    cglGenTransformFeedbacks(n, ids)

cdef GLboolean GetglIsTransformFeedback(GLuint id):
    global cglIsTransformFeedback
    cglIsTransformFeedback = <GL_IS_TRANSFORM_FEEDBACK>getFunction(b"glIsTransformFeedback")
    cglIsTransformFeedback(id)

cdef void GetglPauseTransformFeedback():
    global cglPauseTransformFeedback
    cglPauseTransformFeedback = <GL_PAUSE_TRANSFORM_FEEDBACK>getFunction(b"glPauseTransformFeedback")
    cglPauseTransformFeedback()

cdef void GetglResumeTransformFeedback():
    global cglResumeTransformFeedback
    cglResumeTransformFeedback = <GL_RESUME_TRANSFORM_FEEDBACK>getFunction(b"glResumeTransformFeedback")
    cglResumeTransformFeedback()

cdef void GetglDrawTransformFeedback(GLenum mode, GLuint id):
    global cglDrawTransformFeedback
    cglDrawTransformFeedback = <GL_DRAW_TRANSFORM_FEEDBACK>getFunction(b"glDrawTransformFeedback")
    cglDrawTransformFeedback(mode, id)

cdef void GetglDrawTransformFeedbackStream(GLenum mode, GLuint id, GLuint stream):
    global cglDrawTransformFeedbackStream
    cglDrawTransformFeedbackStream = <GL_DRAW_TRANSFORM_FEEDBACK_STREAM>getFunction(b"glDrawTransformFeedbackStream")
    cglDrawTransformFeedbackStream(mode, id, stream)

cdef void GetglBeginQueryIndexed(GLenum target, GLuint index, GLuint id):
    global cglBeginQueryIndexed
    cglBeginQueryIndexed = <GL_BEGIN_QUERY_INDEXED>getFunction(b"glBeginQueryIndexed")
    cglBeginQueryIndexed(target, index, id)

cdef void GetglEndQueryIndexed(GLenum target, GLuint index):
    global cglEndQueryIndexed
    cglEndQueryIndexed = <GL_END_QUERY_INDEXED>getFunction(b"glEndQueryIndexed")
    cglEndQueryIndexed(target, index)

cdef void GetglGetQueryIndexediv(GLenum target, GLuint index, GLenum pname, GLint *params):
    global cglGetQueryIndexediv
    cglGetQueryIndexediv = <GL_GET_QUERY_INDEXEDIV>getFunction(b"glGetQueryIndexediv")
    cglGetQueryIndexediv(target, index, pname, params)

cglMinSampleShading = GetglMinSampleShading
cglBlendEquationi = GetglBlendEquationi
cglBlendEquationSeparatei = GetglBlendEquationSeparatei
cglBlendFunci = GetglBlendFunci
cglBlendFuncSeparatei = GetglBlendFuncSeparatei
cglDrawArraysIndirect = GetglDrawArraysIndirect
cglDrawElementsIndirect = GetglDrawElementsIndirect
cglUniform1d = GetglUniform1d
cglUniform2d = GetglUniform2d
cglUniform3d = GetglUniform3d
cglUniform4d = GetglUniform4d
cglUniform1dv = GetglUniform1dv
cglUniform2dv = GetglUniform2dv
cglUniform3dv = GetglUniform3dv
cglUniform4dv = GetglUniform4dv
cglUniformMatrix2dv = GetglUniformMatrix2dv
cglUniformMatrix3dv = GetglUniformMatrix3dv
cglUniformMatrix4dv = GetglUniformMatrix4dv
cglUniformMatrix2x3dv = GetglUniformMatrix2x3dv
cglUniformMatrix2x4dv = GetglUniformMatrix2x4dv
cglUniformMatrix3x2dv = GetglUniformMatrix3x2dv
cglUniformMatrix3x4dv = GetglUniformMatrix3x4dv
cglUniformMatrix4x2dv = GetglUniformMatrix4x2dv
cglUniformMatrix4x3dv = GetglUniformMatrix4x3dv
cglGetUniformdv = GetglGetUniformdv
cglGetSubroutineUniformLocation = GetglGetSubroutineUniformLocation
cglGetSubroutineIndex = GetglGetSubroutineIndex
cglGetActiveSubroutineUniformiv = GetglGetActiveSubroutineUniformiv
cglGetActiveSubroutineUniformName = GetglGetActiveSubroutineUniformName
cglGetActiveSubroutineName = GetglGetActiveSubroutineName
cglUniformSubroutinesuiv = GetglUniformSubroutinesuiv
cglGetUniformSubroutineuiv = GetglGetUniformSubroutineuiv
cglGetProgramStageiv = GetglGetProgramStageiv
cglPatchParameteri = GetglPatchParameteri
cglPatchParameterfv = GetglPatchParameterfv
cglBindTransformFeedback = GetglBindTransformFeedback
cglDeleteTransformFeedbacks = GetglDeleteTransformFeedbacks
cglGenTransformFeedbacks = GetglGenTransformFeedbacks
cglIsTransformFeedback = GetglIsTransformFeedback
cglPauseTransformFeedback = GetglPauseTransformFeedback
cglResumeTransformFeedback = GetglResumeTransformFeedback
cglDrawTransformFeedback = GetglDrawTransformFeedback
cglDrawTransformFeedbackStream = GetglDrawTransformFeedbackStream
cglBeginQueryIndexed = GetglBeginQueryIndexed
cglEndQueryIndexed = GetglEndQueryIndexed
cglGetQueryIndexediv = GetglGetQueryIndexediv


cpdef void glMinSampleShading(GLfloat value):
    cglMinSampleShading(value)

cpdef void glBlendEquationi(GLuint buf, GLenum mode):
    cglBlendEquationi(buf, mode)

cpdef void glBlendEquationSeparatei(GLuint buf, GLenum modeRGB, GLenum modeAlpha):
    cglBlendEquationSeparatei(buf, modeRGB, modeAlpha)

cpdef void glBlendFunci(GLuint buf, GLenum src, GLenum dst):
    cglBlendFunci(buf, src, dst)

cpdef void glBlendFuncSeparatei(GLuint buf, GLenum srcRGB, GLenum dstRGB, GLenum srcAlpha, GLenum dstAlpha):
    cglBlendFuncSeparatei(buf, srcRGB, dstRGB, srcAlpha, dstAlpha)

cpdef void glDrawArraysIndirect(GLenum mode, const void *indirect):
    cglDrawArraysIndirect(mode, indirect)

cpdef void glDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect):
    cglDrawElementsIndirect(mode, type, indirect)

cpdef void glUniform1d(GLint location, GLdouble x):
    cglUniform1d(location, x)

cpdef void glUniform2d(GLint location, GLdouble x, GLdouble y):
    cglUniform2d(location, x, y)

cpdef void glUniform3d(GLint location, GLdouble x, GLdouble y, GLdouble z):
    cglUniform3d(location, x, y, z)

cpdef void glUniform4d(GLint location, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglUniform4d(location, x, y, z, w)

cpdef void glUniform1dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform1dv(location, count, value)

cpdef void glUniform2dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform2dv(location, count, value)

cpdef void glUniform3dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform3dv(location, count, value)

cpdef void glUniform4dv(GLint location, GLsizei count, const GLdouble *value):
    cglUniform4dv(location, count, value)

cpdef void glUniformMatrix2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix2dv(location, count, transpose, value)

cpdef void glUniformMatrix3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix3dv(location, count, transpose, value)

cpdef void glUniformMatrix4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix4dv(location, count, transpose, value)

cpdef void glUniformMatrix2x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix2x3dv(location, count, transpose, value)

cpdef void glUniformMatrix2x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix2x4dv(location, count, transpose, value)

cpdef void glUniformMatrix3x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix3x2dv(location, count, transpose, value)

cpdef void glUniformMatrix3x4dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix3x4dv(location, count, transpose, value)

cpdef void glUniformMatrix4x2dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix4x2dv(location, count, transpose, value)

cpdef void glUniformMatrix4x3dv(GLint location, GLsizei count, GLboolean transpose, const GLdouble *value):
    cglUniformMatrix4x3dv(location, count, transpose, value)

cpdef void glGetUniformdv(GLuint program, GLint location, GLdouble *params):
    cglGetUniformdv(program, location, params)

cpdef GLint glGetSubroutineUniformLocation(GLuint program, GLenum shadertype, const GLchar *name):
    cglGetSubroutineUniformLocation(program, shadertype, name)

cpdef GLuint glGetSubroutineIndex(GLuint program, GLenum shadertype, const GLchar *name):
    cglGetSubroutineIndex(program, shadertype, name)

cpdef void glGetActiveSubroutineUniformiv(GLuint program, GLenum shadertype, GLuint index, GLenum pname, GLint *values):
    cglGetActiveSubroutineUniformiv(program, shadertype, index, pname, values)

cpdef void glGetActiveSubroutineUniformName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    cglGetActiveSubroutineUniformName(program, shadertype, index, bufSize, length, name)

cpdef void glGetActiveSubroutineName(GLuint program, GLenum shadertype, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    cglGetActiveSubroutineName(program, shadertype, index, bufSize, length, name)

cpdef void glUniformSubroutinesuiv(GLenum shadertype, GLsizei count, const GLuint *indices):
    cglUniformSubroutinesuiv(shadertype, count, indices)

cpdef void glGetUniformSubroutineuiv(GLenum shadertype, GLint location, GLuint *params):
    cglGetUniformSubroutineuiv(shadertype, location, params)

cpdef void glGetProgramStageiv(GLuint program, GLenum shadertype, GLenum pname, GLint *values):
    cglGetProgramStageiv(program, shadertype, pname, values)

cpdef void glPatchParameteri(GLenum pname, GLint value):
    cglPatchParameteri(pname, value)

cpdef void glPatchParameterfv(GLenum pname, const GLfloat *values):
    cglPatchParameterfv(pname, values)

cpdef void glBindTransformFeedback(GLenum target, GLuint id):
    cglBindTransformFeedback(target, id)

cpdef void glDeleteTransformFeedbacks(GLsizei n, const GLuint *ids):
    cglDeleteTransformFeedbacks(n, ids)

cpdef void glGenTransformFeedbacks(GLsizei n, GLuint *ids):
    cglGenTransformFeedbacks(n, ids)

cpdef GLboolean glIsTransformFeedback(GLuint id):
    cglIsTransformFeedback(id)

cpdef void glPauseTransformFeedback():
    cglPauseTransformFeedback()

cpdef void glResumeTransformFeedback():
    cglResumeTransformFeedback()

cpdef void glDrawTransformFeedback(GLenum mode, GLuint id):
    cglDrawTransformFeedback(mode, id)

cpdef void glDrawTransformFeedbackStream(GLenum mode, GLuint id, GLuint stream):
    cglDrawTransformFeedbackStream(mode, id, stream)

cpdef void glBeginQueryIndexed(GLenum target, GLuint index, GLuint id):
    cglBeginQueryIndexed(target, index, id)

cpdef void glEndQueryIndexed(GLenum target, GLuint index):
    cglEndQueryIndexed(target, index)

cpdef void glGetQueryIndexediv(GLenum target, GLuint index, GLenum pname, GLint *params):
    cglGetQueryIndexediv(target, index, pname, params)
