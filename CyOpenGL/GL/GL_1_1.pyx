# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_COLOR_LOGIC_OP = 0x0BF2
cdef GLenum GL_POLYGON_OFFSET_UNITS = 0x2A00
cdef GLenum GL_POLYGON_OFFSET_POINT = 0x2A01
cdef GLenum GL_POLYGON_OFFSET_LINE = 0x2A02
cdef GLenum GL_POLYGON_OFFSET_FILL = 0x8037
cdef GLenum GL_POLYGON_OFFSET_FACTOR = 0x8038
cdef GLenum GL_TEXTURE_BINDING_1D = 0x8068
cdef GLenum GL_TEXTURE_BINDING_2D = 0x8069
cdef GLenum GL_TEXTURE_INTERNAL_FORMAT = 0x1003
cdef GLenum GL_TEXTURE_RED_SIZE = 0x805C
cdef GLenum GL_TEXTURE_GREEN_SIZE = 0x805D
cdef GLenum GL_TEXTURE_BLUE_SIZE = 0x805E
cdef GLenum GL_TEXTURE_ALPHA_SIZE = 0x805F
cdef GLenum GL_DOUBLE = 0x140A
cdef GLenum GL_PROXY_TEXTURE_1D = 0x8063
cdef GLenum GL_PROXY_TEXTURE_2D = 0x8064
cdef GLenum GL_R3_G3_B2 = 0x2A10
cdef GLenum GL_RGB4 = 0x804F
cdef GLenum GL_RGB5 = 0x8050
cdef GLenum GL_RGB8 = 0x8051
cdef GLenum GL_RGB10 = 0x8052
cdef GLenum GL_RGB12 = 0x8053
cdef GLenum GL_RGB16 = 0x8054
cdef GLenum GL_RGBA2 = 0x8055
cdef GLenum GL_RGBA4 = 0x8056
cdef GLenum GL_RGB5_A1 = 0x8057
cdef GLenum GL_RGBA8 = 0x8058
cdef GLenum GL_RGB10_A2 = 0x8059
cdef GLenum GL_RGBA12 = 0x805A
cdef GLenum GL_RGBA16 = 0x805B
cdef GLenum GL_CLIENT_PIXEL_STORE_BIT = 0x00000001
cdef GLenum GL_CLIENT_VERTEX_ARRAY_BIT = 0x00000002
cdef GLenum GL_CLIENT_ALL_ATTRIB_BITS = 0xFFFFFFFF
cdef GLenum GL_VERTEX_ARRAY_POINTER = 0x808E
cdef GLenum GL_NORMAL_ARRAY_POINTER = 0x808F
cdef GLenum GL_COLOR_ARRAY_POINTER = 0x8090
cdef GLenum GL_INDEX_ARRAY_POINTER = 0x8091
cdef GLenum GL_TEXTURE_COORD_ARRAY_POINTER = 0x8092
cdef GLenum GL_EDGE_FLAG_ARRAY_POINTER = 0x8093
cdef GLenum GL_FEEDBACK_BUFFER_POINTER = 0x0DF0
cdef GLenum GL_SELECTION_BUFFER_POINTER = 0x0DF3
cdef GLenum GL_CLIENT_ATTRIB_STACK_DEPTH = 0x0BB1
cdef GLenum GL_INDEX_LOGIC_OP = 0x0BF1
cdef GLenum GL_MAX_CLIENT_ATTRIB_STACK_DEPTH = 0x0D3B
cdef GLenum GL_FEEDBACK_BUFFER_SIZE = 0x0DF1
cdef GLenum GL_FEEDBACK_BUFFER_TYPE = 0x0DF2
cdef GLenum GL_SELECTION_BUFFER_SIZE = 0x0DF4
cdef GLenum GL_VERTEX_ARRAY = 0x8074
cdef GLenum GL_NORMAL_ARRAY = 0x8075
cdef GLenum GL_COLOR_ARRAY = 0x8076
cdef GLenum GL_INDEX_ARRAY = 0x8077
cdef GLenum GL_TEXTURE_COORD_ARRAY = 0x8078
cdef GLenum GL_EDGE_FLAG_ARRAY = 0x8079
cdef GLenum GL_VERTEX_ARRAY_SIZE = 0x807A
cdef GLenum GL_VERTEX_ARRAY_TYPE = 0x807B
cdef GLenum GL_VERTEX_ARRAY_STRIDE = 0x807C
cdef GLenum GL_NORMAL_ARRAY_TYPE = 0x807E
cdef GLenum GL_NORMAL_ARRAY_STRIDE = 0x807F
cdef GLenum GL_COLOR_ARRAY_SIZE = 0x8081
cdef GLenum GL_COLOR_ARRAY_TYPE = 0x8082
cdef GLenum GL_COLOR_ARRAY_STRIDE = 0x8083
cdef GLenum GL_INDEX_ARRAY_TYPE = 0x8085
cdef GLenum GL_INDEX_ARRAY_STRIDE = 0x8086
cdef GLenum GL_TEXTURE_COORD_ARRAY_SIZE = 0x8088
cdef GLenum GL_TEXTURE_COORD_ARRAY_TYPE = 0x8089
cdef GLenum GL_TEXTURE_COORD_ARRAY_STRIDE = 0x808A
cdef GLenum GL_EDGE_FLAG_ARRAY_STRIDE = 0x808C
cdef GLenum GL_TEXTURE_LUMINANCE_SIZE = 0x8060
cdef GLenum GL_TEXTURE_INTENSITY_SIZE = 0x8061
cdef GLenum GL_TEXTURE_PRIORITY = 0x8066
cdef GLenum GL_TEXTURE_RESIDENT = 0x8067
cdef GLenum GL_ALPHA4 = 0x803B
cdef GLenum GL_ALPHA8 = 0x803C
cdef GLenum GL_ALPHA12 = 0x803D
cdef GLenum GL_ALPHA16 = 0x803E
cdef GLenum GL_LUMINANCE4 = 0x803F
cdef GLenum GL_LUMINANCE8 = 0x8040
cdef GLenum GL_LUMINANCE12 = 0x8041
cdef GLenum GL_LUMINANCE16 = 0x8042
cdef GLenum GL_LUMINANCE4_ALPHA4 = 0x8043
cdef GLenum GL_LUMINANCE6_ALPHA2 = 0x8044
cdef GLenum GL_LUMINANCE8_ALPHA8 = 0x8045
cdef GLenum GL_LUMINANCE12_ALPHA4 = 0x8046
cdef GLenum GL_LUMINANCE12_ALPHA12 = 0x8047
cdef GLenum GL_LUMINANCE16_ALPHA16 = 0x8048
cdef GLenum GL_INTENSITY = 0x8049
cdef GLenum GL_INTENSITY4 = 0x804A
cdef GLenum GL_INTENSITY8 = 0x804B
cdef GLenum GL_INTENSITY12 = 0x804C
cdef GLenum GL_INTENSITY16 = 0x804D
cdef GLenum GL_V2F = 0x2A20
cdef GLenum GL_V3F = 0x2A21
cdef GLenum GL_C4UB_V2F = 0x2A22
cdef GLenum GL_C4UB_V3F = 0x2A23
cdef GLenum GL_C3F_V3F = 0x2A24
cdef GLenum GL_N3F_V3F = 0x2A25
cdef GLenum GL_C4F_N3F_V3F = 0x2A26
cdef GLenum GL_T2F_V3F = 0x2A27
cdef GLenum GL_T4F_V4F = 0x2A28
cdef GLenum GL_T2F_C4UB_V3F = 0x2A29
cdef GLenum GL_T2F_C3F_V3F = 0x2A2A
cdef GLenum GL_T2F_N3F_V3F = 0x2A2B
cdef GLenum GL_T2F_C4F_N3F_V3F = 0x2A2C
cdef GLenum GL_T4F_C4F_N3F_V4F = 0x2A2D

ctypedef void (*GL_DRAW_ARRAYS)(GLenum mode, GLint first, GLsizei count)
ctypedef void (*GL_DRAW_ELEMENTS)(GLenum mode, GLsizei count, GLenum type, const void *indices)
ctypedef void (*GL_GET_POINTERV)(GLenum pname, void **params)
ctypedef void (*GL_POLYGON_OFFSET)(GLfloat factor, GLfloat units)
ctypedef void (*GL_COPY_TEX_IMAGE1D)(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
ctypedef void (*GL_COPY_TEX_IMAGE2D)(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border)
ctypedef void (*GL_COPY_TEX_SUB_IMAGE1D)(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
ctypedef void (*GL_COPY_TEX_SUB_IMAGE2D)(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*GL_TEX_SUB_IMAGE1D)(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels)
ctypedef void (*GL_TEX_SUB_IMAGE2D)(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
ctypedef void (*GL_BIND_TEXTURE)(GLenum target, GLuint texture)
ctypedef void (*GL_DELETE_TEXTURES)(GLsizei n, const GLuint *textures)
ctypedef void (*GL_GEN_TEXTURES)(GLsizei n, GLuint *textures)
ctypedef GLboolean (*GL_IS_TEXTURE)(GLuint texture)
ctypedef void (*GL_ARRAY_ELEMENT)(GLint i)
ctypedef void (*GL_COLOR_POINTER)(GLint size, GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*GL_DISABLE_CLIENT_STATE)(GLenum array)
ctypedef void (*GL_EDGE_FLAG_POINTER)(GLsizei stride, const void *pointer)
ctypedef void (*GL_ENABLE_CLIENT_STATE)(GLenum array)
ctypedef void (*GL_INDEX_POINTER)(GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*GL_INTERLEAVED_ARRAYS)(GLenum format, GLsizei stride, const void *pointer)
ctypedef void (*GL_NORMAL_POINTER)(GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*GL_TEX_COORD_POINTER)(GLint size, GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*GL_VERTEX_POINTER)(GLint size, GLenum type, GLsizei stride, const void *pointer)
ctypedef GLboolean (*GL_ARE_TEXTURES_RESIDENT)(GLsizei n, const GLuint *textures, GLboolean *residences)
ctypedef void (*GL_PRIORITIZE_TEXTURES)(GLsizei n, const GLuint *textures, const GLfloat *priorities)
ctypedef void (*GL_INDEXUB)(GLubyte c)
ctypedef void (*GL_INDEXUBV)(const GLubyte *c)
ctypedef void (*GL_POP_CLIENT_ATTRIB)()
ctypedef void (*GL_PUSH_CLIENT_ATTRIB)(GLbitfield mask)

cdef GL_DRAW_ARRAYS cglDrawArrays = NULL
cdef GL_DRAW_ELEMENTS cglDrawElements = NULL
cdef GL_GET_POINTERV cglGetPointerv = NULL
cdef GL_POLYGON_OFFSET cglPolygonOffset = NULL
cdef GL_COPY_TEX_IMAGE1D cglCopyTexImage1D = NULL
cdef GL_COPY_TEX_IMAGE2D cglCopyTexImage2D = NULL
cdef GL_COPY_TEX_SUB_IMAGE1D cglCopyTexSubImage1D = NULL
cdef GL_COPY_TEX_SUB_IMAGE2D cglCopyTexSubImage2D = NULL
cdef GL_TEX_SUB_IMAGE1D cglTexSubImage1D = NULL
cdef GL_TEX_SUB_IMAGE2D cglTexSubImage2D = NULL
cdef GL_BIND_TEXTURE cglBindTexture = NULL
cdef GL_DELETE_TEXTURES cglDeleteTextures = NULL
cdef GL_GEN_TEXTURES cglGenTextures = NULL
cdef GL_IS_TEXTURE cglIsTexture = NULL
cdef GL_ARRAY_ELEMENT cglArrayElement = NULL
cdef GL_COLOR_POINTER cglColorPointer = NULL
cdef GL_DISABLE_CLIENT_STATE cglDisableClientState = NULL
cdef GL_EDGE_FLAG_POINTER cglEdgeFlagPointer = NULL
cdef GL_ENABLE_CLIENT_STATE cglEnableClientState = NULL
cdef GL_INDEX_POINTER cglIndexPointer = NULL
cdef GL_INTERLEAVED_ARRAYS cglInterleavedArrays = NULL
cdef GL_NORMAL_POINTER cglNormalPointer = NULL
cdef GL_TEX_COORD_POINTER cglTexCoordPointer = NULL
cdef GL_VERTEX_POINTER cglVertexPointer = NULL
cdef GL_ARE_TEXTURES_RESIDENT cglAreTexturesResident = NULL
cdef GL_PRIORITIZE_TEXTURES cglPrioritizeTextures = NULL
cdef GL_INDEXUB cglIndexub = NULL
cdef GL_INDEXUBV cglIndexubv = NULL
cdef GL_POP_CLIENT_ATTRIB cglPopClientAttrib = NULL
cdef GL_PUSH_CLIENT_ATTRIB cglPushClientAttrib = NULL


cdef void GetglDrawArrays(GLenum mode, GLint first, GLsizei count):
    global cglDrawArrays
    cglDrawArrays = <GL_DRAW_ARRAYS>getFunction(b"glDrawArrays")
    cglDrawArrays(mode, first, count)

cdef void GetglDrawElements(GLenum mode, GLsizei count, GLenum type, const void *indices):
    global cglDrawElements
    cglDrawElements = <GL_DRAW_ELEMENTS>getFunction(b"glDrawElements")
    cglDrawElements(mode, count, type, indices)

cdef void GetglGetPointerv(GLenum pname, void **params):
    global cglGetPointerv
    cglGetPointerv = <GL_GET_POINTERV>getFunction(b"glGetPointerv")
    cglGetPointerv(pname, params)

cdef void GetglPolygonOffset(GLfloat factor, GLfloat units):
    global cglPolygonOffset
    cglPolygonOffset = <GL_POLYGON_OFFSET>getFunction(b"glPolygonOffset")
    cglPolygonOffset(factor, units)

cdef void GetglCopyTexImage1D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border):
    global cglCopyTexImage1D
    cglCopyTexImage1D = <GL_COPY_TEX_IMAGE1D>getFunction(b"glCopyTexImage1D")
    cglCopyTexImage1D(target, level, internalformat, x, y, width, border)

cdef void GetglCopyTexImage2D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border):
    global cglCopyTexImage2D
    cglCopyTexImage2D = <GL_COPY_TEX_IMAGE2D>getFunction(b"glCopyTexImage2D")
    cglCopyTexImage2D(target, level, internalformat, x, y, width, height, border)

cdef void GetglCopyTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width):
    global cglCopyTexSubImage1D
    cglCopyTexSubImage1D = <GL_COPY_TEX_SUB_IMAGE1D>getFunction(b"glCopyTexSubImage1D")
    cglCopyTexSubImage1D(target, level, xoffset, x, y, width)

cdef void GetglCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglCopyTexSubImage2D
    cglCopyTexSubImage2D = <GL_COPY_TEX_SUB_IMAGE2D>getFunction(b"glCopyTexSubImage2D")
    cglCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)

cdef void GetglTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels):
    global cglTexSubImage1D
    cglTexSubImage1D = <GL_TEX_SUB_IMAGE1D>getFunction(b"glTexSubImage1D")
    cglTexSubImage1D(target, level, xoffset, width, format, type, pixels)

cdef void GetglTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    global cglTexSubImage2D
    cglTexSubImage2D = <GL_TEX_SUB_IMAGE2D>getFunction(b"glTexSubImage2D")
    cglTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)

cdef void GetglBindTexture(GLenum target, GLuint texture):
    global cglBindTexture
    cglBindTexture = <GL_BIND_TEXTURE>getFunction(b"glBindTexture")
    cglBindTexture(target, texture)

cdef void GetglDeleteTextures(GLsizei n, const GLuint *textures):
    global cglDeleteTextures
    cglDeleteTextures = <GL_DELETE_TEXTURES>getFunction(b"glDeleteTextures")
    cglDeleteTextures(n, textures)

cdef void GetglGenTextures(GLsizei n, GLuint *textures):
    global cglGenTextures
    cglGenTextures = <GL_GEN_TEXTURES>getFunction(b"glGenTextures")
    cglGenTextures(n, textures)

cdef GLboolean GetglIsTexture(GLuint texture):
    global cglIsTexture
    cglIsTexture = <GL_IS_TEXTURE>getFunction(b"glIsTexture")
    cglIsTexture(texture)

cdef void GetglArrayElement(GLint i):
    global cglArrayElement
    cglArrayElement = <GL_ARRAY_ELEMENT>getFunction(b"glArrayElement")
    cglArrayElement(i)

cdef void GetglColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglColorPointer
    cglColorPointer = <GL_COLOR_POINTER>getFunction(b"glColorPointer")
    cglColorPointer(size, type, stride, pointer)

cdef void GetglDisableClientState(GLenum array):
    global cglDisableClientState
    cglDisableClientState = <GL_DISABLE_CLIENT_STATE>getFunction(b"glDisableClientState")
    cglDisableClientState(array)

cdef void GetglEdgeFlagPointer(GLsizei stride, const void *pointer):
    global cglEdgeFlagPointer
    cglEdgeFlagPointer = <GL_EDGE_FLAG_POINTER>getFunction(b"glEdgeFlagPointer")
    cglEdgeFlagPointer(stride, pointer)

cdef void GetglEnableClientState(GLenum array):
    global cglEnableClientState
    cglEnableClientState = <GL_ENABLE_CLIENT_STATE>getFunction(b"glEnableClientState")
    cglEnableClientState(array)

cdef void GetglIndexPointer(GLenum type, GLsizei stride, const void *pointer):
    global cglIndexPointer
    cglIndexPointer = <GL_INDEX_POINTER>getFunction(b"glIndexPointer")
    cglIndexPointer(type, stride, pointer)

cdef void GetglInterleavedArrays(GLenum format, GLsizei stride, const void *pointer):
    global cglInterleavedArrays
    cglInterleavedArrays = <GL_INTERLEAVED_ARRAYS>getFunction(b"glInterleavedArrays")
    cglInterleavedArrays(format, stride, pointer)

cdef void GetglNormalPointer(GLenum type, GLsizei stride, const void *pointer):
    global cglNormalPointer
    cglNormalPointer = <GL_NORMAL_POINTER>getFunction(b"glNormalPointer")
    cglNormalPointer(type, stride, pointer)

cdef void GetglTexCoordPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglTexCoordPointer
    cglTexCoordPointer = <GL_TEX_COORD_POINTER>getFunction(b"glTexCoordPointer")
    cglTexCoordPointer(size, type, stride, pointer)

cdef void GetglVertexPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglVertexPointer
    cglVertexPointer = <GL_VERTEX_POINTER>getFunction(b"glVertexPointer")
    cglVertexPointer(size, type, stride, pointer)

cdef GLboolean GetglAreTexturesResident(GLsizei n, const GLuint *textures, GLboolean *residences):
    global cglAreTexturesResident
    cglAreTexturesResident = <GL_ARE_TEXTURES_RESIDENT>getFunction(b"glAreTexturesResident")
    cglAreTexturesResident(n, textures, residences)

cdef void GetglPrioritizeTextures(GLsizei n, const GLuint *textures, const GLfloat *priorities):
    global cglPrioritizeTextures
    cglPrioritizeTextures = <GL_PRIORITIZE_TEXTURES>getFunction(b"glPrioritizeTextures")
    cglPrioritizeTextures(n, textures, priorities)

cdef void GetglIndexub(GLubyte c):
    global cglIndexub
    cglIndexub = <GL_INDEXUB>getFunction(b"glIndexub")
    cglIndexub(c)

cdef void GetglIndexubv(const GLubyte *c):
    global cglIndexubv
    cglIndexubv = <GL_INDEXUBV>getFunction(b"glIndexubv")
    cglIndexubv(c)

cdef void GetglPopClientAttrib():
    global cglPopClientAttrib
    cglPopClientAttrib = <GL_POP_CLIENT_ATTRIB>getFunction(b"glPopClientAttrib")
    cglPopClientAttrib()

cdef void GetglPushClientAttrib(GLbitfield mask):
    global cglPushClientAttrib
    cglPushClientAttrib = <GL_PUSH_CLIENT_ATTRIB>getFunction(b"glPushClientAttrib")
    cglPushClientAttrib(mask)

cglDrawArrays = GetglDrawArrays
cglDrawElements = GetglDrawElements
cglGetPointerv = GetglGetPointerv
cglPolygonOffset = GetglPolygonOffset
cglCopyTexImage1D = GetglCopyTexImage1D
cglCopyTexImage2D = GetglCopyTexImage2D
cglCopyTexSubImage1D = GetglCopyTexSubImage1D
cglCopyTexSubImage2D = GetglCopyTexSubImage2D
cglTexSubImage1D = GetglTexSubImage1D
cglTexSubImage2D = GetglTexSubImage2D
cglBindTexture = GetglBindTexture
cglDeleteTextures = GetglDeleteTextures
cglGenTextures = GetglGenTextures
cglIsTexture = GetglIsTexture
cglArrayElement = GetglArrayElement
cglColorPointer = GetglColorPointer
cglDisableClientState = GetglDisableClientState
cglEdgeFlagPointer = GetglEdgeFlagPointer
cglEnableClientState = GetglEnableClientState
cglIndexPointer = GetglIndexPointer
cglInterleavedArrays = GetglInterleavedArrays
cglNormalPointer = GetglNormalPointer
cglTexCoordPointer = GetglTexCoordPointer
cglVertexPointer = GetglVertexPointer
cglAreTexturesResident = GetglAreTexturesResident
cglPrioritizeTextures = GetglPrioritizeTextures
cglIndexub = GetglIndexub
cglIndexubv = GetglIndexubv
cglPopClientAttrib = GetglPopClientAttrib
cglPushClientAttrib = GetglPushClientAttrib


cpdef void glDrawArrays(GLenum mode, GLint first, GLsizei count):
    cglDrawArrays(mode, first, count)

cpdef void glDrawElements(GLenum mode, GLsizei count, GLenum type, const void *indices):
    cglDrawElements(mode, count, type, indices)

cpdef void glGetPointerv(GLenum pname, void **params):
    cglGetPointerv(pname, params)

cpdef void glPolygonOffset(GLfloat factor, GLfloat units):
    cglPolygonOffset(factor, units)

cpdef void glCopyTexImage1D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border):
    cglCopyTexImage1D(target, level, internalformat, x, y, width, border)

cpdef void glCopyTexImage2D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border):
    cglCopyTexImage2D(target, level, internalformat, x, y, width, height, border)

cpdef void glCopyTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width):
    cglCopyTexSubImage1D(target, level, xoffset, x, y, width)

cpdef void glCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    cglCopyTexSubImage2D(target, level, xoffset, yoffset, x, y, width, height)

cpdef void glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels):
    cglTexSubImage1D(target, level, xoffset, width, format, type, pixels)

cpdef void glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    cglTexSubImage2D(target, level, xoffset, yoffset, width, height, format, type, pixels)

cpdef void glBindTexture(GLenum target, GLuint texture):
    cglBindTexture(target, texture)

cpdef void glDeleteTextures(GLsizei n, const GLuint *textures):
    cglDeleteTextures(n, textures)

cpdef void glGenTextures(GLsizei n, GLuint *textures):
    cglGenTextures(n, textures)

cpdef GLboolean glIsTexture(GLuint texture):
    cglIsTexture(texture)

cpdef void glArrayElement(GLint i):
    cglArrayElement(i)

cpdef void glColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglColorPointer(size, type, stride, pointer)

cpdef void glDisableClientState(GLenum array):
    cglDisableClientState(array)

cpdef void glEdgeFlagPointer(GLsizei stride, const void *pointer):
    cglEdgeFlagPointer(stride, pointer)

cpdef void glEnableClientState(GLenum array):
    cglEnableClientState(array)

cpdef void glIndexPointer(GLenum type, GLsizei stride, const void *pointer):
    cglIndexPointer(type, stride, pointer)

cpdef void glInterleavedArrays(GLenum format, GLsizei stride, const void *pointer):
    cglInterleavedArrays(format, stride, pointer)

cpdef void glNormalPointer(GLenum type, GLsizei stride, const void *pointer):
    cglNormalPointer(type, stride, pointer)

cpdef void glTexCoordPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglTexCoordPointer(size, type, stride, pointer)

cpdef void glVertexPointer(GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglVertexPointer(size, type, stride, pointer)

cpdef GLboolean glAreTexturesResident(GLsizei n, const GLuint *textures, GLboolean *residences):
    cglAreTexturesResident(n, textures, residences)

cpdef void glPrioritizeTextures(GLsizei n, const GLuint *textures, const GLfloat *priorities):
    cglPrioritizeTextures(n, textures, priorities)

cpdef void glIndexub(GLubyte c):
    cglIndexub(c)

cpdef void glIndexubv(const GLubyte *c):
    cglIndexubv(c)

cpdef void glPopClientAttrib():
    cglPopClientAttrib()

cpdef void glPushClientAttrib(GLbitfield mask):
    cglPushClientAttrib(mask)
