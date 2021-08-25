# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_ANY_SAMPLES_PASSED = 0x8C2F
cdef GLenum GL_INT_2_10_10_10_REV = 0x8D9F
cdef GLenum GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = 0x88FC
cdef GLenum GL_ONE_MINUS_SRC1_ALPHA = 0x88FB
cdef GLenum GL_ONE_MINUS_SRC1_COLOR = 0x88FA
cdef GLenum GL_RGB10_A2UI = 0x906F
cdef GLenum GL_SAMPLER_BINDING = 0x8919
cdef GLenum GL_SRC1_COLOR = 0x88F9
cdef GLenum GL_TEXTURE_SWIZZLE_A = 0x8E45
cdef GLenum GL_TEXTURE_SWIZZLE_B = 0x8E44
cdef GLenum GL_TEXTURE_SWIZZLE_G = 0x8E43
cdef GLenum GL_TEXTURE_SWIZZLE_R = 0x8E42
cdef GLenum GL_TEXTURE_SWIZZLE_RGBA = 0x8E46
cdef GLenum GL_TIMESTAMP = 0x8E28
cdef GLenum GL_TIME_ELAPSED = 0x88BF
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 0x88FE

ctypedef void (*PFNGLBINDFRAGDATALOCATIONINDEXEDPROC)(GLuint program, GLuint colorNumber, GLuint index, const GLchar *name)
ctypedef void (*PFNGLBINDSAMPLERPROC)(GLuint unit, GLuint sampler)
ctypedef void (*PFNGLCOLORP3UIPROC)(GLenum type, GLuint color)
ctypedef void (*PFNGLCOLORP3UIVPROC)(GLenum type, const GLuint *color)
ctypedef void (*PFNGLCOLORP4UIPROC)(GLenum type, GLuint color)
ctypedef void (*PFNGLCOLORP4UIVPROC)(GLenum type, const GLuint *color)
ctypedef void (*PFNGLDELETESAMPLERSPROC)(GLsizei count, const GLuint *samplers)
ctypedef void (*PFNGLGENSAMPLERSPROC)(GLsizei count, GLuint *samplers)
ctypedef GLint (*PFNGLGETFRAGDATAINDEXPROC)(GLuint program, const GLchar *name)
ctypedef void (*PFNGLGETQUERYOBJECTI64VPROC)(GLuint id, GLenum pname, GLint64 *params)
ctypedef void (*PFNGLGETQUERYOBJECTUI64VPROC)(GLuint id, GLenum pname, GLuint64 *params)
ctypedef void (*PFNGLGETSAMPLERPARAMETERIIVPROC)(GLuint sampler, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETSAMPLERPARAMETERIUIVPROC)(GLuint sampler, GLenum pname, GLuint *params)
ctypedef void (*PFNGLGETSAMPLERPARAMETERFVPROC)(GLuint sampler, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLGETSAMPLERPARAMETERIVPROC)(GLuint sampler, GLenum pname, GLint *params)
ctypedef GLboolean (*PFNGLISSAMPLERPROC)(GLuint sampler)
ctypedef void (*PFNGLMULTITEXCOORDP1UIPROC)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*PFNGLMULTITEXCOORDP1UIVPROC)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*PFNGLMULTITEXCOORDP2UIPROC)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*PFNGLMULTITEXCOORDP2UIVPROC)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*PFNGLMULTITEXCOORDP3UIPROC)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*PFNGLMULTITEXCOORDP3UIVPROC)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*PFNGLMULTITEXCOORDP4UIPROC)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*PFNGLMULTITEXCOORDP4UIVPROC)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*PFNGLNORMALP3UIPROC)(GLenum type, GLuint coords)
ctypedef void (*PFNGLNORMALP3UIVPROC)(GLenum type, const GLuint *coords)
ctypedef void (*PFNGLQUERYCOUNTERPROC)(GLuint id, GLenum target)
ctypedef void (*PFNGLSAMPLERPARAMETERIIVPROC)(GLuint sampler, GLenum pname, const GLint *param)
ctypedef void (*PFNGLSAMPLERPARAMETERIUIVPROC)(GLuint sampler, GLenum pname, const GLuint *param)
ctypedef void (*PFNGLSAMPLERPARAMETERFPROC)(GLuint sampler, GLenum pname, GLfloat param)
ctypedef void (*PFNGLSAMPLERPARAMETERFVPROC)(GLuint sampler, GLenum pname, const GLfloat *param)
ctypedef void (*PFNGLSAMPLERPARAMETERIPROC)(GLuint sampler, GLenum pname, GLint param)
ctypedef void (*PFNGLSAMPLERPARAMETERIVPROC)(GLuint sampler, GLenum pname, const GLint *param)
ctypedef void (*PFNGLSECONDARYCOLORP3UIPROC)(GLenum type, GLuint color)
ctypedef void (*PFNGLSECONDARYCOLORP3UIVPROC)(GLenum type, const GLuint *color)
ctypedef void (*PFNGLTEXCOORDP1UIPROC)(GLenum type, GLuint coords)
ctypedef void (*PFNGLTEXCOORDP1UIVPROC)(GLenum type, const GLuint *coords)
ctypedef void (*PFNGLTEXCOORDP2UIPROC)(GLenum type, GLuint coords)
ctypedef void (*PFNGLTEXCOORDP2UIVPROC)(GLenum type, const GLuint *coords)
ctypedef void (*PFNGLTEXCOORDP3UIPROC)(GLenum type, GLuint coords)
ctypedef void (*PFNGLTEXCOORDP3UIVPROC)(GLenum type, const GLuint *coords)
ctypedef void (*PFNGLTEXCOORDP4UIPROC)(GLenum type, GLuint coords)
ctypedef void (*PFNGLTEXCOORDP4UIVPROC)(GLenum type, const GLuint *coords)
ctypedef void (*PFNGLVERTEXATTRIBDIVISORPROC)(GLuint index, GLuint divisor)
ctypedef void (*PFNGLVERTEXATTRIBP1UIPROC)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*PFNGLVERTEXATTRIBP1UIVPROC)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*PFNGLVERTEXATTRIBP2UIPROC)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*PFNGLVERTEXATTRIBP2UIVPROC)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*PFNGLVERTEXATTRIBP3UIPROC)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*PFNGLVERTEXATTRIBP3UIVPROC)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*PFNGLVERTEXATTRIBP4UIPROC)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*PFNGLVERTEXATTRIBP4UIVPROC)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*PFNGLVERTEXP2UIPROC)(GLenum type, GLuint value)
ctypedef void (*PFNGLVERTEXP2UIVPROC)(GLenum type, const GLuint *value)
ctypedef void (*PFNGLVERTEXP3UIPROC)(GLenum type, GLuint value)
ctypedef void (*PFNGLVERTEXP3UIVPROC)(GLenum type, const GLuint *value)
ctypedef void (*PFNGLVERTEXP4UIPROC)(GLenum type, GLuint value)
ctypedef void (*PFNGLVERTEXP4UIVPROC)(GLenum type, const GLuint *value)

cdef PFNGLBINDFRAGDATALOCATIONINDEXEDPROC cglBindFragDataLocationIndexed = NULL
cdef PFNGLBINDSAMPLERPROC cglBindSampler = NULL
cdef PFNGLCOLORP3UIPROC cglColorP3ui = NULL
cdef PFNGLCOLORP3UIVPROC cglColorP3uiv = NULL
cdef PFNGLCOLORP4UIPROC cglColorP4ui = NULL
cdef PFNGLCOLORP4UIVPROC cglColorP4uiv = NULL
cdef PFNGLDELETESAMPLERSPROC cglDeleteSamplers = NULL
cdef PFNGLGENSAMPLERSPROC cglGenSamplers = NULL
cdef PFNGLGETFRAGDATAINDEXPROC cglGetFragDataIndex = NULL
cdef PFNGLGETQUERYOBJECTI64VPROC cglGetQueryObjecti64v = NULL
cdef PFNGLGETQUERYOBJECTUI64VPROC cglGetQueryObjectui64v = NULL
cdef PFNGLGETSAMPLERPARAMETERIIVPROC cglGetSamplerParameterIiv = NULL
cdef PFNGLGETSAMPLERPARAMETERIUIVPROC cglGetSamplerParameterIuiv = NULL
cdef PFNGLGETSAMPLERPARAMETERFVPROC cglGetSamplerParameterfv = NULL
cdef PFNGLGETSAMPLERPARAMETERIVPROC cglGetSamplerParameteriv = NULL
cdef PFNGLISSAMPLERPROC cglIsSampler = NULL
cdef PFNGLMULTITEXCOORDP1UIPROC cglMultiTexCoordP1ui = NULL
cdef PFNGLMULTITEXCOORDP1UIVPROC cglMultiTexCoordP1uiv = NULL
cdef PFNGLMULTITEXCOORDP2UIPROC cglMultiTexCoordP2ui = NULL
cdef PFNGLMULTITEXCOORDP2UIVPROC cglMultiTexCoordP2uiv = NULL
cdef PFNGLMULTITEXCOORDP3UIPROC cglMultiTexCoordP3ui = NULL
cdef PFNGLMULTITEXCOORDP3UIVPROC cglMultiTexCoordP3uiv = NULL
cdef PFNGLMULTITEXCOORDP4UIPROC cglMultiTexCoordP4ui = NULL
cdef PFNGLMULTITEXCOORDP4UIVPROC cglMultiTexCoordP4uiv = NULL
cdef PFNGLNORMALP3UIPROC cglNormalP3ui = NULL
cdef PFNGLNORMALP3UIVPROC cglNormalP3uiv = NULL
cdef PFNGLQUERYCOUNTERPROC cglQueryCounter = NULL
cdef PFNGLSAMPLERPARAMETERIIVPROC cglSamplerParameterIiv = NULL
cdef PFNGLSAMPLERPARAMETERIUIVPROC cglSamplerParameterIuiv = NULL
cdef PFNGLSAMPLERPARAMETERFPROC cglSamplerParameterf = NULL
cdef PFNGLSAMPLERPARAMETERFVPROC cglSamplerParameterfv = NULL
cdef PFNGLSAMPLERPARAMETERIPROC cglSamplerParameteri = NULL
cdef PFNGLSAMPLERPARAMETERIVPROC cglSamplerParameteriv = NULL
cdef PFNGLSECONDARYCOLORP3UIPROC cglSecondaryColorP3ui = NULL
cdef PFNGLSECONDARYCOLORP3UIVPROC cglSecondaryColorP3uiv = NULL
cdef PFNGLTEXCOORDP1UIPROC cglTexCoordP1ui = NULL
cdef PFNGLTEXCOORDP1UIVPROC cglTexCoordP1uiv = NULL
cdef PFNGLTEXCOORDP2UIPROC cglTexCoordP2ui = NULL
cdef PFNGLTEXCOORDP2UIVPROC cglTexCoordP2uiv = NULL
cdef PFNGLTEXCOORDP3UIPROC cglTexCoordP3ui = NULL
cdef PFNGLTEXCOORDP3UIVPROC cglTexCoordP3uiv = NULL
cdef PFNGLTEXCOORDP4UIPROC cglTexCoordP4ui = NULL
cdef PFNGLTEXCOORDP4UIVPROC cglTexCoordP4uiv = NULL
cdef PFNGLVERTEXATTRIBDIVISORPROC cglVertexAttribDivisor = NULL
cdef PFNGLVERTEXATTRIBP1UIPROC cglVertexAttribP1ui = NULL
cdef PFNGLVERTEXATTRIBP1UIVPROC cglVertexAttribP1uiv = NULL
cdef PFNGLVERTEXATTRIBP2UIPROC cglVertexAttribP2ui = NULL
cdef PFNGLVERTEXATTRIBP2UIVPROC cglVertexAttribP2uiv = NULL
cdef PFNGLVERTEXATTRIBP3UIPROC cglVertexAttribP3ui = NULL
cdef PFNGLVERTEXATTRIBP3UIVPROC cglVertexAttribP3uiv = NULL
cdef PFNGLVERTEXATTRIBP4UIPROC cglVertexAttribP4ui = NULL
cdef PFNGLVERTEXATTRIBP4UIVPROC cglVertexAttribP4uiv = NULL
cdef PFNGLVERTEXP2UIPROC cglVertexP2ui = NULL
cdef PFNGLVERTEXP2UIVPROC cglVertexP2uiv = NULL
cdef PFNGLVERTEXP3UIPROC cglVertexP3ui = NULL
cdef PFNGLVERTEXP3UIVPROC cglVertexP3uiv = NULL
cdef PFNGLVERTEXP4UIPROC cglVertexP4ui = NULL
cdef PFNGLVERTEXP4UIVPROC cglVertexP4uiv = NULL


cdef void GetglBindFragDataLocationIndexed(GLuint program, GLuint colorNumber, GLuint index, const GLchar *name):
    global cglBindFragDataLocationIndexed
    cglBindFragDataLocationIndexed = <PFNGLBINDFRAGDATALOCATIONINDEXEDPROC>getFunction("glBindFragDataLocationIndexed")
    cglBindFragDataLocationIndexed(program, colorNumber, index, name)

cdef void GetglBindSampler(GLuint unit, GLuint sampler):
    global cglBindSampler
    cglBindSampler = <PFNGLBINDSAMPLERPROC>getFunction("glBindSampler")
    cglBindSampler(unit, sampler)

cdef void GetglColorP3ui(GLenum type, GLuint color):
    global cglColorP3ui
    cglColorP3ui = <PFNGLCOLORP3UIPROC>getFunction("glColorP3ui")
    cglColorP3ui(type, color)

cdef void GetglColorP3uiv(GLenum type, const GLuint *color):
    global cglColorP3uiv
    cglColorP3uiv = <PFNGLCOLORP3UIVPROC>getFunction("glColorP3uiv")
    cglColorP3uiv(type, color)

cdef void GetglColorP4ui(GLenum type, GLuint color):
    global cglColorP4ui
    cglColorP4ui = <PFNGLCOLORP4UIPROC>getFunction("glColorP4ui")
    cglColorP4ui(type, color)

cdef void GetglColorP4uiv(GLenum type, const GLuint *color):
    global cglColorP4uiv
    cglColorP4uiv = <PFNGLCOLORP4UIVPROC>getFunction("glColorP4uiv")
    cglColorP4uiv(type, color)

cdef void GetglDeleteSamplers(GLsizei count, const GLuint *samplers):
    global cglDeleteSamplers
    cglDeleteSamplers = <PFNGLDELETESAMPLERSPROC>getFunction("glDeleteSamplers")
    cglDeleteSamplers(count, samplers)

cdef void GetglGenSamplers(GLsizei count, GLuint *samplers):
    global cglGenSamplers
    cglGenSamplers = <PFNGLGENSAMPLERSPROC>getFunction("glGenSamplers")
    cglGenSamplers(count, samplers)

cdef GLint GetglGetFragDataIndex(GLuint program, const GLchar *name):
    global cglGetFragDataIndex
    cglGetFragDataIndex = <PFNGLGETFRAGDATAINDEXPROC>getFunction("glGetFragDataIndex")
    cglGetFragDataIndex(program, name)

cdef void GetglGetQueryObjecti64v(GLuint id, GLenum pname, GLint64 *params):
    global cglGetQueryObjecti64v
    cglGetQueryObjecti64v = <PFNGLGETQUERYOBJECTI64VPROC>getFunction("glGetQueryObjecti64v")
    cglGetQueryObjecti64v(id, pname, params)

cdef void GetglGetQueryObjectui64v(GLuint id, GLenum pname, GLuint64 *params):
    global cglGetQueryObjectui64v
    cglGetQueryObjectui64v = <PFNGLGETQUERYOBJECTUI64VPROC>getFunction("glGetQueryObjectui64v")
    cglGetQueryObjectui64v(id, pname, params)

cdef void GetglGetSamplerParameterIiv(GLuint sampler, GLenum pname, GLint *params):
    global cglGetSamplerParameterIiv
    cglGetSamplerParameterIiv = <PFNGLGETSAMPLERPARAMETERIIVPROC>getFunction("glGetSamplerParameterIiv")
    cglGetSamplerParameterIiv(sampler, pname, params)

cdef void GetglGetSamplerParameterIuiv(GLuint sampler, GLenum pname, GLuint *params):
    global cglGetSamplerParameterIuiv
    cglGetSamplerParameterIuiv = <PFNGLGETSAMPLERPARAMETERIUIVPROC>getFunction("glGetSamplerParameterIuiv")
    cglGetSamplerParameterIuiv(sampler, pname, params)

cdef void GetglGetSamplerParameterfv(GLuint sampler, GLenum pname, GLfloat *params):
    global cglGetSamplerParameterfv
    cglGetSamplerParameterfv = <PFNGLGETSAMPLERPARAMETERFVPROC>getFunction("glGetSamplerParameterfv")
    cglGetSamplerParameterfv(sampler, pname, params)

cdef void GetglGetSamplerParameteriv(GLuint sampler, GLenum pname, GLint *params):
    global cglGetSamplerParameteriv
    cglGetSamplerParameteriv = <PFNGLGETSAMPLERPARAMETERIVPROC>getFunction("glGetSamplerParameteriv")
    cglGetSamplerParameteriv(sampler, pname, params)

cdef GLboolean GetglIsSampler(GLuint sampler):
    global cglIsSampler
    cglIsSampler = <PFNGLISSAMPLERPROC>getFunction("glIsSampler")
    cglIsSampler(sampler)

cdef void GetglMultiTexCoordP1ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP1ui
    cglMultiTexCoordP1ui = <PFNGLMULTITEXCOORDP1UIPROC>getFunction("glMultiTexCoordP1ui")
    cglMultiTexCoordP1ui(texture, type, coords)

cdef void GetglMultiTexCoordP1uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP1uiv
    cglMultiTexCoordP1uiv = <PFNGLMULTITEXCOORDP1UIVPROC>getFunction("glMultiTexCoordP1uiv")
    cglMultiTexCoordP1uiv(texture, type, coords)

cdef void GetglMultiTexCoordP2ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP2ui
    cglMultiTexCoordP2ui = <PFNGLMULTITEXCOORDP2UIPROC>getFunction("glMultiTexCoordP2ui")
    cglMultiTexCoordP2ui(texture, type, coords)

cdef void GetglMultiTexCoordP2uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP2uiv
    cglMultiTexCoordP2uiv = <PFNGLMULTITEXCOORDP2UIVPROC>getFunction("glMultiTexCoordP2uiv")
    cglMultiTexCoordP2uiv(texture, type, coords)

cdef void GetglMultiTexCoordP3ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP3ui
    cglMultiTexCoordP3ui = <PFNGLMULTITEXCOORDP3UIPROC>getFunction("glMultiTexCoordP3ui")
    cglMultiTexCoordP3ui(texture, type, coords)

cdef void GetglMultiTexCoordP3uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP3uiv
    cglMultiTexCoordP3uiv = <PFNGLMULTITEXCOORDP3UIVPROC>getFunction("glMultiTexCoordP3uiv")
    cglMultiTexCoordP3uiv(texture, type, coords)

cdef void GetglMultiTexCoordP4ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP4ui
    cglMultiTexCoordP4ui = <PFNGLMULTITEXCOORDP4UIPROC>getFunction("glMultiTexCoordP4ui")
    cglMultiTexCoordP4ui(texture, type, coords)

cdef void GetglMultiTexCoordP4uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP4uiv
    cglMultiTexCoordP4uiv = <PFNGLMULTITEXCOORDP4UIVPROC>getFunction("glMultiTexCoordP4uiv")
    cglMultiTexCoordP4uiv(texture, type, coords)

cdef void GetglNormalP3ui(GLenum type, GLuint coords):
    global cglNormalP3ui
    cglNormalP3ui = <PFNGLNORMALP3UIPROC>getFunction("glNormalP3ui")
    cglNormalP3ui(type, coords)

cdef void GetglNormalP3uiv(GLenum type, const GLuint *coords):
    global cglNormalP3uiv
    cglNormalP3uiv = <PFNGLNORMALP3UIVPROC>getFunction("glNormalP3uiv")
    cglNormalP3uiv(type, coords)

cdef void GetglQueryCounter(GLuint id, GLenum target):
    global cglQueryCounter
    cglQueryCounter = <PFNGLQUERYCOUNTERPROC>getFunction("glQueryCounter")
    cglQueryCounter(id, target)

cdef void GetglSamplerParameterIiv(GLuint sampler, GLenum pname, const GLint *param):
    global cglSamplerParameterIiv
    cglSamplerParameterIiv = <PFNGLSAMPLERPARAMETERIIVPROC>getFunction("glSamplerParameterIiv")
    cglSamplerParameterIiv(sampler, pname, param)

cdef void GetglSamplerParameterIuiv(GLuint sampler, GLenum pname, const GLuint *param):
    global cglSamplerParameterIuiv
    cglSamplerParameterIuiv = <PFNGLSAMPLERPARAMETERIUIVPROC>getFunction("glSamplerParameterIuiv")
    cglSamplerParameterIuiv(sampler, pname, param)

cdef void GetglSamplerParameterf(GLuint sampler, GLenum pname, GLfloat param):
    global cglSamplerParameterf
    cglSamplerParameterf = <PFNGLSAMPLERPARAMETERFPROC>getFunction("glSamplerParameterf")
    cglSamplerParameterf(sampler, pname, param)

cdef void GetglSamplerParameterfv(GLuint sampler, GLenum pname, const GLfloat *param):
    global cglSamplerParameterfv
    cglSamplerParameterfv = <PFNGLSAMPLERPARAMETERFVPROC>getFunction("glSamplerParameterfv")
    cglSamplerParameterfv(sampler, pname, param)

cdef void GetglSamplerParameteri(GLuint sampler, GLenum pname, GLint param):
    global cglSamplerParameteri
    cglSamplerParameteri = <PFNGLSAMPLERPARAMETERIPROC>getFunction("glSamplerParameteri")
    cglSamplerParameteri(sampler, pname, param)

cdef void GetglSamplerParameteriv(GLuint sampler, GLenum pname, const GLint *param):
    global cglSamplerParameteriv
    cglSamplerParameteriv = <PFNGLSAMPLERPARAMETERIVPROC>getFunction("glSamplerParameteriv")
    cglSamplerParameteriv(sampler, pname, param)

cdef void GetglSecondaryColorP3ui(GLenum type, GLuint color):
    global cglSecondaryColorP3ui
    cglSecondaryColorP3ui = <PFNGLSECONDARYCOLORP3UIPROC>getFunction("glSecondaryColorP3ui")
    cglSecondaryColorP3ui(type, color)

cdef void GetglSecondaryColorP3uiv(GLenum type, const GLuint *color):
    global cglSecondaryColorP3uiv
    cglSecondaryColorP3uiv = <PFNGLSECONDARYCOLORP3UIVPROC>getFunction("glSecondaryColorP3uiv")
    cglSecondaryColorP3uiv(type, color)

cdef void GetglTexCoordP1ui(GLenum type, GLuint coords):
    global cglTexCoordP1ui
    cglTexCoordP1ui = <PFNGLTEXCOORDP1UIPROC>getFunction("glTexCoordP1ui")
    cglTexCoordP1ui(type, coords)

cdef void GetglTexCoordP1uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP1uiv
    cglTexCoordP1uiv = <PFNGLTEXCOORDP1UIVPROC>getFunction("glTexCoordP1uiv")
    cglTexCoordP1uiv(type, coords)

cdef void GetglTexCoordP2ui(GLenum type, GLuint coords):
    global cglTexCoordP2ui
    cglTexCoordP2ui = <PFNGLTEXCOORDP2UIPROC>getFunction("glTexCoordP2ui")
    cglTexCoordP2ui(type, coords)

cdef void GetglTexCoordP2uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP2uiv
    cglTexCoordP2uiv = <PFNGLTEXCOORDP2UIVPROC>getFunction("glTexCoordP2uiv")
    cglTexCoordP2uiv(type, coords)

cdef void GetglTexCoordP3ui(GLenum type, GLuint coords):
    global cglTexCoordP3ui
    cglTexCoordP3ui = <PFNGLTEXCOORDP3UIPROC>getFunction("glTexCoordP3ui")
    cglTexCoordP3ui(type, coords)

cdef void GetglTexCoordP3uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP3uiv
    cglTexCoordP3uiv = <PFNGLTEXCOORDP3UIVPROC>getFunction("glTexCoordP3uiv")
    cglTexCoordP3uiv(type, coords)

cdef void GetglTexCoordP4ui(GLenum type, GLuint coords):
    global cglTexCoordP4ui
    cglTexCoordP4ui = <PFNGLTEXCOORDP4UIPROC>getFunction("glTexCoordP4ui")
    cglTexCoordP4ui(type, coords)

cdef void GetglTexCoordP4uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP4uiv
    cglTexCoordP4uiv = <PFNGLTEXCOORDP4UIVPROC>getFunction("glTexCoordP4uiv")
    cglTexCoordP4uiv(type, coords)

cdef void GetglVertexAttribDivisor(GLuint index, GLuint divisor):
    global cglVertexAttribDivisor
    cglVertexAttribDivisor = <PFNGLVERTEXATTRIBDIVISORPROC>getFunction("glVertexAttribDivisor")
    cglVertexAttribDivisor(index, divisor)

cdef void GetglVertexAttribP1ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP1ui
    cglVertexAttribP1ui = <PFNGLVERTEXATTRIBP1UIPROC>getFunction("glVertexAttribP1ui")
    cglVertexAttribP1ui(index, type, normalized, value)

cdef void GetglVertexAttribP1uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP1uiv
    cglVertexAttribP1uiv = <PFNGLVERTEXATTRIBP1UIVPROC>getFunction("glVertexAttribP1uiv")
    cglVertexAttribP1uiv(index, type, normalized, value)

cdef void GetglVertexAttribP2ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP2ui
    cglVertexAttribP2ui = <PFNGLVERTEXATTRIBP2UIPROC>getFunction("glVertexAttribP2ui")
    cglVertexAttribP2ui(index, type, normalized, value)

cdef void GetglVertexAttribP2uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP2uiv
    cglVertexAttribP2uiv = <PFNGLVERTEXATTRIBP2UIVPROC>getFunction("glVertexAttribP2uiv")
    cglVertexAttribP2uiv(index, type, normalized, value)

cdef void GetglVertexAttribP3ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP3ui
    cglVertexAttribP3ui = <PFNGLVERTEXATTRIBP3UIPROC>getFunction("glVertexAttribP3ui")
    cglVertexAttribP3ui(index, type, normalized, value)

cdef void GetglVertexAttribP3uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP3uiv
    cglVertexAttribP3uiv = <PFNGLVERTEXATTRIBP3UIVPROC>getFunction("glVertexAttribP3uiv")
    cglVertexAttribP3uiv(index, type, normalized, value)

cdef void GetglVertexAttribP4ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP4ui
    cglVertexAttribP4ui = <PFNGLVERTEXATTRIBP4UIPROC>getFunction("glVertexAttribP4ui")
    cglVertexAttribP4ui(index, type, normalized, value)

cdef void GetglVertexAttribP4uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP4uiv
    cglVertexAttribP4uiv = <PFNGLVERTEXATTRIBP4UIVPROC>getFunction("glVertexAttribP4uiv")
    cglVertexAttribP4uiv(index, type, normalized, value)

cdef void GetglVertexP2ui(GLenum type, GLuint value):
    global cglVertexP2ui
    cglVertexP2ui = <PFNGLVERTEXP2UIPROC>getFunction("glVertexP2ui")
    cglVertexP2ui(type, value)

cdef void GetglVertexP2uiv(GLenum type, const GLuint *value):
    global cglVertexP2uiv
    cglVertexP2uiv = <PFNGLVERTEXP2UIVPROC>getFunction("glVertexP2uiv")
    cglVertexP2uiv(type, value)

cdef void GetglVertexP3ui(GLenum type, GLuint value):
    global cglVertexP3ui
    cglVertexP3ui = <PFNGLVERTEXP3UIPROC>getFunction("glVertexP3ui")
    cglVertexP3ui(type, value)

cdef void GetglVertexP3uiv(GLenum type, const GLuint *value):
    global cglVertexP3uiv
    cglVertexP3uiv = <PFNGLVERTEXP3UIVPROC>getFunction("glVertexP3uiv")
    cglVertexP3uiv(type, value)

cdef void GetglVertexP4ui(GLenum type, GLuint value):
    global cglVertexP4ui
    cglVertexP4ui = <PFNGLVERTEXP4UIPROC>getFunction("glVertexP4ui")
    cglVertexP4ui(type, value)

cdef void GetglVertexP4uiv(GLenum type, const GLuint *value):
    global cglVertexP4uiv
    cglVertexP4uiv = <PFNGLVERTEXP4UIVPROC>getFunction("glVertexP4uiv")
    cglVertexP4uiv(type, value)

cglBindFragDataLocationIndexed = GetglBindFragDataLocationIndexed
cglBindSampler = GetglBindSampler
cglColorP3ui = GetglColorP3ui
cglColorP3uiv = GetglColorP3uiv
cglColorP4ui = GetglColorP4ui
cglColorP4uiv = GetglColorP4uiv
cglDeleteSamplers = GetglDeleteSamplers
cglGenSamplers = GetglGenSamplers
cglGetFragDataIndex = GetglGetFragDataIndex
cglGetQueryObjecti64v = GetglGetQueryObjecti64v
cglGetQueryObjectui64v = GetglGetQueryObjectui64v
cglGetSamplerParameterIiv = GetglGetSamplerParameterIiv
cglGetSamplerParameterIuiv = GetglGetSamplerParameterIuiv
cglGetSamplerParameterfv = GetglGetSamplerParameterfv
cglGetSamplerParameteriv = GetglGetSamplerParameteriv
cglIsSampler = GetglIsSampler
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
cglQueryCounter = GetglQueryCounter
cglSamplerParameterIiv = GetglSamplerParameterIiv
cglSamplerParameterIuiv = GetglSamplerParameterIuiv
cglSamplerParameterf = GetglSamplerParameterf
cglSamplerParameterfv = GetglSamplerParameterfv
cglSamplerParameteri = GetglSamplerParameteri
cglSamplerParameteriv = GetglSamplerParameteriv
cglSecondaryColorP3ui = GetglSecondaryColorP3ui
cglSecondaryColorP3uiv = GetglSecondaryColorP3uiv
cglTexCoordP1ui = GetglTexCoordP1ui
cglTexCoordP1uiv = GetglTexCoordP1uiv
cglTexCoordP2ui = GetglTexCoordP2ui
cglTexCoordP2uiv = GetglTexCoordP2uiv
cglTexCoordP3ui = GetglTexCoordP3ui
cglTexCoordP3uiv = GetglTexCoordP3uiv
cglTexCoordP4ui = GetglTexCoordP4ui
cglTexCoordP4uiv = GetglTexCoordP4uiv
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


cdef void glBindFragDataLocationIndexed(GLuint program, GLuint colorNumber, GLuint index, const GLchar *name):
    cglBindFragDataLocationIndexed(program, colorNumber, index, name)

cdef void glBindSampler(GLuint unit, GLuint sampler):
    cglBindSampler(unit, sampler)

cdef void glColorP3ui(GLenum type, GLuint color):
    cglColorP3ui(type, color)

cdef void glColorP3uiv(GLenum type, const GLuint *color):
    cglColorP3uiv(type, color)

cdef void glColorP4ui(GLenum type, GLuint color):
    cglColorP4ui(type, color)

cdef void glColorP4uiv(GLenum type, const GLuint *color):
    cglColorP4uiv(type, color)

cdef void glDeleteSamplers(GLsizei count, const GLuint *samplers):
    cglDeleteSamplers(count, samplers)

cdef void glGenSamplers(GLsizei count, GLuint *samplers):
    cglGenSamplers(count, samplers)

cdef GLint glGetFragDataIndex(GLuint program, const GLchar *name):
    cglGetFragDataIndex(program, name)

cdef void glGetQueryObjecti64v(GLuint id, GLenum pname, GLint64 *params):
    cglGetQueryObjecti64v(id, pname, params)

cdef void glGetQueryObjectui64v(GLuint id, GLenum pname, GLuint64 *params):
    cglGetQueryObjectui64v(id, pname, params)

cdef void glGetSamplerParameterIiv(GLuint sampler, GLenum pname, GLint *params):
    cglGetSamplerParameterIiv(sampler, pname, params)

cdef void glGetSamplerParameterIuiv(GLuint sampler, GLenum pname, GLuint *params):
    cglGetSamplerParameterIuiv(sampler, pname, params)

cdef void glGetSamplerParameterfv(GLuint sampler, GLenum pname, GLfloat *params):
    cglGetSamplerParameterfv(sampler, pname, params)

cdef void glGetSamplerParameteriv(GLuint sampler, GLenum pname, GLint *params):
    cglGetSamplerParameteriv(sampler, pname, params)

cdef GLboolean glIsSampler(GLuint sampler):
    cglIsSampler(sampler)

cdef void glMultiTexCoordP1ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP1ui(texture, type, coords)

cdef void glMultiTexCoordP1uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP1uiv(texture, type, coords)

cdef void glMultiTexCoordP2ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP2ui(texture, type, coords)

cdef void glMultiTexCoordP2uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP2uiv(texture, type, coords)

cdef void glMultiTexCoordP3ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP3ui(texture, type, coords)

cdef void glMultiTexCoordP3uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP3uiv(texture, type, coords)

cdef void glMultiTexCoordP4ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP4ui(texture, type, coords)

cdef void glMultiTexCoordP4uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP4uiv(texture, type, coords)

cdef void glNormalP3ui(GLenum type, GLuint coords):
    cglNormalP3ui(type, coords)

cdef void glNormalP3uiv(GLenum type, const GLuint *coords):
    cglNormalP3uiv(type, coords)

cdef void glQueryCounter(GLuint id, GLenum target):
    cglQueryCounter(id, target)

cdef void glSamplerParameterIiv(GLuint sampler, GLenum pname, const GLint *param):
    cglSamplerParameterIiv(sampler, pname, param)

cdef void glSamplerParameterIuiv(GLuint sampler, GLenum pname, const GLuint *param):
    cglSamplerParameterIuiv(sampler, pname, param)

cdef void glSamplerParameterf(GLuint sampler, GLenum pname, GLfloat param):
    cglSamplerParameterf(sampler, pname, param)

cdef void glSamplerParameterfv(GLuint sampler, GLenum pname, const GLfloat *param):
    cglSamplerParameterfv(sampler, pname, param)

cdef void glSamplerParameteri(GLuint sampler, GLenum pname, GLint param):
    cglSamplerParameteri(sampler, pname, param)

cdef void glSamplerParameteriv(GLuint sampler, GLenum pname, const GLint *param):
    cglSamplerParameteriv(sampler, pname, param)

cdef void glSecondaryColorP3ui(GLenum type, GLuint color):
    cglSecondaryColorP3ui(type, color)

cdef void glSecondaryColorP3uiv(GLenum type, const GLuint *color):
    cglSecondaryColorP3uiv(type, color)

cdef void glTexCoordP1ui(GLenum type, GLuint coords):
    cglTexCoordP1ui(type, coords)

cdef void glTexCoordP1uiv(GLenum type, const GLuint *coords):
    cglTexCoordP1uiv(type, coords)

cdef void glTexCoordP2ui(GLenum type, GLuint coords):
    cglTexCoordP2ui(type, coords)

cdef void glTexCoordP2uiv(GLenum type, const GLuint *coords):
    cglTexCoordP2uiv(type, coords)

cdef void glTexCoordP3ui(GLenum type, GLuint coords):
    cglTexCoordP3ui(type, coords)

cdef void glTexCoordP3uiv(GLenum type, const GLuint *coords):
    cglTexCoordP3uiv(type, coords)

cdef void glTexCoordP4ui(GLenum type, GLuint coords):
    cglTexCoordP4ui(type, coords)

cdef void glTexCoordP4uiv(GLenum type, const GLuint *coords):
    cglTexCoordP4uiv(type, coords)

cdef void glVertexAttribDivisor(GLuint index, GLuint divisor):
    cglVertexAttribDivisor(index, divisor)

cdef void glVertexAttribP1ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP1ui(index, type, normalized, value)

cdef void glVertexAttribP1uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP1uiv(index, type, normalized, value)

cdef void glVertexAttribP2ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP2ui(index, type, normalized, value)

cdef void glVertexAttribP2uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP2uiv(index, type, normalized, value)

cdef void glVertexAttribP3ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP3ui(index, type, normalized, value)

cdef void glVertexAttribP3uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP3uiv(index, type, normalized, value)

cdef void glVertexAttribP4ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP4ui(index, type, normalized, value)

cdef void glVertexAttribP4uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP4uiv(index, type, normalized, value)

cdef void glVertexP2ui(GLenum type, GLuint value):
    cglVertexP2ui(type, value)

cdef void glVertexP2uiv(GLenum type, const GLuint *value):
    cglVertexP2uiv(type, value)

cdef void glVertexP3ui(GLenum type, GLuint value):
    cglVertexP3ui(type, value)

cdef void glVertexP3uiv(GLenum type, const GLuint *value):
    cglVertexP3uiv(type, value)

cdef void glVertexP4ui(GLenum type, GLuint value):
    cglVertexP4ui(type, value)

cdef void glVertexP4uiv(GLenum type, const GLuint *value):
    cglVertexP4uiv(type, value)
