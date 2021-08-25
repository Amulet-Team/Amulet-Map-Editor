ctypedef unsigned int GLenum
ctypedef unsigned char GLboolean
ctypedef unsigned int GLbitfield
ctypedef void GLvoid
ctypedef signed char GLbyte
ctypedef short GLshort
ctypedef int GLint
ctypedef int GLclampx
ctypedef unsigned char GLubyte
ctypedef unsigned short GLushort
ctypedef unsigned int GLuint
ctypedef int GLsizei
ctypedef float GLfloat
ctypedef float GLclampf
ctypedef double GLdouble
ctypedef double GLclampd
ctypedef void *GLeglClientBufferEXT
ctypedef void *GLeglImageOES
ctypedef char GLchar
ctypedef char GLcharARB
ctypedef int GLhandleARB
ctypedef unsigned short GLhalfARB
ctypedef unsigned short GLhalf
ctypedef GLint GLfixed
ctypedef int * GLintptr
ctypedef int GLsizeiptr
ctypedef int GLint64
ctypedef int GLuint64
ctypedef ptrdiff_t GLintptrARB
ctypedef ptrdiff_t GLsizeiptrARB
ctypedef int GLint64EXT
ctypedef int GLuint64EXT
ctypedef int *GLsync
ctypedef void ( *GLDEBUGPROC)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,const void *userParam)
ctypedef void ( *GLDEBUGPROCARB)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,const void *userParam)
ctypedef void ( *GLDEBUGPROCKHR)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,const void *userParam)
ctypedef void ( *GLDEBUGPROCAMD)(GLuint id,GLenum category,GLenum severity,GLsizei length,const GLchar *message,void *userParam)
ctypedef unsigned short GLhalfNV
ctypedef GLintptr GLvdpauSurfaceNV
ctypedef void ( *GLVULKANPROCNV)()

cdef GLenum GL_ACTIVE_TEXTURE
cdef GLenum GL_ADD_SIGNED
cdef GLenum GL_CLAMP_TO_BORDER
cdef GLenum GL_CLIENT_ACTIVE_TEXTURE
cdef GLenum GL_COMBINE
cdef GLenum GL_COMBINE_ALPHA
cdef GLenum GL_COMBINE_RGB
cdef GLenum GL_COMPRESSED_ALPHA
cdef GLenum GL_COMPRESSED_INTENSITY
cdef GLenum GL_COMPRESSED_LUMINANCE
cdef GLenum GL_COMPRESSED_LUMINANCE_ALPHA
cdef GLenum GL_COMPRESSED_RGB
cdef GLenum GL_COMPRESSED_RGBA
cdef GLenum GL_COMPRESSED_TEXTURE_FORMATS
cdef GLenum GL_CONSTANT
cdef GLenum GL_DOT3_RGB
cdef GLenum GL_DOT3_RGBA
cdef GLenum GL_INTERPOLATE
cdef GLenum GL_MAX_CUBE_MAP_TEXTURE_SIZE
cdef GLenum GL_MAX_TEXTURE_UNITS
cdef GLenum GL_MULTISAMPLE
cdef GLenum GL_MULTISAMPLE_BIT
cdef GLenum GL_NORMAL_MAP
cdef GLenum GL_NUM_COMPRESSED_TEXTURE_FORMATS
cdef GLenum GL_OPERAND0_ALPHA
cdef GLenum GL_OPERAND0_RGB
cdef GLenum GL_OPERAND1_ALPHA
cdef GLenum GL_OPERAND1_RGB
cdef GLenum GL_OPERAND2_ALPHA
cdef GLenum GL_OPERAND2_RGB
cdef GLenum GL_PREVIOUS
cdef GLenum GL_PRIMARY_COLOR
cdef GLenum GL_PROXY_TEXTURE_CUBE_MAP
cdef GLenum GL_REFLECTION_MAP
cdef GLenum GL_RGB_SCALE
cdef GLenum GL_SAMPLES
cdef GLenum GL_SAMPLE_ALPHA_TO_COVERAGE
cdef GLenum GL_SAMPLE_ALPHA_TO_ONE
cdef GLenum GL_SAMPLE_BUFFERS
cdef GLenum GL_SAMPLE_COVERAGE
cdef GLenum GL_SAMPLE_COVERAGE_INVERT
cdef GLenum GL_SAMPLE_COVERAGE_VALUE
cdef GLenum GL_SOURCE0_ALPHA
cdef GLenum GL_SOURCE0_RGB
cdef GLenum GL_SOURCE1_ALPHA
cdef GLenum GL_SOURCE1_RGB
cdef GLenum GL_SOURCE2_ALPHA
cdef GLenum GL_SOURCE2_RGB
cdef GLenum GL_SUBTRACT
cdef GLenum GL_TEXTURE0
cdef GLenum GL_TEXTURE1
cdef GLenum GL_TEXTURE10
cdef GLenum GL_TEXTURE11
cdef GLenum GL_TEXTURE12
cdef GLenum GL_TEXTURE13
cdef GLenum GL_TEXTURE14
cdef GLenum GL_TEXTURE15
cdef GLenum GL_TEXTURE16
cdef GLenum GL_TEXTURE17
cdef GLenum GL_TEXTURE18
cdef GLenum GL_TEXTURE19
cdef GLenum GL_TEXTURE2
cdef GLenum GL_TEXTURE20
cdef GLenum GL_TEXTURE21
cdef GLenum GL_TEXTURE22
cdef GLenum GL_TEXTURE23
cdef GLenum GL_TEXTURE24
cdef GLenum GL_TEXTURE25
cdef GLenum GL_TEXTURE26
cdef GLenum GL_TEXTURE27
cdef GLenum GL_TEXTURE28
cdef GLenum GL_TEXTURE29
cdef GLenum GL_TEXTURE3
cdef GLenum GL_TEXTURE30
cdef GLenum GL_TEXTURE31
cdef GLenum GL_TEXTURE4
cdef GLenum GL_TEXTURE5
cdef GLenum GL_TEXTURE6
cdef GLenum GL_TEXTURE7
cdef GLenum GL_TEXTURE8
cdef GLenum GL_TEXTURE9
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP
cdef GLenum GL_TEXTURE_COMPRESSED
cdef GLenum GL_TEXTURE_COMPRESSED_IMAGE_SIZE
cdef GLenum GL_TEXTURE_COMPRESSION_HINT
cdef GLenum GL_TEXTURE_CUBE_MAP
cdef GLenum GL_TEXTURE_CUBE_MAP_NEGATIVE_X
cdef GLenum GL_TEXTURE_CUBE_MAP_NEGATIVE_Y
cdef GLenum GL_TEXTURE_CUBE_MAP_NEGATIVE_Z
cdef GLenum GL_TEXTURE_CUBE_MAP_POSITIVE_X
cdef GLenum GL_TEXTURE_CUBE_MAP_POSITIVE_Y
cdef GLenum GL_TEXTURE_CUBE_MAP_POSITIVE_Z
cdef GLenum GL_TRANSPOSE_COLOR_MATRIX
cdef GLenum GL_TRANSPOSE_MODELVIEW_MATRIX
cdef GLenum GL_TRANSPOSE_PROJECTION_MATRIX
cdef GLenum GL_TRANSPOSE_TEXTURE_MATRIX
cdef void glActiveTexture(GLenum texture)
cdef void glClientActiveTexture(GLenum texture)
cdef void glCompressedTexImage1D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei imageSize, const void *data)
cdef void glCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void *data)
cdef void glCompressedTexImage3D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const void *data)
cdef void glCompressedTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data)
cdef void glCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data)
cdef void glCompressedTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data)
cdef void glGetCompressedTexImage(GLenum target, GLint level, void *img)
cdef void glLoadTransposeMatrixd(const GLdouble *m)
cdef void glLoadTransposeMatrixf(const GLfloat *m)
cdef void glMultTransposeMatrixd(const GLdouble *m)
cdef void glMultTransposeMatrixf(const GLfloat *m)
cdef void glMultiTexCoord1d(GLenum target, GLdouble s)
cdef void glMultiTexCoord1dv(GLenum target, const GLdouble *v)
cdef void glMultiTexCoord1f(GLenum target, GLfloat s)
cdef void glMultiTexCoord1fv(GLenum target, const GLfloat *v)
cdef void glMultiTexCoord1i(GLenum target, GLint s)
cdef void glMultiTexCoord1iv(GLenum target, const GLint *v)
cdef void glMultiTexCoord1s(GLenum target, GLshort s)
cdef void glMultiTexCoord1sv(GLenum target, const GLshort *v)
cdef void glMultiTexCoord2d(GLenum target, GLdouble s, GLdouble t)
cdef void glMultiTexCoord2dv(GLenum target, const GLdouble *v)
cdef void glMultiTexCoord2f(GLenum target, GLfloat s, GLfloat t)
cdef void glMultiTexCoord2fv(GLenum target, const GLfloat *v)
cdef void glMultiTexCoord2i(GLenum target, GLint s, GLint t)
cdef void glMultiTexCoord2iv(GLenum target, const GLint *v)
cdef void glMultiTexCoord2s(GLenum target, GLshort s, GLshort t)
cdef void glMultiTexCoord2sv(GLenum target, const GLshort *v)
cdef void glMultiTexCoord3d(GLenum target, GLdouble s, GLdouble t, GLdouble r)
cdef void glMultiTexCoord3dv(GLenum target, const GLdouble *v)
cdef void glMultiTexCoord3f(GLenum target, GLfloat s, GLfloat t, GLfloat r)
cdef void glMultiTexCoord3fv(GLenum target, const GLfloat *v)
cdef void glMultiTexCoord3i(GLenum target, GLint s, GLint t, GLint r)
cdef void glMultiTexCoord3iv(GLenum target, const GLint *v)
cdef void glMultiTexCoord3s(GLenum target, GLshort s, GLshort t, GLshort r)
cdef void glMultiTexCoord3sv(GLenum target, const GLshort *v)
cdef void glMultiTexCoord4d(GLenum target, GLdouble s, GLdouble t, GLdouble r, GLdouble q)
cdef void glMultiTexCoord4dv(GLenum target, const GLdouble *v)
cdef void glMultiTexCoord4f(GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q)
cdef void glMultiTexCoord4fv(GLenum target, const GLfloat *v)
cdef void glMultiTexCoord4i(GLenum target, GLint s, GLint t, GLint r, GLint q)
cdef void glMultiTexCoord4iv(GLenum target, const GLint *v)
cdef void glMultiTexCoord4s(GLenum target, GLshort s, GLshort t, GLshort r, GLshort q)
cdef void glMultiTexCoord4sv(GLenum target, const GLshort *v)
cdef void glSampleCoverage(GLfloat value, GLboolean invert)
