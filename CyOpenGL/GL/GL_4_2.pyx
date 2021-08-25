# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_ACTIVE_ATOMIC_COUNTER_BUFFERS = 0x92D9
cdef GLenum GL_ALL_BARRIER_BITS = 0xFFFFFFFF
cdef GLenum GL_ATOMIC_COUNTER_BARRIER_BIT = 0x00001000
cdef GLenum GL_ATOMIC_COUNTER_BUFFER = 0x92C0
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTERS = 0x92C5
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_ACTIVE_ATOMIC_COUNTER_INDICES = 0x92C6
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_BINDING = 0x92C1
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_DATA_SIZE = 0x92C4
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_FRAGMENT_SHADER = 0x92CB
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_GEOMETRY_SHADER = 0x92CA
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_CONTROL_SHADER = 0x92C8
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x92C9
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_VERTEX_SHADER = 0x92C7
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_SIZE = 0x92C3
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_START = 0x92C2
cdef GLenum GL_BUFFER_UPDATE_BARRIER_BIT = 0x00000200
cdef GLenum GL_COMMAND_BARRIER_BIT = 0x00000040
cdef GLenum GL_COMPRESSED_RGBA_BPTC_UNORM = 0x8E8C
cdef GLenum GL_COMPRESSED_RGB_BPTC_SIGNED_FLOAT = 0x8E8E
cdef GLenum GL_COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT = 0x8E8F
cdef GLenum GL_COMPRESSED_SRGB_ALPHA_BPTC_UNORM = 0x8E8D
cdef GLenum GL_COPY_READ_BUFFER_BINDING = 0x8F36
cdef GLenum GL_COPY_WRITE_BUFFER_BINDING = 0x8F37
cdef GLenum GL_ELEMENT_ARRAY_BARRIER_BIT = 0x00000002
cdef GLenum GL_FRAMEBUFFER_BARRIER_BIT = 0x00000400
cdef GLenum GL_IMAGE_1D = 0x904C
cdef GLenum GL_IMAGE_1D_ARRAY = 0x9052
cdef GLenum GL_IMAGE_2D = 0x904D
cdef GLenum GL_IMAGE_2D_ARRAY = 0x9053
cdef GLenum GL_IMAGE_2D_MULTISAMPLE = 0x9055
cdef GLenum GL_IMAGE_2D_MULTISAMPLE_ARRAY = 0x9056
cdef GLenum GL_IMAGE_2D_RECT = 0x904F
cdef GLenum GL_IMAGE_3D = 0x904E
cdef GLenum GL_IMAGE_BINDING_ACCESS = 0x8F3E
cdef GLenum GL_IMAGE_BINDING_FORMAT = 0x906E
cdef GLenum GL_IMAGE_BINDING_LAYER = 0x8F3D
cdef GLenum GL_IMAGE_BINDING_LAYERED = 0x8F3C
cdef GLenum GL_IMAGE_BINDING_LEVEL = 0x8F3B
cdef GLenum GL_IMAGE_BINDING_NAME = 0x8F3A
cdef GLenum GL_IMAGE_BUFFER = 0x9051
cdef GLenum GL_IMAGE_CUBE = 0x9050
cdef GLenum GL_IMAGE_CUBE_MAP_ARRAY = 0x9054
cdef GLenum GL_IMAGE_FORMAT_COMPATIBILITY_BY_CLASS = 0x90C9
cdef GLenum GL_IMAGE_FORMAT_COMPATIBILITY_BY_SIZE = 0x90C8
cdef GLenum GL_IMAGE_FORMAT_COMPATIBILITY_TYPE = 0x90C7
cdef GLenum GL_INT_IMAGE_1D = 0x9057
cdef GLenum GL_INT_IMAGE_1D_ARRAY = 0x905D
cdef GLenum GL_INT_IMAGE_2D = 0x9058
cdef GLenum GL_INT_IMAGE_2D_ARRAY = 0x905E
cdef GLenum GL_INT_IMAGE_2D_MULTISAMPLE = 0x9060
cdef GLenum GL_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x9061
cdef GLenum GL_INT_IMAGE_2D_RECT = 0x905A
cdef GLenum GL_INT_IMAGE_3D = 0x9059
cdef GLenum GL_INT_IMAGE_BUFFER = 0x905C
cdef GLenum GL_INT_IMAGE_CUBE = 0x905B
cdef GLenum GL_INT_IMAGE_CUBE_MAP_ARRAY = 0x905F
cdef GLenum GL_MAX_ATOMIC_COUNTER_BUFFER_BINDINGS = 0x92DC
cdef GLenum GL_MAX_ATOMIC_COUNTER_BUFFER_SIZE = 0x92D8
cdef GLenum GL_MAX_COMBINED_ATOMIC_COUNTERS = 0x92D7
cdef GLenum GL_MAX_COMBINED_ATOMIC_COUNTER_BUFFERS = 0x92D1
cdef GLenum GL_MAX_COMBINED_IMAGE_UNIFORMS = 0x90CF
cdef GLenum GL_MAX_COMBINED_IMAGE_UNITS_AND_FRAGMENT_OUTPUTS = 0x8F39
cdef GLenum GL_MAX_FRAGMENT_ATOMIC_COUNTERS = 0x92D6
cdef GLenum GL_MAX_FRAGMENT_ATOMIC_COUNTER_BUFFERS = 0x92D0
cdef GLenum GL_MAX_FRAGMENT_IMAGE_UNIFORMS = 0x90CE
cdef GLenum GL_MAX_GEOMETRY_ATOMIC_COUNTERS = 0x92D5
cdef GLenum GL_MAX_GEOMETRY_ATOMIC_COUNTER_BUFFERS = 0x92CF
cdef GLenum GL_MAX_GEOMETRY_IMAGE_UNIFORMS = 0x90CD
cdef GLenum GL_MAX_IMAGE_SAMPLES = 0x906D
cdef GLenum GL_MAX_IMAGE_UNITS = 0x8F38
cdef GLenum GL_MAX_TESS_CONTROL_ATOMIC_COUNTERS = 0x92D3
cdef GLenum GL_MAX_TESS_CONTROL_ATOMIC_COUNTER_BUFFERS = 0x92CD
cdef GLenum GL_MAX_TESS_CONTROL_IMAGE_UNIFORMS = 0x90CB
cdef GLenum GL_MAX_TESS_EVALUATION_ATOMIC_COUNTERS = 0x92D4
cdef GLenum GL_MAX_TESS_EVALUATION_ATOMIC_COUNTER_BUFFERS = 0x92CE
cdef GLenum GL_MAX_TESS_EVALUATION_IMAGE_UNIFORMS = 0x90CC
cdef GLenum GL_MAX_VERTEX_ATOMIC_COUNTERS = 0x92D2
cdef GLenum GL_MAX_VERTEX_ATOMIC_COUNTER_BUFFERS = 0x92CC
cdef GLenum GL_MAX_VERTEX_IMAGE_UNIFORMS = 0x90CA
cdef GLenum GL_MIN_MAP_BUFFER_ALIGNMENT = 0x90BC
cdef GLenum GL_NUM_SAMPLE_COUNTS = 0x9380
cdef GLenum GL_PACK_COMPRESSED_BLOCK_DEPTH = 0x912D
cdef GLenum GL_PACK_COMPRESSED_BLOCK_HEIGHT = 0x912C
cdef GLenum GL_PACK_COMPRESSED_BLOCK_SIZE = 0x912E
cdef GLenum GL_PACK_COMPRESSED_BLOCK_WIDTH = 0x912B
cdef GLenum GL_PIXEL_BUFFER_BARRIER_BIT = 0x00000080
cdef GLenum GL_SHADER_IMAGE_ACCESS_BARRIER_BIT = 0x00000020
cdef GLenum GL_TEXTURE_FETCH_BARRIER_BIT = 0x00000008
cdef GLenum GL_TEXTURE_IMMUTABLE_FORMAT = 0x912F
cdef GLenum GL_TEXTURE_UPDATE_BARRIER_BIT = 0x00000100
cdef GLenum GL_TRANSFORM_FEEDBACK_ACTIVE = 0x8E24
cdef GLenum GL_TRANSFORM_FEEDBACK_BARRIER_BIT = 0x00000800
cdef GLenum GL_TRANSFORM_FEEDBACK_PAUSED = 0x8E23
cdef GLenum GL_UNIFORM_ATOMIC_COUNTER_BUFFER_INDEX = 0x92DA
cdef GLenum GL_UNIFORM_BARRIER_BIT = 0x00000004
cdef GLenum GL_UNPACK_COMPRESSED_BLOCK_DEPTH = 0x9129
cdef GLenum GL_UNPACK_COMPRESSED_BLOCK_HEIGHT = 0x9128
cdef GLenum GL_UNPACK_COMPRESSED_BLOCK_SIZE = 0x912A
cdef GLenum GL_UNPACK_COMPRESSED_BLOCK_WIDTH = 0x9127
cdef GLenum GL_UNSIGNED_INT_ATOMIC_COUNTER = 0x92DB
cdef GLenum GL_UNSIGNED_INT_IMAGE_1D = 0x9062
cdef GLenum GL_UNSIGNED_INT_IMAGE_1D_ARRAY = 0x9068
cdef GLenum GL_UNSIGNED_INT_IMAGE_2D = 0x9063
cdef GLenum GL_UNSIGNED_INT_IMAGE_2D_ARRAY = 0x9069
cdef GLenum GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE = 0x906B
cdef GLenum GL_UNSIGNED_INT_IMAGE_2D_MULTISAMPLE_ARRAY = 0x906C
cdef GLenum GL_UNSIGNED_INT_IMAGE_2D_RECT = 0x9065
cdef GLenum GL_UNSIGNED_INT_IMAGE_3D = 0x9064
cdef GLenum GL_UNSIGNED_INT_IMAGE_BUFFER = 0x9067
cdef GLenum GL_UNSIGNED_INT_IMAGE_CUBE = 0x9066
cdef GLenum GL_UNSIGNED_INT_IMAGE_CUBE_MAP_ARRAY = 0x906A
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_BARRIER_BIT = 0x00000001

ctypedef void (*PFNGLBINDIMAGETEXTUREPROC)(GLuint unit, GLuint texture, GLint level, GLboolean layered, GLint layer, GLenum access, GLenum format)
ctypedef void (*PFNGLDRAWARRAYSINSTANCEDBASEINSTANCEPROC)(GLenum mode, GLint first, GLsizei count, GLsizei instancecount, GLuint baseinstance)
ctypedef void (*PFNGLDRAWELEMENTSINSTANCEDBASEINSTANCEPROC)(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLuint baseinstance)
ctypedef void (*PFNGLDRAWELEMENTSINSTANCEDBASEVERTEXBASEINSTANCEPROC)(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex, GLuint baseinstance)
ctypedef void (*PFNGLDRAWTRANSFORMFEEDBACKINSTANCEDPROC)(GLenum mode, GLuint id, GLsizei instancecount)
ctypedef void (*PFNGLDRAWTRANSFORMFEEDBACKSTREAMINSTANCEDPROC)(GLenum mode, GLuint id, GLuint stream, GLsizei instancecount)
ctypedef void (*PFNGLGETACTIVEATOMICCOUNTERBUFFERIVPROC)(GLuint program, GLuint bufferIndex, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETINTERNALFORMATIVPROC)(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint *params)
ctypedef void (*PFNGLMEMORYBARRIERPROC)(GLbitfield barriers)
ctypedef void (*PFNGLTEXSTORAGE1DPROC)(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width)
ctypedef void (*PFNGLTEXSTORAGE2DPROC)(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height)
ctypedef void (*PFNGLTEXSTORAGE3DPROC)(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth)

cdef PFNGLBINDIMAGETEXTUREPROC cglBindImageTexture = NULL
cdef PFNGLDRAWARRAYSINSTANCEDBASEINSTANCEPROC cglDrawArraysInstancedBaseInstance = NULL
cdef PFNGLDRAWELEMENTSINSTANCEDBASEINSTANCEPROC cglDrawElementsInstancedBaseInstance = NULL
cdef PFNGLDRAWELEMENTSINSTANCEDBASEVERTEXBASEINSTANCEPROC cglDrawElementsInstancedBaseVertexBaseInstance = NULL
cdef PFNGLDRAWTRANSFORMFEEDBACKINSTANCEDPROC cglDrawTransformFeedbackInstanced = NULL
cdef PFNGLDRAWTRANSFORMFEEDBACKSTREAMINSTANCEDPROC cglDrawTransformFeedbackStreamInstanced = NULL
cdef PFNGLGETACTIVEATOMICCOUNTERBUFFERIVPROC cglGetActiveAtomicCounterBufferiv = NULL
cdef PFNGLGETINTERNALFORMATIVPROC cglGetInternalformativ = NULL
cdef PFNGLMEMORYBARRIERPROC cglMemoryBarrier = NULL
cdef PFNGLTEXSTORAGE1DPROC cglTexStorage1D = NULL
cdef PFNGLTEXSTORAGE2DPROC cglTexStorage2D = NULL
cdef PFNGLTEXSTORAGE3DPROC cglTexStorage3D = NULL


cdef void GetglBindImageTexture(GLuint unit, GLuint texture, GLint level, GLboolean layered, GLint layer, GLenum access, GLenum format):
    global cglBindImageTexture
    cglBindImageTexture = <PFNGLBINDIMAGETEXTUREPROC>getFunction(b"glBindImageTexture")
    cglBindImageTexture(unit, texture, level, layered, layer, access, format)

cdef void GetglDrawArraysInstancedBaseInstance(GLenum mode, GLint first, GLsizei count, GLsizei instancecount, GLuint baseinstance):
    global cglDrawArraysInstancedBaseInstance
    cglDrawArraysInstancedBaseInstance = <PFNGLDRAWARRAYSINSTANCEDBASEINSTANCEPROC>getFunction(b"glDrawArraysInstancedBaseInstance")
    cglDrawArraysInstancedBaseInstance(mode, first, count, instancecount, baseinstance)

cdef void GetglDrawElementsInstancedBaseInstance(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLuint baseinstance):
    global cglDrawElementsInstancedBaseInstance
    cglDrawElementsInstancedBaseInstance = <PFNGLDRAWELEMENTSINSTANCEDBASEINSTANCEPROC>getFunction(b"glDrawElementsInstancedBaseInstance")
    cglDrawElementsInstancedBaseInstance(mode, count, type, indices, instancecount, baseinstance)

cdef void GetglDrawElementsInstancedBaseVertexBaseInstance(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex, GLuint baseinstance):
    global cglDrawElementsInstancedBaseVertexBaseInstance
    cglDrawElementsInstancedBaseVertexBaseInstance = <PFNGLDRAWELEMENTSINSTANCEDBASEVERTEXBASEINSTANCEPROC>getFunction(b"glDrawElementsInstancedBaseVertexBaseInstance")
    cglDrawElementsInstancedBaseVertexBaseInstance(mode, count, type, indices, instancecount, basevertex, baseinstance)

cdef void GetglDrawTransformFeedbackInstanced(GLenum mode, GLuint id, GLsizei instancecount):
    global cglDrawTransformFeedbackInstanced
    cglDrawTransformFeedbackInstanced = <PFNGLDRAWTRANSFORMFEEDBACKINSTANCEDPROC>getFunction(b"glDrawTransformFeedbackInstanced")
    cglDrawTransformFeedbackInstanced(mode, id, instancecount)

cdef void GetglDrawTransformFeedbackStreamInstanced(GLenum mode, GLuint id, GLuint stream, GLsizei instancecount):
    global cglDrawTransformFeedbackStreamInstanced
    cglDrawTransformFeedbackStreamInstanced = <PFNGLDRAWTRANSFORMFEEDBACKSTREAMINSTANCEDPROC>getFunction(b"glDrawTransformFeedbackStreamInstanced")
    cglDrawTransformFeedbackStreamInstanced(mode, id, stream, instancecount)

cdef void GetglGetActiveAtomicCounterBufferiv(GLuint program, GLuint bufferIndex, GLenum pname, GLint *params):
    global cglGetActiveAtomicCounterBufferiv
    cglGetActiveAtomicCounterBufferiv = <PFNGLGETACTIVEATOMICCOUNTERBUFFERIVPROC>getFunction(b"glGetActiveAtomicCounterBufferiv")
    cglGetActiveAtomicCounterBufferiv(program, bufferIndex, pname, params)

cdef void GetglGetInternalformativ(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint *params):
    global cglGetInternalformativ
    cglGetInternalformativ = <PFNGLGETINTERNALFORMATIVPROC>getFunction(b"glGetInternalformativ")
    cglGetInternalformativ(target, internalformat, pname, count, params)

cdef void GetglMemoryBarrier(GLbitfield barriers):
    global cglMemoryBarrier
    cglMemoryBarrier = <PFNGLMEMORYBARRIERPROC>getFunction(b"glMemoryBarrier")
    cglMemoryBarrier(barriers)

cdef void GetglTexStorage1D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width):
    global cglTexStorage1D
    cglTexStorage1D = <PFNGLTEXSTORAGE1DPROC>getFunction(b"glTexStorage1D")
    cglTexStorage1D(target, levels, internalformat, width)

cdef void GetglTexStorage2D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height):
    global cglTexStorage2D
    cglTexStorage2D = <PFNGLTEXSTORAGE2DPROC>getFunction(b"glTexStorage2D")
    cglTexStorage2D(target, levels, internalformat, width, height)

cdef void GetglTexStorage3D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth):
    global cglTexStorage3D
    cglTexStorage3D = <PFNGLTEXSTORAGE3DPROC>getFunction(b"glTexStorage3D")
    cglTexStorage3D(target, levels, internalformat, width, height, depth)

cglBindImageTexture = GetglBindImageTexture
cglDrawArraysInstancedBaseInstance = GetglDrawArraysInstancedBaseInstance
cglDrawElementsInstancedBaseInstance = GetglDrawElementsInstancedBaseInstance
cglDrawElementsInstancedBaseVertexBaseInstance = GetglDrawElementsInstancedBaseVertexBaseInstance
cglDrawTransformFeedbackInstanced = GetglDrawTransformFeedbackInstanced
cglDrawTransformFeedbackStreamInstanced = GetglDrawTransformFeedbackStreamInstanced
cglGetActiveAtomicCounterBufferiv = GetglGetActiveAtomicCounterBufferiv
cglGetInternalformativ = GetglGetInternalformativ
cglMemoryBarrier = GetglMemoryBarrier
cglTexStorage1D = GetglTexStorage1D
cglTexStorage2D = GetglTexStorage2D
cglTexStorage3D = GetglTexStorage3D


cdef void glBindImageTexture(GLuint unit, GLuint texture, GLint level, GLboolean layered, GLint layer, GLenum access, GLenum format):
    cglBindImageTexture(unit, texture, level, layered, layer, access, format)

cdef void glDrawArraysInstancedBaseInstance(GLenum mode, GLint first, GLsizei count, GLsizei instancecount, GLuint baseinstance):
    cglDrawArraysInstancedBaseInstance(mode, first, count, instancecount, baseinstance)

cdef void glDrawElementsInstancedBaseInstance(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLuint baseinstance):
    cglDrawElementsInstancedBaseInstance(mode, count, type, indices, instancecount, baseinstance)

cdef void glDrawElementsInstancedBaseVertexBaseInstance(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount, GLint basevertex, GLuint baseinstance):
    cglDrawElementsInstancedBaseVertexBaseInstance(mode, count, type, indices, instancecount, basevertex, baseinstance)

cdef void glDrawTransformFeedbackInstanced(GLenum mode, GLuint id, GLsizei instancecount):
    cglDrawTransformFeedbackInstanced(mode, id, instancecount)

cdef void glDrawTransformFeedbackStreamInstanced(GLenum mode, GLuint id, GLuint stream, GLsizei instancecount):
    cglDrawTransformFeedbackStreamInstanced(mode, id, stream, instancecount)

cdef void glGetActiveAtomicCounterBufferiv(GLuint program, GLuint bufferIndex, GLenum pname, GLint *params):
    cglGetActiveAtomicCounterBufferiv(program, bufferIndex, pname, params)

cdef void glGetInternalformativ(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint *params):
    cglGetInternalformativ(target, internalformat, pname, count, params)

cdef void glMemoryBarrier(GLbitfield barriers):
    cglMemoryBarrier(barriers)

cdef void glTexStorage1D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width):
    cglTexStorage1D(target, levels, internalformat, width)

cdef void glTexStorage2D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height):
    cglTexStorage2D(target, levels, internalformat, width, height)

cdef void glTexStorage3D(GLenum target, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth):
    cglTexStorage3D(target, levels, internalformat, width, height, depth)
