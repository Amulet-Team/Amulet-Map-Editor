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

cdef GLenum GL_BLEND_COLOR
cdef GLenum GL_BLEND_DST_ALPHA
cdef GLenum GL_BLEND_DST_RGB
cdef GLenum GL_BLEND_EQUATION
cdef GLenum GL_BLEND_SRC_ALPHA
cdef GLenum GL_BLEND_SRC_RGB
cdef GLenum GL_COLOR_SUM
cdef GLenum GL_COMPARE_R_TO_TEXTURE
cdef GLenum GL_CONSTANT_ALPHA
cdef GLenum GL_CONSTANT_COLOR
cdef GLenum GL_CURRENT_FOG_COORDINATE
cdef GLenum GL_CURRENT_SECONDARY_COLOR
cdef GLenum GL_DECR_WRAP
cdef GLenum GL_DEPTH_COMPONENT16
cdef GLenum GL_DEPTH_COMPONENT24
cdef GLenum GL_DEPTH_COMPONENT32
cdef GLenum GL_DEPTH_TEXTURE_MODE
cdef GLenum GL_FOG_COORDINATE
cdef GLenum GL_FOG_COORDINATE_ARRAY
cdef GLenum GL_FOG_COORDINATE_ARRAY_POINTER
cdef GLenum GL_FOG_COORDINATE_ARRAY_STRIDE
cdef GLenum GL_FOG_COORDINATE_ARRAY_TYPE
cdef GLenum GL_FOG_COORDINATE_SOURCE
cdef GLenum GL_FRAGMENT_DEPTH
cdef GLenum GL_FUNC_ADD
cdef GLenum GL_FUNC_REVERSE_SUBTRACT
cdef GLenum GL_FUNC_SUBTRACT
cdef GLenum GL_GENERATE_MIPMAP
cdef GLenum GL_GENERATE_MIPMAP_HINT
cdef GLenum GL_INCR_WRAP
cdef GLenum GL_MAX
cdef GLenum GL_MAX_TEXTURE_LOD_BIAS
cdef GLenum GL_MIN
cdef GLenum GL_MIRRORED_REPEAT
cdef GLenum GL_ONE_MINUS_CONSTANT_ALPHA
cdef GLenum GL_ONE_MINUS_CONSTANT_COLOR
cdef GLenum GL_POINT_DISTANCE_ATTENUATION
cdef GLenum GL_POINT_FADE_THRESHOLD_SIZE
cdef GLenum GL_POINT_SIZE_MAX
cdef GLenum GL_POINT_SIZE_MIN
cdef GLenum GL_SECONDARY_COLOR_ARRAY
cdef GLenum GL_SECONDARY_COLOR_ARRAY_POINTER
cdef GLenum GL_SECONDARY_COLOR_ARRAY_SIZE
cdef GLenum GL_SECONDARY_COLOR_ARRAY_STRIDE
cdef GLenum GL_SECONDARY_COLOR_ARRAY_TYPE
cdef GLenum GL_TEXTURE_COMPARE_FUNC
cdef GLenum GL_TEXTURE_COMPARE_MODE
cdef GLenum GL_TEXTURE_DEPTH_SIZE
cdef GLenum GL_TEXTURE_FILTER_CONTROL
cdef GLenum GL_TEXTURE_LOD_BIAS
cdef void glBlendColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
cdef void glBlendEquation(GLenum mode)
cdef void glBlendFuncSeparate(GLenum sfactorRGB, GLenum dfactorRGB, GLenum sfactorAlpha, GLenum dfactorAlpha)
cdef void glFogCoordPointer(GLenum type, GLsizei stride, const void *pointer)
cdef void glFogCoordd(GLdouble coord)
cdef void glFogCoorddv(const GLdouble *coord)
cdef void glFogCoordf(GLfloat coord)
cdef void glFogCoordfv(const GLfloat *coord)
cdef void glMultiDrawArrays(GLenum mode, const GLint *first, const GLsizei *count, GLsizei drawcount)
cdef void glMultiDrawElements(GLenum mode, const GLsizei *count, GLenum type, const void **indices, GLsizei drawcount)
cdef void glPointParameterf(GLenum pname, GLfloat param)
cdef void glPointParameterfv(GLenum pname, const GLfloat *params)
cdef void glPointParameteri(GLenum pname, GLint param)
cdef void glPointParameteriv(GLenum pname, const GLint *params)
cdef void glSecondaryColor3b(GLbyte red, GLbyte green, GLbyte blue)
cdef void glSecondaryColor3bv(const GLbyte *v)
cdef void glSecondaryColor3d(GLdouble red, GLdouble green, GLdouble blue)
cdef void glSecondaryColor3dv(const GLdouble *v)
cdef void glSecondaryColor3f(GLfloat red, GLfloat green, GLfloat blue)
cdef void glSecondaryColor3fv(const GLfloat *v)
cdef void glSecondaryColor3i(GLint red, GLint green, GLint blue)
cdef void glSecondaryColor3iv(const GLint *v)
cdef void glSecondaryColor3s(GLshort red, GLshort green, GLshort blue)
cdef void glSecondaryColor3sv(const GLshort *v)
cdef void glSecondaryColor3ub(GLubyte red, GLubyte green, GLubyte blue)
cdef void glSecondaryColor3ubv(const GLubyte *v)
cdef void glSecondaryColor3ui(GLuint red, GLuint green, GLuint blue)
cdef void glSecondaryColor3uiv(const GLuint *v)
cdef void glSecondaryColor3us(GLushort red, GLushort green, GLushort blue)
cdef void glSecondaryColor3usv(const GLushort *v)
cdef void glSecondaryColorPointer(GLint size, GLenum type, GLsizei stride, const void *pointer)
cdef void glWindowPos2d(GLdouble x, GLdouble y)
cdef void glWindowPos2dv(const GLdouble *v)
cdef void glWindowPos2f(GLfloat x, GLfloat y)
cdef void glWindowPos2fv(const GLfloat *v)
cdef void glWindowPos2i(GLint x, GLint y)
cdef void glWindowPos2iv(const GLint *v)
cdef void glWindowPos2s(GLshort x, GLshort y)
cdef void glWindowPos2sv(const GLshort *v)
cdef void glWindowPos3d(GLdouble x, GLdouble y, GLdouble z)
cdef void glWindowPos3dv(const GLdouble *v)
cdef void glWindowPos3f(GLfloat x, GLfloat y, GLfloat z)
cdef void glWindowPos3fv(const GLfloat *v)
cdef void glWindowPos3i(GLint x, GLint y, GLint z)
cdef void glWindowPos3iv(const GLint *v)
cdef void glWindowPos3s(GLshort x, GLshort y, GLshort z)
cdef void glWindowPos3sv(const GLshort *v)
