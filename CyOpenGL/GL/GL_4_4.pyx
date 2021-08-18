# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_MAX_VERTEX_ATTRIB_STRIDE = 0x82E5
cdef GLenum GL_PRIMITIVE_RESTART_FOR_PATCHES_SUPPORTED = 0x8221
cdef GLenum GL_TEXTURE_BUFFER_BINDING = 0x8C2A
cdef GLenum GL_MAP_READ_BIT = 0x0001
cdef GLenum GL_MAP_WRITE_BIT = 0x0002
cdef GLenum GL_MAP_PERSISTENT_BIT = 0x0040
cdef GLenum GL_MAP_COHERENT_BIT = 0x0080
cdef GLenum GL_DYNAMIC_STORAGE_BIT = 0x0100
cdef GLenum GL_CLIENT_STORAGE_BIT = 0x0200
cdef GLenum GL_CLIENT_MAPPED_BUFFER_BARRIER_BIT = 0x00004000
cdef GLenum GL_BUFFER_IMMUTABLE_STORAGE = 0x821F
cdef GLenum GL_BUFFER_STORAGE_FLAGS = 0x8220
cdef GLenum GL_CLEAR_TEXTURE = 0x9365
cdef GLenum GL_LOCATION_COMPONENT = 0x934A
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER = 0x8C8E
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_INDEX = 0x934B
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_STRIDE = 0x934C
cdef GLenum GL_QUERY_BUFFER = 0x9192
cdef GLenum GL_QUERY_BUFFER_BARRIER_BIT = 0x00008000
cdef GLenum GL_QUERY_BUFFER_BINDING = 0x9193
cdef GLenum GL_QUERY_RESULT_NO_WAIT = 0x9194
cdef GLenum GL_MIRROR_CLAMP_TO_EDGE = 0x8743
cdef GLenum GL_STENCIL_INDEX = 0x1901
cdef GLenum GL_STENCIL_INDEX8 = 0x8D48
cdef GLenum GL_UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B

ctypedef void (*GL_BUFFER_STORAGE)(GLenum target, GLsizeiptr size, const void *data, GLbitfield flags)
ctypedef void (*GL_CLEAR_TEX_IMAGE)(GLuint texture, GLint level, GLenum format, GLenum type, const void *data)
ctypedef void (*GL_CLEAR_TEX_SUB_IMAGE)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *data)
ctypedef void (*GL_BIND_BUFFERS_BASE)(GLenum target, GLuint first, GLsizei count, const GLuint *buffers)
ctypedef void (*GL_BIND_BUFFERS_RANGE)(GLenum target, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizeiptr *sizes)
ctypedef void (*GL_BIND_TEXTURES)(GLuint first, GLsizei count, const GLuint *textures)
ctypedef void (*GL_BIND_SAMPLERS)(GLuint first, GLsizei count, const GLuint *samplers)
ctypedef void (*GL_BIND_IMAGE_TEXTURES)(GLuint first, GLsizei count, const GLuint *textures)
ctypedef void (*GL_BIND_VERTEX_BUFFERS)(GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides)

cdef GL_BUFFER_STORAGE cglBufferStorage = NULL
cdef GL_CLEAR_TEX_IMAGE cglClearTexImage = NULL
cdef GL_CLEAR_TEX_SUB_IMAGE cglClearTexSubImage = NULL
cdef GL_BIND_BUFFERS_BASE cglBindBuffersBase = NULL
cdef GL_BIND_BUFFERS_RANGE cglBindBuffersRange = NULL
cdef GL_BIND_TEXTURES cglBindTextures = NULL
cdef GL_BIND_SAMPLERS cglBindSamplers = NULL
cdef GL_BIND_IMAGE_TEXTURES cglBindImageTextures = NULL
cdef GL_BIND_VERTEX_BUFFERS cglBindVertexBuffers = NULL


cdef void GetglBufferStorage(GLenum target, GLsizeiptr size, const void *data, GLbitfield flags):
    global cglBufferStorage
    cglBufferStorage = <GL_BUFFER_STORAGE>getFunction(b"glBufferStorage")
    cglBufferStorage(target, size, data, flags)

cdef void GetglClearTexImage(GLuint texture, GLint level, GLenum format, GLenum type, const void *data):
    global cglClearTexImage
    cglClearTexImage = <GL_CLEAR_TEX_IMAGE>getFunction(b"glClearTexImage")
    cglClearTexImage(texture, level, format, type, data)

cdef void GetglClearTexSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *data):
    global cglClearTexSubImage
    cglClearTexSubImage = <GL_CLEAR_TEX_SUB_IMAGE>getFunction(b"glClearTexSubImage")
    cglClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data)

cdef void GetglBindBuffersBase(GLenum target, GLuint first, GLsizei count, const GLuint *buffers):
    global cglBindBuffersBase
    cglBindBuffersBase = <GL_BIND_BUFFERS_BASE>getFunction(b"glBindBuffersBase")
    cglBindBuffersBase(target, first, count, buffers)

cdef void GetglBindBuffersRange(GLenum target, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizeiptr *sizes):
    global cglBindBuffersRange
    cglBindBuffersRange = <GL_BIND_BUFFERS_RANGE>getFunction(b"glBindBuffersRange")
    cglBindBuffersRange(target, first, count, buffers, offsets, sizes)

cdef void GetglBindTextures(GLuint first, GLsizei count, const GLuint *textures):
    global cglBindTextures
    cglBindTextures = <GL_BIND_TEXTURES>getFunction(b"glBindTextures")
    cglBindTextures(first, count, textures)

cdef void GetglBindSamplers(GLuint first, GLsizei count, const GLuint *samplers):
    global cglBindSamplers
    cglBindSamplers = <GL_BIND_SAMPLERS>getFunction(b"glBindSamplers")
    cglBindSamplers(first, count, samplers)

cdef void GetglBindImageTextures(GLuint first, GLsizei count, const GLuint *textures):
    global cglBindImageTextures
    cglBindImageTextures = <GL_BIND_IMAGE_TEXTURES>getFunction(b"glBindImageTextures")
    cglBindImageTextures(first, count, textures)

cdef void GetglBindVertexBuffers(GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides):
    global cglBindVertexBuffers
    cglBindVertexBuffers = <GL_BIND_VERTEX_BUFFERS>getFunction(b"glBindVertexBuffers")
    cglBindVertexBuffers(first, count, buffers, offsets, strides)

cglBufferStorage = GetglBufferStorage
cglClearTexImage = GetglClearTexImage
cglClearTexSubImage = GetglClearTexSubImage
cglBindBuffersBase = GetglBindBuffersBase
cglBindBuffersRange = GetglBindBuffersRange
cglBindTextures = GetglBindTextures
cglBindSamplers = GetglBindSamplers
cglBindImageTextures = GetglBindImageTextures
cglBindVertexBuffers = GetglBindVertexBuffers


cpdef void glBufferStorage(GLenum target, GLsizeiptr size, const void *data, GLbitfield flags):
    cglBufferStorage(target, size, data, flags)

cpdef void glClearTexImage(GLuint texture, GLint level, GLenum format, GLenum type, const void *data):
    cglClearTexImage(texture, level, format, type, data)

cpdef void glClearTexSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *data):
    cglClearTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, data)

cpdef void glBindBuffersBase(GLenum target, GLuint first, GLsizei count, const GLuint *buffers):
    cglBindBuffersBase(target, first, count, buffers)

cpdef void glBindBuffersRange(GLenum target, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizeiptr *sizes):
    cglBindBuffersRange(target, first, count, buffers, offsets, sizes)

cpdef void glBindTextures(GLuint first, GLsizei count, const GLuint *textures):
    cglBindTextures(first, count, textures)

cpdef void glBindSamplers(GLuint first, GLsizei count, const GLuint *samplers):
    cglBindSamplers(first, count, samplers)

cpdef void glBindImageTextures(GLuint first, GLsizei count, const GLuint *textures):
    cglBindImageTextures(first, count, textures)

cpdef void glBindVertexBuffers(GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides):
    cglBindVertexBuffers(first, count, buffers, offsets, strides)
