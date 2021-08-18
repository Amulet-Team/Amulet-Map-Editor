# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_CONTEXT_CORE_PROFILE_BIT = 0x00000001
cdef GLenum GL_CONTEXT_COMPATIBILITY_PROFILE_BIT = 0x00000002
cdef GLenum GL_LINES_ADJACENCY = 0x000A
cdef GLenum GL_LINE_STRIP_ADJACENCY = 0x000B
cdef GLenum GL_TRIANGLES_ADJACENCY = 0x000C
cdef GLenum GL_TRIANGLE_STRIP_ADJACENCY = 0x000D
cdef GLenum GL_PROGRAM_POINT_SIZE = 0x8642
cdef GLenum GL_MAX_GEOMETRY_TEXTURE_IMAGE_UNITS = 0x8C29
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_LAYERED = 0x8DA7
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_LAYER_TARGETS = 0x8DA8
cdef GLenum GL_GEOMETRY_SHADER = 0x8DD9
cdef GLenum GL_GEOMETRY_VERTICES_OUT = 0x8916
cdef GLenum GL_GEOMETRY_INPUT_TYPE = 0x8917
cdef GLenum GL_GEOMETRY_OUTPUT_TYPE = 0x8918
cdef GLenum GL_MAX_GEOMETRY_UNIFORM_COMPONENTS = 0x8DDF
cdef GLenum GL_MAX_GEOMETRY_OUTPUT_VERTICES = 0x8DE0
cdef GLenum GL_MAX_GEOMETRY_TOTAL_OUTPUT_COMPONENTS = 0x8DE1
cdef GLenum GL_MAX_VERTEX_OUTPUT_COMPONENTS = 0x9122
cdef GLenum GL_MAX_GEOMETRY_INPUT_COMPONENTS = 0x9123
cdef GLenum GL_MAX_GEOMETRY_OUTPUT_COMPONENTS = 0x9124
cdef GLenum GL_MAX_FRAGMENT_INPUT_COMPONENTS = 0x9125
cdef GLenum GL_CONTEXT_PROFILE_MASK = 0x9126
cdef GLenum GL_DEPTH_CLAMP = 0x864F
cdef GLenum GL_QUADS_FOLLOW_PROVOKING_VERTEX_CONVENTION = 0x8E4C
cdef GLenum GL_FIRST_VERTEX_CONVENTION = 0x8E4D
cdef GLenum GL_LAST_VERTEX_CONVENTION = 0x8E4E
cdef GLenum GL_PROVOKING_VERTEX = 0x8E4F
cdef GLenum GL_TEXTURE_CUBE_MAP_SEAMLESS = 0x884F
cdef GLenum GL_MAX_SERVER_WAIT_TIMEOUT = 0x9111
cdef GLenum GL_OBJECT_TYPE = 0x9112
cdef GLenum GL_SYNC_CONDITION = 0x9113
cdef GLenum GL_SYNC_STATUS = 0x9114
cdef GLenum GL_SYNC_FLAGS = 0x9115
cdef GLenum GL_SYNC_FENCE = 0x9116
cdef GLenum GL_SYNC_GPU_COMMANDS_COMPLETE = 0x9117
cdef GLenum GL_UNSIGNALED = 0x9118
cdef GLenum GL_SIGNALED = 0x9119
cdef GLenum GL_ALREADY_SIGNALED = 0x911A
cdef GLenum GL_TIMEOUT_EXPIRED = 0x911B
cdef GLenum GL_CONDITION_SATISFIED = 0x911C
cdef GLenum GL_WAIT_FAILED = 0x911D
cdef GLenum GL_TIMEOUT_IGNORED = 0xFFFFFFFFFFFFFFFF
cdef GLenum GL_SYNC_FLUSH_COMMANDS_BIT = 0x00000001
cdef GLenum GL_SAMPLE_POSITION = 0x8E50
cdef GLenum GL_SAMPLE_MASK = 0x8E51
cdef GLenum GL_SAMPLE_MASK_VALUE = 0x8E52
cdef GLenum GL_MAX_SAMPLE_MASK_WORDS = 0x8E59
cdef GLenum GL_TEXTURE_2D_MULTISAMPLE = 0x9100
cdef GLenum GL_PROXY_TEXTURE_2D_MULTISAMPLE = 0x9101
cdef GLenum GL_TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9102
cdef GLenum GL_PROXY_TEXTURE_2D_MULTISAMPLE_ARRAY = 0x9103
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE = 0x9104
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 0x9105
cdef GLenum GL_TEXTURE_SAMPLES = 0x9106
cdef GLenum GL_TEXTURE_FIXED_SAMPLE_LOCATIONS = 0x9107
cdef GLenum GL_SAMPLER_2D_MULTISAMPLE = 0x9108
cdef GLenum GL_INT_SAMPLER_2D_MULTISAMPLE = 0x9109
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE = 0x910A
cdef GLenum GL_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910B
cdef GLenum GL_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910C
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_MULTISAMPLE_ARRAY = 0x910D
cdef GLenum GL_MAX_COLOR_TEXTURE_SAMPLES = 0x910E
cdef GLenum GL_MAX_DEPTH_TEXTURE_SAMPLES = 0x910F
cdef GLenum GL_MAX_INTEGER_SAMPLES = 0x9110

ctypedef void (*GL_DRAW_ELEMENTS_BASE_VERTEX)(GLenum mode, GLsizei count, GLenum type, const void *indices, GLint basevertex)
ctypedef void (*GL_DRAW_RANGE_ELEMENTS_BASE_VERTEX)(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices, GLint basevertex)
ctypedef void (*GL_DRAW_ELEMENTS_INSTANCED_BASE_VERTEX)(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex)
ctypedef void (*GL_MULTI_DRAW_ELEMENTS_BASE_VERTEX)(GLenum mode, const GLsizei *count, GLenum type, const void *const*indices, GLsizei drawcount, const GLint *basevertex)
ctypedef void (*GL_PROVOKING_VERTEX)(GLenum mode)
ctypedef GLsync (*GL_FENCE_SYNC)(GLenum condition, GLbitfield flags)
ctypedef GLboolean (*GL_IS_SYNC)(GLsync sync)
ctypedef void (*GL_DELETE_SYNC)(GLsync sync)
ctypedef GLenum (*GL_CLIENT_WAIT_SYNC)(GLsync sync, GLbitfield flags, GLuint64 timeout)
ctypedef void (*GL_WAIT_SYNC)(GLsync sync, GLbitfield flags, GLuint64 timeout)
ctypedef void (*GL_GET_INTEGER64V)(GLenum pname, GLint64 *data)
ctypedef void (*GL_GET_SYNCIV)(GLsync sync, GLenum pname, GLsizei count, GLsizei *length, GLint *values)
ctypedef void (*GL_GET_INTEGER64I_V)(GLenum target, GLuint index, GLint64 *data)
ctypedef void (*GL_GET_BUFFER_PARAMETERI64V)(GLenum target, GLenum pname, GLint64 *params)
ctypedef void (*GL_FRAMEBUFFER_TEXTURE)(GLenum target, GLenum attachment, GLuint texture, GLint level)
ctypedef void (*GL_TEX_IMAGE2D_MULTISAMPLE)(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
ctypedef void (*GL_TEX_IMAGE3D_MULTISAMPLE)(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
ctypedef void (*GL_GET_MULTISAMPLEFV)(GLenum pname, GLuint index, GLfloat *val)
ctypedef void (*GL_SAMPLE_MASKI)(GLuint maskNumber, GLbitfield mask)

cdef GL_DRAW_ELEMENTS_BASE_VERTEX cglDrawElementsBaseVertex = NULL
cdef GL_DRAW_RANGE_ELEMENTS_BASE_VERTEX cglDrawRangeElementsBaseVertex = NULL
cdef GL_DRAW_ELEMENTS_INSTANCED_BASE_VERTEX cglDrawElementsInstancedBaseVertex = NULL
cdef GL_MULTI_DRAW_ELEMENTS_BASE_VERTEX cglMultiDrawElementsBaseVertex = NULL
cdef GL_PROVOKING_VERTEX cglProvokingVertex = NULL
cdef GL_FENCE_SYNC cglFenceSync = NULL
cdef GL_IS_SYNC cglIsSync = NULL
cdef GL_DELETE_SYNC cglDeleteSync = NULL
cdef GL_CLIENT_WAIT_SYNC cglClientWaitSync = NULL
cdef GL_WAIT_SYNC cglWaitSync = NULL
cdef GL_GET_INTEGER64V cglGetInteger64v = NULL
cdef GL_GET_SYNCIV cglGetSynciv = NULL
cdef GL_GET_INTEGER64I_V cglGetInteger64i_v = NULL
cdef GL_GET_BUFFER_PARAMETERI64V cglGetBufferParameteri64v = NULL
cdef GL_FRAMEBUFFER_TEXTURE cglFramebufferTexture = NULL
cdef GL_TEX_IMAGE2D_MULTISAMPLE cglTexImage2DMultisample = NULL
cdef GL_TEX_IMAGE3D_MULTISAMPLE cglTexImage3DMultisample = NULL
cdef GL_GET_MULTISAMPLEFV cglGetMultisamplefv = NULL
cdef GL_SAMPLE_MASKI cglSampleMaski = NULL


cdef void GetglDrawElementsBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLint basevertex):
    global cglDrawElementsBaseVertex
    cglDrawElementsBaseVertex = <GL_DRAW_ELEMENTS_BASE_VERTEX>getFunction(b"glDrawElementsBaseVertex")
    cglDrawElementsBaseVertex(mode, count, type, indices, basevertex)

cdef void GetglDrawRangeElementsBaseVertex(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices, GLint basevertex):
    global cglDrawRangeElementsBaseVertex
    cglDrawRangeElementsBaseVertex = <GL_DRAW_RANGE_ELEMENTS_BASE_VERTEX>getFunction(b"glDrawRangeElementsBaseVertex")
    cglDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex)

cdef void GetglDrawElementsInstancedBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex):
    global cglDrawElementsInstancedBaseVertex
    cglDrawElementsInstancedBaseVertex = <GL_DRAW_ELEMENTS_INSTANCED_BASE_VERTEX>getFunction(b"glDrawElementsInstancedBaseVertex")
    cglDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex)

cdef void GetglMultiDrawElementsBaseVertex(GLenum mode, const GLsizei *count, GLenum type, const void *const*indices, GLsizei drawcount, const GLint *basevertex):
    global cglMultiDrawElementsBaseVertex
    cglMultiDrawElementsBaseVertex = <GL_MULTI_DRAW_ELEMENTS_BASE_VERTEX>getFunction(b"glMultiDrawElementsBaseVertex")
    cglMultiDrawElementsBaseVertex(mode, count, type, indices, drawcount, basevertex)

cdef void GetglProvokingVertex(GLenum mode):
    global cglProvokingVertex
    cglProvokingVertex = <GL_PROVOKING_VERTEX>getFunction(b"glProvokingVertex")
    cglProvokingVertex(mode)

cdef GLsync GetglFenceSync(GLenum condition, GLbitfield flags):
    global cglFenceSync
    cglFenceSync = <GL_FENCE_SYNC>getFunction(b"glFenceSync")
    cglFenceSync(condition, flags)

cdef GLboolean GetglIsSync(GLsync sync):
    global cglIsSync
    cglIsSync = <GL_IS_SYNC>getFunction(b"glIsSync")
    cglIsSync(sync)

cdef void GetglDeleteSync(GLsync sync):
    global cglDeleteSync
    cglDeleteSync = <GL_DELETE_SYNC>getFunction(b"glDeleteSync")
    cglDeleteSync(sync)

cdef GLenum GetglClientWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout):
    global cglClientWaitSync
    cglClientWaitSync = <GL_CLIENT_WAIT_SYNC>getFunction(b"glClientWaitSync")
    cglClientWaitSync(sync, flags, timeout)

cdef void GetglWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout):
    global cglWaitSync
    cglWaitSync = <GL_WAIT_SYNC>getFunction(b"glWaitSync")
    cglWaitSync(sync, flags, timeout)

cdef void GetglGetInteger64v(GLenum pname, GLint64 *data):
    global cglGetInteger64v
    cglGetInteger64v = <GL_GET_INTEGER64V>getFunction(b"glGetInteger64v")
    cglGetInteger64v(pname, data)

cdef void GetglGetSynciv(GLsync sync, GLenum pname, GLsizei count, GLsizei *length, GLint *values):
    global cglGetSynciv
    cglGetSynciv = <GL_GET_SYNCIV>getFunction(b"glGetSynciv")
    cglGetSynciv(sync, pname, count, length, values)

cdef void GetglGetInteger64i_v(GLenum target, GLuint index, GLint64 *data):
    global cglGetInteger64i_v
    cglGetInteger64i_v = <GL_GET_INTEGER64I_V>getFunction(b"glGetInteger64i_v")
    cglGetInteger64i_v(target, index, data)

cdef void GetglGetBufferParameteri64v(GLenum target, GLenum pname, GLint64 *params):
    global cglGetBufferParameteri64v
    cglGetBufferParameteri64v = <GL_GET_BUFFER_PARAMETERI64V>getFunction(b"glGetBufferParameteri64v")
    cglGetBufferParameteri64v(target, pname, params)

cdef void GetglFramebufferTexture(GLenum target, GLenum attachment, GLuint texture, GLint level):
    global cglFramebufferTexture
    cglFramebufferTexture = <GL_FRAMEBUFFER_TEXTURE>getFunction(b"glFramebufferTexture")
    cglFramebufferTexture(target, attachment, texture, level)

cdef void GetglTexImage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    global cglTexImage2DMultisample
    cglTexImage2DMultisample = <GL_TEX_IMAGE2D_MULTISAMPLE>getFunction(b"glTexImage2DMultisample")
    cglTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

cdef void GetglTexImage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    global cglTexImage3DMultisample
    cglTexImage3DMultisample = <GL_TEX_IMAGE3D_MULTISAMPLE>getFunction(b"glTexImage3DMultisample")
    cglTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

cdef void GetglGetMultisamplefv(GLenum pname, GLuint index, GLfloat *val):
    global cglGetMultisamplefv
    cglGetMultisamplefv = <GL_GET_MULTISAMPLEFV>getFunction(b"glGetMultisamplefv")
    cglGetMultisamplefv(pname, index, val)

cdef void GetglSampleMaski(GLuint maskNumber, GLbitfield mask):
    global cglSampleMaski
    cglSampleMaski = <GL_SAMPLE_MASKI>getFunction(b"glSampleMaski")
    cglSampleMaski(maskNumber, mask)

cglDrawElementsBaseVertex = GetglDrawElementsBaseVertex
cglDrawRangeElementsBaseVertex = GetglDrawRangeElementsBaseVertex
cglDrawElementsInstancedBaseVertex = GetglDrawElementsInstancedBaseVertex
cglMultiDrawElementsBaseVertex = GetglMultiDrawElementsBaseVertex
cglProvokingVertex = GetglProvokingVertex
cglFenceSync = GetglFenceSync
cglIsSync = GetglIsSync
cglDeleteSync = GetglDeleteSync
cglClientWaitSync = GetglClientWaitSync
cglWaitSync = GetglWaitSync
cglGetInteger64v = GetglGetInteger64v
cglGetSynciv = GetglGetSynciv
cglGetInteger64i_v = GetglGetInteger64i_v
cglGetBufferParameteri64v = GetglGetBufferParameteri64v
cglFramebufferTexture = GetglFramebufferTexture
cglTexImage2DMultisample = GetglTexImage2DMultisample
cglTexImage3DMultisample = GetglTexImage3DMultisample
cglGetMultisamplefv = GetglGetMultisamplefv
cglSampleMaski = GetglSampleMaski


cpdef void glDrawElementsBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLint basevertex):
    cglDrawElementsBaseVertex(mode, count, type, indices, basevertex)

cpdef void glDrawRangeElementsBaseVertex(GLenum mode, GLuint start, GLuint end, GLsizei count, GLenum type, const void *indices, GLint basevertex):
    cglDrawRangeElementsBaseVertex(mode, start, end, count, type, indices, basevertex)

cpdef void glDrawElementsInstancedBaseVertex(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex):
    cglDrawElementsInstancedBaseVertex(mode, count, type, indices, instancecount, basevertex)

cpdef void glMultiDrawElementsBaseVertex(GLenum mode, const GLsizei *count, GLenum type, const void *const*indices, GLsizei drawcount, const GLint *basevertex):
    cglMultiDrawElementsBaseVertex(mode, count, type, indices, drawcount, basevertex)

cpdef void glProvokingVertex(GLenum mode):
    cglProvokingVertex(mode)

cpdef GLsync glFenceSync(GLenum condition, GLbitfield flags):
    cglFenceSync(condition, flags)

cpdef GLboolean glIsSync(GLsync sync):
    cglIsSync(sync)

cpdef void glDeleteSync(GLsync sync):
    cglDeleteSync(sync)

cpdef GLenum glClientWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout):
    cglClientWaitSync(sync, flags, timeout)

cpdef void glWaitSync(GLsync sync, GLbitfield flags, GLuint64 timeout):
    cglWaitSync(sync, flags, timeout)

cpdef void glGetInteger64v(GLenum pname, GLint64 *data):
    cglGetInteger64v(pname, data)

cpdef void glGetSynciv(GLsync sync, GLenum pname, GLsizei count, GLsizei *length, GLint *values):
    cglGetSynciv(sync, pname, count, length, values)

cpdef void glGetInteger64i_v(GLenum target, GLuint index, GLint64 *data):
    cglGetInteger64i_v(target, index, data)

cpdef void glGetBufferParameteri64v(GLenum target, GLenum pname, GLint64 *params):
    cglGetBufferParameteri64v(target, pname, params)

cpdef void glFramebufferTexture(GLenum target, GLenum attachment, GLuint texture, GLint level):
    cglFramebufferTexture(target, attachment, texture, level)

cpdef void glTexImage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    cglTexImage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

cpdef void glTexImage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    cglTexImage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

cpdef void glGetMultisamplefv(GLenum pname, GLuint index, GLfloat *val):
    cglGetMultisamplefv(pname, index, val)

cpdef void glSampleMaski(GLuint maskNumber, GLbitfield mask):
    cglSampleMaski(maskNumber, mask)
