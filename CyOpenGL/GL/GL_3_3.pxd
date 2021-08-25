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

cdef GLenum GL_ANY_SAMPLES_PASSED
cdef GLenum GL_INT_2_10_10_10_REV
cdef GLenum GL_MAX_DUAL_SOURCE_DRAW_BUFFERS
cdef GLenum GL_ONE_MINUS_SRC1_ALPHA
cdef GLenum GL_ONE_MINUS_SRC1_COLOR
cdef GLenum GL_RGB10_A2UI
cdef GLenum GL_SAMPLER_BINDING
cdef GLenum GL_SRC1_COLOR
cdef GLenum GL_TEXTURE_SWIZZLE_A
cdef GLenum GL_TEXTURE_SWIZZLE_B
cdef GLenum GL_TEXTURE_SWIZZLE_G
cdef GLenum GL_TEXTURE_SWIZZLE_R
cdef GLenum GL_TEXTURE_SWIZZLE_RGBA
cdef GLenum GL_TIMESTAMP
cdef GLenum GL_TIME_ELAPSED
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_DIVISOR
cdef void glBindFragDataLocationIndexed(GLuint program, GLuint colorNumber, GLuint index, const GLchar *name)
cdef void glBindSampler(GLuint unit, GLuint sampler)
cdef void glColorP3ui(GLenum type, GLuint color)
cdef void glColorP3uiv(GLenum type, const GLuint *color)
cdef void glColorP4ui(GLenum type, GLuint color)
cdef void glColorP4uiv(GLenum type, const GLuint *color)
cdef void glDeleteSamplers(GLsizei count, const GLuint *samplers)
cdef void glGenSamplers(GLsizei count, GLuint *samplers)
cdef GLint glGetFragDataIndex(GLuint program, const GLchar *name)
cdef void glGetQueryObjecti64v(GLuint id, GLenum pname, GLint64 *params)
cdef void glGetQueryObjectui64v(GLuint id, GLenum pname, GLuint64 *params)
cdef void glGetSamplerParameterIiv(GLuint sampler, GLenum pname, GLint *params)
cdef void glGetSamplerParameterIuiv(GLuint sampler, GLenum pname, GLuint *params)
cdef void glGetSamplerParameterfv(GLuint sampler, GLenum pname, GLfloat *params)
cdef void glGetSamplerParameteriv(GLuint sampler, GLenum pname, GLint *params)
cdef GLboolean glIsSampler(GLuint sampler)
cdef void glMultiTexCoordP1ui(GLenum texture, GLenum type, GLuint coords)
cdef void glMultiTexCoordP1uiv(GLenum texture, GLenum type, const GLuint *coords)
cdef void glMultiTexCoordP2ui(GLenum texture, GLenum type, GLuint coords)
cdef void glMultiTexCoordP2uiv(GLenum texture, GLenum type, const GLuint *coords)
cdef void glMultiTexCoordP3ui(GLenum texture, GLenum type, GLuint coords)
cdef void glMultiTexCoordP3uiv(GLenum texture, GLenum type, const GLuint *coords)
cdef void glMultiTexCoordP4ui(GLenum texture, GLenum type, GLuint coords)
cdef void glMultiTexCoordP4uiv(GLenum texture, GLenum type, const GLuint *coords)
cdef void glNormalP3ui(GLenum type, GLuint coords)
cdef void glNormalP3uiv(GLenum type, const GLuint *coords)
cdef void glQueryCounter(GLuint id, GLenum target)
cdef void glSamplerParameterIiv(GLuint sampler, GLenum pname, const GLint *param)
cdef void glSamplerParameterIuiv(GLuint sampler, GLenum pname, const GLuint *param)
cdef void glSamplerParameterf(GLuint sampler, GLenum pname, GLfloat param)
cdef void glSamplerParameterfv(GLuint sampler, GLenum pname, const GLfloat *param)
cdef void glSamplerParameteri(GLuint sampler, GLenum pname, GLint param)
cdef void glSamplerParameteriv(GLuint sampler, GLenum pname, const GLint *param)
cdef void glSecondaryColorP3ui(GLenum type, GLuint color)
cdef void glSecondaryColorP3uiv(GLenum type, const GLuint *color)
cdef void glTexCoordP1ui(GLenum type, GLuint coords)
cdef void glTexCoordP1uiv(GLenum type, const GLuint *coords)
cdef void glTexCoordP2ui(GLenum type, GLuint coords)
cdef void glTexCoordP2uiv(GLenum type, const GLuint *coords)
cdef void glTexCoordP3ui(GLenum type, GLuint coords)
cdef void glTexCoordP3uiv(GLenum type, const GLuint *coords)
cdef void glTexCoordP4ui(GLenum type, GLuint coords)
cdef void glTexCoordP4uiv(GLenum type, const GLuint *coords)
cdef void glVertexAttribDivisor(GLuint index, GLuint divisor)
cdef void glVertexAttribP1ui(GLuint index, GLenum type, GLboolean normalized, GLuint value)
cdef void glVertexAttribP1uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
cdef void glVertexAttribP2ui(GLuint index, GLenum type, GLboolean normalized, GLuint value)
cdef void glVertexAttribP2uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
cdef void glVertexAttribP3ui(GLuint index, GLenum type, GLboolean normalized, GLuint value)
cdef void glVertexAttribP3uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
cdef void glVertexAttribP4ui(GLuint index, GLenum type, GLboolean normalized, GLuint value)
cdef void glVertexAttribP4uiv(GLuint index, GLenum type, GLboolean normalized, const GLuint *value)
cdef void glVertexP2ui(GLenum type, GLuint value)
cdef void glVertexP2uiv(GLenum type, const GLuint *value)
cdef void glVertexP3ui(GLenum type, GLuint value)
cdef void glVertexP3uiv(GLenum type, const GLuint *value)
cdef void glVertexP4ui(GLenum type, GLuint value)
cdef void glVertexP4uiv(GLenum type, const GLuint *value)
