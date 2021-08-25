# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_ACTIVE_ATTRIBUTES = 0x8B89
cdef GLenum GL_ACTIVE_ATTRIBUTE_MAX_LENGTH = 0x8B8A
cdef GLenum GL_ACTIVE_UNIFORMS = 0x8B86
cdef GLenum GL_ACTIVE_UNIFORM_MAX_LENGTH = 0x8B87
cdef GLenum GL_ATTACHED_SHADERS = 0x8B85
cdef GLenum GL_BLEND_EQUATION_ALPHA = 0x883D
cdef GLenum GL_BLEND_EQUATION_RGB = 0x8009
cdef GLenum GL_BOOL = 0x8B56
cdef GLenum GL_BOOL_VEC2 = 0x8B57
cdef GLenum GL_BOOL_VEC3 = 0x8B58
cdef GLenum GL_BOOL_VEC4 = 0x8B59
cdef GLenum GL_COMPILE_STATUS = 0x8B81
cdef GLenum GL_COORD_REPLACE = 0x8862
cdef GLenum GL_CURRENT_PROGRAM = 0x8B8D
cdef GLenum GL_CURRENT_VERTEX_ATTRIB = 0x8626
cdef GLenum GL_DELETE_STATUS = 0x8B80
cdef GLenum GL_DRAW_BUFFER0 = 0x8825
cdef GLenum GL_DRAW_BUFFER1 = 0x8826
cdef GLenum GL_DRAW_BUFFER10 = 0x882F
cdef GLenum GL_DRAW_BUFFER11 = 0x8830
cdef GLenum GL_DRAW_BUFFER12 = 0x8831
cdef GLenum GL_DRAW_BUFFER13 = 0x8832
cdef GLenum GL_DRAW_BUFFER14 = 0x8833
cdef GLenum GL_DRAW_BUFFER15 = 0x8834
cdef GLenum GL_DRAW_BUFFER2 = 0x8827
cdef GLenum GL_DRAW_BUFFER3 = 0x8828
cdef GLenum GL_DRAW_BUFFER4 = 0x8829
cdef GLenum GL_DRAW_BUFFER5 = 0x882A
cdef GLenum GL_DRAW_BUFFER6 = 0x882B
cdef GLenum GL_DRAW_BUFFER7 = 0x882C
cdef GLenum GL_DRAW_BUFFER8 = 0x882D
cdef GLenum GL_DRAW_BUFFER9 = 0x882E
cdef GLenum GL_FLOAT_MAT2 = 0x8B5A
cdef GLenum GL_FLOAT_MAT3 = 0x8B5B
cdef GLenum GL_FLOAT_MAT4 = 0x8B5C
cdef GLenum GL_FLOAT_VEC2 = 0x8B50
cdef GLenum GL_FLOAT_VEC3 = 0x8B51
cdef GLenum GL_FLOAT_VEC4 = 0x8B52
cdef GLenum GL_FRAGMENT_SHADER = 0x8B30
cdef GLenum GL_FRAGMENT_SHADER_DERIVATIVE_HINT = 0x8B8B
cdef GLenum GL_INFO_LOG_LENGTH = 0x8B84
cdef GLenum GL_INT_VEC2 = 0x8B53
cdef GLenum GL_INT_VEC3 = 0x8B54
cdef GLenum GL_INT_VEC4 = 0x8B55
cdef GLenum GL_LINK_STATUS = 0x8B82
cdef GLenum GL_LOWER_LEFT = 0x8CA1
cdef GLenum GL_MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
cdef GLenum GL_MAX_DRAW_BUFFERS = 0x8824
cdef GLenum GL_MAX_FRAGMENT_UNIFORM_COMPONENTS = 0x8B49
cdef GLenum GL_MAX_TEXTURE_COORDS = 0x8871
cdef GLenum GL_MAX_TEXTURE_IMAGE_UNITS = 0x8872
cdef GLenum GL_MAX_VARYING_FLOATS = 0x8B4B
cdef GLenum GL_MAX_VERTEX_ATTRIBS = 0x8869
cdef GLenum GL_MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
cdef GLenum GL_MAX_VERTEX_UNIFORM_COMPONENTS = 0x8B4A
cdef GLenum GL_POINT_SPRITE = 0x8861
cdef GLenum GL_POINT_SPRITE_COORD_ORIGIN = 0x8CA0
cdef GLenum GL_SAMPLER_1D = 0x8B5D
cdef GLenum GL_SAMPLER_1D_SHADOW = 0x8B61
cdef GLenum GL_SAMPLER_2D = 0x8B5E
cdef GLenum GL_SAMPLER_2D_SHADOW = 0x8B62
cdef GLenum GL_SAMPLER_3D = 0x8B5F
cdef GLenum GL_SAMPLER_CUBE = 0x8B60
cdef GLenum GL_SHADER_SOURCE_LENGTH = 0x8B88
cdef GLenum GL_SHADER_TYPE = 0x8B4F
cdef GLenum GL_SHADING_LANGUAGE_VERSION = 0x8B8C
cdef GLenum GL_STENCIL_BACK_FAIL = 0x8801
cdef GLenum GL_STENCIL_BACK_FUNC = 0x8800
cdef GLenum GL_STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
cdef GLenum GL_STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
cdef GLenum GL_STENCIL_BACK_REF = 0x8CA3
cdef GLenum GL_STENCIL_BACK_VALUE_MASK = 0x8CA4
cdef GLenum GL_STENCIL_BACK_WRITEMASK = 0x8CA5
cdef GLenum GL_UPPER_LEFT = 0x8CA2
cdef GLenum GL_VALIDATE_STATUS = 0x8B83
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
cdef GLenum GL_VERTEX_PROGRAM_POINT_SIZE = 0x8642
cdef GLenum GL_VERTEX_PROGRAM_TWO_SIDE = 0x8643
cdef GLenum GL_VERTEX_SHADER = 0x8B31

ctypedef void (*PFNGLATTACHSHADERPROC)(GLuint program, GLuint shader)
ctypedef void (*PFNGLBINDATTRIBLOCATIONPROC)(GLuint program, GLuint index, const GLchar *name)
ctypedef void (*PFNGLBLENDEQUATIONSEPARATEPROC)(GLenum modeRGB, GLenum modeAlpha)
ctypedef void (*PFNGLCOMPILESHADERPROC)(GLuint shader)
ctypedef GLuint (*PFNGLCREATEPROGRAMPROC)()
ctypedef GLuint (*PFNGLCREATESHADERPROC)(GLenum type)
ctypedef void (*PFNGLDELETEPROGRAMPROC)(GLuint program)
ctypedef void (*PFNGLDELETESHADERPROC)(GLuint shader)
ctypedef void (*PFNGLDETACHSHADERPROC)(GLuint program, GLuint shader)
ctypedef void (*PFNGLDISABLEVERTEXATTRIBARRAYPROC)(GLuint index)
ctypedef void (*PFNGLDRAWBUFFERSPROC)(GLsizei n, const GLenum *bufs)
ctypedef void (*PFNGLENABLEVERTEXATTRIBARRAYPROC)(GLuint index)
ctypedef void (*PFNGLGETACTIVEATTRIBPROC)(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name)
ctypedef void (*PFNGLGETACTIVEUNIFORMPROC)(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name)
ctypedef void (*PFNGLGETATTACHEDSHADERSPROC)(GLuint program, GLsizei maxCount, GLsizei *count, GLuint *shaders)
ctypedef GLint (*PFNGLGETATTRIBLOCATIONPROC)(GLuint program, const GLchar *name)
ctypedef void (*PFNGLGETPROGRAMINFOLOGPROC)(GLuint program, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
ctypedef void (*PFNGLGETPROGRAMIVPROC)(GLuint program, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETSHADERINFOLOGPROC)(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog)
ctypedef void (*PFNGLGETSHADERSOURCEPROC)(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *source)
ctypedef void (*PFNGLGETSHADERIVPROC)(GLuint shader, GLenum pname, GLint *params)
ctypedef GLint (*PFNGLGETUNIFORMLOCATIONPROC)(GLuint program, const GLchar *name)
ctypedef void (*PFNGLGETUNIFORMFVPROC)(GLuint program, GLint location, GLfloat *params)
ctypedef void (*PFNGLGETUNIFORMIVPROC)(GLuint program, GLint location, GLint *params)
ctypedef void (*PFNGLGETVERTEXATTRIBPOINTERVPROC)(GLuint index, GLenum pname, void **pointer)
ctypedef void (*PFNGLGETVERTEXATTRIBDVPROC)(GLuint index, GLenum pname, GLdouble *params)
ctypedef void (*PFNGLGETVERTEXATTRIBFVPROC)(GLuint index, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLGETVERTEXATTRIBIVPROC)(GLuint index, GLenum pname, GLint *params)
ctypedef GLboolean (*PFNGLISPROGRAMPROC)(GLuint program)
ctypedef GLboolean (*PFNGLISSHADERPROC)(GLuint shader)
ctypedef void (*PFNGLLINKPROGRAMPROC)(GLuint program)
ctypedef void (*PFNGLSHADERSOURCEPROC)(GLuint shader, GLsizei count, const GLchar **string, const GLint *length)
ctypedef void (*PFNGLSTENCILFUNCSEPARATEPROC)(GLenum face, GLenum func, GLint ref, GLuint mask)
ctypedef void (*PFNGLSTENCILMASKSEPARATEPROC)(GLenum face, GLuint mask)
ctypedef void (*PFNGLSTENCILOPSEPARATEPROC)(GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass)
ctypedef void (*PFNGLUNIFORM1FPROC)(GLint location, GLfloat v0)
ctypedef void (*PFNGLUNIFORM1FVPROC)(GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*PFNGLUNIFORM1IPROC)(GLint location, GLint v0)
ctypedef void (*PFNGLUNIFORM1IVPROC)(GLint location, GLsizei count, const GLint *value)
ctypedef void (*PFNGLUNIFORM2FPROC)(GLint location, GLfloat v0, GLfloat v1)
ctypedef void (*PFNGLUNIFORM2FVPROC)(GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*PFNGLUNIFORM2IPROC)(GLint location, GLint v0, GLint v1)
ctypedef void (*PFNGLUNIFORM2IVPROC)(GLint location, GLsizei count, const GLint *value)
ctypedef void (*PFNGLUNIFORM3FPROC)(GLint location, GLfloat v0, GLfloat v1, GLfloat v2)
ctypedef void (*PFNGLUNIFORM3FVPROC)(GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*PFNGLUNIFORM3IPROC)(GLint location, GLint v0, GLint v1, GLint v2)
ctypedef void (*PFNGLUNIFORM3IVPROC)(GLint location, GLsizei count, const GLint *value)
ctypedef void (*PFNGLUNIFORM4FPROC)(GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3)
ctypedef void (*PFNGLUNIFORM4FVPROC)(GLint location, GLsizei count, const GLfloat *value)
ctypedef void (*PFNGLUNIFORM4IPROC)(GLint location, GLint v0, GLint v1, GLint v2, GLint v3)
ctypedef void (*PFNGLUNIFORM4IVPROC)(GLint location, GLsizei count, const GLint *value)
ctypedef void (*PFNGLUNIFORMMATRIX2FVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLUNIFORMMATRIX3FVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLUNIFORMMATRIX4FVPROC)(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value)
ctypedef void (*PFNGLUSEPROGRAMPROC)(GLuint program)
ctypedef void (*PFNGLVALIDATEPROGRAMPROC)(GLuint program)
ctypedef void (*PFNGLVERTEXATTRIB1DPROC)(GLuint index, GLdouble x)
ctypedef void (*PFNGLVERTEXATTRIB1DVPROC)(GLuint index, const GLdouble *v)
ctypedef void (*PFNGLVERTEXATTRIB1FPROC)(GLuint index, GLfloat x)
ctypedef void (*PFNGLVERTEXATTRIB1FVPROC)(GLuint index, const GLfloat *v)
ctypedef void (*PFNGLVERTEXATTRIB1SPROC)(GLuint index, GLshort x)
ctypedef void (*PFNGLVERTEXATTRIB1SVPROC)(GLuint index, const GLshort *v)
ctypedef void (*PFNGLVERTEXATTRIB2DPROC)(GLuint index, GLdouble x, GLdouble y)
ctypedef void (*PFNGLVERTEXATTRIB2DVPROC)(GLuint index, const GLdouble *v)
ctypedef void (*PFNGLVERTEXATTRIB2FPROC)(GLuint index, GLfloat x, GLfloat y)
ctypedef void (*PFNGLVERTEXATTRIB2FVPROC)(GLuint index, const GLfloat *v)
ctypedef void (*PFNGLVERTEXATTRIB2SPROC)(GLuint index, GLshort x, GLshort y)
ctypedef void (*PFNGLVERTEXATTRIB2SVPROC)(GLuint index, const GLshort *v)
ctypedef void (*PFNGLVERTEXATTRIB3DPROC)(GLuint index, GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*PFNGLVERTEXATTRIB3DVPROC)(GLuint index, const GLdouble *v)
ctypedef void (*PFNGLVERTEXATTRIB3FPROC)(GLuint index, GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*PFNGLVERTEXATTRIB3FVPROC)(GLuint index, const GLfloat *v)
ctypedef void (*PFNGLVERTEXATTRIB3SPROC)(GLuint index, GLshort x, GLshort y, GLshort z)
ctypedef void (*PFNGLVERTEXATTRIB3SVPROC)(GLuint index, const GLshort *v)
ctypedef void (*PFNGLVERTEXATTRIB4NBVPROC)(GLuint index, const GLbyte *v)
ctypedef void (*PFNGLVERTEXATTRIB4NIVPROC)(GLuint index, const GLint *v)
ctypedef void (*PFNGLVERTEXATTRIB4NSVPROC)(GLuint index, const GLshort *v)
ctypedef void (*PFNGLVERTEXATTRIB4NUBPROC)(GLuint index, GLubyte x, GLubyte y, GLubyte z, GLubyte w)
ctypedef void (*PFNGLVERTEXATTRIB4NUBVPROC)(GLuint index, const GLubyte *v)
ctypedef void (*PFNGLVERTEXATTRIB4NUIVPROC)(GLuint index, const GLuint *v)
ctypedef void (*PFNGLVERTEXATTRIB4NUSVPROC)(GLuint index, const GLushort *v)
ctypedef void (*PFNGLVERTEXATTRIB4BVPROC)(GLuint index, const GLbyte *v)
ctypedef void (*PFNGLVERTEXATTRIB4DPROC)(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*PFNGLVERTEXATTRIB4DVPROC)(GLuint index, const GLdouble *v)
ctypedef void (*PFNGLVERTEXATTRIB4FPROC)(GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w)
ctypedef void (*PFNGLVERTEXATTRIB4FVPROC)(GLuint index, const GLfloat *v)
ctypedef void (*PFNGLVERTEXATTRIB4IVPROC)(GLuint index, const GLint *v)
ctypedef void (*PFNGLVERTEXATTRIB4SPROC)(GLuint index, GLshort x, GLshort y, GLshort z, GLshort w)
ctypedef void (*PFNGLVERTEXATTRIB4SVPROC)(GLuint index, const GLshort *v)
ctypedef void (*PFNGLVERTEXATTRIB4UBVPROC)(GLuint index, const GLubyte *v)
ctypedef void (*PFNGLVERTEXATTRIB4UIVPROC)(GLuint index, const GLuint *v)
ctypedef void (*PFNGLVERTEXATTRIB4USVPROC)(GLuint index, const GLushort *v)
ctypedef void (*PFNGLVERTEXATTRIBPOINTERPROC)(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void *pointer)

cdef PFNGLATTACHSHADERPROC cglAttachShader = NULL
cdef PFNGLBINDATTRIBLOCATIONPROC cglBindAttribLocation = NULL
cdef PFNGLBLENDEQUATIONSEPARATEPROC cglBlendEquationSeparate = NULL
cdef PFNGLCOMPILESHADERPROC cglCompileShader = NULL
cdef PFNGLCREATEPROGRAMPROC cglCreateProgram = NULL
cdef PFNGLCREATESHADERPROC cglCreateShader = NULL
cdef PFNGLDELETEPROGRAMPROC cglDeleteProgram = NULL
cdef PFNGLDELETESHADERPROC cglDeleteShader = NULL
cdef PFNGLDETACHSHADERPROC cglDetachShader = NULL
cdef PFNGLDISABLEVERTEXATTRIBARRAYPROC cglDisableVertexAttribArray = NULL
cdef PFNGLDRAWBUFFERSPROC cglDrawBuffers = NULL
cdef PFNGLENABLEVERTEXATTRIBARRAYPROC cglEnableVertexAttribArray = NULL
cdef PFNGLGETACTIVEATTRIBPROC cglGetActiveAttrib = NULL
cdef PFNGLGETACTIVEUNIFORMPROC cglGetActiveUniform = NULL
cdef PFNGLGETATTACHEDSHADERSPROC cglGetAttachedShaders = NULL
cdef PFNGLGETATTRIBLOCATIONPROC cglGetAttribLocation = NULL
cdef PFNGLGETPROGRAMINFOLOGPROC cglGetProgramInfoLog = NULL
cdef PFNGLGETPROGRAMIVPROC cglGetProgramiv = NULL
cdef PFNGLGETSHADERINFOLOGPROC cglGetShaderInfoLog = NULL
cdef PFNGLGETSHADERSOURCEPROC cglGetShaderSource = NULL
cdef PFNGLGETSHADERIVPROC cglGetShaderiv = NULL
cdef PFNGLGETUNIFORMLOCATIONPROC cglGetUniformLocation = NULL
cdef PFNGLGETUNIFORMFVPROC cglGetUniformfv = NULL
cdef PFNGLGETUNIFORMIVPROC cglGetUniformiv = NULL
cdef PFNGLGETVERTEXATTRIBPOINTERVPROC cglGetVertexAttribPointerv = NULL
cdef PFNGLGETVERTEXATTRIBDVPROC cglGetVertexAttribdv = NULL
cdef PFNGLGETVERTEXATTRIBFVPROC cglGetVertexAttribfv = NULL
cdef PFNGLGETVERTEXATTRIBIVPROC cglGetVertexAttribiv = NULL
cdef PFNGLISPROGRAMPROC cglIsProgram = NULL
cdef PFNGLISSHADERPROC cglIsShader = NULL
cdef PFNGLLINKPROGRAMPROC cglLinkProgram = NULL
cdef PFNGLSHADERSOURCEPROC cglShaderSource = NULL
cdef PFNGLSTENCILFUNCSEPARATEPROC cglStencilFuncSeparate = NULL
cdef PFNGLSTENCILMASKSEPARATEPROC cglStencilMaskSeparate = NULL
cdef PFNGLSTENCILOPSEPARATEPROC cglStencilOpSeparate = NULL
cdef PFNGLUNIFORM1FPROC cglUniform1f = NULL
cdef PFNGLUNIFORM1FVPROC cglUniform1fv = NULL
cdef PFNGLUNIFORM1IPROC cglUniform1i = NULL
cdef PFNGLUNIFORM1IVPROC cglUniform1iv = NULL
cdef PFNGLUNIFORM2FPROC cglUniform2f = NULL
cdef PFNGLUNIFORM2FVPROC cglUniform2fv = NULL
cdef PFNGLUNIFORM2IPROC cglUniform2i = NULL
cdef PFNGLUNIFORM2IVPROC cglUniform2iv = NULL
cdef PFNGLUNIFORM3FPROC cglUniform3f = NULL
cdef PFNGLUNIFORM3FVPROC cglUniform3fv = NULL
cdef PFNGLUNIFORM3IPROC cglUniform3i = NULL
cdef PFNGLUNIFORM3IVPROC cglUniform3iv = NULL
cdef PFNGLUNIFORM4FPROC cglUniform4f = NULL
cdef PFNGLUNIFORM4FVPROC cglUniform4fv = NULL
cdef PFNGLUNIFORM4IPROC cglUniform4i = NULL
cdef PFNGLUNIFORM4IVPROC cglUniform4iv = NULL
cdef PFNGLUNIFORMMATRIX2FVPROC cglUniformMatrix2fv = NULL
cdef PFNGLUNIFORMMATRIX3FVPROC cglUniformMatrix3fv = NULL
cdef PFNGLUNIFORMMATRIX4FVPROC cglUniformMatrix4fv = NULL
cdef PFNGLUSEPROGRAMPROC cglUseProgram = NULL
cdef PFNGLVALIDATEPROGRAMPROC cglValidateProgram = NULL
cdef PFNGLVERTEXATTRIB1DPROC cglVertexAttrib1d = NULL
cdef PFNGLVERTEXATTRIB1DVPROC cglVertexAttrib1dv = NULL
cdef PFNGLVERTEXATTRIB1FPROC cglVertexAttrib1f = NULL
cdef PFNGLVERTEXATTRIB1FVPROC cglVertexAttrib1fv = NULL
cdef PFNGLVERTEXATTRIB1SPROC cglVertexAttrib1s = NULL
cdef PFNGLVERTEXATTRIB1SVPROC cglVertexAttrib1sv = NULL
cdef PFNGLVERTEXATTRIB2DPROC cglVertexAttrib2d = NULL
cdef PFNGLVERTEXATTRIB2DVPROC cglVertexAttrib2dv = NULL
cdef PFNGLVERTEXATTRIB2FPROC cglVertexAttrib2f = NULL
cdef PFNGLVERTEXATTRIB2FVPROC cglVertexAttrib2fv = NULL
cdef PFNGLVERTEXATTRIB2SPROC cglVertexAttrib2s = NULL
cdef PFNGLVERTEXATTRIB2SVPROC cglVertexAttrib2sv = NULL
cdef PFNGLVERTEXATTRIB3DPROC cglVertexAttrib3d = NULL
cdef PFNGLVERTEXATTRIB3DVPROC cglVertexAttrib3dv = NULL
cdef PFNGLVERTEXATTRIB3FPROC cglVertexAttrib3f = NULL
cdef PFNGLVERTEXATTRIB3FVPROC cglVertexAttrib3fv = NULL
cdef PFNGLVERTEXATTRIB3SPROC cglVertexAttrib3s = NULL
cdef PFNGLVERTEXATTRIB3SVPROC cglVertexAttrib3sv = NULL
cdef PFNGLVERTEXATTRIB4NBVPROC cglVertexAttrib4Nbv = NULL
cdef PFNGLVERTEXATTRIB4NIVPROC cglVertexAttrib4Niv = NULL
cdef PFNGLVERTEXATTRIB4NSVPROC cglVertexAttrib4Nsv = NULL
cdef PFNGLVERTEXATTRIB4NUBPROC cglVertexAttrib4Nub = NULL
cdef PFNGLVERTEXATTRIB4NUBVPROC cglVertexAttrib4Nubv = NULL
cdef PFNGLVERTEXATTRIB4NUIVPROC cglVertexAttrib4Nuiv = NULL
cdef PFNGLVERTEXATTRIB4NUSVPROC cglVertexAttrib4Nusv = NULL
cdef PFNGLVERTEXATTRIB4BVPROC cglVertexAttrib4bv = NULL
cdef PFNGLVERTEXATTRIB4DPROC cglVertexAttrib4d = NULL
cdef PFNGLVERTEXATTRIB4DVPROC cglVertexAttrib4dv = NULL
cdef PFNGLVERTEXATTRIB4FPROC cglVertexAttrib4f = NULL
cdef PFNGLVERTEXATTRIB4FVPROC cglVertexAttrib4fv = NULL
cdef PFNGLVERTEXATTRIB4IVPROC cglVertexAttrib4iv = NULL
cdef PFNGLVERTEXATTRIB4SPROC cglVertexAttrib4s = NULL
cdef PFNGLVERTEXATTRIB4SVPROC cglVertexAttrib4sv = NULL
cdef PFNGLVERTEXATTRIB4UBVPROC cglVertexAttrib4ubv = NULL
cdef PFNGLVERTEXATTRIB4UIVPROC cglVertexAttrib4uiv = NULL
cdef PFNGLVERTEXATTRIB4USVPROC cglVertexAttrib4usv = NULL
cdef PFNGLVERTEXATTRIBPOINTERPROC cglVertexAttribPointer = NULL


cdef void GetglAttachShader(GLuint program, GLuint shader):
    global cglAttachShader
    cglAttachShader = <PFNGLATTACHSHADERPROC>getFunction(b"glAttachShader")
    cglAttachShader(program, shader)

cdef void GetglBindAttribLocation(GLuint program, GLuint index, const GLchar *name):
    global cglBindAttribLocation
    cglBindAttribLocation = <PFNGLBINDATTRIBLOCATIONPROC>getFunction(b"glBindAttribLocation")
    cglBindAttribLocation(program, index, name)

cdef void GetglBlendEquationSeparate(GLenum modeRGB, GLenum modeAlpha):
    global cglBlendEquationSeparate
    cglBlendEquationSeparate = <PFNGLBLENDEQUATIONSEPARATEPROC>getFunction(b"glBlendEquationSeparate")
    cglBlendEquationSeparate(modeRGB, modeAlpha)

cdef void GetglCompileShader(GLuint shader):
    global cglCompileShader
    cglCompileShader = <PFNGLCOMPILESHADERPROC>getFunction(b"glCompileShader")
    cglCompileShader(shader)

cdef GLuint GetglCreateProgram():
    global cglCreateProgram
    cglCreateProgram = <PFNGLCREATEPROGRAMPROC>getFunction(b"glCreateProgram")
    cglCreateProgram()

cdef GLuint GetglCreateShader(GLenum type):
    global cglCreateShader
    cglCreateShader = <PFNGLCREATESHADERPROC>getFunction(b"glCreateShader")
    cglCreateShader(type)

cdef void GetglDeleteProgram(GLuint program):
    global cglDeleteProgram
    cglDeleteProgram = <PFNGLDELETEPROGRAMPROC>getFunction(b"glDeleteProgram")
    cglDeleteProgram(program)

cdef void GetglDeleteShader(GLuint shader):
    global cglDeleteShader
    cglDeleteShader = <PFNGLDELETESHADERPROC>getFunction(b"glDeleteShader")
    cglDeleteShader(shader)

cdef void GetglDetachShader(GLuint program, GLuint shader):
    global cglDetachShader
    cglDetachShader = <PFNGLDETACHSHADERPROC>getFunction(b"glDetachShader")
    cglDetachShader(program, shader)

cdef void GetglDisableVertexAttribArray(GLuint index):
    global cglDisableVertexAttribArray
    cglDisableVertexAttribArray = <PFNGLDISABLEVERTEXATTRIBARRAYPROC>getFunction(b"glDisableVertexAttribArray")
    cglDisableVertexAttribArray(index)

cdef void GetglDrawBuffers(GLsizei n, const GLenum *bufs):
    global cglDrawBuffers
    cglDrawBuffers = <PFNGLDRAWBUFFERSPROC>getFunction(b"glDrawBuffers")
    cglDrawBuffers(n, bufs)

cdef void GetglEnableVertexAttribArray(GLuint index):
    global cglEnableVertexAttribArray
    cglEnableVertexAttribArray = <PFNGLENABLEVERTEXATTRIBARRAYPROC>getFunction(b"glEnableVertexAttribArray")
    cglEnableVertexAttribArray(index)

cdef void GetglGetActiveAttrib(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name):
    global cglGetActiveAttrib
    cglGetActiveAttrib = <PFNGLGETACTIVEATTRIBPROC>getFunction(b"glGetActiveAttrib")
    cglGetActiveAttrib(program, index, bufSize, length, size, type, name)

cdef void GetglGetActiveUniform(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name):
    global cglGetActiveUniform
    cglGetActiveUniform = <PFNGLGETACTIVEUNIFORMPROC>getFunction(b"glGetActiveUniform")
    cglGetActiveUniform(program, index, bufSize, length, size, type, name)

cdef void GetglGetAttachedShaders(GLuint program, GLsizei maxCount, GLsizei *count, GLuint *shaders):
    global cglGetAttachedShaders
    cglGetAttachedShaders = <PFNGLGETATTACHEDSHADERSPROC>getFunction(b"glGetAttachedShaders")
    cglGetAttachedShaders(program, maxCount, count, shaders)

cdef GLint GetglGetAttribLocation(GLuint program, const GLchar *name):
    global cglGetAttribLocation
    cglGetAttribLocation = <PFNGLGETATTRIBLOCATIONPROC>getFunction(b"glGetAttribLocation")
    cglGetAttribLocation(program, name)

cdef void GetglGetProgramInfoLog(GLuint program, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    global cglGetProgramInfoLog
    cglGetProgramInfoLog = <PFNGLGETPROGRAMINFOLOGPROC>getFunction(b"glGetProgramInfoLog")
    cglGetProgramInfoLog(program, bufSize, length, infoLog)

cdef void GetglGetProgramiv(GLuint program, GLenum pname, GLint *params):
    global cglGetProgramiv
    cglGetProgramiv = <PFNGLGETPROGRAMIVPROC>getFunction(b"glGetProgramiv")
    cglGetProgramiv(program, pname, params)

cdef void GetglGetShaderInfoLog(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    global cglGetShaderInfoLog
    cglGetShaderInfoLog = <PFNGLGETSHADERINFOLOGPROC>getFunction(b"glGetShaderInfoLog")
    cglGetShaderInfoLog(shader, bufSize, length, infoLog)

cdef void GetglGetShaderSource(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *source):
    global cglGetShaderSource
    cglGetShaderSource = <PFNGLGETSHADERSOURCEPROC>getFunction(b"glGetShaderSource")
    cglGetShaderSource(shader, bufSize, length, source)

cdef void GetglGetShaderiv(GLuint shader, GLenum pname, GLint *params):
    global cglGetShaderiv
    cglGetShaderiv = <PFNGLGETSHADERIVPROC>getFunction(b"glGetShaderiv")
    cglGetShaderiv(shader, pname, params)

cdef GLint GetglGetUniformLocation(GLuint program, const GLchar *name):
    global cglGetUniformLocation
    cglGetUniformLocation = <PFNGLGETUNIFORMLOCATIONPROC>getFunction(b"glGetUniformLocation")
    cglGetUniformLocation(program, name)

cdef void GetglGetUniformfv(GLuint program, GLint location, GLfloat *params):
    global cglGetUniformfv
    cglGetUniformfv = <PFNGLGETUNIFORMFVPROC>getFunction(b"glGetUniformfv")
    cglGetUniformfv(program, location, params)

cdef void GetglGetUniformiv(GLuint program, GLint location, GLint *params):
    global cglGetUniformiv
    cglGetUniformiv = <PFNGLGETUNIFORMIVPROC>getFunction(b"glGetUniformiv")
    cglGetUniformiv(program, location, params)

cdef void GetglGetVertexAttribPointerv(GLuint index, GLenum pname, void **pointer):
    global cglGetVertexAttribPointerv
    cglGetVertexAttribPointerv = <PFNGLGETVERTEXATTRIBPOINTERVPROC>getFunction(b"glGetVertexAttribPointerv")
    cglGetVertexAttribPointerv(index, pname, pointer)

cdef void GetglGetVertexAttribdv(GLuint index, GLenum pname, GLdouble *params):
    global cglGetVertexAttribdv
    cglGetVertexAttribdv = <PFNGLGETVERTEXATTRIBDVPROC>getFunction(b"glGetVertexAttribdv")
    cglGetVertexAttribdv(index, pname, params)

cdef void GetglGetVertexAttribfv(GLuint index, GLenum pname, GLfloat *params):
    global cglGetVertexAttribfv
    cglGetVertexAttribfv = <PFNGLGETVERTEXATTRIBFVPROC>getFunction(b"glGetVertexAttribfv")
    cglGetVertexAttribfv(index, pname, params)

cdef void GetglGetVertexAttribiv(GLuint index, GLenum pname, GLint *params):
    global cglGetVertexAttribiv
    cglGetVertexAttribiv = <PFNGLGETVERTEXATTRIBIVPROC>getFunction(b"glGetVertexAttribiv")
    cglGetVertexAttribiv(index, pname, params)

cdef GLboolean GetglIsProgram(GLuint program):
    global cglIsProgram
    cglIsProgram = <PFNGLISPROGRAMPROC>getFunction(b"glIsProgram")
    cglIsProgram(program)

cdef GLboolean GetglIsShader(GLuint shader):
    global cglIsShader
    cglIsShader = <PFNGLISSHADERPROC>getFunction(b"glIsShader")
    cglIsShader(shader)

cdef void GetglLinkProgram(GLuint program):
    global cglLinkProgram
    cglLinkProgram = <PFNGLLINKPROGRAMPROC>getFunction(b"glLinkProgram")
    cglLinkProgram(program)

cdef void GetglShaderSource(GLuint shader, GLsizei count, const GLchar **string, const GLint *length):
    global cglShaderSource
    cglShaderSource = <PFNGLSHADERSOURCEPROC>getFunction(b"glShaderSource")
    cglShaderSource(shader, count, string, length)

cdef void GetglStencilFuncSeparate(GLenum face, GLenum func, GLint ref, GLuint mask):
    global cglStencilFuncSeparate
    cglStencilFuncSeparate = <PFNGLSTENCILFUNCSEPARATEPROC>getFunction(b"glStencilFuncSeparate")
    cglStencilFuncSeparate(face, func, ref, mask)

cdef void GetglStencilMaskSeparate(GLenum face, GLuint mask):
    global cglStencilMaskSeparate
    cglStencilMaskSeparate = <PFNGLSTENCILMASKSEPARATEPROC>getFunction(b"glStencilMaskSeparate")
    cglStencilMaskSeparate(face, mask)

cdef void GetglStencilOpSeparate(GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass):
    global cglStencilOpSeparate
    cglStencilOpSeparate = <PFNGLSTENCILOPSEPARATEPROC>getFunction(b"glStencilOpSeparate")
    cglStencilOpSeparate(face, sfail, dpfail, dppass)

cdef void GetglUniform1f(GLint location, GLfloat v0):
    global cglUniform1f
    cglUniform1f = <PFNGLUNIFORM1FPROC>getFunction(b"glUniform1f")
    cglUniform1f(location, v0)

cdef void GetglUniform1fv(GLint location, GLsizei count, const GLfloat *value):
    global cglUniform1fv
    cglUniform1fv = <PFNGLUNIFORM1FVPROC>getFunction(b"glUniform1fv")
    cglUniform1fv(location, count, value)

cdef void GetglUniform1i(GLint location, GLint v0):
    global cglUniform1i
    cglUniform1i = <PFNGLUNIFORM1IPROC>getFunction(b"glUniform1i")
    cglUniform1i(location, v0)

cdef void GetglUniform1iv(GLint location, GLsizei count, const GLint *value):
    global cglUniform1iv
    cglUniform1iv = <PFNGLUNIFORM1IVPROC>getFunction(b"glUniform1iv")
    cglUniform1iv(location, count, value)

cdef void GetglUniform2f(GLint location, GLfloat v0, GLfloat v1):
    global cglUniform2f
    cglUniform2f = <PFNGLUNIFORM2FPROC>getFunction(b"glUniform2f")
    cglUniform2f(location, v0, v1)

cdef void GetglUniform2fv(GLint location, GLsizei count, const GLfloat *value):
    global cglUniform2fv
    cglUniform2fv = <PFNGLUNIFORM2FVPROC>getFunction(b"glUniform2fv")
    cglUniform2fv(location, count, value)

cdef void GetglUniform2i(GLint location, GLint v0, GLint v1):
    global cglUniform2i
    cglUniform2i = <PFNGLUNIFORM2IPROC>getFunction(b"glUniform2i")
    cglUniform2i(location, v0, v1)

cdef void GetglUniform2iv(GLint location, GLsizei count, const GLint *value):
    global cglUniform2iv
    cglUniform2iv = <PFNGLUNIFORM2IVPROC>getFunction(b"glUniform2iv")
    cglUniform2iv(location, count, value)

cdef void GetglUniform3f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2):
    global cglUniform3f
    cglUniform3f = <PFNGLUNIFORM3FPROC>getFunction(b"glUniform3f")
    cglUniform3f(location, v0, v1, v2)

cdef void GetglUniform3fv(GLint location, GLsizei count, const GLfloat *value):
    global cglUniform3fv
    cglUniform3fv = <PFNGLUNIFORM3FVPROC>getFunction(b"glUniform3fv")
    cglUniform3fv(location, count, value)

cdef void GetglUniform3i(GLint location, GLint v0, GLint v1, GLint v2):
    global cglUniform3i
    cglUniform3i = <PFNGLUNIFORM3IPROC>getFunction(b"glUniform3i")
    cglUniform3i(location, v0, v1, v2)

cdef void GetglUniform3iv(GLint location, GLsizei count, const GLint *value):
    global cglUniform3iv
    cglUniform3iv = <PFNGLUNIFORM3IVPROC>getFunction(b"glUniform3iv")
    cglUniform3iv(location, count, value)

cdef void GetglUniform4f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3):
    global cglUniform4f
    cglUniform4f = <PFNGLUNIFORM4FPROC>getFunction(b"glUniform4f")
    cglUniform4f(location, v0, v1, v2, v3)

cdef void GetglUniform4fv(GLint location, GLsizei count, const GLfloat *value):
    global cglUniform4fv
    cglUniform4fv = <PFNGLUNIFORM4FVPROC>getFunction(b"glUniform4fv")
    cglUniform4fv(location, count, value)

cdef void GetglUniform4i(GLint location, GLint v0, GLint v1, GLint v2, GLint v3):
    global cglUniform4i
    cglUniform4i = <PFNGLUNIFORM4IPROC>getFunction(b"glUniform4i")
    cglUniform4i(location, v0, v1, v2, v3)

cdef void GetglUniform4iv(GLint location, GLsizei count, const GLint *value):
    global cglUniform4iv
    cglUniform4iv = <PFNGLUNIFORM4IVPROC>getFunction(b"glUniform4iv")
    cglUniform4iv(location, count, value)

cdef void GetglUniformMatrix2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix2fv
    cglUniformMatrix2fv = <PFNGLUNIFORMMATRIX2FVPROC>getFunction(b"glUniformMatrix2fv")
    cglUniformMatrix2fv(location, count, transpose, value)

cdef void GetglUniformMatrix3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix3fv
    cglUniformMatrix3fv = <PFNGLUNIFORMMATRIX3FVPROC>getFunction(b"glUniformMatrix3fv")
    cglUniformMatrix3fv(location, count, transpose, value)

cdef void GetglUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    global cglUniformMatrix4fv
    cglUniformMatrix4fv = <PFNGLUNIFORMMATRIX4FVPROC>getFunction(b"glUniformMatrix4fv")
    cglUniformMatrix4fv(location, count, transpose, value)

cdef void GetglUseProgram(GLuint program):
    global cglUseProgram
    cglUseProgram = <PFNGLUSEPROGRAMPROC>getFunction(b"glUseProgram")
    cglUseProgram(program)

cdef void GetglValidateProgram(GLuint program):
    global cglValidateProgram
    cglValidateProgram = <PFNGLVALIDATEPROGRAMPROC>getFunction(b"glValidateProgram")
    cglValidateProgram(program)

cdef void GetglVertexAttrib1d(GLuint index, GLdouble x):
    global cglVertexAttrib1d
    cglVertexAttrib1d = <PFNGLVERTEXATTRIB1DPROC>getFunction(b"glVertexAttrib1d")
    cglVertexAttrib1d(index, x)

cdef void GetglVertexAttrib1dv(GLuint index, const GLdouble *v):
    global cglVertexAttrib1dv
    cglVertexAttrib1dv = <PFNGLVERTEXATTRIB1DVPROC>getFunction(b"glVertexAttrib1dv")
    cglVertexAttrib1dv(index, v)

cdef void GetglVertexAttrib1f(GLuint index, GLfloat x):
    global cglVertexAttrib1f
    cglVertexAttrib1f = <PFNGLVERTEXATTRIB1FPROC>getFunction(b"glVertexAttrib1f")
    cglVertexAttrib1f(index, x)

cdef void GetglVertexAttrib1fv(GLuint index, const GLfloat *v):
    global cglVertexAttrib1fv
    cglVertexAttrib1fv = <PFNGLVERTEXATTRIB1FVPROC>getFunction(b"glVertexAttrib1fv")
    cglVertexAttrib1fv(index, v)

cdef void GetglVertexAttrib1s(GLuint index, GLshort x):
    global cglVertexAttrib1s
    cglVertexAttrib1s = <PFNGLVERTEXATTRIB1SPROC>getFunction(b"glVertexAttrib1s")
    cglVertexAttrib1s(index, x)

cdef void GetglVertexAttrib1sv(GLuint index, const GLshort *v):
    global cglVertexAttrib1sv
    cglVertexAttrib1sv = <PFNGLVERTEXATTRIB1SVPROC>getFunction(b"glVertexAttrib1sv")
    cglVertexAttrib1sv(index, v)

cdef void GetglVertexAttrib2d(GLuint index, GLdouble x, GLdouble y):
    global cglVertexAttrib2d
    cglVertexAttrib2d = <PFNGLVERTEXATTRIB2DPROC>getFunction(b"glVertexAttrib2d")
    cglVertexAttrib2d(index, x, y)

cdef void GetglVertexAttrib2dv(GLuint index, const GLdouble *v):
    global cglVertexAttrib2dv
    cglVertexAttrib2dv = <PFNGLVERTEXATTRIB2DVPROC>getFunction(b"glVertexAttrib2dv")
    cglVertexAttrib2dv(index, v)

cdef void GetglVertexAttrib2f(GLuint index, GLfloat x, GLfloat y):
    global cglVertexAttrib2f
    cglVertexAttrib2f = <PFNGLVERTEXATTRIB2FPROC>getFunction(b"glVertexAttrib2f")
    cglVertexAttrib2f(index, x, y)

cdef void GetglVertexAttrib2fv(GLuint index, const GLfloat *v):
    global cglVertexAttrib2fv
    cglVertexAttrib2fv = <PFNGLVERTEXATTRIB2FVPROC>getFunction(b"glVertexAttrib2fv")
    cglVertexAttrib2fv(index, v)

cdef void GetglVertexAttrib2s(GLuint index, GLshort x, GLshort y):
    global cglVertexAttrib2s
    cglVertexAttrib2s = <PFNGLVERTEXATTRIB2SPROC>getFunction(b"glVertexAttrib2s")
    cglVertexAttrib2s(index, x, y)

cdef void GetglVertexAttrib2sv(GLuint index, const GLshort *v):
    global cglVertexAttrib2sv
    cglVertexAttrib2sv = <PFNGLVERTEXATTRIB2SVPROC>getFunction(b"glVertexAttrib2sv")
    cglVertexAttrib2sv(index, v)

cdef void GetglVertexAttrib3d(GLuint index, GLdouble x, GLdouble y, GLdouble z):
    global cglVertexAttrib3d
    cglVertexAttrib3d = <PFNGLVERTEXATTRIB3DPROC>getFunction(b"glVertexAttrib3d")
    cglVertexAttrib3d(index, x, y, z)

cdef void GetglVertexAttrib3dv(GLuint index, const GLdouble *v):
    global cglVertexAttrib3dv
    cglVertexAttrib3dv = <PFNGLVERTEXATTRIB3DVPROC>getFunction(b"glVertexAttrib3dv")
    cglVertexAttrib3dv(index, v)

cdef void GetglVertexAttrib3f(GLuint index, GLfloat x, GLfloat y, GLfloat z):
    global cglVertexAttrib3f
    cglVertexAttrib3f = <PFNGLVERTEXATTRIB3FPROC>getFunction(b"glVertexAttrib3f")
    cglVertexAttrib3f(index, x, y, z)

cdef void GetglVertexAttrib3fv(GLuint index, const GLfloat *v):
    global cglVertexAttrib3fv
    cglVertexAttrib3fv = <PFNGLVERTEXATTRIB3FVPROC>getFunction(b"glVertexAttrib3fv")
    cglVertexAttrib3fv(index, v)

cdef void GetglVertexAttrib3s(GLuint index, GLshort x, GLshort y, GLshort z):
    global cglVertexAttrib3s
    cglVertexAttrib3s = <PFNGLVERTEXATTRIB3SPROC>getFunction(b"glVertexAttrib3s")
    cglVertexAttrib3s(index, x, y, z)

cdef void GetglVertexAttrib3sv(GLuint index, const GLshort *v):
    global cglVertexAttrib3sv
    cglVertexAttrib3sv = <PFNGLVERTEXATTRIB3SVPROC>getFunction(b"glVertexAttrib3sv")
    cglVertexAttrib3sv(index, v)

cdef void GetglVertexAttrib4Nbv(GLuint index, const GLbyte *v):
    global cglVertexAttrib4Nbv
    cglVertexAttrib4Nbv = <PFNGLVERTEXATTRIB4NBVPROC>getFunction(b"glVertexAttrib4Nbv")
    cglVertexAttrib4Nbv(index, v)

cdef void GetglVertexAttrib4Niv(GLuint index, const GLint *v):
    global cglVertexAttrib4Niv
    cglVertexAttrib4Niv = <PFNGLVERTEXATTRIB4NIVPROC>getFunction(b"glVertexAttrib4Niv")
    cglVertexAttrib4Niv(index, v)

cdef void GetglVertexAttrib4Nsv(GLuint index, const GLshort *v):
    global cglVertexAttrib4Nsv
    cglVertexAttrib4Nsv = <PFNGLVERTEXATTRIB4NSVPROC>getFunction(b"glVertexAttrib4Nsv")
    cglVertexAttrib4Nsv(index, v)

cdef void GetglVertexAttrib4Nub(GLuint index, GLubyte x, GLubyte y, GLubyte z, GLubyte w):
    global cglVertexAttrib4Nub
    cglVertexAttrib4Nub = <PFNGLVERTEXATTRIB4NUBPROC>getFunction(b"glVertexAttrib4Nub")
    cglVertexAttrib4Nub(index, x, y, z, w)

cdef void GetglVertexAttrib4Nubv(GLuint index, const GLubyte *v):
    global cglVertexAttrib4Nubv
    cglVertexAttrib4Nubv = <PFNGLVERTEXATTRIB4NUBVPROC>getFunction(b"glVertexAttrib4Nubv")
    cglVertexAttrib4Nubv(index, v)

cdef void GetglVertexAttrib4Nuiv(GLuint index, const GLuint *v):
    global cglVertexAttrib4Nuiv
    cglVertexAttrib4Nuiv = <PFNGLVERTEXATTRIB4NUIVPROC>getFunction(b"glVertexAttrib4Nuiv")
    cglVertexAttrib4Nuiv(index, v)

cdef void GetglVertexAttrib4Nusv(GLuint index, const GLushort *v):
    global cglVertexAttrib4Nusv
    cglVertexAttrib4Nusv = <PFNGLVERTEXATTRIB4NUSVPROC>getFunction(b"glVertexAttrib4Nusv")
    cglVertexAttrib4Nusv(index, v)

cdef void GetglVertexAttrib4bv(GLuint index, const GLbyte *v):
    global cglVertexAttrib4bv
    cglVertexAttrib4bv = <PFNGLVERTEXATTRIB4BVPROC>getFunction(b"glVertexAttrib4bv")
    cglVertexAttrib4bv(index, v)

cdef void GetglVertexAttrib4d(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglVertexAttrib4d
    cglVertexAttrib4d = <PFNGLVERTEXATTRIB4DPROC>getFunction(b"glVertexAttrib4d")
    cglVertexAttrib4d(index, x, y, z, w)

cdef void GetglVertexAttrib4dv(GLuint index, const GLdouble *v):
    global cglVertexAttrib4dv
    cglVertexAttrib4dv = <PFNGLVERTEXATTRIB4DVPROC>getFunction(b"glVertexAttrib4dv")
    cglVertexAttrib4dv(index, v)

cdef void GetglVertexAttrib4f(GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    global cglVertexAttrib4f
    cglVertexAttrib4f = <PFNGLVERTEXATTRIB4FPROC>getFunction(b"glVertexAttrib4f")
    cglVertexAttrib4f(index, x, y, z, w)

cdef void GetglVertexAttrib4fv(GLuint index, const GLfloat *v):
    global cglVertexAttrib4fv
    cglVertexAttrib4fv = <PFNGLVERTEXATTRIB4FVPROC>getFunction(b"glVertexAttrib4fv")
    cglVertexAttrib4fv(index, v)

cdef void GetglVertexAttrib4iv(GLuint index, const GLint *v):
    global cglVertexAttrib4iv
    cglVertexAttrib4iv = <PFNGLVERTEXATTRIB4IVPROC>getFunction(b"glVertexAttrib4iv")
    cglVertexAttrib4iv(index, v)

cdef void GetglVertexAttrib4s(GLuint index, GLshort x, GLshort y, GLshort z, GLshort w):
    global cglVertexAttrib4s
    cglVertexAttrib4s = <PFNGLVERTEXATTRIB4SPROC>getFunction(b"glVertexAttrib4s")
    cglVertexAttrib4s(index, x, y, z, w)

cdef void GetglVertexAttrib4sv(GLuint index, const GLshort *v):
    global cglVertexAttrib4sv
    cglVertexAttrib4sv = <PFNGLVERTEXATTRIB4SVPROC>getFunction(b"glVertexAttrib4sv")
    cglVertexAttrib4sv(index, v)

cdef void GetglVertexAttrib4ubv(GLuint index, const GLubyte *v):
    global cglVertexAttrib4ubv
    cglVertexAttrib4ubv = <PFNGLVERTEXATTRIB4UBVPROC>getFunction(b"glVertexAttrib4ubv")
    cglVertexAttrib4ubv(index, v)

cdef void GetglVertexAttrib4uiv(GLuint index, const GLuint *v):
    global cglVertexAttrib4uiv
    cglVertexAttrib4uiv = <PFNGLVERTEXATTRIB4UIVPROC>getFunction(b"glVertexAttrib4uiv")
    cglVertexAttrib4uiv(index, v)

cdef void GetglVertexAttrib4usv(GLuint index, const GLushort *v):
    global cglVertexAttrib4usv
    cglVertexAttrib4usv = <PFNGLVERTEXATTRIB4USVPROC>getFunction(b"glVertexAttrib4usv")
    cglVertexAttrib4usv(index, v)

cdef void GetglVertexAttribPointer(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void *pointer):
    global cglVertexAttribPointer
    cglVertexAttribPointer = <PFNGLVERTEXATTRIBPOINTERPROC>getFunction(b"glVertexAttribPointer")
    cglVertexAttribPointer(index, size, type, normalized, stride, pointer)

cglAttachShader = GetglAttachShader
cglBindAttribLocation = GetglBindAttribLocation
cglBlendEquationSeparate = GetglBlendEquationSeparate
cglCompileShader = GetglCompileShader
cglCreateProgram = GetglCreateProgram
cglCreateShader = GetglCreateShader
cglDeleteProgram = GetglDeleteProgram
cglDeleteShader = GetglDeleteShader
cglDetachShader = GetglDetachShader
cglDisableVertexAttribArray = GetglDisableVertexAttribArray
cglDrawBuffers = GetglDrawBuffers
cglEnableVertexAttribArray = GetglEnableVertexAttribArray
cglGetActiveAttrib = GetglGetActiveAttrib
cglGetActiveUniform = GetglGetActiveUniform
cglGetAttachedShaders = GetglGetAttachedShaders
cglGetAttribLocation = GetglGetAttribLocation
cglGetProgramInfoLog = GetglGetProgramInfoLog
cglGetProgramiv = GetglGetProgramiv
cglGetShaderInfoLog = GetglGetShaderInfoLog
cglGetShaderSource = GetglGetShaderSource
cglGetShaderiv = GetglGetShaderiv
cglGetUniformLocation = GetglGetUniformLocation
cglGetUniformfv = GetglGetUniformfv
cglGetUniformiv = GetglGetUniformiv
cglGetVertexAttribPointerv = GetglGetVertexAttribPointerv
cglGetVertexAttribdv = GetglGetVertexAttribdv
cglGetVertexAttribfv = GetglGetVertexAttribfv
cglGetVertexAttribiv = GetglGetVertexAttribiv
cglIsProgram = GetglIsProgram
cglIsShader = GetglIsShader
cglLinkProgram = GetglLinkProgram
cglShaderSource = GetglShaderSource
cglStencilFuncSeparate = GetglStencilFuncSeparate
cglStencilMaskSeparate = GetglStencilMaskSeparate
cglStencilOpSeparate = GetglStencilOpSeparate
cglUniform1f = GetglUniform1f
cglUniform1fv = GetglUniform1fv
cglUniform1i = GetglUniform1i
cglUniform1iv = GetglUniform1iv
cglUniform2f = GetglUniform2f
cglUniform2fv = GetglUniform2fv
cglUniform2i = GetglUniform2i
cglUniform2iv = GetglUniform2iv
cglUniform3f = GetglUniform3f
cglUniform3fv = GetglUniform3fv
cglUniform3i = GetglUniform3i
cglUniform3iv = GetglUniform3iv
cglUniform4f = GetglUniform4f
cglUniform4fv = GetglUniform4fv
cglUniform4i = GetglUniform4i
cglUniform4iv = GetglUniform4iv
cglUniformMatrix2fv = GetglUniformMatrix2fv
cglUniformMatrix3fv = GetglUniformMatrix3fv
cglUniformMatrix4fv = GetglUniformMatrix4fv
cglUseProgram = GetglUseProgram
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


cdef void glAttachShader(GLuint program, GLuint shader):
    cglAttachShader(program, shader)

cdef void glBindAttribLocation(GLuint program, GLuint index, const GLchar *name):
    cglBindAttribLocation(program, index, name)

cdef void glBlendEquationSeparate(GLenum modeRGB, GLenum modeAlpha):
    cglBlendEquationSeparate(modeRGB, modeAlpha)

cdef void glCompileShader(GLuint shader):
    cglCompileShader(shader)

cdef GLuint glCreateProgram():
    cglCreateProgram()

cdef GLuint glCreateShader(GLenum type):
    cglCreateShader(type)

cdef void glDeleteProgram(GLuint program):
    cglDeleteProgram(program)

cdef void glDeleteShader(GLuint shader):
    cglDeleteShader(shader)

cdef void glDetachShader(GLuint program, GLuint shader):
    cglDetachShader(program, shader)

cdef void glDisableVertexAttribArray(GLuint index):
    cglDisableVertexAttribArray(index)

cdef void glDrawBuffers(GLsizei n, const GLenum *bufs):
    cglDrawBuffers(n, bufs)

cdef void glEnableVertexAttribArray(GLuint index):
    cglEnableVertexAttribArray(index)

cdef void glGetActiveAttrib(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name):
    cglGetActiveAttrib(program, index, bufSize, length, size, type, name)

cdef void glGetActiveUniform(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLint *size, GLenum *type, GLchar *name):
    cglGetActiveUniform(program, index, bufSize, length, size, type, name)

cdef void glGetAttachedShaders(GLuint program, GLsizei maxCount, GLsizei *count, GLuint *shaders):
    cglGetAttachedShaders(program, maxCount, count, shaders)

cdef GLint glGetAttribLocation(GLuint program, const GLchar *name):
    cglGetAttribLocation(program, name)

cdef void glGetProgramInfoLog(GLuint program, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    cglGetProgramInfoLog(program, bufSize, length, infoLog)

cdef void glGetProgramiv(GLuint program, GLenum pname, GLint *params):
    cglGetProgramiv(program, pname, params)

cdef void glGetShaderInfoLog(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *infoLog):
    cglGetShaderInfoLog(shader, bufSize, length, infoLog)

cdef void glGetShaderSource(GLuint shader, GLsizei bufSize, GLsizei *length, GLchar *source):
    cglGetShaderSource(shader, bufSize, length, source)

cdef void glGetShaderiv(GLuint shader, GLenum pname, GLint *params):
    cglGetShaderiv(shader, pname, params)

cdef GLint glGetUniformLocation(GLuint program, const GLchar *name):
    cglGetUniformLocation(program, name)

cdef void glGetUniformfv(GLuint program, GLint location, GLfloat *params):
    cglGetUniformfv(program, location, params)

cdef void glGetUniformiv(GLuint program, GLint location, GLint *params):
    cglGetUniformiv(program, location, params)

cdef void glGetVertexAttribPointerv(GLuint index, GLenum pname, void **pointer):
    cglGetVertexAttribPointerv(index, pname, pointer)

cdef void glGetVertexAttribdv(GLuint index, GLenum pname, GLdouble *params):
    cglGetVertexAttribdv(index, pname, params)

cdef void glGetVertexAttribfv(GLuint index, GLenum pname, GLfloat *params):
    cglGetVertexAttribfv(index, pname, params)

cdef void glGetVertexAttribiv(GLuint index, GLenum pname, GLint *params):
    cglGetVertexAttribiv(index, pname, params)

cdef GLboolean glIsProgram(GLuint program):
    cglIsProgram(program)

cdef GLboolean glIsShader(GLuint shader):
    cglIsShader(shader)

cdef void glLinkProgram(GLuint program):
    cglLinkProgram(program)

cdef void glShaderSource(GLuint shader, GLsizei count, const GLchar **string, const GLint *length):
    cglShaderSource(shader, count, string, length)

cdef void glStencilFuncSeparate(GLenum face, GLenum func, GLint ref, GLuint mask):
    cglStencilFuncSeparate(face, func, ref, mask)

cdef void glStencilMaskSeparate(GLenum face, GLuint mask):
    cglStencilMaskSeparate(face, mask)

cdef void glStencilOpSeparate(GLenum face, GLenum sfail, GLenum dpfail, GLenum dppass):
    cglStencilOpSeparate(face, sfail, dpfail, dppass)

cdef void glUniform1f(GLint location, GLfloat v0):
    cglUniform1f(location, v0)

cdef void glUniform1fv(GLint location, GLsizei count, const GLfloat *value):
    cglUniform1fv(location, count, value)

cdef void glUniform1i(GLint location, GLint v0):
    cglUniform1i(location, v0)

cdef void glUniform1iv(GLint location, GLsizei count, const GLint *value):
    cglUniform1iv(location, count, value)

cdef void glUniform2f(GLint location, GLfloat v0, GLfloat v1):
    cglUniform2f(location, v0, v1)

cdef void glUniform2fv(GLint location, GLsizei count, const GLfloat *value):
    cglUniform2fv(location, count, value)

cdef void glUniform2i(GLint location, GLint v0, GLint v1):
    cglUniform2i(location, v0, v1)

cdef void glUniform2iv(GLint location, GLsizei count, const GLint *value):
    cglUniform2iv(location, count, value)

cdef void glUniform3f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2):
    cglUniform3f(location, v0, v1, v2)

cdef void glUniform3fv(GLint location, GLsizei count, const GLfloat *value):
    cglUniform3fv(location, count, value)

cdef void glUniform3i(GLint location, GLint v0, GLint v1, GLint v2):
    cglUniform3i(location, v0, v1, v2)

cdef void glUniform3iv(GLint location, GLsizei count, const GLint *value):
    cglUniform3iv(location, count, value)

cdef void glUniform4f(GLint location, GLfloat v0, GLfloat v1, GLfloat v2, GLfloat v3):
    cglUniform4f(location, v0, v1, v2, v3)

cdef void glUniform4fv(GLint location, GLsizei count, const GLfloat *value):
    cglUniform4fv(location, count, value)

cdef void glUniform4i(GLint location, GLint v0, GLint v1, GLint v2, GLint v3):
    cglUniform4i(location, v0, v1, v2, v3)

cdef void glUniform4iv(GLint location, GLsizei count, const GLint *value):
    cglUniform4iv(location, count, value)

cdef void glUniformMatrix2fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix2fv(location, count, transpose, value)

cdef void glUniformMatrix3fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix3fv(location, count, transpose, value)

cdef void glUniformMatrix4fv(GLint location, GLsizei count, GLboolean transpose, const GLfloat *value):
    cglUniformMatrix4fv(location, count, transpose, value)

cdef void glUseProgram(GLuint program):
    cglUseProgram(program)

cdef void glValidateProgram(GLuint program):
    cglValidateProgram(program)

cdef void glVertexAttrib1d(GLuint index, GLdouble x):
    cglVertexAttrib1d(index, x)

cdef void glVertexAttrib1dv(GLuint index, const GLdouble *v):
    cglVertexAttrib1dv(index, v)

cdef void glVertexAttrib1f(GLuint index, GLfloat x):
    cglVertexAttrib1f(index, x)

cdef void glVertexAttrib1fv(GLuint index, const GLfloat *v):
    cglVertexAttrib1fv(index, v)

cdef void glVertexAttrib1s(GLuint index, GLshort x):
    cglVertexAttrib1s(index, x)

cdef void glVertexAttrib1sv(GLuint index, const GLshort *v):
    cglVertexAttrib1sv(index, v)

cdef void glVertexAttrib2d(GLuint index, GLdouble x, GLdouble y):
    cglVertexAttrib2d(index, x, y)

cdef void glVertexAttrib2dv(GLuint index, const GLdouble *v):
    cglVertexAttrib2dv(index, v)

cdef void glVertexAttrib2f(GLuint index, GLfloat x, GLfloat y):
    cglVertexAttrib2f(index, x, y)

cdef void glVertexAttrib2fv(GLuint index, const GLfloat *v):
    cglVertexAttrib2fv(index, v)

cdef void glVertexAttrib2s(GLuint index, GLshort x, GLshort y):
    cglVertexAttrib2s(index, x, y)

cdef void glVertexAttrib2sv(GLuint index, const GLshort *v):
    cglVertexAttrib2sv(index, v)

cdef void glVertexAttrib3d(GLuint index, GLdouble x, GLdouble y, GLdouble z):
    cglVertexAttrib3d(index, x, y, z)

cdef void glVertexAttrib3dv(GLuint index, const GLdouble *v):
    cglVertexAttrib3dv(index, v)

cdef void glVertexAttrib3f(GLuint index, GLfloat x, GLfloat y, GLfloat z):
    cglVertexAttrib3f(index, x, y, z)

cdef void glVertexAttrib3fv(GLuint index, const GLfloat *v):
    cglVertexAttrib3fv(index, v)

cdef void glVertexAttrib3s(GLuint index, GLshort x, GLshort y, GLshort z):
    cglVertexAttrib3s(index, x, y, z)

cdef void glVertexAttrib3sv(GLuint index, const GLshort *v):
    cglVertexAttrib3sv(index, v)

cdef void glVertexAttrib4Nbv(GLuint index, const GLbyte *v):
    cglVertexAttrib4Nbv(index, v)

cdef void glVertexAttrib4Niv(GLuint index, const GLint *v):
    cglVertexAttrib4Niv(index, v)

cdef void glVertexAttrib4Nsv(GLuint index, const GLshort *v):
    cglVertexAttrib4Nsv(index, v)

cdef void glVertexAttrib4Nub(GLuint index, GLubyte x, GLubyte y, GLubyte z, GLubyte w):
    cglVertexAttrib4Nub(index, x, y, z, w)

cdef void glVertexAttrib4Nubv(GLuint index, const GLubyte *v):
    cglVertexAttrib4Nubv(index, v)

cdef void glVertexAttrib4Nuiv(GLuint index, const GLuint *v):
    cglVertexAttrib4Nuiv(index, v)

cdef void glVertexAttrib4Nusv(GLuint index, const GLushort *v):
    cglVertexAttrib4Nusv(index, v)

cdef void glVertexAttrib4bv(GLuint index, const GLbyte *v):
    cglVertexAttrib4bv(index, v)

cdef void glVertexAttrib4d(GLuint index, GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglVertexAttrib4d(index, x, y, z, w)

cdef void glVertexAttrib4dv(GLuint index, const GLdouble *v):
    cglVertexAttrib4dv(index, v)

cdef void glVertexAttrib4f(GLuint index, GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    cglVertexAttrib4f(index, x, y, z, w)

cdef void glVertexAttrib4fv(GLuint index, const GLfloat *v):
    cglVertexAttrib4fv(index, v)

cdef void glVertexAttrib4iv(GLuint index, const GLint *v):
    cglVertexAttrib4iv(index, v)

cdef void glVertexAttrib4s(GLuint index, GLshort x, GLshort y, GLshort z, GLshort w):
    cglVertexAttrib4s(index, x, y, z, w)

cdef void glVertexAttrib4sv(GLuint index, const GLshort *v):
    cglVertexAttrib4sv(index, v)

cdef void glVertexAttrib4ubv(GLuint index, const GLubyte *v):
    cglVertexAttrib4ubv(index, v)

cdef void glVertexAttrib4uiv(GLuint index, const GLuint *v):
    cglVertexAttrib4uiv(index, v)

cdef void glVertexAttrib4usv(GLuint index, const GLushort *v):
    cglVertexAttrib4usv(index, v)

cdef void glVertexAttribPointer(GLuint index, GLint size, GLenum type, GLboolean normalized, GLsizei stride, const void *pointer):
    cglVertexAttribPointer(index, size, type, normalized, stride, pointer)
