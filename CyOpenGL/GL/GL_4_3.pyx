# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_ACTIVE_RESOURCES = 0x92F5
cdef GLenum GL_ACTIVE_VARIABLES = 0x9305
cdef GLenum GL_ANY_SAMPLES_PASSED_CONSERVATIVE = 0x8D6A
cdef GLenum GL_ARRAY_SIZE = 0x92FB
cdef GLenum GL_ARRAY_STRIDE = 0x92FE
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_INDEX = 0x9301
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER = 0x90ED
cdef GLenum GL_AUTO_GENERATE_MIPMAP = 0x8295
cdef GLenum GL_BLOCK_INDEX = 0x92FD
cdef GLenum GL_BUFFER = 0x82E0
cdef GLenum GL_BUFFER_BINDING = 0x9302
cdef GLenum GL_BUFFER_DATA_SIZE = 0x9303
cdef GLenum GL_BUFFER_VARIABLE = 0x92E5
cdef GLenum GL_CAVEAT_SUPPORT = 0x82B8
cdef GLenum GL_CLEAR_BUFFER = 0x82B4
cdef GLenum GL_COLOR_COMPONENTS = 0x8283
cdef GLenum GL_COLOR_ENCODING = 0x8296
cdef GLenum GL_COLOR_RENDERABLE = 0x8286
cdef GLenum GL_COMPRESSED_R11_EAC = 0x9270
cdef GLenum GL_COMPRESSED_RG11_EAC = 0x9272
cdef GLenum GL_COMPRESSED_RGB8_ETC2 = 0x9274
cdef GLenum GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9276
cdef GLenum GL_COMPRESSED_RGBA8_ETC2_EAC = 0x9278
cdef GLenum GL_COMPRESSED_SIGNED_R11_EAC = 0x9271
cdef GLenum GL_COMPRESSED_SIGNED_RG11_EAC = 0x9273
cdef GLenum GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 0x9279
cdef GLenum GL_COMPRESSED_SRGB8_ETC2 = 0x9275
cdef GLenum GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9277
cdef GLenum GL_COMPUTE_SHADER = 0x91B9
cdef GLenum GL_COMPUTE_SHADER_BIT = 0x00000020
cdef GLenum GL_COMPUTE_SUBROUTINE = 0x92ED
cdef GLenum GL_COMPUTE_SUBROUTINE_UNIFORM = 0x92F3
cdef GLenum GL_COMPUTE_TEXTURE = 0x82A0
cdef GLenum GL_COMPUTE_WORK_GROUP_SIZE = 0x8267
cdef GLenum GL_CONTEXT_FLAG_DEBUG_BIT = 0x00000002
cdef GLenum GL_DEBUG_CALLBACK_FUNCTION = 0x8244
cdef GLenum GL_DEBUG_CALLBACK_USER_PARAM = 0x8245
cdef GLenum GL_DEBUG_GROUP_STACK_DEPTH = 0x826D
cdef GLenum GL_DEBUG_LOGGED_MESSAGES = 0x9145
cdef GLenum GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH = 0x8243
cdef GLenum GL_DEBUG_OUTPUT = 0x92E0
cdef GLenum GL_DEBUG_OUTPUT_SYNCHRONOUS = 0x8242
cdef GLenum GL_DEBUG_SEVERITY_HIGH = 0x9146
cdef GLenum GL_DEBUG_SEVERITY_LOW = 0x9148
cdef GLenum GL_DEBUG_SEVERITY_MEDIUM = 0x9147
cdef GLenum GL_DEBUG_SEVERITY_NOTIFICATION = 0x826B
cdef GLenum GL_DEBUG_SOURCE_API = 0x8246
cdef GLenum GL_DEBUG_SOURCE_APPLICATION = 0x824A
cdef GLenum GL_DEBUG_SOURCE_OTHER = 0x824B
cdef GLenum GL_DEBUG_SOURCE_SHADER_COMPILER = 0x8248
cdef GLenum GL_DEBUG_SOURCE_THIRD_PARTY = 0x8249
cdef GLenum GL_DEBUG_SOURCE_WINDOW_SYSTEM = 0x8247
cdef GLenum GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR = 0x824D
cdef GLenum GL_DEBUG_TYPE_ERROR = 0x824C
cdef GLenum GL_DEBUG_TYPE_MARKER = 0x8268
cdef GLenum GL_DEBUG_TYPE_OTHER = 0x8251
cdef GLenum GL_DEBUG_TYPE_PERFORMANCE = 0x8250
cdef GLenum GL_DEBUG_TYPE_POP_GROUP = 0x826A
cdef GLenum GL_DEBUG_TYPE_PORTABILITY = 0x824F
cdef GLenum GL_DEBUG_TYPE_PUSH_GROUP = 0x8269
cdef GLenum GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR = 0x824E
cdef GLenum GL_DEPTH_COMPONENTS = 0x8284
cdef GLenum GL_DEPTH_RENDERABLE = 0x8287
cdef GLenum GL_DEPTH_STENCIL_TEXTURE_MODE = 0x90EA
cdef GLenum GL_DISPATCH_INDIRECT_BUFFER = 0x90EE
cdef GLenum GL_DISPATCH_INDIRECT_BUFFER_BINDING = 0x90EF
cdef GLenum GL_DISPLAY_LIST = 0x82E7
cdef GLenum GL_FILTER = 0x829A
cdef GLenum GL_FRAGMENT_SUBROUTINE = 0x92EC
cdef GLenum GL_FRAGMENT_SUBROUTINE_UNIFORM = 0x92F2
cdef GLenum GL_FRAGMENT_TEXTURE = 0x829F
cdef GLenum GL_FRAMEBUFFER_BLEND = 0x828B
cdef GLenum GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS = 0x9314
cdef GLenum GL_FRAMEBUFFER_DEFAULT_HEIGHT = 0x9311
cdef GLenum GL_FRAMEBUFFER_DEFAULT_LAYERS = 0x9312
cdef GLenum GL_FRAMEBUFFER_DEFAULT_SAMPLES = 0x9313
cdef GLenum GL_FRAMEBUFFER_DEFAULT_WIDTH = 0x9310
cdef GLenum GL_FRAMEBUFFER_RENDERABLE = 0x8289
cdef GLenum GL_FRAMEBUFFER_RENDERABLE_LAYERED = 0x828A
cdef GLenum GL_FULL_SUPPORT = 0x82B7
cdef GLenum GL_GEOMETRY_SUBROUTINE = 0x92EB
cdef GLenum GL_GEOMETRY_SUBROUTINE_UNIFORM = 0x92F1
cdef GLenum GL_GEOMETRY_TEXTURE = 0x829E
cdef GLenum GL_GET_TEXTURE_IMAGE_FORMAT = 0x8291
cdef GLenum GL_GET_TEXTURE_IMAGE_TYPE = 0x8292
cdef GLenum GL_IMAGE_CLASS_10_10_10_2 = 0x82C3
cdef GLenum GL_IMAGE_CLASS_11_11_10 = 0x82C2
cdef GLenum GL_IMAGE_CLASS_1_X_16 = 0x82BE
cdef GLenum GL_IMAGE_CLASS_1_X_32 = 0x82BB
cdef GLenum GL_IMAGE_CLASS_1_X_8 = 0x82C1
cdef GLenum GL_IMAGE_CLASS_2_X_16 = 0x82BD
cdef GLenum GL_IMAGE_CLASS_2_X_32 = 0x82BA
cdef GLenum GL_IMAGE_CLASS_2_X_8 = 0x82C0
cdef GLenum GL_IMAGE_CLASS_4_X_16 = 0x82BC
cdef GLenum GL_IMAGE_CLASS_4_X_32 = 0x82B9
cdef GLenum GL_IMAGE_CLASS_4_X_8 = 0x82BF
cdef GLenum GL_IMAGE_COMPATIBILITY_CLASS = 0x82A8
cdef GLenum GL_IMAGE_PIXEL_FORMAT = 0x82A9
cdef GLenum GL_IMAGE_PIXEL_TYPE = 0x82AA
cdef GLenum GL_IMAGE_TEXEL_SIZE = 0x82A7
cdef GLenum GL_INTERNALFORMAT_ALPHA_SIZE = 0x8274
cdef GLenum GL_INTERNALFORMAT_ALPHA_TYPE = 0x827B
cdef GLenum GL_INTERNALFORMAT_BLUE_SIZE = 0x8273
cdef GLenum GL_INTERNALFORMAT_BLUE_TYPE = 0x827A
cdef GLenum GL_INTERNALFORMAT_DEPTH_SIZE = 0x8275
cdef GLenum GL_INTERNALFORMAT_DEPTH_TYPE = 0x827C
cdef GLenum GL_INTERNALFORMAT_GREEN_SIZE = 0x8272
cdef GLenum GL_INTERNALFORMAT_GREEN_TYPE = 0x8279
cdef GLenum GL_INTERNALFORMAT_PREFERRED = 0x8270
cdef GLenum GL_INTERNALFORMAT_RED_SIZE = 0x8271
cdef GLenum GL_INTERNALFORMAT_RED_TYPE = 0x8278
cdef GLenum GL_INTERNALFORMAT_SHARED_SIZE = 0x8277
cdef GLenum GL_INTERNALFORMAT_STENCIL_SIZE = 0x8276
cdef GLenum GL_INTERNALFORMAT_STENCIL_TYPE = 0x827D
cdef GLenum GL_INTERNALFORMAT_SUPPORTED = 0x826F
cdef GLenum GL_IS_PER_PATCH = 0x92E7
cdef GLenum GL_IS_ROW_MAJOR = 0x9300
cdef GLenum GL_LOCATION = 0x930E
cdef GLenum GL_LOCATION_INDEX = 0x930F
cdef GLenum GL_MANUAL_GENERATE_MIPMAP = 0x8294
cdef GLenum GL_MATRIX_STRIDE = 0x92FF
cdef GLenum GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS = 0x8266
cdef GLenum GL_MAX_COMBINED_DIMENSIONS = 0x8282
cdef GLenum GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES = 0x8F39
cdef GLenum GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS = 0x90DC
cdef GLenum GL_MAX_COMPUTE_ATOMIC_COUNTERS = 0x8265
cdef GLenum GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = 0x8264
cdef GLenum GL_MAX_COMPUTE_IMAGE_UNIFORMS = 0x91BD
cdef GLenum GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS = 0x90DB
cdef GLenum GL_MAX_COMPUTE_SHARED_MEMORY_SIZE = 0x8262
cdef GLenum GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS = 0x91BC
cdef GLenum GL_MAX_COMPUTE_UNIFORM_BLOCKS = 0x91BB
cdef GLenum GL_MAX_COMPUTE_UNIFORM_COMPONENTS = 0x8263
cdef GLenum GL_MAX_COMPUTE_WORK_GROUP_COUNT = 0x91BE
cdef GLenum GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS = 0x90EB
cdef GLenum GL_MAX_COMPUTE_WORK_GROUP_SIZE = 0x91BF
cdef GLenum GL_MAX_DEBUG_GROUP_STACK_DEPTH = 0x826C
cdef GLenum GL_MAX_DEBUG_LOGGED_MESSAGES = 0x9144
cdef GLenum GL_MAX_DEBUG_MESSAGE_LENGTH = 0x9143
cdef GLenum GL_MAX_DEPTH = 0x8280
cdef GLenum GL_MAX_ELEMENT_INDEX = 0x8D6B
cdef GLenum GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS = 0x90DA
cdef GLenum GL_MAX_FRAMEBUFFER_HEIGHT = 0x9316
cdef GLenum GL_MAX_FRAMEBUFFER_LAYERS = 0x9317
cdef GLenum GL_MAX_FRAMEBUFFER_SAMPLES = 0x9318
cdef GLenum GL_MAX_FRAMEBUFFER_WIDTH = 0x9315
cdef GLenum GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS = 0x90D7
cdef GLenum GL_MAX_HEIGHT = 0x827F
cdef GLenum GL_MAX_LABEL_LENGTH = 0x82E8
cdef GLenum GL_MAX_LAYERS = 0x8281
cdef GLenum GL_MAX_NAME_LENGTH = 0x92F6
cdef GLenum GL_MAX_NUM_ACTIVE_VARIABLES = 0x92F7
cdef GLenum GL_MAX_NUM_COMPATIBLE_SUBROUTINES = 0x92F8
cdef GLenum GL_MAX_SHADER_STORAGE_BLOCK_SIZE = 0x90DE
cdef GLenum GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS = 0x90DD
cdef GLenum GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS = 0x90D8
cdef GLenum GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS = 0x90D9
cdef GLenum GL_MAX_UNIFORM_LOCATIONS = 0x826E
cdef GLenum GL_MAX_VERTEX_ATTRIB_BINDINGS = 0x82DA
cdef GLenum GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D9
cdef GLenum GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS = 0x90D6
cdef GLenum GL_MAX_WIDTH = 0x827E
cdef GLenum GL_MIPMAP = 0x8293
cdef GLenum GL_NAME_LENGTH = 0x92F9
cdef GLenum GL_NUM_ACTIVE_VARIABLES = 0x9304
cdef GLenum GL_NUM_SHADING_LANGUAGE_VERSIONS = 0x82E9
cdef GLenum GL_OFFSET = 0x92FC
cdef GLenum GL_PRIMITIVE_RESTART_FIXED_INDEX = 0x8D69
cdef GLenum GL_PROGRAM = 0x82E2
cdef GLenum GL_PROGRAM_INPUT = 0x92E3
cdef GLenum GL_PROGRAM_OUTPUT = 0x92E4
cdef GLenum GL_PROGRAM_PIPELINE = 0x82E4
cdef GLenum GL_QUERY = 0x82E3
cdef GLenum GL_READ_PIXELS = 0x828C
cdef GLenum GL_READ_PIXELS_FORMAT = 0x828D
cdef GLenum GL_READ_PIXELS_TYPE = 0x828E
cdef GLenum GL_REFERENCED_BY_COMPUTE_SHADER = 0x930B
cdef GLenum GL_REFERENCED_BY_FRAGMENT_SHADER = 0x930A
cdef GLenum GL_REFERENCED_BY_GEOMETRY_SHADER = 0x9309
cdef GLenum GL_REFERENCED_BY_TESS_CONTROL_SHADER = 0x9307
cdef GLenum GL_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x9308
cdef GLenum GL_REFERENCED_BY_VERTEX_SHADER = 0x9306
cdef GLenum GL_SAMPLER = 0x82E6
cdef GLenum GL_SHADER = 0x82E1
cdef GLenum GL_SHADER_IMAGE_ATOMIC = 0x82A6
cdef GLenum GL_SHADER_IMAGE_LOAD = 0x82A4
cdef GLenum GL_SHADER_IMAGE_STORE = 0x82A5
cdef GLenum GL_SHADER_STORAGE_BARRIER_BIT = 0x00002000
cdef GLenum GL_SHADER_STORAGE_BLOCK = 0x92E6
cdef GLenum GL_SHADER_STORAGE_BUFFER = 0x90D2
cdef GLenum GL_SHADER_STORAGE_BUFFER_BINDING = 0x90D3
cdef GLenum GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT = 0x90DF
cdef GLenum GL_SHADER_STORAGE_BUFFER_SIZE = 0x90D5
cdef GLenum GL_SHADER_STORAGE_BUFFER_START = 0x90D4
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST = 0x82AC
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE = 0x82AE
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST = 0x82AD
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE = 0x82AF
cdef GLenum GL_SRGB_READ = 0x8297
cdef GLenum GL_SRGB_WRITE = 0x8298
cdef GLenum GL_STACK_OVERFLOW = 0x0503
cdef GLenum GL_STACK_UNDERFLOW = 0x0504
cdef GLenum GL_STENCIL_COMPONENTS = 0x8285
cdef GLenum GL_STENCIL_RENDERABLE = 0x8288
cdef GLenum GL_TESS_CONTROL_SUBROUTINE = 0x92E9
cdef GLenum GL_TESS_CONTROL_SUBROUTINE_UNIFORM = 0x92EF
cdef GLenum GL_TESS_CONTROL_TEXTURE = 0x829C
cdef GLenum GL_TESS_EVALUATION_SUBROUTINE = 0x92EA
cdef GLenum GL_TESS_EVALUATION_SUBROUTINE_UNIFORM = 0x92F0
cdef GLenum GL_TESS_EVALUATION_TEXTURE = 0x829D
cdef GLenum GL_TEXTURE_BUFFER_OFFSET = 0x919D
cdef GLenum GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT = 0x919F
cdef GLenum GL_TEXTURE_BUFFER_SIZE = 0x919E
cdef GLenum GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT = 0x82B2
cdef GLenum GL_TEXTURE_COMPRESSED_BLOCK_SIZE = 0x82B3
cdef GLenum GL_TEXTURE_COMPRESSED_BLOCK_WIDTH = 0x82B1
cdef GLenum GL_TEXTURE_GATHER = 0x82A2
cdef GLenum GL_TEXTURE_GATHER_SHADOW = 0x82A3
cdef GLenum GL_TEXTURE_IMAGE_FORMAT = 0x828F
cdef GLenum GL_TEXTURE_IMAGE_TYPE = 0x8290
cdef GLenum GL_TEXTURE_IMMUTABLE_LEVELS = 0x82DF
cdef GLenum GL_TEXTURE_SHADOW = 0x82A1
cdef GLenum GL_TEXTURE_VIEW = 0x82B5
cdef GLenum GL_TEXTURE_VIEW_MIN_LAYER = 0x82DD
cdef GLenum GL_TEXTURE_VIEW_MIN_LEVEL = 0x82DB
cdef GLenum GL_TEXTURE_VIEW_NUM_LAYERS = 0x82DE
cdef GLenum GL_TEXTURE_VIEW_NUM_LEVELS = 0x82DC
cdef GLenum GL_TOP_LEVEL_ARRAY_SIZE = 0x930C
cdef GLenum GL_TOP_LEVEL_ARRAY_STRIDE = 0x930D
cdef GLenum GL_TRANSFORM_FEEDBACK_VARYING = 0x92F4
cdef GLenum GL_TYPE = 0x92FA
cdef GLenum GL_UNIFORM = 0x92E1
cdef GLenum GL_UNIFORM_BLOCK = 0x92E2
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER = 0x90EC
cdef GLenum GL_VERTEX_ARRAY = 0x8074
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_LONG = 0x874E
cdef GLenum GL_VERTEX_ATTRIB_BINDING = 0x82D4
cdef GLenum GL_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D5
cdef GLenum GL_VERTEX_BINDING_BUFFER = 0x8F4F
cdef GLenum GL_VERTEX_BINDING_DIVISOR = 0x82D6
cdef GLenum GL_VERTEX_BINDING_OFFSET = 0x82D7
cdef GLenum GL_VERTEX_BINDING_STRIDE = 0x82D8
cdef GLenum GL_VERTEX_SUBROUTINE = 0x92E8
cdef GLenum GL_VERTEX_SUBROUTINE_UNIFORM = 0x92EE
cdef GLenum GL_VERTEX_TEXTURE = 0x829B
cdef GLenum GL_VIEW_CLASS_128_BITS = 0x82C4
cdef GLenum GL_VIEW_CLASS_16_BITS = 0x82CA
cdef GLenum GL_VIEW_CLASS_24_BITS = 0x82C9
cdef GLenum GL_VIEW_CLASS_32_BITS = 0x82C8
cdef GLenum GL_VIEW_CLASS_48_BITS = 0x82C7
cdef GLenum GL_VIEW_CLASS_64_BITS = 0x82C6
cdef GLenum GL_VIEW_CLASS_8_BITS = 0x82CB
cdef GLenum GL_VIEW_CLASS_96_BITS = 0x82C5
cdef GLenum GL_VIEW_CLASS_BPTC_FLOAT = 0x82D3
cdef GLenum GL_VIEW_CLASS_BPTC_UNORM = 0x82D2
cdef GLenum GL_VIEW_CLASS_RGTC1_RED = 0x82D0
cdef GLenum GL_VIEW_CLASS_RGTC2_RG = 0x82D1
cdef GLenum GL_VIEW_CLASS_S3TC_DXT1_RGB = 0x82CC
cdef GLenum GL_VIEW_CLASS_S3TC_DXT1_RGBA = 0x82CD
cdef GLenum GL_VIEW_CLASS_S3TC_DXT3_RGBA = 0x82CE
cdef GLenum GL_VIEW_CLASS_S3TC_DXT5_RGBA = 0x82CF
cdef GLenum GL_VIEW_COMPATIBILITY_CLASS = 0x82B6

ctypedef void (*PFNGLBINDVERTEXBUFFERPROC)(GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)
ctypedef void (*PFNGLCLEARBUFFERDATAPROC)(GLenum target, GLenum internalformat, GLenum format, GLenum type, const void *data)
ctypedef void (*PFNGLCLEARBUFFERSUBDATAPROC)(GLenum target, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data)
ctypedef void (*PFNGLCOPYIMAGESUBDATAPROC)(GLuint srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei srcDepth)
ctypedef void (*PFNGLDEBUGMESSAGECALLBACKPROC)(GLDEBUGPROC callback, const void *userParam)
ctypedef void (*PFNGLDEBUGMESSAGECONTROLPROC)(GLenum source, GLenum type, GLenum severity, GLsizei count, const GLuint *ids, GLboolean enabled)
ctypedef void (*PFNGLDEBUGMESSAGEINSERTPROC)(GLenum source, GLenum type, GLuint id, GLenum severity, GLsizei length, const GLchar *buf)
ctypedef void (*PFNGLDISPATCHCOMPUTEPROC)(GLuint num_groups_x, GLuint num_groups_y, GLuint num_groups_z)
ctypedef void (*PFNGLDISPATCHCOMPUTEINDIRECTPROC)(GLintptr indirect)
ctypedef void (*PFNGLFRAMEBUFFERPARAMETERIPROC)(GLenum target, GLenum pname, GLint param)
ctypedef GLuint (*PFNGLGETDEBUGMESSAGELOGPROC)(GLuint count, GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids, GLenum *severities, GLsizei *lengths, GLchar *messageLog)
ctypedef void (*PFNGLGETFRAMEBUFFERPARAMETERIVPROC)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETINTERNALFORMATI64VPROC)(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint64 *params)
ctypedef void (*PFNGLGETOBJECTLABELPROC)(GLenum identifier, GLuint name, GLsizei bufSize, GLsizei *length, GLchar *label)
ctypedef void (*PFNGLGETOBJECTPTRLABELPROC)(const void *ptr, GLsizei bufSize, GLsizei *length, GLchar *label)
ctypedef void (*PFNGLGETPOINTERVPROC)(GLenum pname, void **params)
ctypedef void (*PFNGLGETPROGRAMINTERFACEIVPROC)(GLuint program, GLenum programInterface, GLenum pname, GLint *params)
ctypedef GLuint (*PFNGLGETPROGRAMRESOURCEINDEXPROC)(GLuint program, GLenum programInterface, const GLchar *name)
ctypedef GLint (*PFNGLGETPROGRAMRESOURCELOCATIONPROC)(GLuint program, GLenum programInterface, const GLchar *name)
ctypedef GLint (*PFNGLGETPROGRAMRESOURCELOCATIONINDEXPROC)(GLuint program, GLenum programInterface, const GLchar *name)
ctypedef void (*PFNGLGETPROGRAMRESOURCENAMEPROC)(GLuint program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
ctypedef void (*PFNGLGETPROGRAMRESOURCEIVPROC)(GLuint program, GLenum programInterface, GLuint index, GLsizei propCount, const GLenum *props, GLsizei count, GLsizei *length, GLint *params)
ctypedef void (*PFNGLINVALIDATEBUFFERDATAPROC)(GLuint buffer)
ctypedef void (*PFNGLINVALIDATEBUFFERSUBDATAPROC)(GLuint buffer, GLintptr offset, GLsizeiptr length)
ctypedef void (*PFNGLINVALIDATEFRAMEBUFFERPROC)(GLenum target, GLsizei numAttachments, const GLenum *attachments)
ctypedef void (*PFNGLINVALIDATESUBFRAMEBUFFERPROC)(GLenum target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*PFNGLINVALIDATETEXIMAGEPROC)(GLuint texture, GLint level)
ctypedef void (*PFNGLINVALIDATETEXSUBIMAGEPROC)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth)
ctypedef void (*PFNGLMULTIDRAWARRAYSINDIRECTPROC)(GLenum mode, const void *indirect, GLsizei drawcount, GLsizei stride)
ctypedef void (*PFNGLMULTIDRAWELEMENTSINDIRECTPROC)(GLenum mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei stride)
ctypedef void (*PFNGLOBJECTLABELPROC)(GLenum identifier, GLuint name, GLsizei length, const GLchar *label)
ctypedef void (*PFNGLOBJECTPTRLABELPROC)(const void *ptr, GLsizei length, const GLchar *label)
ctypedef void (*PFNGLPOPDEBUGGROUPPROC)()
ctypedef void (*PFNGLPUSHDEBUGGROUPPROC)(GLenum source, GLuint id, GLsizei length, const GLchar *message)
ctypedef void (*PFNGLSHADERSTORAGEBLOCKBINDINGPROC)(GLuint program, GLuint storageBlockIndex, GLuint storageBlockBinding)
ctypedef void (*PFNGLTEXBUFFERRANGEPROC)(GLenum target, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size)
ctypedef void (*PFNGLTEXSTORAGE2DMULTISAMPLEPROC)(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
ctypedef void (*PFNGLTEXSTORAGE3DMULTISAMPLEPROC)(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
ctypedef void (*PFNGLTEXTUREVIEWPROC)(GLuint texture, GLenum target, GLuint origtexture, GLenum internalformat, GLuint minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers)
ctypedef void (*PFNGLVERTEXATTRIBBINDINGPROC)(GLuint attribindex, GLuint bindingindex)
ctypedef void (*PFNGLVERTEXATTRIBFORMATPROC)(GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset)
ctypedef void (*PFNGLVERTEXATTRIBIFORMATPROC)(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
ctypedef void (*PFNGLVERTEXATTRIBLFORMATPROC)(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
ctypedef void (*PFNGLVERTEXBINDINGDIVISORPROC)(GLuint bindingindex, GLuint divisor)

cdef PFNGLBINDVERTEXBUFFERPROC cglBindVertexBuffer = NULL
cdef PFNGLCLEARBUFFERDATAPROC cglClearBufferData = NULL
cdef PFNGLCLEARBUFFERSUBDATAPROC cglClearBufferSubData = NULL
cdef PFNGLCOPYIMAGESUBDATAPROC cglCopyImageSubData = NULL
cdef PFNGLDEBUGMESSAGECALLBACKPROC cglDebugMessageCallback = NULL
cdef PFNGLDEBUGMESSAGECONTROLPROC cglDebugMessageControl = NULL
cdef PFNGLDEBUGMESSAGEINSERTPROC cglDebugMessageInsert = NULL
cdef PFNGLDISPATCHCOMPUTEPROC cglDispatchCompute = NULL
cdef PFNGLDISPATCHCOMPUTEINDIRECTPROC cglDispatchComputeIndirect = NULL
cdef PFNGLFRAMEBUFFERPARAMETERIPROC cglFramebufferParameteri = NULL
cdef PFNGLGETDEBUGMESSAGELOGPROC cglGetDebugMessageLog = NULL
cdef PFNGLGETFRAMEBUFFERPARAMETERIVPROC cglGetFramebufferParameteriv = NULL
cdef PFNGLGETINTERNALFORMATI64VPROC cglGetInternalformati64v = NULL
cdef PFNGLGETOBJECTLABELPROC cglGetObjectLabel = NULL
cdef PFNGLGETOBJECTPTRLABELPROC cglGetObjectPtrLabel = NULL
cdef PFNGLGETPOINTERVPROC cglGetPointerv = NULL
cdef PFNGLGETPROGRAMINTERFACEIVPROC cglGetProgramInterfaceiv = NULL
cdef PFNGLGETPROGRAMRESOURCEINDEXPROC cglGetProgramResourceIndex = NULL
cdef PFNGLGETPROGRAMRESOURCELOCATIONPROC cglGetProgramResourceLocation = NULL
cdef PFNGLGETPROGRAMRESOURCELOCATIONINDEXPROC cglGetProgramResourceLocationIndex = NULL
cdef PFNGLGETPROGRAMRESOURCENAMEPROC cglGetProgramResourceName = NULL
cdef PFNGLGETPROGRAMRESOURCEIVPROC cglGetProgramResourceiv = NULL
cdef PFNGLINVALIDATEBUFFERDATAPROC cglInvalidateBufferData = NULL
cdef PFNGLINVALIDATEBUFFERSUBDATAPROC cglInvalidateBufferSubData = NULL
cdef PFNGLINVALIDATEFRAMEBUFFERPROC cglInvalidateFramebuffer = NULL
cdef PFNGLINVALIDATESUBFRAMEBUFFERPROC cglInvalidateSubFramebuffer = NULL
cdef PFNGLINVALIDATETEXIMAGEPROC cglInvalidateTexImage = NULL
cdef PFNGLINVALIDATETEXSUBIMAGEPROC cglInvalidateTexSubImage = NULL
cdef PFNGLMULTIDRAWARRAYSINDIRECTPROC cglMultiDrawArraysIndirect = NULL
cdef PFNGLMULTIDRAWELEMENTSINDIRECTPROC cglMultiDrawElementsIndirect = NULL
cdef PFNGLOBJECTLABELPROC cglObjectLabel = NULL
cdef PFNGLOBJECTPTRLABELPROC cglObjectPtrLabel = NULL
cdef PFNGLPOPDEBUGGROUPPROC cglPopDebugGroup = NULL
cdef PFNGLPUSHDEBUGGROUPPROC cglPushDebugGroup = NULL
cdef PFNGLSHADERSTORAGEBLOCKBINDINGPROC cglShaderStorageBlockBinding = NULL
cdef PFNGLTEXBUFFERRANGEPROC cglTexBufferRange = NULL
cdef PFNGLTEXSTORAGE2DMULTISAMPLEPROC cglTexStorage2DMultisample = NULL
cdef PFNGLTEXSTORAGE3DMULTISAMPLEPROC cglTexStorage3DMultisample = NULL
cdef PFNGLTEXTUREVIEWPROC cglTextureView = NULL
cdef PFNGLVERTEXATTRIBBINDINGPROC cglVertexAttribBinding = NULL
cdef PFNGLVERTEXATTRIBFORMATPROC cglVertexAttribFormat = NULL
cdef PFNGLVERTEXATTRIBIFORMATPROC cglVertexAttribIFormat = NULL
cdef PFNGLVERTEXATTRIBLFORMATPROC cglVertexAttribLFormat = NULL
cdef PFNGLVERTEXBINDINGDIVISORPROC cglVertexBindingDivisor = NULL


cdef void GetglBindVertexBuffer(GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride):
    global cglBindVertexBuffer
    cglBindVertexBuffer = <PFNGLBINDVERTEXBUFFERPROC>getFunction(b"glBindVertexBuffer")
    cglBindVertexBuffer(bindingindex, buffer, offset, stride)

cdef void GetglClearBufferData(GLenum target, GLenum internalformat, GLenum format, GLenum type, const void *data):
    global cglClearBufferData
    cglClearBufferData = <PFNGLCLEARBUFFERDATAPROC>getFunction(b"glClearBufferData")
    cglClearBufferData(target, internalformat, format, type, data)

cdef void GetglClearBufferSubData(GLenum target, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data):
    global cglClearBufferSubData
    cglClearBufferSubData = <PFNGLCLEARBUFFERSUBDATAPROC>getFunction(b"glClearBufferSubData")
    cglClearBufferSubData(target, internalformat, offset, size, format, type, data)

cdef void GetglCopyImageSubData(GLuint srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei srcDepth):
    global cglCopyImageSubData
    cglCopyImageSubData = <PFNGLCOPYIMAGESUBDATAPROC>getFunction(b"glCopyImageSubData")
    cglCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth)

cdef void GetglDebugMessageCallback(GLDEBUGPROC callback, const void *userParam):
    global cglDebugMessageCallback
    cglDebugMessageCallback = <PFNGLDEBUGMESSAGECALLBACKPROC>getFunction(b"glDebugMessageCallback")
    cglDebugMessageCallback(callback, userParam)

cdef void GetglDebugMessageControl(GLenum source, GLenum type, GLenum severity, GLsizei count, const GLuint *ids, GLboolean enabled):
    global cglDebugMessageControl
    cglDebugMessageControl = <PFNGLDEBUGMESSAGECONTROLPROC>getFunction(b"glDebugMessageControl")
    cglDebugMessageControl(source, type, severity, count, ids, enabled)

cdef void GetglDebugMessageInsert(GLenum source, GLenum type, GLuint id, GLenum severity, GLsizei length, const GLchar *buf):
    global cglDebugMessageInsert
    cglDebugMessageInsert = <PFNGLDEBUGMESSAGEINSERTPROC>getFunction(b"glDebugMessageInsert")
    cglDebugMessageInsert(source, type, id, severity, length, buf)

cdef void GetglDispatchCompute(GLuint num_groups_x, GLuint num_groups_y, GLuint num_groups_z):
    global cglDispatchCompute
    cglDispatchCompute = <PFNGLDISPATCHCOMPUTEPROC>getFunction(b"glDispatchCompute")
    cglDispatchCompute(num_groups_x, num_groups_y, num_groups_z)

cdef void GetglDispatchComputeIndirect(GLintptr indirect):
    global cglDispatchComputeIndirect
    cglDispatchComputeIndirect = <PFNGLDISPATCHCOMPUTEINDIRECTPROC>getFunction(b"glDispatchComputeIndirect")
    cglDispatchComputeIndirect(indirect)

cdef void GetglFramebufferParameteri(GLenum target, GLenum pname, GLint param):
    global cglFramebufferParameteri
    cglFramebufferParameteri = <PFNGLFRAMEBUFFERPARAMETERIPROC>getFunction(b"glFramebufferParameteri")
    cglFramebufferParameteri(target, pname, param)

cdef GLuint GetglGetDebugMessageLog(GLuint count, GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids, GLenum *severities, GLsizei *lengths, GLchar *messageLog):
    global cglGetDebugMessageLog
    cglGetDebugMessageLog = <PFNGLGETDEBUGMESSAGELOGPROC>getFunction(b"glGetDebugMessageLog")
    cglGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog)

cdef void GetglGetFramebufferParameteriv(GLenum target, GLenum pname, GLint *params):
    global cglGetFramebufferParameteriv
    cglGetFramebufferParameteriv = <PFNGLGETFRAMEBUFFERPARAMETERIVPROC>getFunction(b"glGetFramebufferParameteriv")
    cglGetFramebufferParameteriv(target, pname, params)

cdef void GetglGetInternalformati64v(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint64 *params):
    global cglGetInternalformati64v
    cglGetInternalformati64v = <PFNGLGETINTERNALFORMATI64VPROC>getFunction(b"glGetInternalformati64v")
    cglGetInternalformati64v(target, internalformat, pname, count, params)

cdef void GetglGetObjectLabel(GLenum identifier, GLuint name, GLsizei bufSize, GLsizei *length, GLchar *label):
    global cglGetObjectLabel
    cglGetObjectLabel = <PFNGLGETOBJECTLABELPROC>getFunction(b"glGetObjectLabel")
    cglGetObjectLabel(identifier, name, bufSize, length, label)

cdef void GetglGetObjectPtrLabel(const void *ptr, GLsizei bufSize, GLsizei *length, GLchar *label):
    global cglGetObjectPtrLabel
    cglGetObjectPtrLabel = <PFNGLGETOBJECTPTRLABELPROC>getFunction(b"glGetObjectPtrLabel")
    cglGetObjectPtrLabel(ptr, bufSize, length, label)

cdef void GetglGetPointerv(GLenum pname, void **params):
    global cglGetPointerv
    cglGetPointerv = <PFNGLGETPOINTERVPROC>getFunction(b"glGetPointerv")
    cglGetPointerv(pname, params)

cdef void GetglGetProgramInterfaceiv(GLuint program, GLenum programInterface, GLenum pname, GLint *params):
    global cglGetProgramInterfaceiv
    cglGetProgramInterfaceiv = <PFNGLGETPROGRAMINTERFACEIVPROC>getFunction(b"glGetProgramInterfaceiv")
    cglGetProgramInterfaceiv(program, programInterface, pname, params)

cdef GLuint GetglGetProgramResourceIndex(GLuint program, GLenum programInterface, const GLchar *name):
    global cglGetProgramResourceIndex
    cglGetProgramResourceIndex = <PFNGLGETPROGRAMRESOURCEINDEXPROC>getFunction(b"glGetProgramResourceIndex")
    cglGetProgramResourceIndex(program, programInterface, name)

cdef GLint GetglGetProgramResourceLocation(GLuint program, GLenum programInterface, const GLchar *name):
    global cglGetProgramResourceLocation
    cglGetProgramResourceLocation = <PFNGLGETPROGRAMRESOURCELOCATIONPROC>getFunction(b"glGetProgramResourceLocation")
    cglGetProgramResourceLocation(program, programInterface, name)

cdef GLint GetglGetProgramResourceLocationIndex(GLuint program, GLenum programInterface, const GLchar *name):
    global cglGetProgramResourceLocationIndex
    cglGetProgramResourceLocationIndex = <PFNGLGETPROGRAMRESOURCELOCATIONINDEXPROC>getFunction(b"glGetProgramResourceLocationIndex")
    cglGetProgramResourceLocationIndex(program, programInterface, name)

cdef void GetglGetProgramResourceName(GLuint program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    global cglGetProgramResourceName
    cglGetProgramResourceName = <PFNGLGETPROGRAMRESOURCENAMEPROC>getFunction(b"glGetProgramResourceName")
    cglGetProgramResourceName(program, programInterface, index, bufSize, length, name)

cdef void GetglGetProgramResourceiv(GLuint program, GLenum programInterface, GLuint index, GLsizei propCount, const GLenum *props, GLsizei count, GLsizei *length, GLint *params):
    global cglGetProgramResourceiv
    cglGetProgramResourceiv = <PFNGLGETPROGRAMRESOURCEIVPROC>getFunction(b"glGetProgramResourceiv")
    cglGetProgramResourceiv(program, programInterface, index, propCount, props, count, length, params)

cdef void GetglInvalidateBufferData(GLuint buffer):
    global cglInvalidateBufferData
    cglInvalidateBufferData = <PFNGLINVALIDATEBUFFERDATAPROC>getFunction(b"glInvalidateBufferData")
    cglInvalidateBufferData(buffer)

cdef void GetglInvalidateBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr length):
    global cglInvalidateBufferSubData
    cglInvalidateBufferSubData = <PFNGLINVALIDATEBUFFERSUBDATAPROC>getFunction(b"glInvalidateBufferSubData")
    cglInvalidateBufferSubData(buffer, offset, length)

cdef void GetglInvalidateFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments):
    global cglInvalidateFramebuffer
    cglInvalidateFramebuffer = <PFNGLINVALIDATEFRAMEBUFFERPROC>getFunction(b"glInvalidateFramebuffer")
    cglInvalidateFramebuffer(target, numAttachments, attachments)

cdef void GetglInvalidateSubFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglInvalidateSubFramebuffer
    cglInvalidateSubFramebuffer = <PFNGLINVALIDATESUBFRAMEBUFFERPROC>getFunction(b"glInvalidateSubFramebuffer")
    cglInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height)

cdef void GetglInvalidateTexImage(GLuint texture, GLint level):
    global cglInvalidateTexImage
    cglInvalidateTexImage = <PFNGLINVALIDATETEXIMAGEPROC>getFunction(b"glInvalidateTexImage")
    cglInvalidateTexImage(texture, level)

cdef void GetglInvalidateTexSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth):
    global cglInvalidateTexSubImage
    cglInvalidateTexSubImage = <PFNGLINVALIDATETEXSUBIMAGEPROC>getFunction(b"glInvalidateTexSubImage")
    cglInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth)

cdef void GetglMultiDrawArraysIndirect(GLenum mode, const void *indirect, GLsizei drawcount, GLsizei stride):
    global cglMultiDrawArraysIndirect
    cglMultiDrawArraysIndirect = <PFNGLMULTIDRAWARRAYSINDIRECTPROC>getFunction(b"glMultiDrawArraysIndirect")
    cglMultiDrawArraysIndirect(mode, indirect, drawcount, stride)

cdef void GetglMultiDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei stride):
    global cglMultiDrawElementsIndirect
    cglMultiDrawElementsIndirect = <PFNGLMULTIDRAWELEMENTSINDIRECTPROC>getFunction(b"glMultiDrawElementsIndirect")
    cglMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride)

cdef void GetglObjectLabel(GLenum identifier, GLuint name, GLsizei length, const GLchar *label):
    global cglObjectLabel
    cglObjectLabel = <PFNGLOBJECTLABELPROC>getFunction(b"glObjectLabel")
    cglObjectLabel(identifier, name, length, label)

cdef void GetglObjectPtrLabel(const void *ptr, GLsizei length, const GLchar *label):
    global cglObjectPtrLabel
    cglObjectPtrLabel = <PFNGLOBJECTPTRLABELPROC>getFunction(b"glObjectPtrLabel")
    cglObjectPtrLabel(ptr, length, label)

cdef void GetglPopDebugGroup():
    global cglPopDebugGroup
    cglPopDebugGroup = <PFNGLPOPDEBUGGROUPPROC>getFunction(b"glPopDebugGroup")
    cglPopDebugGroup()

cdef void GetglPushDebugGroup(GLenum source, GLuint id, GLsizei length, const GLchar *message):
    global cglPushDebugGroup
    cglPushDebugGroup = <PFNGLPUSHDEBUGGROUPPROC>getFunction(b"glPushDebugGroup")
    cglPushDebugGroup(source, id, length, message)

cdef void GetglShaderStorageBlockBinding(GLuint program, GLuint storageBlockIndex, GLuint storageBlockBinding):
    global cglShaderStorageBlockBinding
    cglShaderStorageBlockBinding = <PFNGLSHADERSTORAGEBLOCKBINDINGPROC>getFunction(b"glShaderStorageBlockBinding")
    cglShaderStorageBlockBinding(program, storageBlockIndex, storageBlockBinding)

cdef void GetglTexBufferRange(GLenum target, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size):
    global cglTexBufferRange
    cglTexBufferRange = <PFNGLTEXBUFFERRANGEPROC>getFunction(b"glTexBufferRange")
    cglTexBufferRange(target, internalformat, buffer, offset, size)

cdef void GetglTexStorage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    global cglTexStorage2DMultisample
    cglTexStorage2DMultisample = <PFNGLTEXSTORAGE2DMULTISAMPLEPROC>getFunction(b"glTexStorage2DMultisample")
    cglTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

cdef void GetglTexStorage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    global cglTexStorage3DMultisample
    cglTexStorage3DMultisample = <PFNGLTEXSTORAGE3DMULTISAMPLEPROC>getFunction(b"glTexStorage3DMultisample")
    cglTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

cdef void GetglTextureView(GLuint texture, GLenum target, GLuint origtexture, GLenum internalformat, GLuint minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers):
    global cglTextureView
    cglTextureView = <PFNGLTEXTUREVIEWPROC>getFunction(b"glTextureView")
    cglTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers)

cdef void GetglVertexAttribBinding(GLuint attribindex, GLuint bindingindex):
    global cglVertexAttribBinding
    cglVertexAttribBinding = <PFNGLVERTEXATTRIBBINDINGPROC>getFunction(b"glVertexAttribBinding")
    cglVertexAttribBinding(attribindex, bindingindex)

cdef void GetglVertexAttribFormat(GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset):
    global cglVertexAttribFormat
    cglVertexAttribFormat = <PFNGLVERTEXATTRIBFORMATPROC>getFunction(b"glVertexAttribFormat")
    cglVertexAttribFormat(attribindex, size, type, normalized, relativeoffset)

cdef void GetglVertexAttribIFormat(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    global cglVertexAttribIFormat
    cglVertexAttribIFormat = <PFNGLVERTEXATTRIBIFORMATPROC>getFunction(b"glVertexAttribIFormat")
    cglVertexAttribIFormat(attribindex, size, type, relativeoffset)

cdef void GetglVertexAttribLFormat(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    global cglVertexAttribLFormat
    cglVertexAttribLFormat = <PFNGLVERTEXATTRIBLFORMATPROC>getFunction(b"glVertexAttribLFormat")
    cglVertexAttribLFormat(attribindex, size, type, relativeoffset)

cdef void GetglVertexBindingDivisor(GLuint bindingindex, GLuint divisor):
    global cglVertexBindingDivisor
    cglVertexBindingDivisor = <PFNGLVERTEXBINDINGDIVISORPROC>getFunction(b"glVertexBindingDivisor")
    cglVertexBindingDivisor(bindingindex, divisor)

cglBindVertexBuffer = GetglBindVertexBuffer
cglClearBufferData = GetglClearBufferData
cglClearBufferSubData = GetglClearBufferSubData
cglCopyImageSubData = GetglCopyImageSubData
cglDebugMessageCallback = GetglDebugMessageCallback
cglDebugMessageControl = GetglDebugMessageControl
cglDebugMessageInsert = GetglDebugMessageInsert
cglDispatchCompute = GetglDispatchCompute
cglDispatchComputeIndirect = GetglDispatchComputeIndirect
cglFramebufferParameteri = GetglFramebufferParameteri
cglGetDebugMessageLog = GetglGetDebugMessageLog
cglGetFramebufferParameteriv = GetglGetFramebufferParameteriv
cglGetInternalformati64v = GetglGetInternalformati64v
cglGetObjectLabel = GetglGetObjectLabel
cglGetObjectPtrLabel = GetglGetObjectPtrLabel
cglGetPointerv = GetglGetPointerv
cglGetProgramInterfaceiv = GetglGetProgramInterfaceiv
cglGetProgramResourceIndex = GetglGetProgramResourceIndex
cglGetProgramResourceLocation = GetglGetProgramResourceLocation
cglGetProgramResourceLocationIndex = GetglGetProgramResourceLocationIndex
cglGetProgramResourceName = GetglGetProgramResourceName
cglGetProgramResourceiv = GetglGetProgramResourceiv
cglInvalidateBufferData = GetglInvalidateBufferData
cglInvalidateBufferSubData = GetglInvalidateBufferSubData
cglInvalidateFramebuffer = GetglInvalidateFramebuffer
cglInvalidateSubFramebuffer = GetglInvalidateSubFramebuffer
cglInvalidateTexImage = GetglInvalidateTexImage
cglInvalidateTexSubImage = GetglInvalidateTexSubImage
cglMultiDrawArraysIndirect = GetglMultiDrawArraysIndirect
cglMultiDrawElementsIndirect = GetglMultiDrawElementsIndirect
cglObjectLabel = GetglObjectLabel
cglObjectPtrLabel = GetglObjectPtrLabel
cglPopDebugGroup = GetglPopDebugGroup
cglPushDebugGroup = GetglPushDebugGroup
cglShaderStorageBlockBinding = GetglShaderStorageBlockBinding
cglTexBufferRange = GetglTexBufferRange
cglTexStorage2DMultisample = GetglTexStorage2DMultisample
cglTexStorage3DMultisample = GetglTexStorage3DMultisample
cglTextureView = GetglTextureView
cglVertexAttribBinding = GetglVertexAttribBinding
cglVertexAttribFormat = GetglVertexAttribFormat
cglVertexAttribIFormat = GetglVertexAttribIFormat
cglVertexAttribLFormat = GetglVertexAttribLFormat
cglVertexBindingDivisor = GetglVertexBindingDivisor


cdef void glBindVertexBuffer(GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride):
    cglBindVertexBuffer(bindingindex, buffer, offset, stride)

cdef void glClearBufferData(GLenum target, GLenum internalformat, GLenum format, GLenum type, const void *data):
    cglClearBufferData(target, internalformat, format, type, data)

cdef void glClearBufferSubData(GLenum target, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data):
    cglClearBufferSubData(target, internalformat, offset, size, format, type, data)

cdef void glCopyImageSubData(GLuint srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei srcDepth):
    cglCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth)

cdef void glDebugMessageCallback(GLDEBUGPROC callback, const void *userParam):
    cglDebugMessageCallback(callback, userParam)

cdef void glDebugMessageControl(GLenum source, GLenum type, GLenum severity, GLsizei count, const GLuint *ids, GLboolean enabled):
    cglDebugMessageControl(source, type, severity, count, ids, enabled)

cdef void glDebugMessageInsert(GLenum source, GLenum type, GLuint id, GLenum severity, GLsizei length, const GLchar *buf):
    cglDebugMessageInsert(source, type, id, severity, length, buf)

cdef void glDispatchCompute(GLuint num_groups_x, GLuint num_groups_y, GLuint num_groups_z):
    cglDispatchCompute(num_groups_x, num_groups_y, num_groups_z)

cdef void glDispatchComputeIndirect(GLintptr indirect):
    cglDispatchComputeIndirect(indirect)

cdef void glFramebufferParameteri(GLenum target, GLenum pname, GLint param):
    cglFramebufferParameteri(target, pname, param)

cdef GLuint glGetDebugMessageLog(GLuint count, GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids, GLenum *severities, GLsizei *lengths, GLchar *messageLog):
    cglGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog)

cdef void glGetFramebufferParameteriv(GLenum target, GLenum pname, GLint *params):
    cglGetFramebufferParameteriv(target, pname, params)

cdef void glGetInternalformati64v(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint64 *params):
    cglGetInternalformati64v(target, internalformat, pname, count, params)

cdef void glGetObjectLabel(GLenum identifier, GLuint name, GLsizei bufSize, GLsizei *length, GLchar *label):
    cglGetObjectLabel(identifier, name, bufSize, length, label)

cdef void glGetObjectPtrLabel(const void *ptr, GLsizei bufSize, GLsizei *length, GLchar *label):
    cglGetObjectPtrLabel(ptr, bufSize, length, label)

cdef void glGetPointerv(GLenum pname, void **params):
    cglGetPointerv(pname, params)

cdef void glGetProgramInterfaceiv(GLuint program, GLenum programInterface, GLenum pname, GLint *params):
    cglGetProgramInterfaceiv(program, programInterface, pname, params)

cdef GLuint glGetProgramResourceIndex(GLuint program, GLenum programInterface, const GLchar *name):
    cglGetProgramResourceIndex(program, programInterface, name)

cdef GLint glGetProgramResourceLocation(GLuint program, GLenum programInterface, const GLchar *name):
    cglGetProgramResourceLocation(program, programInterface, name)

cdef GLint glGetProgramResourceLocationIndex(GLuint program, GLenum programInterface, const GLchar *name):
    cglGetProgramResourceLocationIndex(program, programInterface, name)

cdef void glGetProgramResourceName(GLuint program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    cglGetProgramResourceName(program, programInterface, index, bufSize, length, name)

cdef void glGetProgramResourceiv(GLuint program, GLenum programInterface, GLuint index, GLsizei propCount, const GLenum *props, GLsizei count, GLsizei *length, GLint *params):
    cglGetProgramResourceiv(program, programInterface, index, propCount, props, count, length, params)

cdef void glInvalidateBufferData(GLuint buffer):
    cglInvalidateBufferData(buffer)

cdef void glInvalidateBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr length):
    cglInvalidateBufferSubData(buffer, offset, length)

cdef void glInvalidateFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments):
    cglInvalidateFramebuffer(target, numAttachments, attachments)

cdef void glInvalidateSubFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height):
    cglInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height)

cdef void glInvalidateTexImage(GLuint texture, GLint level):
    cglInvalidateTexImage(texture, level)

cdef void glInvalidateTexSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth):
    cglInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth)

cdef void glMultiDrawArraysIndirect(GLenum mode, const void *indirect, GLsizei drawcount, GLsizei stride):
    cglMultiDrawArraysIndirect(mode, indirect, drawcount, stride)

cdef void glMultiDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei stride):
    cglMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride)

cdef void glObjectLabel(GLenum identifier, GLuint name, GLsizei length, const GLchar *label):
    cglObjectLabel(identifier, name, length, label)

cdef void glObjectPtrLabel(const void *ptr, GLsizei length, const GLchar *label):
    cglObjectPtrLabel(ptr, length, label)

cdef void glPopDebugGroup():
    cglPopDebugGroup()

cdef void glPushDebugGroup(GLenum source, GLuint id, GLsizei length, const GLchar *message):
    cglPushDebugGroup(source, id, length, message)

cdef void glShaderStorageBlockBinding(GLuint program, GLuint storageBlockIndex, GLuint storageBlockBinding):
    cglShaderStorageBlockBinding(program, storageBlockIndex, storageBlockBinding)

cdef void glTexBufferRange(GLenum target, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size):
    cglTexBufferRange(target, internalformat, buffer, offset, size)

cdef void glTexStorage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    cglTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

cdef void glTexStorage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    cglTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

cdef void glTextureView(GLuint texture, GLenum target, GLuint origtexture, GLenum internalformat, GLuint minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers):
    cglTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers)

cdef void glVertexAttribBinding(GLuint attribindex, GLuint bindingindex):
    cglVertexAttribBinding(attribindex, bindingindex)

cdef void glVertexAttribFormat(GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset):
    cglVertexAttribFormat(attribindex, size, type, normalized, relativeoffset)

cdef void glVertexAttribIFormat(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    cglVertexAttribIFormat(attribindex, size, type, relativeoffset)

cdef void glVertexAttribLFormat(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    cglVertexAttribLFormat(attribindex, size, type, relativeoffset)

cdef void glVertexBindingDivisor(GLuint bindingindex, GLuint divisor):
    cglVertexBindingDivisor(bindingindex, divisor)
