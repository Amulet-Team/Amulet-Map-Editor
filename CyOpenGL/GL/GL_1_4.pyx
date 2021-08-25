# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_BLEND_COLOR = 0x8005
cdef GLenum GL_BLEND_DST_ALPHA = 0x80CA
cdef GLenum GL_BLEND_DST_RGB = 0x80C8
cdef GLenum GL_BLEND_EQUATION = 0x8009
cdef GLenum GL_BLEND_SRC_ALPHA = 0x80CB
cdef GLenum GL_BLEND_SRC_RGB = 0x80C9
cdef GLenum GL_COLOR_SUM = 0x8458
cdef GLenum GL_COMPARE_R_TO_TEXTURE = 0x884E
cdef GLenum GL_CONSTANT_ALPHA = 0x8003
cdef GLenum GL_CONSTANT_COLOR = 0x8001
cdef GLenum GL_CURRENT_FOG_COORDINATE = 0x8453
cdef GLenum GL_CURRENT_SECONDARY_COLOR = 0x8459
cdef GLenum GL_DECR_WRAP = 0x8508
cdef GLenum GL_DEPTH_COMPONENT16 = 0x81A5
cdef GLenum GL_DEPTH_COMPONENT24 = 0x81A6
cdef GLenum GL_DEPTH_COMPONENT32 = 0x81A7
cdef GLenum GL_DEPTH_TEXTURE_MODE = 0x884B
cdef GLenum GL_FOG_COORDINATE = 0x8451
cdef GLenum GL_FOG_COORDINATE_ARRAY = 0x8457
cdef GLenum GL_FOG_COORDINATE_ARRAY_POINTER = 0x8456
cdef GLenum GL_FOG_COORDINATE_ARRAY_STRIDE = 0x8455
cdef GLenum GL_FOG_COORDINATE_ARRAY_TYPE = 0x8454
cdef GLenum GL_FOG_COORDINATE_SOURCE = 0x8450
cdef GLenum GL_FRAGMENT_DEPTH = 0x8452
cdef GLenum GL_FUNC_ADD = 0x8006
cdef GLenum GL_FUNC_REVERSE_SUBTRACT = 0x800B
cdef GLenum GL_FUNC_SUBTRACT = 0x800A
cdef GLenum GL_GENERATE_MIPMAP = 0x8191
cdef GLenum GL_GENERATE_MIPMAP_HINT = 0x8192
cdef GLenum GL_INCR_WRAP = 0x8507
cdef GLenum GL_MAX = 0x8008
cdef GLenum GL_MAX_TEXTURE_LOD_BIAS = 0x84FD
cdef GLenum GL_MIN = 0x8007
cdef GLenum GL_MIRRORED_REPEAT = 0x8370
cdef GLenum GL_ONE_MINUS_CONSTANT_ALPHA = 0x8004
cdef GLenum GL_ONE_MINUS_CONSTANT_COLOR = 0x8002
cdef GLenum GL_POINT_DISTANCE_ATTENUATION = 0x8129
cdef GLenum GL_POINT_FADE_THRESHOLD_SIZE = 0x8128
cdef GLenum GL_POINT_SIZE_MAX = 0x8127
cdef GLenum GL_POINT_SIZE_MIN = 0x8126
cdef GLenum GL_SECONDARY_COLOR_ARRAY = 0x845E
cdef GLenum GL_SECONDARY_COLOR_ARRAY_POINTER = 0x845D
cdef GLenum GL_SECONDARY_COLOR_ARRAY_SIZE = 0x845A
cdef GLenum GL_SECONDARY_COLOR_ARRAY_STRIDE = 0x845C
cdef GLenum GL_SECONDARY_COLOR_ARRAY_TYPE = 0x845B
cdef GLenum GL_TEXTURE_COMPARE_FUNC = 0x884D
cdef GLenum GL_TEXTURE_COMPARE_MODE = 0x884C
cdef GLenum GL_TEXTURE_DEPTH_SIZE = 0x884A
cdef GLenum GL_TEXTURE_FILTER_CONTROL = 0x8500
cdef GLenum GL_TEXTURE_LOD_BIAS = 0x8501

ctypedef void (*PFNGLBLENDCOLORPROC)(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
ctypedef void (*PFNGLBLENDEQUATIONPROC)(GLenum mode)
ctypedef void (*PFNGLBLENDFUNCSEPARATEPROC)(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
ctypedef void (*PFNGLFOGCOORDPOINTERPROC)(GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*PFNGLFOGCOORDDPROC)(GLdouble coord)
ctypedef void (*PFNGLFOGCOORDDVPROC)(const GLdouble *coord)
ctypedef void (*PFNGLFOGCOORDFPROC)(GLfloat coord)
ctypedef void (*PFNGLFOGCOORDFVPROC)(const GLfloat *coord)
ctypedef void (*PFNGLMULTIDRAWARRAYSPROC)(GLenum mode, const GLint *first, const GLsizei *count, GLsizei drawcount)
ctypedef void (*PFNGLMULTIDRAWELEMENTSPROC)(GLenum mode, const GLsizei *count, GLenum type, const void **indices, GLsizei drawcount)
ctypedef void (*PFNGLPOINTPARAMETERFPROC)(GLenum pname, GLfloat param)
ctypedef void (*PFNGLPOINTPARAMETERFVPROC)(GLenum pname, const GLfloat *params)
ctypedef void (*PFNGLPOINTPARAMETERIPROC)(GLenum pname, GLint param)
ctypedef void (*PFNGLPOINTPARAMETERIVPROC)(GLenum pname, const GLint *params)
ctypedef void (*PFNGLSECONDARYCOLOR3BPROC)(GLbyte red, GLbyte green, GLbyte blue)
ctypedef void (*PFNGLSECONDARYCOLOR3BVPROC)(const GLbyte *v)
ctypedef void (*PFNGLSECONDARYCOLOR3DPROC)(GLdouble red, GLdouble green, GLdouble blue)
ctypedef void (*PFNGLSECONDARYCOLOR3DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLSECONDARYCOLOR3FPROC)(GLfloat red, GLfloat green, GLfloat blue)
ctypedef void (*PFNGLSECONDARYCOLOR3FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLSECONDARYCOLOR3IPROC)(GLint red, GLint green, GLint blue)
ctypedef void (*PFNGLSECONDARYCOLOR3IVPROC)(const GLint *v)
ctypedef void (*PFNGLSECONDARYCOLOR3SPROC)(GLshort red, GLshort green, GLshort blue)
ctypedef void (*PFNGLSECONDARYCOLOR3SVPROC)(const GLshort *v)
ctypedef void (*PFNGLSECONDARYCOLOR3UBPROC)(GLubyte red, GLubyte green, GLubyte blue)
ctypedef void (*PFNGLSECONDARYCOLOR3UBVPROC)(const GLubyte *v)
ctypedef void (*PFNGLSECONDARYCOLOR3UIPROC)(GLuint red, GLuint green, GLuint blue)
ctypedef void (*PFNGLSECONDARYCOLOR3UIVPROC)(const GLuint *v)
ctypedef void (*PFNGLSECONDARYCOLOR3USPROC)(GLushort red, GLushort green, GLushort blue)
ctypedef void (*PFNGLSECONDARYCOLOR3USVPROC)(const GLushort *v)
ctypedef void (*PFNGLSECONDARYCOLORPOINTERPROC)(GLint size, GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*PFNGLWINDOWPOS2DPROC)(GLdouble x, GLdouble y)
ctypedef void (*PFNGLWINDOWPOS2DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLWINDOWPOS2FPROC)(GLfloat x, GLfloat y)
ctypedef void (*PFNGLWINDOWPOS2FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLWINDOWPOS2IPROC)(GLint x, GLint y)
ctypedef void (*PFNGLWINDOWPOS2IVPROC)(const GLint *v)
ctypedef void (*PFNGLWINDOWPOS2SPROC)(GLshort x, GLshort y)
ctypedef void (*PFNGLWINDOWPOS2SVPROC)(const GLshort *v)
ctypedef void (*PFNGLWINDOWPOS3DPROC)(GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*PFNGLWINDOWPOS3DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLWINDOWPOS3FPROC)(GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*PFNGLWINDOWPOS3FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLWINDOWPOS3IPROC)(GLint x, GLint y, GLint z)
ctypedef void (*PFNGLWINDOWPOS3IVPROC)(const GLint *v)
ctypedef void (*PFNGLWINDOWPOS3SPROC)(GLshort x, GLshort y, GLshort z)
ctypedef void (*PFNGLWINDOWPOS3SVPROC)(const GLshort *v)

cdef PFNGLBLENDCOLORPROC cglBlendColor = NULL
cdef PFNGLBLENDEQUATIONPROC cglBlendEquation = NULL
cdef PFNGLBLENDFUNCSEPARATEPROC cglBlendFuncSeparate = NULL
cdef PFNGLFOGCOORDPOINTERPROC cglFogCoordPointer = NULL
cdef PFNGLFOGCOORDDPROC cglFogCoordd = NULL
cdef PFNGLFOGCOORDDVPROC cglFogCoorddv = NULL
cdef PFNGLFOGCOORDFPROC cglFogCoordf = NULL
cdef PFNGLFOGCOORDFVPROC cglFogCoordfv = NULL
cdef PFNGLMULTIDRAWARRAYSPROC cglMultiDrawArrays = NULL
cdef PFNGLMULTIDRAWELEMENTSPROC cglMultiDrawElements = NULL
cdef PFNGLPOINTPARAMETERFPROC cglPointParameterf = NULL
cdef PFNGLPOINTPARAMETERFVPROC cglPointParameterfv = NULL
cdef PFNGLPOINTPARAMETERIPROC cglPointParameteri = NULL
cdef PFNGLPOINTPARAMETERIVPROC cglPointParameteriv = NULL
cdef PFNGLSECONDARYCOLOR3BPROC cglSecondaryColor3b = NULL
cdef PFNGLSECONDARYCOLOR3BVPROC cglSecondaryColor3bv = NULL
cdef PFNGLSECONDARYCOLOR3DPROC cglSecondaryColor3d = NULL
cdef PFNGLSECONDARYCOLOR3DVPROC cglSecondaryColor3dv = NULL
cdef PFNGLSECONDARYCOLOR3FPROC cglSecondaryColor3f = NULL
cdef PFNGLSECONDARYCOLOR3FVPROC cglSecondaryColor3fv = NULL
cdef PFNGLSECONDARYCOLOR3IPROC cglSecondaryColor3i = NULL
cdef PFNGLSECONDARYCOLOR3IVPROC cglSecondaryColor3iv = NULL
cdef PFNGLSECONDARYCOLOR3SPROC cglSecondaryColor3s = NULL
cdef PFNGLSECONDARYCOLOR3SVPROC cglSecondaryColor3sv = NULL
cdef PFNGLSECONDARYCOLOR3UBPROC cglSecondaryColor3ub = NULL
cdef PFNGLSECONDARYCOLOR3UBVPROC cglSecondaryColor3ubv = NULL
cdef PFNGLSECONDARYCOLOR3UIPROC cglSecondaryColor3ui = NULL
cdef PFNGLSECONDARYCOLOR3UIVPROC cglSecondaryColor3uiv = NULL
cdef PFNGLSECONDARYCOLOR3USPROC cglSecondaryColor3us = NULL
cdef PFNGLSECONDARYCOLOR3USVPROC cglSecondaryColor3usv = NULL
cdef PFNGLSECONDARYCOLORPOINTERPROC cglSecondaryColorPointer = NULL
cdef PFNGLWINDOWPOS2DPROC cglWindowPos2d = NULL
cdef PFNGLWINDOWPOS2DVPROC cglWindowPos2dv = NULL
cdef PFNGLWINDOWPOS2FPROC cglWindowPos2f = NULL
cdef PFNGLWINDOWPOS2FVPROC cglWindowPos2fv = NULL
cdef PFNGLWINDOWPOS2IPROC cglWindowPos2i = NULL
cdef PFNGLWINDOWPOS2IVPROC cglWindowPos2iv = NULL
cdef PFNGLWINDOWPOS2SPROC cglWindowPos2s = NULL
cdef PFNGLWINDOWPOS2SVPROC cglWindowPos2sv = NULL
cdef PFNGLWINDOWPOS3DPROC cglWindowPos3d = NULL
cdef PFNGLWINDOWPOS3DVPROC cglWindowPos3dv = NULL
cdef PFNGLWINDOWPOS3FPROC cglWindowPos3f = NULL
cdef PFNGLWINDOWPOS3FVPROC cglWindowPos3fv = NULL
cdef PFNGLWINDOWPOS3IPROC cglWindowPos3i = NULL
cdef PFNGLWINDOWPOS3IVPROC cglWindowPos3iv = NULL
cdef PFNGLWINDOWPOS3SPROC cglWindowPos3s = NULL
cdef PFNGLWINDOWPOS3SVPROC cglWindowPos3sv = NULL


cdef void GetglBlendColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    global cglBlendColor
    cglBlendColor = <PFNGLBLENDCOLORPROC>getFunction(b"glBlendColor")
    cglBlendColor(red, green, blue, alpha)

cdef void GetglBlendEquation(GLenum mode):
    global cglBlendEquation
    cglBlendEquation = <PFNGLBLENDEQUATIONPROC>getFunction(b"glBlendEquation")
    cglBlendEquation(mode)

cdef void GetglBlendFuncSeparate(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha):
    global cglBlendFuncSeparate
    cglBlendFuncSeparate = <PFNGLBLENDFUNCSEPARATEPROC>getFunction(b"glBlendFuncSeparate")
    cglBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)

cdef void GetglFogCoordPointer(GLenum type, GLsizei stride, const void *pointer):
    global cglFogCoordPointer
    cglFogCoordPointer = <PFNGLFOGCOORDPOINTERPROC>getFunction(b"glFogCoordPointer")
    cglFogCoordPointer(type, stride, pointer)

cdef void GetglFogCoordd(GLdouble coord):
    global cglFogCoordd
    cglFogCoordd = <PFNGLFOGCOORDDPROC>getFunction(b"glFogCoordd")
    cglFogCoordd(coord)

cdef void GetglFogCoorddv(const GLdouble *coord):
    global cglFogCoorddv
    cglFogCoorddv = <PFNGLFOGCOORDDVPROC>getFunction(b"glFogCoorddv")
    cglFogCoorddv(coord)

cdef void GetglFogCoordf(GLfloat coord):
    global cglFogCoordf
    cglFogCoordf = <PFNGLFOGCOORDFPROC>getFunction(b"glFogCoordf")
    cglFogCoordf(coord)

cdef void GetglFogCoordfv(const GLfloat *coord):
    global cglFogCoordfv
    cglFogCoordfv = <PFNGLFOGCOORDFVPROC>getFunction(b"glFogCoordfv")
    cglFogCoordfv(coord)

cdef void GetglMultiDrawArrays(GLenum mode, const GLint *first, const GLsizei *count, GLsizei drawcount):
    global cglMultiDrawArrays
    cglMultiDrawArrays = <PFNGLMULTIDRAWARRAYSPROC>getFunction(b"glMultiDrawArrays")
    cglMultiDrawArrays(mode, first, count, drawcount)

cdef void GetglMultiDrawElements(GLenum mode, const GLsizei *count, GLenum type, const void **indices, GLsizei drawcount):
    global cglMultiDrawElements
    cglMultiDrawElements = <PFNGLMULTIDRAWELEMENTSPROC>getFunction(b"glMultiDrawElements")
    cglMultiDrawElements(mode, count, type, indices, drawcount)

cdef void GetglPointParameterf(GLenum pname, GLfloat param):
    global cglPointParameterf
    cglPointParameterf = <PFNGLPOINTPARAMETERFPROC>getFunction(b"glPointParameterf")
    cglPointParameterf(pname, param)

cdef void GetglPointParameterfv(GLenum pname, const GLfloat *params):
    global cglPointParameterfv
    cglPointParameterfv = <PFNGLPOINTPARAMETERFVPROC>getFunction(b"glPointParameterfv")
    cglPointParameterfv(pname, params)

cdef void GetglPointParameteri(GLenum pname, GLint param):
    global cglPointParameteri
    cglPointParameteri = <PFNGLPOINTPARAMETERIPROC>getFunction(b"glPointParameteri")
    cglPointParameteri(pname, param)

cdef void GetglPointParameteriv(GLenum pname, const GLint *params):
    global cglPointParameteriv
    cglPointParameteriv = <PFNGLPOINTPARAMETERIVPROC>getFunction(b"glPointParameteriv")
    cglPointParameteriv(pname, params)

cdef void GetglSecondaryColor3b(GLbyte red, GLbyte green, GLbyte blue):
    global cglSecondaryColor3b
    cglSecondaryColor3b = <PFNGLSECONDARYCOLOR3BPROC>getFunction(b"glSecondaryColor3b")
    cglSecondaryColor3b(red, green, blue)

cdef void GetglSecondaryColor3bv(const GLbyte *v):
    global cglSecondaryColor3bv
    cglSecondaryColor3bv = <PFNGLSECONDARYCOLOR3BVPROC>getFunction(b"glSecondaryColor3bv")
    cglSecondaryColor3bv(v)

cdef void GetglSecondaryColor3d(GLdouble red, GLdouble green, GLdouble blue):
    global cglSecondaryColor3d
    cglSecondaryColor3d = <PFNGLSECONDARYCOLOR3DPROC>getFunction(b"glSecondaryColor3d")
    cglSecondaryColor3d(red, green, blue)

cdef void GetglSecondaryColor3dv(const GLdouble *v):
    global cglSecondaryColor3dv
    cglSecondaryColor3dv = <PFNGLSECONDARYCOLOR3DVPROC>getFunction(b"glSecondaryColor3dv")
    cglSecondaryColor3dv(v)

cdef void GetglSecondaryColor3f(GLfloat red, GLfloat green, GLfloat blue):
    global cglSecondaryColor3f
    cglSecondaryColor3f = <PFNGLSECONDARYCOLOR3FPROC>getFunction(b"glSecondaryColor3f")
    cglSecondaryColor3f(red, green, blue)

cdef void GetglSecondaryColor3fv(const GLfloat *v):
    global cglSecondaryColor3fv
    cglSecondaryColor3fv = <PFNGLSECONDARYCOLOR3FVPROC>getFunction(b"glSecondaryColor3fv")
    cglSecondaryColor3fv(v)

cdef void GetglSecondaryColor3i(GLint red, GLint green, GLint blue):
    global cglSecondaryColor3i
    cglSecondaryColor3i = <PFNGLSECONDARYCOLOR3IPROC>getFunction(b"glSecondaryColor3i")
    cglSecondaryColor3i(red, green, blue)

cdef void GetglSecondaryColor3iv(const GLint *v):
    global cglSecondaryColor3iv
    cglSecondaryColor3iv = <PFNGLSECONDARYCOLOR3IVPROC>getFunction(b"glSecondaryColor3iv")
    cglSecondaryColor3iv(v)

cdef void GetglSecondaryColor3s(GLshort red, GLshort green, GLshort blue):
    global cglSecondaryColor3s
    cglSecondaryColor3s = <PFNGLSECONDARYCOLOR3SPROC>getFunction(b"glSecondaryColor3s")
    cglSecondaryColor3s(red, green, blue)

cdef void GetglSecondaryColor3sv(const GLshort *v):
    global cglSecondaryColor3sv
    cglSecondaryColor3sv = <PFNGLSECONDARYCOLOR3SVPROC>getFunction(b"glSecondaryColor3sv")
    cglSecondaryColor3sv(v)

cdef void GetglSecondaryColor3ub(GLubyte red, GLubyte green, GLubyte blue):
    global cglSecondaryColor3ub
    cglSecondaryColor3ub = <PFNGLSECONDARYCOLOR3UBPROC>getFunction(b"glSecondaryColor3ub")
    cglSecondaryColor3ub(red, green, blue)

cdef void GetglSecondaryColor3ubv(const GLubyte *v):
    global cglSecondaryColor3ubv
    cglSecondaryColor3ubv = <PFNGLSECONDARYCOLOR3UBVPROC>getFunction(b"glSecondaryColor3ubv")
    cglSecondaryColor3ubv(v)

cdef void GetglSecondaryColor3ui(GLuint red, GLuint green, GLuint blue):
    global cglSecondaryColor3ui
    cglSecondaryColor3ui = <PFNGLSECONDARYCOLOR3UIPROC>getFunction(b"glSecondaryColor3ui")
    cglSecondaryColor3ui(red, green, blue)

cdef void GetglSecondaryColor3uiv(const GLuint *v):
    global cglSecondaryColor3uiv
    cglSecondaryColor3uiv = <PFNGLSECONDARYCOLOR3UIVPROC>getFunction(b"glSecondaryColor3uiv")
    cglSecondaryColor3uiv(v)

cdef void GetglSecondaryColor3us(GLushort red, GLushort green, GLushort blue):
    global cglSecondaryColor3us
    cglSecondaryColor3us = <PFNGLSECONDARYCOLOR3USPROC>getFunction(b"glSecondaryColor3us")
    cglSecondaryColor3us(red, green, blue)

cdef void GetglSecondaryColor3usv(const GLushort *v):
    global cglSecondaryColor3usv
    cglSecondaryColor3usv = <PFNGLSECONDARYCOLOR3USVPROC>getFunction(b"glSecondaryColor3usv")
    cglSecondaryColor3usv(v)

cdef void GetglSecondaryColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglSecondaryColorPointer
    cglSecondaryColorPointer = <PFNGLSECONDARYCOLORPOINTERPROC>getFunction(b"glSecondaryColorPointer")
    cglSecondaryColorPointer(size, type, stride, pointer)

cdef void GetglWindowPos2d(GLdouble x, GLdouble y):
    global cglWindowPos2d
    cglWindowPos2d = <PFNGLWINDOWPOS2DPROC>getFunction(b"glWindowPos2d")
    cglWindowPos2d(x, y)

cdef void GetglWindowPos2dv(const GLdouble *v):
    global cglWindowPos2dv
    cglWindowPos2dv = <PFNGLWINDOWPOS2DVPROC>getFunction(b"glWindowPos2dv")
    cglWindowPos2dv(v)

cdef void GetglWindowPos2f(GLfloat x, GLfloat y):
    global cglWindowPos2f
    cglWindowPos2f = <PFNGLWINDOWPOS2FPROC>getFunction(b"glWindowPos2f")
    cglWindowPos2f(x, y)

cdef void GetglWindowPos2fv(const GLfloat *v):
    global cglWindowPos2fv
    cglWindowPos2fv = <PFNGLWINDOWPOS2FVPROC>getFunction(b"glWindowPos2fv")
    cglWindowPos2fv(v)

cdef void GetglWindowPos2i(GLint x, GLint y):
    global cglWindowPos2i
    cglWindowPos2i = <PFNGLWINDOWPOS2IPROC>getFunction(b"glWindowPos2i")
    cglWindowPos2i(x, y)

cdef void GetglWindowPos2iv(const GLint *v):
    global cglWindowPos2iv
    cglWindowPos2iv = <PFNGLWINDOWPOS2IVPROC>getFunction(b"glWindowPos2iv")
    cglWindowPos2iv(v)

cdef void GetglWindowPos2s(GLshort x, GLshort y):
    global cglWindowPos2s
    cglWindowPos2s = <PFNGLWINDOWPOS2SPROC>getFunction(b"glWindowPos2s")
    cglWindowPos2s(x, y)

cdef void GetglWindowPos2sv(const GLshort *v):
    global cglWindowPos2sv
    cglWindowPos2sv = <PFNGLWINDOWPOS2SVPROC>getFunction(b"glWindowPos2sv")
    cglWindowPos2sv(v)

cdef void GetglWindowPos3d(GLdouble x, GLdouble y, GLdouble z):
    global cglWindowPos3d
    cglWindowPos3d = <PFNGLWINDOWPOS3DPROC>getFunction(b"glWindowPos3d")
    cglWindowPos3d(x, y, z)

cdef void GetglWindowPos3dv(const GLdouble *v):
    global cglWindowPos3dv
    cglWindowPos3dv = <PFNGLWINDOWPOS3DVPROC>getFunction(b"glWindowPos3dv")
    cglWindowPos3dv(v)

cdef void GetglWindowPos3f(GLfloat x, GLfloat y, GLfloat z):
    global cglWindowPos3f
    cglWindowPos3f = <PFNGLWINDOWPOS3FPROC>getFunction(b"glWindowPos3f")
    cglWindowPos3f(x, y, z)

cdef void GetglWindowPos3fv(const GLfloat *v):
    global cglWindowPos3fv
    cglWindowPos3fv = <PFNGLWINDOWPOS3FVPROC>getFunction(b"glWindowPos3fv")
    cglWindowPos3fv(v)

cdef void GetglWindowPos3i(GLint x, GLint y, GLint z):
    global cglWindowPos3i
    cglWindowPos3i = <PFNGLWINDOWPOS3IPROC>getFunction(b"glWindowPos3i")
    cglWindowPos3i(x, y, z)

cdef void GetglWindowPos3iv(const GLint *v):
    global cglWindowPos3iv
    cglWindowPos3iv = <PFNGLWINDOWPOS3IVPROC>getFunction(b"glWindowPos3iv")
    cglWindowPos3iv(v)

cdef void GetglWindowPos3s(GLshort x, GLshort y, GLshort z):
    global cglWindowPos3s
    cglWindowPos3s = <PFNGLWINDOWPOS3SPROC>getFunction(b"glWindowPos3s")
    cglWindowPos3s(x, y, z)

cdef void GetglWindowPos3sv(const GLshort *v):
    global cglWindowPos3sv
    cglWindowPos3sv = <PFNGLWINDOWPOS3SVPROC>getFunction(b"glWindowPos3sv")
    cglWindowPos3sv(v)

cglBlendColor = GetglBlendColor
cglBlendEquation = GetglBlendEquation
cglBlendFuncSeparate = GetglBlendFuncSeparate
cglFogCoordPointer = GetglFogCoordPointer
cglFogCoordd = GetglFogCoordd
cglFogCoorddv = GetglFogCoorddv
cglFogCoordf = GetglFogCoordf
cglFogCoordfv = GetglFogCoordfv
cglMultiDrawArrays = GetglMultiDrawArrays
cglMultiDrawElements = GetglMultiDrawElements
cglPointParameterf = GetglPointParameterf
cglPointParameterfv = GetglPointParameterfv
cglPointParameteri = GetglPointParameteri
cglPointParameteriv = GetglPointParameteriv
cglSecondaryColor3b = GetglSecondaryColor3b
cglSecondaryColor3bv = GetglSecondaryColor3bv
cglSecondaryColor3d = GetglSecondaryColor3d
cglSecondaryColor3dv = GetglSecondaryColor3dv
cglSecondaryColor3f = GetglSecondaryColor3f
cglSecondaryColor3fv = GetglSecondaryColor3fv
cglSecondaryColor3i = GetglSecondaryColor3i
cglSecondaryColor3iv = GetglSecondaryColor3iv
cglSecondaryColor3s = GetglSecondaryColor3s
cglSecondaryColor3sv = GetglSecondaryColor3sv
cglSecondaryColor3ub = GetglSecondaryColor3ub
cglSecondaryColor3ubv = GetglSecondaryColor3ubv
cglSecondaryColor3ui = GetglSecondaryColor3ui
cglSecondaryColor3uiv = GetglSecondaryColor3uiv
cglSecondaryColor3us = GetglSecondaryColor3us
cglSecondaryColor3usv = GetglSecondaryColor3usv
cglSecondaryColorPointer = GetglSecondaryColorPointer
cglWindowPos2d = GetglWindowPos2d
cglWindowPos2dv = GetglWindowPos2dv
cglWindowPos2f = GetglWindowPos2f
cglWindowPos2fv = GetglWindowPos2fv
cglWindowPos2i = GetglWindowPos2i
cglWindowPos2iv = GetglWindowPos2iv
cglWindowPos2s = GetglWindowPos2s
cglWindowPos2sv = GetglWindowPos2sv
cglWindowPos3d = GetglWindowPos3d
cglWindowPos3dv = GetglWindowPos3dv
cglWindowPos3f = GetglWindowPos3f
cglWindowPos3fv = GetglWindowPos3fv
cglWindowPos3i = GetglWindowPos3i
cglWindowPos3iv = GetglWindowPos3iv
cglWindowPos3s = GetglWindowPos3s
cglWindowPos3sv = GetglWindowPos3sv


cdef void glBlendColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    cglBlendColor(red, green, blue, alpha)

cdef void glBlendEquation(GLenum mode):
    cglBlendEquation(mode)

cdef void glBlendFuncSeparate(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha):
    cglBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)

cdef void glFogCoordPointer(GLenum type, GLsizei stride, const void *pointer):
    cglFogCoordPointer(type, stride, pointer)

cdef void glFogCoordd(GLdouble coord):
    cglFogCoordd(coord)

cdef void glFogCoorddv(const GLdouble *coord):
    cglFogCoorddv(coord)

cdef void glFogCoordf(GLfloat coord):
    cglFogCoordf(coord)

cdef void glFogCoordfv(const GLfloat *coord):
    cglFogCoordfv(coord)

cdef void glMultiDrawArrays(GLenum mode, const GLint *first, const GLsizei *count, GLsizei drawcount):
    cglMultiDrawArrays(mode, first, count, drawcount)

cdef void glMultiDrawElements(GLenum mode, const GLsizei *count, GLenum type, const void **indices, GLsizei drawcount):
    cglMultiDrawElements(mode, count, type, indices, drawcount)

cdef void glPointParameterf(GLenum pname, GLfloat param):
    cglPointParameterf(pname, param)

cdef void glPointParameterfv(GLenum pname, const GLfloat *params):
    cglPointParameterfv(pname, params)

cdef void glPointParameteri(GLenum pname, GLint param):
    cglPointParameteri(pname, param)

cdef void glPointParameteriv(GLenum pname, const GLint *params):
    cglPointParameteriv(pname, params)

cdef void glSecondaryColor3b(GLbyte red, GLbyte green, GLbyte blue):
    cglSecondaryColor3b(red, green, blue)

cdef void glSecondaryColor3bv(const GLbyte *v):
    cglSecondaryColor3bv(v)

cdef void glSecondaryColor3d(GLdouble red, GLdouble green, GLdouble blue):
    cglSecondaryColor3d(red, green, blue)

cdef void glSecondaryColor3dv(const GLdouble *v):
    cglSecondaryColor3dv(v)

cdef void glSecondaryColor3f(GLfloat red, GLfloat green, GLfloat blue):
    cglSecondaryColor3f(red, green, blue)

cdef void glSecondaryColor3fv(const GLfloat *v):
    cglSecondaryColor3fv(v)

cdef void glSecondaryColor3i(GLint red, GLint green, GLint blue):
    cglSecondaryColor3i(red, green, blue)

cdef void glSecondaryColor3iv(const GLint *v):
    cglSecondaryColor3iv(v)

cdef void glSecondaryColor3s(GLshort red, GLshort green, GLshort blue):
    cglSecondaryColor3s(red, green, blue)

cdef void glSecondaryColor3sv(const GLshort *v):
    cglSecondaryColor3sv(v)

cdef void glSecondaryColor3ub(GLubyte red, GLubyte green, GLubyte blue):
    cglSecondaryColor3ub(red, green, blue)

cdef void glSecondaryColor3ubv(const GLubyte *v):
    cglSecondaryColor3ubv(v)

cdef void glSecondaryColor3ui(GLuint red, GLuint green, GLuint blue):
    cglSecondaryColor3ui(red, green, blue)

cdef void glSecondaryColor3uiv(const GLuint *v):
    cglSecondaryColor3uiv(v)

cdef void glSecondaryColor3us(GLushort red, GLushort green, GLushort blue):
    cglSecondaryColor3us(red, green, blue)

cdef void glSecondaryColor3usv(const GLushort *v):
    cglSecondaryColor3usv(v)

cdef void glSecondaryColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglSecondaryColorPointer(size, type, stride, pointer)

cdef void glWindowPos2d(GLdouble x, GLdouble y):
    cglWindowPos2d(x, y)

cdef void glWindowPos2dv(const GLdouble *v):
    cglWindowPos2dv(v)

cdef void glWindowPos2f(GLfloat x, GLfloat y):
    cglWindowPos2f(x, y)

cdef void glWindowPos2fv(const GLfloat *v):
    cglWindowPos2fv(v)

cdef void glWindowPos2i(GLint x, GLint y):
    cglWindowPos2i(x, y)

cdef void glWindowPos2iv(const GLint *v):
    cglWindowPos2iv(v)

cdef void glWindowPos2s(GLshort x, GLshort y):
    cglWindowPos2s(x, y)

cdef void glWindowPos2sv(const GLshort *v):
    cglWindowPos2sv(v)

cdef void glWindowPos3d(GLdouble x, GLdouble y, GLdouble z):
    cglWindowPos3d(x, y, z)

cdef void glWindowPos3dv(const GLdouble *v):
    cglWindowPos3dv(v)

cdef void glWindowPos3f(GLfloat x, GLfloat y, GLfloat z):
    cglWindowPos3f(x, y, z)

cdef void glWindowPos3fv(const GLfloat *v):
    cglWindowPos3fv(v)

cdef void glWindowPos3i(GLint x, GLint y, GLint z):
    cglWindowPos3i(x, y, z)

cdef void glWindowPos3iv(const GLint *v):
    cglWindowPos3iv(v)

cdef void glWindowPos3s(GLshort x, GLshort y, GLshort z):
    cglWindowPos3s(x, y, z)

cdef void glWindowPos3sv(const GLshort *v):
    cglWindowPos3sv(v)
