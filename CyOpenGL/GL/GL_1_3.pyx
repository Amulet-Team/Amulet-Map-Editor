# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_TEXTURE0 = 0x84C0
cdef GLenum GL_TEXTURE1 = 0x84C1
cdef GLenum GL_TEXTURE2 = 0x84C2
cdef GLenum GL_TEXTURE3 = 0x84C3
cdef GLenum GL_TEXTURE4 = 0x84C4
cdef GLenum GL_TEXTURE5 = 0x84C5
cdef GLenum GL_TEXTURE6 = 0x84C6
cdef GLenum GL_TEXTURE7 = 0x84C7
cdef GLenum GL_TEXTURE8 = 0x84C8
cdef GLenum GL_TEXTURE9 = 0x84C9
cdef GLenum GL_TEXTURE10 = 0x84CA
cdef GLenum GL_TEXTURE11 = 0x84CB
cdef GLenum GL_TEXTURE12 = 0x84CC
cdef GLenum GL_TEXTURE13 = 0x84CD
cdef GLenum GL_TEXTURE14 = 0x84CE
cdef GLenum GL_TEXTURE15 = 0x84CF
cdef GLenum GL_TEXTURE16 = 0x84D0
cdef GLenum GL_TEXTURE17 = 0x84D1
cdef GLenum GL_TEXTURE18 = 0x84D2
cdef GLenum GL_TEXTURE19 = 0x84D3
cdef GLenum GL_TEXTURE20 = 0x84D4
cdef GLenum GL_TEXTURE21 = 0x84D5
cdef GLenum GL_TEXTURE22 = 0x84D6
cdef GLenum GL_TEXTURE23 = 0x84D7
cdef GLenum GL_TEXTURE24 = 0x84D8
cdef GLenum GL_TEXTURE25 = 0x84D9
cdef GLenum GL_TEXTURE26 = 0x84DA
cdef GLenum GL_TEXTURE27 = 0x84DB
cdef GLenum GL_TEXTURE28 = 0x84DC
cdef GLenum GL_TEXTURE29 = 0x84DD
cdef GLenum GL_TEXTURE30 = 0x84DE
cdef GLenum GL_TEXTURE31 = 0x84DF
cdef GLenum GL_ACTIVE_TEXTURE = 0x84E0
cdef GLenum GL_MULTISAMPLE = 0x809D
cdef GLenum GL_SAMPLE_ALPHA_TO_COVERAGE = 0x809E
cdef GLenum GL_SAMPLE_ALPHA_TO_ONE = 0x809F
cdef GLenum GL_SAMPLE_COVERAGE = 0x80A0
cdef GLenum GL_SAMPLE_BUFFERS = 0x80A8
cdef GLenum GL_SAMPLES = 0x80A9
cdef GLenum GL_SAMPLE_COVERAGE_VALUE = 0x80AA
cdef GLenum GL_SAMPLE_COVERAGE_INVERT = 0x80AB
cdef GLenum GL_TEXTURE_CUBE_MAP = 0x8513
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
cdef GLenum GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
cdef GLenum GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
cdef GLenum GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
cdef GLenum GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
cdef GLenum GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
cdef GLenum GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
cdef GLenum GL_PROXY_TEXTURE_CUBE_MAP = 0x851B
cdef GLenum GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
cdef GLenum GL_COMPRESSED_RGB = 0x84ED
cdef GLenum GL_COMPRESSED_RGBA = 0x84EE
cdef GLenum GL_TEXTURE_COMPRESSION_HINT = 0x84EF
cdef GLenum GL_TEXTURE_COMPRESSED_IMAGE_SIZE = 0x86A0
cdef GLenum GL_TEXTURE_COMPRESSED = 0x86A1
cdef GLenum GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x86A2
cdef GLenum GL_COMPRESSED_TEXTURE_FORMATS = 0x86A3
cdef GLenum GL_CLAMP_TO_BORDER = 0x812D
cdef GLenum GL_CLIENT_ACTIVE_TEXTURE = 0x84E1
cdef GLenum GL_MAX_TEXTURE_UNITS = 0x84E2
cdef GLenum GL_TRANSPOSE_MODELVIEW_MATRIX = 0x84E3
cdef GLenum GL_TRANSPOSE_PROJECTION_MATRIX = 0x84E4
cdef GLenum GL_TRANSPOSE_TEXTURE_MATRIX = 0x84E5
cdef GLenum GL_TRANSPOSE_COLOR_MATRIX = 0x84E6
cdef GLenum GL_MULTISAMPLE_BIT = 0x20000000
cdef GLenum GL_NORMAL_MAP = 0x8511
cdef GLenum GL_REFLECTION_MAP = 0x8512
cdef GLenum GL_COMPRESSED_ALPHA = 0x84E9
cdef GLenum GL_COMPRESSED_LUMINANCE = 0x84EA
cdef GLenum GL_COMPRESSED_LUMINANCE_ALPHA = 0x84EB
cdef GLenum GL_COMPRESSED_INTENSITY = 0x84EC
cdef GLenum GL_COMBINE = 0x8570
cdef GLenum GL_COMBINE_RGB = 0x8571
cdef GLenum GL_COMBINE_ALPHA = 0x8572
cdef GLenum GL_SOURCE0_RGB = 0x8580
cdef GLenum GL_SOURCE1_RGB = 0x8581
cdef GLenum GL_SOURCE2_RGB = 0x8582
cdef GLenum GL_SOURCE0_ALPHA = 0x8588
cdef GLenum GL_SOURCE1_ALPHA = 0x8589
cdef GLenum GL_SOURCE2_ALPHA = 0x858A
cdef GLenum GL_OPERAND0_RGB = 0x8590
cdef GLenum GL_OPERAND1_RGB = 0x8591
cdef GLenum GL_OPERAND2_RGB = 0x8592
cdef GLenum GL_OPERAND0_ALPHA = 0x8598
cdef GLenum GL_OPERAND1_ALPHA = 0x8599
cdef GLenum GL_OPERAND2_ALPHA = 0x859A
cdef GLenum GL_RGB_SCALE = 0x8573
cdef GLenum GL_ADD_SIGNED = 0x8574
cdef GLenum GL_INTERPOLATE = 0x8575
cdef GLenum GL_SUBTRACT = 0x84E7
cdef GLenum GL_CONSTANT = 0x8576
cdef GLenum GL_PRIMARY_COLOR = 0x8577
cdef GLenum GL_PREVIOUS = 0x8578
cdef GLenum GL_DOT3_RGB = 0x86AE
cdef GLenum GL_DOT3_RGBA = 0x86AF

ctypedef void (*GL_ACTIVE_TEXTURE)(GLenum texture)
ctypedef void (*GL_SAMPLE_COVERAGE)(GLfloat value, GLboolean invert)
ctypedef void (*GL_COMPRESSED_TEX_IMAGE3D)(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const void *data)
ctypedef void (*GL_COMPRESSED_TEX_IMAGE2D)(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void *data)
ctypedef void (*GL_COMPRESSED_TEX_IMAGE1D)(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei imageSize, const void *data)
ctypedef void (*GL_COMPRESSED_TEX_SUB_IMAGE3D)(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*GL_COMPRESSED_TEX_SUB_IMAGE2D)(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*GL_COMPRESSED_TEX_SUB_IMAGE1D)(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*GL_GET_COMPRESSED_TEX_IMAGE)(GLenum target, GLint level, void *img)
ctypedef void (*GL_CLIENT_ACTIVE_TEXTURE)(GLenum texture)
ctypedef void (*GL_MULTI_TEX_COORD1D)(GLenum target, GLdouble s)
ctypedef void (*GL_MULTI_TEX_COORD1DV)(GLenum target, const GLdouble *v)
ctypedef void (*GL_MULTI_TEX_COORD1F)(GLenum target, GLfloat s)
ctypedef void (*GL_MULTI_TEX_COORD1FV)(GLenum target, const GLfloat *v)
ctypedef void (*GL_MULTI_TEX_COORD1I)(GLenum target, GLint s)
ctypedef void (*GL_MULTI_TEX_COORD1IV)(GLenum target, const GLint *v)
ctypedef void (*GL_MULTI_TEX_COORD1S)(GLenum target, GLshort s)
ctypedef void (*GL_MULTI_TEX_COORD1SV)(GLenum target, const GLshort *v)
ctypedef void (*GL_MULTI_TEX_COORD2D)(GLenum target, GLdouble s, GLdouble t)
ctypedef void (*GL_MULTI_TEX_COORD2DV)(GLenum target, const GLdouble *v)
ctypedef void (*GL_MULTI_TEX_COORD2F)(GLenum target, GLfloat s, GLfloat t)
ctypedef void (*GL_MULTI_TEX_COORD2FV)(GLenum target, const GLfloat *v)
ctypedef void (*GL_MULTI_TEX_COORD2I)(GLenum target, GLint s, GLint t)
ctypedef void (*GL_MULTI_TEX_COORD2IV)(GLenum target, const GLint *v)
ctypedef void (*GL_MULTI_TEX_COORD2S)(GLenum target, GLshort s, GLshort t)
ctypedef void (*GL_MULTI_TEX_COORD2SV)(GLenum target, const GLshort *v)
ctypedef void (*GL_MULTI_TEX_COORD3D)(GLenum target, GLdouble s, GLdouble t, GLdouble r)
ctypedef void (*GL_MULTI_TEX_COORD3DV)(GLenum target, const GLdouble *v)
ctypedef void (*GL_MULTI_TEX_COORD3F)(GLenum target, GLfloat s, GLfloat t, GLfloat r)
ctypedef void (*GL_MULTI_TEX_COORD3FV)(GLenum target, const GLfloat *v)
ctypedef void (*GL_MULTI_TEX_COORD3I)(GLenum target, GLint s, GLint t, GLint r)
ctypedef void (*GL_MULTI_TEX_COORD3IV)(GLenum target, const GLint *v)
ctypedef void (*GL_MULTI_TEX_COORD3S)(GLenum target, GLshort s, GLshort t, GLshort r)
ctypedef void (*GL_MULTI_TEX_COORD3SV)(GLenum target, const GLshort *v)
ctypedef void (*GL_MULTI_TEX_COORD4D)(GLenum target, GLdouble s, GLdouble t, GLdouble r, GLdouble q)
ctypedef void (*GL_MULTI_TEX_COORD4DV)(GLenum target, const GLdouble *v)
ctypedef void (*GL_MULTI_TEX_COORD4F)(GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q)
ctypedef void (*GL_MULTI_TEX_COORD4FV)(GLenum target, const GLfloat *v)
ctypedef void (*GL_MULTI_TEX_COORD4I)(GLenum target, GLint s, GLint t, GLint r, GLint q)
ctypedef void (*GL_MULTI_TEX_COORD4IV)(GLenum target, const GLint *v)
ctypedef void (*GL_MULTI_TEX_COORD4S)(GLenum target, GLshort s, GLshort t, GLshort r, GLshort q)
ctypedef void (*GL_MULTI_TEX_COORD4SV)(GLenum target, const GLshort *v)
ctypedef void (*GL_LOAD_TRANSPOSE_MATRIXF)(const GLfloat *m)
ctypedef void (*GL_LOAD_TRANSPOSE_MATRIXD)(const GLdouble *m)
ctypedef void (*GL_MULT_TRANSPOSE_MATRIXF)(const GLfloat *m)
ctypedef void (*GL_MULT_TRANSPOSE_MATRIXD)(const GLdouble *m)

cdef GL_ACTIVE_TEXTURE cglActiveTexture = NULL
cdef GL_SAMPLE_COVERAGE cglSampleCoverage = NULL
cdef GL_COMPRESSED_TEX_IMAGE3D cglCompressedTexImage3D = NULL
cdef GL_COMPRESSED_TEX_IMAGE2D cglCompressedTexImage2D = NULL
cdef GL_COMPRESSED_TEX_IMAGE1D cglCompressedTexImage1D = NULL
cdef GL_COMPRESSED_TEX_SUB_IMAGE3D cglCompressedTexSubImage3D = NULL
cdef GL_COMPRESSED_TEX_SUB_IMAGE2D cglCompressedTexSubImage2D = NULL
cdef GL_COMPRESSED_TEX_SUB_IMAGE1D cglCompressedTexSubImage1D = NULL
cdef GL_GET_COMPRESSED_TEX_IMAGE cglGetCompressedTexImage = NULL
cdef GL_CLIENT_ACTIVE_TEXTURE cglClientActiveTexture = NULL
cdef GL_MULTI_TEX_COORD1D cglMultiTexCoord1d = NULL
cdef GL_MULTI_TEX_COORD1DV cglMultiTexCoord1dv = NULL
cdef GL_MULTI_TEX_COORD1F cglMultiTexCoord1f = NULL
cdef GL_MULTI_TEX_COORD1FV cglMultiTexCoord1fv = NULL
cdef GL_MULTI_TEX_COORD1I cglMultiTexCoord1i = NULL
cdef GL_MULTI_TEX_COORD1IV cglMultiTexCoord1iv = NULL
cdef GL_MULTI_TEX_COORD1S cglMultiTexCoord1s = NULL
cdef GL_MULTI_TEX_COORD1SV cglMultiTexCoord1sv = NULL
cdef GL_MULTI_TEX_COORD2D cglMultiTexCoord2d = NULL
cdef GL_MULTI_TEX_COORD2DV cglMultiTexCoord2dv = NULL
cdef GL_MULTI_TEX_COORD2F cglMultiTexCoord2f = NULL
cdef GL_MULTI_TEX_COORD2FV cglMultiTexCoord2fv = NULL
cdef GL_MULTI_TEX_COORD2I cglMultiTexCoord2i = NULL
cdef GL_MULTI_TEX_COORD2IV cglMultiTexCoord2iv = NULL
cdef GL_MULTI_TEX_COORD2S cglMultiTexCoord2s = NULL
cdef GL_MULTI_TEX_COORD2SV cglMultiTexCoord2sv = NULL
cdef GL_MULTI_TEX_COORD3D cglMultiTexCoord3d = NULL
cdef GL_MULTI_TEX_COORD3DV cglMultiTexCoord3dv = NULL
cdef GL_MULTI_TEX_COORD3F cglMultiTexCoord3f = NULL
cdef GL_MULTI_TEX_COORD3FV cglMultiTexCoord3fv = NULL
cdef GL_MULTI_TEX_COORD3I cglMultiTexCoord3i = NULL
cdef GL_MULTI_TEX_COORD3IV cglMultiTexCoord3iv = NULL
cdef GL_MULTI_TEX_COORD3S cglMultiTexCoord3s = NULL
cdef GL_MULTI_TEX_COORD3SV cglMultiTexCoord3sv = NULL
cdef GL_MULTI_TEX_COORD4D cglMultiTexCoord4d = NULL
cdef GL_MULTI_TEX_COORD4DV cglMultiTexCoord4dv = NULL
cdef GL_MULTI_TEX_COORD4F cglMultiTexCoord4f = NULL
cdef GL_MULTI_TEX_COORD4FV cglMultiTexCoord4fv = NULL
cdef GL_MULTI_TEX_COORD4I cglMultiTexCoord4i = NULL
cdef GL_MULTI_TEX_COORD4IV cglMultiTexCoord4iv = NULL
cdef GL_MULTI_TEX_COORD4S cglMultiTexCoord4s = NULL
cdef GL_MULTI_TEX_COORD4SV cglMultiTexCoord4sv = NULL
cdef GL_LOAD_TRANSPOSE_MATRIXF cglLoadTransposeMatrixf = NULL
cdef GL_LOAD_TRANSPOSE_MATRIXD cglLoadTransposeMatrixd = NULL
cdef GL_MULT_TRANSPOSE_MATRIXF cglMultTransposeMatrixf = NULL
cdef GL_MULT_TRANSPOSE_MATRIXD cglMultTransposeMatrixd = NULL


cdef void GetglActiveTexture(GLenum texture):
    global cglActiveTexture
    cglActiveTexture = <GL_ACTIVE_TEXTURE>getFunction(b"glActiveTexture")
    cglActiveTexture(texture)

cdef void GetglSampleCoverage(GLfloat value, GLboolean invert):
    global cglSampleCoverage
    cglSampleCoverage = <GL_SAMPLE_COVERAGE>getFunction(b"glSampleCoverage")
    cglSampleCoverage(value, invert)

cdef void GetglCompressedTexImage3D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const void *data):
    global cglCompressedTexImage3D
    cglCompressedTexImage3D = <GL_COMPRESSED_TEX_IMAGE3D>getFunction(b"glCompressedTexImage3D")
    cglCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data)

cdef void GetglCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void *data):
    global cglCompressedTexImage2D
    cglCompressedTexImage2D = <GL_COMPRESSED_TEX_IMAGE2D>getFunction(b"glCompressedTexImage2D")
    cglCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)

cdef void GetglCompressedTexImage1D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei imageSize, const void *data):
    global cglCompressedTexImage1D
    cglCompressedTexImage1D = <GL_COMPRESSED_TEX_IMAGE1D>getFunction(b"glCompressedTexImage1D")
    cglCompressedTexImage1D(target, level, internalformat, width, border, imageSize, data)

cdef void GetglCompressedTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTexSubImage3D
    cglCompressedTexSubImage3D = <GL_COMPRESSED_TEX_SUB_IMAGE3D>getFunction(b"glCompressedTexSubImage3D")
    cglCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

cdef void GetglCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTexSubImage2D
    cglCompressedTexSubImage2D = <GL_COMPRESSED_TEX_SUB_IMAGE2D>getFunction(b"glCompressedTexSubImage2D")
    cglCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)

cdef void GetglCompressedTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTexSubImage1D
    cglCompressedTexSubImage1D = <GL_COMPRESSED_TEX_SUB_IMAGE1D>getFunction(b"glCompressedTexSubImage1D")
    cglCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize, data)

cdef void GetglGetCompressedTexImage(GLenum target, GLint level, void *img):
    global cglGetCompressedTexImage
    cglGetCompressedTexImage = <GL_GET_COMPRESSED_TEX_IMAGE>getFunction(b"glGetCompressedTexImage")
    cglGetCompressedTexImage(target, level, img)

cdef void GetglClientActiveTexture(GLenum texture):
    global cglClientActiveTexture
    cglClientActiveTexture = <GL_CLIENT_ACTIVE_TEXTURE>getFunction(b"glClientActiveTexture")
    cglClientActiveTexture(texture)

cdef void GetglMultiTexCoord1d(GLenum target, GLdouble s):
    global cglMultiTexCoord1d
    cglMultiTexCoord1d = <GL_MULTI_TEX_COORD1D>getFunction(b"glMultiTexCoord1d")
    cglMultiTexCoord1d(target, s)

cdef void GetglMultiTexCoord1dv(GLenum target, const GLdouble *v):
    global cglMultiTexCoord1dv
    cglMultiTexCoord1dv = <GL_MULTI_TEX_COORD1DV>getFunction(b"glMultiTexCoord1dv")
    cglMultiTexCoord1dv(target, v)

cdef void GetglMultiTexCoord1f(GLenum target, GLfloat s):
    global cglMultiTexCoord1f
    cglMultiTexCoord1f = <GL_MULTI_TEX_COORD1F>getFunction(b"glMultiTexCoord1f")
    cglMultiTexCoord1f(target, s)

cdef void GetglMultiTexCoord1fv(GLenum target, const GLfloat *v):
    global cglMultiTexCoord1fv
    cglMultiTexCoord1fv = <GL_MULTI_TEX_COORD1FV>getFunction(b"glMultiTexCoord1fv")
    cglMultiTexCoord1fv(target, v)

cdef void GetglMultiTexCoord1i(GLenum target, GLint s):
    global cglMultiTexCoord1i
    cglMultiTexCoord1i = <GL_MULTI_TEX_COORD1I>getFunction(b"glMultiTexCoord1i")
    cglMultiTexCoord1i(target, s)

cdef void GetglMultiTexCoord1iv(GLenum target, const GLint *v):
    global cglMultiTexCoord1iv
    cglMultiTexCoord1iv = <GL_MULTI_TEX_COORD1IV>getFunction(b"glMultiTexCoord1iv")
    cglMultiTexCoord1iv(target, v)

cdef void GetglMultiTexCoord1s(GLenum target, GLshort s):
    global cglMultiTexCoord1s
    cglMultiTexCoord1s = <GL_MULTI_TEX_COORD1S>getFunction(b"glMultiTexCoord1s")
    cglMultiTexCoord1s(target, s)

cdef void GetglMultiTexCoord1sv(GLenum target, const GLshort *v):
    global cglMultiTexCoord1sv
    cglMultiTexCoord1sv = <GL_MULTI_TEX_COORD1SV>getFunction(b"glMultiTexCoord1sv")
    cglMultiTexCoord1sv(target, v)

cdef void GetglMultiTexCoord2d(GLenum target, GLdouble s, GLdouble t):
    global cglMultiTexCoord2d
    cglMultiTexCoord2d = <GL_MULTI_TEX_COORD2D>getFunction(b"glMultiTexCoord2d")
    cglMultiTexCoord2d(target, s, t)

cdef void GetglMultiTexCoord2dv(GLenum target, const GLdouble *v):
    global cglMultiTexCoord2dv
    cglMultiTexCoord2dv = <GL_MULTI_TEX_COORD2DV>getFunction(b"glMultiTexCoord2dv")
    cglMultiTexCoord2dv(target, v)

cdef void GetglMultiTexCoord2f(GLenum target, GLfloat s, GLfloat t):
    global cglMultiTexCoord2f
    cglMultiTexCoord2f = <GL_MULTI_TEX_COORD2F>getFunction(b"glMultiTexCoord2f")
    cglMultiTexCoord2f(target, s, t)

cdef void GetglMultiTexCoord2fv(GLenum target, const GLfloat *v):
    global cglMultiTexCoord2fv
    cglMultiTexCoord2fv = <GL_MULTI_TEX_COORD2FV>getFunction(b"glMultiTexCoord2fv")
    cglMultiTexCoord2fv(target, v)

cdef void GetglMultiTexCoord2i(GLenum target, GLint s, GLint t):
    global cglMultiTexCoord2i
    cglMultiTexCoord2i = <GL_MULTI_TEX_COORD2I>getFunction(b"glMultiTexCoord2i")
    cglMultiTexCoord2i(target, s, t)

cdef void GetglMultiTexCoord2iv(GLenum target, const GLint *v):
    global cglMultiTexCoord2iv
    cglMultiTexCoord2iv = <GL_MULTI_TEX_COORD2IV>getFunction(b"glMultiTexCoord2iv")
    cglMultiTexCoord2iv(target, v)

cdef void GetglMultiTexCoord2s(GLenum target, GLshort s, GLshort t):
    global cglMultiTexCoord2s
    cglMultiTexCoord2s = <GL_MULTI_TEX_COORD2S>getFunction(b"glMultiTexCoord2s")
    cglMultiTexCoord2s(target, s, t)

cdef void GetglMultiTexCoord2sv(GLenum target, const GLshort *v):
    global cglMultiTexCoord2sv
    cglMultiTexCoord2sv = <GL_MULTI_TEX_COORD2SV>getFunction(b"glMultiTexCoord2sv")
    cglMultiTexCoord2sv(target, v)

cdef void GetglMultiTexCoord3d(GLenum target, GLdouble s, GLdouble t, GLdouble r):
    global cglMultiTexCoord3d
    cglMultiTexCoord3d = <GL_MULTI_TEX_COORD3D>getFunction(b"glMultiTexCoord3d")
    cglMultiTexCoord3d(target, s, t, r)

cdef void GetglMultiTexCoord3dv(GLenum target, const GLdouble *v):
    global cglMultiTexCoord3dv
    cglMultiTexCoord3dv = <GL_MULTI_TEX_COORD3DV>getFunction(b"glMultiTexCoord3dv")
    cglMultiTexCoord3dv(target, v)

cdef void GetglMultiTexCoord3f(GLenum target, GLfloat s, GLfloat t, GLfloat r):
    global cglMultiTexCoord3f
    cglMultiTexCoord3f = <GL_MULTI_TEX_COORD3F>getFunction(b"glMultiTexCoord3f")
    cglMultiTexCoord3f(target, s, t, r)

cdef void GetglMultiTexCoord3fv(GLenum target, const GLfloat *v):
    global cglMultiTexCoord3fv
    cglMultiTexCoord3fv = <GL_MULTI_TEX_COORD3FV>getFunction(b"glMultiTexCoord3fv")
    cglMultiTexCoord3fv(target, v)

cdef void GetglMultiTexCoord3i(GLenum target, GLint s, GLint t, GLint r):
    global cglMultiTexCoord3i
    cglMultiTexCoord3i = <GL_MULTI_TEX_COORD3I>getFunction(b"glMultiTexCoord3i")
    cglMultiTexCoord3i(target, s, t, r)

cdef void GetglMultiTexCoord3iv(GLenum target, const GLint *v):
    global cglMultiTexCoord3iv
    cglMultiTexCoord3iv = <GL_MULTI_TEX_COORD3IV>getFunction(b"glMultiTexCoord3iv")
    cglMultiTexCoord3iv(target, v)

cdef void GetglMultiTexCoord3s(GLenum target, GLshort s, GLshort t, GLshort r):
    global cglMultiTexCoord3s
    cglMultiTexCoord3s = <GL_MULTI_TEX_COORD3S>getFunction(b"glMultiTexCoord3s")
    cglMultiTexCoord3s(target, s, t, r)

cdef void GetglMultiTexCoord3sv(GLenum target, const GLshort *v):
    global cglMultiTexCoord3sv
    cglMultiTexCoord3sv = <GL_MULTI_TEX_COORD3SV>getFunction(b"glMultiTexCoord3sv")
    cglMultiTexCoord3sv(target, v)

cdef void GetglMultiTexCoord4d(GLenum target, GLdouble s, GLdouble t, GLdouble r, GLdouble q):
    global cglMultiTexCoord4d
    cglMultiTexCoord4d = <GL_MULTI_TEX_COORD4D>getFunction(b"glMultiTexCoord4d")
    cglMultiTexCoord4d(target, s, t, r, q)

cdef void GetglMultiTexCoord4dv(GLenum target, const GLdouble *v):
    global cglMultiTexCoord4dv
    cglMultiTexCoord4dv = <GL_MULTI_TEX_COORD4DV>getFunction(b"glMultiTexCoord4dv")
    cglMultiTexCoord4dv(target, v)

cdef void GetglMultiTexCoord4f(GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q):
    global cglMultiTexCoord4f
    cglMultiTexCoord4f = <GL_MULTI_TEX_COORD4F>getFunction(b"glMultiTexCoord4f")
    cglMultiTexCoord4f(target, s, t, r, q)

cdef void GetglMultiTexCoord4fv(GLenum target, const GLfloat *v):
    global cglMultiTexCoord4fv
    cglMultiTexCoord4fv = <GL_MULTI_TEX_COORD4FV>getFunction(b"glMultiTexCoord4fv")
    cglMultiTexCoord4fv(target, v)

cdef void GetglMultiTexCoord4i(GLenum target, GLint s, GLint t, GLint r, GLint q):
    global cglMultiTexCoord4i
    cglMultiTexCoord4i = <GL_MULTI_TEX_COORD4I>getFunction(b"glMultiTexCoord4i")
    cglMultiTexCoord4i(target, s, t, r, q)

cdef void GetglMultiTexCoord4iv(GLenum target, const GLint *v):
    global cglMultiTexCoord4iv
    cglMultiTexCoord4iv = <GL_MULTI_TEX_COORD4IV>getFunction(b"glMultiTexCoord4iv")
    cglMultiTexCoord4iv(target, v)

cdef void GetglMultiTexCoord4s(GLenum target, GLshort s, GLshort t, GLshort r, GLshort q):
    global cglMultiTexCoord4s
    cglMultiTexCoord4s = <GL_MULTI_TEX_COORD4S>getFunction(b"glMultiTexCoord4s")
    cglMultiTexCoord4s(target, s, t, r, q)

cdef void GetglMultiTexCoord4sv(GLenum target, const GLshort *v):
    global cglMultiTexCoord4sv
    cglMultiTexCoord4sv = <GL_MULTI_TEX_COORD4SV>getFunction(b"glMultiTexCoord4sv")
    cglMultiTexCoord4sv(target, v)

cdef void GetglLoadTransposeMatrixf(const GLfloat *m):
    global cglLoadTransposeMatrixf
    cglLoadTransposeMatrixf = <GL_LOAD_TRANSPOSE_MATRIXF>getFunction(b"glLoadTransposeMatrixf")
    cglLoadTransposeMatrixf(m)

cdef void GetglLoadTransposeMatrixd(const GLdouble *m):
    global cglLoadTransposeMatrixd
    cglLoadTransposeMatrixd = <GL_LOAD_TRANSPOSE_MATRIXD>getFunction(b"glLoadTransposeMatrixd")
    cglLoadTransposeMatrixd(m)

cdef void GetglMultTransposeMatrixf(const GLfloat *m):
    global cglMultTransposeMatrixf
    cglMultTransposeMatrixf = <GL_MULT_TRANSPOSE_MATRIXF>getFunction(b"glMultTransposeMatrixf")
    cglMultTransposeMatrixf(m)

cdef void GetglMultTransposeMatrixd(const GLdouble *m):
    global cglMultTransposeMatrixd
    cglMultTransposeMatrixd = <GL_MULT_TRANSPOSE_MATRIXD>getFunction(b"glMultTransposeMatrixd")
    cglMultTransposeMatrixd(m)

cglActiveTexture = GetglActiveTexture
cglSampleCoverage = GetglSampleCoverage
cglCompressedTexImage3D = GetglCompressedTexImage3D
cglCompressedTexImage2D = GetglCompressedTexImage2D
cglCompressedTexImage1D = GetglCompressedTexImage1D
cglCompressedTexSubImage3D = GetglCompressedTexSubImage3D
cglCompressedTexSubImage2D = GetglCompressedTexSubImage2D
cglCompressedTexSubImage1D = GetglCompressedTexSubImage1D
cglGetCompressedTexImage = GetglGetCompressedTexImage
cglClientActiveTexture = GetglClientActiveTexture
cglMultiTexCoord1d = GetglMultiTexCoord1d
cglMultiTexCoord1dv = GetglMultiTexCoord1dv
cglMultiTexCoord1f = GetglMultiTexCoord1f
cglMultiTexCoord1fv = GetglMultiTexCoord1fv
cglMultiTexCoord1i = GetglMultiTexCoord1i
cglMultiTexCoord1iv = GetglMultiTexCoord1iv
cglMultiTexCoord1s = GetglMultiTexCoord1s
cglMultiTexCoord1sv = GetglMultiTexCoord1sv
cglMultiTexCoord2d = GetglMultiTexCoord2d
cglMultiTexCoord2dv = GetglMultiTexCoord2dv
cglMultiTexCoord2f = GetglMultiTexCoord2f
cglMultiTexCoord2fv = GetglMultiTexCoord2fv
cglMultiTexCoord2i = GetglMultiTexCoord2i
cglMultiTexCoord2iv = GetglMultiTexCoord2iv
cglMultiTexCoord2s = GetglMultiTexCoord2s
cglMultiTexCoord2sv = GetglMultiTexCoord2sv
cglMultiTexCoord3d = GetglMultiTexCoord3d
cglMultiTexCoord3dv = GetglMultiTexCoord3dv
cglMultiTexCoord3f = GetglMultiTexCoord3f
cglMultiTexCoord3fv = GetglMultiTexCoord3fv
cglMultiTexCoord3i = GetglMultiTexCoord3i
cglMultiTexCoord3iv = GetglMultiTexCoord3iv
cglMultiTexCoord3s = GetglMultiTexCoord3s
cglMultiTexCoord3sv = GetglMultiTexCoord3sv
cglMultiTexCoord4d = GetglMultiTexCoord4d
cglMultiTexCoord4dv = GetglMultiTexCoord4dv
cglMultiTexCoord4f = GetglMultiTexCoord4f
cglMultiTexCoord4fv = GetglMultiTexCoord4fv
cglMultiTexCoord4i = GetglMultiTexCoord4i
cglMultiTexCoord4iv = GetglMultiTexCoord4iv
cglMultiTexCoord4s = GetglMultiTexCoord4s
cglMultiTexCoord4sv = GetglMultiTexCoord4sv
cglLoadTransposeMatrixf = GetglLoadTransposeMatrixf
cglLoadTransposeMatrixd = GetglLoadTransposeMatrixd
cglMultTransposeMatrixf = GetglMultTransposeMatrixf
cglMultTransposeMatrixd = GetglMultTransposeMatrixd


cpdef void glActiveTexture(GLenum texture):
    cglActiveTexture(texture)

cpdef void glSampleCoverage(GLfloat value, GLboolean invert):
    cglSampleCoverage(value, invert)

cpdef void glCompressedTexImage3D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const void *data):
    cglCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data)

cpdef void glCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void *data):
    cglCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)

cpdef void glCompressedTexImage1D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei imageSize, const void *data):
    cglCompressedTexImage1D(target, level, internalformat, width, border, imageSize, data)

cpdef void glCompressedTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

cpdef void glCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)

cpdef void glCompressedTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize, data)

cpdef void glGetCompressedTexImage(GLenum target, GLint level, void *img):
    cglGetCompressedTexImage(target, level, img)

cpdef void glClientActiveTexture(GLenum texture):
    cglClientActiveTexture(texture)

cpdef void glMultiTexCoord1d(GLenum target, GLdouble s):
    cglMultiTexCoord1d(target, s)

cpdef void glMultiTexCoord1dv(GLenum target, const GLdouble *v):
    cglMultiTexCoord1dv(target, v)

cpdef void glMultiTexCoord1f(GLenum target, GLfloat s):
    cglMultiTexCoord1f(target, s)

cpdef void glMultiTexCoord1fv(GLenum target, const GLfloat *v):
    cglMultiTexCoord1fv(target, v)

cpdef void glMultiTexCoord1i(GLenum target, GLint s):
    cglMultiTexCoord1i(target, s)

cpdef void glMultiTexCoord1iv(GLenum target, const GLint *v):
    cglMultiTexCoord1iv(target, v)

cpdef void glMultiTexCoord1s(GLenum target, GLshort s):
    cglMultiTexCoord1s(target, s)

cpdef void glMultiTexCoord1sv(GLenum target, const GLshort *v):
    cglMultiTexCoord1sv(target, v)

cpdef void glMultiTexCoord2d(GLenum target, GLdouble s, GLdouble t):
    cglMultiTexCoord2d(target, s, t)

cpdef void glMultiTexCoord2dv(GLenum target, const GLdouble *v):
    cglMultiTexCoord2dv(target, v)

cpdef void glMultiTexCoord2f(GLenum target, GLfloat s, GLfloat t):
    cglMultiTexCoord2f(target, s, t)

cpdef void glMultiTexCoord2fv(GLenum target, const GLfloat *v):
    cglMultiTexCoord2fv(target, v)

cpdef void glMultiTexCoord2i(GLenum target, GLint s, GLint t):
    cglMultiTexCoord2i(target, s, t)

cpdef void glMultiTexCoord2iv(GLenum target, const GLint *v):
    cglMultiTexCoord2iv(target, v)

cpdef void glMultiTexCoord2s(GLenum target, GLshort s, GLshort t):
    cglMultiTexCoord2s(target, s, t)

cpdef void glMultiTexCoord2sv(GLenum target, const GLshort *v):
    cglMultiTexCoord2sv(target, v)

cpdef void glMultiTexCoord3d(GLenum target, GLdouble s, GLdouble t, GLdouble r):
    cglMultiTexCoord3d(target, s, t, r)

cpdef void glMultiTexCoord3dv(GLenum target, const GLdouble *v):
    cglMultiTexCoord3dv(target, v)

cpdef void glMultiTexCoord3f(GLenum target, GLfloat s, GLfloat t, GLfloat r):
    cglMultiTexCoord3f(target, s, t, r)

cpdef void glMultiTexCoord3fv(GLenum target, const GLfloat *v):
    cglMultiTexCoord3fv(target, v)

cpdef void glMultiTexCoord3i(GLenum target, GLint s, GLint t, GLint r):
    cglMultiTexCoord3i(target, s, t, r)

cpdef void glMultiTexCoord3iv(GLenum target, const GLint *v):
    cglMultiTexCoord3iv(target, v)

cpdef void glMultiTexCoord3s(GLenum target, GLshort s, GLshort t, GLshort r):
    cglMultiTexCoord3s(target, s, t, r)

cpdef void glMultiTexCoord3sv(GLenum target, const GLshort *v):
    cglMultiTexCoord3sv(target, v)

cpdef void glMultiTexCoord4d(GLenum target, GLdouble s, GLdouble t, GLdouble r, GLdouble q):
    cglMultiTexCoord4d(target, s, t, r, q)

cpdef void glMultiTexCoord4dv(GLenum target, const GLdouble *v):
    cglMultiTexCoord4dv(target, v)

cpdef void glMultiTexCoord4f(GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q):
    cglMultiTexCoord4f(target, s, t, r, q)

cpdef void glMultiTexCoord4fv(GLenum target, const GLfloat *v):
    cglMultiTexCoord4fv(target, v)

cpdef void glMultiTexCoord4i(GLenum target, GLint s, GLint t, GLint r, GLint q):
    cglMultiTexCoord4i(target, s, t, r, q)

cpdef void glMultiTexCoord4iv(GLenum target, const GLint *v):
    cglMultiTexCoord4iv(target, v)

cpdef void glMultiTexCoord4s(GLenum target, GLshort s, GLshort t, GLshort r, GLshort q):
    cglMultiTexCoord4s(target, s, t, r, q)

cpdef void glMultiTexCoord4sv(GLenum target, const GLshort *v):
    cglMultiTexCoord4sv(target, v)

cpdef void glLoadTransposeMatrixf(const GLfloat *m):
    cglLoadTransposeMatrixf(m)

cpdef void glLoadTransposeMatrixd(const GLdouble *m):
    cglLoadTransposeMatrixd(m)

cpdef void glMultTransposeMatrixf(const GLfloat *m):
    cglMultTransposeMatrixf(m)

cpdef void glMultTransposeMatrixd(const GLdouble *m):
    cglMultTransposeMatrixd(m)
