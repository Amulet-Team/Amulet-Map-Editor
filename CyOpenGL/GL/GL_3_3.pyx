# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_TIMESTAMP = 0x8E28
cdef GLenum GL_INT_2_10_10_10_REV = 0x8D9F
cdef GLenum GL_ONE_MINUS_SRC1_COLOR = 0x88FA
cdef GLenum GL_ONE_MINUS_SRC1_ALPHA = 0x88FB
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_DIVISOR = 0x88FE
cdef GLenum GL_TEXTURE_SWIZZLE_B = 0x8E44
cdef GLenum GL_ANY_SAMPLES_PASSED = 0x8C2F
cdef GLenum GL_TEXTURE_SWIZZLE_A = 0x8E45
cdef GLenum GL_TEXTURE_SWIZZLE_RGBA = 0x8E46
cdef GLenum GL_SAMPLER_BINDING = 0x8919
cdef GLenum GL_TEXTURE_SWIZZLE_G = 0x8E43
cdef GLenum GL_TIME_ELAPSED = 0x88BF
cdef GLenum GL_RGB10_A2UI = 0x906F
cdef GLenum GL_TEXTURE_SWIZZLE_R = 0x8E42
cdef GLenum GL_SRC1_COLOR = 0x88F9
cdef GLenum GL_MAX_DUAL_SOURCE_DRAW_BUFFERS = 0x88FC

ctypedef void (*PFNGLCOLORP3UIVPROC)(GLenum type, const GLuint *color)
ctypedef void (*PFNGLSAMPLERPARAMETERIUIVPROC)(GLuint sampler, GLenum pname, const GLuint *param)
ctypedef void (*PFNGLGETQUERYOBJECTUI64VPROC)(GLuint id, GLenum pname, GLuint64 *params)
ctypedef void (*PFNGLGETSAMPLERPARAMETERFVPROC)(GLuint sampler, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLVERTEXP4UIVPROC)(GLenum type, const GLuint *value)
ctypedef void (*PFNGLVERTEXATTRIBP2UIVPROC)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*PFNGLVERTEXATTRIBP4UIVPROC)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*PFNGLVERTEXP4UIPROC)(GLenum type, GLuint value)
ctypedef void (*PFNGLQUERYCOUNTERPROC)(GLuint id, GLenum target)
ctypedef void (*PFNGLTEXCOORDP3UIVPROC)(GLenum type, const GLuint *coords)
ctypedef void (*PFNGLMULTITEXCOORDP2UIVPROC)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*PFNGLTEXCOORDP2UIVPROC)(GLenum type, const GLuint *coords)
ctypedef void (*PFNGLMULTITEXCOORDP3UIPROC)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*PFNGLMULTITEXCOORDP4UIPROC)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*PFNGLDELETESAMPLERSPROC)(GLsizei count, const GLuint *samplers)
ctypedef void (*PFNGLVERTEXATTRIBP1UIVPROC)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef void (*PFNGLMULTITEXCOORDP2UIPROC)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*PFNGLTEXCOORDP2UIPROC)(GLenum type, GLuint coords)
ctypedef void (*PFNGLNORMALP3UIVPROC)(GLenum type, const GLuint *coords)
ctypedef void (*PFNGLVERTEXATTRIBP1UIPROC)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*PFNGLCOLORP4UIVPROC)(GLenum type, const GLuint *color)
ctypedef void (*PFNGLSAMPLERPARAMETERIVPROC)(GLuint sampler, GLenum pname, const GLint *param)
ctypedef void (*PFNGLMULTITEXCOORDP4UIVPROC)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef GLint (*PFNGLGETFRAGDATAINDEXPROC)(GLuint program, const GLchar *name)
ctypedef void (*PFNGLSAMPLERPARAMETERFVPROC)(GLuint sampler, GLenum pname, const GLfloat *param)
ctypedef void (*PFNGLSAMPLERPARAMETERIPROC)(GLuint sampler, GLenum pname, GLint param)
ctypedef void (*PFNGLVERTEXATTRIBP3UIPROC)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*PFNGLBINDSAMPLERPROC)(GLuint unit, GLuint sampler)
ctypedef void (*PFNGLVERTEXATTRIBP3UIVPROC)(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
ctypedef GLboolean (*PFNGLISSAMPLERPROC)(GLuint sampler)
ctypedef void (*PFNGLMULTITEXCOORDP1UIPROC)(GLenum texture, GLenum type, GLuint coords)
ctypedef void (*PFNGLVERTEXP3UIVPROC)(GLenum type, const GLuint *value)
ctypedef void (*PFNGLTEXCOORDP4UIVPROC)(GLenum type, const GLuint *coords)
ctypedef void (*PFNGLSAMPLERPARAMETERFPROC)(GLuint sampler, GLenum pname, GLfloat param)
ctypedef void (*PFNGLSECONDARYCOLORP3UIPROC)(GLenum type, GLuint color)
ctypedef void (*PFNGLGENSAMPLERSPROC)(GLsizei count, GLuint *samplers)
ctypedef void (*PFNGLGETSAMPLERPARAMETERIUIVPROC)(GLuint sampler, GLenum pname, GLuint *params)
ctypedef void (*PFNGLMULTITEXCOORDP1UIVPROC)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*PFNGLGETQUERYOBJECTI64VPROC)(GLuint id, GLenum pname, GLint64 *params)
ctypedef void (*PFNGLTEXCOORDP4UIPROC)(GLenum type, GLuint coords)
ctypedef void (*PFNGLSECONDARYCOLORP3UIVPROC)(GLenum type, const GLuint *color)
ctypedef void (*PFNGLBINDFRAGDATALOCATIONINDEXEDPROC)(GLuint program, GLuint colorNumber, GLuint index, const GLchar *name)
ctypedef void (*PFNGLTEXCOORDP1UIPROC)(GLenum type, GLuint coords)
ctypedef void (*PFNGLNORMALP3UIPROC)(GLenum type, GLuint coords)
ctypedef void (*PFNGLVERTEXP3UIPROC)(GLenum type, GLuint value)
ctypedef void (*PFNGLSAMPLERPARAMETERIIVPROC)(GLuint sampler, GLenum pname, const GLint *param)
ctypedef void (*PFNGLVERTEXP2UIPROC)(GLenum type, GLuint value)
ctypedef void (*PFNGLTEXCOORDP1UIVPROC)(GLenum type, const GLuint *coords)
ctypedef void (*PFNGLGETSAMPLERPARAMETERIVPROC)(GLuint sampler, GLenum pname, GLint *params)
ctypedef void (*PFNGLVERTEXATTRIBP2UIPROC)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*PFNGLTEXCOORDP3UIPROC)(GLenum type, GLuint coords)
ctypedef void (*PFNGLVERTEXATTRIBDIVISORPROC)(GLuint index, GLuint divisor)
ctypedef void (*PFNGLMULTITEXCOORDP3UIVPROC)(GLenum texture, GLenum type, const GLuint *coords)
ctypedef void (*PFNGLCOLORP3UIPROC)(GLenum type, GLuint color)
ctypedef void (*PFNGLVERTEXATTRIBP4UIPROC)(GLuint index, GLenum type, GLboolean normalized, GLuint value)
ctypedef void (*PFNGLCOLORP4UIPROC)(GLenum type, GLuint color)
ctypedef void (*PFNGLVERTEXP2UIVPROC)(GLenum type, const GLuint *value)
ctypedef void (*PFNGLGETSAMPLERPARAMETERIIVPROC)(GLuint sampler, GLenum pname, GLint *params)

cdef PFNGLCOLORP3UIVPROC cglColorP3uiv = NULL
cdef PFNGLSAMPLERPARAMETERIUIVPROC cglSamplerParameterIuiv = NULL
cdef PFNGLGETQUERYOBJECTUI64VPROC cglGetQueryObjectui64v = NULL
cdef PFNGLGETSAMPLERPARAMETERFVPROC cglGetSamplerParameterfv = NULL
cdef PFNGLVERTEXP4UIVPROC cglVertexP4uiv = NULL
cdef PFNGLVERTEXATTRIBP2UIVPROC cglVertexAttribP2uiv = NULL
cdef PFNGLVERTEXATTRIBP4UIVPROC cglVertexAttribP4uiv = NULL
cdef PFNGLVERTEXP4UIPROC cglVertexP4ui = NULL
cdef PFNGLQUERYCOUNTERPROC cglQueryCounter = NULL
cdef PFNGLTEXCOORDP3UIVPROC cglTexCoordP3uiv = NULL
cdef PFNGLMULTITEXCOORDP2UIVPROC cglMultiTexCoordP2uiv = NULL
cdef PFNGLTEXCOORDP2UIVPROC cglTexCoordP2uiv = NULL
cdef PFNGLMULTITEXCOORDP3UIPROC cglMultiTexCoordP3ui = NULL
cdef PFNGLMULTITEXCOORDP4UIPROC cglMultiTexCoordP4ui = NULL
cdef PFNGLDELETESAMPLERSPROC cglDeleteSamplers = NULL
cdef PFNGLVERTEXATTRIBP1UIVPROC cglVertexAttribP1uiv = NULL
cdef PFNGLMULTITEXCOORDP2UIPROC cglMultiTexCoordP2ui = NULL
cdef PFNGLTEXCOORDP2UIPROC cglTexCoordP2ui = NULL
cdef PFNGLNORMALP3UIVPROC cglNormalP3uiv = NULL
cdef PFNGLVERTEXATTRIBP1UIPROC cglVertexAttribP1ui = NULL
cdef PFNGLCOLORP4UIVPROC cglColorP4uiv = NULL
cdef PFNGLSAMPLERPARAMETERIVPROC cglSamplerParameteriv = NULL
cdef PFNGLMULTITEXCOORDP4UIVPROC cglMultiTexCoordP4uiv = NULL
cdef PFNGLGETFRAGDATAINDEXPROC cglGetFragDataIndex = NULL
cdef PFNGLSAMPLERPARAMETERFVPROC cglSamplerParameterfv = NULL
cdef PFNGLSAMPLERPARAMETERIPROC cglSamplerParameteri = NULL
cdef PFNGLVERTEXATTRIBP3UIPROC cglVertexAttribP3ui = NULL
cdef PFNGLBINDSAMPLERPROC cglBindSampler = NULL
cdef PFNGLVERTEXATTRIBP3UIVPROC cglVertexAttribP3uiv = NULL
cdef PFNGLISSAMPLERPROC cglIsSampler = NULL
cdef PFNGLMULTITEXCOORDP1UIPROC cglMultiTexCoordP1ui = NULL
cdef PFNGLVERTEXP3UIVPROC cglVertexP3uiv = NULL
cdef PFNGLTEXCOORDP4UIVPROC cglTexCoordP4uiv = NULL
cdef PFNGLSAMPLERPARAMETERFPROC cglSamplerParameterf = NULL
cdef PFNGLSECONDARYCOLORP3UIPROC cglSecondaryColorP3ui = NULL
cdef PFNGLGENSAMPLERSPROC cglGenSamplers = NULL
cdef PFNGLGETSAMPLERPARAMETERIUIVPROC cglGetSamplerParameterIuiv = NULL
cdef PFNGLMULTITEXCOORDP1UIVPROC cglMultiTexCoordP1uiv = NULL
cdef PFNGLGETQUERYOBJECTI64VPROC cglGetQueryObjecti64v = NULL
cdef PFNGLTEXCOORDP4UIPROC cglTexCoordP4ui = NULL
cdef PFNGLSECONDARYCOLORP3UIVPROC cglSecondaryColorP3uiv = NULL
cdef PFNGLBINDFRAGDATALOCATIONINDEXEDPROC cglBindFragDataLocationIndexed = NULL
cdef PFNGLTEXCOORDP1UIPROC cglTexCoordP1ui = NULL
cdef PFNGLNORMALP3UIPROC cglNormalP3ui = NULL
cdef PFNGLVERTEXP3UIPROC cglVertexP3ui = NULL
cdef PFNGLSAMPLERPARAMETERIIVPROC cglSamplerParameterIiv = NULL
cdef PFNGLVERTEXP2UIPROC cglVertexP2ui = NULL
cdef PFNGLTEXCOORDP1UIVPROC cglTexCoordP1uiv = NULL
cdef PFNGLGETSAMPLERPARAMETERIVPROC cglGetSamplerParameteriv = NULL
cdef PFNGLVERTEXATTRIBP2UIPROC cglVertexAttribP2ui = NULL
cdef PFNGLTEXCOORDP3UIPROC cglTexCoordP3ui = NULL
cdef PFNGLVERTEXATTRIBDIVISORPROC cglVertexAttribDivisor = NULL
cdef PFNGLMULTITEXCOORDP3UIVPROC cglMultiTexCoordP3uiv = NULL
cdef PFNGLCOLORP3UIPROC cglColorP3ui = NULL
cdef PFNGLVERTEXATTRIBP4UIPROC cglVertexAttribP4ui = NULL
cdef PFNGLCOLORP4UIPROC cglColorP4ui = NULL
cdef PFNGLVERTEXP2UIVPROC cglVertexP2uiv = NULL
cdef PFNGLGETSAMPLERPARAMETERIIVPROC cglGetSamplerParameterIiv = NULL


cdef void GetglColorP3uiv(GLenum type, const GLuint *color):
    global cglColorP3uiv
    cglColorP3uiv = <PFNGLCOLORP3UIVPROC>getFunction(b"glColorP3uiv")
    cglColorP3uiv(type, color)

cdef void GetglSamplerParameterIuiv(GLuint sampler, GLenum pname, const GLuint *param):
    global cglSamplerParameterIuiv
    cglSamplerParameterIuiv = <PFNGLSAMPLERPARAMETERIUIVPROC>getFunction(b"glSamplerParameterIuiv")
    cglSamplerParameterIuiv(sampler, pname, param)

cdef void GetglGetQueryObjectui64v(GLuint id, GLenum pname, GLuint64 *params):
    global cglGetQueryObjectui64v
    cglGetQueryObjectui64v = <PFNGLGETQUERYOBJECTUI64VPROC>getFunction(b"glGetQueryObjectui64v")
    cglGetQueryObjectui64v(id, pname, params)

cdef void GetglGetSamplerParameterfv(GLuint sampler, GLenum pname, GLfloat *params):
    global cglGetSamplerParameterfv
    cglGetSamplerParameterfv = <PFNGLGETSAMPLERPARAMETERFVPROC>getFunction(b"glGetSamplerParameterfv")
    cglGetSamplerParameterfv(sampler, pname, params)

cdef void GetglVertexP4uiv(GLenum type, const GLuint *value):
    global cglVertexP4uiv
    cglVertexP4uiv = <PFNGLVERTEXP4UIVPROC>getFunction(b"glVertexP4uiv")
    cglVertexP4uiv(type, value)

cdef void GetglVertexAttribP2uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP2uiv
    cglVertexAttribP2uiv = <PFNGLVERTEXATTRIBP2UIVPROC>getFunction(b"glVertexAttribP2uiv")
    cglVertexAttribP2uiv(index, type, normalized, value)

cdef void GetglVertexAttribP4uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP4uiv
    cglVertexAttribP4uiv = <PFNGLVERTEXATTRIBP4UIVPROC>getFunction(b"glVertexAttribP4uiv")
    cglVertexAttribP4uiv(index, type, normalized, value)

cdef void GetglVertexP4ui(GLenum type, GLuint value):
    global cglVertexP4ui
    cglVertexP4ui = <PFNGLVERTEXP4UIPROC>getFunction(b"glVertexP4ui")
    cglVertexP4ui(type, value)

cdef void GetglQueryCounter(GLuint id, GLenum target):
    global cglQueryCounter
    cglQueryCounter = <PFNGLQUERYCOUNTERPROC>getFunction(b"glQueryCounter")
    cglQueryCounter(id, target)

cdef void GetglTexCoordP3uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP3uiv
    cglTexCoordP3uiv = <PFNGLTEXCOORDP3UIVPROC>getFunction(b"glTexCoordP3uiv")
    cglTexCoordP3uiv(type, coords)

cdef void GetglMultiTexCoordP2uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP2uiv
    cglMultiTexCoordP2uiv = <PFNGLMULTITEXCOORDP2UIVPROC>getFunction(b"glMultiTexCoordP2uiv")
    cglMultiTexCoordP2uiv(texture, type, coords)

cdef void GetglTexCoordP2uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP2uiv
    cglTexCoordP2uiv = <PFNGLTEXCOORDP2UIVPROC>getFunction(b"glTexCoordP2uiv")
    cglTexCoordP2uiv(type, coords)

cdef void GetglMultiTexCoordP3ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP3ui
    cglMultiTexCoordP3ui = <PFNGLMULTITEXCOORDP3UIPROC>getFunction(b"glMultiTexCoordP3ui")
    cglMultiTexCoordP3ui(texture, type, coords)

cdef void GetglMultiTexCoordP4ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP4ui
    cglMultiTexCoordP4ui = <PFNGLMULTITEXCOORDP4UIPROC>getFunction(b"glMultiTexCoordP4ui")
    cglMultiTexCoordP4ui(texture, type, coords)

cdef void GetglDeleteSamplers(GLsizei count, const GLuint *samplers):
    global cglDeleteSamplers
    cglDeleteSamplers = <PFNGLDELETESAMPLERSPROC>getFunction(b"glDeleteSamplers")
    cglDeleteSamplers(count, samplers)

cdef void GetglVertexAttribP1uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP1uiv
    cglVertexAttribP1uiv = <PFNGLVERTEXATTRIBP1UIVPROC>getFunction(b"glVertexAttribP1uiv")
    cglVertexAttribP1uiv(index, type, normalized, value)

cdef void GetglMultiTexCoordP2ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP2ui
    cglMultiTexCoordP2ui = <PFNGLMULTITEXCOORDP2UIPROC>getFunction(b"glMultiTexCoordP2ui")
    cglMultiTexCoordP2ui(texture, type, coords)

cdef void GetglTexCoordP2ui(GLenum type, GLuint coords):
    global cglTexCoordP2ui
    cglTexCoordP2ui = <PFNGLTEXCOORDP2UIPROC>getFunction(b"glTexCoordP2ui")
    cglTexCoordP2ui(type, coords)

cdef void GetglNormalP3uiv(GLenum type, const GLuint *coords):
    global cglNormalP3uiv
    cglNormalP3uiv = <PFNGLNORMALP3UIVPROC>getFunction(b"glNormalP3uiv")
    cglNormalP3uiv(type, coords)

cdef void GetglVertexAttribP1ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP1ui
    cglVertexAttribP1ui = <PFNGLVERTEXATTRIBP1UIPROC>getFunction(b"glVertexAttribP1ui")
    cglVertexAttribP1ui(index, type, normalized, value)

cdef void GetglColorP4uiv(GLenum type, const GLuint *color):
    global cglColorP4uiv
    cglColorP4uiv = <PFNGLCOLORP4UIVPROC>getFunction(b"glColorP4uiv")
    cglColorP4uiv(type, color)

cdef void GetglSamplerParameteriv(GLuint sampler, GLenum pname, const GLint *param):
    global cglSamplerParameteriv
    cglSamplerParameteriv = <PFNGLSAMPLERPARAMETERIVPROC>getFunction(b"glSamplerParameteriv")
    cglSamplerParameteriv(sampler, pname, param)

cdef void GetglMultiTexCoordP4uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP4uiv
    cglMultiTexCoordP4uiv = <PFNGLMULTITEXCOORDP4UIVPROC>getFunction(b"glMultiTexCoordP4uiv")
    cglMultiTexCoordP4uiv(texture, type, coords)

cdef GLint GetglGetFragDataIndex(GLuint program, const GLchar *name):
    global cglGetFragDataIndex
    cglGetFragDataIndex = <PFNGLGETFRAGDATAINDEXPROC>getFunction(b"glGetFragDataIndex")
    cglGetFragDataIndex(program, name)

cdef void GetglSamplerParameterfv(GLuint sampler, GLenum pname, const GLfloat *param):
    global cglSamplerParameterfv
    cglSamplerParameterfv = <PFNGLSAMPLERPARAMETERFVPROC>getFunction(b"glSamplerParameterfv")
    cglSamplerParameterfv(sampler, pname, param)

cdef void GetglSamplerParameteri(GLuint sampler, GLenum pname, GLint param):
    global cglSamplerParameteri
    cglSamplerParameteri = <PFNGLSAMPLERPARAMETERIPROC>getFunction(b"glSamplerParameteri")
    cglSamplerParameteri(sampler, pname, param)

cdef void GetglVertexAttribP3ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP3ui
    cglVertexAttribP3ui = <PFNGLVERTEXATTRIBP3UIPROC>getFunction(b"glVertexAttribP3ui")
    cglVertexAttribP3ui(index, type, normalized, value)

cdef void GetglBindSampler(GLuint unit, GLuint sampler):
    global cglBindSampler
    cglBindSampler = <PFNGLBINDSAMPLERPROC>getFunction(b"glBindSampler")
    cglBindSampler(unit, sampler)

cdef void GetglVertexAttribP3uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    global cglVertexAttribP3uiv
    cglVertexAttribP3uiv = <PFNGLVERTEXATTRIBP3UIVPROC>getFunction(b"glVertexAttribP3uiv")
    cglVertexAttribP3uiv(index, type, normalized, value)

cdef GLboolean GetglIsSampler(GLuint sampler):
    global cglIsSampler
    cglIsSampler = <PFNGLISSAMPLERPROC>getFunction(b"glIsSampler")
    cglIsSampler(sampler)

cdef void GetglMultiTexCoordP1ui(GLenum texture, GLenum type, GLuint coords):
    global cglMultiTexCoordP1ui
    cglMultiTexCoordP1ui = <PFNGLMULTITEXCOORDP1UIPROC>getFunction(b"glMultiTexCoordP1ui")
    cglMultiTexCoordP1ui(texture, type, coords)

cdef void GetglVertexP3uiv(GLenum type, const GLuint *value):
    global cglVertexP3uiv
    cglVertexP3uiv = <PFNGLVERTEXP3UIVPROC>getFunction(b"glVertexP3uiv")
    cglVertexP3uiv(type, value)

cdef void GetglTexCoordP4uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP4uiv
    cglTexCoordP4uiv = <PFNGLTEXCOORDP4UIVPROC>getFunction(b"glTexCoordP4uiv")
    cglTexCoordP4uiv(type, coords)

cdef void GetglSamplerParameterf(GLuint sampler, GLenum pname, GLfloat param):
    global cglSamplerParameterf
    cglSamplerParameterf = <PFNGLSAMPLERPARAMETERFPROC>getFunction(b"glSamplerParameterf")
    cglSamplerParameterf(sampler, pname, param)

cdef void GetglSecondaryColorP3ui(GLenum type, GLuint color):
    global cglSecondaryColorP3ui
    cglSecondaryColorP3ui = <PFNGLSECONDARYCOLORP3UIPROC>getFunction(b"glSecondaryColorP3ui")
    cglSecondaryColorP3ui(type, color)

cdef void GetglGenSamplers(GLsizei count, GLuint *samplers):
    global cglGenSamplers
    cglGenSamplers = <PFNGLGENSAMPLERSPROC>getFunction(b"glGenSamplers")
    cglGenSamplers(count, samplers)

cdef void GetglGetSamplerParameterIuiv(GLuint sampler, GLenum pname, GLuint *params):
    global cglGetSamplerParameterIuiv
    cglGetSamplerParameterIuiv = <PFNGLGETSAMPLERPARAMETERIUIVPROC>getFunction(b"glGetSamplerParameterIuiv")
    cglGetSamplerParameterIuiv(sampler, pname, params)

cdef void GetglMultiTexCoordP1uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP1uiv
    cglMultiTexCoordP1uiv = <PFNGLMULTITEXCOORDP1UIVPROC>getFunction(b"glMultiTexCoordP1uiv")
    cglMultiTexCoordP1uiv(texture, type, coords)

cdef void GetglGetQueryObjecti64v(GLuint id, GLenum pname, GLint64 *params):
    global cglGetQueryObjecti64v
    cglGetQueryObjecti64v = <PFNGLGETQUERYOBJECTI64VPROC>getFunction(b"glGetQueryObjecti64v")
    cglGetQueryObjecti64v(id, pname, params)

cdef void GetglTexCoordP4ui(GLenum type, GLuint coords):
    global cglTexCoordP4ui
    cglTexCoordP4ui = <PFNGLTEXCOORDP4UIPROC>getFunction(b"glTexCoordP4ui")
    cglTexCoordP4ui(type, coords)

cdef void GetglSecondaryColorP3uiv(GLenum type, const GLuint *color):
    global cglSecondaryColorP3uiv
    cglSecondaryColorP3uiv = <PFNGLSECONDARYCOLORP3UIVPROC>getFunction(b"glSecondaryColorP3uiv")
    cglSecondaryColorP3uiv(type, color)

cdef void GetglBindFragDataLocationIndexed(GLuint program, GLuint colorNumber, GLuint index, const GLchar *name):
    global cglBindFragDataLocationIndexed
    cglBindFragDataLocationIndexed = <PFNGLBINDFRAGDATALOCATIONINDEXEDPROC>getFunction(b"glBindFragDataLocationIndexed")
    cglBindFragDataLocationIndexed(program, colorNumber, index, name)

cdef void GetglTexCoordP1ui(GLenum type, GLuint coords):
    global cglTexCoordP1ui
    cglTexCoordP1ui = <PFNGLTEXCOORDP1UIPROC>getFunction(b"glTexCoordP1ui")
    cglTexCoordP1ui(type, coords)

cdef void GetglNormalP3ui(GLenum type, GLuint coords):
    global cglNormalP3ui
    cglNormalP3ui = <PFNGLNORMALP3UIPROC>getFunction(b"glNormalP3ui")
    cglNormalP3ui(type, coords)

cdef void GetglVertexP3ui(GLenum type, GLuint value):
    global cglVertexP3ui
    cglVertexP3ui = <PFNGLVERTEXP3UIPROC>getFunction(b"glVertexP3ui")
    cglVertexP3ui(type, value)

cdef void GetglSamplerParameterIiv(GLuint sampler, GLenum pname, const GLint *param):
    global cglSamplerParameterIiv
    cglSamplerParameterIiv = <PFNGLSAMPLERPARAMETERIIVPROC>getFunction(b"glSamplerParameterIiv")
    cglSamplerParameterIiv(sampler, pname, param)

cdef void GetglVertexP2ui(GLenum type, GLuint value):
    global cglVertexP2ui
    cglVertexP2ui = <PFNGLVERTEXP2UIPROC>getFunction(b"glVertexP2ui")
    cglVertexP2ui(type, value)

cdef void GetglTexCoordP1uiv(GLenum type, const GLuint *coords):
    global cglTexCoordP1uiv
    cglTexCoordP1uiv = <PFNGLTEXCOORDP1UIVPROC>getFunction(b"glTexCoordP1uiv")
    cglTexCoordP1uiv(type, coords)

cdef void GetglGetSamplerParameteriv(GLuint sampler, GLenum pname, GLint *params):
    global cglGetSamplerParameteriv
    cglGetSamplerParameteriv = <PFNGLGETSAMPLERPARAMETERIVPROC>getFunction(b"glGetSamplerParameteriv")
    cglGetSamplerParameteriv(sampler, pname, params)

cdef void GetglVertexAttribP2ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP2ui
    cglVertexAttribP2ui = <PFNGLVERTEXATTRIBP2UIPROC>getFunction(b"glVertexAttribP2ui")
    cglVertexAttribP2ui(index, type, normalized, value)

cdef void GetglTexCoordP3ui(GLenum type, GLuint coords):
    global cglTexCoordP3ui
    cglTexCoordP3ui = <PFNGLTEXCOORDP3UIPROC>getFunction(b"glTexCoordP3ui")
    cglTexCoordP3ui(type, coords)

cdef void GetglVertexAttribDivisor(GLuint index, GLuint divisor):
    global cglVertexAttribDivisor
    cglVertexAttribDivisor = <PFNGLVERTEXATTRIBDIVISORPROC>getFunction(b"glVertexAttribDivisor")
    cglVertexAttribDivisor(index, divisor)

cdef void GetglMultiTexCoordP3uiv(GLenum texture, GLenum type, const GLuint *coords):
    global cglMultiTexCoordP3uiv
    cglMultiTexCoordP3uiv = <PFNGLMULTITEXCOORDP3UIVPROC>getFunction(b"glMultiTexCoordP3uiv")
    cglMultiTexCoordP3uiv(texture, type, coords)

cdef void GetglColorP3ui(GLenum type, GLuint color):
    global cglColorP3ui
    cglColorP3ui = <PFNGLCOLORP3UIPROC>getFunction(b"glColorP3ui")
    cglColorP3ui(type, color)

cdef void GetglVertexAttribP4ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    global cglVertexAttribP4ui
    cglVertexAttribP4ui = <PFNGLVERTEXATTRIBP4UIPROC>getFunction(b"glVertexAttribP4ui")
    cglVertexAttribP4ui(index, type, normalized, value)

cdef void GetglColorP4ui(GLenum type, GLuint color):
    global cglColorP4ui
    cglColorP4ui = <PFNGLCOLORP4UIPROC>getFunction(b"glColorP4ui")
    cglColorP4ui(type, color)

cdef void GetglVertexP2uiv(GLenum type, const GLuint *value):
    global cglVertexP2uiv
    cglVertexP2uiv = <PFNGLVERTEXP2UIVPROC>getFunction(b"glVertexP2uiv")
    cglVertexP2uiv(type, value)

cdef void GetglGetSamplerParameterIiv(GLuint sampler, GLenum pname, GLint *params):
    global cglGetSamplerParameterIiv
    cglGetSamplerParameterIiv = <PFNGLGETSAMPLERPARAMETERIIVPROC>getFunction(b"glGetSamplerParameterIiv")
    cglGetSamplerParameterIiv(sampler, pname, params)

cglColorP3uiv = GetglColorP3uiv
cglSamplerParameterIuiv = GetglSamplerParameterIuiv
cglGetQueryObjectui64v = GetglGetQueryObjectui64v
cglGetSamplerParameterfv = GetglGetSamplerParameterfv
cglVertexP4uiv = GetglVertexP4uiv
cglVertexAttribP2uiv = GetglVertexAttribP2uiv
cglVertexAttribP4uiv = GetglVertexAttribP4uiv
cglVertexP4ui = GetglVertexP4ui
cglQueryCounter = GetglQueryCounter
cglTexCoordP3uiv = GetglTexCoordP3uiv
cglMultiTexCoordP2uiv = GetglMultiTexCoordP2uiv
cglTexCoordP2uiv = GetglTexCoordP2uiv
cglMultiTexCoordP3ui = GetglMultiTexCoordP3ui
cglMultiTexCoordP4ui = GetglMultiTexCoordP4ui
cglDeleteSamplers = GetglDeleteSamplers
cglVertexAttribP1uiv = GetglVertexAttribP1uiv
cglMultiTexCoordP2ui = GetglMultiTexCoordP2ui
cglTexCoordP2ui = GetglTexCoordP2ui
cglNormalP3uiv = GetglNormalP3uiv
cglVertexAttribP1ui = GetglVertexAttribP1ui
cglColorP4uiv = GetglColorP4uiv
cglSamplerParameteriv = GetglSamplerParameteriv
cglMultiTexCoordP4uiv = GetglMultiTexCoordP4uiv
cglGetFragDataIndex = GetglGetFragDataIndex
cglSamplerParameterfv = GetglSamplerParameterfv
cglSamplerParameteri = GetglSamplerParameteri
cglVertexAttribP3ui = GetglVertexAttribP3ui
cglBindSampler = GetglBindSampler
cglVertexAttribP3uiv = GetglVertexAttribP3uiv
cglIsSampler = GetglIsSampler
cglMultiTexCoordP1ui = GetglMultiTexCoordP1ui
cglVertexP3uiv = GetglVertexP3uiv
cglTexCoordP4uiv = GetglTexCoordP4uiv
cglSamplerParameterf = GetglSamplerParameterf
cglSecondaryColorP3ui = GetglSecondaryColorP3ui
cglGenSamplers = GetglGenSamplers
cglGetSamplerParameterIuiv = GetglGetSamplerParameterIuiv
cglMultiTexCoordP1uiv = GetglMultiTexCoordP1uiv
cglGetQueryObjecti64v = GetglGetQueryObjecti64v
cglTexCoordP4ui = GetglTexCoordP4ui
cglSecondaryColorP3uiv = GetglSecondaryColorP3uiv
cglBindFragDataLocationIndexed = GetglBindFragDataLocationIndexed
cglTexCoordP1ui = GetglTexCoordP1ui
cglNormalP3ui = GetglNormalP3ui
cglVertexP3ui = GetglVertexP3ui
cglSamplerParameterIiv = GetglSamplerParameterIiv
cglVertexP2ui = GetglVertexP2ui
cglTexCoordP1uiv = GetglTexCoordP1uiv
cglGetSamplerParameteriv = GetglGetSamplerParameteriv
cglVertexAttribP2ui = GetglVertexAttribP2ui
cglTexCoordP3ui = GetglTexCoordP3ui
cglVertexAttribDivisor = GetglVertexAttribDivisor
cglMultiTexCoordP3uiv = GetglMultiTexCoordP3uiv
cglColorP3ui = GetglColorP3ui
cglVertexAttribP4ui = GetglVertexAttribP4ui
cglColorP4ui = GetglColorP4ui
cglVertexP2uiv = GetglVertexP2uiv
cglGetSamplerParameterIiv = GetglGetSamplerParameterIiv


cdef void glColorP3uiv(GLenum type, const GLuint *color):
    cglColorP3uiv(type, color)

cdef void glSamplerParameterIuiv(GLuint sampler, GLenum pname, const GLuint *param):
    cglSamplerParameterIuiv(sampler, pname, param)

cdef void glGetQueryObjectui64v(GLuint id, GLenum pname, GLuint64 *params):
    cglGetQueryObjectui64v(id, pname, params)

cdef void glGetSamplerParameterfv(GLuint sampler, GLenum pname, GLfloat *params):
    cglGetSamplerParameterfv(sampler, pname, params)

cdef void glVertexP4uiv(GLenum type, const GLuint *value):
    cglVertexP4uiv(type, value)

cdef void glVertexAttribP2uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP2uiv(index, type, normalized, value)

cdef void glVertexAttribP4uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP4uiv(index, type, normalized, value)

cdef void glVertexP4ui(GLenum type, GLuint value):
    cglVertexP4ui(type, value)

cdef void glQueryCounter(GLuint id, GLenum target):
    cglQueryCounter(id, target)

cdef void glTexCoordP3uiv(GLenum type, const GLuint *coords):
    cglTexCoordP3uiv(type, coords)

cdef void glMultiTexCoordP2uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP2uiv(texture, type, coords)

cdef void glTexCoordP2uiv(GLenum type, const GLuint *coords):
    cglTexCoordP2uiv(type, coords)

cdef void glMultiTexCoordP3ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP3ui(texture, type, coords)

cdef void glMultiTexCoordP4ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP4ui(texture, type, coords)

cdef void glDeleteSamplers(GLsizei count, const GLuint *samplers):
    cglDeleteSamplers(count, samplers)

cdef void glVertexAttribP1uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP1uiv(index, type, normalized, value)

cdef void glMultiTexCoordP2ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP2ui(texture, type, coords)

cdef void glTexCoordP2ui(GLenum type, GLuint coords):
    cglTexCoordP2ui(type, coords)

cdef void glNormalP3uiv(GLenum type, const GLuint *coords):
    cglNormalP3uiv(type, coords)

cdef void glVertexAttribP1ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP1ui(index, type, normalized, value)

cdef void glColorP4uiv(GLenum type, const GLuint *color):
    cglColorP4uiv(type, color)

cdef void glSamplerParameteriv(GLuint sampler, GLenum pname, const GLint *param):
    cglSamplerParameteriv(sampler, pname, param)

cdef void glMultiTexCoordP4uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP4uiv(texture, type, coords)

cdef GLint glGetFragDataIndex(GLuint program, const GLchar *name):
    cglGetFragDataIndex(program, name)

cdef void glSamplerParameterfv(GLuint sampler, GLenum pname, const GLfloat *param):
    cglSamplerParameterfv(sampler, pname, param)

cdef void glSamplerParameteri(GLuint sampler, GLenum pname, GLint param):
    cglSamplerParameteri(sampler, pname, param)

cdef void glVertexAttribP3ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP3ui(index, type, normalized, value)

cdef void glBindSampler(GLuint unit, GLuint sampler):
    cglBindSampler(unit, sampler)

cdef void glVertexAttribP3uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value):
    cglVertexAttribP3uiv(index, type, normalized, value)

cdef GLboolean glIsSampler(GLuint sampler):
    cglIsSampler(sampler)

cdef void glMultiTexCoordP1ui(GLenum texture, GLenum type, GLuint coords):
    cglMultiTexCoordP1ui(texture, type, coords)

cdef void glVertexP3uiv(GLenum type, const GLuint *value):
    cglVertexP3uiv(type, value)

cdef void glTexCoordP4uiv(GLenum type, const GLuint *coords):
    cglTexCoordP4uiv(type, coords)

cdef void glSamplerParameterf(GLuint sampler, GLenum pname, GLfloat param):
    cglSamplerParameterf(sampler, pname, param)

cdef void glSecondaryColorP3ui(GLenum type, GLuint color):
    cglSecondaryColorP3ui(type, color)

cdef void glGenSamplers(GLsizei count, GLuint *samplers):
    cglGenSamplers(count, samplers)

cdef void glGetSamplerParameterIuiv(GLuint sampler, GLenum pname, GLuint *params):
    cglGetSamplerParameterIuiv(sampler, pname, params)

cdef void glMultiTexCoordP1uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP1uiv(texture, type, coords)

cdef void glGetQueryObjecti64v(GLuint id, GLenum pname, GLint64 *params):
    cglGetQueryObjecti64v(id, pname, params)

cdef void glTexCoordP4ui(GLenum type, GLuint coords):
    cglTexCoordP4ui(type, coords)

cdef void glSecondaryColorP3uiv(GLenum type, const GLuint *color):
    cglSecondaryColorP3uiv(type, color)

cdef void glBindFragDataLocationIndexed(GLuint program, GLuint colorNumber, GLuint index, const GLchar *name):
    cglBindFragDataLocationIndexed(program, colorNumber, index, name)

cdef void glTexCoordP1ui(GLenum type, GLuint coords):
    cglTexCoordP1ui(type, coords)

cdef void glNormalP3ui(GLenum type, GLuint coords):
    cglNormalP3ui(type, coords)

cdef void glVertexP3ui(GLenum type, GLuint value):
    cglVertexP3ui(type, value)

cdef void glSamplerParameterIiv(GLuint sampler, GLenum pname, const GLint *param):
    cglSamplerParameterIiv(sampler, pname, param)

cdef void glVertexP2ui(GLenum type, GLuint value):
    cglVertexP2ui(type, value)

cdef void glTexCoordP1uiv(GLenum type, const GLuint *coords):
    cglTexCoordP1uiv(type, coords)

cdef void glGetSamplerParameteriv(GLuint sampler, GLenum pname, GLint *params):
    cglGetSamplerParameteriv(sampler, pname, params)

cdef void glVertexAttribP2ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP2ui(index, type, normalized, value)

cdef void glTexCoordP3ui(GLenum type, GLuint coords):
    cglTexCoordP3ui(type, coords)

cdef void glVertexAttribDivisor(GLuint index, GLuint divisor):
    cglVertexAttribDivisor(index, divisor)

cdef void glMultiTexCoordP3uiv(GLenum texture, GLenum type, const GLuint *coords):
    cglMultiTexCoordP3uiv(texture, type, coords)

cdef void glColorP3ui(GLenum type, GLuint color):
    cglColorP3ui(type, color)

cdef void glVertexAttribP4ui(GLuint index, GLenum type, GLboolean normalized, GLuint value):
    cglVertexAttribP4ui(index, type, normalized, value)

cdef void glColorP4ui(GLenum type, GLuint color):
    cglColorP4ui(type, color)

cdef void glVertexP2uiv(GLenum type, const GLuint *value):
    cglVertexP2uiv(type, value)

cdef void glGetSamplerParameterIiv(GLuint sampler, GLenum pname, GLint *params):
    cglGetSamplerParameterIiv(sampler, pname, params)
