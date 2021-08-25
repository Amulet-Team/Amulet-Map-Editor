# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_TESS_EVALUATION_SHADER_INVOCATIONS = 0x82F2
cdef GLenum GL_MAX_TEXTURE_MAX_ANISOTROPY = 0x84FF
cdef GLenum GL_PRIMITIVES_SUBMITTED = 0x82EF
cdef GLenum GL_NONE = 0
cdef GLenum GL_SPIR_V_EXTENSIONS = 0x9553
cdef GLenum GL_TEXTURE_MAX_ANISOTROPY = 0x84FE
cdef GLenum GL_TRANSFORM_FEEDBACK_STREAM_OVERFLOW = 0x82ED
cdef GLenum GL_GEOMETRY_SHADER_INVOCATIONS = 0x887F
cdef GLenum GL_CONTEXT_RELEASE_BEHAVIOR = 0x82FB
cdef GLenum GL_VERTEX_SHADER_INVOCATIONS = 0x82F0
cdef GLenum GL_CONTEXT_FLAG_NO_ERROR_BIT = 0x00000008
cdef GLenum GL_VERTICES_SUBMITTED = 0x82EE
cdef GLenum GL_SPIR_V_BINARY = 0x9552
cdef GLenum GL_CLIPPING_OUTPUT_PRIMITIVES = 0x82F7
cdef GLenum GL_NUM_SPIR_V_EXTENSIONS = 0x9554
cdef GLenum GL_POLYGON_OFFSET_CLAMP = 0x8E1B
cdef GLenum GL_COMPUTE_SHADER_INVOCATIONS = 0x82F5
cdef GLenum GL_SHADER_BINARY_FORMAT_SPIR_V = 0x9551
cdef GLenum GL_PARAMETER_BUFFER = 0x80EE
cdef GLenum GL_GEOMETRY_SHADER_PRIMITIVES_EMITTED = 0x82F3
cdef GLenum GL_FRAGMENT_SHADER_INVOCATIONS = 0x82F4
cdef GLenum GL_PARAMETER_BUFFER_BINDING = 0x80EF
cdef GLenum GL_CLIPPING_INPUT_PRIMITIVES = 0x82F6
cdef GLenum GL_TRANSFORM_FEEDBACK_OVERFLOW = 0x82EC
cdef GLenum GL_TESS_CONTROL_SHADER_PATCHES = 0x82F1
cdef GLenum GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH = 0x82FC

ctypedef void (*PFNGLSPECIALIZESHADERPROC)(GLuint shader, const GLchar *pEntryPoint, GLuint numSpecializationConstants, const GLuint *pConstantIndex, const GLuint *pConstantValue)
ctypedef void (*PFNGLPOLYGONOFFSETCLAMPPROC)(GLfloat factor, GLfloat units, GLfloat clamp)
ctypedef void (*PFNGLMULTIDRAWARRAYSINDIRECTCOUNTPROC)(GLenum mode, const void *indirect, GLintptr drawcount, GLsizei maxdrawcount, GLsizei stride)
ctypedef void (*PFNGLMULTIDRAWELEMENTSINDIRECTCOUNTPROC)(GLenum mode, GLenum type, const void *indirect, GLintptr drawcount, GLsizei maxdrawcount, GLsizei stride)

cdef PFNGLSPECIALIZESHADERPROC cglSpecializeShader = NULL
cdef PFNGLPOLYGONOFFSETCLAMPPROC cglPolygonOffsetClamp = NULL
cdef PFNGLMULTIDRAWARRAYSINDIRECTCOUNTPROC cglMultiDrawArraysIndirectCount = NULL
cdef PFNGLMULTIDRAWELEMENTSINDIRECTCOUNTPROC cglMultiDrawElementsIndirectCount = NULL


cdef void GetglSpecializeShader(GLuint shader, const GLchar *pEntryPoint, GLuint numSpecializationConstants, const GLuint *pConstantIndex, const GLuint *pConstantValue):
    global cglSpecializeShader
    cglSpecializeShader = <PFNGLSPECIALIZESHADERPROC>getFunction(b"glSpecializeShader")
    cglSpecializeShader(shader, pEntryPoint, numSpecializationConstants, pConstantIndex, pConstantValue)

cdef void GetglPolygonOffsetClamp(GLfloat factor, GLfloat units, GLfloat clamp):
    global cglPolygonOffsetClamp
    cglPolygonOffsetClamp = <PFNGLPOLYGONOFFSETCLAMPPROC>getFunction(b"glPolygonOffsetClamp")
    cglPolygonOffsetClamp(factor, units, clamp)

cdef void GetglMultiDrawArraysIndirectCount(GLenum mode, const void *indirect, GLintptr drawcount, GLsizei maxdrawcount, GLsizei stride):
    global cglMultiDrawArraysIndirectCount
    cglMultiDrawArraysIndirectCount = <PFNGLMULTIDRAWARRAYSINDIRECTCOUNTPROC>getFunction(b"glMultiDrawArraysIndirectCount")
    cglMultiDrawArraysIndirectCount(mode, indirect, drawcount, maxdrawcount, stride)

cdef void GetglMultiDrawElementsIndirectCount(GLenum mode, GLenum type, const void *indirect, GLintptr drawcount, GLsizei maxdrawcount, GLsizei stride):
    global cglMultiDrawElementsIndirectCount
    cglMultiDrawElementsIndirectCount = <PFNGLMULTIDRAWELEMENTSINDIRECTCOUNTPROC>getFunction(b"glMultiDrawElementsIndirectCount")
    cglMultiDrawElementsIndirectCount(mode, type, indirect, drawcount, maxdrawcount, stride)

cglSpecializeShader = GetglSpecializeShader
cglPolygonOffsetClamp = GetglPolygonOffsetClamp
cglMultiDrawArraysIndirectCount = GetglMultiDrawArraysIndirectCount
cglMultiDrawElementsIndirectCount = GetglMultiDrawElementsIndirectCount


cdef void glSpecializeShader(GLuint shader, const GLchar *pEntryPoint, GLuint numSpecializationConstants, const GLuint *pConstantIndex, const GLuint *pConstantValue):
    cglSpecializeShader(shader, pEntryPoint, numSpecializationConstants, pConstantIndex, pConstantValue)

cdef void glPolygonOffsetClamp(GLfloat factor, GLfloat units, GLfloat clamp):
    cglPolygonOffsetClamp(factor, units, clamp)

cdef void glMultiDrawArraysIndirectCount(GLenum mode, const void *indirect, GLintptr drawcount, GLsizei maxdrawcount, GLsizei stride):
    cglMultiDrawArraysIndirectCount(mode, indirect, drawcount, maxdrawcount, stride)

cdef void glMultiDrawElementsIndirectCount(GLenum mode, GLenum type, const void *indirect, GLintptr drawcount, GLsizei maxdrawcount, GLsizei stride):
    cglMultiDrawElementsIndirectCount(mode, type, indirect, drawcount, maxdrawcount, stride)
