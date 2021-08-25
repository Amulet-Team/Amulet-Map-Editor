# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_ALREADY_SIGNALED = 0x911A
cdef GLenum GL_CONDITION_SATISFIED = 0x911C
cdef GLenum GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 0x00000002
cdef GLenum GL_CONTEXT_CORE_PROFILE_BIT = 0x00000001
cdef GLenum GL_CONTEXT_PROFILE_MASK = 0x9126
cdef GLenum GL_DEPTH_CLAMP = 0x864F
cdef GLenum GL_FIRST_VERTEX_CONVENTION = 0x8E4D
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_LAYERED = 0x8DA7
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS = 0x8DA8
cdef GLenum GL_GEOMETRY_INPUT_TYPE = 0x8917
cdef GLenum GL_GEOMETRY_OUTPUT_TYPE = 0x8918
cdef GLenum GL_GEOMETRY_SHADER = 0x8DD9
cdef GLenum GL_GEOMETRY_VERTICES_OUT = 0x8916
cdef GLenum GL_INT_SAMPLER_2D_MULTISAMPLE = 0x9109
cdef GLenum GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910C
cdef GLenum GL_LAST_VERTEX_CONVENTION = 0x8E4E
cdef GLenum GL_LINES_ADJACENCY = 0x000A
cdef GLenum GL_LINE_STRIP_ADJACENCY = 0x000B
cdef GLenum GL_MAX_COLOR_TEXTURE_SAMPLES = 0x910E
cdef GLenum GL_MAX_DEPTH_TEXTURE_SAMPLES = 0x910F
cdef GLenum GL_MAX_FRAGMENT_INPUT_COMPONENTS = 0x9125
cdef GLenum GL_MAX_GEOMETRY_INPUT_COMPONENTS = 0x9123
cdef GLenum GL_MAX_GEOMETRY_OUTPUT_COMPONENTS = 0x9124
cdef GLenum GL_MAX_GEOMETRY_OUTPUT_VERTICES = 0x8DE0
cdef GLenum GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS = 0x8C29
cdef GLenum GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS = 0x8DE1
cdef GLenum GL_MAX_GEOMETRY_UNIFORM_COMPONENTS = 0x8DDF
cdef GLenum GL_MAX_INTEGER_SAMPLES = 0x9110
cdef GLenum GL_MAX_SAMPLE_MASK_WORDS = 0x8E59
cdef GLenum GL_MAX_SERVER_WAIT_TIMEOUT = 0x9111
cdef GLenum GL_MAX_VERTEX_OUTPUT_COMPONENTS = 0x9122
cdef GLenum GL_OBJECT_TYPE = 0x9112
cdef GLenum GL_PROGRAM_POINT_SIZE = 0x8642
cdef GLenum GL_PROVOKING_VERTEX = 0x8E4F
cdef GLenum GL_PROXY_TEXTURE_2D_MULTISAMPLE = 0x9101
cdef GLenum GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9103
cdef GLenum GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION = 0x8E4C
cdef GLenum GL_SAMPLER_2D_MULTISAMPLE = 0x9108
cdef GLenum GL_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910B
cdef GLenum GL_SAMPLE_MASK = 0x8E51
cdef GLenum GL_SAMPLE_MASK_VALUE = 0x8E52
cdef GLenum GL_SAMPLE_POSITION = 0x8E50
cdef GLenum GL_SIGNALED = 0x9119
cdef GLenum GL_SYNC_CONDITION = 0x9113
cdef GLenum GL_SYNC_FENCE = 0x9116
cdef GLenum GL_SYNC_FLAGS = 0x9115
cdef GLenum GL_SYNC_FLUSH_COMMANDS_BIT = 0x00000001
cdef GLenum GL_SYNC_GPU_COMMANDS_COMPLETE = 0x9117
cdef GLenum GL_SYNC_STATUS = 0x9114
cdef GLenum GL_TEXTURE_2D_MULTISAMPLE = 0x9100
cdef GLenum GL_TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9102
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE = 0x9104
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 0x9105
cdef GLenum GL_TEXTURE_CUBE_MAP_SEAMLESS = 0x884F
cdef GLenum GL_TEXTURE_FIXED_SAMPLE_LOCATIONS = 0x9107
cdef GLenum GL_TEXTURE_SAMPLES = 0x9106
cdef GLenum GL_TIMEOUT_EXPIRED = 0x911B
cdef GLenum GL_TIMEOUT_IGNORED = 0xFFFFFFFFFFFFFFFF
cdef GLenum GL_TRIANGLES_ADJACENCY = 0x000C
cdef GLenum GL_TRIANGLE_STRIP_ADJACENCY = 0x000D
cdef GLenum GL_UNSIGNALED = 0x9118
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 0x910A
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910D
cdef GLenum GL_WAIT_FAILED = 0x911D

ctypedef GLenum (*PFNGLCLIENTWAITSYNCPROC)(GLsync sync, GLbitfield flags, GLuint64 timeout)
ctypedef void (*PFNGLDELETESYNCPROC)(GLsync sync)
ctypedef void (*PFNGLDRAWELEMENTSBASEVERTEXPROC)(GLenum mode, GLsizei count, GLenum type, const void *indices, GLint basevertex)
ctypedef void (*PFNGLDRAWELEMENTSINSTANCEDBASEVERTEXPROC)(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex)
ctypedef void (*PFNGLDRAWRANGEELEMENTSBASEVERTEXPROC)(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices, GLint basevertex)
ctypedef GLsync (*PFNGLFENCESYNCPROC)(GLenum condition, GLbitfield flags)
ctypedef void (*PFNGLFRAMEBUFFERTEXTUREPROC)(GLenum target, GLenum attachment, GLuint texture, GLint level)
ctypedef void (*PFNGLGETBUFFERPARAMETERI64VPROC)(GLenum target, GLenum pname, GLint64 *params)
ctypedef void (*PFNGLGETINTEGER64I_VPROC)(GLenum target, GLuint index, GLint64 *data)
ctypedef void (*PFNGLGETINTEGER64VPROC)(GLenum pname, GLint64 *data)
ctypedef void (*PFNGLGETMULTISAMPLEFVPROC)(GLenum pname, GLuint index, GLfloat *val)
ctypedef void (*PFNGLGETSYNCIVPROC)(GLsync sync, GLenum pname, GLsizei count, GLsizei *length, GLint *values)
ctypedef GLboolean (*PFNGLISSYNCPROC)(GLsync sync)
ctypedef void (*PFNGLMULTIDRAWELEMENTSBASEVERTEXPROC)(GLenum mode, const GLsizei *count, GLenum type, const void **indices, GLsizei drawcount, const GLint *basevertex)
ctypedef void (*PFNGLPROVOKINGVERTEXPROC)(GLenum mode)
ctypedef void (*PFNGLSAMPLEMASKIPROC)(GLuint maskNumber, GLbitfield mask)
ctypedef void (*PFNGLTEXIMAGE2DMULTISAMPLEPROC)(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
ctypedef void (*PFNGLTEXIMAGE3DMULTISAMPLEPROC)(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
ctypedef void (*PFNGLWAITSYNCPROC)(GLsync sync, GLbitfield flags, GLuint64 timeout)

cdef PFNGLCLIENTWAITSYNCPROC cglClientWaitSync = NULL
cdef PFNGLDELETESYNCPROC cglDeleteSync = NULL
cdef PFNGLDRAWELEMENTSBASEVERTEXPROC cglDrawElementsBaseVertex = NULL
cdef PFNGLDRAWELEMENTSINSTANCEDBASEVERTEXPROC cglDrawElementsInstancedBaseVertex = NULL
cdef PFNGLDRAWRANGEELEMENTSBASEVERTEXPROC cglDrawRangeElementsBaseVertex = NULL
cdef PFNGLFENCESYNCPROC cglFenceSync = NULL
cdef PFNGLFRAMEBUFFERTEXTUREPROC cglFramebufferTexture = NULL
cdef PFNGLGETBUFFERPARAMETERI64VPROC cglGetBufferParameteri64v = NULL
cdef PFNGLGETINTEGER64I_VPROC cglGetInteger64i_v = NULL
cdef PFNGLGETINTEGER64VPROC cglGetInteger64v = NULL
cdef PFNGLGETMULTISAMPLEFVPROC cglGetMultisamplefv = NULL
cdef PFNGLGETSYNCIVPROC cglGetSynciv = NULL
cdef PFNGLISSYNCPROC cglIsSync = NULL
cdef PFNGLMULTIDRAWELEMENTSBASEVERTEXPROC cglMultiDrawElementsBaseVertex = NULL
cdef PFNGLPROVOKINGVERTEXPROC cglProvokingVertex = NULL
cdef PFNGLSAMPLEMASKIPROC cglSampleMaski = NULL
cdef PFNGLTEXIMAGE2DMULTISAMPLEPROC cglTexImage2DMultisample = NULL
cdef PFNGLTEXIMAGE3DMULTISAMPLEPROC cglTexImage3DMultisample = NULL
cdef PFNGLWAITSYNCPROC cglWaitSync = NULL


cdef GLenum GetglClientWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout):
    global cglClientWaitSync
    cglClientWaitSync = <PFNGLCLIENTWAITSYNCPROC>getFunction("glClientWaitSync")
    cglClientWaitSync(sync, flags, timeout)

cdef void GetglDeleteSync(GLsync sync):
    global cglDeleteSync
    cglDeleteSync = <PFNGLDELETESYNCPROC>getFunction("glDeleteSync")
    cglDeleteSync(sync)

cdef void GetglDrawElementsBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLint basevertex):
    global cglDrawElementsBaseVertex
    cglDrawElementsBaseVertex = <PFNGLDRAWELEMENTSBASEVERTEXPROC>getFunction("glDrawElementsBaseVertex")
    cglDrawElementsBaseVertex(mode, count, type, indices, basevertex)

cdef void GetglDrawElementsInstancedBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex):
    global cglDrawElementsInstancedBaseVertex
    cglDrawElementsInstancedBaseVertex = <PFNGLDRAWELEMENTSINSTANCEDBASEVERTEXPROC>getFunction("glDrawElementsInstancedBaseVertex")
    cglDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex)

cdef void GetglDrawRangeElementsBaseVertex(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices, GLint basevertex):
    global cglDrawRangeElementsBaseVertex
    cglDrawRangeElementsBaseVertex = <PFNGLDRAWRANGEELEMENTSBASEVERTEXPROC>getFunction("glDrawRangeElementsBaseVertex")
    cglDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex)

cdef GLsync GetglFenceSync(GLenum condition, GLbitfield flags):
    global cglFenceSync
    cglFenceSync = <PFNGLFENCESYNCPROC>getFunction("glFenceSync")
    cglFenceSync(condition, flags)

cdef void GetglFramebufferTexture(GLenum target, GLenum attachment, GLuint texture, GLint level):
    global cglFramebufferTexture
    cglFramebufferTexture = <PFNGLFRAMEBUFFERTEXTUREPROC>getFunction("glFramebufferTexture")
    cglFramebufferTexture(target, attachment, texture, level)

cdef void GetglGetBufferParameteri64v(GLenum target, GLenum pname, GLint64 *params):
    global cglGetBufferParameteri64v
    cglGetBufferParameteri64v = <PFNGLGETBUFFERPARAMETERI64VPROC>getFunction("glGetBufferParameteri64v")
    cglGetBufferParameteri64v(target, pname, params)

cdef void GetglGetInteger64i_v(GLenum target, GLuint index, GLint64 *data):
    global cglGetInteger64i_v
    cglGetInteger64i_v = <PFNGLGETINTEGER64I_VPROC>getFunction("glGetInteger64i_v")
    cglGetInteger64i_v(target, index, data)

cdef void GetglGetInteger64v(GLenum pname, GLint64 *data):
    global cglGetInteger64v
    cglGetInteger64v = <PFNGLGETINTEGER64VPROC>getFunction("glGetInteger64v")
    cglGetInteger64v(pname, data)

cdef void GetglGetMultisamplefv(GLenum pname, GLuint index, GLfloat *val):
    global cglGetMultisamplefv
    cglGetMultisamplefv = <PFNGLGETMULTISAMPLEFVPROC>getFunction("glGetMultisamplefv")
    cglGetMultisamplefv(pname, index, val)

cdef void GetglGetSynciv(GLsync sync, GLenum pname, GLsizei count, GLsizei *length, GLint *values):
    global cglGetSynciv
    cglGetSynciv = <PFNGLGETSYNCIVPROC>getFunction("glGetSynciv")
    cglGetSynciv(sync, pname, count, length, values)

cdef GLboolean GetglIsSync(GLsync sync):
    global cglIsSync
    cglIsSync = <PFNGLISSYNCPROC>getFunction("glIsSync")
    cglIsSync(sync)

cdef void GetglMultiDrawElementsBaseVertex(GLenum mode, const GLsizei *count, GLenum type, const void **indices, GLsizei drawcount, const GLint *basevertex):
    global cglMultiDrawElementsBaseVertex
    cglMultiDrawElementsBaseVertex = <PFNGLMULTIDRAWELEMENTSBASEVERTEXPROC>getFunction("glMultiDrawElementsBaseVertex")
    cglMultiDrawElementsBaseVertex(mode, count, type, indices, drawcount, basevertex)

cdef void GetglProvokingVertex(GLenum mode):
    global cglProvokingVertex
    cglProvokingVertex = <PFNGLPROVOKINGVERTEXPROC>getFunction("glProvokingVertex")
    cglProvokingVertex(mode)

cdef void GetglSampleMaski(GLuint maskNumber, GLbitfield mask):
    global cglSampleMaski
    cglSampleMaski = <PFNGLSAMPLEMASKIPROC>getFunction("glSampleMaski")
    cglSampleMaski(maskNumber, mask)

cdef void GetglTexImage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    global cglTexImage2DMultisample
    cglTexImage2DMultisample = <PFNGLTEXIMAGE2DMULTISAMPLEPROC>getFunction("glTexImage2DMultisample")
    cglTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

cdef void GetglTexImage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    global cglTexImage3DMultisample
    cglTexImage3DMultisample = <PFNGLTEXIMAGE3DMULTISAMPLEPROC>getFunction("glTexImage3DMultisample")
    cglTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

cdef void GetglWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout):
    global cglWaitSync
    cglWaitSync = <PFNGLWAITSYNCPROC>getFunction("glWaitSync")
    cglWaitSync(sync, flags, timeout)

cglClientWaitSync = GetglClientWaitSync
cglDeleteSync = GetglDeleteSync
cglDrawElementsBaseVertex = GetglDrawElementsBaseVertex
cglDrawElementsInstancedBaseVertex = GetglDrawElementsInstancedBaseVertex
cglDrawRangeElementsBaseVertex = GetglDrawRangeElementsBaseVertex
cglFenceSync = GetglFenceSync
cglFramebufferTexture = GetglFramebufferTexture
cglGetBufferParameteri64v = GetglGetBufferParameteri64v
cglGetInteger64i_v = GetglGetInteger64i_v
cglGetInteger64v = GetglGetInteger64v
cglGetMultisamplefv = GetglGetMultisamplefv
cglGetSynciv = GetglGetSynciv
cglIsSync = GetglIsSync
cglMultiDrawElementsBaseVertex = GetglMultiDrawElementsBaseVertex
cglProvokingVertex = GetglProvokingVertex
cglSampleMaski = GetglSampleMaski
cglTexImage2DMultisample = GetglTexImage2DMultisample
cglTexImage3DMultisample = GetglTexImage3DMultisample
cglWaitSync = GetglWaitSync


cdef GLenum glClientWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout):
    cglClientWaitSync(sync, flags, timeout)

cdef void glDeleteSync(GLsync sync):
    cglDeleteSync(sync)

cdef void glDrawElementsBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLint basevertex):
    cglDrawElementsBaseVertex(mode, count, type, indices, basevertex)

cdef void glDrawElementsInstancedBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex):
    cglDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex)

cdef void glDrawRangeElementsBaseVertex(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices, GLint basevertex):
    cglDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex)

cdef GLsync glFenceSync(GLenum condition, GLbitfield flags):
    cglFenceSync(condition, flags)

cdef void glFramebufferTexture(GLenum target, GLenum attachment, GLuint texture, GLint level):
    cglFramebufferTexture(target, attachment, texture, level)

cdef void glGetBufferParameteri64v(GLenum target, GLenum pname, GLint64 *params):
    cglGetBufferParameteri64v(target, pname, params)

cdef void glGetInteger64i_v(GLenum target, GLuint index, GLint64 *data):
    cglGetInteger64i_v(target, index, data)

cdef void glGetInteger64v(GLenum pname, GLint64 *data):
    cglGetInteger64v(pname, data)

cdef void glGetMultisamplefv(GLenum pname, GLuint index, GLfloat *val):
    cglGetMultisamplefv(pname, index, val)

cdef void glGetSynciv(GLsync sync, GLenum pname, GLsizei count, GLsizei *length, GLint *values):
    cglGetSynciv(sync, pname, count, length, values)

cdef GLboolean glIsSync(GLsync sync):
    cglIsSync(sync)

cdef void glMultiDrawElementsBaseVertex(GLenum mode, const GLsizei *count, GLenum type, const void **indices, GLsizei drawcount, const GLint *basevertex):
    cglMultiDrawElementsBaseVertex(mode, count, type, indices, drawcount, basevertex)

cdef void glProvokingVertex(GLenum mode):
    cglProvokingVertex(mode)

cdef void glSampleMaski(GLuint maskNumber, GLbitfield mask):
    cglSampleMaski(maskNumber, mask)

cdef void glTexImage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    cglTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

cdef void glTexImage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    cglTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

cdef void glWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout):
    cglWaitSync(sync, flags, timeout)
