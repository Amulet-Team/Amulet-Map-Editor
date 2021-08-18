# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 0x88FE
cdef GLenum GL_SRC1_COLOR = 0x88F9
cdef GLenum GL_ONE_MINUS_SRC1_COLOR = 0x88FA
cdef GLenum GL_ONE_MINUS_SRC1_ALPHA = 0x88FB
cdef GLenum GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = 0x88FC
cdef GLenum GL_ANY_SAMPLES_PASSED = 0x8C2F
cdef GLenum GL_SAMPLER_BINDING = 0x8919
cdef GLenum GL_RGB10_A2UI = 0x906F
cdef GLenum GL_TEXTURE_SWIZZLE_R = 0x8E42
cdef GLenum GL_TEXTURE_SWIZZLE_G = 0x8E43
cdef GLenum GL_TEXTURE_SWIZZLE_B = 0x8E44
cdef GLenum GL_TEXTURE_SWIZZLE_A = 0x8E45
cdef GLenum GL_TEXTURE_SWIZZLE_RGBA = 0x8E46
cdef GLenum GL_TIME_ELAPSED = 0x88BF
cdef GLenum GL_TIMESTAMP = 0x8E28
cdef GLenum GL_INT_2_10_10_10_REV = 0x8D9F

ctypedef void (*GL_BIND_FRAG_DATA_LOCATION_INDEXED)(GLuint program, GLuint colorNumber, GLuint index, const GLchar *name)
ctypedef GLint (*GL_GET_FRAG_DATA_INDEX)(GLuint program, const GLchar *name)
ctypedef void (*GL_GEN_SAMPLERS)(GLsizei count, GLuint *samplers)
ctypedef void (*GL_DELETE_SAMPLERS)(GLsizei count, const GLuint *samplers)
ctypedef GLboolean (*GL_IS_SAMPLER)(GLuint sampler)
ctypedef void (*GL_BIND_SAMPLER)(GLuint unit, GLuint sampler)
ctypedef void (*GL_SAMPLER_PARAMETERI)(GLuint sampler, GLenum pname, GLint param)
ctypedef void (*GL_SAMPLER_PARAMETERIV)(GLuint sampler, GLenum pname, const GLint *param)
ctypedef void (*GL_SAMPLER_PARAMETERF)(GLuint sampler, GLenum pname, GLfloat param)
ctypedef void (*GL_SAMPLER_PARAMETERFV)(GLuint sampler, GLenum pname, const GLfloat *param)
ctypedef void (*GL_SAMPLER_PARAMETER_IIV)(GLuint sampler, GLenum pname, const GLint *param)
ctypedef void (*GL_SAMPLER_PARAMETER_IUIV)(GLuint sampler, GLenum pname, const GLuint *param)
ctypedef void (*GL_GET_SAMPLER_PARAMETERIV)(GLuint sampler, GLenum pname, GLint *params)
ctypedef void (*GL_GET_SAMPLER_PARAMETER_IIV)(GLuint sampler, GLenum pname, GLint *params)
ctypedef void (*GL_GET_SAMPLER_PARAMETERFV)(GLuint sampler, GLenum pname, GLfloat *params)
ctypedef void (*GL_GET_SAMPLER_PARAMETER_IUIV)(GLuint sampler, GLenum pname, GLuint *params)
ctypedef void (*GL_QUERY_COUNTER)(GLuint id, GLenum target)
ctypedef void (*GL_GET_QUERY_OBJECTI64V)(GLuint id, GLenum pname, GLint64 *params)
ctypedef void (*GL_GET_QUERY_OBJECTUI64V)(GLuint id, GLenum pname, GLuint64 *params)
ctypedef void (*GL_VERTEX_ATTRIB_DIVISOR)(GLuint index, GLuint divisor)
ctypedef void (*GL_VERTEX_ATTRIB_P1UI)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*GL_VERTEX_ATTRIB_P1UIV)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*GL_VERTEX_ATTRIB_P2UI)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*GL_VERTEX_ATTRIB_P2UIV)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*GL_VERTEX_ATTRIB_P3UI)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*GL_VERTEX_ATTRIB_P3UIV)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*GL_VERTEX_ATTRIB_P4UI)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*GL_VERTEX_ATTRIB_P4UIV)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*GL_VERTEX_P2UI)(GLenum type, GLuint value)
ctypedef void (*GL_VERTEX_P2UIV)(GLenum type, const GLuint *value)
ctypedef void (*GL_VERTEX_P3UI)(GLenum type, GLuint value)
ctypedef void (*GL_VERTEX_P3UIV)(GLenum type, const GLuint *value)
ctypedef void (*GL_VERTEX_P4UI)(GLenum type, GLuint value)
ctypedef void (*GL_VERTEX_P4UIV)(GLenum type, const GLuint *value)
ctypedef void (*GL_TEX_COORD_P1UI)(GLenum type, GLuint coords)
ctypedef void (*GL_TEX_COORD_P1UIV)(GLenum type, const GLuint *coords)
ctypedef void (*GL_TEX_COORD_P2UI)(GLenum type, GLuint coords)
ctypedef void (*GL_TEX_COORD_P2UIV)(GLenum type, const GLuint *coords)
ctypedef void (*GL_TEX_COORD_P3UI)(GLenum type, GLuint coords)
ctypedef void (*GL_TEX_COORD_P3UIV)(GLenum type, const GLuint *coords)
ctypedef void (*GL_TEX_COORD_P4UI)(GLenum type, GLuint coords)
ctypedef void (*GL_TEX_COORD_P4UIV)(GLenum type, const GLuint *coords)
ctypedef void (*GL_MULTI_TEX_COORD_P1UI)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*GL_MULTI_TEX_COORD_P1UIV)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*GL_MULTI_TEX_COORD_P2UI)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*GL_MULTI_TEX_COORD_P2UIV)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*GL_MULTI_TEX_COORD_P3UI)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*GL_MULTI_TEX_COORD_P3UIV)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*GL_MULTI_TEX_COORD_P4UI)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*GL_MULTI_TEX_COORD_P4UIV)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*GL_NORMAL_P3UI)(GLenum type, GLuint coords)
ctypedef void (*GL_NORMAL_P3UIV)(GLenum type, const GLuint *coords)
ctypedef void (*GL_COLOR_P3UI)(GLenum type, GLuint color)
ctypedef void (*GL_COLOR_P3UIV)(GLenum type, const GLuint *color)
ctypedef void (*GL_COLOR_P4UI)(GLenum type, GLuint color)
ctypedef void (*GL_COLOR_P4UIV)(GLenum type, const GLuint *color)
ctypedef void (*GL_SECONDARY_COLOR_P3UI)(GLenum type, GLuint color)
ctypedef void (*GL_SECONDARY_COLOR_P3UIV)(GLenum type, const GLuint *color)

cdef GL_BIND_FRAG_DATA_LOCATION_INDEXED cglBindFragDataLocationIndexed = NULL
cdef GL_GET_FRAG_DATA_INDEX cglGetFragDataIndex = NULL
cdef GL_GEN_SAMPLERS cglGenSamplers = NULL
cdef GL_DELETE_SAMPLERS cglDeleteSamplers = NULL
cdef GL_IS_SAMPLER cglIsSampler = NULL
cdef GL_BIND_SAMPLER cglBindSampler = NULL
cdef GL_SAMPLER_PARAMETERI cglSamplerParameteri = NULL
cdef GL_SAMPLER_PARAMETERIV cglSamplerParameteriv = NULL
cdef GL_SAMPLER_PARAMETERF cglSamplerParameterf = NULL
cdef GL_SAMPLER_PARAMETERFV cglSamplerParameterfv = NULL
cdef GL_SAMPLER_PARAMETER_IIV cglSamplerParameterIiv = NULL
cdef GL_SAMPLER_PARAMETER_IUIV cglSamplerParameterIuiv = NULL
cdef GL_GET_SAMPLER_PARAMETERIV cglGetSamplerParameteriv = NULL
cdef GL_GET_SAMPLER_PARAMETER_IIV cglGetSamplerParameterIiv = NULL
cdef GL_GET_SAMPLER_PARAMETERFV cglGetSamplerParameterfv = NULL
cdef GL_GET_SAMPLER_PARAMETER_IUIV cglGetSamplerParameterIuiv = NULL
cdef GL_QUERY_COUNTER cglQueryCounter = NULL
cdef GL_GET_QUERY_OBJECTI64V cglGetQueryObjecti64v = NULL
cdef GL_GET_QUERY_OBJECTUI64V cglGetQueryObjectui64v = NULL
cdef GL_VERTEX_ATTRIB_DIVISOR cglVertexAttribDivisor = NULL
cdef GL_VERTEX_ATTRIB_P1UI cglVertexAttribP1ui = NULL
cdef GL_VERTEX_ATTRIB_P1UIV cglVertexAttribP1uiv = NULL
cdef GL_VERTEX_ATTRIB_P2UI cglVertexAttribP2ui = NULL
cdef GL_VERTEX_ATTRIB_P2UIV cglVertexAttribP2uiv = NULL
cdef GL_VERTEX_ATTRIB_P3UI cglVertexAttribP3ui = NULL
cdef GL_VERTEX_ATTRIB_P3UIV cglVertexAttribP3uiv = NULL
cdef GL_VERTEX_ATTRIB_P4UI cglVertexAttribP4ui = NULL
cdef GL_VERTEX_ATTRIB_P4UIV cglVertexAttribP4uiv = NULL
cdef GL_VERTEX_P2UI cglVertexP2ui = NULL
cdef GL_VERTEX_P2UIV cglVertexP2uiv = NULL
cdef GL_VERTEX_P3UI cglVertexP3ui = NULL
cdef GL_VERTEX_P3UIV cglVertexP3uiv = NULL
cdef GL_VERTEX_P4UI cglVertexP4ui = NULL
cdef GL_VERTEX_P4UIV cglVertexP4uiv = NULL
cdef GL_TEX_COORD_P1UI cglTexCoordP1ui = NULL
cdef GL_TEX_COORD_P1UIV cglTexCoordP1uiv = NULL
cdef GL_TEX_COORD_P2UI cglTexCoordP2ui = NULL
cdef GL_TEX_COORD_P2UIV cglTexCoordP2uiv = NULL
cdef GL_TEX_COORD_P3UI cglTexCoordP3ui = NULL
cdef GL_TEX_COORD_P3UIV cglTexCoordP3uiv = NULL
cdef GL_TEX_COORD_P4UI cglTexCoordP4ui = NULL
cdef GL_TEX_COORD_P4UIV cglTexCoordP4uiv = NULL
cdef GL_MULTI_TEX_COORD_P1UI cglMultiTexCoordP1ui = NULL
cdef GL_MULTI_TEX_COORD_P1UIV cglMultiTexCoordP1uiv = NULL
cdef GL_MULTI_TEX_COORD_P2UI cglMultiTexCoordP2ui = NULL
cdef GL_MULTI_TEX_COORD_P2UIV cglMultiTexCoordP2uiv = NULL
cdef GL_MULTI_TEX_COORD_P3UI cglMultiTexCoordP3ui = NULL
cdef GL_MULTI_TEX_COORD_P3UIV cglMultiTexCoordP3uiv = NULL
cdef GL_MULTI_TEX_COORD_P4UI cglMultiTexCoordP4ui = NULL
cdef GL_MULTI_TEX_COORD_P4UIV cglMultiTexCoordP4uiv = NULL
cdef GL_NORMAL_P3UI cglNormalP3ui = NULL
cdef GL_NORMAL_P3UIV cglNormalP3uiv = NULL
cdef GL_COLOR_P3UI cglColorP3ui = NULL
cdef GL_COLOR_P3UIV cglColorP3uiv = NULL
cdef GL_COLOR_P4UI cglColorP4ui = NULL
cdef GL_COLOR_P4UIV cglColorP4uiv = NULL
cdef GL_SECONDARY_COLOR_P3UI cglSecondaryColorP3ui = NULL
cdef GL_SECONDARY_COLOR_P3UIV cglSecondaryColorP3uiv = NULL


cdef void GetglBindFragDataLocationIndexed(GLuint program, GLuint colorNumber, GLuint index, const GLchar *name):
    global cglBindFragDataLocationIndexed
    cglBindFragDataLocationIndexed = <GL_BIND_FRAG_DATA_LOCATION_INDEXED>getFunction(b"glBindFragDataLocationIndexed")
    cglBindFragDataLocationIndexed(program, colorNumber, index, name)

cdef GLint GetglGetFragDataIndex(GLuint program, const GLchar *name):
    global cglGetFragDataIndex
    cglGetFragDataIndex = <GL_GET_FRAG_DATA_INDEX>getFunction(b"glGetFragDataIndex")
    cglGetFragDataIndex(program, name)

cdef void GetglGenSamplers(GLsizei count, GLuint *samplers):
    global cglGenSamplers
    cglGenSamplers = <GL_GEN_SAMPLERS>getFunction(b"glGenSamplers")
    cglGenSamplers(count, samplers)

cdef void GetglDeleteSamplers(GLsizei count, const GLuint *samplers):
    global cglDeleteSamplers
    cglDeleteSamplers = <GL_DELETE_SAMPLERS>getFunction(b"glDeleteSamplers")
    cglDeleteSamplers(count, samplers)

cdef GLboolean GetglIsSampler(GLuint sampler):
    global cglIsSampler
    cglIsSampler = <GL_IS_SAMPLER>getFunction(b"glIsSampler")
    cglIsSampler(sampler)

cdef void GetglBindSampler(GLuint unit, GLuint sampler):
    global cglBindSampler
    cglBindSampler = <GL_BIND_SAMPLER>getFunction(b"glBindSampler")
    cglBindSampler(unit, sampler)

cdef void GetglSamplerParameteri(GLuint sampler, GLenum pname, GLint param):
    global cglSamplerParameteri
    cglSamplerParameteri = <GL_SAMPLER_PARAMETERI>getFunction(b"glSamplerParameteri")
    cglSamplerParameteri(sampler, pname, param)

cdef void GetglSamplerParameteriv(GLuint sampler, GLenum pname, const GLint *param):
    global cglSamplerParameteriv
    cglSamplerParameteriv = <GL_SAMPLER_PARAMETERIV>getFunction(b"glSamplerParameteriv")
    cglSamplerParameteriv(sampler, pname, param)

cdef void GetglSamplerParameterf(GLuint sampler, GLenum pname, GLfloat param):
    global cglSamplerParameterf
    cglSamplerParameterf = <GL_SAMPLER_PARAMETERF>getFunction(b"glSamplerParameterf")
    cglSamplerParameterf(sampler, pname, param)

cdef void GetglSamplerParameterfv(GLuint sampler, GLenum pname, const GLfloat *param):
    global cglSamplerParameterfv
    cglSamplerParameterfv = <GL_SAMPLER_PARAMETERFV>getFunction(b"glSamplerParameterfv")
    cglSamplerParameterfv(sampler, pname, param)

cdef void GetglSamplerParameterIiv(GLuint sampler, GLenum pname, const GLint *param):
    global cglSamplerParameterIiv
    cglSamplerParameterIiv = <GL_SAMPLER_PARAMETER_IIV>getFunction(b"glSamplerParameterIiv")
    cglSamplerParameterIiv(sampler, pname, param)

cdef void GetglSamplerParameterIuiv(GLuint sampler, GLenum pname, const GLuint *param):
    global cglSamplerParameterIuiv
    cglSamplerParameterIuiv = <GL_SAMPLER_PARAMETER_IUIV>getFunction(b"glSamplerParameterIuiv")
    cglSamplerParameterIuiv(sampler, pname, param)

cdef void GetglGetSamplerParameteriv(GLuint sampler, GLenum pname, GLint *params):
    global cglGetSamplerParameteriv
    cglGetSamplerParameteriv = <GL_GET_SAMPLER_PARAMETERIV>getFunction(b"glGetSamplerParameteriv")
    cglGetSamplerParameteriv(sampler, pname, params)

cdef void GetglGetSamplerParameterIiv(GLuint sampler, GLenum pname, GLint *params):
    global cglGetSamplerParameterIiv
    cglGetSamplerParameterIiv = <GL_GET_SAMPLER_PARAMETER_IIV>getFunction(b"glGetSamplerParameterIiv")
    cglGetSamplerParameterIiv(sampler, pname, params)

cdef void GetglGetSamplerParameterfv(GLuint sampler, GLenum pname, GLfloat *params):
    global cglGetSamplerParameterfv
    cglGetSamplerParameterfv = <GL_GET_SAMPLER_PARAMETERFV>getFunction(b"glGetSamplerParameterfv")
    cglGetSamplerParameterfv(sampler, pname, params)

cdef void GetglGetSamplerParameterIuiv(GLuint sampler, GLenum pname, GLuint *params):
    global cglGetSamplerParameterIuiv
    cglGetSamplerParameterIuiv = <GL_GET_SAMPLER_PARAMETER_IUIV>getFunction(b"glGetSamplerParameterIuiv")
    cglGetSamplerParameterIuiv(sampler, pname, params)

cdef void GetglQueryCounter(GLuint id, GLenum target):
    global cglQueryCounter
    cglQueryCounter = <GL_QUERY_COUNTER>getFunction(b"glQueryCounter")
    cglQueryCounter(id, target)

cdef void GetglGetQueryObjecti64v(GLuint id, GLenum pname, GLint64 *params):
    global cglGetQueryObjecti64v
    cglGetQueryObjecti64v = <GL_GET_QUERY_OBJECTI64V>getFunction(b"glGetQueryObjecti64v")
    cglGetQueryObjecti64v(id, pname, params)

cdef void GetglGetQueryObjectui64v(GLuint id, GLenum pname, GLuint64 *params):
    global cglGetQueryObjectui64v
    cglGetQueryObjectui64v = <GL_GET_QUERY_OBJECTUI64V>getFunction(b"glGetQueryObjectui64v")
    cglGetQueryObjectui64v(id, pname, params)

cdef void GetglVertexAttribDivisor(GLuint index, GLuint divisor):
    global cglVertexAttribDivisor
    cglVertexAttribDivisor = <GL_VERTEX_ATTRIB_DIVISOR>getFunction(b"glVertexAttribDivisor")
    cglVertexAttribDivisor(index, divisor)

cdef void GetglVertexAttribP1ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP1ui
    cglVertexAttribP1ui = <GL_VERTEX_ATTRIB_P1UI>getFunction(b"glVertexAttribP1ui")
    cglVertexAttribP1ui(index, type, normalized, value)

cdef void GetglVertexAttribP1uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP1uiv
    cglVertexAttribP1uiv = <GL_VERTEX_ATTRIB_P1UIV>getFunction(b"glVertexAttribP1uiv")
    cglVertexAttribP1uiv(index, type, normalized, value)

cdef void GetglVertexAttribP2ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP2ui
    cglVertexAttribP2ui = <GL_VERTEX_ATTRIB_P2UI>getFunction(b"glVertexAttribP2ui")
    cglVertexAttribP2ui(index, type, normalized, value)

cdef void GetglVertexAttribP2uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP2uiv
    cglVertexAttribP2uiv = <GL_VERTEX_ATTRIB_P2UIV>getFunction(b"glVertexAttribP2uiv")
    cglVertexAttribP2uiv(index, type, normalized, value)

cdef void GetglVertexAttribP3ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP3ui
    cglVertexAttribP3ui = <GL_VERTEX_ATTRIB_P3UI>getFunction(b"glVertexAttribP3ui")
    cglVertexAttribP3ui(index, type, normalized, value)

cdef void GetglVertexAttribP3uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP3uiv
    cglVertexAttribP3uiv = <GL_VERTEX_ATTRIB_P3UIV>getFunction(b"glVertexAttribP3uiv")
    cglVertexAttribP3uiv(index, type, normalized, value)

cdef void GetglVertexAttribP4ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP4ui
    cglVertexAttribP4ui = <GL_VERTEX_ATTRIB_P4UI>getFunction(b"glVertexAttribP4ui")
    cglVertexAttribP4ui(index, type, normalized, value)

cdef void GetglVertexAttribP4uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP4uiv
    cglVertexAttribP4uiv = <GL_VERTEX_ATTRIB_P4UIV>getFunction(b"glVertexAttribP4uiv")
    cglVertexAttribP4uiv(index, type, normalized, value)

cdef void GetglVertexP2ui(GLenum type, GLuint value):
    global cglVertexP2ui
    cglVertexP2ui = <GL_VERTEX_P2UI>getFunction(b"glVertexP2ui")
    cglVertexP2ui(type, value)

cdef void GetglVertexP2uiv(GLenum type, const GLuint *value):
    global cglVertexP2uiv
    cglVertexP2uiv = <GL_VERTEX_P2UIV>getFunction(b"glVertexP2uiv")
    cglVertexP2uiv(type, value)

cdef void GetglVertexP3ui(GLenum type, GLuint value):
    global cglVertexP3ui
    cglVertexP3ui = <GL_VERTEX_P3UI>getFunction(b"glVertexP3ui")
    cglVertexP3ui(type, value)

cdef void GetglVertexP3uiv(GLenum type, const GLuint *value):
    global cglVertexP3uiv
    cglVertexP3uiv = <GL_VERTEX_P3UIV>getFunction(b"glVertexP3uiv")
    cglVertexP3uiv(type, value)

cdef void GetglVertexP4ui(GLenum type, GLuint value):
    global cglVertexP4ui
    cglVertexP4ui = <GL_VERTEX_P4UI>getFunction(b"glVertexP4ui")
    cglVertexP4ui(type, value)

cdef void GetglVertexP4uiv(GLenum type, const GLuint *value):
    global cglVertexP4uiv
    cglVertexP4uiv = <GL_VERTEX_P4UIV>getFunction(b"glVertexP4uiv")
    cglVertexP4uiv(type, value)

cdef void GetglTexCoordP1ui(GLenum type, GLuint coords):
    global cglTexCoordP1ui
    cglTexCoordP1ui = <GL_TEX_COORD_P1UI>getFunction(b"glTexCoordP1ui")
    cglTexCoordP1ui(type, coords)

cdef void GetglTexCoordP1uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP1uiv
    cglTexCoordP1uiv = <GL_TEX_COORD_P1UIV>getFunction(b"glTexCoordP1uiv")
    cglTexCoordP1uiv(type, coords)

cdef void GetglTexCoordP2ui(GLenum type, GLuint coords):
    global cglTexCoordP2ui
    cglTexCoordP2ui = <GL_TEX_COORD_P2UI>getFunction(b"glTexCoordP2ui")
    cglTexCoordP2ui(type, coords)

cdef void GetglTexCoordP2uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP2uiv
    cglTexCoordP2uiv = <GL_TEX_COORD_P2UIV>getFunction(b"glTexCoordP2uiv")
    cglTexCoordP2uiv(type, coords)

cdef void GetglTexCoordP3ui(GLenum type, GLuint coords):
    global cglTexCoordP3ui
    cglTexCoordP3ui = <GL_TEX_COORD_P3UI>getFunction(b"glTexCoordP3ui")
    cglTexCoordP3ui(type, coords)

cdef void GetglTexCoordP3uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP3uiv
    cglTexCoordP3uiv = <GL_TEX_COORD_P3UIV>getFunction(b"glTexCoordP3uiv")
    cglTexCoordP3uiv(type, coords)

cdef void GetglTexCoordP4ui(GLenum type, GLuint coords):
    global cglTexCoordP4ui
    cglTexCoordP4ui = <GL_TEX_COORD_P4UI>getFunction(b"glTexCoordP4ui")
    cglTexCoordP4ui(type, coords)

cdef void GetglTexCoordP4uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP4uiv
    cglTexCoordP4uiv = <GL_TEX_COORD_P4UIV>getFunction(b"glTexCoordP4uiv")
    cglTexCoordP4uiv(type, coords)

cdef void GetglMultiTexCoordP1ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP1ui
    cglMultiTexCoordP1ui = <GL_MULTI_TEX_COORD_P1UI>getFunction(b"glMultiTexCoordP1ui")
    cglMultiTexCoordP1ui(texture, type, coords)

cdef void GetglMultiTexCoordP1uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP1uiv
    cglMultiTexCoordP1uiv = <GL_MULTI_TEX_COORD_P1UIV>getFunction(b"glMultiTexCoordP1uiv")
    cglMultiTexCoordP1uiv(texture, type, coords)

cdef void GetglMultiTexCoordP2ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP2ui
    cglMultiTexCoordP2ui = <GL_MULTI_TEX_COORD_P2UI>getFunction(b"glMultiTexCoordP2ui")
    cglMultiTexCoordP2ui(texture, type, coords)

cdef void GetglMultiTexCoordP2uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP2uiv
    cglMultiTexCoordP2uiv = <GL_MULTI_TEX_COORD_P2UIV>getFunction(b"glMultiTexCoordP2uiv")
    cglMultiTexCoordP2uiv(texture, type, coords)

cdef void GetglMultiTexCoordP3ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP3ui
    cglMultiTexCoordP3ui = <GL_MULTI_TEX_COORD_P3UI>getFunction(b"glMultiTexCoordP3ui")
    cglMultiTexCoordP3ui(texture, type, coords)

cdef void GetglMultiTexCoordP3uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP3uiv
    cglMultiTexCoordP3uiv = <GL_MULTI_TEX_COORD_P3UIV>getFunction(b"glMultiTexCoordP3uiv")
    cglMultiTexCoordP3uiv(texture, type, coords)

cdef void GetglMultiTexCoordP4ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP4ui
    cglMultiTexCoordP4ui = <GL_MULTI_TEX_COORD_P4UI>getFunction(b"glMultiTexCoordP4ui")
    cglMultiTexCoordP4ui(texture, type, coords)

cdef void GetglMultiTexCoordP4uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP4uiv
    cglMultiTexCoordP4uiv = <GL_MULTI_TEX_COORD_P4UIV>getFunction(b"glMultiTexCoordP4uiv")
    cglMultiTexCoordP4uiv(texture, type, coords)

cdef void GetglNormalP3ui(GLenum type, GLuint coords):
    global cglNormalP3ui
    cglNormalP3ui = <GL_NORMAL_P3UI>getFunction(b"glNormalP3ui")
    cglNormalP3ui(type, coords)

cdef void GetglNormalP3uiv(GLenum type, const GLuint *coords):
    global cglNormalP3uiv
    cglNormalP3uiv = <GL_NORMAL_P3UIV>getFunction(b"glNormalP3uiv")
    cglNormalP3uiv(type, coords)

cdef void GetglColorP3ui(GLenum type, GLuint color):
    global cglColorP3ui
    cglColorP3ui = <GL_COLOR_P3UI>getFunction(b"glColorP3ui")
    cglColorP3ui(type, color)

cdef void GetglColorP3uiv(GLenum type, const GLuint *color):
    global cglColorP3uiv
    cglColorP3uiv = <GL_COLOR_P3UIV>getFunction(b"glColorP3uiv")
    cglColorP3uiv(type, color)

cdef void GetglColorP4ui(GLenum type, GLuint color):
    global cglColorP4ui
    cglColorP4ui = <GL_COLOR_P4UI>getFunction(b"glColorP4ui")
    cglColorP4ui(type, color)

cdef void GetglColorP4uiv(GLenum type, const GLuint *color):
    global cglColorP4uiv
    cglColorP4uiv = <GL_COLOR_P4UIV>getFunction(b"glColorP4uiv")
    cglColorP4uiv(type, color)

cdef void GetglSecondaryColorP3ui(GLenum type, GLuint color):
    global cglSecondaryColorP3ui
    cglSecondaryColorP3ui = <GL_SECONDARY_COLOR_P3UI>getFunction(b"glSecondaryColorP3ui")
    cglSecondaryColorP3ui(type, color)

cdef void GetglSecondaryColorP3uiv(GLenum type, const GLuint *color):
    global cglSecondaryColorP3uiv
    cglSecondaryColorP3uiv = <GL_SECONDARY_COLOR_P3UIV>getFunction(b"glSecondaryColorP3uiv")
    cglSecondaryColorP3uiv(type, color)

cglBindFragDataLocationIndexed = GetglBindFragDataLocationIndexed
cglGetFragDataIndex = GetglGetFragDataIndex
cglGenSamplers = GetglGenSamplers
cglDeleteSamplers = GetglDeleteSamplers
cglIsSampler = GetglIsSampler
cglBindSampler = GetglBindSampler
cglSamplerParameteri = GetglSamplerParameteri
cglSamplerParameteriv = GetglSamplerParameteriv
cglSamplerParameterf = GetglSamplerParameterf
cglSamplerParameterfv = GetglSamplerParameterfv
cglSamplerParameterIiv = GetglSamplerParameterIiv
cglSamplerParameterIuiv = GetglSamplerParameterIuiv
cglGetSamplerParameteriv = GetglGetSamplerParameteriv
cglGetSamplerParameterIiv = GetglGetSamplerParameterIiv
cglGetSamplerParameterfv = GetglGetSamplerParameterfv
cglGetSamplerParameterIuiv = GetglGetSamplerParameterIuiv
cglQueryCounter = GetglQueryCounter
cglGetQueryObjecti64v = GetglGetQueryObjecti64v
cglGetQueryObjectui64v = GetglGetQueryObjectui64v
cglVertexAttribDivisor = GetglVertexAttribDivisor
cglVertexAttribP1ui = GetglVertexAttribP1ui
cglVertexAttribP1uiv = GetglVertexAttribP1uiv
cglVertexAttribP2ui = GetglVertexAttribP2ui
cglVertexAttribP2uiv = GetglVertexAttribP2uiv
cglVertexAttribP3ui = GetglVertexAttribP3ui
cglVertexAttribP3uiv = GetglVertexAttribP3uiv
cglVertexAttribP4ui = GetglVertexAttribP4ui
cglVertexAttribP4uiv = GetglVertexAttribP4uiv
cglVertexP2ui = GetglVertexP2ui
cglVertexP2uiv = GetglVertexP2uiv
cglVertexP3ui = GetglVertexP3ui
cglVertexP3uiv = GetglVertexP3uiv
cglVertexP4ui = GetglVertexP4ui
cglVertexP4uiv = GetglVertexP4uiv
cglTexCoordP1ui = GetglTexCoordP1ui
cglTexCoordP1uiv = GetglTexCoordP1uiv
cglTexCoordP2ui = GetglTexCoordP2ui
cglTexCoordP2uiv = GetglTexCoordP2uiv
cglTexCoordP3ui = GetglTexCoordP3ui
cglTexCoordP3uiv = GetglTexCoordP3uiv
cglTexCoordP4ui = GetglTexCoordP4ui
cglTexCoordP4uiv = GetglTexCoordP4uiv
cglMultiTexCoordP1ui = GetglMultiTexCoordP1ui
cglMultiTexCoordP1uiv = GetglMultiTexCoordP1uiv
cglMultiTexCoordP2ui = GetglMultiTexCoordP2ui
cglMultiTexCoordP2uiv = GetglMultiTexCoordP2uiv
cglMultiTexCoordP3ui = GetglMultiTexCoordP3ui
cglMultiTexCoordP3uiv = GetglMultiTexCoordP3uiv
cglMultiTexCoordP4ui = GetglMultiTexCoordP4ui
cglMultiTexCoordP4uiv = GetglMultiTexCoordP4uiv
cglNormalP3ui = GetglNormalP3ui
cglNormalP3uiv = GetglNormalP3uiv
cglColorP3ui = GetglColorP3ui
cglColorP3uiv = GetglColorP3uiv
cglColorP4ui = GetglColorP4ui
cglColorP4uiv = GetglColorP4uiv
cglSecondaryColorP3ui = GetglSecondaryColorP3ui
cglSecondaryColorP3uiv = GetglSecondaryColorP3uiv


cpdef void glBindFragDataLocationIndexed(GLuint program, GLuint colorNumber, GLuint index, const GLchar *name):
    cglBindFragDataLocationIndexed(program, colorNumber, index, name)

cpdef GLint glGetFragDataIndex(GLuint program, const GLchar *name):
    cglGetFragDataIndex(program, name)

cpdef void glGenSamplers(GLsizei count, GLuint *samplers):
    cglGenSamplers(count, samplers)

cpdef void glDeleteSamplers(GLsizei count, const GLuint *samplers):
    cglDeleteSamplers(count, samplers)

cpdef GLboolean glIsSampler(GLuint sampler):
    cglIsSampler(sampler)

cpdef void glBindSampler(GLuint unit, GLuint sampler):
    cglBindSampler(unit, sampler)

cpdef void glSamplerParameteri(GLuint sampler, GLenum pname, GLint param):
    cglSamplerParameteri(sampler, pname, param)

cpdef void glSamplerParameteriv(GLuint sampler, GLenum pname, const GLint *param):
    cglSamplerParameteriv(sampler, pname, param)

cpdef void glSamplerParameterf(GLuint sampler, GLenum pname, GLfloat param):
    cglSamplerParameterf(sampler, pname, param)

cpdef void glSamplerParameterfv(GLuint sampler, GLenum pname, const GLfloat *param):
    cglSamplerParameterfv(sampler, pname, param)

cpdef void glSamplerParameterIiv(GLuint sampler, GLenum pname, const GLint *param):
    cglSamplerParameterIiv(sampler, pname, param)

cpdef void glSamplerParameterIuiv(GLuint sampler, GLenum pname, const GLuint *param):
    cglSamplerParameterIuiv(sampler, pname, param)

cpdef void glGetSamplerParameteriv(GLuint sampler, GLenum pname, GLint *params):
    cglGetSamplerParameteriv(sampler, pname, params)

cpdef void glGetSamplerParameterIiv(GLuint sampler, GLenum pname, GLint *params):
    cglGetSamplerParameterIiv(sampler, pname, params)

cpdef void glGetSamplerParameterfv(GLuint sampler, GLenum pname, GLfloat *params):
    cglGetSamplerParameterfv(sampler, pname, params)

cpdef void glGetSamplerParameterIuiv(GLuint sampler, GLenum pname, GLuint *params):
    cglGetSamplerParameterIuiv(sampler, pname, params)

cpdef void glQueryCounter(GLuint id, GLenum target):
    cglQueryCounter(id, target)

cpdef void glGetQueryObjecti64v(GLuint id, GLenum pname, GLint64 *params):
    cglGetQueryObjecti64v(id, pname, params)

cpdef void glGetQueryObjectui64v(GLuint id, GLenum pname, GLuint64 *params):
    cglGetQueryObjectui64v(id, pname, params)

cpdef void glVertexAttribDivisor(GLuint index, GLuint divisor):
    cglVertexAttribDivisor(index, divisor)

cpdef void glVertexAttribP1ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP1ui(index, type, normalized, value)

cpdef void glVertexAttribP1uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP1uiv(index, type, normalized, value)

cpdef void glVertexAttribP2ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP2ui(index, type, normalized, value)

cpdef void glVertexAttribP2uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP2uiv(index, type, normalized, value)

cpdef void glVertexAttribP3ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP3ui(index, type, normalized, value)

cpdef void glVertexAttribP3uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP3uiv(index, type, normalized, value)

cpdef void glVertexAttribP4ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP4ui(index, type, normalized, value)

cpdef void glVertexAttribP4uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP4uiv(index, type, normalized, value)

cpdef void glVertexP2ui(GLenum type, GLuint value):
    cglVertexP2ui(type, value)

cpdef void glVertexP2uiv(GLenum type, const GLuint *value):
    cglVertexP2uiv(type, value)

cpdef void glVertexP3ui(GLenum type, GLuint value):
    cglVertexP3ui(type, value)

cpdef void glVertexP3uiv(GLenum type, const GLuint *value):
    cglVertexP3uiv(type, value)

cpdef void glVertexP4ui(GLenum type, GLuint value):
    cglVertexP4ui(type, value)

cpdef void glVertexP4uiv(GLenum type, const GLuint *value):
    cglVertexP4uiv(type, value)

cpdef void glTexCoordP1ui(GLenum type, GLuint coords):
    cglTexCoordP1ui(type, coords)

cpdef void glTexCoordP1uiv(GLenum type, const GLuint *coords):
    cglTexCoordP1uiv(type, coords)

cpdef void glTexCoordP2ui(GLenum type, GLuint coords):
    cglTexCoordP2ui(type, coords)

cpdef void glTexCoordP2uiv(GLenum type, const GLuint *coords):
    cglTexCoordP2uiv(type, coords)

cpdef void glTexCoordP3ui(GLenum type, GLuint coords):
    cglTexCoordP3ui(type, coords)

cpdef void glTexCoordP3uiv(GLenum type, const GLuint *coords):
    cglTexCoordP3uiv(type, coords)

cpdef void glTexCoordP4ui(GLenum type, GLuint coords):
    cglTexCoordP4ui(type, coords)

cpdef void glTexCoordP4uiv(GLenum type, const GLuint *coords):
    cglTexCoordP4uiv(type, coords)

cpdef void glMultiTexCoordP1ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP1ui(texture, type, coords)

cpdef void glMultiTexCoordP1uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP1uiv(texture, type, coords)

cpdef void glMultiTexCoordP2ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP2ui(texture, type, coords)

cpdef void glMultiTexCoordP2uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP2uiv(texture, type, coords)

cpdef void glMultiTexCoordP3ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP3ui(texture, type, coords)

cpdef void glMultiTexCoordP3uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP3uiv(texture, type, coords)

cpdef void glMultiTexCoordP4ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP4ui(texture, type, coords)

cpdef void glMultiTexCoordP4uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP4uiv(texture, type, coords)

cpdef void glNormalP3ui(GLenum type, GLuint coords):
    cglNormalP3ui(type, coords)

cpdef void glNormalP3uiv(GLenum type, const GLuint *coords):
    cglNormalP3uiv(type, coords)

cpdef void glColorP3ui(GLenum type, GLuint color):
    cglColorP3ui(type, color)

cpdef void glColorP3uiv(GLenum type, const GLuint *color):
    cglColorP3uiv(type, color)

cpdef void glColorP4ui(GLenum type, GLuint color):
    cglColorP4ui(type, color)

cpdef void glColorP4uiv(GLenum type, const GLuint *color):
    cglColorP4uiv(type, color)

cpdef void glSecondaryColorP3ui(GLenum type, GLuint color):
    cglSecondaryColorP3ui(type, color)

cpdef void glSecondaryColorP3uiv(GLenum type, const GLuint *color):
    cglSecondaryColorP3uiv(type, color)
