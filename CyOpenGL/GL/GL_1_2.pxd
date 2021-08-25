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

cdef GLenum GL_ALIASED_LINE_WIDTH_RANGE
cdef GLenum GL_ALIASED_POINT_SIZE_RANGE
cdef GLenum GL_BGR
cdef GLenum GL_BGRA
cdef GLenum GL_CLAMP_TO_EDGE
cdef GLenum GL_LIGHT_MODEL_COLOR_CONTROL
cdef GLenum GL_MAX_3D_TEXTURE_SIZE
cdef GLenum GL_MAX_ELEMENTS_INDICES
cdef GLenum GL_MAX_ELEMENTS_VERTICES
cdef GLenum GL_PACK_IMAGE_HEIGHT
cdef GLenum GL_PACK_SKIP_IMAGES
cdef GLenum GL_PROXY_TEXTURE_3D
cdef GLenum GL_RESCALE_NORMAL
cdef GLenum GL_SEPARATE_SPECULAR_COLOR
cdef GLenum GL_SINGLE_COLOR
cdef GLenum GL_SMOOTH_LINE_WIDTH_GRANULARITY
cdef GLenum GL_SMOOTH_LINE_WIDTH_RANGE
cdef GLenum GL_SMOOTH_POINT_SIZE_GRANULARITY
cdef GLenum GL_SMOOTH_POINT_SIZE_RANGE
cdef GLenum GL_TEXTURE_3D
cdef GLenum GL_TEXTURE_BASE_LEVEL
cdef GLenum GL_TEXTURE_BINDING_3D
cdef GLenum GL_TEXTURE_DEPTH
cdef GLenum GL_TEXTURE_MAX_LEVEL
cdef GLenum GL_TEXTURE_MAX_LOD
cdef GLenum GL_TEXTURE_MIN_LOD
cdef GLenum GL_TEXTURE_WRAP_R
cdef GLenum GL_UNPACK_IMAGE_HEIGHT
cdef GLenum GL_UNPACK_SKIP_IMAGES
cdef GLenum GL_UNSIGNED_BYTE_2_3_3_REV
cdef GLenum GL_UNSIGNED_BYTE_3_3_2
cdef GLenum GL_UNSIGNED_INT_10_10_10_2
cdef GLenum GL_UNSIGNED_INT_2_10_10_10_REV
cdef GLenum GL_UNSIGNED_INT_8_8_8_8
cdef GLenum GL_UNSIGNED_INT_8_8_8_8_REV
cdef GLenum GL_UNSIGNED_SHORT_1_5_5_5_REV
cdef GLenum GL_UNSIGNED_SHORT_4_4_4_4
cdef GLenum GL_UNSIGNED_SHORT_4_4_4_4_REV
cdef GLenum GL_UNSIGNED_SHORT_5_5_5_1
cdef GLenum GL_UNSIGNED_SHORT_5_6_5
cdef GLenum GL_UNSIGNED_SHORT_5_6_5_REV
cdef void glCopyTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height)
cdef void glDrawRangeElements(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices)
cdef void glTexImage3D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLsizei depth, GLint border, GLenum format, GLenum type, const void *pixels)
cdef void glTexSubImage3D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels)
