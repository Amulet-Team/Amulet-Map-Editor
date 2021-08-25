# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_UNIFORM_BLOCK_DATA_SIZE = 0x8A40
cdef GLenum GL_COPY_READ_BUFFER = 0x8F36
cdef GLenum GL_TEXTURE_BINDING_BUFFER = 0x8C2C
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER = 0x8A45
cdef GLenum GL_RG8_SNORM = 0x8F95
cdef GLenum GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 0x8A31
cdef GLenum GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS = 0x8A32
cdef GLenum GL_UNIFORM_SIZE = 0x8A38
cdef GLenum GL_MAX_GEOMETRY_UNIFORM_BLOCKS = 0x8A2C
cdef GLenum GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 0x8A33
cdef GLenum GL_RGB16_SNORM = 0x8F9A
cdef GLenum GL_R8_SNORM = 0x8F94
cdef GLenum GL_UNIFORM_NAME_LENGTH = 0x8A39
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_RECT = 0x8DD5
cdef GLenum GL_TEXTURE_RECTANGLE = 0x84F5
cdef GLenum GL_MAX_TEXTURE_BUFFER_SIZE = 0x8C2B
cdef GLenum GL_RGB8_SNORM = 0x8F96
cdef GLenum GL_MAX_VERTEX_UNIFORM_BLOCKS = 0x8A2B
cdef GLenum GL_RGBA8_SNORM = 0x8F97
cdef GLenum GL_UNSIGNED_INT_SAMPLER_BUFFER = 0x8DD8
cdef GLenum GL_INT_SAMPLER_BUFFER = 0x8DD0
cdef GLenum GL_ACTIVE_UNIFORM_BLOCKS = 0x8A36
cdef GLenum GL_TEXTURE_BUFFER = 0x8C2A
cdef GLenum GL_MAX_UNIFORM_BLOCK_SIZE = 0x8A30
cdef GLenum GL_PRIMITIVE_RESTART = 0x8F9D
cdef GLenum GL_UNIFORM_BUFFER_START = 0x8A29
cdef GLenum GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT = 0x8A34
cdef GLenum GL_SAMPLER_2D_RECT = 0x8B63
cdef GLenum GL_INVALID_INDEX = 0xFFFFFFFF
cdef GLenum GL_UNIFORM_ARRAY_STRIDE = 0x8A3C
cdef GLenum GL_UNIFORM_BLOCK_NAME_LENGTH = 0x8A41
cdef GLenum GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 0x8A43
cdef GLenum GL_UNIFORM_OFFSET = 0x8A3B
cdef GLenum GL_MAX_RECTANGLE_TEXTURE_SIZE = 0x84F8
cdef GLenum GL_INT_SAMPLER_2D_RECT = 0x8DCD
cdef GLenum GL_UNIFORM_BLOCK_BINDING = 0x8A3F
cdef GLenum GL_TEXTURE_BUFFER_DATA_STORE_BINDING = 0x8C2D
cdef GLenum GL_UNIFORM_BUFFER = 0x8A11
cdef GLenum GL_R16_SNORM = 0x8F98
cdef GLenum GL_SIGNED_NORMALIZED = 0x8F9C
cdef GLenum GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 0x8A35
cdef GLenum GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS = 0x8A42
cdef GLenum GL_UNIFORM_BUFFER_SIZE = 0x8A2A
cdef GLenum GL_MAX_COMBINED_UNIFORM_BLOCKS = 0x8A2E
cdef GLenum GL_COPY_WRITE_BUFFER = 0x8F37
cdef GLenum GL_RGBA16_SNORM = 0x8F9B
cdef GLenum GL_PRIMITIVE_RESTART_INDEX = 0x8F9E
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 0x8A46
cdef GLenum GL_UNIFORM_BLOCK_INDEX = 0x8A3A
cdef GLenum GL_MAX_UNIFORM_BUFFER_BINDINGS = 0x8A2F
cdef GLenum GL_TEXTURE_BINDING_RECTANGLE = 0x84F6
cdef GLenum GL_RG16_SNORM = 0x8F99
cdef GLenum GL_UNIFORM_BUFFER_BINDING = 0x8A28
cdef GLenum GL_UNIFORM_IS_ROW_MAJOR = 0x8A3E
cdef GLenum GL_PROXY_TEXTURE_RECTANGLE = 0x84F7
cdef GLenum GL_SAMPLER_BUFFER = 0x8DC2
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 0x8A44
cdef GLenum GL_MAX_FRAGMENT_UNIFORM_BLOCKS = 0x8A2D
cdef GLenum GL_UNIFORM_TYPE = 0x8A37
cdef GLenum GL_SAMPLER_2D_RECT_SHADOW = 0x8B64
cdef GLenum GL_UNIFORM_MATRIX_STRIDE = 0x8A3D

ctypedef void (*PFNGLTEXBUFFERPROC)(GLenum target, GLenum internalformat, GLuint buffer)
ctypedef void (*PFNGLGETACTIVEUNIFORMBLOCKIVPROC)(GLuint program, GLuint uniformBlockIndex, GLenum pname, GLint *params)
ctypedef void (*PFNGLPRIMITIVERESTARTINDEXPROC)(GLuint index)
ctypedef void (*PFNGLGETINTEGERI_VPROC)(GLenum target, GLuint index, GLint *data)
ctypedef void (*PFNGLBINDBUFFERRANGEPROC)(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
ctypedef void (*PFNGLDRAWARRAYSINSTANCEDPROC)(GLenum mode, GLint first, GLsizei count, GLsizei instancecount)
ctypedef void (*PFNGLUNIFORMBLOCKBINDINGPROC)(GLuint program, GLuint uniformBlockIndex, GLuint uniformBlockBinding)
ctypedef void (*PFNGLGETACTIVEUNIFORMSIVPROC)(GLuint program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETACTIVEUNIFORMNAMEPROC)(GLuint program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformName)
ctypedef void (*PFNGLGETACTIVEUNIFORMBLOCKNAMEPROC)(GLuint program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformBlockName)
ctypedef void (*PFNGLDRAWELEMENTSINSTANCEDPROC)(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount)
ctypedef void (*PFNGLBINDBUFFERBASEPROC)(GLenum target, GLuint index, GLuint buffer)
ctypedef GLuint (*PFNGLGETUNIFORMBLOCKINDEXPROC)(GLuint program, const GLchar *uniformBlockName)
ctypedef void (*PFNGLGETUNIFORMINDICESPROC)(GLuint program, GLsizei uniformCount, const GLchar **uniformNames, GLuint *uniformIndices)
ctypedef void (*PFNGLCOPYBUFFERSUBDATAPROC)(GLenum readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size)

cdef PFNGLTEXBUFFERPROC cglTexBuffer = NULL
cdef PFNGLGETACTIVEUNIFORMBLOCKIVPROC cglGetActiveUniformBlockiv = NULL
cdef PFNGLPRIMITIVERESTARTINDEXPROC cglPrimitiveRestartIndex = NULL
cdef PFNGLGETINTEGERI_VPROC cglGetIntegeri_v = NULL
cdef PFNGLBINDBUFFERRANGEPROC cglBindBufferRange = NULL
cdef PFNGLDRAWARRAYSINSTANCEDPROC cglDrawArraysInstanced = NULL
cdef PFNGLUNIFORMBLOCKBINDINGPROC cglUniformBlockBinding = NULL
cdef PFNGLGETACTIVEUNIFORMSIVPROC cglGetActiveUniformsiv = NULL
cdef PFNGLGETACTIVEUNIFORMNAMEPROC cglGetActiveUniformName = NULL
cdef PFNGLGETACTIVEUNIFORMBLOCKNAMEPROC cglGetActiveUniformBlockName = NULL
cdef PFNGLDRAWELEMENTSINSTANCEDPROC cglDrawElementsInstanced = NULL
cdef PFNGLBINDBUFFERBASEPROC cglBindBufferBase = NULL
cdef PFNGLGETUNIFORMBLOCKINDEXPROC cglGetUniformBlockIndex = NULL
cdef PFNGLGETUNIFORMINDICESPROC cglGetUniformIndices = NULL
cdef PFNGLCOPYBUFFERSUBDATAPROC cglCopyBufferSubData = NULL


cdef void GetglTexBuffer(GLenum target, GLenum internalformat, GLuint buffer):
    global cglTexBuffer
    cglTexBuffer = <PFNGLTEXBUFFERPROC>getFunction(b"glTexBuffer")
    cglTexBuffer(target, internalformat, buffer)

cdef void GetglGetActiveUniformBlockiv(GLuint program, GLuint uniformBlockIndex, GLenum pname, GLint *params):
    global cglGetActiveUniformBlockiv
    cglGetActiveUniformBlockiv = <PFNGLGETACTIVEUNIFORMBLOCKIVPROC>getFunction(b"glGetActiveUniformBlockiv")
    cglGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params)

cdef void GetglPrimitiveRestartIndex(GLuint index):
    global cglPrimitiveRestartIndex
    cglPrimitiveRestartIndex = <PFNGLPRIMITIVERESTARTINDEXPROC>getFunction(b"glPrimitiveRestartIndex")
    cglPrimitiveRestartIndex(index)

cdef void GetglGetIntegeri_v(GLenum target, GLuint index, GLint *data):
    global cglGetIntegeri_v
    cglGetIntegeri_v = <PFNGLGETINTEGERI_VPROC>getFunction(b"glGetIntegeri_v")
    cglGetIntegeri_v(target, index, data)

cdef void GetglBindBufferRange(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size):
    global cglBindBufferRange
    cglBindBufferRange = <PFNGLBINDBUFFERRANGEPROC>getFunction(b"glBindBufferRange")
    cglBindBufferRange(target, index, buffer, offset, size)

cdef void GetglDrawArraysInstanced(GLenum mode, GLint first, GLsizei count, GLsizei instancecount):
    global cglDrawArraysInstanced
    cglDrawArraysInstanced = <PFNGLDRAWARRAYSINSTANCEDPROC>getFunction(b"glDrawArraysInstanced")
    cglDrawArraysInstanced(mode, first, count, instancecount)

cdef void GetglUniformBlockBinding(GLuint program, GLuint uniformBlockIndex, GLuint uniformBlockBinding):
    global cglUniformBlockBinding
    cglUniformBlockBinding = <PFNGLUNIFORMBLOCKBINDINGPROC>getFunction(b"glUniformBlockBinding")
    cglUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding)

cdef void GetglGetActiveUniformsiv(GLuint program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint *params):
    global cglGetActiveUniformsiv
    cglGetActiveUniformsiv = <PFNGLGETACTIVEUNIFORMSIVPROC>getFunction(b"glGetActiveUniformsiv")
    cglGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params)

cdef void GetglGetActiveUniformName(GLuint program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformName):
    global cglGetActiveUniformName
    cglGetActiveUniformName = <PFNGLGETACTIVEUNIFORMNAMEPROC>getFunction(b"glGetActiveUniformName")
    cglGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName)

cdef void GetglGetActiveUniformBlockName(GLuint program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformBlockName):
    global cglGetActiveUniformBlockName
    cglGetActiveUniformBlockName = <PFNGLGETACTIVEUNIFORMBLOCKNAMEPROC>getFunction(b"glGetActiveUniformBlockName")
    cglGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName)

cdef void GetglDrawElementsInstanced(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount):
    global cglDrawElementsInstanced
    cglDrawElementsInstanced = <PFNGLDRAWELEMENTSINSTANCEDPROC>getFunction(b"glDrawElementsInstanced")
    cglDrawElementsInstanced(mode, count, type, indices, instancecount)

cdef void GetglBindBufferBase(GLenum target, GLuint index, GLuint buffer):
    global cglBindBufferBase
    cglBindBufferBase = <PFNGLBINDBUFFERBASEPROC>getFunction(b"glBindBufferBase")
    cglBindBufferBase(target, index, buffer)

cdef GLuint GetglGetUniformBlockIndex(GLuint program, const GLchar *uniformBlockName):
    global cglGetUniformBlockIndex
    cglGetUniformBlockIndex = <PFNGLGETUNIFORMBLOCKINDEXPROC>getFunction(b"glGetUniformBlockIndex")
    cglGetUniformBlockIndex(program, uniformBlockName)

cdef void GetglGetUniformIndices(GLuint program, GLsizei uniformCount, const GLchar **uniformNames, GLuint *uniformIndices):
    global cglGetUniformIndices
    cglGetUniformIndices = <PFNGLGETUNIFORMINDICESPROC>getFunction(b"glGetUniformIndices")
    cglGetUniformIndices(program, uniformCount, uniformNames, uniformIndices)

cdef void GetglCopyBufferSubData(GLenum readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size):
    global cglCopyBufferSubData
    cglCopyBufferSubData = <PFNGLCOPYBUFFERSUBDATAPROC>getFunction(b"glCopyBufferSubData")
    cglCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size)

cglTexBuffer = GetglTexBuffer
cglGetActiveUniformBlockiv = GetglGetActiveUniformBlockiv
cglPrimitiveRestartIndex = GetglPrimitiveRestartIndex
cglGetIntegeri_v = GetglGetIntegeri_v
cglBindBufferRange = GetglBindBufferRange
cglDrawArraysInstanced = GetglDrawArraysInstanced
cglUniformBlockBinding = GetglUniformBlockBinding
cglGetActiveUniformsiv = GetglGetActiveUniformsiv
cglGetActiveUniformName = GetglGetActiveUniformName
cglGetActiveUniformBlockName = GetglGetActiveUniformBlockName
cglDrawElementsInstanced = GetglDrawElementsInstanced
cglBindBufferBase = GetglBindBufferBase
cglGetUniformBlockIndex = GetglGetUniformBlockIndex
cglGetUniformIndices = GetglGetUniformIndices
cglCopyBufferSubData = GetglCopyBufferSubData


cdef void glTexBuffer(GLenum target, GLenum internalformat, GLuint buffer):
    cglTexBuffer(target, internalformat, buffer)

cdef void glGetActiveUniformBlockiv(GLuint program, GLuint uniformBlockIndex, GLenum pname, GLint *params):
    cglGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params)

cdef void glPrimitiveRestartIndex(GLuint index):
    cglPrimitiveRestartIndex(index)

cdef void glGetIntegeri_v(GLenum target, GLuint index, GLint *data):
    cglGetIntegeri_v(target, index, data)

cdef void glBindBufferRange(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size):
    cglBindBufferRange(target, index, buffer, offset, size)

cdef void glDrawArraysInstanced(GLenum mode, GLint first, GLsizei count, GLsizei instancecount):
    cglDrawArraysInstanced(mode, first, count, instancecount)

cdef void glUniformBlockBinding(GLuint program, GLuint uniformBlockIndex, GLuint uniformBlockBinding):
    cglUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding)

cdef void glGetActiveUniformsiv(GLuint program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint *params):
    cglGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params)

cdef void glGetActiveUniformName(GLuint program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformName):
    cglGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName)

cdef void glGetActiveUniformBlockName(GLuint program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformBlockName):
    cglGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName)

cdef void glDrawElementsInstanced(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount):
    cglDrawElementsInstanced(mode, count, type, indices, instancecount)

cdef void glBindBufferBase(GLenum target, GLuint index, GLuint buffer):
    cglBindBufferBase(target, index, buffer)

cdef GLuint glGetUniformBlockIndex(GLuint program, const GLchar *uniformBlockName):
    cglGetUniformBlockIndex(program, uniformBlockName)

cdef void glGetUniformIndices(GLuint program, GLsizei uniformCount, const GLchar **uniformNames, GLuint *uniformIndices):
    cglGetUniformIndices(program, uniformCount, uniformNames, uniformIndices)

cdef void glCopyBufferSubData(GLenum readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size):
    cglCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size)
