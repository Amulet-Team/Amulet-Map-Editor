# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_BLEND_EQUATION_RGB = 0x8009
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
cdef GLenum GL_CURRENT_VERTEX_ATTRIB = 0x8626
cdef GLenum GL_VERTEX_PROGRAM_POINT_SIZE = 0x8642
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
cdef GLenum GL_STENCIL_BACK_FUNC = 0x8800
cdef GLenum GL_STENCIL_BACK_FAIL = 0x8801
cdef GLenum GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
cdef GLenum GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
cdef GLenum GL_MAX_DRAW_BUFFERS = 0x8824
cdef GLenum GL_DRAW_BUFFER0 = 0x8825
cdef GLenum GL_DRAW_BUFFER1 = 0x8826
cdef GLenum GL_DRAW_BUFFER2 = 0x8827
cdef GLenum GL_DRAW_BUFFER3 = 0x8828
cdef GLenum GL_DRAW_BUFFER4 = 0x8829
cdef GLenum GL_DRAW_BUFFER5 = 0x882A
cdef GLenum GL_DRAW_BUFFER6 = 0x882B
cdef GLenum GL_DRAW_BUFFER7 = 0x882C
cdef GLenum GL_DRAW_BUFFER8 = 0x882D
cdef GLenum GL_DRAW_BUFFER9 = 0x882E
cdef GLenum GL_DRAW_BUFFER10 = 0x882F
cdef GLenum GL_DRAW_BUFFER11 = 0x8830
cdef GLenum GL_DRAW_BUFFER12 = 0x8831
cdef GLenum GL_DRAW_BUFFER13 = 0x8832
cdef GLenum GL_DRAW_BUFFER14 = 0x8833
cdef GLenum GL_DRAW_BUFFER15 = 0x8834
cdef GLenum GL_BLEND_EQUATION_ALPHA = 0x883D
cdef GLenum GL_MAX_VERTEX_ATTRIBS = 0x8869
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
cdef GLenum GL_MAX_TEXTURE_IMAGE_UNITS = 0x8872
cdef GLenum GL_FRAGMENT_SHADER = 0x8B30
cdef GLenum GL_VERTEX_SHADER = 0x8B31
cdef GLenum GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 0x8B49
cdef GLenum GL_MAX_VERTEX_UNIFORM_COMPONENTS = 0x8B4A
cdef GLenum GL_MAX_VARYING_FLOATS = 0x8B4B
cdef GLenum GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
cdef GLenum GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
cdef GLenum GL_SHADER_TYPE = 0x8B4F
cdef GLenum GL_FLOAT_VEC2 = 0x8B50
cdef GLenum GL_FLOAT_VEC3 = 0x8B51
cdef GLenum GL_FLOAT_VEC4 = 0x8B52
cdef GLenum GL_INT_VEC2 = 0x8B53
cdef GLenum GL_INT_VEC3 = 0x8B54
cdef GLenum GL_INT_VEC4 = 0x8B55
cdef GLenum GL_BOOL = 0x8B56
cdef GLenum GL_BOOL_VEC2 = 0x8B57
cdef GLenum GL_BOOL_VEC3 = 0x8B58
cdef GLenum GL_BOOL_VEC4 = 0x8B59
cdef GLenum GL_FLOAT_MAT2 = 0x8B5A
cdef GLenum GL_FLOAT_MAT3 = 0x8B5B
cdef GLenum GL_FLOAT_MAT4 = 0x8B5C
cdef GLenum GL_SAMPLER_1D = 0x8B5D
cdef GLenum GL_SAMPLER_2D = 0x8B5E
cdef GLenum GL_SAMPLER_3D = 0x8B5F
cdef GLenum GL_SAMPLER_CUBE = 0x8B60
cdef GLenum GL_SAMPLER_1D_SHADOW = 0x8B61
cdef GLenum GL_SAMPLER_2D_SHADOW = 0x8B62
cdef GLenum GL_DELETE_STATUS = 0x8B80
cdef GLenum GL_COMPILE_STATUS = 0x8B81
cdef GLenum GL_LINK_STATUS = 0x8B82
cdef GLenum GL_VALIDATE_STATUS = 0x8B83
cdef GLenum GL_INFO_LOG_LENGTH = 0x8B84
cdef GLenum GL_ATTACHED_SHADERS = 0x8B85
cdef GLenum GL_ACTIVE_UNIFORMS = 0x8B86
cdef GLenum GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
cdef GLenum GL_SHADER_SOURCE_LENGTH = 0x8B88
cdef GLenum GL_ACTIVE_ATTRIBUTES = 0x8B89
cdef GLenum GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
cdef GLenum GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 0x8B8B
cdef GLenum GL_SHADING_LANGUAGE_VERSION = 0x8B8C
cdef GLenum GL_CURRENT_PROGRAM = 0x8B8D
cdef GLenum GL_POINT_SPRITE_COORD_ORIGIN = 0x8CA0
cdef GLenum GL_LOWER_LEFT = 0x8CA1
cdef GLenum GL_UPPER_LEFT = 0x8CA2
cdef GLenum GL_STENCIL_BACK_REF = 0x8CA3
cdef GLenum GL_STENCIL_BACK_VALUE_MASK = 0x8CA4
cdef GLenum GL_STENCIL_BACK_WRITEMASK = 0x8CA5
cdef GLenum GL_VERTEX_PROGRAM_TWO_SIDE = 0x8643
cdef GLenum GL_POINT_SPRITE = 0x8861
cdef GLenum GL_COORD_REPLACE = 0x8862
cdef GLenum GL_MAX_TEXTURE_COORDS = 0x8871

ctypedef void (*GL_BLEND_EQUATION_SEPARATE)(GLenum modeRGB, GLenum modeAlpha)
ctypedef void (*GL_DRAW_BUFFERS)(GLsizei n, const GLenum *bufs)
ctypedef void (*GL_STENCIL_OP_SEPARATE)(GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass)
ctypedef void (*GL_STENCIL_FUNC_SEPARATE)(GLenum face, GLenum func, GLint ref, GLuint mask)
ctypedef void (*GL_STENCIL_MASK_SEPARATE)(GLenum face, GLuint mask)
ctypedef void (*GL_ATTACH_SHADER)(GLuint program, GLuint shader)
ctypedef void (*GL_BIND_ATTRIB_LOCATION)(GLuint program, GLuint index, const GLchar *name)
ctypedef void (*GL_COMPILE_SHADER)(GLuint shader)
ctypedef GLuint (*GL_CREATE_PROGRAM)()
ctypedef GLuint (*GL_CREATE_SHADER)(GLenum type)
ctypedef void (*GL_DELETE_PROGRAM)(GLuint program)
ctypedef void (*GL_DELETE_SHADER)(GLuint shader)
ctypedef void (*GL_DETACH_SHADER)(GLuint program, GLuint shader)
ctypedef void (*GL_DISABLE_VERTEX_ATTRIB_ARRAY)(GLuint index)
ctypedef void (*GL_ENABLE_VERTEX_ATTRIB_ARRAY)(GLuint index)
ctypedef void (*GL_GET_ACTIVE_ATTRIB)(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name)
ctypedef void (*GL_GET_ACTIVE_UNIFORM)(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name)
ctypedef void (*GL_GET_ATTACHED_SHADERS)(GLuint program, GLsizei maxCount, GLsizei *count, GLuint *shaders)
ctypedef GLint (*GL_GET_ATTRIB_LOCATION)(GLuint program, const GLchar *name)
ctypedef void (*GL_GET_PROGRAMIV)(GLuint program, GLenum pname, GLint *params)
ctypedef void (*GL_GET_PROGRAM_INFO_LOG)(GLuint program, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
ctypedef void (*GL_GET_SHADERIV)(GLuint shader, GLenum pname, GLint *params)
ctypedef void (*GL_GET_SHADER_INFO_LOG)(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
ctypedef void (*GL_GET_SHADER_SOURCE)(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *source)
ctypedef GLint (*GL_GET_UNIFORM_LOCATION)(GLuint program, const GLchar *name)
ctypedef void (*GL_GET_UNIFORMFV)(GLuint program, GLint location, GLfloat *params)
ctypedef void (*GL_GET_UNIFORMIV)(GLuint program, GLint location, GLint *params)
ctypedef void (*GL_GET_VERTEX_ATTRIBDV)(GLuint index, GLenum pname, GLdouble *params)
ctypedef void (*GL_GET_VERTEX_ATTRIBFV)(GLuint index, GLenum pname, GLfloat *params)
ctypedef void (*GL_GET_VERTEX_ATTRIBIV)(GLuint index, GLenum pname, GLint *params)
ctypedef void (*GL_GET_VERTEX_ATTRIB_POINTERV)(GLuint index, GLenum pname, void **pointer)
ctypedef GLboolean (*GL_IS_PROGRAM)(GLuint program)
ctypedef GLboolean (*GL_IS_SHADER)(GLuint shader)
ctypedef void (*GL_LINK_PROGRAM)(GLuint program)
ctypedef void (*GL_SHADER_SOURCE)(GLuint shader, GLsizei count, const GLchar *const*string, const GLint *length)
ctypedef void (*GL_USE_PROGRAM)(GLuint program)
ctypedef void (*GL_UNIFORM1F)(GLint location, GLfloat v0)
ctypedef void (*GL_UNIFORM2F)(GLint location, GLfloat v0, GLfloat v1)
ctypedef void (*GL_UNIFORM3F)(GLint location, GLfloat v0, GLfloat v1, GLfloat v2)
ctypedef void (*GL_UNIFORM4F)(GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
ctypedef void (*GL_UNIFORM1I)(GLint location, GLint v0)
ctypedef void (*GL_UNIFORM2I)(GLint location, GLint v0, GLint v1)
ctypedef void (*GL_UNIFORM3I)(GLint location, GLint v0, GLint v1, GLint v2)
ctypedef void (*GL_UNIFORM4I)(GLint location, GLint v0, GLint v1, GLint v2, GLint v3)
ctypedef void (*GL_UNIFORM1FV)(GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*GL_UNIFORM2FV)(GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*GL_UNIFORM3FV)(GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*GL_UNIFORM4FV)(GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*GL_UNIFORM1IV)(GLint location, GLsizei count, const GLint *value)
ctypedef void (*GL_UNIFORM2IV)(GLint location, GLsizei count, const GLint *value)
ctypedef void (*GL_UNIFORM3IV)(GLint location, GLsizei count, const GLint *value)
ctypedef void (*GL_UNIFORM4IV)(GLint location, GLsizei count, const GLint *value)
ctypedef void (*GL_UNIFORM_MATRIX2FV)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_UNIFORM_MATRIX3FV)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_UNIFORM_MATRIX4FV)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*GL_VALIDATE_PROGRAM)(GLuint program)
ctypedef void (*GL_VERTEX_ATTRIB1D)(GLuint index, GLdouble x)
ctypedef void (*GL_VERTEX_ATTRIB1DV)(GLuint index, const GLdouble *v)
ctypedef void (*GL_VERTEX_ATTRIB1F)(GLuint index, GLfloat x)
ctypedef void (*GL_VERTEX_ATTRIB1FV)(GLuint index, const GLfloat *v)
ctypedef void (*GL_VERTEX_ATTRIB1S)(GLuint index, GLshort x)
ctypedef void (*GL_VERTEX_ATTRIB1SV)(GLuint index, const GLshort *v)
ctypedef void (*GL_VERTEX_ATTRIB2D)(GLuint index, GLdouble x, GLdouble y)
ctypedef void (*GL_VERTEX_ATTRIB2DV)(GLuint index, const GLdouble *v)
ctypedef void (*GL_VERTEX_ATTRIB2F)(GLuint index, GLfloat x, GLfloat y)
ctypedef void (*GL_VERTEX_ATTRIB2FV)(GLuint index, const GLfloat *v)
ctypedef void (*GL_VERTEX_ATTRIB2S)(GLuint index, GLshort x, GLshort y)
ctypedef void (*GL_VERTEX_ATTRIB2SV)(GLuint index, const GLshort *v)
ctypedef void (*GL_VERTEX_ATTRIB3D)(GLuint index, GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*GL_VERTEX_ATTRIB3DV)(GLuint index, const GLdouble *v)
ctypedef void (*GL_VERTEX_ATTRIB3F)(GLuint index, GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*GL_VERTEX_ATTRIB3FV)(GLuint index, const GLfloat *v)
ctypedef void (*GL_VERTEX_ATTRIB3S)(GLuint index, GLshort x, GLshort y, GLshort z)
ctypedef void (*GL_VERTEX_ATTRIB3SV)(GLuint index, const GLshort *v)
ctypedef void (*GL_VERTEX_ATTRIB4_NBV)(GLuint index, const GLbyte *v)
ctypedef void (*GL_VERTEX_ATTRIB4_NIV)(GLuint index, const GLint *v)
ctypedef void (*GL_VERTEX_ATTRIB4_NSV)(GLuint index, const GLshort *v)
ctypedef void (*GL_VERTEX_ATTRIB4_NUB)(GLuint index, GLubyte x, GLubyte y, GLubyte z, GLubyte w)
ctypedef void (*GL_VERTEX_ATTRIB4_NUBV)(GLuint index, const GLubyte *v)
ctypedef void (*GL_VERTEX_ATTRIB4_NUIV)(GLuint index, const GLuint *v)
ctypedef void (*GL_VERTEX_ATTRIB4_NUSV)(GLuint index, const GLushort *v)
ctypedef void (*GL_VERTEX_ATTRIB4BV)(GLuint index, const GLbyte *v)
ctypedef void (*GL_VERTEX_ATTRIB4D)(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*GL_VERTEX_ATTRIB4DV)(GLuint index, const GLdouble *v)
ctypedef void (*GL_VERTEX_ATTRIB4F)(GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w)
ctypedef void (*GL_VERTEX_ATTRIB4FV)(GLuint index, const GLfloat *v)
ctypedef void (*GL_VERTEX_ATTRIB4IV)(GLuint index, const GLint *v)
ctypedef void (*GL_VERTEX_ATTRIB4S)(GLuint index, GLshort x, GLshort y, GLshort z, GLshort w)
ctypedef void (*GL_VERTEX_ATTRIB4SV)(GLuint index, const GLshort *v)
ctypedef void (*GL_VERTEX_ATTRIB4UBV)(GLuint index, const GLubyte *v)
ctypedef void (*GL_VERTEX_ATTRIB4UIV)(GLuint index, const GLuint *v)
ctypedef void (*GL_VERTEX_ATTRIB4USV)(GLuint index, const GLushort *v)
ctypedef void (*GL_VERTEX_ATTRIB_POINTER)(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void *pointer)

cdef GL_BLEND_EQUATION_SEPARATE cglBlendEquationSeparate = NULL
cdef GL_DRAW_BUFFERS cglDrawBuffers = NULL
cdef GL_STENCIL_OP_SEPARATE cglStencilOpSeparate = NULL
cdef GL_STENCIL_FUNC_SEPARATE cglStencilFuncSeparate = NULL
cdef GL_STENCIL_MASK_SEPARATE cglStencilMaskSeparate = NULL
cdef GL_ATTACH_SHADER cglAttachShader = NULL
cdef GL_BIND_ATTRIB_LOCATION cglBindAttribLocation = NULL
cdef GL_COMPILE_SHADER cglCompileShader = NULL
cdef GL_CREATE_PROGRAM cglCreateProgram = NULL
cdef GL_CREATE_SHADER cglCreateShader = NULL
cdef GL_DELETE_PROGRAM cglDeleteProgram = NULL
cdef GL_DELETE_SHADER cglDeleteShader = NULL
cdef GL_DETACH_SHADER cglDetachShader = NULL
cdef GL_DISABLE_VERTEX_ATTRIB_ARRAY cglDisableVertexAttribArray = NULL
cdef GL_ENABLE_VERTEX_ATTRIB_ARRAY cglEnableVertexAttribArray = NULL
cdef GL_GET_ACTIVE_ATTRIB cglGetActiveAttrib = NULL
cdef GL_GET_ACTIVE_UNIFORM cglGetActiveUniform = NULL
cdef GL_GET_ATTACHED_SHADERS cglGetAttachedShaders = NULL
cdef GL_GET_ATTRIB_LOCATION cglGetAttribLocation = NULL
cdef GL_GET_PROGRAMIV cglGetProgramiv = NULL
cdef GL_GET_PROGRAM_INFO_LOG cglGetProgramInfoLog = NULL
cdef GL_GET_SHADERIV cglGetShaderiv = NULL
cdef GL_GET_SHADER_INFO_LOG cglGetShaderInfoLog = NULL
cdef GL_GET_SHADER_SOURCE cglGetShaderSource = NULL
cdef GL_GET_UNIFORM_LOCATION cglGetUniformLocation = NULL
cdef GL_GET_UNIFORMFV cglGetUniformfv = NULL
cdef GL_GET_UNIFORMIV cglGetUniformiv = NULL
cdef GL_GET_VERTEX_ATTRIBDV cglGetVertexAttribdv = NULL
cdef GL_GET_VERTEX_ATTRIBFV cglGetVertexAttribfv = NULL
cdef GL_GET_VERTEX_ATTRIBIV cglGetVertexAttribiv = NULL
cdef GL_GET_VERTEX_ATTRIB_POINTERV cglGetVertexAttribPointerv = NULL
cdef GL_IS_PROGRAM cglIsProgram = NULL
cdef GL_IS_SHADER cglIsShader = NULL
cdef GL_LINK_PROGRAM cglLinkProgram = NULL
cdef GL_SHADER_SOURCE cglShaderSource = NULL
cdef GL_USE_PROGRAM cglUseProgram = NULL
cdef GL_UNIFORM1F cglUniform1f = NULL
cdef GL_UNIFORM2F cglUniform2f = NULL
cdef GL_UNIFORM3F cglUniform3f = NULL
cdef GL_UNIFORM4F cglUniform4f = NULL
cdef GL_UNIFORM1I cglUniform1i = NULL
cdef GL_UNIFORM2I cglUniform2i = NULL
cdef GL_UNIFORM3I cglUniform3i = NULL
cdef GL_UNIFORM4I cglUniform4i = NULL
cdef GL_UNIFORM1FV cglUniform1fv = NULL
cdef GL_UNIFORM2FV cglUniform2fv = NULL
cdef GL_UNIFORM3FV cglUniform3fv = NULL
cdef GL_UNIFORM4FV cglUniform4fv = NULL
cdef GL_UNIFORM1IV cglUniform1iv = NULL
cdef GL_UNIFORM2IV cglUniform2iv = NULL
cdef GL_UNIFORM3IV cglUniform3iv = NULL
cdef GL_UNIFORM4IV cglUniform4iv = NULL
cdef GL_UNIFORM_MATRIX2FV cglUniformMatrix2fv = NULL
cdef GL_UNIFORM_MATRIX3FV cglUniformMatrix3fv = NULL
cdef GL_UNIFORM_MATRIX4FV cglUniformMatrix4fv = NULL
cdef GL_VALIDATE_PROGRAM cglValidateProgram = NULL
cdef GL_VERTEX_ATTRIB1D cglVertexAttrib1d = NULL
cdef GL_VERTEX_ATTRIB1DV cglVertexAttrib1dv = NULL
cdef GL_VERTEX_ATTRIB1F cglVertexAttrib1f = NULL
cdef GL_VERTEX_ATTRIB1FV cglVertexAttrib1fv = NULL
cdef GL_VERTEX_ATTRIB1S cglVertexAttrib1s = NULL
cdef GL_VERTEX_ATTRIB1SV cglVertexAttrib1sv = NULL
cdef GL_VERTEX_ATTRIB2D cglVertexAttrib2d = NULL
cdef GL_VERTEX_ATTRIB2DV cglVertexAttrib2dv = NULL
cdef GL_VERTEX_ATTRIB2F cglVertexAttrib2f = NULL
cdef GL_VERTEX_ATTRIB2FV cglVertexAttrib2fv = NULL
cdef GL_VERTEX_ATTRIB2S cglVertexAttrib2s = NULL
cdef GL_VERTEX_ATTRIB2SV cglVertexAttrib2sv = NULL
cdef GL_VERTEX_ATTRIB3D cglVertexAttrib3d = NULL
cdef GL_VERTEX_ATTRIB3DV cglVertexAttrib3dv = NULL
cdef GL_VERTEX_ATTRIB3F cglVertexAttrib3f = NULL
cdef GL_VERTEX_ATTRIB3FV cglVertexAttrib3fv = NULL
cdef GL_VERTEX_ATTRIB3S cglVertexAttrib3s = NULL
cdef GL_VERTEX_ATTRIB3SV cglVertexAttrib3sv = NULL
cdef GL_VERTEX_ATTRIB4_NBV cglVertexAttrib4Nbv = NULL
cdef GL_VERTEX_ATTRIB4_NIV cglVertexAttrib4Niv = NULL
cdef GL_VERTEX_ATTRIB4_NSV cglVertexAttrib4Nsv = NULL
cdef GL_VERTEX_ATTRIB4_NUB cglVertexAttrib4Nub = NULL
cdef GL_VERTEX_ATTRIB4_NUBV cglVertexAttrib4Nubv = NULL
cdef GL_VERTEX_ATTRIB4_NUIV cglVertexAttrib4Nuiv = NULL
cdef GL_VERTEX_ATTRIB4_NUSV cglVertexAttrib4Nusv = NULL
cdef GL_VERTEX_ATTRIB4BV cglVertexAttrib4bv = NULL
cdef GL_VERTEX_ATTRIB4D cglVertexAttrib4d = NULL
cdef GL_VERTEX_ATTRIB4DV cglVertexAttrib4dv = NULL
cdef GL_VERTEX_ATTRIB4F cglVertexAttrib4f = NULL
cdef GL_VERTEX_ATTRIB4FV cglVertexAttrib4fv = NULL
cdef GL_VERTEX_ATTRIB4IV cglVertexAttrib4iv = NULL
cdef GL_VERTEX_ATTRIB4S cglVertexAttrib4s = NULL
cdef GL_VERTEX_ATTRIB4SV cglVertexAttrib4sv = NULL
cdef GL_VERTEX_ATTRIB4UBV cglVertexAttrib4ubv = NULL
cdef GL_VERTEX_ATTRIB4UIV cglVertexAttrib4uiv = NULL
cdef GL_VERTEX_ATTRIB4USV cglVertexAttrib4usv = NULL
cdef GL_VERTEX_ATTRIB_POINTER cglVertexAttribPointer = NULL


cdef void GetglBlendEquationSeparate(GLenum modeRGB, GLenum modeAlpha):
    global cglBlendEquationSeparate
    cglBlendEquationSeparate = <GL_BLEND_EQUATION_SEPARATE>getFunction(b"glBlendEquationSeparate")
    cglBlendEquationSeparate(modeRGB, modeAlpha)

cdef void GetglDrawBuffers(GLsizei n, const GLenum *bufs):
    global cglDrawBuffers
    cglDrawBuffers = <GL_DRAW_BUFFERS>getFunction(b"glDrawBuffers")
    cglDrawBuffers(n, bufs)

cdef void GetglStencilOpSeparate(GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass):
    global cglStencilOpSeparate
    cglStencilOpSeparate = <GL_STENCIL_OP_SEPARATE>getFunction(b"glStencilOpSeparate")
    cglStencilOpSeparate(face, sfail, dpfail, dppass)

cdef void GetglStencilFuncSeparate(GLenum face, GLenum func, GLint ref, GLuint mask):
    global cglStencilFuncSeparate
    cglStencilFuncSeparate = <GL_STENCIL_FUNC_SEPARATE>getFunction(b"glStencilFuncSeparate")
    cglStencilFuncSeparate(face, func, ref, mask)

cdef void GetglStencilMaskSeparate(GLenum face, GLuint mask):
    global cglStencilMaskSeparate
    cglStencilMaskSeparate = <GL_STENCIL_MASK_SEPARATE>getFunction(b"glStencilMaskSeparate")
    cglStencilMaskSeparate(face, mask)

cdef void GetglAttachShader(GLuint program, GLuint shader):
    global cglAttachShader
    cglAttachShader = <GL_ATTACH_SHADER>getFunction(b"glAttachShader")
    cglAttachShader(program, shader)

cdef void GetglBindAttribLocation(GLuint program, GLuint index, const GLchar *name):
    global cglBindAttribLocation
    cglBindAttribLocation = <GL_BIND_ATTRIB_LOCATION>getFunction(b"glBindAttribLocation")
    cglBindAttribLocation(program, index, name)

cdef void GetglCompileShader(GLuint shader):
    global cglCompileShader
    cglCompileShader = <GL_COMPILE_SHADER>getFunction(b"glCompileShader")
    cglCompileShader(shader)

cdef GLuint GetglCreateProgram():
    global cglCreateProgram
    cglCreateProgram = <GL_CREATE_PROGRAM>getFunction(b"glCreateProgram")
    cglCreateProgram()

cdef GLuint GetglCreateShader(GLenum type):
    global cglCreateShader
    cglCreateShader = <GL_CREATE_SHADER>getFunction(b"glCreateShader")
    cglCreateShader(type)

cdef void GetglDeleteProgram(GLuint program):
    global cglDeleteProgram
    cglDeleteProgram = <GL_DELETE_PROGRAM>getFunction(b"glDeleteProgram")
    cglDeleteProgram(program)

cdef void GetglDeleteShader(GLuint shader):
    global cglDeleteShader
    cglDeleteShader = <GL_DELETE_SHADER>getFunction(b"glDeleteShader")
    cglDeleteShader(shader)

cdef void GetglDetachShader(GLuint program, GLuint shader):
    global cglDetachShader
    cglDetachShader = <GL_DETACH_SHADER>getFunction(b"glDetachShader")
    cglDetachShader(program, shader)

cdef void GetglDisableVertexAttribArray(GLuint index):
    global cglDisableVertexAttribArray
    cglDisableVertexAttribArray = <GL_DISABLE_VERTEX_ATTRIB_ARRAY>getFunction(b"glDisableVertexAttribArray")
    cglDisableVertexAttribArray(index)

cdef void GetglEnableVertexAttribArray(GLuint index):
    global cglEnableVertexAttribArray
    cglEnableVertexAttribArray = <GL_ENABLE_VERTEX_ATTRIB_ARRAY>getFunction(b"glEnableVertexAttribArray")
    cglEnableVertexAttribArray(index)

cdef void GetglGetActiveAttrib(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name):
    global cglGetActiveAttrib
    cglGetActiveAttrib = <GL_GET_ACTIVE_ATTRIB>getFunction(b"glGetActiveAttrib")
    cglGetActiveAttrib(program, index, bufSize, length, size, type, name)

cdef void GetglGetActiveUniform(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name):
    global cglGetActiveUniform
    cglGetActiveUniform = <GL_GET_ACTIVE_UNIFORM>getFunction(b"glGetActiveUniform")
    cglGetActiveUniform(program, index, bufSize, length, size, type, name)

cdef void GetglGetAttachedShaders(GLuint program, GLsizei maxCount, GLsizei *count, GLuint *shaders):
    global cglGetAttachedShaders
    cglGetAttachedShaders = <GL_GET_ATTACHED_SHADERS>getFunction(b"glGetAttachedShaders")
    cglGetAttachedShaders(program, maxCount, count, shaders)

cdef GLint GetglGetAttribLocation(GLuint program, const GLchar *name):
    global cglGetAttribLocation
    cglGetAttribLocation = <GL_GET_ATTRIB_LOCATION>getFunction(b"glGetAttribLocation")
    cglGetAttribLocation(program, name)

cdef void GetglGetProgramiv(GLuint program, GLenum pname, GLint *params):
    global cglGetProgramiv
    cglGetProgramiv = <GL_GET_PROGRAMIV>getFunction(b"glGetProgramiv")
    cglGetProgramiv(program, pname, params)

cdef void GetglGetProgramInfoLog(GLuint program, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    global cglGetProgramInfoLog
    cglGetProgramInfoLog = <GL_GET_PROGRAM_INFO_LOG>getFunction(b"glGetProgramInfoLog")
    cglGetProgramInfoLog(program, bufSize, length, infoLog)

cdef void GetglGetShaderiv(GLuint shader, GLenum pname, GLint *params):
    global cglGetShaderiv
    cglGetShaderiv = <GL_GET_SHADERIV>getFunction(b"glGetShaderiv")
    cglGetShaderiv(shader, pname, params)

cdef void GetglGetShaderInfoLog(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    global cglGetShaderInfoLog
    cglGetShaderInfoLog = <GL_GET_SHADER_INFO_LOG>getFunction(b"glGetShaderInfoLog")
    cglGetShaderInfoLog(shader, bufSize, length, infoLog)

cdef void GetglGetShaderSource(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *source):
    global cglGetShaderSource
    cglGetShaderSource = <GL_GET_SHADER_SOURCE>getFunction(b"glGetShaderSource")
    cglGetShaderSource(shader, bufSize, length, source)

cdef GLint GetglGetUniformLocation(GLuint program, const GLchar *name):
    global cglGetUniformLocation
    cglGetUniformLocation = <GL_GET_UNIFORM_LOCATION>getFunction(b"glGetUniformLocation")
    cglGetUniformLocation(program, name)

cdef void GetglGetUniformfv(GLuint program, GLint location, GLfloat *params):
    global cglGetUniformfv
    cglGetUniformfv = <GL_GET_UNIFORMFV>getFunction(b"glGetUniformfv")
    cglGetUniformfv(program, location, params)

cdef void GetglGetUniformiv(GLuint program, GLint location, GLint *params):
    global cglGetUniformiv
    cglGetUniformiv = <GL_GET_UNIFORMIV>getFunction(b"glGetUniformiv")
    cglGetUniformiv(program, location, params)

cdef void GetglGetVertexAttribdv(GLuint index, GLenum pname, GLdouble *params):
    global cglGetVertexAttribdv
    cglGetVertexAttribdv = <GL_GET_VERTEX_ATTRIBDV>getFunction(b"glGetVertexAttribdv")
    cglGetVertexAttribdv(index, pname, params)

cdef void GetglGetVertexAttribfv(GLuint index, GLenum pname, GLfloat *params):
    global cglGetVertexAttribfv
    cglGetVertexAttribfv = <GL_GET_VERTEX_ATTRIBFV>getFunction(b"glGetVertexAttribfv")
    cglGetVertexAttribfv(index, pname, params)

cdef void GetglGetVertexAttribiv(GLuint index, GLenum pname, GLint *params):
    global cglGetVertexAttribiv
    cglGetVertexAttribiv = <GL_GET_VERTEX_ATTRIBIV>getFunction(b"glGetVertexAttribiv")
    cglGetVertexAttribiv(index, pname, params)

cdef void GetglGetVertexAttribPointerv(GLuint index, GLenum pname, void **pointer):
    global cglGetVertexAttribPointerv
    cglGetVertexAttribPointerv = <GL_GET_VERTEX_ATTRIB_POINTERV>getFunction(b"glGetVertexAttribPointerv")
    cglGetVertexAttribPointerv(index, pname, pointer)

cdef GLboolean GetglIsProgram(GLuint program):
    global cglIsProgram
    cglIsProgram = <GL_IS_PROGRAM>getFunction(b"glIsProgram")
    cglIsProgram(program)

cdef GLboolean GetglIsShader(GLuint shader):
    global cglIsShader
    cglIsShader = <GL_IS_SHADER>getFunction(b"glIsShader")
    cglIsShader(shader)

cdef void GetglLinkProgram(GLuint program):
    global cglLinkProgram
    cglLinkProgram = <GL_LINK_PROGRAM>getFunction(b"glLinkProgram")
    cglLinkProgram(program)

cdef void GetglShaderSource(GLuint shader, GLsizei count, const GLchar *const*string, const GLint *length):
    global cglShaderSource
    cglShaderSource = <GL_SHADER_SOURCE>getFunction(b"glShaderSource")
    cglShaderSource(shader, count, string, length)

cdef void GetglUseProgram(GLuint program):
    global cglUseProgram
    cglUseProgram = <GL_USE_PROGRAM>getFunction(b"glUseProgram")
    cglUseProgram(program)

cdef void GetglUniform1f(GLint location, GLfloat v0):
    global cglUniform1f
    cglUniform1f = <GL_UNIFORM1F>getFunction(b"glUniform1f")
    cglUniform1f(location, v0)

cdef void GetglUniform2f(GLint location, GLfloat v0, GLfloat v1):
    global cglUniform2f
    cglUniform2f = <GL_UNIFORM2F>getFunction(b"glUniform2f")
    cglUniform2f(location, v0, v1)

cdef void GetglUniform3f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2):
    global cglUniform3f
    cglUniform3f = <GL_UNIFORM3F>getFunction(b"glUniform3f")
    cglUniform3f(location, v0, v1, v2)

cdef void GetglUniform4f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3):
    global cglUniform4f
    cglUniform4f = <GL_UNIFORM4F>getFunction(b"glUniform4f")
    cglUniform4f(location, v0, v1, v2, v3)

cdef void GetglUniform1i(GLint location, GLint v0):
    global cglUniform1i
    cglUniform1i = <GL_UNIFORM1I>getFunction(b"glUniform1i")
    cglUniform1i(location, v0)

cdef void GetglUniform2i(GLint location, GLint v0, GLint v1):
    global cglUniform2i
    cglUniform2i = <GL_UNIFORM2I>getFunction(b"glUniform2i")
    cglUniform2i(location, v0, v1)

cdef void GetglUniform3i(GLint location, GLint v0, GLint v1, GLint v2):
    global cglUniform3i
    cglUniform3i = <GL_UNIFORM3I>getFunction(b"glUniform3i")
    cglUniform3i(location, v0, v1, v2)

cdef void GetglUniform4i(GLint location, GLint v0, GLint v1, GLint v2, GLint v3):
    global cglUniform4i
    cglUniform4i = <GL_UNIFORM4I>getFunction(b"glUniform4i")
    cglUniform4i(location, v0, v1, v2, v3)

cdef void GetglUniform1fv(GLint location, GLsizei count, const GLfloat *value):
    global cglUniform1fv
    cglUniform1fv = <GL_UNIFORM1FV>getFunction(b"glUniform1fv")
    cglUniform1fv(location, count, value)

cdef void GetglUniform2fv(GLint location, GLsizei count, const GLfloat *value):
    global cglUniform2fv
    cglUniform2fv = <GL_UNIFORM2FV>getFunction(b"glUniform2fv")
    cglUniform2fv(location, count, value)

cdef void GetglUniform3fv(GLint location, GLsizei count, const GLfloat *value):
    global cglUniform3fv
    cglUniform3fv = <GL_UNIFORM3FV>getFunction(b"glUniform3fv")
    cglUniform3fv(location, count, value)

cdef void GetglUniform4fv(GLint location, GLsizei count, const GLfloat *value):
    global cglUniform4fv
    cglUniform4fv = <GL_UNIFORM4FV>getFunction(b"glUniform4fv")
    cglUniform4fv(location, count, value)

cdef void GetglUniform1iv(GLint location, GLsizei count, const GLint *value):
    global cglUniform1iv
    cglUniform1iv = <GL_UNIFORM1IV>getFunction(b"glUniform1iv")
    cglUniform1iv(location, count, value)

cdef void GetglUniform2iv(GLint location, GLsizei count, const GLint *value):
    global cglUniform2iv
    cglUniform2iv = <GL_UNIFORM2IV>getFunction(b"glUniform2iv")
    cglUniform2iv(location, count, value)

cdef void GetglUniform3iv(GLint location, GLsizei count, const GLint *value):
    global cglUniform3iv
    cglUniform3iv = <GL_UNIFORM3IV>getFunction(b"glUniform3iv")
    cglUniform3iv(location, count, value)

cdef void GetglUniform4iv(GLint location, GLsizei count, const GLint *value):
    global cglUniform4iv
    cglUniform4iv = <GL_UNIFORM4IV>getFunction(b"glUniform4iv")
    cglUniform4iv(location, count, value)

cdef void GetglUniformMatrix2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix2fv
    cglUniformMatrix2fv = <GL_UNIFORM_MATRIX2FV>getFunction(b"glUniformMatrix2fv")
    cglUniformMatrix2fv(location, count, transpose, value)

cdef void GetglUniformMatrix3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix3fv
    cglUniformMatrix3fv = <GL_UNIFORM_MATRIX3FV>getFunction(b"glUniformMatrix3fv")
    cglUniformMatrix3fv(location, count, transpose, value)

cdef void GetglUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix4fv
    cglUniformMatrix4fv = <GL_UNIFORM_MATRIX4FV>getFunction(b"glUniformMatrix4fv")
    cglUniformMatrix4fv(location, count, transpose, value)

cdef void GetglValidateProgram(GLuint program):
    global cglValidateProgram
    cglValidateProgram = <GL_VALIDATE_PROGRAM>getFunction(b"glValidateProgram")
    cglValidateProgram(program)

cdef void GetglVertexAttrib1d(GLuint index, GLdouble x):
    global cglVertexAttrib1d
    cglVertexAttrib1d = <GL_VERTEX_ATTRIB1D>getFunction(b"glVertexAttrib1d")
    cglVertexAttrib1d(index, x)

cdef void GetglVertexAttrib1dv(GLuint index, const GLdouble *v):
    global cglVertexAttrib1dv
    cglVertexAttrib1dv = <GL_VERTEX_ATTRIB1DV>getFunction(b"glVertexAttrib1dv")
    cglVertexAttrib1dv(index, v)

cdef void GetglVertexAttrib1f(GLuint index, GLfloat x):
    global cglVertexAttrib1f
    cglVertexAttrib1f = <GL_VERTEX_ATTRIB1F>getFunction(b"glVertexAttrib1f")
    cglVertexAttrib1f(index, x)

cdef void GetglVertexAttrib1fv(GLuint index, const GLfloat *v):
    global cglVertexAttrib1fv
    cglVertexAttrib1fv = <GL_VERTEX_ATTRIB1FV>getFunction(b"glVertexAttrib1fv")
    cglVertexAttrib1fv(index, v)

cdef void GetglVertexAttrib1s(GLuint index, GLshort x):
    global cglVertexAttrib1s
    cglVertexAttrib1s = <GL_VERTEX_ATTRIB1S>getFunction(b"glVertexAttrib1s")
    cglVertexAttrib1s(index, x)

cdef void GetglVertexAttrib1sv(GLuint index, const GLshort *v):
    global cglVertexAttrib1sv
    cglVertexAttrib1sv = <GL_VERTEX_ATTRIB1SV>getFunction(b"glVertexAttrib1sv")
    cglVertexAttrib1sv(index, v)

cdef void GetglVertexAttrib2d(GLuint index, GLdouble x, GLdouble y):
    global cglVertexAttrib2d
    cglVertexAttrib2d = <GL_VERTEX_ATTRIB2D>getFunction(b"glVertexAttrib2d")
    cglVertexAttrib2d(index, x, y)

cdef void GetglVertexAttrib2dv(GLuint index, const GLdouble *v):
    global cglVertexAttrib2dv
    cglVertexAttrib2dv = <GL_VERTEX_ATTRIB2DV>getFunction(b"glVertexAttrib2dv")
    cglVertexAttrib2dv(index, v)

cdef void GetglVertexAttrib2f(GLuint index, GLfloat x, GLfloat y):
    global cglVertexAttrib2f
    cglVertexAttrib2f = <GL_VERTEX_ATTRIB2F>getFunction(b"glVertexAttrib2f")
    cglVertexAttrib2f(index, x, y)

cdef void GetglVertexAttrib2fv(GLuint index, const GLfloat *v):
    global cglVertexAttrib2fv
    cglVertexAttrib2fv = <GL_VERTEX_ATTRIB2FV>getFunction(b"glVertexAttrib2fv")
    cglVertexAttrib2fv(index, v)

cdef void GetglVertexAttrib2s(GLuint index, GLshort x, GLshort y):
    global cglVertexAttrib2s
    cglVertexAttrib2s = <GL_VERTEX_ATTRIB2S>getFunction(b"glVertexAttrib2s")
    cglVertexAttrib2s(index, x, y)

cdef void GetglVertexAttrib2sv(GLuint index, const GLshort *v):
    global cglVertexAttrib2sv
    cglVertexAttrib2sv = <GL_VERTEX_ATTRIB2SV>getFunction(b"glVertexAttrib2sv")
    cglVertexAttrib2sv(index, v)

cdef void GetglVertexAttrib3d(GLuint index, GLdouble x, GLdouble y, GLdouble z):
    global cglVertexAttrib3d
    cglVertexAttrib3d = <GL_VERTEX_ATTRIB3D>getFunction(b"glVertexAttrib3d")
    cglVertexAttrib3d(index, x, y, z)

cdef void GetglVertexAttrib3dv(GLuint index, const GLdouble *v):
    global cglVertexAttrib3dv
    cglVertexAttrib3dv = <GL_VERTEX_ATTRIB3DV>getFunction(b"glVertexAttrib3dv")
    cglVertexAttrib3dv(index, v)

cdef void GetglVertexAttrib3f(GLuint index, GLfloat x, GLfloat y, GLfloat z):
    global cglVertexAttrib3f
    cglVertexAttrib3f = <GL_VERTEX_ATTRIB3F>getFunction(b"glVertexAttrib3f")
    cglVertexAttrib3f(index, x, y, z)

cdef void GetglVertexAttrib3fv(GLuint index, const GLfloat *v):
    global cglVertexAttrib3fv
    cglVertexAttrib3fv = <GL_VERTEX_ATTRIB3FV>getFunction(b"glVertexAttrib3fv")
    cglVertexAttrib3fv(index, v)

cdef void GetglVertexAttrib3s(GLuint index, GLshort x, GLshort y, GLshort z):
    global cglVertexAttrib3s
    cglVertexAttrib3s = <GL_VERTEX_ATTRIB3S>getFunction(b"glVertexAttrib3s")
    cglVertexAttrib3s(index, x, y, z)

cdef void GetglVertexAttrib3sv(GLuint index, const GLshort *v):
    global cglVertexAttrib3sv
    cglVertexAttrib3sv = <GL_VERTEX_ATTRIB3SV>getFunction(b"glVertexAttrib3sv")
    cglVertexAttrib3sv(index, v)

cdef void GetglVertexAttrib4Nbv(GLuint index, const GLbyte *v):
    global cglVertexAttrib4Nbv
    cglVertexAttrib4Nbv = <GL_VERTEX_ATTRIB4_NBV>getFunction(b"glVertexAttrib4Nbv")
    cglVertexAttrib4Nbv(index, v)

cdef void GetglVertexAttrib4Niv(GLuint index, const GLint *v):
    global cglVertexAttrib4Niv
    cglVertexAttrib4Niv = <GL_VERTEX_ATTRIB4_NIV>getFunction(b"glVertexAttrib4Niv")
    cglVertexAttrib4Niv(index, v)

cdef void GetglVertexAttrib4Nsv(GLuint index, const GLshort *v):
    global cglVertexAttrib4Nsv
    cglVertexAttrib4Nsv = <GL_VERTEX_ATTRIB4_NSV>getFunction(b"glVertexAttrib4Nsv")
    cglVertexAttrib4Nsv(index, v)

cdef void GetglVertexAttrib4Nub(GLuint index, GLubyte x, GLubyte y, GLubyte z, GLubyte w):
    global cglVertexAttrib4Nub
    cglVertexAttrib4Nub = <GL_VERTEX_ATTRIB4_NUB>getFunction(b"glVertexAttrib4Nub")
    cglVertexAttrib4Nub(index, x, y, z, w)

cdef void GetglVertexAttrib4Nubv(GLuint index, const GLubyte *v):
    global cglVertexAttrib4Nubv
    cglVertexAttrib4Nubv = <GL_VERTEX_ATTRIB4_NUBV>getFunction(b"glVertexAttrib4Nubv")
    cglVertexAttrib4Nubv(index, v)

cdef void GetglVertexAttrib4Nuiv(GLuint index, const GLuint *v):
    global cglVertexAttrib4Nuiv
    cglVertexAttrib4Nuiv = <GL_VERTEX_ATTRIB4_NUIV>getFunction(b"glVertexAttrib4Nuiv")
    cglVertexAttrib4Nuiv(index, v)

cdef void GetglVertexAttrib4Nusv(GLuint index, const GLushort *v):
    global cglVertexAttrib4Nusv
    cglVertexAttrib4Nusv = <GL_VERTEX_ATTRIB4_NUSV>getFunction(b"glVertexAttrib4Nusv")
    cglVertexAttrib4Nusv(index, v)

cdef void GetglVertexAttrib4bv(GLuint index, const GLbyte *v):
    global cglVertexAttrib4bv
    cglVertexAttrib4bv = <GL_VERTEX_ATTRIB4BV>getFunction(b"glVertexAttrib4bv")
    cglVertexAttrib4bv(index, v)

cdef void GetglVertexAttrib4d(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglVertexAttrib4d
    cglVertexAttrib4d = <GL_VERTEX_ATTRIB4D>getFunction(b"glVertexAttrib4d")
    cglVertexAttrib4d(index, x, y, z, w)

cdef void GetglVertexAttrib4dv(GLuint index, const GLdouble *v):
    global cglVertexAttrib4dv
    cglVertexAttrib4dv = <GL_VERTEX_ATTRIB4DV>getFunction(b"glVertexAttrib4dv")
    cglVertexAttrib4dv(index, v)

cdef void GetglVertexAttrib4f(GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    global cglVertexAttrib4f
    cglVertexAttrib4f = <GL_VERTEX_ATTRIB4F>getFunction(b"glVertexAttrib4f")
    cglVertexAttrib4f(index, x, y, z, w)

cdef void GetglVertexAttrib4fv(GLuint index, const GLfloat *v):
    global cglVertexAttrib4fv
    cglVertexAttrib4fv = <GL_VERTEX_ATTRIB4FV>getFunction(b"glVertexAttrib4fv")
    cglVertexAttrib4fv(index, v)

cdef void GetglVertexAttrib4iv(GLuint index, const GLint *v):
    global cglVertexAttrib4iv
    cglVertexAttrib4iv = <GL_VERTEX_ATTRIB4IV>getFunction(b"glVertexAttrib4iv")
    cglVertexAttrib4iv(index, v)

cdef void GetglVertexAttrib4s(GLuint index, GLshort x, GLshort y, GLshort z, GLshort w):
    global cglVertexAttrib4s
    cglVertexAttrib4s = <GL_VERTEX_ATTRIB4S>getFunction(b"glVertexAttrib4s")
    cglVertexAttrib4s(index, x, y, z, w)

cdef void GetglVertexAttrib4sv(GLuint index, const GLshort *v):
    global cglVertexAttrib4sv
    cglVertexAttrib4sv = <GL_VERTEX_ATTRIB4SV>getFunction(b"glVertexAttrib4sv")
    cglVertexAttrib4sv(index, v)

cdef void GetglVertexAttrib4ubv(GLuint index, const GLubyte *v):
    global cglVertexAttrib4ubv
    cglVertexAttrib4ubv = <GL_VERTEX_ATTRIB4UBV>getFunction(b"glVertexAttrib4ubv")
    cglVertexAttrib4ubv(index, v)

cdef void GetglVertexAttrib4uiv(GLuint index, const GLuint *v):
    global cglVertexAttrib4uiv
    cglVertexAttrib4uiv = <GL_VERTEX_ATTRIB4UIV>getFunction(b"glVertexAttrib4uiv")
    cglVertexAttrib4uiv(index, v)

cdef void GetglVertexAttrib4usv(GLuint index, const GLushort *v):
    global cglVertexAttrib4usv
    cglVertexAttrib4usv = <GL_VERTEX_ATTRIB4USV>getFunction(b"glVertexAttrib4usv")
    cglVertexAttrib4usv(index, v)

cdef void GetglVertexAttribPointer(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void *pointer):
    global cglVertexAttribPointer
    cglVertexAttribPointer = <GL_VERTEX_ATTRIB_POINTER>getFunction(b"glVertexAttribPointer")
    cglVertexAttribPointer(index, size, type, normalized, stride, pointer)

cglBlendEquationSeparate = GetglBlendEquationSeparate
cglDrawBuffers = GetglDrawBuffers
cglStencilOpSeparate = GetglStencilOpSeparate
cglStencilFuncSeparate = GetglStencilFuncSeparate
cglStencilMaskSeparate = GetglStencilMaskSeparate
cglAttachShader = GetglAttachShader
cglBindAttribLocation = GetglBindAttribLocation
cglCompileShader = GetglCompileShader
cglCreateProgram = GetglCreateProgram
cglCreateShader = GetglCreateShader
cglDeleteProgram = GetglDeleteProgram
cglDeleteShader = GetglDeleteShader
cglDetachShader = GetglDetachShader
cglDisableVertexAttribArray = GetglDisableVertexAttribArray
cglEnableVertexAttribArray = GetglEnableVertexAttribArray
cglGetActiveAttrib = GetglGetActiveAttrib
cglGetActiveUniform = GetglGetActiveUniform
cglGetAttachedShaders = GetglGetAttachedShaders
cglGetAttribLocation = GetglGetAttribLocation
cglGetProgramiv = GetglGetProgramiv
cglGetProgramInfoLog = GetglGetProgramInfoLog
cglGetShaderiv = GetglGetShaderiv
cglGetShaderInfoLog = GetglGetShaderInfoLog
cglGetShaderSource = GetglGetShaderSource
cglGetUniformLocation = GetglGetUniformLocation
cglGetUniformfv = GetglGetUniformfv
cglGetUniformiv = GetglGetUniformiv
cglGetVertexAttribdv = GetglGetVertexAttribdv
cglGetVertexAttribfv = GetglGetVertexAttribfv
cglGetVertexAttribiv = GetglGetVertexAttribiv
cglGetVertexAttribPointerv = GetglGetVertexAttribPointerv
cglIsProgram = GetglIsProgram
cglIsShader = GetglIsShader
cglLinkProgram = GetglLinkProgram
cglShaderSource = GetglShaderSource
cglUseProgram = GetglUseProgram
cglUniform1f = GetglUniform1f
cglUniform2f = GetglUniform2f
cglUniform3f = GetglUniform3f
cglUniform4f = GetglUniform4f
cglUniform1i = GetglUniform1i
cglUniform2i = GetglUniform2i
cglUniform3i = GetglUniform3i
cglUniform4i = GetglUniform4i
cglUniform1fv = GetglUniform1fv
cglUniform2fv = GetglUniform2fv
cglUniform3fv = GetglUniform3fv
cglUniform4fv = GetglUniform4fv
cglUniform1iv = GetglUniform1iv
cglUniform2iv = GetglUniform2iv
cglUniform3iv = GetglUniform3iv
cglUniform4iv = GetglUniform4iv
cglUniformMatrix2fv = GetglUniformMatrix2fv
cglUniformMatrix3fv = GetglUniformMatrix3fv
cglUniformMatrix4fv = GetglUniformMatrix4fv
cglValidateProgram = GetglValidateProgram
cglVertexAttrib1d = GetglVertexAttrib1d
cglVertexAttrib1dv = GetglVertexAttrib1dv
cglVertexAttrib1f = GetglVertexAttrib1f
cglVertexAttrib1fv = GetglVertexAttrib1fv
cglVertexAttrib1s = GetglVertexAttrib1s
cglVertexAttrib1sv = GetglVertexAttrib1sv
cglVertexAttrib2d = GetglVertexAttrib2d
cglVertexAttrib2dv = GetglVertexAttrib2dv
cglVertexAttrib2f = GetglVertexAttrib2f
cglVertexAttrib2fv = GetglVertexAttrib2fv
cglVertexAttrib2s = GetglVertexAttrib2s
cglVertexAttrib2sv = GetglVertexAttrib2sv
cglVertexAttrib3d = GetglVertexAttrib3d
cglVertexAttrib3dv = GetglVertexAttrib3dv
cglVertexAttrib3f = GetglVertexAttrib3f
cglVertexAttrib3fv = GetglVertexAttrib3fv
cglVertexAttrib3s = GetglVertexAttrib3s
cglVertexAttrib3sv = GetglVertexAttrib3sv
cglVertexAttrib4Nbv = GetglVertexAttrib4Nbv
cglVertexAttrib4Niv = GetglVertexAttrib4Niv
cglVertexAttrib4Nsv = GetglVertexAttrib4Nsv
cglVertexAttrib4Nub = GetglVertexAttrib4Nub
cglVertexAttrib4Nubv = GetglVertexAttrib4Nubv
cglVertexAttrib4Nuiv = GetglVertexAttrib4Nuiv
cglVertexAttrib4Nusv = GetglVertexAttrib4Nusv
cglVertexAttrib4bv = GetglVertexAttrib4bv
cglVertexAttrib4d = GetglVertexAttrib4d
cglVertexAttrib4dv = GetglVertexAttrib4dv
cglVertexAttrib4f = GetglVertexAttrib4f
cglVertexAttrib4fv = GetglVertexAttrib4fv
cglVertexAttrib4iv = GetglVertexAttrib4iv
cglVertexAttrib4s = GetglVertexAttrib4s
cglVertexAttrib4sv = GetglVertexAttrib4sv
cglVertexAttrib4ubv = GetglVertexAttrib4ubv
cglVertexAttrib4uiv = GetglVertexAttrib4uiv
cglVertexAttrib4usv = GetglVertexAttrib4usv
cglVertexAttribPointer = GetglVertexAttribPointer


cpdef void glBlendEquationSeparate(GLenum modeRGB, GLenum modeAlpha):
    cglBlendEquationSeparate(modeRGB, modeAlpha)

cpdef void glDrawBuffers(GLsizei n, const GLenum *bufs):
    cglDrawBuffers(n, bufs)

cpdef void glStencilOpSeparate(GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass):
    cglStencilOpSeparate(face, sfail, dpfail, dppass)

cpdef void glStencilFuncSeparate(GLenum face, GLenum func, GLint ref, GLuint mask):
    cglStencilFuncSeparate(face, func, ref, mask)

cpdef void glStencilMaskSeparate(GLenum face, GLuint mask):
    cglStencilMaskSeparate(face, mask)

cpdef void glAttachShader(GLuint program, GLuint shader):
    cglAttachShader(program, shader)

cpdef void glBindAttribLocation(GLuint program, GLuint index, const GLchar *name):
    cglBindAttribLocation(program, index, name)

cpdef void glCompileShader(GLuint shader):
    cglCompileShader(shader)

cpdef GLuint glCreateProgram():
    cglCreateProgram()

cpdef GLuint glCreateShader(GLenum type):
    cglCreateShader(type)

cpdef void glDeleteProgram(GLuint program):
    cglDeleteProgram(program)

cpdef void glDeleteShader(GLuint shader):
    cglDeleteShader(shader)

cpdef void glDetachShader(GLuint program, GLuint shader):
    cglDetachShader(program, shader)

cpdef void glDisableVertexAttribArray(GLuint index):
    cglDisableVertexAttribArray(index)

cpdef void glEnableVertexAttribArray(GLuint index):
    cglEnableVertexAttribArray(index)

cpdef void glGetActiveAttrib(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name):
    cglGetActiveAttrib(program, index, bufSize, length, size, type, name)

cpdef void glGetActiveUniform(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name):
    cglGetActiveUniform(program, index, bufSize, length, size, type, name)

cpdef void glGetAttachedShaders(GLuint program, GLsizei maxCount, GLsizei *count, GLuint *shaders):
    cglGetAttachedShaders(program, maxCount, count, shaders)

cpdef GLint glGetAttribLocation(GLuint program, const GLchar *name):
    cglGetAttribLocation(program, name)

cpdef void glGetProgramiv(GLuint program, GLenum pname, GLint *params):
    cglGetProgramiv(program, pname, params)

cpdef void glGetProgramInfoLog(GLuint program, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    cglGetProgramInfoLog(program, bufSize, length, infoLog)

cpdef void glGetShaderiv(GLuint shader, GLenum pname, GLint *params):
    cglGetShaderiv(shader, pname, params)

cpdef void glGetShaderInfoLog(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    cglGetShaderInfoLog(shader, bufSize, length, infoLog)

cpdef void glGetShaderSource(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *source):
    cglGetShaderSource(shader, bufSize, length, source)

cpdef GLint glGetUniformLocation(GLuint program, const GLchar *name):
    cglGetUniformLocation(program, name)

cpdef void glGetUniformfv(GLuint program, GLint location, GLfloat *params):
    cglGetUniformfv(program, location, params)

cpdef void glGetUniformiv(GLuint program, GLint location, GLint *params):
    cglGetUniformiv(program, location, params)

cpdef void glGetVertexAttribdv(GLuint index, GLenum pname, GLdouble *params):
    cglGetVertexAttribdv(index, pname, params)

cpdef void glGetVertexAttribfv(GLuint index, GLenum pname, GLfloat *params):
    cglGetVertexAttribfv(index, pname, params)

cpdef void glGetVertexAttribiv(GLuint index, GLenum pname, GLint *params):
    cglGetVertexAttribiv(index, pname, params)

cpdef void glGetVertexAttribPointerv(GLuint index, GLenum pname, void **pointer):
    cglGetVertexAttribPointerv(index, pname, pointer)

cpdef GLboolean glIsProgram(GLuint program):
    cglIsProgram(program)

cpdef GLboolean glIsShader(GLuint shader):
    cglIsShader(shader)

cpdef void glLinkProgram(GLuint program):
    cglLinkProgram(program)

cpdef void glShaderSource(GLuint shader, GLsizei count, const GLchar *const*string, const GLint *length):
    cglShaderSource(shader, count, string, length)

cpdef void glUseProgram(GLuint program):
    cglUseProgram(program)

cpdef void glUniform1f(GLint location, GLfloat v0):
    cglUniform1f(location, v0)

cpdef void glUniform2f(GLint location, GLfloat v0, GLfloat v1):
    cglUniform2f(location, v0, v1)

cpdef void glUniform3f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2):
    cglUniform3f(location, v0, v1, v2)

cpdef void glUniform4f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3):
    cglUniform4f(location, v0, v1, v2, v3)

cpdef void glUniform1i(GLint location, GLint v0):
    cglUniform1i(location, v0)

cpdef void glUniform2i(GLint location, GLint v0, GLint v1):
    cglUniform2i(location, v0, v1)

cpdef void glUniform3i(GLint location, GLint v0, GLint v1, GLint v2):
    cglUniform3i(location, v0, v1, v2)

cpdef void glUniform4i(GLint location, GLint v0, GLint v1, GLint v2, GLint v3):
    cglUniform4i(location, v0, v1, v2, v3)

cpdef void glUniform1fv(GLint location, GLsizei count, const GLfloat *value):
    cglUniform1fv(location, count, value)

cpdef void glUniform2fv(GLint location, GLsizei count, const GLfloat *value):
    cglUniform2fv(location, count, value)

cpdef void glUniform3fv(GLint location, GLsizei count, const GLfloat *value):
    cglUniform3fv(location, count, value)

cpdef void glUniform4fv(GLint location, GLsizei count, const GLfloat *value):
    cglUniform4fv(location, count, value)

cpdef void glUniform1iv(GLint location, GLsizei count, const GLint *value):
    cglUniform1iv(location, count, value)

cpdef void glUniform2iv(GLint location, GLsizei count, const GLint *value):
    cglUniform2iv(location, count, value)

cpdef void glUniform3iv(GLint location, GLsizei count, const GLint *value):
    cglUniform3iv(location, count, value)

cpdef void glUniform4iv(GLint location, GLsizei count, const GLint *value):
    cglUniform4iv(location, count, value)

cpdef void glUniformMatrix2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix2fv(location, count, transpose, value)

cpdef void glUniformMatrix3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix3fv(location, count, transpose, value)

cpdef void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix4fv(location, count, transpose, value)

cpdef void glValidateProgram(GLuint program):
    cglValidateProgram(program)

cpdef void glVertexAttrib1d(GLuint index, GLdouble x):
    cglVertexAttrib1d(index, x)

cpdef void glVertexAttrib1dv(GLuint index, const GLdouble *v):
    cglVertexAttrib1dv(index, v)

cpdef void glVertexAttrib1f(GLuint index, GLfloat x):
    cglVertexAttrib1f(index, x)

cpdef void glVertexAttrib1fv(GLuint index, const GLfloat *v):
    cglVertexAttrib1fv(index, v)

cpdef void glVertexAttrib1s(GLuint index, GLshort x):
    cglVertexAttrib1s(index, x)

cpdef void glVertexAttrib1sv(GLuint index, const GLshort *v):
    cglVertexAttrib1sv(index, v)

cpdef void glVertexAttrib2d(GLuint index, GLdouble x, GLdouble y):
    cglVertexAttrib2d(index, x, y)

cpdef void glVertexAttrib2dv(GLuint index, const GLdouble *v):
    cglVertexAttrib2dv(index, v)

cpdef void glVertexAttrib2f(GLuint index, GLfloat x, GLfloat y):
    cglVertexAttrib2f(index, x, y)

cpdef void glVertexAttrib2fv(GLuint index, const GLfloat *v):
    cglVertexAttrib2fv(index, v)

cpdef void glVertexAttrib2s(GLuint index, GLshort x, GLshort y):
    cglVertexAttrib2s(index, x, y)

cpdef void glVertexAttrib2sv(GLuint index, const GLshort *v):
    cglVertexAttrib2sv(index, v)

cpdef void glVertexAttrib3d(GLuint index, GLdouble x, GLdouble y, GLdouble z):
    cglVertexAttrib3d(index, x, y, z)

cpdef void glVertexAttrib3dv(GLuint index, const GLdouble *v):
    cglVertexAttrib3dv(index, v)

cpdef void glVertexAttrib3f(GLuint index, GLfloat x, GLfloat y, GLfloat z):
    cglVertexAttrib3f(index, x, y, z)

cpdef void glVertexAttrib3fv(GLuint index, const GLfloat *v):
    cglVertexAttrib3fv(index, v)

cpdef void glVertexAttrib3s(GLuint index, GLshort x, GLshort y, GLshort z):
    cglVertexAttrib3s(index, x, y, z)

cpdef void glVertexAttrib3sv(GLuint index, const GLshort *v):
    cglVertexAttrib3sv(index, v)

cpdef void glVertexAttrib4Nbv(GLuint index, const GLbyte *v):
    cglVertexAttrib4Nbv(index, v)

cpdef void glVertexAttrib4Niv(GLuint index, const GLint *v):
    cglVertexAttrib4Niv(index, v)

cpdef void glVertexAttrib4Nsv(GLuint index, const GLshort *v):
    cglVertexAttrib4Nsv(index, v)

cpdef void glVertexAttrib4Nub(GLuint index, GLubyte x, GLubyte y, GLubyte z, GLubyte w):
    cglVertexAttrib4Nub(index, x, y, z, w)

cpdef void glVertexAttrib4Nubv(GLuint index, const GLubyte *v):
    cglVertexAttrib4Nubv(index, v)

cpdef void glVertexAttrib4Nuiv(GLuint index, const GLuint *v):
    cglVertexAttrib4Nuiv(index, v)

cpdef void glVertexAttrib4Nusv(GLuint index, const GLushort *v):
    cglVertexAttrib4Nusv(index, v)

cpdef void glVertexAttrib4bv(GLuint index, const GLbyte *v):
    cglVertexAttrib4bv(index, v)

cpdef void glVertexAttrib4d(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglVertexAttrib4d(index, x, y, z, w)

cpdef void glVertexAttrib4dv(GLuint index, const GLdouble *v):
    cglVertexAttrib4dv(index, v)

cpdef void glVertexAttrib4f(GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    cglVertexAttrib4f(index, x, y, z, w)

cpdef void glVertexAttrib4fv(GLuint index, const GLfloat *v):
    cglVertexAttrib4fv(index, v)

cpdef void glVertexAttrib4iv(GLuint index, const GLint *v):
    cglVertexAttrib4iv(index, v)

cpdef void glVertexAttrib4s(GLuint index, GLshort x, GLshort y, GLshort z, GLshort w):
    cglVertexAttrib4s(index, x, y, z, w)

cpdef void glVertexAttrib4sv(GLuint index, const GLshort *v):
    cglVertexAttrib4sv(index, v)

cpdef void glVertexAttrib4ubv(GLuint index, const GLubyte *v):
    cglVertexAttrib4ubv(index, v)

cpdef void glVertexAttrib4uiv(GLuint index, const GLuint *v):
    cglVertexAttrib4uiv(index, v)

cpdef void glVertexAttrib4usv(GLuint index, const GLushort *v):
    cglVertexAttrib4usv(index, v)

cpdef void glVertexAttribPointer(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void *pointer):
    cglVertexAttribPointer(index, size, type, normalized, stride, pointer)
