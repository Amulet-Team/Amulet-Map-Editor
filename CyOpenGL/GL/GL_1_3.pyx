# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_TEXTURE26 = 0x84DA
cdef GLenum GL_TEXTURE24 = 0x84D8
cdef GLenum GL_TEXTURE2 = 0x84C2
cdef GLenum GL_PROXY_TEXTURE_CUBE_MAP = 0x851B
cdef GLenum GL_OPERAND0_ALPHA = 0x8598
cdef GLenum GL_PRIMARY_COLOR = 0x8577
cdef GLenum GL_TRANSPOSE_COLOR_MATRIX = 0x84E6
cdef GLenum GL_TEXTURE14 = 0x84CE
cdef GLenum GL_TEXTURE19 = 0x84D3
cdef GLenum GL_OPERAND2_ALPHA = 0x859A
cdef GLenum GL_CONSTANT = 0x8576
cdef GLenum GL_TEXTURE_COMPRESSED_IMAGE_SIZE = 0x86A0
cdef GLenum GL_TEXTURE9 = 0x84C9
cdef GLenum GL_SAMPLE_ALPHA_TO_ONE = 0x809F
cdef GLenum GL_TEXTURE6 = 0x84C6
cdef GLenum GL_COMBINE_RGB = 0x8571
cdef GLenum GL_DOT3_RGBA = 0x86AF
cdef GLenum GL_TEXTURE20 = 0x84D4
cdef GLenum GL_TEXTURE7 = 0x84C7
cdef GLenum GL_NORMAL_MAP = 0x8511
cdef GLenum GL_TRANSPOSE_MODELVIEW_MATRIX = 0x84E3
cdef GLenum GL_SAMPLE_BUFFERS = 0x80A8
cdef GLenum GL_TEXTURE_CUBE_MAP = 0x8513
cdef GLenum GL_SAMPLE_COVERAGE_VALUE = 0x80AA
cdef GLenum GL_TEXTURE17 = 0x84D1
cdef GLenum GL_TEXTURE27 = 0x84DB
cdef GLenum GL_SAMPLES = 0x80A9
cdef GLenum GL_SUBTRACT = 0x84E7
cdef GLenum GL_TEXTURE23 = 0x84D7
cdef GLenum GL_TEXTURE1 = 0x84C1
cdef GLenum GL_TEXTURE13 = 0x84CD
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
cdef GLenum GL_TRANSPOSE_TEXTURE_MATRIX = 0x84E5
cdef GLenum GL_TEXTURE12 = 0x84CC
cdef GLenum GL_COMPRESSED_RGB = 0x84ED
cdef GLenum GL_TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
cdef GLenum GL_TEXTURE0 = 0x84C0
cdef GLenum GL_MAX_TEXTURE_UNITS = 0x84E2
cdef GLenum GL_RGB_SCALE = 0x8573
cdef GLenum GL_TEXTURE4 = 0x84C4
cdef GLenum GL_TEXTURE5 = 0x84C5
cdef GLenum GL_CLIENT_ACTIVE_TEXTURE = 0x84E1
cdef GLenum GL_TEXTURE28 = 0x84DC
cdef GLenum GL_TEXTURE30 = 0x84DE
cdef GLenum GL_SOURCE1_ALPHA = 0x8589
cdef GLenum GL_TEXTURE31 = 0x84DF
cdef GLenum GL_TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
cdef GLenum GL_SOURCE2_ALPHA = 0x858A
cdef GLenum GL_MULTISAMPLE = 0x809D
cdef GLenum GL_TEXTURE11 = 0x84CB
cdef GLenum GL_OPERAND1_RGB = 0x8591
cdef GLenum GL_TEXTURE25 = 0x84D9
cdef GLenum GL_COMPRESSED_LUMINANCE_ALPHA = 0x84EB
cdef GLenum GL_REFLECTION_MAP = 0x8512
cdef GLenum GL_TEXTURE_COMPRESSION_HINT = 0x84EF
cdef GLenum GL_TEXTURE8 = 0x84C8
cdef GLenum GL_TEXTURE15 = 0x84CF
cdef GLenum GL_MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
cdef GLenum GL_PREVIOUS = 0x8578
cdef GLenum GL_SAMPLE_COVERAGE = 0x80A0
cdef GLenum GL_TEXTURE18 = 0x84D2
cdef GLenum GL_COMPRESSED_LUMINANCE = 0x84EA
cdef GLenum GL_TEXTURE22 = 0x84D6
cdef GLenum GL_OPERAND1_ALPHA = 0x8599
cdef GLenum GL_COMPRESSED_INTENSITY = 0x84EC
cdef GLenum GL_COMPRESSED_ALPHA = 0x84E9
cdef GLenum GL_TEXTURE10 = 0x84CA
cdef GLenum GL_COMPRESSED_TEXTURE_FORMATS = 0x86A3
cdef GLenum GL_DOT3_RGB = 0x86AE
cdef GLenum GL_COMBINE_ALPHA = 0x8572
cdef GLenum GL_TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
cdef GLenum GL_ADD_SIGNED = 0x8574
cdef GLenum GL_TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
cdef GLenum GL_COMPRESSED_RGBA = 0x84EE
cdef GLenum GL_OPERAND0_RGB = 0x8590
cdef GLenum GL_CLAMP_TO_BORDER = 0x812D
cdef GLenum GL_COMBINE = 0x8570
cdef GLenum GL_TRANSPOSE_PROJECTION_MATRIX = 0x84E4
cdef GLenum GL_SOURCE0_ALPHA = 0x8588
cdef GLenum GL_ACTIVE_TEXTURE = 0x84E0
cdef GLenum GL_TEXTURE3 = 0x84C3
cdef GLenum GL_INTERPOLATE = 0x8575
cdef GLenum GL_TEXTURE21 = 0x84D5
cdef GLenum GL_TEXTURE16 = 0x84D0
cdef GLenum GL_MULTISAMPLE_BIT = 0x20000000
cdef GLenum GL_SAMPLE_ALPHA_TO_COVERAGE = 0x809E
cdef GLenum GL_SOURCE2_RGB = 0x8582
cdef GLenum GL_TEXTURE29 = 0x84DD
cdef GLenum GL_TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
cdef GLenum GL_SAMPLE_COVERAGE_INVERT = 0x80AB
cdef GLenum GL_OPERAND2_RGB = 0x8592
cdef GLenum GL_SOURCE0_RGB = 0x8580
cdef GLenum GL_TEXTURE_COMPRESSED = 0x86A1
cdef GLenum GL_TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
cdef GLenum GL_SOURCE1_RGB = 0x8581
cdef GLenum GL_NUM_COMPRESSED_TEXTURE_FORMATS = 0x86A2

ctypedef void (*PFNGLCOMPRESSEDTEXIMAGE1DPROC)(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei imageSize, const void *data)
ctypedef void (*PFNGLGETCOMPRESSEDTEXIMAGEPROC)(GLenum target, GLint level, void *img)
ctypedef void (*PFNGLMULTTRANSPOSEMATRIXFPROC)(const GLfloat *m)
ctypedef void (*PFNGLMULTITEXCOORD4SPROC)(GLenum target, GLshort s, GLshort t, GLshort r, GLshort q)
ctypedef void (*PFNGLMULTITEXCOORD4SVPROC)(GLenum target, const GLshort *v)
ctypedef void (*PFNGLMULTITEXCOORD1FPROC)(GLenum target, GLfloat s)
ctypedef void (*PFNGLMULTITEXCOORD3SPROC)(GLenum target, GLshort s, GLshort t, GLshort r)
ctypedef void (*PFNGLCOMPRESSEDTEXSUBIMAGE3DPROC)(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*PFNGLMULTITEXCOORD3FVPROC)(GLenum target, const GLfloat *v)
ctypedef void (*PFNGLMULTITEXCOORD4IPROC)(GLenum target, GLint s, GLint t, GLint r, GLint q)
ctypedef void (*PFNGLMULTITEXCOORD2FPROC)(GLenum target, GLfloat s, GLfloat t)
ctypedef void (*PFNGLMULTITEXCOORD3IVPROC)(GLenum target, const GLint *v)
ctypedef void (*PFNGLACTIVETEXTUREPROC)(GLenum texture)
ctypedef void (*PFNGLMULTITEXCOORD4DPROC)(GLenum target, GLdouble s, GLdouble t, GLdouble r, GLdouble q)
ctypedef void (*PFNGLMULTITEXCOORD4FPROC)(GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q)
ctypedef void (*PFNGLMULTITEXCOORD1FVPROC)(GLenum target, const GLfloat *v)
ctypedef void (*PFNGLMULTITEXCOORD1SPROC)(GLenum target, GLshort s)
ctypedef void (*PFNGLMULTITEXCOORD4FVPROC)(GLenum target, const GLfloat *v)
ctypedef void (*PFNGLLOADTRANSPOSEMATRIXDPROC)(const GLdouble *m)
ctypedef void (*PFNGLMULTITEXCOORD2SVPROC)(GLenum target, const GLshort *v)
ctypedef void (*PFNGLCOMPRESSEDTEXSUBIMAGE1DPROC)(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*PFNGLMULTITEXCOORD1DVPROC)(GLenum target, const GLdouble *v)
ctypedef void (*PFNGLMULTITEXCOORD4IVPROC)(GLenum target, const GLint *v)
ctypedef void (*PFNGLMULTITEXCOORD1DPROC)(GLenum target, GLdouble s)
ctypedef void (*PFNGLCOMPRESSEDTEXSUBIMAGE2DPROC)(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*PFNGLMULTITEXCOORD1IVPROC)(GLenum target, const GLint *v)
ctypedef void (*PFNGLMULTTRANSPOSEMATRIXDPROC)(const GLdouble *m)
ctypedef void (*PFNGLMULTITEXCOORD3IPROC)(GLenum target, GLint s, GLint t, GLint r)
ctypedef void (*PFNGLCOMPRESSEDTEXIMAGE3DPROC)(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const void *data)
ctypedef void (*PFNGLLOADTRANSPOSEMATRIXFPROC)(const GLfloat *m)
ctypedef void (*PFNGLMULTITEXCOORD2SPROC)(GLenum target, GLshort s, GLshort t)
ctypedef void (*PFNGLMULTITEXCOORD2DPROC)(GLenum target, GLdouble s, GLdouble t)
ctypedef void (*PFNGLMULTITEXCOORD1SVPROC)(GLenum target, const GLshort *v)
ctypedef void (*PFNGLMULTITEXCOORD3DVPROC)(GLenum target, const GLdouble *v)
ctypedef void (*PFNGLMULTITEXCOORD3FPROC)(GLenum target, GLfloat s, GLfloat t, GLfloat r)
ctypedef void (*PFNGLCLIENTACTIVETEXTUREPROC)(GLenum texture)
ctypedef void (*PFNGLSAMPLECOVERAGEPROC)(GLfloat value, GLboolean invert)
ctypedef void (*PFNGLMULTITEXCOORD3SVPROC)(GLenum target, const GLshort *v)
ctypedef void (*PFNGLMULTITEXCOORD4DVPROC)(GLenum target, const GLdouble *v)
ctypedef void (*PFNGLMULTITEXCOORD2IPROC)(GLenum target, GLint s, GLint t)
ctypedef void (*PFNGLMULTITEXCOORD3DPROC)(GLenum target, GLdouble s, GLdouble t, GLdouble r)
ctypedef void (*PFNGLCOMPRESSEDTEXIMAGE2DPROC)(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void *data)
ctypedef void (*PFNGLMULTITEXCOORD2FVPROC)(GLenum target, const GLfloat *v)
ctypedef void (*PFNGLMULTITEXCOORD2IVPROC)(GLenum target, const GLint *v)
ctypedef void (*PFNGLMULTITEXCOORD2DVPROC)(GLenum target, const GLdouble *v)
ctypedef void (*PFNGLMULTITEXCOORD1IPROC)(GLenum target, GLint s)

cdef PFNGLCOMPRESSEDTEXIMAGE1DPROC cglCompressedTexImage1D = NULL
cdef PFNGLGETCOMPRESSEDTEXIMAGEPROC cglGetCompressedTexImage = NULL
cdef PFNGLMULTTRANSPOSEMATRIXFPROC cglMultTransposeMatrixf = NULL
cdef PFNGLMULTITEXCOORD4SPROC cglMultiTexCoord4s = NULL
cdef PFNGLMULTITEXCOORD4SVPROC cglMultiTexCoord4sv = NULL
cdef PFNGLMULTITEXCOORD1FPROC cglMultiTexCoord1f = NULL
cdef PFNGLMULTITEXCOORD3SPROC cglMultiTexCoord3s = NULL
cdef PFNGLCOMPRESSEDTEXSUBIMAGE3DPROC cglCompressedTexSubImage3D = NULL
cdef PFNGLMULTITEXCOORD3FVPROC cglMultiTexCoord3fv = NULL
cdef PFNGLMULTITEXCOORD4IPROC cglMultiTexCoord4i = NULL
cdef PFNGLMULTITEXCOORD2FPROC cglMultiTexCoord2f = NULL
cdef PFNGLMULTITEXCOORD3IVPROC cglMultiTexCoord3iv = NULL
cdef PFNGLACTIVETEXTUREPROC cglActiveTexture = NULL
cdef PFNGLMULTITEXCOORD4DPROC cglMultiTexCoord4d = NULL
cdef PFNGLMULTITEXCOORD4FPROC cglMultiTexCoord4f = NULL
cdef PFNGLMULTITEXCOORD1FVPROC cglMultiTexCoord1fv = NULL
cdef PFNGLMULTITEXCOORD1SPROC cglMultiTexCoord1s = NULL
cdef PFNGLMULTITEXCOORD4FVPROC cglMultiTexCoord4fv = NULL
cdef PFNGLLOADTRANSPOSEMATRIXDPROC cglLoadTransposeMatrixd = NULL
cdef PFNGLMULTITEXCOORD2SVPROC cglMultiTexCoord2sv = NULL
cdef PFNGLCOMPRESSEDTEXSUBIMAGE1DPROC cglCompressedTexSubImage1D = NULL
cdef PFNGLMULTITEXCOORD1DVPROC cglMultiTexCoord1dv = NULL
cdef PFNGLMULTITEXCOORD4IVPROC cglMultiTexCoord4iv = NULL
cdef PFNGLMULTITEXCOORD1DPROC cglMultiTexCoord1d = NULL
cdef PFNGLCOMPRESSEDTEXSUBIMAGE2DPROC cglCompressedTexSubImage2D = NULL
cdef PFNGLMULTITEXCOORD1IVPROC cglMultiTexCoord1iv = NULL
cdef PFNGLMULTTRANSPOSEMATRIXDPROC cglMultTransposeMatrixd = NULL
cdef PFNGLMULTITEXCOORD3IPROC cglMultiTexCoord3i = NULL
cdef PFNGLCOMPRESSEDTEXIMAGE3DPROC cglCompressedTexImage3D = NULL
cdef PFNGLLOADTRANSPOSEMATRIXFPROC cglLoadTransposeMatrixf = NULL
cdef PFNGLMULTITEXCOORD2SPROC cglMultiTexCoord2s = NULL
cdef PFNGLMULTITEXCOORD2DPROC cglMultiTexCoord2d = NULL
cdef PFNGLMULTITEXCOORD1SVPROC cglMultiTexCoord1sv = NULL
cdef PFNGLMULTITEXCOORD3DVPROC cglMultiTexCoord3dv = NULL
cdef PFNGLMULTITEXCOORD3FPROC cglMultiTexCoord3f = NULL
cdef PFNGLCLIENTACTIVETEXTUREPROC cglClientActiveTexture = NULL
cdef PFNGLSAMPLECOVERAGEPROC cglSampleCoverage = NULL
cdef PFNGLMULTITEXCOORD3SVPROC cglMultiTexCoord3sv = NULL
cdef PFNGLMULTITEXCOORD4DVPROC cglMultiTexCoord4dv = NULL
cdef PFNGLMULTITEXCOORD2IPROC cglMultiTexCoord2i = NULL
cdef PFNGLMULTITEXCOORD3DPROC cglMultiTexCoord3d = NULL
cdef PFNGLCOMPRESSEDTEXIMAGE2DPROC cglCompressedTexImage2D = NULL
cdef PFNGLMULTITEXCOORD2FVPROC cglMultiTexCoord2fv = NULL
cdef PFNGLMULTITEXCOORD2IVPROC cglMultiTexCoord2iv = NULL
cdef PFNGLMULTITEXCOORD2DVPROC cglMultiTexCoord2dv = NULL
cdef PFNGLMULTITEXCOORD1IPROC cglMultiTexCoord1i = NULL


cdef void GetglCompressedTexImage1D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei imageSize, const void *data):
    global cglCompressedTexImage1D
    cglCompressedTexImage1D = <PFNGLCOMPRESSEDTEXIMAGE1DPROC>getFunction(b"glCompressedTexImage1D")
    cglCompressedTexImage1D(target, level, internalformat, width, border, imageSize, data)

cdef void GetglGetCompressedTexImage(GLenum target, GLint level, void *img):
    global cglGetCompressedTexImage
    cglGetCompressedTexImage = <PFNGLGETCOMPRESSEDTEXIMAGEPROC>getFunction(b"glGetCompressedTexImage")
    cglGetCompressedTexImage(target, level, img)

cdef void GetglMultTransposeMatrixf(const GLfloat *m):
    global cglMultTransposeMatrixf
    cglMultTransposeMatrixf = <PFNGLMULTTRANSPOSEMATRIXFPROC>getFunction(b"glMultTransposeMatrixf")
    cglMultTransposeMatrixf(m)

cdef void GetglMultiTexCoord4s(GLenum target, GLshort s, GLshort t, GLshort r, GLshort q):
    global cglMultiTexCoord4s
    cglMultiTexCoord4s = <PFNGLMULTITEXCOORD4SPROC>getFunction(b"glMultiTexCoord4s")
    cglMultiTexCoord4s(target, s, t, r, q)

cdef void GetglMultiTexCoord4sv(GLenum target, const GLshort *v):
    global cglMultiTexCoord4sv
    cglMultiTexCoord4sv = <PFNGLMULTITEXCOORD4SVPROC>getFunction(b"glMultiTexCoord4sv")
    cglMultiTexCoord4sv(target, v)

cdef void GetglMultiTexCoord1f(GLenum target, GLfloat s):
    global cglMultiTexCoord1f
    cglMultiTexCoord1f = <PFNGLMULTITEXCOORD1FPROC>getFunction(b"glMultiTexCoord1f")
    cglMultiTexCoord1f(target, s)

cdef void GetglMultiTexCoord3s(GLenum target, GLshort s, GLshort t, GLshort r):
    global cglMultiTexCoord3s
    cglMultiTexCoord3s = <PFNGLMULTITEXCOORD3SPROC>getFunction(b"glMultiTexCoord3s")
    cglMultiTexCoord3s(target, s, t, r)

cdef void GetglCompressedTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTexSubImage3D
    cglCompressedTexSubImage3D = <PFNGLCOMPRESSEDTEXSUBIMAGE3DPROC>getFunction(b"glCompressedTexSubImage3D")
    cglCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

cdef void GetglMultiTexCoord3fv(GLenum target, const GLfloat *v):
    global cglMultiTexCoord3fv
    cglMultiTexCoord3fv = <PFNGLMULTITEXCOORD3FVPROC>getFunction(b"glMultiTexCoord3fv")
    cglMultiTexCoord3fv(target, v)

cdef void GetglMultiTexCoord4i(GLenum target, GLint s, GLint t, GLint r, GLint q):
    global cglMultiTexCoord4i
    cglMultiTexCoord4i = <PFNGLMULTITEXCOORD4IPROC>getFunction(b"glMultiTexCoord4i")
    cglMultiTexCoord4i(target, s, t, r, q)

cdef void GetglMultiTexCoord2f(GLenum target, GLfloat s, GLfloat t):
    global cglMultiTexCoord2f
    cglMultiTexCoord2f = <PFNGLMULTITEXCOORD2FPROC>getFunction(b"glMultiTexCoord2f")
    cglMultiTexCoord2f(target, s, t)

cdef void GetglMultiTexCoord3iv(GLenum target, const GLint *v):
    global cglMultiTexCoord3iv
    cglMultiTexCoord3iv = <PFNGLMULTITEXCOORD3IVPROC>getFunction(b"glMultiTexCoord3iv")
    cglMultiTexCoord3iv(target, v)

cdef void GetglActiveTexture(GLenum texture):
    global cglActiveTexture
    cglActiveTexture = <PFNGLACTIVETEXTUREPROC>getFunction(b"glActiveTexture")
    cglActiveTexture(texture)

cdef void GetglMultiTexCoord4d(GLenum target, GLdouble s, GLdouble t, GLdouble r, GLdouble q):
    global cglMultiTexCoord4d
    cglMultiTexCoord4d = <PFNGLMULTITEXCOORD4DPROC>getFunction(b"glMultiTexCoord4d")
    cglMultiTexCoord4d(target, s, t, r, q)

cdef void GetglMultiTexCoord4f(GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q):
    global cglMultiTexCoord4f
    cglMultiTexCoord4f = <PFNGLMULTITEXCOORD4FPROC>getFunction(b"glMultiTexCoord4f")
    cglMultiTexCoord4f(target, s, t, r, q)

cdef void GetglMultiTexCoord1fv(GLenum target, const GLfloat *v):
    global cglMultiTexCoord1fv
    cglMultiTexCoord1fv = <PFNGLMULTITEXCOORD1FVPROC>getFunction(b"glMultiTexCoord1fv")
    cglMultiTexCoord1fv(target, v)

cdef void GetglMultiTexCoord1s(GLenum target, GLshort s):
    global cglMultiTexCoord1s
    cglMultiTexCoord1s = <PFNGLMULTITEXCOORD1SPROC>getFunction(b"glMultiTexCoord1s")
    cglMultiTexCoord1s(target, s)

cdef void GetglMultiTexCoord4fv(GLenum target, const GLfloat *v):
    global cglMultiTexCoord4fv
    cglMultiTexCoord4fv = <PFNGLMULTITEXCOORD4FVPROC>getFunction(b"glMultiTexCoord4fv")
    cglMultiTexCoord4fv(target, v)

cdef void GetglLoadTransposeMatrixd(const GLdouble *m):
    global cglLoadTransposeMatrixd
    cglLoadTransposeMatrixd = <PFNGLLOADTRANSPOSEMATRIXDPROC>getFunction(b"glLoadTransposeMatrixd")
    cglLoadTransposeMatrixd(m)

cdef void GetglMultiTexCoord2sv(GLenum target, const GLshort *v):
    global cglMultiTexCoord2sv
    cglMultiTexCoord2sv = <PFNGLMULTITEXCOORD2SVPROC>getFunction(b"glMultiTexCoord2sv")
    cglMultiTexCoord2sv(target, v)

cdef void GetglCompressedTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTexSubImage1D
    cglCompressedTexSubImage1D = <PFNGLCOMPRESSEDTEXSUBIMAGE1DPROC>getFunction(b"glCompressedTexSubImage1D")
    cglCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize, data)

cdef void GetglMultiTexCoord1dv(GLenum target, const GLdouble *v):
    global cglMultiTexCoord1dv
    cglMultiTexCoord1dv = <PFNGLMULTITEXCOORD1DVPROC>getFunction(b"glMultiTexCoord1dv")
    cglMultiTexCoord1dv(target, v)

cdef void GetglMultiTexCoord4iv(GLenum target, const GLint *v):
    global cglMultiTexCoord4iv
    cglMultiTexCoord4iv = <PFNGLMULTITEXCOORD4IVPROC>getFunction(b"glMultiTexCoord4iv")
    cglMultiTexCoord4iv(target, v)

cdef void GetglMultiTexCoord1d(GLenum target, GLdouble s):
    global cglMultiTexCoord1d
    cglMultiTexCoord1d = <PFNGLMULTITEXCOORD1DPROC>getFunction(b"glMultiTexCoord1d")
    cglMultiTexCoord1d(target, s)

cdef void GetglCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTexSubImage2D
    cglCompressedTexSubImage2D = <PFNGLCOMPRESSEDTEXSUBIMAGE2DPROC>getFunction(b"glCompressedTexSubImage2D")
    cglCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)

cdef void GetglMultiTexCoord1iv(GLenum target, const GLint *v):
    global cglMultiTexCoord1iv
    cglMultiTexCoord1iv = <PFNGLMULTITEXCOORD1IVPROC>getFunction(b"glMultiTexCoord1iv")
    cglMultiTexCoord1iv(target, v)

cdef void GetglMultTransposeMatrixd(const GLdouble *m):
    global cglMultTransposeMatrixd
    cglMultTransposeMatrixd = <PFNGLMULTTRANSPOSEMATRIXDPROC>getFunction(b"glMultTransposeMatrixd")
    cglMultTransposeMatrixd(m)

cdef void GetglMultiTexCoord3i(GLenum target, GLint s, GLint t, GLint r):
    global cglMultiTexCoord3i
    cglMultiTexCoord3i = <PFNGLMULTITEXCOORD3IPROC>getFunction(b"glMultiTexCoord3i")
    cglMultiTexCoord3i(target, s, t, r)

cdef void GetglCompressedTexImage3D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const void *data):
    global cglCompressedTexImage3D
    cglCompressedTexImage3D = <PFNGLCOMPRESSEDTEXIMAGE3DPROC>getFunction(b"glCompressedTexImage3D")
    cglCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data)

cdef void GetglLoadTransposeMatrixf(const GLfloat *m):
    global cglLoadTransposeMatrixf
    cglLoadTransposeMatrixf = <PFNGLLOADTRANSPOSEMATRIXFPROC>getFunction(b"glLoadTransposeMatrixf")
    cglLoadTransposeMatrixf(m)

cdef void GetglMultiTexCoord2s(GLenum target, GLshort s, GLshort t):
    global cglMultiTexCoord2s
    cglMultiTexCoord2s = <PFNGLMULTITEXCOORD2SPROC>getFunction(b"glMultiTexCoord2s")
    cglMultiTexCoord2s(target, s, t)

cdef void GetglMultiTexCoord2d(GLenum target, GLdouble s, GLdouble t):
    global cglMultiTexCoord2d
    cglMultiTexCoord2d = <PFNGLMULTITEXCOORD2DPROC>getFunction(b"glMultiTexCoord2d")
    cglMultiTexCoord2d(target, s, t)

cdef void GetglMultiTexCoord1sv(GLenum target, const GLshort *v):
    global cglMultiTexCoord1sv
    cglMultiTexCoord1sv = <PFNGLMULTITEXCOORD1SVPROC>getFunction(b"glMultiTexCoord1sv")
    cglMultiTexCoord1sv(target, v)

cdef void GetglMultiTexCoord3dv(GLenum target, const GLdouble *v):
    global cglMultiTexCoord3dv
    cglMultiTexCoord3dv = <PFNGLMULTITEXCOORD3DVPROC>getFunction(b"glMultiTexCoord3dv")
    cglMultiTexCoord3dv(target, v)

cdef void GetglMultiTexCoord3f(GLenum target, GLfloat s, GLfloat t, GLfloat r):
    global cglMultiTexCoord3f
    cglMultiTexCoord3f = <PFNGLMULTITEXCOORD3FPROC>getFunction(b"glMultiTexCoord3f")
    cglMultiTexCoord3f(target, s, t, r)

cdef void GetglClientActiveTexture(GLenum texture):
    global cglClientActiveTexture
    cglClientActiveTexture = <PFNGLCLIENTACTIVETEXTUREPROC>getFunction(b"glClientActiveTexture")
    cglClientActiveTexture(texture)

cdef void GetglSampleCoverage(GLfloat value, GLboolean invert):
    global cglSampleCoverage
    cglSampleCoverage = <PFNGLSAMPLECOVERAGEPROC>getFunction(b"glSampleCoverage")
    cglSampleCoverage(value, invert)

cdef void GetglMultiTexCoord3sv(GLenum target, const GLshort *v):
    global cglMultiTexCoord3sv
    cglMultiTexCoord3sv = <PFNGLMULTITEXCOORD3SVPROC>getFunction(b"glMultiTexCoord3sv")
    cglMultiTexCoord3sv(target, v)

cdef void GetglMultiTexCoord4dv(GLenum target, const GLdouble *v):
    global cglMultiTexCoord4dv
    cglMultiTexCoord4dv = <PFNGLMULTITEXCOORD4DVPROC>getFunction(b"glMultiTexCoord4dv")
    cglMultiTexCoord4dv(target, v)

cdef void GetglMultiTexCoord2i(GLenum target, GLint s, GLint t):
    global cglMultiTexCoord2i
    cglMultiTexCoord2i = <PFNGLMULTITEXCOORD2IPROC>getFunction(b"glMultiTexCoord2i")
    cglMultiTexCoord2i(target, s, t)

cdef void GetglMultiTexCoord3d(GLenum target, GLdouble s, GLdouble t, GLdouble r):
    global cglMultiTexCoord3d
    cglMultiTexCoord3d = <PFNGLMULTITEXCOORD3DPROC>getFunction(b"glMultiTexCoord3d")
    cglMultiTexCoord3d(target, s, t, r)

cdef void GetglCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void *data):
    global cglCompressedTexImage2D
    cglCompressedTexImage2D = <PFNGLCOMPRESSEDTEXIMAGE2DPROC>getFunction(b"glCompressedTexImage2D")
    cglCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)

cdef void GetglMultiTexCoord2fv(GLenum target, const GLfloat *v):
    global cglMultiTexCoord2fv
    cglMultiTexCoord2fv = <PFNGLMULTITEXCOORD2FVPROC>getFunction(b"glMultiTexCoord2fv")
    cglMultiTexCoord2fv(target, v)

cdef void GetglMultiTexCoord2iv(GLenum target, const GLint *v):
    global cglMultiTexCoord2iv
    cglMultiTexCoord2iv = <PFNGLMULTITEXCOORD2IVPROC>getFunction(b"glMultiTexCoord2iv")
    cglMultiTexCoord2iv(target, v)

cdef void GetglMultiTexCoord2dv(GLenum target, const GLdouble *v):
    global cglMultiTexCoord2dv
    cglMultiTexCoord2dv = <PFNGLMULTITEXCOORD2DVPROC>getFunction(b"glMultiTexCoord2dv")
    cglMultiTexCoord2dv(target, v)

cdef void GetglMultiTexCoord1i(GLenum target, GLint s):
    global cglMultiTexCoord1i
    cglMultiTexCoord1i = <PFNGLMULTITEXCOORD1IPROC>getFunction(b"glMultiTexCoord1i")
    cglMultiTexCoord1i(target, s)

cglCompressedTexImage1D = GetglCompressedTexImage1D
cglGetCompressedTexImage = GetglGetCompressedTexImage
cglMultTransposeMatrixf = GetglMultTransposeMatrixf
cglMultiTexCoord4s = GetglMultiTexCoord4s
cglMultiTexCoord4sv = GetglMultiTexCoord4sv
cglMultiTexCoord1f = GetglMultiTexCoord1f
cglMultiTexCoord3s = GetglMultiTexCoord3s
cglCompressedTexSubImage3D = GetglCompressedTexSubImage3D
cglMultiTexCoord3fv = GetglMultiTexCoord3fv
cglMultiTexCoord4i = GetglMultiTexCoord4i
cglMultiTexCoord2f = GetglMultiTexCoord2f
cglMultiTexCoord3iv = GetglMultiTexCoord3iv
cglActiveTexture = GetglActiveTexture
cglMultiTexCoord4d = GetglMultiTexCoord4d
cglMultiTexCoord4f = GetglMultiTexCoord4f
cglMultiTexCoord1fv = GetglMultiTexCoord1fv
cglMultiTexCoord1s = GetglMultiTexCoord1s
cglMultiTexCoord4fv = GetglMultiTexCoord4fv
cglLoadTransposeMatrixd = GetglLoadTransposeMatrixd
cglMultiTexCoord2sv = GetglMultiTexCoord2sv
cglCompressedTexSubImage1D = GetglCompressedTexSubImage1D
cglMultiTexCoord1dv = GetglMultiTexCoord1dv
cglMultiTexCoord4iv = GetglMultiTexCoord4iv
cglMultiTexCoord1d = GetglMultiTexCoord1d
cglCompressedTexSubImage2D = GetglCompressedTexSubImage2D
cglMultiTexCoord1iv = GetglMultiTexCoord1iv
cglMultTransposeMatrixd = GetglMultTransposeMatrixd
cglMultiTexCoord3i = GetglMultiTexCoord3i
cglCompressedTexImage3D = GetglCompressedTexImage3D
cglLoadTransposeMatrixf = GetglLoadTransposeMatrixf
cglMultiTexCoord2s = GetglMultiTexCoord2s
cglMultiTexCoord2d = GetglMultiTexCoord2d
cglMultiTexCoord1sv = GetglMultiTexCoord1sv
cglMultiTexCoord3dv = GetglMultiTexCoord3dv
cglMultiTexCoord3f = GetglMultiTexCoord3f
cglClientActiveTexture = GetglClientActiveTexture
cglSampleCoverage = GetglSampleCoverage
cglMultiTexCoord3sv = GetglMultiTexCoord3sv
cglMultiTexCoord4dv = GetglMultiTexCoord4dv
cglMultiTexCoord2i = GetglMultiTexCoord2i
cglMultiTexCoord3d = GetglMultiTexCoord3d
cglCompressedTexImage2D = GetglCompressedTexImage2D
cglMultiTexCoord2fv = GetglMultiTexCoord2fv
cglMultiTexCoord2iv = GetglMultiTexCoord2iv
cglMultiTexCoord2dv = GetglMultiTexCoord2dv
cglMultiTexCoord1i = GetglMultiTexCoord1i


cdef void glCompressedTexImage1D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei imageSize, const void *data):
    cglCompressedTexImage1D(target, level, internalformat, width, border, imageSize, data)

cdef void glGetCompressedTexImage(GLenum target, GLint level, void *img):
    cglGetCompressedTexImage(target, level, img)

cdef void glMultTransposeMatrixf(const GLfloat *m):
    cglMultTransposeMatrixf(m)

cdef void glMultiTexCoord4s(GLenum target, GLshort s, GLshort t, GLshort r, GLshort q):
    cglMultiTexCoord4s(target, s, t, r, q)

cdef void glMultiTexCoord4sv(GLenum target, const GLshort *v):
    cglMultiTexCoord4sv(target, v)

cdef void glMultiTexCoord1f(GLenum target, GLfloat s):
    cglMultiTexCoord1f(target, s)

cdef void glMultiTexCoord3s(GLenum target, GLshort s, GLshort t, GLshort r):
    cglMultiTexCoord3s(target, s, t, r)

cdef void glCompressedTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTexSubImage3D(target, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

cdef void glMultiTexCoord3fv(GLenum target, const GLfloat *v):
    cglMultiTexCoord3fv(target, v)

cdef void glMultiTexCoord4i(GLenum target, GLint s, GLint t, GLint r, GLint q):
    cglMultiTexCoord4i(target, s, t, r, q)

cdef void glMultiTexCoord2f(GLenum target, GLfloat s, GLfloat t):
    cglMultiTexCoord2f(target, s, t)

cdef void glMultiTexCoord3iv(GLenum target, const GLint *v):
    cglMultiTexCoord3iv(target, v)

cdef void glActiveTexture(GLenum texture):
    cglActiveTexture(texture)

cdef void glMultiTexCoord4d(GLenum target, GLdouble s, GLdouble t, GLdouble r, GLdouble q):
    cglMultiTexCoord4d(target, s, t, r, q)

cdef void glMultiTexCoord4f(GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q):
    cglMultiTexCoord4f(target, s, t, r, q)

cdef void glMultiTexCoord1fv(GLenum target, const GLfloat *v):
    cglMultiTexCoord1fv(target, v)

cdef void glMultiTexCoord1s(GLenum target, GLshort s):
    cglMultiTexCoord1s(target, s)

cdef void glMultiTexCoord4fv(GLenum target, const GLfloat *v):
    cglMultiTexCoord4fv(target, v)

cdef void glLoadTransposeMatrixd(const GLdouble *m):
    cglLoadTransposeMatrixd(m)

cdef void glMultiTexCoord2sv(GLenum target, const GLshort *v):
    cglMultiTexCoord2sv(target, v)

cdef void glCompressedTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTexSubImage1D(target, level, xoffset, width, format, imageSize, data)

cdef void glMultiTexCoord1dv(GLenum target, const GLdouble *v):
    cglMultiTexCoord1dv(target, v)

cdef void glMultiTexCoord4iv(GLenum target, const GLint *v):
    cglMultiTexCoord4iv(target, v)

cdef void glMultiTexCoord1d(GLenum target, GLdouble s):
    cglMultiTexCoord1d(target, s)

cdef void glCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTexSubImage2D(target, level, xoffset, yoffset, width, height, format, imageSize, data)

cdef void glMultiTexCoord1iv(GLenum target, const GLint *v):
    cglMultiTexCoord1iv(target, v)

cdef void glMultTransposeMatrixd(const GLdouble *m):
    cglMultTransposeMatrixd(m)

cdef void glMultiTexCoord3i(GLenum target, GLint s, GLint t, GLint r):
    cglMultiTexCoord3i(target, s, t, r)

cdef void glCompressedTexImage3D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const void *data):
    cglCompressedTexImage3D(target, level, internalformat, width, height, depth, border, imageSize, data)

cdef void glLoadTransposeMatrixf(const GLfloat *m):
    cglLoadTransposeMatrixf(m)

cdef void glMultiTexCoord2s(GLenum target, GLshort s, GLshort t):
    cglMultiTexCoord2s(target, s, t)

cdef void glMultiTexCoord2d(GLenum target, GLdouble s, GLdouble t):
    cglMultiTexCoord2d(target, s, t)

cdef void glMultiTexCoord1sv(GLenum target, const GLshort *v):
    cglMultiTexCoord1sv(target, v)

cdef void glMultiTexCoord3dv(GLenum target, const GLdouble *v):
    cglMultiTexCoord3dv(target, v)

cdef void glMultiTexCoord3f(GLenum target, GLfloat s, GLfloat t, GLfloat r):
    cglMultiTexCoord3f(target, s, t, r)

cdef void glClientActiveTexture(GLenum texture):
    cglClientActiveTexture(texture)

cdef void glSampleCoverage(GLfloat value, GLboolean invert):
    cglSampleCoverage(value, invert)

cdef void glMultiTexCoord3sv(GLenum target, const GLshort *v):
    cglMultiTexCoord3sv(target, v)

cdef void glMultiTexCoord4dv(GLenum target, const GLdouble *v):
    cglMultiTexCoord4dv(target, v)

cdef void glMultiTexCoord2i(GLenum target, GLint s, GLint t):
    cglMultiTexCoord2i(target, s, t)

cdef void glMultiTexCoord3d(GLenum target, GLdouble s, GLdouble t, GLdouble r):
    cglMultiTexCoord3d(target, s, t, r)

cdef void glCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void *data):
    cglCompressedTexImage2D(target, level, internalformat, width, height, border, imageSize, data)

cdef void glMultiTexCoord2fv(GLenum target, const GLfloat *v):
    cglMultiTexCoord2fv(target, v)

cdef void glMultiTexCoord2iv(GLenum target, const GLint *v):
    cglMultiTexCoord2iv(target, v)

cdef void glMultiTexCoord2dv(GLenum target, const GLdouble *v):
    cglMultiTexCoord2dv(target, v)

cdef void glMultiTexCoord1i(GLenum target, GLint s):
    cglMultiTexCoord1i(target, s)
