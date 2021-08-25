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

cdef GLenum GL_CLIPPING_INPUT_PRIMITIVES
cdef GLenum GL_CLIPPING_OUTPUT_PRIMITIVES
cdef GLenum GL_COMPUTE_SHADER_INVOCATIONS
cdef GLenum GL_CONTEXT_FLAG_NO_ERROR_BIT
cdef GLenum GL_CONTEXT_RELEASE_BEHAVIOR
cdef GLenum GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH
cdef GLenum GL_FRAGMENT_SHADER_INVOCATIONS
cdef GLenum GL_GEOMETRY_SHADER_INVOCATIONS
cdef GLenum GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED
cdef GLenum GL_MAX_TEXTURE_MAX_ANISOTROPY
cdef GLenum GL_NONE
cdef GLenum GL_NUM_SPIR_V_EXTENSIONS
cdef GLenum GL_PARAMETER_BUFFER
cdef GLenum GL_PARAMETER_BUFFER_BINDING
cdef GLenum GL_POLYGON_OFFSET_CLAMP
cdef GLenum GL_PRIMITIVES_SUBMITTED
cdef GLenum GL_SHADER_BINARY_FORMAT_SPIR_V
cdef GLenum GL_SPIR_V_BINARY
cdef GLenum GL_SPIR_V_EXTENSIONS
cdef GLenum GL_TESS_CONTROL_SHADER_PATCHES
cdef GLenum GL_TESS_EVALUATION_SHADER_INVOCATIONS
cdef GLenum GL_TEXTURE_MAX_ANISOTROPY
cdef GLenum GL_TRANSFORM_FEEDBACK_OVERFLOW
cdef GLenum GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW
cdef GLenum GL_VERTEX_SHADER_INVOCATIONS
cdef GLenum GL_VERTICES_SUBMITTED
cdef void glMultiDrawArraysIndirectCount(GLenum mode, const void *indirect, GLintptr drawcount, GLsizei maxdrawcount, GLsizei stride)
cdef void glMultiDrawElementsIndirectCount(GLenum mode, GLenum type, const void *indirect, GLintptr drawcount, GLsizei maxdrawcount, GLsizei stride)
cdef void glPolygonOffsetClamp(GLfloat factor, GLfloat units, GLfloat clamp)
cdef void glSpecializeShader(GLuint shader, const GLchar *pEntryPoint, GLuint numSpecializationConstants, const GLuint *pConstantIndex, const GLuint *pConstantValue)
