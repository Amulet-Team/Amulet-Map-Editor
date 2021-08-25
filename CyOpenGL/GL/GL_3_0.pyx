# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_INT_SAMPLER_2D_ARRAY = 0x8DCF
cdef GLenum GL_READ_FRAMEBUFFER = 0x8CA8
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
cdef GLenum GL_COLOR_ATTACHMENT16 = 0x8CF0
cdef GLenum GL_RG32F = 0x8230
cdef GLenum GL_RGBA8UI = 0x8D7C
cdef GLenum GL_COMPARE_REF_TO_TEXTURE = 0x884E
cdef GLenum GL_RGBA32F = 0x8814
cdef GLenum GL_TRANSFORM_FEEDBACK_VARYING_MAX_LENGTH = 0x8C76
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER = 0x8C8E
cdef GLenum GL_R8UI = 0x8232
cdef GLenum GL_INTERLEAVED_ATTRIBS = 0x8C8C
cdef GLenum GL_CLIP_DISTANCE3 = 0x3003
cdef GLenum GL_FLOAT_32_UNSIGNED_INT_24_8_REV = 0x8DAD
cdef GLenum GL_TEXTURE_BINDING_1D_ARRAY = 0x8C1C
cdef GLenum GL_COLOR_ATTACHMENT23 = 0x8CF7
cdef GLenum GL_COMPRESSED_SIGNED_RG_RGTC2 = 0x8DBE
cdef GLenum GL_FRAMEBUFFER_COMPLETE = 0x8CD5
cdef GLenum GL_RENDERBUFFER_RED_SIZE = 0x8D50
cdef GLenum GL_INT_SAMPLER_3D = 0x8DCB
cdef GLenum GL_TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 0x8C88
cdef GLenum GL_QUERY_BY_REGION_NO_WAIT = 0x8E16
cdef GLenum GL_TEXTURE_GREEN_TYPE = 0x8C11
cdef GLenum GL_SAMPLER_1D_ARRAY = 0x8DC0
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 0x8CD4
cdef GLenum GL_MAP_FLUSH_EXPLICIT_BIT = 0x0010
cdef GLenum GL_RGBA16F = 0x881A
cdef GLenum GL_QUERY_WAIT = 0x8E13
cdef GLenum GL_DEPTH_STENCIL = 0x84F9
cdef GLenum GL_MAX_SAMPLES = 0x8D57
cdef GLenum GL_RG = 0x8227
cdef GLenum GL_TEXTURE_DEPTH_TYPE = 0x8C16
cdef GLenum GL_CLIP_DISTANCE2 = 0x3002
cdef GLenum GL_STENCIL_INDEX4 = 0x8D47
cdef GLenum GL_RG8UI = 0x8238
cdef GLenum GL_RGB16UI = 0x8D77
cdef GLenum GL_UNSIGNED_INT_VEC3 = 0x8DC7
cdef GLenum GL_COMPRESSED_RED_RGTC1 = 0x8DBB
cdef GLenum GL_SAMPLER_CUBE_SHADOW = 0x8DC5
cdef GLenum GL_QUERY_NO_WAIT = 0x8E14
cdef GLenum GL_COLOR_ATTACHMENT5 = 0x8CE5
cdef GLenum GL_CLIP_DISTANCE4 = 0x3004
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 0x8216
cdef GLenum GL_CONTEXT_FLAGS = 0x821E
cdef GLenum GL_COMPRESSED_RG = 0x8226
cdef GLenum GL_COLOR_ATTACHMENT20 = 0x8CF4
cdef GLenum GL_DEPTH_ATTACHMENT = 0x8D00
cdef GLenum GL_CLAMP_FRAGMENT_COLOR = 0x891B
cdef GLenum GL_COLOR_ATTACHMENT2 = 0x8CE2
cdef GLenum GL_UNSIGNED_INT_5_9_9_9_REV = 0x8C3E
cdef GLenum GL_R8 = 0x8229
cdef GLenum GL_MAX_ARRAY_TEXTURE_LAYERS = 0x88FF
cdef GLenum GL_UNSIGNED_INT_VEC4 = 0x8DC8
cdef GLenum GL_MAP_WRITE_BIT = 0x0002
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
cdef GLenum GL_UNSIGNED_INT_24_8 = 0x84FA
cdef GLenum GL_COLOR_ATTACHMENT17 = 0x8CF1
cdef GLenum GL_CLIP_DISTANCE7 = 0x3007
cdef GLenum GL_TEXTURE_STENCIL_SIZE = 0x88F1
cdef GLenum GL_MAJOR_VERSION = 0x821B
cdef GLenum GL_RGBA16UI = 0x8D76
cdef GLenum GL_TRANSFORM_FEEDBACK_VARYINGS = 0x8C83
cdef GLenum GL_UNSIGNED_INT_SAMPLER_1D = 0x8DD1
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
cdef GLenum GL_TEXTURE_ALPHA_TYPE = 0x8C13
cdef GLenum GL_CLIP_DISTANCE5 = 0x3005
cdef GLenum GL_COMPRESSED_SIGNED_RED_RGTC1 = 0x8DBC
cdef GLenum GL_RGBA32I = 0x8D82
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x8DD7
cdef GLenum GL_COLOR_ATTACHMENT7 = 0x8CE7
cdef GLenum GL_MAP_INVALIDATE_BUFFER_BIT = 0x0008
cdef GLenum GL_COLOR_ATTACHMENT12 = 0x8CEC
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 0x8211
cdef GLenum GL_RG8 = 0x822B
cdef GLenum GL_R32F = 0x822E
cdef GLenum GL_R8I = 0x8231
cdef GLenum GL_RENDERBUFFER_SAMPLES = 0x8CAB
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_DRAW_BUFFER = 0x8CDB
cdef GLenum GL_COLOR_ATTACHMENT27 = 0x8CFB
cdef GLenum GL_MAP_INVALIDATE_RANGE_BIT = 0x0004
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_SIZE = 0x8C85
cdef GLenum GL_CLIP_DISTANCE6 = 0x3006
cdef GLenum GL_RGB_INTEGER = 0x8D98
cdef GLenum GL_RG32UI = 0x823C
cdef GLenum GL_READ_FRAMEBUFFER_BINDING = 0x8CAA
cdef GLenum GL_MINOR_VERSION = 0x821C
cdef GLenum GL_DEPTH24_STENCIL8 = 0x88F0
cdef GLenum GL_NUM_EXTENSIONS = 0x821D
cdef GLenum GL_RG16UI = 0x823A
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 0x8213
cdef GLenum GL_RGB16I = 0x8D89
cdef GLenum GL_UNSIGNED_INT_SAMPLER_1D_ARRAY = 0x8DD6
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 0x8210
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 0x8214
cdef GLenum GL_RENDERBUFFER_BINDING = 0x8CA7
cdef GLenum GL_PROXY_TEXTURE_1D_ARRAY = 0x8C19
cdef GLenum GL_RG_INTEGER = 0x8228
cdef GLenum GL_GREEN_INTEGER = 0x8D95
cdef GLenum GL_COLOR_ATTACHMENT11 = 0x8CEB
cdef GLenum GL_RENDERBUFFER_WIDTH = 0x8D42
cdef GLenum GL_RASTERIZER_DISCARD = 0x8C89
cdef GLenum GL_COLOR_ATTACHMENT15 = 0x8CEF
cdef GLenum GL_R16I = 0x8233
cdef GLenum GL_RGBA8I = 0x8D8E
cdef GLenum GL_RGBA32UI = 0x8D70
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 0x8D56
cdef GLenum GL_DEPTH_STENCIL_ATTACHMENT = 0x821A
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
cdef GLenum GL_MAP_UNSYNCHRONIZED_BIT = 0x0020
cdef GLenum GL_UNSIGNED_INT_SAMPLER_2D = 0x8DD2
cdef GLenum GL_CLAMP_VERTEX_COLOR = 0x891A
cdef GLenum GL_COLOR_ATTACHMENT25 = 0x8CF9
cdef GLenum GL_TEXTURE_BINDING_2D_ARRAY = 0x8C1D
cdef GLenum GL_MAX_RENDERBUFFER_SIZE = 0x84E8
cdef GLenum GL_COLOR_ATTACHMENT10 = 0x8CEA
cdef GLenum GL_RG16F = 0x822F
cdef GLenum GL_RGB32UI = 0x8D71
cdef GLenum GL_DRAW_FRAMEBUFFER = 0x8CA9
cdef GLenum GL_RGBA16I = 0x8D88
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_START = 0x8C84
cdef GLenum GL_RGB32I = 0x8D83
cdef GLenum GL_FRAMEBUFFER_DEFAULT = 0x8218
cdef GLenum GL_UNSIGNED_INT_VEC2 = 0x8DC6
cdef GLenum GL_DRAW_FRAMEBUFFER_BINDING = 0x8CA6
cdef GLenum GL_MAX_COLOR_ATTACHMENTS = 0x8CDF
cdef GLenum GL_INVALID_FRAMEBUFFER_OPERATION = 0x0506
cdef GLenum GL_COLOR_ATTACHMENT19 = 0x8CF3
cdef GLenum GL_MAX_VARYING_COMPONENTS = 0x8B4B
cdef GLenum GL_RENDERBUFFER_GREEN_SIZE = 0x8D51
cdef GLenum GL_UNSIGNED_NORMALIZED = 0x8C17
cdef GLenum GL_STENCIL_INDEX1 = 0x8D46
cdef GLenum GL_COLOR_ATTACHMENT14 = 0x8CEE
cdef GLenum GL_COLOR_ATTACHMENT29 = 0x8CFD
cdef GLenum GL_COLOR_ATTACHMENT9 = 0x8CE9
cdef GLenum GL_RGB8UI = 0x8D7D
cdef GLenum GL_COMPRESSED_RG_RGTC2 = 0x8DBD
cdef GLenum GL_BGR_INTEGER = 0x8D9A
cdef GLenum GL_R32I = 0x8235
cdef GLenum GL_TEXTURE_INTENSITY_TYPE = 0x8C15
cdef GLenum GL_BUFFER_MAP_OFFSET = 0x9121
cdef GLenum GL_UNSIGNED_INT_SAMPLER_CUBE = 0x8DD4
cdef GLenum GL_RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
cdef GLenum GL_CONTEXT_FLAG_FORWARD_COMPATIBLE_BIT = 0x00000001
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_INTEGER = 0x88FD
cdef GLenum GL_INT_SAMPLER_2D = 0x8DCA
cdef GLenum GL_COLOR_ATTACHMENT22 = 0x8CF6
cdef GLenum GL_TEXTURE_RED_TYPE = 0x8C10
cdef GLenum GL_COLOR_ATTACHMENT4 = 0x8CE4
cdef GLenum GL_PRIMITIVES_GENERATED = 0x8C87
cdef GLenum GL_COLOR_ATTACHMENT1 = 0x8CE1
cdef GLenum GL_STENCIL_INDEX16 = 0x8D49
cdef GLenum GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 0x8C80
cdef GLenum GL_QUERY_BY_REGION_WAIT = 0x8E15
cdef GLenum GL_RED_INTEGER = 0x8D94
cdef GLenum GL_INT_SAMPLER_1D_ARRAY = 0x8DCE
cdef GLenum GL_COLOR_ATTACHMENT28 = 0x8CFC
cdef GLenum GL_VERTEX_ARRAY_BINDING = 0x85B5
cdef GLenum GL_STENCIL_ATTACHMENT = 0x8D20
cdef GLenum GL_COLOR_ATTACHMENT31 = 0x8CFF
cdef GLenum GL_COLOR_ATTACHMENT13 = 0x8CED
cdef GLenum GL_RENDERBUFFER_DEPTH_SIZE = 0x8D54
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_MODE = 0x8C7F
cdef GLenum GL_CLIP_DISTANCE0 = 0x3000
cdef GLenum GL_RENDERBUFFER_STENCIL_SIZE = 0x8D55
cdef GLenum GL_RG16 = 0x822C
cdef GLenum GL_BUFFER_MAP_LENGTH = 0x9120
cdef GLenum GL_CLAMP_READ_COLOR = 0x891C
cdef GLenum GL_BLUE_INTEGER = 0x8D96
cdef GLenum GL_RENDERBUFFER = 0x8D41
cdef GLenum GL_RGB9_E5 = 0x8C3D
cdef GLenum GL_DEPTH32F_STENCIL8 = 0x8CAD
cdef GLenum GL_TEXTURE_BLUE_TYPE = 0x8C12
cdef GLenum GL_RENDERBUFFER_ALPHA_SIZE = 0x8D53
cdef GLenum GL_RENDERBUFFER_HEIGHT = 0x8D43
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
cdef GLenum GL_INT_SAMPLER_1D = 0x8DC9
cdef GLenum GL_FRAMEBUFFER_UNDEFINED = 0x8219
cdef GLenum GL_COLOR_ATTACHMENT8 = 0x8CE8
cdef GLenum GL_SAMPLER_2D_ARRAY = 0x8DC1
cdef GLenum GL_R16 = 0x822A
cdef GLenum GL_COLOR_ATTACHMENT21 = 0x8CF5
cdef GLenum GL_COLOR_ATTACHMENT18 = 0x8CF2
cdef GLenum GL_MIN_PROGRAM_TEXEL_OFFSET = 0x8904
cdef GLenum GL_UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B
cdef GLenum GL_R32UI = 0x8236
cdef GLenum GL_BGRA_INTEGER = 0x8D9B
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_RED_SIZE = 0x8212
cdef GLenum GL_COLOR_ATTACHMENT30 = 0x8CFE
cdef GLenum GL_FIXED_ONLY = 0x891D
cdef GLenum GL_TEXTURE_1D_ARRAY = 0x8C18
cdef GLenum GL_PROXY_TEXTURE_2D_ARRAY = 0x8C1B
cdef GLenum GL_R11F_G11F_B10F = 0x8C3A
cdef GLenum GL_TEXTURE_2D_ARRAY = 0x8C1A
cdef GLenum GL_SAMPLER_2D_ARRAY_SHADOW = 0x8DC4
cdef GLenum GL_MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 0x8C8A
cdef GLenum GL_MAP_READ_BIT = 0x0001
cdef GLenum GL_COLOR_ATTACHMENT24 = 0x8CF8
cdef GLenum GL_RENDERBUFFER_BLUE_SIZE = 0x8D52
cdef GLenum GL_RGB16F = 0x881B
cdef GLenum GL_RG8I = 0x8237
cdef GLenum GL_CLIP_DISTANCE1 = 0x3001
cdef GLenum GL_RGB8I = 0x8D8F
cdef GLenum GL_FRAMEBUFFER_BINDING = 0x8CA6
cdef GLenum GL_COLOR_ATTACHMENT6 = 0x8CE6
cdef GLenum GL_COLOR_ATTACHMENT0 = 0x8CE0
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 0x8217
cdef GLenum GL_COLOR_ATTACHMENT3 = 0x8CE3
cdef GLenum GL_ALPHA_INTEGER = 0x8D97
cdef GLenum GL_UNSIGNED_INT_SAMPLER_3D = 0x8DD3
cdef GLenum GL_R16F = 0x822D
cdef GLenum GL_MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 0x8C8B
cdef GLenum GL_RGB32F = 0x8815
cdef GLenum GL_COMPRESSED_RED = 0x8225
cdef GLenum GL_FRAMEBUFFER_SRGB = 0x8DB9
cdef GLenum GL_RGBA_INTEGER = 0x8D99
cdef GLenum GL_MAX_CLIP_DISTANCES = 0x0D32
cdef GLenum GL_INT_SAMPLER_CUBE = 0x8DCC
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_READ_BUFFER = 0x8CDC
cdef GLenum GL_RG16I = 0x8239
cdef GLenum GL_COLOR_ATTACHMENT26 = 0x8CFA
cdef GLenum GL_TEXTURE_LUMINANCE_TYPE = 0x8C14
cdef GLenum GL_FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
cdef GLenum GL_FRAMEBUFFER_UNSUPPORTED = 0x8CDD
cdef GLenum GL_MAX_PROGRAM_TEXEL_OFFSET = 0x8905
cdef GLenum GL_STENCIL_INDEX8 = 0x8D48
cdef GLenum GL_HALF_FLOAT = 0x140B
cdef GLenum GL_DEPTH_COMPONENT32F = 0x8CAC
cdef GLenum GL_INDEX = 0x8222
cdef GLenum GL_TEXTURE_SHARED_SIZE = 0x8C3F
cdef GLenum GL_RG32I = 0x823B
cdef GLenum GL_SEPARATE_ATTRIBS = 0x8C8D
cdef GLenum GL_TRANSFORM_FEEDBACK_BUFFER_BINDING = 0x8C8F
cdef GLenum GL_SAMPLER_1D_ARRAY_SHADOW = 0x8DC3
cdef GLenum GL_FRAMEBUFFER = 0x8D40
cdef GLenum GL_FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 0x8215
cdef GLenum GL_R16UI = 0x8234
cdef GLenum GL_BUFFER_ACCESS_FLAGS = 0x911F

ctypedef GLboolean (*PFNGLISRENDERBUFFERPROC)(GLuint renderbuffer)
ctypedef void (*PFNGLVERTEXATTRIBI4IPROC)(GLuint index, GLint x, GLint y, GLint z, GLint w)
ctypedef void (*PFNGLGETRENDERBUFFERPARAMETERIVPROC)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*PFNGLVERTEXATTRIBI4SVPROC)(GLuint index, const GLshort *v)
ctypedef void (*PFNGLUNIFORM3UIVPROC)(GLint location, GLsizei count, const GLuint *value)
ctypedef void (*PFNGLENABLEIPROC)(GLenum target, GLuint index)
ctypedef void (*PFNGLTRANSFORMFEEDBACKVARYINGSPROC)(GLuint program, GLsizei count, const GLchar **varyings, GLenum bufferMode)
ctypedef GLboolean (*PFNGLISENABLEDIPROC)(GLenum target, GLuint index)
ctypedef void (*PFNGLTEXPARAMETERIUIVPROC)(GLenum target, GLenum pname, const GLuint *params)
ctypedef void (*PFNGLUNIFORM2UIVPROC)(GLint location, GLsizei count, const GLuint *value)
ctypedef void (*PFNGLCLEARBUFFERFVPROC)(GLenum buffer, GLint drawbuffer, const GLfloat *value)
ctypedef void (*PFNGLVERTEXATTRIBI2IPROC)(GLuint index, GLint x, GLint y)
ctypedef void (*PFNGLFRAMEBUFFERTEXTURE2DPROC)(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level)
ctypedef void (*PFNGLVERTEXATTRIBI1IVPROC)(GLuint index, const GLint *v)
ctypedef void (*PFNGLVERTEXATTRIBIPOINTERPROC)(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer)
ctypedef void (*PFNGLFRAMEBUFFERTEXTURELAYERPROC)(GLenum target, GLenum attachment, GLuint texture, GLint level, GLint layer)
ctypedef void (*PFNGLVERTEXATTRIBI4BVPROC)(GLuint index, const GLbyte *v)
ctypedef void (*PFNGLVERTEXATTRIBI4IVPROC)(GLuint index, const GLint *v)
ctypedef void (*PFNGLGETFRAMEBUFFERATTACHMENTPARAMETERIVPROC)(GLenum target, GLenum attachment, GLenum pname, GLint *params)
ctypedef void (*PFNGLGENVERTEXARRAYSPROC)(GLsizei n, GLuint *arrays)
ctypedef void (*PFNGLVERTEXATTRIBI3UIPROC)(GLuint index, GLuint x, GLuint y, GLuint z)
ctypedef void (*PFNGLGENRENDERBUFFERSPROC)(GLsizei n, GLuint *renderbuffers)
ctypedef GLint (*PFNGLGETFRAGDATALOCATIONPROC)(GLuint program, const GLchar *name)
ctypedef void (*PFNGLFRAMEBUFFERTEXTURE1DPROC)(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level)
ctypedef void (*PFNGLVERTEXATTRIBI3IVPROC)(GLuint index, const GLint *v)
ctypedef void (*PFNGLVERTEXATTRIBI1IPROC)(GLuint index, GLint x)
ctypedef void (*PFNGLENDCONDITIONALRENDERPROC)()
ctypedef const GLubyte *(*PFNGLGETSTRINGIPROC)(GLenum name, GLuint index)
ctypedef void (*PFNGLDELETEVERTEXARRAYSPROC)(GLsizei n, const GLuint *arrays)
ctypedef void (*PFNGLBLITFRAMEBUFFERPROC)(GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
ctypedef void *(*PFNGLMAPBUFFERRANGEPROC)(GLenum target, GLintptr offset, GLsizeiptr length, GLbitfield access)
ctypedef void (*PFNGLFRAMEBUFFERTEXTURE3DPROC)(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level, GLint zoffset)
ctypedef void (*PFNGLUNIFORM4UIPROC)(GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3)
ctypedef GLboolean (*PFNGLISFRAMEBUFFERPROC)(GLuint framebuffer)
ctypedef void (*PFNGLDELETERENDERBUFFERSPROC)(GLsizei n, const GLuint *renderbuffers)
ctypedef void (*PFNGLVERTEXATTRIBI4UBVPROC)(GLuint index, const GLubyte *v)
ctypedef void (*PFNGLUNIFORM4UIVPROC)(GLint location, GLsizei count, const GLuint *value)
ctypedef void (*PFNGLBINDVERTEXARRAYPROC)(GLuint array)
ctypedef void (*PFNGLGETTEXPARAMETERIUIVPROC)(GLenum target, GLenum pname, GLuint *params)
ctypedef void (*PFNGLRENDERBUFFERSTORAGEPROC)(GLenum target, GLenum internalformat, GLsizei width, GLsizei height)
ctypedef void (*PFNGLVERTEXATTRIBI2UIVPROC)(GLuint index, const GLuint *v)
ctypedef void (*PFNGLBINDFRAGDATALOCATIONPROC)(GLuint program, GLuint color, const GLchar *name)
ctypedef void (*PFNGLVERTEXATTRIBI3UIVPROC)(GLuint index, const GLuint *v)
ctypedef void (*PFNGLGETTRANSFORMFEEDBACKVARYINGPROC)(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum *type, GLchar *name)
ctypedef void (*PFNGLVERTEXATTRIBI4UIPROC)(GLuint index, GLuint x, GLuint y, GLuint z, GLuint w)
ctypedef void (*PFNGLGETUNIFORMUIVPROC)(GLuint program, GLint location, GLuint *params)
ctypedef void (*PFNGLBINDBUFFERRANGEPROC)(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
ctypedef void (*PFNGLBEGINTRANSFORMFEEDBACKPROC)(GLenum primitiveMode)
ctypedef void (*PFNGLCLEARBUFFERFIPROC)(GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil)
ctypedef void (*PFNGLGETTEXPARAMETERIIVPROC)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*PFNGLUNIFORM2UIPROC)(GLint location, GLuint v0, GLuint v1)
ctypedef void (*PFNGLBINDFRAMEBUFFERPROC)(GLenum target, GLuint framebuffer)
ctypedef void (*PFNGLRENDERBUFFERSTORAGEMULTISAMPLEPROC)(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height)
ctypedef void (*PFNGLDISABLEIPROC)(GLenum target, GLuint index)
ctypedef void (*PFNGLDELETEFRAMEBUFFERSPROC)(GLsizei n, const GLuint *framebuffers)
ctypedef void (*PFNGLVERTEXATTRIBI4USVPROC)(GLuint index, const GLushort *v)
ctypedef void (*PFNGLVERTEXATTRIBI2IVPROC)(GLuint index, const GLint *v)
ctypedef void (*PFNGLUNIFORM1UIPROC)(GLint location, GLuint v0)
ctypedef void (*PFNGLCLEARBUFFERIVPROC)(GLenum buffer, GLint drawbuffer, const GLint *value)
ctypedef void (*PFNGLCLAMPCOLORPROC)(GLenum target, GLenum clamp)
ctypedef void (*PFNGLBINDBUFFERBASEPROC)(GLenum target, GLuint index, GLuint buffer)
ctypedef void (*PFNGLENDTRANSFORMFEEDBACKPROC)()
ctypedef void (*PFNGLVERTEXATTRIBI3IPROC)(GLuint index, GLint x, GLint y, GLint z)
ctypedef void (*PFNGLGENERATEMIPMAPPROC)(GLenum target)
ctypedef void (*PFNGLFLUSHMAPPEDBUFFERRANGEPROC)(GLenum target, GLintptr offset, GLsizeiptr length)
ctypedef void (*PFNGLGETVERTEXATTRIBIIVPROC)(GLuint index, GLenum pname, GLint *params)
ctypedef void (*PFNGLUNIFORM1UIVPROC)(GLint location, GLsizei count, const GLuint *value)
ctypedef void (*PFNGLTEXPARAMETERIIVPROC)(GLenum target, GLenum pname, const GLint *params)
ctypedef void (*PFNGLBINDRENDERBUFFERPROC)(GLenum target, GLuint renderbuffer)
ctypedef void (*PFNGLVERTEXATTRIBI4UIVPROC)(GLuint index, const GLuint *v)
ctypedef GLenum (*PFNGLCHECKFRAMEBUFFERSTATUSPROC)(GLenum target)
ctypedef void (*PFNGLFRAMEBUFFERRENDERBUFFERPROC)(GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
ctypedef void (*PFNGLVERTEXATTRIBI1UIPROC)(GLuint index, GLuint x)
ctypedef void (*PFNGLUNIFORM3UIPROC)(GLint location, GLuint v0, GLuint v1, GLuint v2)
ctypedef void (*PFNGLGENFRAMEBUFFERSPROC)(GLsizei n, GLuint *framebuffers)
ctypedef void (*PFNGLBEGINCONDITIONALRENDERPROC)(GLuint id, GLenum mode)
ctypedef void (*PFNGLVERTEXATTRIBI1UIVPROC)(GLuint index, const GLuint *v)
ctypedef void (*PFNGLGETINTEGERI_VPROC)(GLenum target, GLuint index, GLint *data)
ctypedef void (*PFNGLCOLORMASKIPROC)(GLuint index, GLboolean r, GLboolean g, GLboolean b, GLboolean a)
ctypedef GLboolean (*PFNGLISVERTEXARRAYPROC)(GLuint array)
ctypedef void (*PFNGLVERTEXATTRIBI2UIPROC)(GLuint index, GLuint x, GLuint y)
ctypedef void (*PFNGLCLEARBUFFERUIVPROC)(GLenum buffer, GLint drawbuffer, const GLuint *value)
ctypedef void (*PFNGLGETBOOLEANI_VPROC)(GLenum target, GLuint index, GLboolean *data)
ctypedef void (*PFNGLGETVERTEXATTRIBIUIVPROC)(GLuint index, GLenum pname, GLuint *params)

cdef PFNGLISRENDERBUFFERPROC cglIsRenderbuffer = NULL
cdef PFNGLVERTEXATTRIBI4IPROC cglVertexAttribI4i = NULL
cdef PFNGLGETRENDERBUFFERPARAMETERIVPROC cglGetRenderbufferParameteriv = NULL
cdef PFNGLVERTEXATTRIBI4SVPROC cglVertexAttribI4sv = NULL
cdef PFNGLUNIFORM3UIVPROC cglUniform3uiv = NULL
cdef PFNGLENABLEIPROC cglEnablei = NULL
cdef PFNGLTRANSFORMFEEDBACKVARYINGSPROC cglTransformFeedbackVaryings = NULL
cdef PFNGLISENABLEDIPROC cglIsEnabledi = NULL
cdef PFNGLTEXPARAMETERIUIVPROC cglTexParameterIuiv = NULL
cdef PFNGLUNIFORM2UIVPROC cglUniform2uiv = NULL
cdef PFNGLCLEARBUFFERFVPROC cglClearBufferfv = NULL
cdef PFNGLVERTEXATTRIBI2IPROC cglVertexAttribI2i = NULL
cdef PFNGLFRAMEBUFFERTEXTURE2DPROC cglFramebufferTexture2D = NULL
cdef PFNGLVERTEXATTRIBI1IVPROC cglVertexAttribI1iv = NULL
cdef PFNGLVERTEXATTRIBIPOINTERPROC cglVertexAttribIPointer = NULL
cdef PFNGLFRAMEBUFFERTEXTURELAYERPROC cglFramebufferTextureLayer = NULL
cdef PFNGLVERTEXATTRIBI4BVPROC cglVertexAttribI4bv = NULL
cdef PFNGLVERTEXATTRIBI4IVPROC cglVertexAttribI4iv = NULL
cdef PFNGLGETFRAMEBUFFERATTACHMENTPARAMETERIVPROC cglGetFramebufferAttachmentParameteriv = NULL
cdef PFNGLGENVERTEXARRAYSPROC cglGenVertexArrays = NULL
cdef PFNGLVERTEXATTRIBI3UIPROC cglVertexAttribI3ui = NULL
cdef PFNGLGENRENDERBUFFERSPROC cglGenRenderbuffers = NULL
cdef PFNGLGETFRAGDATALOCATIONPROC cglGetFragDataLocation = NULL
cdef PFNGLFRAMEBUFFERTEXTURE1DPROC cglFramebufferTexture1D = NULL
cdef PFNGLVERTEXATTRIBI3IVPROC cglVertexAttribI3iv = NULL
cdef PFNGLVERTEXATTRIBI1IPROC cglVertexAttribI1i = NULL
cdef PFNGLENDCONDITIONALRENDERPROC cglEndConditionalRender = NULL
cdef PFNGLGETSTRINGIPROC cglGetStringi = NULL
cdef PFNGLDELETEVERTEXARRAYSPROC cglDeleteVertexArrays = NULL
cdef PFNGLBLITFRAMEBUFFERPROC cglBlitFramebuffer = NULL
cdef PFNGLMAPBUFFERRANGEPROC cglMapBufferRange = NULL
cdef PFNGLFRAMEBUFFERTEXTURE3DPROC cglFramebufferTexture3D = NULL
cdef PFNGLUNIFORM4UIPROC cglUniform4ui = NULL
cdef PFNGLISFRAMEBUFFERPROC cglIsFramebuffer = NULL
cdef PFNGLDELETERENDERBUFFERSPROC cglDeleteRenderbuffers = NULL
cdef PFNGLVERTEXATTRIBI4UBVPROC cglVertexAttribI4ubv = NULL
cdef PFNGLUNIFORM4UIVPROC cglUniform4uiv = NULL
cdef PFNGLBINDVERTEXARRAYPROC cglBindVertexArray = NULL
cdef PFNGLGETTEXPARAMETERIUIVPROC cglGetTexParameterIuiv = NULL
cdef PFNGLRENDERBUFFERSTORAGEPROC cglRenderbufferStorage = NULL
cdef PFNGLVERTEXATTRIBI2UIVPROC cglVertexAttribI2uiv = NULL
cdef PFNGLBINDFRAGDATALOCATIONPROC cglBindFragDataLocation = NULL
cdef PFNGLVERTEXATTRIBI3UIVPROC cglVertexAttribI3uiv = NULL
cdef PFNGLGETTRANSFORMFEEDBACKVARYINGPROC cglGetTransformFeedbackVarying = NULL
cdef PFNGLVERTEXATTRIBI4UIPROC cglVertexAttribI4ui = NULL
cdef PFNGLGETUNIFORMUIVPROC cglGetUniformuiv = NULL
cdef PFNGLBINDBUFFERRANGEPROC cglBindBufferRange = NULL
cdef PFNGLBEGINTRANSFORMFEEDBACKPROC cglBeginTransformFeedback = NULL
cdef PFNGLCLEARBUFFERFIPROC cglClearBufferfi = NULL
cdef PFNGLGETTEXPARAMETERIIVPROC cglGetTexParameterIiv = NULL
cdef PFNGLUNIFORM2UIPROC cglUniform2ui = NULL
cdef PFNGLBINDFRAMEBUFFERPROC cglBindFramebuffer = NULL
cdef PFNGLRENDERBUFFERSTORAGEMULTISAMPLEPROC cglRenderbufferStorageMultisample = NULL
cdef PFNGLDISABLEIPROC cglDisablei = NULL
cdef PFNGLDELETEFRAMEBUFFERSPROC cglDeleteFramebuffers = NULL
cdef PFNGLVERTEXATTRIBI4USVPROC cglVertexAttribI4usv = NULL
cdef PFNGLVERTEXATTRIBI2IVPROC cglVertexAttribI2iv = NULL
cdef PFNGLUNIFORM1UIPROC cglUniform1ui = NULL
cdef PFNGLCLEARBUFFERIVPROC cglClearBufferiv = NULL
cdef PFNGLCLAMPCOLORPROC cglClampColor = NULL
cdef PFNGLBINDBUFFERBASEPROC cglBindBufferBase = NULL
cdef PFNGLENDTRANSFORMFEEDBACKPROC cglEndTransformFeedback = NULL
cdef PFNGLVERTEXATTRIBI3IPROC cglVertexAttribI3i = NULL
cdef PFNGLGENERATEMIPMAPPROC cglGenerateMipmap = NULL
cdef PFNGLFLUSHMAPPEDBUFFERRANGEPROC cglFlushMappedBufferRange = NULL
cdef PFNGLGETVERTEXATTRIBIIVPROC cglGetVertexAttribIiv = NULL
cdef PFNGLUNIFORM1UIVPROC cglUniform1uiv = NULL
cdef PFNGLTEXPARAMETERIIVPROC cglTexParameterIiv = NULL
cdef PFNGLBINDRENDERBUFFERPROC cglBindRenderbuffer = NULL
cdef PFNGLVERTEXATTRIBI4UIVPROC cglVertexAttribI4uiv = NULL
cdef PFNGLCHECKFRAMEBUFFERSTATUSPROC cglCheckFramebufferStatus = NULL
cdef PFNGLFRAMEBUFFERRENDERBUFFERPROC cglFramebufferRenderbuffer = NULL
cdef PFNGLVERTEXATTRIBI1UIPROC cglVertexAttribI1ui = NULL
cdef PFNGLUNIFORM3UIPROC cglUniform3ui = NULL
cdef PFNGLGENFRAMEBUFFERSPROC cglGenFramebuffers = NULL
cdef PFNGLBEGINCONDITIONALRENDERPROC cglBeginConditionalRender = NULL
cdef PFNGLVERTEXATTRIBI1UIVPROC cglVertexAttribI1uiv = NULL
cdef PFNGLGETINTEGERI_VPROC cglGetIntegeri_v = NULL
cdef PFNGLCOLORMASKIPROC cglColorMaski = NULL
cdef PFNGLISVERTEXARRAYPROC cglIsVertexArray = NULL
cdef PFNGLVERTEXATTRIBI2UIPROC cglVertexAttribI2ui = NULL
cdef PFNGLCLEARBUFFERUIVPROC cglClearBufferuiv = NULL
cdef PFNGLGETBOOLEANI_VPROC cglGetBooleani_v = NULL
cdef PFNGLGETVERTEXATTRIBIUIVPROC cglGetVertexAttribIuiv = NULL


cdef GLboolean GetglIsRenderbuffer(GLuint renderbuffer):
    global cglIsRenderbuffer
    cglIsRenderbuffer = <PFNGLISRENDERBUFFERPROC>getFunction(b"glIsRenderbuffer")
    cglIsRenderbuffer(renderbuffer)

cdef void GetglVertexAttribI4i(GLuint index, GLint x, GLint y, GLint z, GLint w):
    global cglVertexAttribI4i
    cglVertexAttribI4i = <PFNGLVERTEXATTRIBI4IPROC>getFunction(b"glVertexAttribI4i")
    cglVertexAttribI4i(index, x, y, z, w)

cdef void GetglGetRenderbufferParameteriv(GLenum target, GLenum pname, GLint *params):
    global cglGetRenderbufferParameteriv
    cglGetRenderbufferParameteriv = <PFNGLGETRENDERBUFFERPARAMETERIVPROC>getFunction(b"glGetRenderbufferParameteriv")
    cglGetRenderbufferParameteriv(target, pname, params)

cdef void GetglVertexAttribI4sv(GLuint index, const GLshort *v):
    global cglVertexAttribI4sv
    cglVertexAttribI4sv = <PFNGLVERTEXATTRIBI4SVPROC>getFunction(b"glVertexAttribI4sv")
    cglVertexAttribI4sv(index, v)

cdef void GetglUniform3uiv(GLint location, GLsizei count, const GLuint *value):
    global cglUniform3uiv
    cglUniform3uiv = <PFNGLUNIFORM3UIVPROC>getFunction(b"glUniform3uiv")
    cglUniform3uiv(location, count, value)

cdef void GetglEnablei(GLenum target, GLuint index):
    global cglEnablei
    cglEnablei = <PFNGLENABLEIPROC>getFunction(b"glEnablei")
    cglEnablei(target, index)

cdef void GetglTransformFeedbackVaryings(GLuint program, GLsizei count, const GLchar **varyings, GLenum bufferMode):
    global cglTransformFeedbackVaryings
    cglTransformFeedbackVaryings = <PFNGLTRANSFORMFEEDBACKVARYINGSPROC>getFunction(b"glTransformFeedbackVaryings")
    cglTransformFeedbackVaryings(program, count, varyings, bufferMode)

cdef GLboolean GetglIsEnabledi(GLenum target, GLuint index):
    global cglIsEnabledi
    cglIsEnabledi = <PFNGLISENABLEDIPROC>getFunction(b"glIsEnabledi")
    cglIsEnabledi(target, index)

cdef void GetglTexParameterIuiv(GLenum target, GLenum pname, const GLuint *params):
    global cglTexParameterIuiv
    cglTexParameterIuiv = <PFNGLTEXPARAMETERIUIVPROC>getFunction(b"glTexParameterIuiv")
    cglTexParameterIuiv(target, pname, params)

cdef void GetglUniform2uiv(GLint location, GLsizei count, const GLuint *value):
    global cglUniform2uiv
    cglUniform2uiv = <PFNGLUNIFORM2UIVPROC>getFunction(b"glUniform2uiv")
    cglUniform2uiv(location, count, value)

cdef void GetglClearBufferfv(GLenum buffer, GLint drawbuffer, const GLfloat *value):
    global cglClearBufferfv
    cglClearBufferfv = <PFNGLCLEARBUFFERFVPROC>getFunction(b"glClearBufferfv")
    cglClearBufferfv(buffer, drawbuffer, value)

cdef void GetglVertexAttribI2i(GLuint index, GLint x, GLint y):
    global cglVertexAttribI2i
    cglVertexAttribI2i = <PFNGLVERTEXATTRIBI2IPROC>getFunction(b"glVertexAttribI2i")
    cglVertexAttribI2i(index, x, y)

cdef void GetglFramebufferTexture2D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level):
    global cglFramebufferTexture2D
    cglFramebufferTexture2D = <PFNGLFRAMEBUFFERTEXTURE2DPROC>getFunction(b"glFramebufferTexture2D")
    cglFramebufferTexture2D(target, attachment, textarget, texture, level)

cdef void GetglVertexAttribI1iv(GLuint index, const GLint *v):
    global cglVertexAttribI1iv
    cglVertexAttribI1iv = <PFNGLVERTEXATTRIBI1IVPROC>getFunction(b"glVertexAttribI1iv")
    cglVertexAttribI1iv(index, v)

cdef void GetglVertexAttribIPointer(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer):
    global cglVertexAttribIPointer
    cglVertexAttribIPointer = <PFNGLVERTEXATTRIBIPOINTERPROC>getFunction(b"glVertexAttribIPointer")
    cglVertexAttribIPointer(index, size, type, stride, pointer)

cdef void GetglFramebufferTextureLayer(GLenum target, GLenum attachment, GLuint texture, GLint level, GLint layer):
    global cglFramebufferTextureLayer
    cglFramebufferTextureLayer = <PFNGLFRAMEBUFFERTEXTURELAYERPROC>getFunction(b"glFramebufferTextureLayer")
    cglFramebufferTextureLayer(target, attachment, texture, level, layer)

cdef void GetglVertexAttribI4bv(GLuint index, const GLbyte *v):
    global cglVertexAttribI4bv
    cglVertexAttribI4bv = <PFNGLVERTEXATTRIBI4BVPROC>getFunction(b"glVertexAttribI4bv")
    cglVertexAttribI4bv(index, v)

cdef void GetglVertexAttribI4iv(GLuint index, const GLint *v):
    global cglVertexAttribI4iv
    cglVertexAttribI4iv = <PFNGLVERTEXATTRIBI4IVPROC>getFunction(b"glVertexAttribI4iv")
    cglVertexAttribI4iv(index, v)

cdef void GetglGetFramebufferAttachmentParameteriv(GLenum target, GLenum attachment, GLenum pname, GLint *params):
    global cglGetFramebufferAttachmentParameteriv
    cglGetFramebufferAttachmentParameteriv = <PFNGLGETFRAMEBUFFERATTACHMENTPARAMETERIVPROC>getFunction(b"glGetFramebufferAttachmentParameteriv")
    cglGetFramebufferAttachmentParameteriv(target, attachment, pname, params)

cdef void GetglGenVertexArrays(GLsizei n, GLuint *arrays):
    global cglGenVertexArrays
    cglGenVertexArrays = <PFNGLGENVERTEXARRAYSPROC>getFunction(b"glGenVertexArrays")
    cglGenVertexArrays(n, arrays)

cdef void GetglVertexAttribI3ui(GLuint index, GLuint x, GLuint y, GLuint z):
    global cglVertexAttribI3ui
    cglVertexAttribI3ui = <PFNGLVERTEXATTRIBI3UIPROC>getFunction(b"glVertexAttribI3ui")
    cglVertexAttribI3ui(index, x, y, z)

cdef void GetglGenRenderbuffers(GLsizei n, GLuint *renderbuffers):
    global cglGenRenderbuffers
    cglGenRenderbuffers = <PFNGLGENRENDERBUFFERSPROC>getFunction(b"glGenRenderbuffers")
    cglGenRenderbuffers(n, renderbuffers)

cdef GLint GetglGetFragDataLocation(GLuint program, const GLchar *name):
    global cglGetFragDataLocation
    cglGetFragDataLocation = <PFNGLGETFRAGDATALOCATIONPROC>getFunction(b"glGetFragDataLocation")
    cglGetFragDataLocation(program, name)

cdef void GetglFramebufferTexture1D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level):
    global cglFramebufferTexture1D
    cglFramebufferTexture1D = <PFNGLFRAMEBUFFERTEXTURE1DPROC>getFunction(b"glFramebufferTexture1D")
    cglFramebufferTexture1D(target, attachment, textarget, texture, level)

cdef void GetglVertexAttribI3iv(GLuint index, const GLint *v):
    global cglVertexAttribI3iv
    cglVertexAttribI3iv = <PFNGLVERTEXATTRIBI3IVPROC>getFunction(b"glVertexAttribI3iv")
    cglVertexAttribI3iv(index, v)

cdef void GetglVertexAttribI1i(GLuint index, GLint x):
    global cglVertexAttribI1i
    cglVertexAttribI1i = <PFNGLVERTEXATTRIBI1IPROC>getFunction(b"glVertexAttribI1i")
    cglVertexAttribI1i(index, x)

cdef void GetglEndConditionalRender():
    global cglEndConditionalRender
    cglEndConditionalRender = <PFNGLENDCONDITIONALRENDERPROC>getFunction(b"glEndConditionalRender")
    cglEndConditionalRender()

cdef const GLubyte *GetglGetStringi(GLenum name, GLuint index):
    global cglGetStringi
    cglGetStringi = <PFNGLGETSTRINGIPROC>getFunction(b"glGetStringi")
    cglGetStringi(name, index)

cdef void GetglDeleteVertexArrays(GLsizei n, const GLuint *arrays):
    global cglDeleteVertexArrays
    cglDeleteVertexArrays = <PFNGLDELETEVERTEXARRAYSPROC>getFunction(b"glDeleteVertexArrays")
    cglDeleteVertexArrays(n, arrays)

cdef void GetglBlitFramebuffer(GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter):
    global cglBlitFramebuffer
    cglBlitFramebuffer = <PFNGLBLITFRAMEBUFFERPROC>getFunction(b"glBlitFramebuffer")
    cglBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)

cdef void *GetglMapBufferRange(GLenum target, GLintptr offset, GLsizeiptr length, GLbitfield access):
    global cglMapBufferRange
    cglMapBufferRange = <PFNGLMAPBUFFERRANGEPROC>getFunction(b"glMapBufferRange")
    cglMapBufferRange(target, offset, length, access)

cdef void GetglFramebufferTexture3D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level, GLint zoffset):
    global cglFramebufferTexture3D
    cglFramebufferTexture3D = <PFNGLFRAMEBUFFERTEXTURE3DPROC>getFunction(b"glFramebufferTexture3D")
    cglFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset)

cdef void GetglUniform4ui(GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3):
    global cglUniform4ui
    cglUniform4ui = <PFNGLUNIFORM4UIPROC>getFunction(b"glUniform4ui")
    cglUniform4ui(location, v0, v1, v2, v3)

cdef GLboolean GetglIsFramebuffer(GLuint framebuffer):
    global cglIsFramebuffer
    cglIsFramebuffer = <PFNGLISFRAMEBUFFERPROC>getFunction(b"glIsFramebuffer")
    cglIsFramebuffer(framebuffer)

cdef void GetglDeleteRenderbuffers(GLsizei n, const GLuint *renderbuffers):
    global cglDeleteRenderbuffers
    cglDeleteRenderbuffers = <PFNGLDELETERENDERBUFFERSPROC>getFunction(b"glDeleteRenderbuffers")
    cglDeleteRenderbuffers(n, renderbuffers)

cdef void GetglVertexAttribI4ubv(GLuint index, const GLubyte *v):
    global cglVertexAttribI4ubv
    cglVertexAttribI4ubv = <PFNGLVERTEXATTRIBI4UBVPROC>getFunction(b"glVertexAttribI4ubv")
    cglVertexAttribI4ubv(index, v)

cdef void GetglUniform4uiv(GLint location, GLsizei count, const GLuint *value):
    global cglUniform4uiv
    cglUniform4uiv = <PFNGLUNIFORM4UIVPROC>getFunction(b"glUniform4uiv")
    cglUniform4uiv(location, count, value)

cdef void GetglBindVertexArray(GLuint array):
    global cglBindVertexArray
    cglBindVertexArray = <PFNGLBINDVERTEXARRAYPROC>getFunction(b"glBindVertexArray")
    cglBindVertexArray(array)

cdef void GetglGetTexParameterIuiv(GLenum target, GLenum pname, GLuint *params):
    global cglGetTexParameterIuiv
    cglGetTexParameterIuiv = <PFNGLGETTEXPARAMETERIUIVPROC>getFunction(b"glGetTexParameterIuiv")
    cglGetTexParameterIuiv(target, pname, params)

cdef void GetglRenderbufferStorage(GLenum target, GLenum internalformat, GLsizei width, GLsizei height):
    global cglRenderbufferStorage
    cglRenderbufferStorage = <PFNGLRENDERBUFFERSTORAGEPROC>getFunction(b"glRenderbufferStorage")
    cglRenderbufferStorage(target, internalformat, width, height)

cdef void GetglVertexAttribI2uiv(GLuint index, const GLuint *v):
    global cglVertexAttribI2uiv
    cglVertexAttribI2uiv = <PFNGLVERTEXATTRIBI2UIVPROC>getFunction(b"glVertexAttribI2uiv")
    cglVertexAttribI2uiv(index, v)

cdef void GetglBindFragDataLocation(GLuint program, GLuint color, const GLchar *name):
    global cglBindFragDataLocation
    cglBindFragDataLocation = <PFNGLBINDFRAGDATALOCATIONPROC>getFunction(b"glBindFragDataLocation")
    cglBindFragDataLocation(program, color, name)

cdef void GetglVertexAttribI3uiv(GLuint index, const GLuint *v):
    global cglVertexAttribI3uiv
    cglVertexAttribI3uiv = <PFNGLVERTEXATTRIBI3UIVPROC>getFunction(b"glVertexAttribI3uiv")
    cglVertexAttribI3uiv(index, v)

cdef void GetglGetTransformFeedbackVarying(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum *type, GLchar *name):
    global cglGetTransformFeedbackVarying
    cglGetTransformFeedbackVarying = <PFNGLGETTRANSFORMFEEDBACKVARYINGPROC>getFunction(b"glGetTransformFeedbackVarying")
    cglGetTransformFeedbackVarying(program, index, bufSize, length, size, type, name)

cdef void GetglVertexAttribI4ui(GLuint index, GLuint x, GLuint y, GLuint z, GLuint w):
    global cglVertexAttribI4ui
    cglVertexAttribI4ui = <PFNGLVERTEXATTRIBI4UIPROC>getFunction(b"glVertexAttribI4ui")
    cglVertexAttribI4ui(index, x, y, z, w)

cdef void GetglGetUniformuiv(GLuint program, GLint location, GLuint *params):
    global cglGetUniformuiv
    cglGetUniformuiv = <PFNGLGETUNIFORMUIVPROC>getFunction(b"glGetUniformuiv")
    cglGetUniformuiv(program, location, params)

cdef void GetglBindBufferRange(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size):
    global cglBindBufferRange
    cglBindBufferRange = <PFNGLBINDBUFFERRANGEPROC>getFunction(b"glBindBufferRange")
    cglBindBufferRange(target, index, buffer, offset, size)

cdef void GetglBeginTransformFeedback(GLenum primitiveMode):
    global cglBeginTransformFeedback
    cglBeginTransformFeedback = <PFNGLBEGINTRANSFORMFEEDBACKPROC>getFunction(b"glBeginTransformFeedback")
    cglBeginTransformFeedback(primitiveMode)

cdef void GetglClearBufferfi(GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil):
    global cglClearBufferfi
    cglClearBufferfi = <PFNGLCLEARBUFFERFIPROC>getFunction(b"glClearBufferfi")
    cglClearBufferfi(buffer, drawbuffer, depth, stencil)

cdef void GetglGetTexParameterIiv(GLenum target, GLenum pname, GLint *params):
    global cglGetTexParameterIiv
    cglGetTexParameterIiv = <PFNGLGETTEXPARAMETERIIVPROC>getFunction(b"glGetTexParameterIiv")
    cglGetTexParameterIiv(target, pname, params)

cdef void GetglUniform2ui(GLint location, GLuint v0, GLuint v1):
    global cglUniform2ui
    cglUniform2ui = <PFNGLUNIFORM2UIPROC>getFunction(b"glUniform2ui")
    cglUniform2ui(location, v0, v1)

cdef void GetglBindFramebuffer(GLenum target, GLuint framebuffer):
    global cglBindFramebuffer
    cglBindFramebuffer = <PFNGLBINDFRAMEBUFFERPROC>getFunction(b"glBindFramebuffer")
    cglBindFramebuffer(target, framebuffer)

cdef void GetglRenderbufferStorageMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height):
    global cglRenderbufferStorageMultisample
    cglRenderbufferStorageMultisample = <PFNGLRENDERBUFFERSTORAGEMULTISAMPLEPROC>getFunction(b"glRenderbufferStorageMultisample")
    cglRenderbufferStorageMultisample(target, samples, internalformat, width, height)

cdef void GetglDisablei(GLenum target, GLuint index):
    global cglDisablei
    cglDisablei = <PFNGLDISABLEIPROC>getFunction(b"glDisablei")
    cglDisablei(target, index)

cdef void GetglDeleteFramebuffers(GLsizei n, const GLuint *framebuffers):
    global cglDeleteFramebuffers
    cglDeleteFramebuffers = <PFNGLDELETEFRAMEBUFFERSPROC>getFunction(b"glDeleteFramebuffers")
    cglDeleteFramebuffers(n, framebuffers)

cdef void GetglVertexAttribI4usv(GLuint index, const GLushort *v):
    global cglVertexAttribI4usv
    cglVertexAttribI4usv = <PFNGLVERTEXATTRIBI4USVPROC>getFunction(b"glVertexAttribI4usv")
    cglVertexAttribI4usv(index, v)

cdef void GetglVertexAttribI2iv(GLuint index, const GLint *v):
    global cglVertexAttribI2iv
    cglVertexAttribI2iv = <PFNGLVERTEXATTRIBI2IVPROC>getFunction(b"glVertexAttribI2iv")
    cglVertexAttribI2iv(index, v)

cdef void GetglUniform1ui(GLint location, GLuint v0):
    global cglUniform1ui
    cglUniform1ui = <PFNGLUNIFORM1UIPROC>getFunction(b"glUniform1ui")
    cglUniform1ui(location, v0)

cdef void GetglClearBufferiv(GLenum buffer, GLint drawbuffer, const GLint *value):
    global cglClearBufferiv
    cglClearBufferiv = <PFNGLCLEARBUFFERIVPROC>getFunction(b"glClearBufferiv")
    cglClearBufferiv(buffer, drawbuffer, value)

cdef void GetglClampColor(GLenum target, GLenum clamp):
    global cglClampColor
    cglClampColor = <PFNGLCLAMPCOLORPROC>getFunction(b"glClampColor")
    cglClampColor(target, clamp)

cdef void GetglBindBufferBase(GLenum target, GLuint index, GLuint buffer):
    global cglBindBufferBase
    cglBindBufferBase = <PFNGLBINDBUFFERBASEPROC>getFunction(b"glBindBufferBase")
    cglBindBufferBase(target, index, buffer)

cdef void GetglEndTransformFeedback():
    global cglEndTransformFeedback
    cglEndTransformFeedback = <PFNGLENDTRANSFORMFEEDBACKPROC>getFunction(b"glEndTransformFeedback")
    cglEndTransformFeedback()

cdef void GetglVertexAttribI3i(GLuint index, GLint x, GLint y, GLint z):
    global cglVertexAttribI3i
    cglVertexAttribI3i = <PFNGLVERTEXATTRIBI3IPROC>getFunction(b"glVertexAttribI3i")
    cglVertexAttribI3i(index, x, y, z)

cdef void GetglGenerateMipmap(GLenum target):
    global cglGenerateMipmap
    cglGenerateMipmap = <PFNGLGENERATEMIPMAPPROC>getFunction(b"glGenerateMipmap")
    cglGenerateMipmap(target)

cdef void GetglFlushMappedBufferRange(GLenum target, GLintptr offset, GLsizeiptr length):
    global cglFlushMappedBufferRange
    cglFlushMappedBufferRange = <PFNGLFLUSHMAPPEDBUFFERRANGEPROC>getFunction(b"glFlushMappedBufferRange")
    cglFlushMappedBufferRange(target, offset, length)

cdef void GetglGetVertexAttribIiv(GLuint index, GLenum pname, GLint *params):
    global cglGetVertexAttribIiv
    cglGetVertexAttribIiv = <PFNGLGETVERTEXATTRIBIIVPROC>getFunction(b"glGetVertexAttribIiv")
    cglGetVertexAttribIiv(index, pname, params)

cdef void GetglUniform1uiv(GLint location, GLsizei count, const GLuint *value):
    global cglUniform1uiv
    cglUniform1uiv = <PFNGLUNIFORM1UIVPROC>getFunction(b"glUniform1uiv")
    cglUniform1uiv(location, count, value)

cdef void GetglTexParameterIiv(GLenum target, GLenum pname, const GLint *params):
    global cglTexParameterIiv
    cglTexParameterIiv = <PFNGLTEXPARAMETERIIVPROC>getFunction(b"glTexParameterIiv")
    cglTexParameterIiv(target, pname, params)

cdef void GetglBindRenderbuffer(GLenum target, GLuint renderbuffer):
    global cglBindRenderbuffer
    cglBindRenderbuffer = <PFNGLBINDRENDERBUFFERPROC>getFunction(b"glBindRenderbuffer")
    cglBindRenderbuffer(target, renderbuffer)

cdef void GetglVertexAttribI4uiv(GLuint index, const GLuint *v):
    global cglVertexAttribI4uiv
    cglVertexAttribI4uiv = <PFNGLVERTEXATTRIBI4UIVPROC>getFunction(b"glVertexAttribI4uiv")
    cglVertexAttribI4uiv(index, v)

cdef GLenum GetglCheckFramebufferStatus(GLenum target):
    global cglCheckFramebufferStatus
    cglCheckFramebufferStatus = <PFNGLCHECKFRAMEBUFFERSTATUSPROC>getFunction(b"glCheckFramebufferStatus")
    cglCheckFramebufferStatus(target)

cdef void GetglFramebufferRenderbuffer(GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer):
    global cglFramebufferRenderbuffer
    cglFramebufferRenderbuffer = <PFNGLFRAMEBUFFERRENDERBUFFERPROC>getFunction(b"glFramebufferRenderbuffer")
    cglFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)

cdef void GetglVertexAttribI1ui(GLuint index, GLuint x):
    global cglVertexAttribI1ui
    cglVertexAttribI1ui = <PFNGLVERTEXATTRIBI1UIPROC>getFunction(b"glVertexAttribI1ui")
    cglVertexAttribI1ui(index, x)

cdef void GetglUniform3ui(GLint location, GLuint v0, GLuint v1, GLuint v2):
    global cglUniform3ui
    cglUniform3ui = <PFNGLUNIFORM3UIPROC>getFunction(b"glUniform3ui")
    cglUniform3ui(location, v0, v1, v2)

cdef void GetglGenFramebuffers(GLsizei n, GLuint *framebuffers):
    global cglGenFramebuffers
    cglGenFramebuffers = <PFNGLGENFRAMEBUFFERSPROC>getFunction(b"glGenFramebuffers")
    cglGenFramebuffers(n, framebuffers)

cdef void GetglBeginConditionalRender(GLuint id, GLenum mode):
    global cglBeginConditionalRender
    cglBeginConditionalRender = <PFNGLBEGINCONDITIONALRENDERPROC>getFunction(b"glBeginConditionalRender")
    cglBeginConditionalRender(id, mode)

cdef void GetglVertexAttribI1uiv(GLuint index, const GLuint *v):
    global cglVertexAttribI1uiv
    cglVertexAttribI1uiv = <PFNGLVERTEXATTRIBI1UIVPROC>getFunction(b"glVertexAttribI1uiv")
    cglVertexAttribI1uiv(index, v)

cdef void GetglGetIntegeri_v(GLenum target, GLuint index, GLint *data):
    global cglGetIntegeri_v
    cglGetIntegeri_v = <PFNGLGETINTEGERI_VPROC>getFunction(b"glGetIntegeri_v")
    cglGetIntegeri_v(target, index, data)

cdef void GetglColorMaski(GLuint index, GLboolean r, GLboolean g, GLboolean b, GLboolean a):
    global cglColorMaski
    cglColorMaski = <PFNGLCOLORMASKIPROC>getFunction(b"glColorMaski")
    cglColorMaski(index, r, g, b, a)

cdef GLboolean GetglIsVertexArray(GLuint array):
    global cglIsVertexArray
    cglIsVertexArray = <PFNGLISVERTEXARRAYPROC>getFunction(b"glIsVertexArray")
    cglIsVertexArray(array)

cdef void GetglVertexAttribI2ui(GLuint index, GLuint x, GLuint y):
    global cglVertexAttribI2ui
    cglVertexAttribI2ui = <PFNGLVERTEXATTRIBI2UIPROC>getFunction(b"glVertexAttribI2ui")
    cglVertexAttribI2ui(index, x, y)

cdef void GetglClearBufferuiv(GLenum buffer, GLint drawbuffer, const GLuint *value):
    global cglClearBufferuiv
    cglClearBufferuiv = <PFNGLCLEARBUFFERUIVPROC>getFunction(b"glClearBufferuiv")
    cglClearBufferuiv(buffer, drawbuffer, value)

cdef void GetglGetBooleani_v(GLenum target, GLuint index, GLboolean *data):
    global cglGetBooleani_v
    cglGetBooleani_v = <PFNGLGETBOOLEANI_VPROC>getFunction(b"glGetBooleani_v")
    cglGetBooleani_v(target, index, data)

cdef void GetglGetVertexAttribIuiv(GLuint index, GLenum pname, GLuint *params):
    global cglGetVertexAttribIuiv
    cglGetVertexAttribIuiv = <PFNGLGETVERTEXATTRIBIUIVPROC>getFunction(b"glGetVertexAttribIuiv")
    cglGetVertexAttribIuiv(index, pname, params)

cglIsRenderbuffer = GetglIsRenderbuffer
cglVertexAttribI4i = GetglVertexAttribI4i
cglGetRenderbufferParameteriv = GetglGetRenderbufferParameteriv
cglVertexAttribI4sv = GetglVertexAttribI4sv
cglUniform3uiv = GetglUniform3uiv
cglEnablei = GetglEnablei
cglTransformFeedbackVaryings = GetglTransformFeedbackVaryings
cglIsEnabledi = GetglIsEnabledi
cglTexParameterIuiv = GetglTexParameterIuiv
cglUniform2uiv = GetglUniform2uiv
cglClearBufferfv = GetglClearBufferfv
cglVertexAttribI2i = GetglVertexAttribI2i
cglFramebufferTexture2D = GetglFramebufferTexture2D
cglVertexAttribI1iv = GetglVertexAttribI1iv
cglVertexAttribIPointer = GetglVertexAttribIPointer
cglFramebufferTextureLayer = GetglFramebufferTextureLayer
cglVertexAttribI4bv = GetglVertexAttribI4bv
cglVertexAttribI4iv = GetglVertexAttribI4iv
cglGetFramebufferAttachmentParameteriv = GetglGetFramebufferAttachmentParameteriv
cglGenVertexArrays = GetglGenVertexArrays
cglVertexAttribI3ui = GetglVertexAttribI3ui
cglGenRenderbuffers = GetglGenRenderbuffers
cglGetFragDataLocation = GetglGetFragDataLocation
cglFramebufferTexture1D = GetglFramebufferTexture1D
cglVertexAttribI3iv = GetglVertexAttribI3iv
cglVertexAttribI1i = GetglVertexAttribI1i
cglEndConditionalRender = GetglEndConditionalRender
cglGetStringi = GetglGetStringi
cglDeleteVertexArrays = GetglDeleteVertexArrays
cglBlitFramebuffer = GetglBlitFramebuffer
cglMapBufferRange = GetglMapBufferRange
cglFramebufferTexture3D = GetglFramebufferTexture3D
cglUniform4ui = GetglUniform4ui
cglIsFramebuffer = GetglIsFramebuffer
cglDeleteRenderbuffers = GetglDeleteRenderbuffers
cglVertexAttribI4ubv = GetglVertexAttribI4ubv
cglUniform4uiv = GetglUniform4uiv
cglBindVertexArray = GetglBindVertexArray
cglGetTexParameterIuiv = GetglGetTexParameterIuiv
cglRenderbufferStorage = GetglRenderbufferStorage
cglVertexAttribI2uiv = GetglVertexAttribI2uiv
cglBindFragDataLocation = GetglBindFragDataLocation
cglVertexAttribI3uiv = GetglVertexAttribI3uiv
cglGetTransformFeedbackVarying = GetglGetTransformFeedbackVarying
cglVertexAttribI4ui = GetglVertexAttribI4ui
cglGetUniformuiv = GetglGetUniformuiv
cglBindBufferRange = GetglBindBufferRange
cglBeginTransformFeedback = GetglBeginTransformFeedback
cglClearBufferfi = GetglClearBufferfi
cglGetTexParameterIiv = GetglGetTexParameterIiv
cglUniform2ui = GetglUniform2ui
cglBindFramebuffer = GetglBindFramebuffer
cglRenderbufferStorageMultisample = GetglRenderbufferStorageMultisample
cglDisablei = GetglDisablei
cglDeleteFramebuffers = GetglDeleteFramebuffers
cglVertexAttribI4usv = GetglVertexAttribI4usv
cglVertexAttribI2iv = GetglVertexAttribI2iv
cglUniform1ui = GetglUniform1ui
cglClearBufferiv = GetglClearBufferiv
cglClampColor = GetglClampColor
cglBindBufferBase = GetglBindBufferBase
cglEndTransformFeedback = GetglEndTransformFeedback
cglVertexAttribI3i = GetglVertexAttribI3i
cglGenerateMipmap = GetglGenerateMipmap
cglFlushMappedBufferRange = GetglFlushMappedBufferRange
cglGetVertexAttribIiv = GetglGetVertexAttribIiv
cglUniform1uiv = GetglUniform1uiv
cglTexParameterIiv = GetglTexParameterIiv
cglBindRenderbuffer = GetglBindRenderbuffer
cglVertexAttribI4uiv = GetglVertexAttribI4uiv
cglCheckFramebufferStatus = GetglCheckFramebufferStatus
cglFramebufferRenderbuffer = GetglFramebufferRenderbuffer
cglVertexAttribI1ui = GetglVertexAttribI1ui
cglUniform3ui = GetglUniform3ui
cglGenFramebuffers = GetglGenFramebuffers
cglBeginConditionalRender = GetglBeginConditionalRender
cglVertexAttribI1uiv = GetglVertexAttribI1uiv
cglGetIntegeri_v = GetglGetIntegeri_v
cglColorMaski = GetglColorMaski
cglIsVertexArray = GetglIsVertexArray
cglVertexAttribI2ui = GetglVertexAttribI2ui
cglClearBufferuiv = GetglClearBufferuiv
cglGetBooleani_v = GetglGetBooleani_v
cglGetVertexAttribIuiv = GetglGetVertexAttribIuiv


cdef GLboolean glIsRenderbuffer(GLuint renderbuffer):
    cglIsRenderbuffer(renderbuffer)

cdef void glVertexAttribI4i(GLuint index, GLint x, GLint y, GLint z, GLint w):
    cglVertexAttribI4i(index, x, y, z, w)

cdef void glGetRenderbufferParameteriv(GLenum target, GLenum pname, GLint *params):
    cglGetRenderbufferParameteriv(target, pname, params)

cdef void glVertexAttribI4sv(GLuint index, const GLshort *v):
    cglVertexAttribI4sv(index, v)

cdef void glUniform3uiv(GLint location, GLsizei count, const GLuint *value):
    cglUniform3uiv(location, count, value)

cdef void glEnablei(GLenum target, GLuint index):
    cglEnablei(target, index)

cdef void glTransformFeedbackVaryings(GLuint program, GLsizei count, const GLchar **varyings, GLenum bufferMode):
    cglTransformFeedbackVaryings(program, count, varyings, bufferMode)

cdef GLboolean glIsEnabledi(GLenum target, GLuint index):
    cglIsEnabledi(target, index)

cdef void glTexParameterIuiv(GLenum target, GLenum pname, const GLuint *params):
    cglTexParameterIuiv(target, pname, params)

cdef void glUniform2uiv(GLint location, GLsizei count, const GLuint *value):
    cglUniform2uiv(location, count, value)

cdef void glClearBufferfv(GLenum buffer, GLint drawbuffer, const GLfloat *value):
    cglClearBufferfv(buffer, drawbuffer, value)

cdef void glVertexAttribI2i(GLuint index, GLint x, GLint y):
    cglVertexAttribI2i(index, x, y)

cdef void glFramebufferTexture2D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level):
    cglFramebufferTexture2D(target, attachment, textarget, texture, level)

cdef void glVertexAttribI1iv(GLuint index, const GLint *v):
    cglVertexAttribI1iv(index, v)

cdef void glVertexAttribIPointer(GLuint index, GLint size, GLenum type, GLsizei stride, const void *pointer):
    cglVertexAttribIPointer(index, size, type, stride, pointer)

cdef void glFramebufferTextureLayer(GLenum target, GLenum attachment, GLuint texture, GLint level, GLint layer):
    cglFramebufferTextureLayer(target, attachment, texture, level, layer)

cdef void glVertexAttribI4bv(GLuint index, const GLbyte *v):
    cglVertexAttribI4bv(index, v)

cdef void glVertexAttribI4iv(GLuint index, const GLint *v):
    cglVertexAttribI4iv(index, v)

cdef void glGetFramebufferAttachmentParameteriv(GLenum target, GLenum attachment, GLenum pname, GLint *params):
    cglGetFramebufferAttachmentParameteriv(target, attachment, pname, params)

cdef void glGenVertexArrays(GLsizei n, GLuint *arrays):
    cglGenVertexArrays(n, arrays)

cdef void glVertexAttribI3ui(GLuint index, GLuint x, GLuint y, GLuint z):
    cglVertexAttribI3ui(index, x, y, z)

cdef void glGenRenderbuffers(GLsizei n, GLuint *renderbuffers):
    cglGenRenderbuffers(n, renderbuffers)

cdef GLint glGetFragDataLocation(GLuint program, const GLchar *name):
    cglGetFragDataLocation(program, name)

cdef void glFramebufferTexture1D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level):
    cglFramebufferTexture1D(target, attachment, textarget, texture, level)

cdef void glVertexAttribI3iv(GLuint index, const GLint *v):
    cglVertexAttribI3iv(index, v)

cdef void glVertexAttribI1i(GLuint index, GLint x):
    cglVertexAttribI1i(index, x)

cdef void glEndConditionalRender():
    cglEndConditionalRender()

cdef const GLubyte *glGetStringi(GLenum name, GLuint index):
    cglGetStringi(name, index)

cdef void glDeleteVertexArrays(GLsizei n, const GLuint *arrays):
    cglDeleteVertexArrays(n, arrays)

cdef void glBlitFramebuffer(GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter):
    cglBlitFramebuffer(srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)

cdef void *glMapBufferRange(GLenum target, GLintptr offset, GLsizeiptr length, GLbitfield access):
    cglMapBufferRange(target, offset, length, access)

cdef void glFramebufferTexture3D(GLenum target, GLenum attachment, GLenum textarget, GLuint texture, GLint level, GLint zoffset):
    cglFramebufferTexture3D(target, attachment, textarget, texture, level, zoffset)

cdef void glUniform4ui(GLint location, GLuint v0, GLuint v1, GLuint v2, GLuint v3):
    cglUniform4ui(location, v0, v1, v2, v3)

cdef GLboolean glIsFramebuffer(GLuint framebuffer):
    cglIsFramebuffer(framebuffer)

cdef void glDeleteRenderbuffers(GLsizei n, const GLuint *renderbuffers):
    cglDeleteRenderbuffers(n, renderbuffers)

cdef void glVertexAttribI4ubv(GLuint index, const GLubyte *v):
    cglVertexAttribI4ubv(index, v)

cdef void glUniform4uiv(GLint location, GLsizei count, const GLuint *value):
    cglUniform4uiv(location, count, value)

cdef void glBindVertexArray(GLuint array):
    cglBindVertexArray(array)

cdef void glGetTexParameterIuiv(GLenum target, GLenum pname, GLuint *params):
    cglGetTexParameterIuiv(target, pname, params)

cdef void glRenderbufferStorage(GLenum target, GLenum internalformat, GLsizei width, GLsizei height):
    cglRenderbufferStorage(target, internalformat, width, height)

cdef void glVertexAttribI2uiv(GLuint index, const GLuint *v):
    cglVertexAttribI2uiv(index, v)

cdef void glBindFragDataLocation(GLuint program, GLuint color, const GLchar *name):
    cglBindFragDataLocation(program, color, name)

cdef void glVertexAttribI3uiv(GLuint index, const GLuint *v):
    cglVertexAttribI3uiv(index, v)

cdef void glGetTransformFeedbackVarying(GLuint program, GLuint index, GLsizei bufSize, GLsizei *length, GLsizei *size, GLenum *type, GLchar *name):
    cglGetTransformFeedbackVarying(program, index, bufSize, length, size, type, name)

cdef void glVertexAttribI4ui(GLuint index, GLuint x, GLuint y, GLuint z, GLuint w):
    cglVertexAttribI4ui(index, x, y, z, w)

cdef void glGetUniformuiv(GLuint program, GLint location, GLuint *params):
    cglGetUniformuiv(program, location, params)

cdef void glBindBufferRange(GLenum target, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size):
    cglBindBufferRange(target, index, buffer, offset, size)

cdef void glBeginTransformFeedback(GLenum primitiveMode):
    cglBeginTransformFeedback(primitiveMode)

cdef void glClearBufferfi(GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil):
    cglClearBufferfi(buffer, drawbuffer, depth, stencil)

cdef void glGetTexParameterIiv(GLenum target, GLenum pname, GLint *params):
    cglGetTexParameterIiv(target, pname, params)

cdef void glUniform2ui(GLint location, GLuint v0, GLuint v1):
    cglUniform2ui(location, v0, v1)

cdef void glBindFramebuffer(GLenum target, GLuint framebuffer):
    cglBindFramebuffer(target, framebuffer)

cdef void glRenderbufferStorageMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height):
    cglRenderbufferStorageMultisample(target, samples, internalformat, width, height)

cdef void glDisablei(GLenum target, GLuint index):
    cglDisablei(target, index)

cdef void glDeleteFramebuffers(GLsizei n, const GLuint *framebuffers):
    cglDeleteFramebuffers(n, framebuffers)

cdef void glVertexAttribI4usv(GLuint index, const GLushort *v):
    cglVertexAttribI4usv(index, v)

cdef void glVertexAttribI2iv(GLuint index, const GLint *v):
    cglVertexAttribI2iv(index, v)

cdef void glUniform1ui(GLint location, GLuint v0):
    cglUniform1ui(location, v0)

cdef void glClearBufferiv(GLenum buffer, GLint drawbuffer, const GLint *value):
    cglClearBufferiv(buffer, drawbuffer, value)

cdef void glClampColor(GLenum target, GLenum clamp):
    cglClampColor(target, clamp)

cdef void glBindBufferBase(GLenum target, GLuint index, GLuint buffer):
    cglBindBufferBase(target, index, buffer)

cdef void glEndTransformFeedback():
    cglEndTransformFeedback()

cdef void glVertexAttribI3i(GLuint index, GLint x, GLint y, GLint z):
    cglVertexAttribI3i(index, x, y, z)

cdef void glGenerateMipmap(GLenum target):
    cglGenerateMipmap(target)

cdef void glFlushMappedBufferRange(GLenum target, GLintptr offset, GLsizeiptr length):
    cglFlushMappedBufferRange(target, offset, length)

cdef void glGetVertexAttribIiv(GLuint index, GLenum pname, GLint *params):
    cglGetVertexAttribIiv(index, pname, params)

cdef void glUniform1uiv(GLint location, GLsizei count, const GLuint *value):
    cglUniform1uiv(location, count, value)

cdef void glTexParameterIiv(GLenum target, GLenum pname, const GLint *params):
    cglTexParameterIiv(target, pname, params)

cdef void glBindRenderbuffer(GLenum target, GLuint renderbuffer):
    cglBindRenderbuffer(target, renderbuffer)

cdef void glVertexAttribI4uiv(GLuint index, const GLuint *v):
    cglVertexAttribI4uiv(index, v)

cdef GLenum glCheckFramebufferStatus(GLenum target):
    cglCheckFramebufferStatus(target)

cdef void glFramebufferRenderbuffer(GLenum target, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer):
    cglFramebufferRenderbuffer(target, attachment, renderbuffertarget, renderbuffer)

cdef void glVertexAttribI1ui(GLuint index, GLuint x):
    cglVertexAttribI1ui(index, x)

cdef void glUniform3ui(GLint location, GLuint v0, GLuint v1, GLuint v2):
    cglUniform3ui(location, v0, v1, v2)

cdef void glGenFramebuffers(GLsizei n, GLuint *framebuffers):
    cglGenFramebuffers(n, framebuffers)

cdef void glBeginConditionalRender(GLuint id, GLenum mode):
    cglBeginConditionalRender(id, mode)

cdef void glVertexAttribI1uiv(GLuint index, const GLuint *v):
    cglVertexAttribI1uiv(index, v)

cdef void glGetIntegeri_v(GLenum target, GLuint index, GLint *data):
    cglGetIntegeri_v(target, index, data)

cdef void glColorMaski(GLuint index, GLboolean r, GLboolean g, GLboolean b, GLboolean a):
    cglColorMaski(index, r, g, b, a)

cdef GLboolean glIsVertexArray(GLuint array):
    cglIsVertexArray(array)

cdef void glVertexAttribI2ui(GLuint index, GLuint x, GLuint y):
    cglVertexAttribI2ui(index, x, y)

cdef void glClearBufferuiv(GLenum buffer, GLint drawbuffer, const GLuint *value):
    cglClearBufferuiv(buffer, drawbuffer, value)

cdef void glGetBooleani_v(GLenum target, GLuint index, GLboolean *data):
    cglGetBooleani_v(target, index, data)

cdef void glGetVertexAttribIuiv(GLuint index, GLenum pname, GLuint *params):
    cglGetVertexAttribIuiv(index, pname, params)
