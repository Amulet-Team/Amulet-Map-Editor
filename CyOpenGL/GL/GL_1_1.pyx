# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_ALPHA12 = 0x803D
cdef GLenum GL_ALPHA16 = 0x803E
cdef GLenum GL_ALPHA4 = 0x803B
cdef GLenum GL_ALPHA8 = 0x803C
cdef GLenum GL_C3F_V3F = 0x2A24
cdef GLenum GL_C4F_N3F_V3F = 0x2A26
cdef GLenum GL_C4UB_V2F = 0x2A22
cdef GLenum GL_C4UB_V3F = 0x2A23
cdef GLenum GL_CLIENT_ALL_ATTRIB_BITS = 0xFFFFFFFF
cdef GLenum GL_CLIENT_ATTRIB_STACK_DEPTH = 0x0BB1
cdef GLenum GL_CLIENT_PIXEL_STORE_BIT = 0x00000001
cdef GLenum GL_CLIENT_VERTEX_ARRAY_BIT = 0x00000002
cdef GLenum GL_COLOR_ARRAY = 0x8076
cdef GLenum GL_COLOR_ARRAY_POINTER = 0x8090
cdef GLenum GL_COLOR_ARRAY_SIZE = 0x8081
cdef GLenum GL_COLOR_ARRAY_STRIDE = 0x8083
cdef GLenum GL_COLOR_ARRAY_TYPE = 0x8082
cdef GLenum GL_COLOR_LOGIC_OP = 0x0BF2
cdef GLenum GL_DOUBLE = 0x140A
cdef GLenum GL_EDGE_FLAG_ARRAY = 0x8079
cdef GLenum GL_EDGE_FLAG_ARRAY_POINTER = 0x8093
cdef GLenum GL_EDGE_FLAG_ARRAY_STRIDE = 0x808C
cdef GLenum GL_FEEDBACK_BUFFER_POINTER = 0x0DF0
cdef GLenum GL_FEEDBACK_BUFFER_SIZE = 0x0DF1
cdef GLenum GL_FEEDBACK_BUFFER_TYPE = 0x0DF2
cdef GLenum GL_INDEX_ARRAY = 0x8077
cdef GLenum GL_INDEX_ARRAY_POINTER = 0x8091
cdef GLenum GL_INDEX_ARRAY_STRIDE = 0x8086
cdef GLenum GL_INDEX_ARRAY_TYPE = 0x8085
cdef GLenum GL_INDEX_LOGIC_OP = 0x0BF1
cdef GLenum GL_INTENSITY = 0x8049
cdef GLenum GL_INTENSITY12 = 0x804C
cdef GLenum GL_INTENSITY16 = 0x804D
cdef GLenum GL_INTENSITY4 = 0x804A
cdef GLenum GL_INTENSITY8 = 0x804B
cdef GLenum GL_LUMINANCE12 = 0x8041
cdef GLenum GL_LUMINANCE12_ALPHA12 = 0x8047
cdef GLenum GL_LUMINANCE12_ALPHA4 = 0x8046
cdef GLenum GL_LUMINANCE16 = 0x8042
cdef GLenum GL_LUMINANCE16_ALPHA16 = 0x8048
cdef GLenum GL_LUMINANCE4 = 0x803F
cdef GLenum GL_LUMINANCE4_ALPHA4 = 0x8043
cdef GLenum GL_LUMINANCE6_ALPHA2 = 0x8044
cdef GLenum GL_LUMINANCE8 = 0x8040
cdef GLenum GL_LUMINANCE8_ALPHA8 = 0x8045
cdef GLenum GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 0x0D3B
cdef GLenum GL_N3F_V3F = 0x2A25
cdef GLenum GL_NORMAL_ARRAY = 0x8075
cdef GLenum GL_NORMAL_ARRAY_POINTER = 0x808F
cdef GLenum GL_NORMAL_ARRAY_STRIDE = 0x807F
cdef GLenum GL_NORMAL_ARRAY_TYPE = 0x807E
cdef GLenum GL_POLYGON_OFFSET_FACTOR = 0x8038
cdef GLenum GL_POLYGON_OFFSET_FILL = 0x8037
cdef GLenum GL_POLYGON_OFFSET_LINE = 0x2A02
cdef GLenum GL_POLYGON_OFFSET_POINT = 0x2A01
cdef GLenum GL_POLYGON_OFFSET_UNITS = 0x2A00
cdef GLenum GL_PROXY_TEXTURE_1D = 0x8063
cdef GLenum GL_PROXY_TEXTURE_2D = 0x8064
cdef GLenum GL_R3_G3_B2 = 0x2A10
cdef GLenum GL_RGB10 = 0x8052
cdef GLenum GL_RGB10_A2 = 0x8059
cdef GLenum GL_RGB12 = 0x8053
cdef GLenum GL_RGB16 = 0x8054
cdef GLenum GL_RGB4 = 0x804F
cdef GLenum GL_RGB5 = 0x8050
cdef GLenum GL_RGB5_A1 = 0x8057
cdef GLenum GL_RGB8 = 0x8051
cdef GLenum GL_RGBA12 = 0x805A
cdef GLenum GL_RGBA16 = 0x805B
cdef GLenum GL_RGBA2 = 0x8055
cdef GLenum GL_RGBA4 = 0x8056
cdef GLenum GL_RGBA8 = 0x8058
cdef GLenum GL_SELECTION_BUFFER_POINTER = 0x0DF3
cdef GLenum GL_SELECTION_BUFFER_SIZE = 0x0DF4
cdef GLenum GL_T2F_C3F_V3F = 0x2A2A
cdef GLenum GL_T2F_C4F_N3F_V3F = 0x2A2C
cdef GLenum GL_T2F_C4UB_V3F = 0x2A29
cdef GLenum GL_T2F_N3F_V3F = 0x2A2B
cdef GLenum GL_T2F_V3F = 0x2A27
cdef GLenum GL_T4F_C4F_N3F_V4F = 0x2A2D
cdef GLenum GL_T4F_V4F = 0x2A28
cdef GLenum GL_TEXTURE_ALPHA_SIZE = 0x805F
cdef GLenum GL_TEXTURE_BINDING_1D = 0x8068
cdef GLenum GL_TEXTURE_BINDING_2D = 0x8069
cdef GLenum GL_TEXTURE_BLUE_SIZE = 0x805E
cdef GLenum GL_TEXTURE_COORD_ARRAY = 0x8078
cdef GLenum GL_TEXTURE_COORD_ARRAY_POINTER = 0x8092
cdef GLenum GL_TEXTURE_COORD_ARRAY_SIZE = 0x8088
cdef GLenum GL_TEXTURE_COORD_ARRAY_STRIDE = 0x808A
cdef GLenum GL_TEXTURE_COORD_ARRAY_TYPE = 0x8089
cdef GLenum GL_TEXTURE_GREEN_SIZE = 0x805D
cdef GLenum GL_TEXTURE_INTENSITY_SIZE = 0x8061
cdef GLenum GL_TEXTURE_INTERNAL_FORMAT = 0x1003
cdef GLenum GL_TEXTURE_LUMINANCE_SIZE = 0x8060
cdef GLenum GL_TEXTURE_PRIORITY = 0x8066
cdef GLenum GL_TEXTURE_RED_SIZE = 0x805C
cdef GLenum GL_TEXTURE_RESIDENT = 0x8067
cdef GLenum GL_V2F = 0x2A20
cdef GLenum GL_V3F = 0x2A21
cdef GLenum GL_VERTEX_ARRAY = 0x8074
cdef GLenum GL_VERTEX_ARRAY_POINTER = 0x808E
cdef GLenum GL_VERTEX_ARRAY_SIZE = 0x807A
cdef GLenum GL_VERTEX_ARRAY_STRIDE = 0x807C
cdef GLenum GL_VERTEX_ARRAY_TYPE = 0x807B

ctypedef GLboolean (*PFNGLARETEXTURESRESIDENTPROC)(GLsizei n, const GLuint *textures, GLboolean *residences)
ctypedef void (*PFNGLARRAYELEMENTPROC)(GLint i)
ctypedef void (*PFNGLBINDTEXTUREPROC)(GLenum target, GLuint texture)
ctypedef void (*PFNGLCOLORPOINTERPROC)(GLint size, GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*PFNGLCOPYTEXIMAGE1DPROC)(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
ctypedef void (*PFNGLCOPYTEXIMAGE2DPROC)(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border)
ctypedef void (*PFNGLCOPYTEXSUBIMAGE1DPROC)(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
ctypedef void (*PFNGLCOPYTEXSUBIMAGE2DPROC)(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*PFNGLDELETETEXTURESPROC)(GLsizei n, const GLuint *textures)
ctypedef void (*PFNGLDISABLECLIENTSTATEPROC)(GLenum array)
ctypedef void (*PFNGLDRAWARRAYSPROC)(GLenum mode, GLint first, GLsizei count)
ctypedef void (*PFNGLDRAWELEMENTSPROC)(GLenum mode, GLsizei count, GLenum type, const void *indices)
ctypedef void (*PFNGLEDGEFLAGPOINTERPROC)(GLsizei stride, const void *pointer)
ctypedef void (*PFNGLENABLECLIENTSTATEPROC)(GLenum array)
ctypedef void (*PFNGLGENTEXTURESPROC)(GLsizei n, GLuint *textures)
ctypedef void (*PFNGLGETPOINTERVPROC)(GLenum pname, void **params)
ctypedef void (*PFNGLINDEXPOINTERPROC)(GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*PFNGLINDEXUBPROC)(GLubyte c)
ctypedef void (*PFNGLINDEXUBVPROC)(const GLubyte *c)
ctypedef void (*PFNGLINTERLEAVEDARRAYSPROC)(GLenum format, GLsizei stride, const void *pointer)
ctypedef GLboolean (*PFNGLISTEXTUREPROC)(GLuint texture)
ctypedef void (*PFNGLNORMALPOINTERPROC)(GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*PFNGLPOLYGONOFFSETPROC)(GLfloat factor, GLfloat units)
ctypedef void (*PFNGLPOPCLIENTATTRIBPROC)()
ctypedef void (*PFNGLPRIORITIZETEXTURESPROC)(GLsizei n, const GLuint *textures, const GLfloat *priorities)
ctypedef void (*PFNGLPUSHCLIENTATTRIBPROC)(GLbitfield mask)
ctypedef void (*PFNGLTEXCOORDPOINTERPROC)(GLint size, GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*PFNGLTEXSUBIMAGE1DPROC)(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels)
ctypedef void (*PFNGLTEXSUBIMAGE2DPROC)(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
ctypedef void (*PFNGLVERTEXPOINTERPROC)(GLint size, GLenum type, GLsizei stride, const void *pointer)

cdef PFNGLARETEXTURESRESIDENTPROC cglAreTexturesResident = NULL
cdef PFNGLARRAYELEMENTPROC cglArrayElement = NULL
cdef PFNGLBINDTEXTUREPROC cglBindTexture = NULL
cdef PFNGLCOLORPOINTERPROC cglColorPointer = NULL
cdef PFNGLCOPYTEXIMAGE1DPROC cglCopyTexImage1D = NULL
cdef PFNGLCOPYTEXIMAGE2DPROC cglCopyTexImage2D = NULL
cdef PFNGLCOPYTEXSUBIMAGE1DPROC cglCopyTexSubImage1D = NULL
cdef PFNGLCOPYTEXSUBIMAGE2DPROC cglCopyTexSubImage2D = NULL
cdef PFNGLDELETETEXTURESPROC cglDeleteTextures = NULL
cdef PFNGLDISABLECLIENTSTATEPROC cglDisableClientState = NULL
cdef PFNGLDRAWARRAYSPROC cglDrawArrays = NULL
cdef PFNGLDRAWELEMENTSPROC cglDrawElements = NULL
cdef PFNGLEDGEFLAGPOINTERPROC cglEdgeFlagPointer = NULL
cdef PFNGLENABLECLIENTSTATEPROC cglEnableClientState = NULL
cdef PFNGLGENTEXTURESPROC cglGenTextures = NULL
cdef PFNGLGETPOINTERVPROC cglGetPointerv = NULL
cdef PFNGLINDEXPOINTERPROC cglIndexPointer = NULL
cdef PFNGLINDEXUBPROC cglIndexub = NULL
cdef PFNGLINDEXUBVPROC cglIndexubv = NULL
cdef PFNGLINTERLEAVEDARRAYSPROC cglInterleavedArrays = NULL
cdef PFNGLISTEXTUREPROC cglIsTexture = NULL
cdef PFNGLNORMALPOINTERPROC cglNormalPointer = NULL
cdef PFNGLPOLYGONOFFSETPROC cglPolygonOffset = NULL
cdef PFNGLPOPCLIENTATTRIBPROC cglPopClientAttrib = NULL
cdef PFNGLPRIORITIZETEXTURESPROC cglPrioritizeTextures = NULL
cdef PFNGLPUSHCLIENTATTRIBPROC cglPushClientAttrib = NULL
cdef PFNGLTEXCOORDPOINTERPROC cglTexCoordPointer = NULL
cdef PFNGLTEXSUBIMAGE1DPROC cglTexSubImage1D = NULL
cdef PFNGLTEXSUBIMAGE2DPROC cglTexSubImage2D = NULL
cdef PFNGLVERTEXPOINTERPROC cglVertexPointer = NULL


cdef GLboolean GetglAreTexturesResident(GLsizei n, const GLuint *textures, GLboolean *residences):
    global cglAreTexturesResident
    cglAreTexturesResident = <PFNGLARETEXTURESRESIDENTPROC>getFunction(b"glAreTexturesResident")
    cglAreTexturesResident(n, textures, residences)

cdef void GetglArrayElement(GLint i):
    global cglArrayElement
    cglArrayElement = <PFNGLARRAYELEMENTPROC>getFunction(b"glArrayElement")
    cglArrayElement(i)

cdef void GetglBindTexture(GLenum target, GLuint texture):
    global cglBindTexture
    cglBindTexture = <PFNGLBINDTEXTUREPROC>getFunction(b"glBindTexture")
    cglBindTexture(target, texture)

cdef void GetglColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglColorPointer
    cglColorPointer = <PFNGLCOLORPOINTERPROC>getFunction(b"glColorPointer")
    cglColorPointer(size, type, stride, pointer)

cdef void GetglCopyTexImage1D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border):
    global cglCopyTexImage1D
    cglCopyTexImage1D = <PFNGLCOPYTEXIMAGE1DPROC>getFunction(b"glCopyTexImage1D")
    cglCopyTexImage1D(target, level, internalformat, x, y, width, border)

cdef void GetglCopyTexImage2D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border):
    global cglCopyTexImage2D
    cglCopyTexImage2D = <PFNGLCOPYTEXIMAGE2DPROC>getFunction(b"glCopyTexImage2D")
    cglCopyTexImage2D(target, level, internalformat, x, y, width, height, border)

cdef void GetglCopyTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width):
    global cglCopyTexSubImage1D
    cglCopyTexSubImage1D = <PFNGLCOPYTEXSUBIMAGE1DPROC>getFunction(b"glCopyTexSubImage1D")
    cglCopyTexSubImage1D(target, level, xoffset, x, y, width)

cdef void GetglCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglCopyTexSubImage2D
    cglCopyTexSubImage2D = <PFNGLCOPYTEXSUBIMAGE2DPROC>getFunction(b"glCopyTexSubImage2D")
    cglCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)

cdef void GetglDeleteTextures(GLsizei n, const GLuint *textures):
    global cglDeleteTextures
    cglDeleteTextures = <PFNGLDELETETEXTURESPROC>getFunction(b"glDeleteTextures")
    cglDeleteTextures(n, textures)

cdef void GetglDisableClientState(GLenum array):
    global cglDisableClientState
    cglDisableClientState = <PFNGLDISABLECLIENTSTATEPROC>getFunction(b"glDisableClientState")
    cglDisableClientState(array)

cdef void GetglDrawArrays(GLenum mode, GLint first, GLsizei count):
    global cglDrawArrays
    cglDrawArrays = <PFNGLDRAWARRAYSPROC>getFunction(b"glDrawArrays")
    cglDrawArrays(mode, first, count)

cdef void GetglDrawElements(GLenum mode, GLsizei count, GLenum type, const void *indices):
    global cglDrawElements
    cglDrawElements = <PFNGLDRAWELEMENTSPROC>getFunction(b"glDrawElements")
    cglDrawElements(mode, count, type, indices)

cdef void GetglEdgeFlagPointer(GLsizei stride, const void *pointer):
    global cglEdgeFlagPointer
    cglEdgeFlagPointer = <PFNGLEDGEFLAGPOINTERPROC>getFunction(b"glEdgeFlagPointer")
    cglEdgeFlagPointer(stride, pointer)

cdef void GetglEnableClientState(GLenum array):
    global cglEnableClientState
    cglEnableClientState = <PFNGLENABLECLIENTSTATEPROC>getFunction(b"glEnableClientState")
    cglEnableClientState(array)

cdef void GetglGenTextures(GLsizei n, GLuint *textures):
    global cglGenTextures
    cglGenTextures = <PFNGLGENTEXTURESPROC>getFunction(b"glGenTextures")
    cglGenTextures(n, textures)

cdef void GetglGetPointerv(GLenum pname, void **params):
    global cglGetPointerv
    cglGetPointerv = <PFNGLGETPOINTERVPROC>getFunction(b"glGetPointerv")
    cglGetPointerv(pname, params)

cdef void GetglIndexPointer(GLenum type, GLsizei stride, const void *pointer):
    global cglIndexPointer
    cglIndexPointer = <PFNGLINDEXPOINTERPROC>getFunction(b"glIndexPointer")
    cglIndexPointer(type, stride, pointer)

cdef void GetglIndexub(GLubyte c):
    global cglIndexub
    cglIndexub = <PFNGLINDEXUBPROC>getFunction(b"glIndexub")
    cglIndexub(c)

cdef void GetglIndexubv(const GLubyte *c):
    global cglIndexubv
    cglIndexubv = <PFNGLINDEXUBVPROC>getFunction(b"glIndexubv")
    cglIndexubv(c)

cdef void GetglInterleavedArrays(GLenum format, GLsizei stride, const void *pointer):
    global cglInterleavedArrays
    cglInterleavedArrays = <PFNGLINTERLEAVEDARRAYSPROC>getFunction(b"glInterleavedArrays")
    cglInterleavedArrays(format, stride, pointer)

cdef GLboolean GetglIsTexture(GLuint texture):
    global cglIsTexture
    cglIsTexture = <PFNGLISTEXTUREPROC>getFunction(b"glIsTexture")
    cglIsTexture(texture)

cdef void GetglNormalPointer(GLenum type, GLsizei stride, const void *pointer):
    global cglNormalPointer
    cglNormalPointer = <PFNGLNORMALPOINTERPROC>getFunction(b"glNormalPointer")
    cglNormalPointer(type, stride, pointer)

cdef void GetglPolygonOffset(GLfloat factor, GLfloat units):
    global cglPolygonOffset
    cglPolygonOffset = <PFNGLPOLYGONOFFSETPROC>getFunction(b"glPolygonOffset")
    cglPolygonOffset(factor, units)

cdef void GetglPopClientAttrib():
    global cglPopClientAttrib
    cglPopClientAttrib = <PFNGLPOPCLIENTATTRIBPROC>getFunction(b"glPopClientAttrib")
    cglPopClientAttrib()

cdef void GetglPrioritizeTextures(GLsizei n, const GLuint *textures, const GLfloat *priorities):
    global cglPrioritizeTextures
    cglPrioritizeTextures = <PFNGLPRIORITIZETEXTURESPROC>getFunction(b"glPrioritizeTextures")
    cglPrioritizeTextures(n, textures, priorities)

cdef void GetglPushClientAttrib(GLbitfield mask):
    global cglPushClientAttrib
    cglPushClientAttrib = <PFNGLPUSHCLIENTATTRIBPROC>getFunction(b"glPushClientAttrib")
    cglPushClientAttrib(mask)

cdef void GetglTexCoordPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglTexCoordPointer
    cglTexCoordPointer = <PFNGLTEXCOORDPOINTERPROC>getFunction(b"glTexCoordPointer")
    cglTexCoordPointer(size, type, stride, pointer)

cdef void GetglTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels):
    global cglTexSubImage1D
    cglTexSubImage1D = <PFNGLTEXSUBIMAGE1DPROC>getFunction(b"glTexSubImage1D")
    cglTexSubImage1D(target, level, xoffset, width, format, type, pixels)

cdef void GetglTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    global cglTexSubImage2D
    cglTexSubImage2D = <PFNGLTEXSUBIMAGE2DPROC>getFunction(b"glTexSubImage2D")
    cglTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)

cdef void GetglVertexPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglVertexPointer
    cglVertexPointer = <PFNGLVERTEXPOINTERPROC>getFunction(b"glVertexPointer")
    cglVertexPointer(size, type, stride, pointer)

cglAreTexturesResident = GetglAreTexturesResident
cglArrayElement = GetglArrayElement
cglBindTexture = GetglBindTexture
cglColorPointer = GetglColorPointer
cglCopyTexImage1D = GetglCopyTexImage1D
cglCopyTexImage2D = GetglCopyTexImage2D
cglCopyTexSubImage1D = GetglCopyTexSubImage1D
cglCopyTexSubImage2D = GetglCopyTexSubImage2D
cglDeleteTextures = GetglDeleteTextures
cglDisableClientState = GetglDisableClientState
cglDrawArrays = GetglDrawArrays
cglDrawElements = GetglDrawElements
cglEdgeFlagPointer = GetglEdgeFlagPointer
cglEnableClientState = GetglEnableClientState
cglGenTextures = GetglGenTextures
cglGetPointerv = GetglGetPointerv
cglIndexPointer = GetglIndexPointer
cglIndexub = GetglIndexub
cglIndexubv = GetglIndexubv
cglInterleavedArrays = GetglInterleavedArrays
cglIsTexture = GetglIsTexture
cglNormalPointer = GetglNormalPointer
cglPolygonOffset = GetglPolygonOffset
cglPopClientAttrib = GetglPopClientAttrib
cglPrioritizeTextures = GetglPrioritizeTextures
cglPushClientAttrib = GetglPushClientAttrib
cglTexCoordPointer = GetglTexCoordPointer
cglTexSubImage1D = GetglTexSubImage1D
cglTexSubImage2D = GetglTexSubImage2D
cglVertexPointer = GetglVertexPointer


cdef GLboolean glAreTexturesResident(GLsizei n, const GLuint *textures, GLboolean *residences):
    cglAreTexturesResident(n, textures, residences)

cdef void glArrayElement(GLint i):
    cglArrayElement(i)

cdef void glBindTexture(GLenum target, GLuint texture):
    cglBindTexture(target, texture)

cdef void glColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglColorPointer(size, type, stride, pointer)

cdef void glCopyTexImage1D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border):
    cglCopyTexImage1D(target, level, internalformat, x, y, width, border)

cdef void glCopyTexImage2D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border):
    cglCopyTexImage2D(target, level, internalformat, x, y, width, height, border)

cdef void glCopyTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width):
    cglCopyTexSubImage1D(target, level, xoffset, x, y, width)

cdef void glCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    cglCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)

cdef void glDeleteTextures(GLsizei n, const GLuint *textures):
    cglDeleteTextures(n, textures)

cdef void glDisableClientState(GLenum array):
    cglDisableClientState(array)

cdef void glDrawArrays(GLenum mode, GLint first, GLsizei count):
    cglDrawArrays(mode, first, count)

cdef void glDrawElements(GLenum mode, GLsizei count, GLenum type, const void *indices):
    cglDrawElements(mode, count, type, indices)

cdef void glEdgeFlagPointer(GLsizei stride, const void *pointer):
    cglEdgeFlagPointer(stride, pointer)

cdef void glEnableClientState(GLenum array):
    cglEnableClientState(array)

cdef void glGenTextures(GLsizei n, GLuint *textures):
    cglGenTextures(n, textures)

cdef void glGetPointerv(GLenum pname, void **params):
    cglGetPointerv(pname, params)

cdef void glIndexPointer(GLenum type, GLsizei stride, const void *pointer):
    cglIndexPointer(type, stride, pointer)

cdef void glIndexub(GLubyte c):
    cglIndexub(c)

cdef void glIndexubv(const GLubyte *c):
    cglIndexubv(c)

cdef void glInterleavedArrays(GLenum format, GLsizei stride, const void *pointer):
    cglInterleavedArrays(format, stride, pointer)

cdef GLboolean glIsTexture(GLuint texture):
    cglIsTexture(texture)

cdef void glNormalPointer(GLenum type, GLsizei stride, const void *pointer):
    cglNormalPointer(type, stride, pointer)

cdef void glPolygonOffset(GLfloat factor, GLfloat units):
    cglPolygonOffset(factor, units)

cdef void glPopClientAttrib():
    cglPopClientAttrib()

cdef void glPrioritizeTextures(GLsizei n, const GLuint *textures, const GLfloat *priorities):
    cglPrioritizeTextures(n, textures, priorities)

cdef void glPushClientAttrib(GLbitfield mask):
    cglPushClientAttrib(mask)

cdef void glTexCoordPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglTexCoordPointer(size, type, stride, pointer)

cdef void glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels):
    cglTexSubImage1D(target, level, xoffset, width, format, type, pixels)

cdef void glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    cglTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)

cdef void glVertexPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglVertexPointer(size, type, stride, pointer)
