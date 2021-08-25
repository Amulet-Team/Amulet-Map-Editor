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

cdef GLenum GL_ALPHA12
cdef GLenum GL_ALPHA16
cdef GLenum GL_ALPHA4
cdef GLenum GL_ALPHA8
cdef GLenum GL_C3F_V3F
cdef GLenum GL_C4F_N3F_V3F
cdef GLenum GL_C4UB_V2F
cdef GLenum GL_C4UB_V3F
cdef GLenum GL_CLIENT_ALL_ATTRIB_BITS
cdef GLenum GL_CLIENT_ATTRIB_STACK_DEPTH
cdef GLenum GL_CLIENT_PIXEL_STORE_BIT
cdef GLenum GL_CLIENT_VERTEX_ARRAY_BIT
cdef GLenum GL_COLOR_ARRAY
cdef GLenum GL_COLOR_ARRAY_POINTER
cdef GLenum GL_COLOR_ARRAY_SIZE
cdef GLenum GL_COLOR_ARRAY_STRIDE
cdef GLenum GL_COLOR_ARRAY_TYPE
cdef GLenum GL_COLOR_LOGIC_OP
cdef GLenum GL_DOUBLE
cdef GLenum GL_EDGE_FLAG_ARRAY
cdef GLenum GL_EDGE_FLAG_ARRAY_POINTER
cdef GLenum GL_EDGE_FLAG_ARRAY_STRIDE
cdef GLenum GL_FEEDBACK_BUFFER_POINTER
cdef GLenum GL_FEEDBACK_BUFFER_SIZE
cdef GLenum GL_FEEDBACK_BUFFER_TYPE
cdef GLenum GL_INDEX_ARRAY
cdef GLenum GL_INDEX_ARRAY_POINTER
cdef GLenum GL_INDEX_ARRAY_STRIDE
cdef GLenum GL_INDEX_ARRAY_TYPE
cdef GLenum GL_INDEX_LOGIC_OP
cdef GLenum GL_INTENSITY
cdef GLenum GL_INTENSITY12
cdef GLenum GL_INTENSITY16
cdef GLenum GL_INTENSITY4
cdef GLenum GL_INTENSITY8
cdef GLenum GL_LUMINANCE12
cdef GLenum GL_LUMINANCE12_ALPHA12
cdef GLenum GL_LUMINANCE12_ALPHA4
cdef GLenum GL_LUMINANCE16
cdef GLenum GL_LUMINANCE16_ALPHA16
cdef GLenum GL_LUMINANCE4
cdef GLenum GL_LUMINANCE4_ALPHA4
cdef GLenum GL_LUMINANCE6_ALPHA2
cdef GLenum GL_LUMINANCE8
cdef GLenum GL_LUMINANCE8_ALPHA8
cdef GLenum GL_MAX_CLIENT_ATTRIB_STACK_DEPTH
cdef GLenum GL_N3F_V3F
cdef GLenum GL_NORMAL_ARRAY
cdef GLenum GL_NORMAL_ARRAY_POINTER
cdef GLenum GL_NORMAL_ARRAY_STRIDE
cdef GLenum GL_NORMAL_ARRAY_TYPE
cdef GLenum GL_POLYGON_OFFSET_FACTOR
cdef GLenum GL_POLYGON_OFFSET_FILL
cdef GLenum GL_POLYGON_OFFSET_LINE
cdef GLenum GL_POLYGON_OFFSET_POINT
cdef GLenum GL_POLYGON_OFFSET_UNITS
cdef GLenum GL_PROXY_TEXTURE_1D
cdef GLenum GL_PROXY_TEXTURE_2D
cdef GLenum GL_R3_G3_B2
cdef GLenum GL_RGB10
cdef GLenum GL_RGB10_A2
cdef GLenum GL_RGB12
cdef GLenum GL_RGB16
cdef GLenum GL_RGB4
cdef GLenum GL_RGB5
cdef GLenum GL_RGB5_A1
cdef GLenum GL_RGB8
cdef GLenum GL_RGBA12
cdef GLenum GL_RGBA16
cdef GLenum GL_RGBA2
cdef GLenum GL_RGBA4
cdef GLenum GL_RGBA8
cdef GLenum GL_SELECTION_BUFFER_POINTER
cdef GLenum GL_SELECTION_BUFFER_SIZE
cdef GLenum GL_T2F_C3F_V3F
cdef GLenum GL_T2F_C4F_N3F_V3F
cdef GLenum GL_T2F_C4UB_V3F
cdef GLenum GL_T2F_N3F_V3F
cdef GLenum GL_T2F_V3F
cdef GLenum GL_T4F_C4F_N3F_V4F
cdef GLenum GL_T4F_V4F
cdef GLenum GL_TEXTURE_ALPHA_SIZE
cdef GLenum GL_TEXTURE_BINDING_1D
cdef GLenum GL_TEXTURE_BINDING_2D
cdef GLenum GL_TEXTURE_BLUE_SIZE
cdef GLenum GL_TEXTURE_COORD_ARRAY
cdef GLenum GL_TEXTURE_COORD_ARRAY_POINTER
cdef GLenum GL_TEXTURE_COORD_ARRAY_SIZE
cdef GLenum GL_TEXTURE_COORD_ARRAY_STRIDE
cdef GLenum GL_TEXTURE_COORD_ARRAY_TYPE
cdef GLenum GL_TEXTURE_GREEN_SIZE
cdef GLenum GL_TEXTURE_INTENSITY_SIZE
cdef GLenum GL_TEXTURE_INTERNAL_FORMAT
cdef GLenum GL_TEXTURE_LUMINANCE_SIZE
cdef GLenum GL_TEXTURE_PRIORITY
cdef GLenum GL_TEXTURE_RED_SIZE
cdef GLenum GL_TEXTURE_RESIDENT
cdef GLenum GL_V2F
cdef GLenum GL_V3F
cdef GLenum GL_VERTEX_ARRAY
cdef GLenum GL_VERTEX_ARRAY_POINTER
cdef GLenum GL_VERTEX_ARRAY_SIZE
cdef GLenum GL_VERTEX_ARRAY_STRIDE
cdef GLenum GL_VERTEX_ARRAY_TYPE
cdef GLboolean glAreTexturesResident(GLsizei n, const GLuint *textures, GLboolean *residences)
cdef void glArrayElement(GLint i)
cdef void glBindTexture(GLenum target, GLuint texture)
cdef void glColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer)
cdef void glCopyTexImage1D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLint border)
cdef void glCopyTexImage2D(GLenum target, GLint level, GLenum internalformat, GLint x, GLint y, GLsizei width, GLsizei height, GLint border)
cdef void glCopyTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
cdef void glCopyTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
cdef void glDeleteTextures(GLsizei n, const GLuint *textures)
cdef void glDisableClientState(GLenum array)
cdef void glDrawArrays(GLenum mode, GLint first, GLsizei count)
cdef void glDrawElements(GLenum mode, GLsizei count, GLenum type, const void *indices)
cdef void glEdgeFlagPointer(GLsizei stride, const void *pointer)
cdef void glEnableClientState(GLenum array)
cdef void glGenTextures(GLsizei n, GLuint *textures)
cdef void glGetPointerv(GLenum pname, void **params)
cdef void glIndexPointer(GLenum type, GLsizei stride, const void *pointer)
cdef void glIndexub(GLubyte c)
cdef void glIndexubv(const GLubyte *c)
cdef void glInterleavedArrays(GLenum format, GLsizei stride, const void *pointer)
cdef GLboolean glIsTexture(GLuint texture)
cdef void glNormalPointer(GLenum type, GLsizei stride, const void *pointer)
cdef void glPolygonOffset(GLfloat factor, GLfloat units)
cdef void glPopClientAttrib()
cdef void glPrioritizeTextures(GLsizei n, const GLuint *textures, const GLfloat *priorities)
cdef void glPushClientAttrib(GLbitfield mask)
cdef void glTexCoordPointer(GLint size, GLenum type, GLsizei stride, const void *pointer)
cdef void glTexSubImage1D(GLenum target, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels)
cdef void glTexSubImage2D(GLenum target, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
cdef void glVertexPointer(GLint size, GLenum type, GLsizei stride, const void *pointer)
