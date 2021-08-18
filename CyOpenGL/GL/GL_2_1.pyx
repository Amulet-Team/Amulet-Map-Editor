# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_PIXEL_PACK_BUFFER = 0x88EB
cdef GLenum GL_PIXEL_UNPACK_BUFFER = 0x88EC
cdef GLenum GL_PIXEL_PACK_BUFFER_BINDING = 0x88ED
cdef GLenum GL_PIXEL_UNPACK_BUFFER_BINDING = 0x88EF
cdef GLenum GL_FLOAT_MAT2x3 = 0x8B65
cdef GLenum GL_FLOAT_MAT2x4 = 0x8B66
cdef GLenum GL_FLOAT_MAT3x2 = 0x8B67
cdef GLenum GL_FLOAT_MAT3x4 = 0x8B68
cdef GLenum GL_FLOAT_MAT4x2 = 0x8B69
cdef GLenum GL_FLOAT_MAT4x3 = 0x8B6A
cdef GLenum GL_SRGB = 0x8C40
cdef GLenum GL_SRGB8 = 0x8C41
cdef GLenum GL_SRGB_ALPHA = 0x8C42
cdef GLenum GL_SRGB8_ALPHA8 = 0x8C43
cdef GLenum GL_COMPRESSED_SRGB = 0x8C48
cdef GLenum GL_COMPRESSED_SRGB_ALPHA = 0x8C49
cdef GLenum GL_CURRENT_RASTER_SECONDARY_COLOR = 0x845F
cdef GLenum GL_SLUMINANCE_ALPHA = 0x8C44
cdef GLenum GL_SLUMINANCE8_ALPHA8 = 0x8C45
cdef GLenum GL_SLUMINANCE = 0x8C46
cdef GLenum GL_SLUMINANCE8 = 0x8C47
cdef GLenum GL_COMPRESSED_SLUMINANCE = 0x8C4A
cdef GLenum GL_COMPRESSED_SLUMINANCE_ALPHA = 0x8C4B

ctypedef void (*GL_UNIFORM_MATRIX2X3FV)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_UNIFORM_MATRIX3X2FV)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_UNIFORM_MATRIX2X4FV)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_UNIFORM_MATRIX4X2FV)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_UNIFORM_MATRIX3X4FV)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_UNIFORM_MATRIX4X3FV)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)

cdef GL_UNIFORM_MATRIX2X3FV cglUniformMatrix2x3fv = NULL
cdef GL_UNIFORM_MATRIX3X2FV cglUniformMatrix3x2fv = NULL
cdef GL_UNIFORM_MATRIX2X4FV cglUniformMatrix2x4fv = NULL
cdef GL_UNIFORM_MATRIX4X2FV cglUniformMatrix4x2fv = NULL
cdef GL_UNIFORM_MATRIX3X4FV cglUniformMatrix3x4fv = NULL
cdef GL_UNIFORM_MATRIX4X3FV cglUniformMatrix4x3fv = NULL


cdef void GetglUniformMatrix2x3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix2x3fv
    cglUniformMatrix2x3fv = <GL_UNIFORM_MATRIX2X3FV>getFunction(b"glUniformMatrix2x3fv")
    cglUniformMatrix2x3fv(location, count, transpose, value)

cdef void GetglUniformMatrix3x2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix3x2fv
    cglUniformMatrix3x2fv = <GL_UNIFORM_MATRIX3X2FV>getFunction(b"glUniformMatrix3x2fv")
    cglUniformMatrix3x2fv(location, count, transpose, value)

cdef void GetglUniformMatrix2x4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix2x4fv
    cglUniformMatrix2x4fv = <GL_UNIFORM_MATRIX2X4FV>getFunction(b"glUniformMatrix2x4fv")
    cglUniformMatrix2x4fv(location, count, transpose, value)

cdef void GetglUniformMatrix4x2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix4x2fv
    cglUniformMatrix4x2fv = <GL_UNIFORM_MATRIX4X2FV>getFunction(b"glUniformMatrix4x2fv")
    cglUniformMatrix4x2fv(location, count, transpose, value)

cdef void GetglUniformMatrix3x4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix3x4fv
    cglUniformMatrix3x4fv = <GL_UNIFORM_MATRIX3X4FV>getFunction(b"glUniformMatrix3x4fv")
    cglUniformMatrix3x4fv(location, count, transpose, value)

cdef void GetglUniformMatrix4x3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix4x3fv
    cglUniformMatrix4x3fv = <GL_UNIFORM_MATRIX4X3FV>getFunction(b"glUniformMatrix4x3fv")
    cglUniformMatrix4x3fv(location, count, transpose, value)

cglUniformMatrix2x3fv = GetglUniformMatrix2x3fv
cglUniformMatrix3x2fv = GetglUniformMatrix3x2fv
cglUniformMatrix2x4fv = GetglUniformMatrix2x4fv
cglUniformMatrix4x2fv = GetglUniformMatrix4x2fv
cglUniformMatrix3x4fv = GetglUniformMatrix3x4fv
cglUniformMatrix4x3fv = GetglUniformMatrix4x3fv


cpdef void glUniformMatrix2x3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix2x3fv(location, count, transpose, value)

cpdef void glUniformMatrix3x2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix3x2fv(location, count, transpose, value)

cpdef void glUniformMatrix2x4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix2x4fv(location, count, transpose, value)

cpdef void glUniformMatrix4x2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix4x2fv(location, count, transpose, value)

cpdef void glUniformMatrix3x4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix3x4fv(location, count, transpose, value)

cpdef void glUniformMatrix4x3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix4x3fv(location, count, transpose, value)
