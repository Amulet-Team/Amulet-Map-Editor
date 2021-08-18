# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_SAMPLER_2D_RECT = 0x8B63
cdef GLenum GL_SAMPLER_2D_RECT_SHADOW = 0x8B64
cdef GLenum GL_SAMPLER_BUFFER = 0x8DC2
cdef GLenum GL_INT_SAMPLER_2D_RECT = 0x8DCD
cdef GLenum GL_INT_SAMPLER_BUFFER = 0x8DD0
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_RECT = 0x8DD5
cdef GLenum GL_UNSIGNED_INT_SAMPLER_BUFFER = 0x8DD8
cdef GLenum GL_TEXTURE_BUFFER = 0x8C2A
cdef GLenum GL_MAX_TEXTURE_BUFFER_SIZE = 0x8C2B
cdef GLenum GL_TEXTURE_BINDING_BUFFER = 0x8C2C
cdef GLenum GL_TEXTURE_BUFFER_DATA_STORE_BINDING = 0x8C2D
cdef GLenum GL_TEXTURE_RECTANGLE = 0x84F5
cdef GLenum GL_TEXTURE_BINDING_RECTANGLE = 0x84F6
cdef GLenum GL_PROXY_TEXTURE_RECTANGLE = 0x84F7
cdef GLenum GL_MAX_RECTANGLE_TEXTURE_SIZE = 0x84F8
cdef GLenum GL_R8_SNORM = 0x8F94
cdef GLenum GL_RG8_SNORM = 0x8F95
cdef GLenum GL_RGB8_SNORM = 0x8F96
cdef GLenum GL_RGBA8_SNORM = 0x8F97
cdef GLenum GL_R16_SNORM = 0x8F98
cdef GLenum GL_RG16_SNORM = 0x8F99
cdef GLenum GL_RGB16_SNORM = 0x8F9A
cdef GLenum GL_RGBA16_SNORM = 0x8F9B
cdef GLenum GL_SIGNED_NORMALIZED = 0x8F9C
cdef GLenum GL_PRIMITIVE_RESTART = 0x8F9D
cdef GLenum GL_PRIMITIVE_RESTART_INDEX = 0x8F9E
cdef GLenum GL_COPY_READ_BUFFER = 0x8F36
cdef GLenum GL_COPY_WRITE_BUFFER = 0x8F37
cdef GLenum GL_UNIFORM_BUFFER = 0x8A11
cdef GLenum GL_UNIFORM_BUFFER_BINDING = 0x8A28
cdef GLenum GL_UNIFORM_BUFFER_START = 0x8A29
cdef GLenum GL_UNIFORM_BUFFER_SIZE = 0x8A2A
cdef GLenum GL_MAX_VERTEX_UNIFORM_BLOCKS = 0x8A2B
cdef GLenum GL_MAX_GEOMETRY_UNIFORM_BLOCKS = 0x8A2C
cdef GLenum GL_MAX_FRAGMENT_UNIFORM_BLOCKS = 0x8A2D
cdef GLenum GL_MAX_COMBINED_UNIFORM_BLOCKS = 0x8A2E
cdef GLenum GL_MAX_UNIFORM_BUFFER_BINDINGS = 0x8A2F
cdef GLenum GL_MAX_UNIFORM_BLOCK_SIZE = 0x8A30
cdef GLenum GL_MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 0x8A31
cdef GLenum GL_MAX_COMBINED_GEOMETRY_UNIFORM_COMPONENTS = 0x8A32
cdef GLenum GL_MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 0x8A33
cdef GLenum GL_UNIFORM_BUFFER_OFFSET_ALIGNMENT = 0x8A34
cdef GLenum GL_ACTIVE_UNIFORM_BLOCK_MAX_NAME_LENGTH = 0x8A35
cdef GLenum GL_ACTIVE_UNIFORM_BLOCKS = 0x8A36
cdef GLenum GL_UNIFORM_TYPE = 0x8A37
cdef GLenum GL_UNIFORM_SIZE = 0x8A38
cdef GLenum GL_UNIFORM_NAME_LENGTH = 0x8A39
cdef GLenum GL_UNIFORM_BLOCK_INDEX = 0x8A3A
cdef GLenum GL_UNIFORM_OFFSET = 0x8A3B
cdef GLenum GL_UNIFORM_ARRAY_STRIDE = 0x8A3C
cdef GLenum GL_UNIFORM_MATRIX_STRIDE = 0x8A3D
cdef GLenum GL_UNIFORM_IS_ROW_MAJOR = 0x8A3E
cdef GLenum GL_UNIFORM_BLOCK_BINDING = 0x8A3F
cdef GLenum GL_UNIFORM_BLOCK_DATA_SIZE = 0x8A40
cdef GLenum GL_UNIFORM_BLOCK_NAME_LENGTH = 0x8A41
cdef GLenum GL_UNIFORM_BLOCK_ACTIVE_UNIFORMS = 0x8A42
cdef GLenum GL_UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 0x8A43
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 0x8A44
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_GEOMETRY_SHADER = 0x8A45
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 0x8A46
cdef GLenum GL_INVALID_INDEX = 0xFFFFFFFF

ctypedef void (*GL_DRAW_ARRAYS_INSTANCED)(GLenum mode, GLint first, GLsizei count, GLsizei instancecount)
ctypedef void (*GL_DRAW_ELEMENTS_INSTANCED)(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount)
ctypedef void (*GL_TEX_BUFFER)(GLenum target, GLenum internalformat, GLuint buffer)
ctypedef void (*GL_PRIMITIVE_RESTART_INDEX)(GLuint index)
ctypedef void (*GL_COPY_BUFFER_SUB_DATA)(GLenum readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size)
ctypedef void (*GL_GET_UNIFORM_INDICES)(GLuint program, GLsizei uniformCount, const GLchar *const*uniformNames, GLuint *uniformIndices)
ctypedef void (*GL_GET_ACTIVE_UNIFORMSIV)(GLuint program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint *params)
ctypedef void (*GL_GET_ACTIVE_UNIFORM_NAME)(GLuint program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformName)
ctypedef GLuint (*GL_GET_UNIFORM_BLOCK_INDEX)(GLuint program, const GLchar *uniformBlockName)
ctypedef void (*GL_GET_ACTIVE_UNIFORM_BLOCKIV)(GLuint program, GLuint uniformBlockIndex, GLenum pname, GLint *params)
ctypedef void (*GL_GET_ACTIVE_UNIFORM_BLOCK_NAME)(GLuint program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformBlockName)
ctypedef void (*GL_UNIFORM_BLOCK_BINDING)(GLuint program, GLuint uniformBlockIndex, GLuint uniformBlockBinding)
ctypedef void (*GL_BIND_BUFFER_RANGE)(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
ctypedef void (*GL_BIND_BUFFER_BASE)(GLenum target, GLuint index, GLuint buffer)
ctypedef void (*GL_GET_INTEGERI_V)(GLenum target, GLuint index, GLint *data)

cdef GL_DRAW_ARRAYS_INSTANCED cglDrawArraysInstanced = NULL
cdef GL_DRAW_ELEMENTS_INSTANCED cglDrawElementsInstanced = NULL
cdef GL_TEX_BUFFER cglTexBuffer = NULL
cdef GL_PRIMITIVE_RESTART_INDEX cglPrimitiveRestartIndex = NULL
cdef GL_COPY_BUFFER_SUB_DATA cglCopyBufferSubData = NULL
cdef GL_GET_UNIFORM_INDICES cglGetUniformIndices = NULL
cdef GL_GET_ACTIVE_UNIFORMSIV cglGetActiveUniformsiv = NULL
cdef GL_GET_ACTIVE_UNIFORM_NAME cglGetActiveUniformName = NULL
cdef GL_GET_UNIFORM_BLOCK_INDEX cglGetUniformBlockIndex = NULL
cdef GL_GET_ACTIVE_UNIFORM_BLOCKIV cglGetActiveUniformBlockiv = NULL
cdef GL_GET_ACTIVE_UNIFORM_BLOCK_NAME cglGetActiveUniformBlockName = NULL
cdef GL_UNIFORM_BLOCK_BINDING cglUniformBlockBinding = NULL
cdef GL_BIND_BUFFER_RANGE cglBindBufferRange = NULL
cdef GL_BIND_BUFFER_BASE cglBindBufferBase = NULL
cdef GL_GET_INTEGERI_V cglGetIntegeri_v = NULL


cdef void GetglDrawArraysInstanced(GLenum mode, GLint first, GLsizei count, GLsizei instancecount):
    global cglDrawArraysInstanced
    cglDrawArraysInstanced = <GL_DRAW_ARRAYS_INSTANCED>getFunction(b"glDrawArraysInstanced")
    cglDrawArraysInstanced(mode, first, count, instancecount)

cdef void GetglDrawElementsInstanced(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount):
    global cglDrawElementsInstanced
    cglDrawElementsInstanced = <GL_DRAW_ELEMENTS_INSTANCED>getFunction(b"glDrawElementsInstanced")
    cglDrawElementsInstanced(mode, count, type, indices, instancecount)

cdef void GetglTexBuffer(GLenum target, GLenum internalformat, GLuint buffer):
    global cglTexBuffer
    cglTexBuffer = <GL_TEX_BUFFER>getFunction(b"glTexBuffer")
    cglTexBuffer(target, internalformat, buffer)

cdef void GetglPrimitiveRestartIndex(GLuint index):
    global cglPrimitiveRestartIndex
    cglPrimitiveRestartIndex = <GL_PRIMITIVE_RESTART_INDEX>getFunction(b"glPrimitiveRestartIndex")
    cglPrimitiveRestartIndex(index)

cdef void GetglCopyBufferSubData(GLenum readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size):
    global cglCopyBufferSubData
    cglCopyBufferSubData = <GL_COPY_BUFFER_SUB_DATA>getFunction(b"glCopyBufferSubData")
    cglCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size)

cdef void GetglGetUniformIndices(GLuint program, GLsizei uniformCount, const GLchar *const*uniformNames, GLuint *uniformIndices):
    global cglGetUniformIndices
    cglGetUniformIndices = <GL_GET_UNIFORM_INDICES>getFunction(b"glGetUniformIndices")
    cglGetUniformIndices(program, uniformCount, uniformNames, uniformIndices)

cdef void GetglGetActiveUniformsiv(GLuint program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint *params):
    global cglGetActiveUniformsiv
    cglGetActiveUniformsiv = <GL_GET_ACTIVE_UNIFORMSIV>getFunction(b"glGetActiveUniformsiv")
    cglGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params)

cdef void GetglGetActiveUniformName(GLuint program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformName):
    global cglGetActiveUniformName
    cglGetActiveUniformName = <GL_GET_ACTIVE_UNIFORM_NAME>getFunction(b"glGetActiveUniformName")
    cglGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName)

cdef GLuint GetglGetUniformBlockIndex(GLuint program, const GLchar *uniformBlockName):
    global cglGetUniformBlockIndex
    cglGetUniformBlockIndex = <GL_GET_UNIFORM_BLOCK_INDEX>getFunction(b"glGetUniformBlockIndex")
    cglGetUniformBlockIndex(program, uniformBlockName)

cdef void GetglGetActiveUniformBlockiv(GLuint program, GLuint uniformBlockIndex, GLenum pname, GLint *params):
    global cglGetActiveUniformBlockiv
    cglGetActiveUniformBlockiv = <GL_GET_ACTIVE_UNIFORM_BLOCKIV>getFunction(b"glGetActiveUniformBlockiv")
    cglGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params)

cdef void GetglGetActiveUniformBlockName(GLuint program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformBlockName):
    global cglGetActiveUniformBlockName
    cglGetActiveUniformBlockName = <GL_GET_ACTIVE_UNIFORM_BLOCK_NAME>getFunction(b"glGetActiveUniformBlockName")
    cglGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName)

cdef void GetglUniformBlockBinding(GLuint program, GLuint uniformBlockIndex, GLuint uniformBlockBinding):
    global cglUniformBlockBinding
    cglUniformBlockBinding = <GL_UNIFORM_BLOCK_BINDING>getFunction(b"glUniformBlockBinding")
    cglUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding)

cdef void GetglBindBufferRange(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size):
    global cglBindBufferRange
    cglBindBufferRange = <GL_BIND_BUFFER_RANGE>getFunction(b"glBindBufferRange")
    cglBindBufferRange(target, index, buffer, offset, size)

cdef void GetglBindBufferBase(GLenum target, GLuint index, GLuint buffer):
    global cglBindBufferBase
    cglBindBufferBase = <GL_BIND_BUFFER_BASE>getFunction(b"glBindBufferBase")
    cglBindBufferBase(target, index, buffer)

cdef void GetglGetIntegeri_v(GLenum target, GLuint index, GLint *data):
    global cglGetIntegeri_v
    cglGetIntegeri_v = <GL_GET_INTEGERI_V>getFunction(b"glGetIntegeri_v")
    cglGetIntegeri_v(target, index, data)

cglDrawArraysInstanced = GetglDrawArraysInstanced
cglDrawElementsInstanced = GetglDrawElementsInstanced
cglTexBuffer = GetglTexBuffer
cglPrimitiveRestartIndex = GetglPrimitiveRestartIndex
cglCopyBufferSubData = GetglCopyBufferSubData
cglGetUniformIndices = GetglGetUniformIndices
cglGetActiveUniformsiv = GetglGetActiveUniformsiv
cglGetActiveUniformName = GetglGetActiveUniformName
cglGetUniformBlockIndex = GetglGetUniformBlockIndex
cglGetActiveUniformBlockiv = GetglGetActiveUniformBlockiv
cglGetActiveUniformBlockName = GetglGetActiveUniformBlockName
cglUniformBlockBinding = GetglUniformBlockBinding
cglBindBufferRange = GetglBindBufferRange
cglBindBufferBase = GetglBindBufferBase
cglGetIntegeri_v = GetglGetIntegeri_v


cpdef void glDrawArraysInstanced(GLenum mode, GLint first, GLsizei count, GLsizei instancecount):
    cglDrawArraysInstanced(mode, first, count, instancecount)

cpdef void glDrawElementsInstanced(GLenum mode, GLsizei count, GLenum type, const void *indices, GLsizei instancecount):
    cglDrawElementsInstanced(mode, count, type, indices, instancecount)

cpdef void glTexBuffer(GLenum target, GLenum internalformat, GLuint buffer):
    cglTexBuffer(target, internalformat, buffer)

cpdef void glPrimitiveRestartIndex(GLuint index):
    cglPrimitiveRestartIndex(index)

cpdef void glCopyBufferSubData(GLenum readTarget, GLenum writeTarget, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size):
    cglCopyBufferSubData(readTarget, writeTarget, readOffset, writeOffset, size)

cpdef void glGetUniformIndices(GLuint program, GLsizei uniformCount, const GLchar *const*uniformNames, GLuint *uniformIndices):
    cglGetUniformIndices(program, uniformCount, uniformNames, uniformIndices)

cpdef void glGetActiveUniformsiv(GLuint program, GLsizei uniformCount, const GLuint *uniformIndices, GLenum pname, GLint *params):
    cglGetActiveUniformsiv(program, uniformCount, uniformIndices, pname, params)

cpdef void glGetActiveUniformName(GLuint program, GLuint uniformIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformName):
    cglGetActiveUniformName(program, uniformIndex, bufSize, length, uniformName)

cpdef GLuint glGetUniformBlockIndex(GLuint program, const GLchar *uniformBlockName):
    cglGetUniformBlockIndex(program, uniformBlockName)

cpdef void glGetActiveUniformBlockiv(GLuint program, GLuint uniformBlockIndex, GLenum pname, GLint *params):
    cglGetActiveUniformBlockiv(program, uniformBlockIndex, pname, params)

cpdef void glGetActiveUniformBlockName(GLuint program, GLuint uniformBlockIndex, GLsizei bufSize, GLsizei *length, GLchar *uniformBlockName):
    cglGetActiveUniformBlockName(program, uniformBlockIndex, bufSize, length, uniformBlockName)

cpdef void glUniformBlockBinding(GLuint program, GLuint uniformBlockIndex, GLuint uniformBlockBinding):
    cglUniformBlockBinding(program, uniformBlockIndex, uniformBlockBinding)

cpdef void glBindBufferRange(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size):
    cglBindBufferRange(target, index, buffer, offset, size)

cpdef void glBindBufferBase(GLenum target, GLuint index, GLuint buffer):
    cglBindBufferBase(target, index, buffer)

cpdef void glGetIntegeri_v(GLenum target, GLuint index, GLint *data):
    cglGetIntegeri_v(target, index, data)
