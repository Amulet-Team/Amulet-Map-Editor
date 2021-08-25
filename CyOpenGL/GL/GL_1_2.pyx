# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_ALIASED_LINE_WIDTH_RANGE = 0x846E
cdef GLenum GL_ALIASED_POINT_SIZE_RANGE = 0x846D
cdef GLenum GL_BGR = 0x80E0
cdef GLenum GL_BGRA = 0x80E1
cdef GLenum GL_CLAMP_TO_EDGE = 0x812F
cdef GLenum GL_LIGHT_MODEL_COLOR_CONTROL = 0x81F8
cdef GLenum GL_MAX_3D_TEXTURE_SIZE = 0x8073
cdef GLenum GL_MAX_ELEMENTS_INDICES = 0x80E9
cdef GLenum GL_MAX_ELEMENTS_VERTICES = 0x80E8
cdef GLenum GL_PACK_IMAGE_HEIGHT = 0x806C
cdef GLenum GL_PACK_SKIP_IMAGES = 0x806B
cdef GLenum GL_PROXY_TEXTURE_3D = 0x8070
cdef GLenum GL_RESCALE_NORMAL = 0x803A
cdef GLenum GL_SEPARATE_SPECULAR_COLOR = 0x81FA
cdef GLenum GL_SINGLE_COLOR = 0x81F9
cdef GLenum GL_SMOOTH_LINE_WIDTH_GRANULARITY = 0x0B23
cdef GLenum GL_SMOOTH_LINE_WIDTH_RANGE = 0x0B22
cdef GLenum GL_SMOOTH_POINT_SIZE_GRANULARITY = 0x0B13
cdef GLenum GL_SMOOTH_POINT_SIZE_RANGE = 0x0B12
cdef GLenum GL_TEXTURE_3D = 0x806F
cdef GLenum GL_TEXTURE_BASE_LEVEL = 0x813C
cdef GLenum GL_TEXTURE_BINDING_3D = 0x806A
cdef GLenum GL_TEXTURE_DEPTH = 0x8071
cdef GLenum GL_TEXTURE_MAX_LEVEL = 0x813D
cdef GLenum GL_TEXTURE_MAX_LOD = 0x813B
cdef GLenum GL_TEXTURE_MIN_LOD = 0x813A
cdef GLenum GL_TEXTURE_WRAP_R = 0x8072
cdef GLenum GL_UNPACK_IMAGE_HEIGHT = 0x806E
cdef GLenum GL_UNPACK_SKIP_IMAGES = 0x806D
cdef GLenum GL_UNSIGNED_BYTE_2_3_3_REV = 0x8362
cdef GLenum GL_UNSIGNED_BYTE_3_3_2 = 0x8032
cdef GLenum GL_UNSIGNED_INT_10_10_10_2 = 0x8036
cdef GLenum GL_UNSIGNED_INT_2_10_10_10_REV = 0x8368
cdef GLenum GL_UNSIGNED_INT_8_8_8_8 = 0x8035
cdef GLenum GL_UNSIGNED_INT_8_8_8_8_REV = 0x8367
cdef GLenum GL_UNSIGNED_SHORT_1_5_5_5_REV = 0x8366
cdef GLenum GL_UNSIGNED_SHORT_4_4_4_4 = 0x8033
cdef GLenum GL_UNSIGNED_SHORT_4_4_4_4_REV = 0x8365
cdef GLenum GL_UNSIGNED_SHORT_5_5_5_1 = 0x8034
cdef GLenum GL_UNSIGNED_SHORT_5_6_5 = 0x8363
cdef GLenum GL_UNSIGNED_SHORT_5_6_5_REV = 0x8364

ctypedef void (*PFNGLCOPYTEXSUBIMAGE3DPROC)(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*PFNGLDRAWRANGEELEMENTSPROC)(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices)
ctypedef void (*PFNGLTEXIMAGE3DPROC)(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const void *pixels)
ctypedef void (*PFNGLTEXSUBIMAGE3DPROC)(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels)

cdef PFNGLCOPYTEXSUBIMAGE3DPROC cglCopyTexSubImage3D = NULL
cdef PFNGLDRAWRANGEELEMENTSPROC cglDrawRangeElements = NULL
cdef PFNGLTEXIMAGE3DPROC cglTexImage3D = NULL
cdef PFNGLTEXSUBIMAGE3DPROC cglTexSubImage3D = NULL


cdef void GetglCopyTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglCopyTexSubImage3D
    cglCopyTexSubImage3D = <PFNGLCOPYTEXSUBIMAGE3DPROC>getFunction("glCopyTexSubImage3D")
    cglCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height)

cdef void GetglDrawRangeElements(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices):
    global cglDrawRangeElements
    cglDrawRangeElements = <PFNGLDRAWRANGEELEMENTSPROC>getFunction("glDrawRangeElements")
    cglDrawRangeElements(mode, start, end, count, type, indices)

cdef void GetglTexImage3D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const void *pixels):
    global cglTexImage3D
    cglTexImage3D = <PFNGLTEXIMAGE3DPROC>getFunction("glTexImage3D")
    cglTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels)

cdef void GetglTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels):
    global cglTexSubImage3D
    cglTexSubImage3D = <PFNGLTEXSUBIMAGE3DPROC>getFunction("glTexSubImage3D")
    cglTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)

cglCopyTexSubImage3D = GetglCopyTexSubImage3D
cglDrawRangeElements = GetglDrawRangeElements
cglTexImage3D = GetglTexImage3D
cglTexSubImage3D = GetglTexSubImage3D


cdef void glCopyTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    cglCopyTexSubImage3D(target, level, xoffset, yoffset, zoffset, x, y, width, height)

cdef void glDrawRangeElements(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices):
    cglDrawRangeElements(mode, start, end, count, type, indices)

cdef void glTexImage3D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const void *pixels):
    cglTexImage3D(target, level, internalformat, width, height, depth, border, format, type, pixels)

cdef void glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels):
    cglTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)
