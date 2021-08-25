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
cdef void glCompressedTexImage1D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLint border, GLsizei imageSize, const void *data)
cdef void glGetCompressedTexImage(GLenum target, GLint level, void *img)
cdef void glMultTransposeMatrixf(const GLfloat *m)
cdef void glMultiTexCoord4s(GLenum target, GLshort s, GLshort t, GLshort r, GLshort q)
cdef void glMultiTexCoord4sv(GLenum target, const GLshort *v)
cdef void glMultiTexCoord1f(GLenum target, GLfloat s)
cdef void glMultiTexCoord3s(GLenum target, GLshort s, GLshort t, GLshort r)
cdef void glCompressedTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data)
cdef void glMultiTexCoord3fv(GLenum target, const GLfloat *v)
cdef void glMultiTexCoord4i(GLenum target, GLint s, GLint t, GLint r, GLint q)
cdef void glMultiTexCoord2f(GLenum target, GLfloat s, GLfloat t)
cdef void glMultiTexCoord3iv(GLenum target, const GLint *v)
cdef void glActiveTexture(GLenum texture)
cdef void glMultiTexCoord4d(GLenum target, GLdouble s, GLdouble t, GLdouble r, GLdouble q)
cdef void glMultiTexCoord4f(GLenum target, GLfloat s, GLfloat t, GLfloat r, GLfloat q)
cdef void glMultiTexCoord1fv(GLenum target, const GLfloat *v)
cdef void glMultiTexCoord1s(GLenum target, GLshort s)
cdef void glMultiTexCoord4fv(GLenum target, const GLfloat *v)
cdef void glLoadTransposeMatrixd(const GLdouble *m)
cdef void glMultiTexCoord2sv(GLenum target, const GLshort *v)
cdef void glCompressedTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data)
cdef void glMultiTexCoord1dv(GLenum target, const GLdouble *v)
cdef void glMultiTexCoord4iv(GLenum target, const GLint *v)
cdef void glMultiTexCoord1d(GLenum target, GLdouble s)
cdef void glCompressedTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data)
cdef void glMultiTexCoord1iv(GLenum target, const GLint *v)
cdef void glMultTransposeMatrixd(const GLdouble *m)
cdef void glMultiTexCoord3i(GLenum target, GLint s, GLint t, GLint r)
cdef void glCompressedTexImage3D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLsizei imageSize, const void *data)
cdef void glLoadTransposeMatrixf(const GLfloat *m)
cdef void glMultiTexCoord2s(GLenum target, GLshort s, GLshort t)
cdef void glMultiTexCoord2d(GLenum target, GLdouble s, GLdouble t)
cdef void glMultiTexCoord1sv(GLenum target, const GLshort *v)
cdef void glMultiTexCoord3dv(GLenum target, const GLdouble *v)
cdef void glMultiTexCoord3f(GLenum target, GLfloat s, GLfloat t, GLfloat r)
cdef void glClientActiveTexture(GLenum texture)
cdef void glSampleCoverage(GLfloat value, GLboolean invert)
cdef void glMultiTexCoord3sv(GLenum target, const GLshort *v)
cdef void glMultiTexCoord4dv(GLenum target, const GLdouble *v)
cdef void glMultiTexCoord2i(GLenum target, GLint s, GLint t)
cdef void glMultiTexCoord3d(GLenum target, GLdouble s, GLdouble t, GLdouble r)
cdef void glCompressedTexImage2D(GLenum target, GLint level, GLenum internalformat, GLsizei width, GLsizei height, GLint border, GLsizei imageSize, const void *data)
cdef void glMultiTexCoord2fv(GLenum target, const GLfloat *v)
cdef void glMultiTexCoord2iv(GLenum target, const GLint *v)
cdef void glMultiTexCoord2dv(GLenum target, const GLdouble *v)
cdef void glMultiTexCoord1i(GLenum target, GLint s)
