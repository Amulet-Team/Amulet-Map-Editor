# cython: language_level=3, boundscheck=False, wraparound=False

ctypedef void (*GL_USE_PROGRAM)(GLuint program)
ctypedef void (*GL_UNIFORM_MATRIX_4FV)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_UNIFORM_1I)(GLint location, GLint v0)
ctypedef void (*GL_BIND_VERTEX_ARRAY)(GLuint array)
ctypedef void (*GL_ACTIVE_TEXTURE)(GLenum texture)

# Initialise the functions with null pointers
cdef GL_USE_PROGRAM cglUseProgram = NULL
cdef GL_UNIFORM_MATRIX_4FV cglUniformMatrix4fv = NULL
cdef GL_UNIFORM_1I cglUniform1i = NULL
cdef GL_BIND_VERTEX_ARRAY cglBindVertexArray = NULL
cdef GL_ACTIVE_TEXTURE cglActiveTexture = NULL

# Define the loader functions. These will only run once and patch in the real function
cdef void GetglUseProgram(GLuint program):
    global cglUseProgram
    cglUseProgram = <GL_USE_PROGRAM>wglGetProcAddress(b"glUseProgram")
    cglUseProgram(program)

cdef void GetglUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix4fv
    cglUniformMatrix4fv = <GL_UNIFORM_MATRIX_4FV>wglGetProcAddress(b"glUniformMatrix4fv")
    cglUniformMatrix4fv(location, count, transpose, value)

cdef void GetglUniform1i(GLint location, GLint v0):
    global cglUniform1i
    cglUniform1i = <GL_UNIFORM_1I>wglGetProcAddress(b"glUniform1i")
    cglUniform1i(location, v0)

cdef void GetglBindVertexArray(GLuint array):
    global cglBindVertexArray
    cglBindVertexArray = <GL_BIND_VERTEX_ARRAY>wglGetProcAddress(b"glBindVertexArray")
    cglBindVertexArray(array)

cdef void GetglActiveTexture(GLenum texture):
    global cglActiveTexture
    cglActiveTexture = <GL_ACTIVE_TEXTURE>wglGetProcAddress(b"glActiveTexture")
    cglActiveTexture(texture)

# Set the functions to the loader functions
cglUseProgram = GetglUseProgram
cglUniformMatrix4fv = GetglUniformMatrix4fv
cglUniform1i = GetglUniform1i
cglBindVertexArray = GetglBindVertexArray
cglActiveTexture = GetglActiveTexture

# The public functions
cpdef void glUseProgram(GLuint program):
    cglUseProgram(program)

cpdef void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat[:] value):
    cglUniformMatrix4fv(location, count, transpose, &value[0])

cpdef void glUniform1i(GLint location, GLint v0):
    cglUniform1i(location, v0)

cpdef void glBindVertexArray(GLuint array):
    cglBindVertexArray(array)

cpdef void glActiveTexture(GLenum texture):
    cglActiveTexture(texture)
