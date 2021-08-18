# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_BLEND_DST_RGB = 0x80C8
cdef GLenum GL_BLEND_SRC_RGB = 0x80C9
cdef GLenum GL_BLEND_DST_ALPHA = 0x80CA
cdef GLenum GL_BLEND_SRC_ALPHA = 0x80CB
cdef GLenum GL_POINT_FADE_THRESHOLD_SIZE = 0x8128
cdef GLenum GL_DEPTH_COMPONENT16 = 0x81A5
cdef GLenum GL_DEPTH_COMPONENT24 = 0x81A6
cdef GLenum GL_DEPTH_COMPONENT32 = 0x81A7
cdef GLenum GL_MIRRORED_REPEAT = 0x8370
cdef GLenum GL_MAX_TEXTURE_LOD_BIAS = 0x84FD
cdef GLenum GL_TEXTURE_LOD_BIAS = 0x8501
cdef GLenum GL_INCR_WRAP = 0x8507
cdef GLenum GL_DECR_WRAP = 0x8508
cdef GLenum GL_TEXTURE_DEPTH_SIZE = 0x884A
cdef GLenum GL_TEXTURE_COMPARE_MODE = 0x884C
cdef GLenum GL_TEXTURE_COMPARE_FUNC = 0x884D
cdef GLenum GL_POINT_SIZE_MIN = 0x8126
cdef GLenum GL_POINT_SIZE_MAX = 0x8127
cdef GLenum GL_POINT_DISTANCE_ATTENUATION = 0x8129
cdef GLenum GL_GENERATE_MIPMAP = 0x8191
cdef GLenum GL_GENERATE_MIPMAP_HINT = 0x8192
cdef GLenum GL_FOG_COORDINATE_SOURCE = 0x8450
cdef GLenum GL_FOG_COORDINATE = 0x8451
cdef GLenum GL_FRAGMENT_DEPTH = 0x8452
cdef GLenum GL_CURRENT_FOG_COORDINATE = 0x8453
cdef GLenum GL_FOG_COORDINATE_ARRAY_TYPE = 0x8454
cdef GLenum GL_FOG_COORDINATE_ARRAY_STRIDE = 0x8455
cdef GLenum GL_FOG_COORDINATE_ARRAY_POINTER = 0x8456
cdef GLenum GL_FOG_COORDINATE_ARRAY = 0x8457
cdef GLenum GL_COLOR_SUM = 0x8458
cdef GLenum GL_CURRENT_SECONDARY_COLOR = 0x8459
cdef GLenum GL_SECONDARY_COLOR_ARRAY_SIZE = 0x845A
cdef GLenum GL_SECONDARY_COLOR_ARRAY_TYPE = 0x845B
cdef GLenum GL_SECONDARY_COLOR_ARRAY_STRIDE = 0x845C
cdef GLenum GL_SECONDARY_COLOR_ARRAY_POINTER = 0x845D
cdef GLenum GL_SECONDARY_COLOR_ARRAY = 0x845E
cdef GLenum GL_TEXTURE_FILTER_CONTROL = 0x8500
cdef GLenum GL_DEPTH_TEXTURE_MODE = 0x884B
cdef GLenum GL_COMPARE_R_TO_TEXTURE = 0x884E
cdef GLenum GL_BLEND_COLOR = 0x8005
cdef GLenum GL_BLEND_EQUATION = 0x8009
cdef GLenum GL_CONSTANT_COLOR = 0x8001
cdef GLenum GL_ONE_MINUS_CONSTANT_COLOR = 0x8002
cdef GLenum GL_CONSTANT_ALPHA = 0x8003
cdef GLenum GL_ONE_MINUS_CONSTANT_ALPHA = 0x8004
cdef GLenum GL_FUNC_ADD = 0x8006
cdef GLenum GL_FUNC_REVERSE_SUBTRACT = 0x800B
cdef GLenum GL_FUNC_SUBTRACT = 0x800A
cdef GLenum GL_MIN = 0x8007
cdef GLenum GL_MAX = 0x8008

ctypedef void (*GL_BLEND_FUNC_SEPARATE)(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
ctypedef void (*GL_MULTI_DRAW_ARRAYS)(GLenum mode, const GLint *first, const GLsizei *count, GLsizei drawcount)
ctypedef void (*GL_MULTI_DRAW_ELEMENTS)(GLenum mode, const GLsizei *count, GLenum type, const void *const*indices, GLsizei drawcount)
ctypedef void (*GL_POINT_PARAMETERF)(GLenum pname, GLfloat param)
ctypedef void (*GL_POINT_PARAMETERFV)(GLenum pname, const GLfloat *params)
ctypedef void (*GL_POINT_PARAMETERI)(GLenum pname, GLint param)
ctypedef void (*GL_POINT_PARAMETERIV)(GLenum pname, const GLint *params)
ctypedef void (*GL_FOG_COORDF)(GLfloat coord)
ctypedef void (*GL_FOG_COORDFV)(const GLfloat *coord)
ctypedef void (*GL_FOG_COORDD)(GLdouble coord)
ctypedef void (*GL_FOG_COORDDV)(const GLdouble *coord)
ctypedef void (*GL_FOG_COORD_POINTER)(GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*GL_SECONDARY_COLOR3B)(GLbyte red, GLbyte green, GLbyte blue)
ctypedef void (*GL_SECONDARY_COLOR3BV)(const GLbyte *v)
ctypedef void (*GL_SECONDARY_COLOR3D)(GLdouble red, GLdouble green, GLdouble blue)
ctypedef void (*GL_SECONDARY_COLOR3DV)(const GLdouble *v)
ctypedef void (*GL_SECONDARY_COLOR3F)(GLfloat red, GLfloat green, GLfloat blue)
ctypedef void (*GL_SECONDARY_COLOR3FV)(const GLfloat *v)
ctypedef void (*GL_SECONDARY_COLOR3I)(GLint red, GLint green, GLint blue)
ctypedef void (*GL_SECONDARY_COLOR3IV)(const GLint *v)
ctypedef void (*GL_SECONDARY_COLOR3S)(GLshort red, GLshort green, GLshort blue)
ctypedef void (*GL_SECONDARY_COLOR3SV)(const GLshort *v)
ctypedef void (*GL_SECONDARY_COLOR3UB)(GLubyte red, GLubyte green, GLubyte blue)
ctypedef void (*GL_SECONDARY_COLOR3UBV)(const GLubyte *v)
ctypedef void (*GL_SECONDARY_COLOR3UI)(GLuint red, GLuint green, GLuint blue)
ctypedef void (*GL_SECONDARY_COLOR3UIV)(const GLuint *v)
ctypedef void (*GL_SECONDARY_COLOR3US)(GLushort red, GLushort green, GLushort blue)
ctypedef void (*GL_SECONDARY_COLOR3USV)(const GLushort *v)
ctypedef void (*GL_SECONDARY_COLOR_POINTER)(GLint size, GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*GL_WINDOW_POS2D)(GLdouble x, GLdouble y)
ctypedef void (*GL_WINDOW_POS2DV)(const GLdouble *v)
ctypedef void (*GL_WINDOW_POS2F)(GLfloat x, GLfloat y)
ctypedef void (*GL_WINDOW_POS2FV)(const GLfloat *v)
ctypedef void (*GL_WINDOW_POS2I)(GLint x, GLint y)
ctypedef void (*GL_WINDOW_POS2IV)(const GLint *v)
ctypedef void (*GL_WINDOW_POS2S)(GLshort x, GLshort y)
ctypedef void (*GL_WINDOW_POS2SV)(const GLshort *v)
ctypedef void (*GL_WINDOW_POS3D)(GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*GL_WINDOW_POS3DV)(const GLdouble *v)
ctypedef void (*GL_WINDOW_POS3F)(GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*GL_WINDOW_POS3FV)(const GLfloat *v)
ctypedef void (*GL_WINDOW_POS3I)(GLint x, GLint y, GLint z)
ctypedef void (*GL_WINDOW_POS3IV)(const GLint *v)
ctypedef void (*GL_WINDOW_POS3S)(GLshort x, GLshort y, GLshort z)
ctypedef void (*GL_WINDOW_POS3SV)(const GLshort *v)
ctypedef void (*GL_BLEND_COLOR)(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
ctypedef void (*GL_BLEND_EQUATION)(GLenum mode)

cdef GL_BLEND_FUNC_SEPARATE cglBlendFuncSeparate = NULL
cdef GL_MULTI_DRAW_ARRAYS cglMultiDrawArrays = NULL
cdef GL_MULTI_DRAW_ELEMENTS cglMultiDrawElements = NULL
cdef GL_POINT_PARAMETERF cglPointParameterf = NULL
cdef GL_POINT_PARAMETERFV cglPointParameterfv = NULL
cdef GL_POINT_PARAMETERI cglPointParameteri = NULL
cdef GL_POINT_PARAMETERIV cglPointParameteriv = NULL
cdef GL_FOG_COORDF cglFogCoordf = NULL
cdef GL_FOG_COORDFV cglFogCoordfv = NULL
cdef GL_FOG_COORDD cglFogCoordd = NULL
cdef GL_FOG_COORDDV cglFogCoorddv = NULL
cdef GL_FOG_COORD_POINTER cglFogCoordPointer = NULL
cdef GL_SECONDARY_COLOR3B cglSecondaryColor3b = NULL
cdef GL_SECONDARY_COLOR3BV cglSecondaryColor3bv = NULL
cdef GL_SECONDARY_COLOR3D cglSecondaryColor3d = NULL
cdef GL_SECONDARY_COLOR3DV cglSecondaryColor3dv = NULL
cdef GL_SECONDARY_COLOR3F cglSecondaryColor3f = NULL
cdef GL_SECONDARY_COLOR3FV cglSecondaryColor3fv = NULL
cdef GL_SECONDARY_COLOR3I cglSecondaryColor3i = NULL
cdef GL_SECONDARY_COLOR3IV cglSecondaryColor3iv = NULL
cdef GL_SECONDARY_COLOR3S cglSecondaryColor3s = NULL
cdef GL_SECONDARY_COLOR3SV cglSecondaryColor3sv = NULL
cdef GL_SECONDARY_COLOR3UB cglSecondaryColor3ub = NULL
cdef GL_SECONDARY_COLOR3UBV cglSecondaryColor3ubv = NULL
cdef GL_SECONDARY_COLOR3UI cglSecondaryColor3ui = NULL
cdef GL_SECONDARY_COLOR3UIV cglSecondaryColor3uiv = NULL
cdef GL_SECONDARY_COLOR3US cglSecondaryColor3us = NULL
cdef GL_SECONDARY_COLOR3USV cglSecondaryColor3usv = NULL
cdef GL_SECONDARY_COLOR_POINTER cglSecondaryColorPointer = NULL
cdef GL_WINDOW_POS2D cglWindowPos2d = NULL
cdef GL_WINDOW_POS2DV cglWindowPos2dv = NULL
cdef GL_WINDOW_POS2F cglWindowPos2f = NULL
cdef GL_WINDOW_POS2FV cglWindowPos2fv = NULL
cdef GL_WINDOW_POS2I cglWindowPos2i = NULL
cdef GL_WINDOW_POS2IV cglWindowPos2iv = NULL
cdef GL_WINDOW_POS2S cglWindowPos2s = NULL
cdef GL_WINDOW_POS2SV cglWindowPos2sv = NULL
cdef GL_WINDOW_POS3D cglWindowPos3d = NULL
cdef GL_WINDOW_POS3DV cglWindowPos3dv = NULL
cdef GL_WINDOW_POS3F cglWindowPos3f = NULL
cdef GL_WINDOW_POS3FV cglWindowPos3fv = NULL
cdef GL_WINDOW_POS3I cglWindowPos3i = NULL
cdef GL_WINDOW_POS3IV cglWindowPos3iv = NULL
cdef GL_WINDOW_POS3S cglWindowPos3s = NULL
cdef GL_WINDOW_POS3SV cglWindowPos3sv = NULL
cdef GL_BLEND_COLOR cglBlendColor = NULL
cdef GL_BLEND_EQUATION cglBlendEquation = NULL


cdef void GetglBlendFuncSeparate(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha):
    global cglBlendFuncSeparate
    cglBlendFuncSeparate = <GL_BLEND_FUNC_SEPARATE>getFunction(b"glBlendFuncSeparate")
    cglBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)

cdef void GetglMultiDrawArrays(GLenum mode, const GLint *first, const GLsizei *count, GLsizei drawcount):
    global cglMultiDrawArrays
    cglMultiDrawArrays = <GL_MULTI_DRAW_ARRAYS>getFunction(b"glMultiDrawArrays")
    cglMultiDrawArrays(mode, first, count, drawcount)

cdef void GetglMultiDrawElements(GLenum mode, const GLsizei *count, GLenum type, const void *const*indices, GLsizei drawcount):
    global cglMultiDrawElements
    cglMultiDrawElements = <GL_MULTI_DRAW_ELEMENTS>getFunction(b"glMultiDrawElements")
    cglMultiDrawElements(mode, count, type, indices, drawcount)

cdef void GetglPointParameterf(GLenum pname, GLfloat param):
    global cglPointParameterf
    cglPointParameterf = <GL_POINT_PARAMETERF>getFunction(b"glPointParameterf")
    cglPointParameterf(pname, param)

cdef void GetglPointParameterfv(GLenum pname, const GLfloat *params):
    global cglPointParameterfv
    cglPointParameterfv = <GL_POINT_PARAMETERFV>getFunction(b"glPointParameterfv")
    cglPointParameterfv(pname, params)

cdef void GetglPointParameteri(GLenum pname, GLint param):
    global cglPointParameteri
    cglPointParameteri = <GL_POINT_PARAMETERI>getFunction(b"glPointParameteri")
    cglPointParameteri(pname, param)

cdef void GetglPointParameteriv(GLenum pname, const GLint *params):
    global cglPointParameteriv
    cglPointParameteriv = <GL_POINT_PARAMETERIV>getFunction(b"glPointParameteriv")
    cglPointParameteriv(pname, params)

cdef void GetglFogCoordf(GLfloat coord):
    global cglFogCoordf
    cglFogCoordf = <GL_FOG_COORDF>getFunction(b"glFogCoordf")
    cglFogCoordf(coord)

cdef void GetglFogCoordfv(const GLfloat *coord):
    global cglFogCoordfv
    cglFogCoordfv = <GL_FOG_COORDFV>getFunction(b"glFogCoordfv")
    cglFogCoordfv(coord)

cdef void GetglFogCoordd(GLdouble coord):
    global cglFogCoordd
    cglFogCoordd = <GL_FOG_COORDD>getFunction(b"glFogCoordd")
    cglFogCoordd(coord)

cdef void GetglFogCoorddv(const GLdouble *coord):
    global cglFogCoorddv
    cglFogCoorddv = <GL_FOG_COORDDV>getFunction(b"glFogCoorddv")
    cglFogCoorddv(coord)

cdef void GetglFogCoordPointer(GLenum type, GLsizei stride, const void *pointer):
    global cglFogCoordPointer
    cglFogCoordPointer = <GL_FOG_COORD_POINTER>getFunction(b"glFogCoordPointer")
    cglFogCoordPointer(type, stride, pointer)

cdef void GetglSecondaryColor3b(GLbyte red, GLbyte green, GLbyte blue):
    global cglSecondaryColor3b
    cglSecondaryColor3b = <GL_SECONDARY_COLOR3B>getFunction(b"glSecondaryColor3b")
    cglSecondaryColor3b(red, green, blue)

cdef void GetglSecondaryColor3bv(const GLbyte *v):
    global cglSecondaryColor3bv
    cglSecondaryColor3bv = <GL_SECONDARY_COLOR3BV>getFunction(b"glSecondaryColor3bv")
    cglSecondaryColor3bv(v)

cdef void GetglSecondaryColor3d(GLdouble red, GLdouble green, GLdouble blue):
    global cglSecondaryColor3d
    cglSecondaryColor3d = <GL_SECONDARY_COLOR3D>getFunction(b"glSecondaryColor3d")
    cglSecondaryColor3d(red, green, blue)

cdef void GetglSecondaryColor3dv(const GLdouble *v):
    global cglSecondaryColor3dv
    cglSecondaryColor3dv = <GL_SECONDARY_COLOR3DV>getFunction(b"glSecondaryColor3dv")
    cglSecondaryColor3dv(v)

cdef void GetglSecondaryColor3f(GLfloat red, GLfloat green, GLfloat blue):
    global cglSecondaryColor3f
    cglSecondaryColor3f = <GL_SECONDARY_COLOR3F>getFunction(b"glSecondaryColor3f")
    cglSecondaryColor3f(red, green, blue)

cdef void GetglSecondaryColor3fv(const GLfloat *v):
    global cglSecondaryColor3fv
    cglSecondaryColor3fv = <GL_SECONDARY_COLOR3FV>getFunction(b"glSecondaryColor3fv")
    cglSecondaryColor3fv(v)

cdef void GetglSecondaryColor3i(GLint red, GLint green, GLint blue):
    global cglSecondaryColor3i
    cglSecondaryColor3i = <GL_SECONDARY_COLOR3I>getFunction(b"glSecondaryColor3i")
    cglSecondaryColor3i(red, green, blue)

cdef void GetglSecondaryColor3iv(const GLint *v):
    global cglSecondaryColor3iv
    cglSecondaryColor3iv = <GL_SECONDARY_COLOR3IV>getFunction(b"glSecondaryColor3iv")
    cglSecondaryColor3iv(v)

cdef void GetglSecondaryColor3s(GLshort red, GLshort green, GLshort blue):
    global cglSecondaryColor3s
    cglSecondaryColor3s = <GL_SECONDARY_COLOR3S>getFunction(b"glSecondaryColor3s")
    cglSecondaryColor3s(red, green, blue)

cdef void GetglSecondaryColor3sv(const GLshort *v):
    global cglSecondaryColor3sv
    cglSecondaryColor3sv = <GL_SECONDARY_COLOR3SV>getFunction(b"glSecondaryColor3sv")
    cglSecondaryColor3sv(v)

cdef void GetglSecondaryColor3ub(GLubyte red, GLubyte green, GLubyte blue):
    global cglSecondaryColor3ub
    cglSecondaryColor3ub = <GL_SECONDARY_COLOR3UB>getFunction(b"glSecondaryColor3ub")
    cglSecondaryColor3ub(red, green, blue)

cdef void GetglSecondaryColor3ubv(const GLubyte *v):
    global cglSecondaryColor3ubv
    cglSecondaryColor3ubv = <GL_SECONDARY_COLOR3UBV>getFunction(b"glSecondaryColor3ubv")
    cglSecondaryColor3ubv(v)

cdef void GetglSecondaryColor3ui(GLuint red, GLuint green, GLuint blue):
    global cglSecondaryColor3ui
    cglSecondaryColor3ui = <GL_SECONDARY_COLOR3UI>getFunction(b"glSecondaryColor3ui")
    cglSecondaryColor3ui(red, green, blue)

cdef void GetglSecondaryColor3uiv(const GLuint *v):
    global cglSecondaryColor3uiv
    cglSecondaryColor3uiv = <GL_SECONDARY_COLOR3UIV>getFunction(b"glSecondaryColor3uiv")
    cglSecondaryColor3uiv(v)

cdef void GetglSecondaryColor3us(GLushort red, GLushort green, GLushort blue):
    global cglSecondaryColor3us
    cglSecondaryColor3us = <GL_SECONDARY_COLOR3US>getFunction(b"glSecondaryColor3us")
    cglSecondaryColor3us(red, green, blue)

cdef void GetglSecondaryColor3usv(const GLushort *v):
    global cglSecondaryColor3usv
    cglSecondaryColor3usv = <GL_SECONDARY_COLOR3USV>getFunction(b"glSecondaryColor3usv")
    cglSecondaryColor3usv(v)

cdef void GetglSecondaryColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglSecondaryColorPointer
    cglSecondaryColorPointer = <GL_SECONDARY_COLOR_POINTER>getFunction(b"glSecondaryColorPointer")
    cglSecondaryColorPointer(size, type, stride, pointer)

cdef void GetglWindowPos2d(GLdouble x, GLdouble y):
    global cglWindowPos2d
    cglWindowPos2d = <GL_WINDOW_POS2D>getFunction(b"glWindowPos2d")
    cglWindowPos2d(x, y)

cdef void GetglWindowPos2dv(const GLdouble *v):
    global cglWindowPos2dv
    cglWindowPos2dv = <GL_WINDOW_POS2DV>getFunction(b"glWindowPos2dv")
    cglWindowPos2dv(v)

cdef void GetglWindowPos2f(GLfloat x, GLfloat y):
    global cglWindowPos2f
    cglWindowPos2f = <GL_WINDOW_POS2F>getFunction(b"glWindowPos2f")
    cglWindowPos2f(x, y)

cdef void GetglWindowPos2fv(const GLfloat *v):
    global cglWindowPos2fv
    cglWindowPos2fv = <GL_WINDOW_POS2FV>getFunction(b"glWindowPos2fv")
    cglWindowPos2fv(v)

cdef void GetglWindowPos2i(GLint x, GLint y):
    global cglWindowPos2i
    cglWindowPos2i = <GL_WINDOW_POS2I>getFunction(b"glWindowPos2i")
    cglWindowPos2i(x, y)

cdef void GetglWindowPos2iv(const GLint *v):
    global cglWindowPos2iv
    cglWindowPos2iv = <GL_WINDOW_POS2IV>getFunction(b"glWindowPos2iv")
    cglWindowPos2iv(v)

cdef void GetglWindowPos2s(GLshort x, GLshort y):
    global cglWindowPos2s
    cglWindowPos2s = <GL_WINDOW_POS2S>getFunction(b"glWindowPos2s")
    cglWindowPos2s(x, y)

cdef void GetglWindowPos2sv(const GLshort *v):
    global cglWindowPos2sv
    cglWindowPos2sv = <GL_WINDOW_POS2SV>getFunction(b"glWindowPos2sv")
    cglWindowPos2sv(v)

cdef void GetglWindowPos3d(GLdouble x, GLdouble y, GLdouble z):
    global cglWindowPos3d
    cglWindowPos3d = <GL_WINDOW_POS3D>getFunction(b"glWindowPos3d")
    cglWindowPos3d(x, y, z)

cdef void GetglWindowPos3dv(const GLdouble *v):
    global cglWindowPos3dv
    cglWindowPos3dv = <GL_WINDOW_POS3DV>getFunction(b"glWindowPos3dv")
    cglWindowPos3dv(v)

cdef void GetglWindowPos3f(GLfloat x, GLfloat y, GLfloat z):
    global cglWindowPos3f
    cglWindowPos3f = <GL_WINDOW_POS3F>getFunction(b"glWindowPos3f")
    cglWindowPos3f(x, y, z)

cdef void GetglWindowPos3fv(const GLfloat *v):
    global cglWindowPos3fv
    cglWindowPos3fv = <GL_WINDOW_POS3FV>getFunction(b"glWindowPos3fv")
    cglWindowPos3fv(v)

cdef void GetglWindowPos3i(GLint x, GLint y, GLint z):
    global cglWindowPos3i
    cglWindowPos3i = <GL_WINDOW_POS3I>getFunction(b"glWindowPos3i")
    cglWindowPos3i(x, y, z)

cdef void GetglWindowPos3iv(const GLint *v):
    global cglWindowPos3iv
    cglWindowPos3iv = <GL_WINDOW_POS3IV>getFunction(b"glWindowPos3iv")
    cglWindowPos3iv(v)

cdef void GetglWindowPos3s(GLshort x, GLshort y, GLshort z):
    global cglWindowPos3s
    cglWindowPos3s = <GL_WINDOW_POS3S>getFunction(b"glWindowPos3s")
    cglWindowPos3s(x, y, z)

cdef void GetglWindowPos3sv(const GLshort *v):
    global cglWindowPos3sv
    cglWindowPos3sv = <GL_WINDOW_POS3SV>getFunction(b"glWindowPos3sv")
    cglWindowPos3sv(v)

cdef void GetglBlendColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    global cglBlendColor
    cglBlendColor = <GL_BLEND_COLOR>getFunction(b"glBlendColor")
    cglBlendColor(red, green, blue, alpha)

cdef void GetglBlendEquation(GLenum mode):
    global cglBlendEquation
    cglBlendEquation = <GL_BLEND_EQUATION>getFunction(b"glBlendEquation")
    cglBlendEquation(mode)

cglBlendFuncSeparate = GetglBlendFuncSeparate
cglMultiDrawArrays = GetglMultiDrawArrays
cglMultiDrawElements = GetglMultiDrawElements
cglPointParameterf = GetglPointParameterf
cglPointParameterfv = GetglPointParameterfv
cglPointParameteri = GetglPointParameteri
cglPointParameteriv = GetglPointParameteriv
cglFogCoordf = GetglFogCoordf
cglFogCoordfv = GetglFogCoordfv
cglFogCoordd = GetglFogCoordd
cglFogCoorddv = GetglFogCoorddv
cglFogCoordPointer = GetglFogCoordPointer
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
cglBlendColor = GetglBlendColor
cglBlendEquation = GetglBlendEquation


cpdef void glBlendFuncSeparate(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha):
    cglBlendFuncSeparate(sfactorRGB, dfactorRGB, sfactorAlpha, dfactorAlpha)

cpdef void glMultiDrawArrays(GLenum mode, const GLint *first, const GLsizei *count, GLsizei drawcount):
    cglMultiDrawArrays(mode, first, count, drawcount)

cpdef void glMultiDrawElements(GLenum mode, const GLsizei *count, GLenum type, const void *const*indices, GLsizei drawcount):
    cglMultiDrawElements(mode, count, type, indices, drawcount)

cpdef void glPointParameterf(GLenum pname, GLfloat param):
    cglPointParameterf(pname, param)

cpdef void glPointParameterfv(GLenum pname, const GLfloat *params):
    cglPointParameterfv(pname, params)

cpdef void glPointParameteri(GLenum pname, GLint param):
    cglPointParameteri(pname, param)

cpdef void glPointParameteriv(GLenum pname, const GLint *params):
    cglPointParameteriv(pname, params)

cpdef void glFogCoordf(GLfloat coord):
    cglFogCoordf(coord)

cpdef void glFogCoordfv(const GLfloat *coord):
    cglFogCoordfv(coord)

cpdef void glFogCoordd(GLdouble coord):
    cglFogCoordd(coord)

cpdef void glFogCoorddv(const GLdouble *coord):
    cglFogCoorddv(coord)

cpdef void glFogCoordPointer(GLenum type, GLsizei stride, const void *pointer):
    cglFogCoordPointer(type, stride, pointer)

cpdef void glSecondaryColor3b(GLbyte red, GLbyte green, GLbyte blue):
    cglSecondaryColor3b(red, green, blue)

cpdef void glSecondaryColor3bv(const GLbyte *v):
    cglSecondaryColor3bv(v)

cpdef void glSecondaryColor3d(GLdouble red, GLdouble green, GLdouble blue):
    cglSecondaryColor3d(red, green, blue)

cpdef void glSecondaryColor3dv(const GLdouble *v):
    cglSecondaryColor3dv(v)

cpdef void glSecondaryColor3f(GLfloat red, GLfloat green, GLfloat blue):
    cglSecondaryColor3f(red, green, blue)

cpdef void glSecondaryColor3fv(const GLfloat *v):
    cglSecondaryColor3fv(v)

cpdef void glSecondaryColor3i(GLint red, GLint green, GLint blue):
    cglSecondaryColor3i(red, green, blue)

cpdef void glSecondaryColor3iv(const GLint *v):
    cglSecondaryColor3iv(v)

cpdef void glSecondaryColor3s(GLshort red, GLshort green, GLshort blue):
    cglSecondaryColor3s(red, green, blue)

cpdef void glSecondaryColor3sv(const GLshort *v):
    cglSecondaryColor3sv(v)

cpdef void glSecondaryColor3ub(GLubyte red, GLubyte green, GLubyte blue):
    cglSecondaryColor3ub(red, green, blue)

cpdef void glSecondaryColor3ubv(const GLubyte *v):
    cglSecondaryColor3ubv(v)

cpdef void glSecondaryColor3ui(GLuint red, GLuint green, GLuint blue):
    cglSecondaryColor3ui(red, green, blue)

cpdef void glSecondaryColor3uiv(const GLuint *v):
    cglSecondaryColor3uiv(v)

cpdef void glSecondaryColor3us(GLushort red, GLushort green, GLushort blue):
    cglSecondaryColor3us(red, green, blue)

cpdef void glSecondaryColor3usv(const GLushort *v):
    cglSecondaryColor3usv(v)

cpdef void glSecondaryColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglSecondaryColorPointer(size, type, stride, pointer)

cpdef void glWindowPos2d(GLdouble x, GLdouble y):
    cglWindowPos2d(x, y)

cpdef void glWindowPos2dv(const GLdouble *v):
    cglWindowPos2dv(v)

cpdef void glWindowPos2f(GLfloat x, GLfloat y):
    cglWindowPos2f(x, y)

cpdef void glWindowPos2fv(const GLfloat *v):
    cglWindowPos2fv(v)

cpdef void glWindowPos2i(GLint x, GLint y):
    cglWindowPos2i(x, y)

cpdef void glWindowPos2iv(const GLint *v):
    cglWindowPos2iv(v)

cpdef void glWindowPos2s(GLshort x, GLshort y):
    cglWindowPos2s(x, y)

cpdef void glWindowPos2sv(const GLshort *v):
    cglWindowPos2sv(v)

cpdef void glWindowPos3d(GLdouble x, GLdouble y, GLdouble z):
    cglWindowPos3d(x, y, z)

cpdef void glWindowPos3dv(const GLdouble *v):
    cglWindowPos3dv(v)

cpdef void glWindowPos3f(GLfloat x, GLfloat y, GLfloat z):
    cglWindowPos3f(x, y, z)

cpdef void glWindowPos3fv(const GLfloat *v):
    cglWindowPos3fv(v)

cpdef void glWindowPos3i(GLint x, GLint y, GLint z):
    cglWindowPos3i(x, y, z)

cpdef void glWindowPos3iv(const GLint *v):
    cglWindowPos3iv(v)

cpdef void glWindowPos3s(GLshort x, GLshort y, GLshort z):
    cglWindowPos3s(x, y, z)

cpdef void glWindowPos3sv(const GLshort *v):
    cglWindowPos3sv(v)

cpdef void glBlendColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    cglBlendColor(red, green, blue, alpha)

cpdef void glBlendEquation(GLenum mode):
    cglBlendEquation(mode)
