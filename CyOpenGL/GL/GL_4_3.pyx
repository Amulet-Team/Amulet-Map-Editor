# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_NUM_SHADING_LANGUAGE_VERSIONS = 0x82E9
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_LONG = 0x874E
cdef GLenum GL_COMPRESSED_RGB8_ETC2 = 0x9274
cdef GLenum GL_COMPRESSED_SRGB8_ETC2 = 0x9275
cdef GLenum GL_COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9276
cdef GLenum GL_COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9277
cdef GLenum GL_COMPRESSED_RGBA8_ETC2_EAC = 0x9278
cdef GLenum GL_COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 0x9279
cdef GLenum GL_COMPRESSED_R11_EAC = 0x9270
cdef GLenum GL_COMPRESSED_SIGNED_R11_EAC = 0x9271
cdef GLenum GL_COMPRESSED_RG11_EAC = 0x9272
cdef GLenum GL_COMPRESSED_SIGNED_RG11_EAC = 0x9273
cdef GLenum GL_PRIMITIVE_RESTART_FIXED_INDEX = 0x8D69
cdef GLenum GL_ANY_SAMPLES_PASSED_CONSERVATIVE = 0x8D6A
cdef GLenum GL_MAX_ELEMENT_INDEX = 0x8D6B
cdef GLenum GL_COMPUTE_SHADER = 0x91B9
cdef GLenum GL_MAX_COMPUTE_UNIFORM_BLOCKS = 0x91BB
cdef GLenum GL_MAX_COMPUTE_TEXTURE_IMAGE_UNITS = 0x91BC
cdef GLenum GL_MAX_COMPUTE_IMAGE_UNIFORMS = 0x91BD
cdef GLenum GL_MAX_COMPUTE_SHARED_MEMORY_SIZE = 0x8262
cdef GLenum GL_MAX_COMPUTE_UNIFORM_COMPONENTS = 0x8263
cdef GLenum GL_MAX_COMPUTE_ATOMIC_COUNTER_BUFFERS = 0x8264
cdef GLenum GL_MAX_COMPUTE_ATOMIC_COUNTERS = 0x8265
cdef GLenum GL_MAX_COMBINED_COMPUTE_UNIFORM_COMPONENTS = 0x8266
cdef GLenum GL_MAX_COMPUTE_WORK_GROUP_INVOCATIONS = 0x90EB
cdef GLenum GL_MAX_COMPUTE_WORK_GROUP_COUNT = 0x91BE
cdef GLenum GL_MAX_COMPUTE_WORK_GROUP_SIZE = 0x91BF
cdef GLenum GL_COMPUTE_WORK_GROUP_SIZE = 0x8267
cdef GLenum GL_UNIFORM_BLOCK_REFERENCED_BY_COMPUTE_SHADER = 0x90EC
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_REFERENCED_BY_COMPUTE_SHADER = 0x90ED
cdef GLenum GL_DISPATCH_INDIRECT_BUFFER = 0x90EE
cdef GLenum GL_DISPATCH_INDIRECT_BUFFER_BINDING = 0x90EF
cdef GLenum GL_COMPUTE_SHADER_BIT = 0x00000020
cdef GLenum GL_DEBUG_OUTPUT_SYNCHRONOUS = 0x8242
cdef GLenum GL_DEBUG_NEXT_LOGGED_MESSAGE_LENGTH = 0x8243
cdef GLenum GL_DEBUG_CALLBACK_FUNCTION = 0x8244
cdef GLenum GL_DEBUG_CALLBACK_USER_PARAM = 0x8245
cdef GLenum GL_DEBUG_SOURCE_API = 0x8246
cdef GLenum GL_DEBUG_SOURCE_WINDOW_SYSTEM = 0x8247
cdef GLenum GL_DEBUG_SOURCE_SHADER_COMPILER = 0x8248
cdef GLenum GL_DEBUG_SOURCE_THIRD_PARTY = 0x8249
cdef GLenum GL_DEBUG_SOURCE_APPLICATION = 0x824A
cdef GLenum GL_DEBUG_SOURCE_OTHER = 0x824B
cdef GLenum GL_DEBUG_TYPE_ERROR = 0x824C
cdef GLenum GL_DEBUG_TYPE_DEPRECATED_BEHAVIOR = 0x824D
cdef GLenum GL_DEBUG_TYPE_UNDEFINED_BEHAVIOR = 0x824E
cdef GLenum GL_DEBUG_TYPE_PORTABILITY = 0x824F
cdef GLenum GL_DEBUG_TYPE_PERFORMANCE = 0x8250
cdef GLenum GL_DEBUG_TYPE_OTHER = 0x8251
cdef GLenum GL_MAX_DEBUG_MESSAGE_LENGTH = 0x9143
cdef GLenum GL_MAX_DEBUG_LOGGED_MESSAGES = 0x9144
cdef GLenum GL_DEBUG_LOGGED_MESSAGES = 0x9145
cdef GLenum GL_DEBUG_SEVERITY_HIGH = 0x9146
cdef GLenum GL_DEBUG_SEVERITY_MEDIUM = 0x9147
cdef GLenum GL_DEBUG_SEVERITY_LOW = 0x9148
cdef GLenum GL_DEBUG_TYPE_MARKER = 0x8268
cdef GLenum GL_DEBUG_TYPE_PUSH_GROUP = 0x8269
cdef GLenum GL_DEBUG_TYPE_POP_GROUP = 0x826A
cdef GLenum GL_DEBUG_SEVERITY_NOTIFICATION = 0x826B
cdef GLenum GL_MAX_DEBUG_GROUP_STACK_DEPTH = 0x826C
cdef GLenum GL_DEBUG_GROUP_STACK_DEPTH = 0x826D
cdef GLenum GL_BUFFER = 0x82E0
cdef GLenum GL_SHADER = 0x82E1
cdef GLenum GL_PROGRAM = 0x82E2
cdef GLenum GL_VERTEX_ARRAY = 0x8074
cdef GLenum GL_QUERY = 0x82E3
cdef GLenum GL_PROGRAM_PIPELINE = 0x82E4
cdef GLenum GL_SAMPLER = 0x82E6
cdef GLenum GL_MAX_LABEL_LENGTH = 0x82E8
cdef GLenum GL_DEBUG_OUTPUT = 0x92E0
cdef GLenum GL_CONTEXT_FLAG_DEBUG_BIT = 0x00000002
cdef GLenum GL_MAX_UNIFORM_LOCATIONS = 0x826E
cdef GLenum GL_FRAMEBUFFER_DEFAULT_WIDTH = 0x9310
cdef GLenum GL_FRAMEBUFFER_DEFAULT_HEIGHT = 0x9311
cdef GLenum GL_FRAMEBUFFER_DEFAULT_LAYERS = 0x9312
cdef GLenum GL_FRAMEBUFFER_DEFAULT_SAMPLES = 0x9313
cdef GLenum GL_FRAMEBUFFER_DEFAULT_FIXED_SAMPLE_LOCATIONS = 0x9314
cdef GLenum GL_MAX_FRAMEBUFFER_WIDTH = 0x9315
cdef GLenum GL_MAX_FRAMEBUFFER_HEIGHT = 0x9316
cdef GLenum GL_MAX_FRAMEBUFFER_LAYERS = 0x9317
cdef GLenum GL_MAX_FRAMEBUFFER_SAMPLES = 0x9318
cdef GLenum GL_INTERNALFORMAT_SUPPORTED = 0x826F
cdef GLenum GL_INTERNALFORMAT_PREFERRED = 0x8270
cdef GLenum GL_INTERNALFORMAT_RED_SIZE = 0x8271
cdef GLenum GL_INTERNALFORMAT_GREEN_SIZE = 0x8272
cdef GLenum GL_INTERNALFORMAT_BLUE_SIZE = 0x8273
cdef GLenum GL_INTERNALFORMAT_ALPHA_SIZE = 0x8274
cdef GLenum GL_INTERNALFORMAT_DEPTH_SIZE = 0x8275
cdef GLenum GL_INTERNALFORMAT_STENCIL_SIZE = 0x8276
cdef GLenum GL_INTERNALFORMAT_SHARED_SIZE = 0x8277
cdef GLenum GL_INTERNALFORMAT_RED_TYPE = 0x8278
cdef GLenum GL_INTERNALFORMAT_GREEN_TYPE = 0x8279
cdef GLenum GL_INTERNALFORMAT_BLUE_TYPE = 0x827A
cdef GLenum GL_INTERNALFORMAT_ALPHA_TYPE = 0x827B
cdef GLenum GL_INTERNALFORMAT_DEPTH_TYPE = 0x827C
cdef GLenum GL_INTERNALFORMAT_STENCIL_TYPE = 0x827D
cdef GLenum GL_MAX_WIDTH = 0x827E
cdef GLenum GL_MAX_HEIGHT = 0x827F
cdef GLenum GL_MAX_DEPTH = 0x8280
cdef GLenum GL_MAX_LAYERS = 0x8281
cdef GLenum GL_MAX_COMBINED_DIMENSIONS = 0x8282
cdef GLenum GL_COLOR_COMPONENTS = 0x8283
cdef GLenum GL_DEPTH_COMPONENTS = 0x8284
cdef GLenum GL_STENCIL_COMPONENTS = 0x8285
cdef GLenum GL_COLOR_RENDERABLE = 0x8286
cdef GLenum GL_DEPTH_RENDERABLE = 0x8287
cdef GLenum GL_STENCIL_RENDERABLE = 0x8288
cdef GLenum GL_FRAMEBUFFER_RENDERABLE = 0x8289
cdef GLenum GL_FRAMEBUFFER_RENDERABLE_LAYERED = 0x828A
cdef GLenum GL_FRAMEBUFFER_BLEND = 0x828B
cdef GLenum GL_READ_PIXELS = 0x828C
cdef GLenum GL_READ_PIXELS_FORMAT = 0x828D
cdef GLenum GL_READ_PIXELS_TYPE = 0x828E
cdef GLenum GL_TEXTURE_IMAGE_FORMAT = 0x828F
cdef GLenum GL_TEXTURE_IMAGE_TYPE = 0x8290
cdef GLenum GL_GET_TEXTURE_IMAGE_FORMAT = 0x8291
cdef GLenum GL_GET_TEXTURE_IMAGE_TYPE = 0x8292
cdef GLenum GL_MIPMAP = 0x8293
cdef GLenum GL_MANUAL_GENERATE_MIPMAP = 0x8294
cdef GLenum GL_AUTO_GENERATE_MIPMAP = 0x8295
cdef GLenum GL_COLOR_ENCODING = 0x8296
cdef GLenum GL_SRGB_READ = 0x8297
cdef GLenum GL_SRGB_WRITE = 0x8298
cdef GLenum GL_FILTER = 0x829A
cdef GLenum GL_VERTEX_TEXTURE = 0x829B
cdef GLenum GL_TESS_CONTROL_TEXTURE = 0x829C
cdef GLenum GL_TESS_EVALUATION_TEXTURE = 0x829D
cdef GLenum GL_GEOMETRY_TEXTURE = 0x829E
cdef GLenum GL_FRAGMENT_TEXTURE = 0x829F
cdef GLenum GL_COMPUTE_TEXTURE = 0x82A0
cdef GLenum GL_TEXTURE_SHADOW = 0x82A1
cdef GLenum GL_TEXTURE_GATHER = 0x82A2
cdef GLenum GL_TEXTURE_GATHER_SHADOW = 0x82A3
cdef GLenum GL_SHADER_IMAGE_LOAD = 0x82A4
cdef GLenum GL_SHADER_IMAGE_STORE = 0x82A5
cdef GLenum GL_SHADER_IMAGE_ATOMIC = 0x82A6
cdef GLenum GL_IMAGE_TEXEL_SIZE = 0x82A7
cdef GLenum GL_IMAGE_COMPATIBILITY_CLASS = 0x82A8
cdef GLenum GL_IMAGE_PIXEL_FORMAT = 0x82A9
cdef GLenum GL_IMAGE_PIXEL_TYPE = 0x82AA
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_TEST = 0x82AC
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_TEST = 0x82AD
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_DEPTH_WRITE = 0x82AE
cdef GLenum GL_SIMULTANEOUS_TEXTURE_AND_STENCIL_WRITE = 0x82AF
cdef GLenum GL_TEXTURE_COMPRESSED_BLOCK_WIDTH = 0x82B1
cdef GLenum GL_TEXTURE_COMPRESSED_BLOCK_HEIGHT = 0x82B2
cdef GLenum GL_TEXTURE_COMPRESSED_BLOCK_SIZE = 0x82B3
cdef GLenum GL_CLEAR_BUFFER = 0x82B4
cdef GLenum GL_TEXTURE_VIEW = 0x82B5
cdef GLenum GL_VIEW_COMPATIBILITY_CLASS = 0x82B6
cdef GLenum GL_FULL_SUPPORT = 0x82B7
cdef GLenum GL_CAVEAT_SUPPORT = 0x82B8
cdef GLenum GL_IMAGE_CLASS_4_X_32 = 0x82B9
cdef GLenum GL_IMAGE_CLASS_2_X_32 = 0x82BA
cdef GLenum GL_IMAGE_CLASS_1_X_32 = 0x82BB
cdef GLenum GL_IMAGE_CLASS_4_X_16 = 0x82BC
cdef GLenum GL_IMAGE_CLASS_2_X_16 = 0x82BD
cdef GLenum GL_IMAGE_CLASS_1_X_16 = 0x82BE
cdef GLenum GL_IMAGE_CLASS_4_X_8 = 0x82BF
cdef GLenum GL_IMAGE_CLASS_2_X_8 = 0x82C0
cdef GLenum GL_IMAGE_CLASS_1_X_8 = 0x82C1
cdef GLenum GL_IMAGE_CLASS_11_11_10 = 0x82C2
cdef GLenum GL_IMAGE_CLASS_10_10_10_2 = 0x82C3
cdef GLenum GL_VIEW_CLASS_128_BITS = 0x82C4
cdef GLenum GL_VIEW_CLASS_96_BITS = 0x82C5
cdef GLenum GL_VIEW_CLASS_64_BITS = 0x82C6
cdef GLenum GL_VIEW_CLASS_48_BITS = 0x82C7
cdef GLenum GL_VIEW_CLASS_32_BITS = 0x82C8
cdef GLenum GL_VIEW_CLASS_24_BITS = 0x82C9
cdef GLenum GL_VIEW_CLASS_16_BITS = 0x82CA
cdef GLenum GL_VIEW_CLASS_8_BITS = 0x82CB
cdef GLenum GL_VIEW_CLASS_S3TC_DXT1_RGB = 0x82CC
cdef GLenum GL_VIEW_CLASS_S3TC_DXT1_RGBA = 0x82CD
cdef GLenum GL_VIEW_CLASS_S3TC_DXT3_RGBA = 0x82CE
cdef GLenum GL_VIEW_CLASS_S3TC_DXT5_RGBA = 0x82CF
cdef GLenum GL_VIEW_CLASS_RGTC1_RED = 0x82D0
cdef GLenum GL_VIEW_CLASS_RGTC2_RG = 0x82D1
cdef GLenum GL_VIEW_CLASS_BPTC_UNORM = 0x82D2
cdef GLenum GL_VIEW_CLASS_BPTC_FLOAT = 0x82D3
cdef GLenum GL_UNIFORM = 0x92E1
cdef GLenum GL_UNIFORM_BLOCK = 0x92E2
cdef GLenum GL_PROGRAM_INPUT = 0x92E3
cdef GLenum GL_PROGRAM_OUTPUT = 0x92E4
cdef GLenum GL_BUFFER_VARIABLE = 0x92E5
cdef GLenum GL_SHADER_STORAGE_BLOCK = 0x92E6
cdef GLenum GL_VERTEX_SUBROUTINE = 0x92E8
cdef GLenum GL_TESS_CONTROL_SUBROUTINE = 0x92E9
cdef GLenum GL_TESS_EVALUATION_SUBROUTINE = 0x92EA
cdef GLenum GL_GEOMETRY_SUBROUTINE = 0x92EB
cdef GLenum GL_FRAGMENT_SUBROUTINE = 0x92EC
cdef GLenum GL_COMPUTE_SUBROUTINE = 0x92ED
cdef GLenum GL_VERTEX_SUBROUTINE_UNIFORM = 0x92EE
cdef GLenum GL_TESS_CONTROL_SUBROUTINE_UNIFORM = 0x92EF
cdef GLenum GL_TESS_EVALUATION_SUBROUTINE_UNIFORM = 0x92F0
cdef GLenum GL_GEOMETRY_SUBROUTINE_UNIFORM = 0x92F1
cdef GLenum GL_FRAGMENT_SUBROUTINE_UNIFORM = 0x92F2
cdef GLenum GL_COMPUTE_SUBROUTINE_UNIFORM = 0x92F3
cdef GLenum GL_TRANSFORM_FEEDBACK_VARYING = 0x92F4
cdef GLenum GL_ACTIVE_RESOURCES = 0x92F5
cdef GLenum GL_MAX_NAME_LENGTH = 0x92F6
cdef GLenum GL_MAX_NUM_ACTIVE_VARIABLES = 0x92F7
cdef GLenum GL_MAX_NUM_COMPATIBLE_SUBROUTINES = 0x92F8
cdef GLenum GL_NAME_LENGTH = 0x92F9
cdef GLenum GL_TYPE = 0x92FA
cdef GLenum GL_ARRAY_SIZE = 0x92FB
cdef GLenum GL_OFFSET = 0x92FC
cdef GLenum GL_BLOCK_INDEX = 0x92FD
cdef GLenum GL_ARRAY_STRIDE = 0x92FE
cdef GLenum GL_MATRIX_STRIDE = 0x92FF
cdef GLenum GL_IS_ROW_MAJOR = 0x9300
cdef GLenum GL_ATOMIC_COUNTER_BUFFER_INDEX = 0x9301
cdef GLenum GL_BUFFER_BINDING = 0x9302
cdef GLenum GL_BUFFER_DATA_SIZE = 0x9303
cdef GLenum GL_NUM_ACTIVE_VARIABLES = 0x9304
cdef GLenum GL_ACTIVE_VARIABLES = 0x9305
cdef GLenum GL_REFERENCED_BY_VERTEX_SHADER = 0x9306
cdef GLenum GL_REFERENCED_BY_TESS_CONTROL_SHADER = 0x9307
cdef GLenum GL_REFERENCED_BY_TESS_EVALUATION_SHADER = 0x9308
cdef GLenum GL_REFERENCED_BY_GEOMETRY_SHADER = 0x9309
cdef GLenum GL_REFERENCED_BY_FRAGMENT_SHADER = 0x930A
cdef GLenum GL_REFERENCED_BY_COMPUTE_SHADER = 0x930B
cdef GLenum GL_TOP_LEVEL_ARRAY_SIZE = 0x930C
cdef GLenum GL_TOP_LEVEL_ARRAY_STRIDE = 0x930D
cdef GLenum GL_LOCATION = 0x930E
cdef GLenum GL_LOCATION_INDEX = 0x930F
cdef GLenum GL_IS_PER_PATCH = 0x92E7
cdef GLenum GL_SHADER_STORAGE_BUFFER = 0x90D2
cdef GLenum GL_SHADER_STORAGE_BUFFER_BINDING = 0x90D3
cdef GLenum GL_SHADER_STORAGE_BUFFER_START = 0x90D4
cdef GLenum GL_SHADER_STORAGE_BUFFER_SIZE = 0x90D5
cdef GLenum GL_MAX_VERTEX_SHADER_STORAGE_BLOCKS = 0x90D6
cdef GLenum GL_MAX_GEOMETRY_SHADER_STORAGE_BLOCKS = 0x90D7
cdef GLenum GL_MAX_TESS_CONTROL_SHADER_STORAGE_BLOCKS = 0x90D8
cdef GLenum GL_MAX_TESS_EVALUATION_SHADER_STORAGE_BLOCKS = 0x90D9
cdef GLenum GL_MAX_FRAGMENT_SHADER_STORAGE_BLOCKS = 0x90DA
cdef GLenum GL_MAX_COMPUTE_SHADER_STORAGE_BLOCKS = 0x90DB
cdef GLenum GL_MAX_COMBINED_SHADER_STORAGE_BLOCKS = 0x90DC
cdef GLenum GL_MAX_SHADER_STORAGE_BUFFER_BINDINGS = 0x90DD
cdef GLenum GL_MAX_SHADER_STORAGE_BLOCK_SIZE = 0x90DE
cdef GLenum GL_SHADER_STORAGE_BUFFER_OFFSET_ALIGNMENT = 0x90DF
cdef GLenum GL_SHADER_STORAGE_BARRIER_BIT = 0x00002000
cdef GLenum GL_MAX_COMBINED_SHADER_OUTPUT_RESOURCES = 0x8F39
cdef GLenum GL_DEPTH_STENCIL_TEXTURE_MODE = 0x90EA
cdef GLenum GL_TEXTURE_BUFFER_OFFSET = 0x919D
cdef GLenum GL_TEXTURE_BUFFER_SIZE = 0x919E
cdef GLenum GL_TEXTURE_BUFFER_OFFSET_ALIGNMENT = 0x919F
cdef GLenum GL_TEXTURE_VIEW_MIN_LEVEL = 0x82DB
cdef GLenum GL_TEXTURE_VIEW_NUM_LEVELS = 0x82DC
cdef GLenum GL_TEXTURE_VIEW_MIN_LAYER = 0x82DD
cdef GLenum GL_TEXTURE_VIEW_NUM_LAYERS = 0x82DE
cdef GLenum GL_TEXTURE_IMMUTABLE_LEVELS = 0x82DF
cdef GLenum GL_VERTEX_ATTRIB_BINDING = 0x82D4
cdef GLenum GL_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D5
cdef GLenum GL_VERTEX_BINDING_DIVISOR = 0x82D6
cdef GLenum GL_VERTEX_BINDING_OFFSET = 0x82D7
cdef GLenum GL_VERTEX_BINDING_STRIDE = 0x82D8
cdef GLenum GL_MAX_VERTEX_ATTRIB_RELATIVE_OFFSET = 0x82D9
cdef GLenum GL_MAX_VERTEX_ATTRIB_BINDINGS = 0x82DA
cdef GLenum GL_VERTEX_BINDING_BUFFER = 0x8F4F
cdef GLenum GL_DISPLAY_LIST = 0x82E7
cdef GLenum GL_STACK_UNDERFLOW = 0x0504
cdef GLenum GL_STACK_OVERFLOW = 0x0503

ctypedef void (*GL_CLEAR_BUFFER_DATA)(GLenum target, GLenum internalformat, GLenum format, GLenum type, const void *data)
ctypedef void (*GL_CLEAR_BUFFER_SUB_DATA)(GLenum target, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data)
ctypedef void (*GL_DISPATCH_COMPUTE)(GLuint num_groups_x, GLuint num_groups_y, GLuint num_groups_z)
ctypedef void (*GL_DISPATCH_COMPUTE_INDIRECT)(GLintptr indirect)
ctypedef void (*GL_COPY_IMAGE_SUB_DATA)(GLuint srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei srcDepth)
ctypedef void (*GL_FRAMEBUFFER_PARAMETERI)(GLenum target, GLenum pname, GLint param)
ctypedef void (*GL_GET_FRAMEBUFFER_PARAMETERIV)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*GL_GET_INTERNALFORMATI64V)(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint64 *params)
ctypedef void (*GL_INVALIDATE_TEX_SUB_IMAGE)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth)
ctypedef void (*GL_INVALIDATE_TEX_IMAGE)(GLuint texture, GLint level)
ctypedef void (*GL_INVALIDATE_BUFFER_SUB_DATA)(GLuint buffer, GLintptr offset, GLsizeiptr length)
ctypedef void (*GL_INVALIDATE_BUFFER_DATA)(GLuint buffer)
ctypedef void (*GL_INVALIDATE_FRAMEBUFFER)(GLenum target, GLsizei numAttachments, const GLenum *attachments)
ctypedef void (*GL_INVALIDATE_SUB_FRAMEBUFFER)(GLenum target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*GL_MULTI_DRAW_ARRAYS_INDIRECT)(GLenum mode, const void *indirect, GLsizei drawcount, GLsizei stride)
ctypedef void (*GL_MULTI_DRAW_ELEMENTS_INDIRECT)(GLenum mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei stride)
ctypedef void (*GL_GET_PROGRAM_INTERFACEIV)(GLuint program, GLenum programInterface, GLenum pname, GLint *params)
ctypedef GLuint (*GL_GET_PROGRAM_RESOURCE_INDEX)(GLuint program, GLenum programInterface, const GLchar *name)
ctypedef void (*GL_GET_PROGRAM_RESOURCE_NAME)(GLuint program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name)
ctypedef void (*GL_GET_PROGRAM_RESOURCEIV)(GLuint program, GLenum programInterface, GLuint index, GLsizei propCount, const GLenum *props, GLsizei count, GLsizei *length, GLint *params)
ctypedef GLint (*GL_GET_PROGRAM_RESOURCE_LOCATION)(GLuint program, GLenum programInterface, const GLchar *name)
ctypedef GLint (*GL_GET_PROGRAM_RESOURCE_LOCATION_INDEX)(GLuint program, GLenum programInterface, const GLchar *name)
ctypedef void (*GL_SHADER_STORAGE_BLOCK_BINDING)(GLuint program, GLuint storageBlockIndex, GLuint storageBlockBinding)
ctypedef void (*GL_TEX_BUFFER_RANGE)(GLenum target, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size)
ctypedef void (*GL_TEX_STORAGE2D_MULTISAMPLE)(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
ctypedef void (*GL_TEX_STORAGE3D_MULTISAMPLE)(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
ctypedef void (*GL_TEXTURE_VIEW)(GLuint texture, GLenum target, GLuint origtexture, GLenum internalformat, GLuint minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers)
ctypedef void (*GL_BIND_VERTEX_BUFFER)(GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)
ctypedef void (*GL_VERTEX_ATTRIB_FORMAT)(GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset)
ctypedef void (*GL_VERTEX_ATTRIB_I_FORMAT)(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
ctypedef void (*GL_VERTEX_ATTRIB_L_FORMAT)(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
ctypedef void (*GL_VERTEX_ATTRIB_BINDING)(GLuint attribindex, GLuint bindingindex)
ctypedef void (*GL_VERTEX_BINDING_DIVISOR)(GLuint bindingindex, GLuint divisor)
ctypedef void (*GL_DEBUG_MESSAGE_CONTROL)(GLenum source, GLenum type, GLenum severity, GLsizei count, const GLuint *ids, GLboolean enabled)
ctypedef void (*GL_DEBUG_MESSAGE_INSERT)(GLenum source, GLenum type, GLuint id, GLenum severity, GLsizei length, const GLchar *buf)
ctypedef void (*GL_DEBUG_MESSAGE_CALLBACK)(GLDEBUGPROC callback, const void *userParam)
ctypedef GLuint (*GL_GET_DEBUG_MESSAGE_LOG)(GLuint count, GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids, GLenum *severities, GLsizei *lengths, GLchar *messageLog)
ctypedef void (*GL_PUSH_DEBUG_GROUP)(GLenum source, GLuint id, GLsizei length, const GLchar *message)
ctypedef void (*GL_POP_DEBUG_GROUP)()
ctypedef void (*GL_OBJECT_LABEL)(GLenum identifier, GLuint name, GLsizei length, const GLchar *label)
ctypedef void (*GL_GET_OBJECT_LABEL)(GLenum identifier, GLuint name, GLsizei bufSize, GLsizei *length, GLchar *label)
ctypedef void (*GL_OBJECT_PTR_LABEL)(const void *ptr, GLsizei length, const GLchar *label)
ctypedef void (*GL_GET_OBJECT_PTR_LABEL)(const void *ptr, GLsizei bufSize, GLsizei *length, GLchar *label)
ctypedef void (*GL_GET_POINTERV)(GLenum pname, void **params)

cdef GL_CLEAR_BUFFER_DATA cglClearBufferData = NULL
cdef GL_CLEAR_BUFFER_SUB_DATA cglClearBufferSubData = NULL
cdef GL_DISPATCH_COMPUTE cglDispatchCompute = NULL
cdef GL_DISPATCH_COMPUTE_INDIRECT cglDispatchComputeIndirect = NULL
cdef GL_COPY_IMAGE_SUB_DATA cglCopyImageSubData = NULL
cdef GL_FRAMEBUFFER_PARAMETERI cglFramebufferParameteri = NULL
cdef GL_GET_FRAMEBUFFER_PARAMETERIV cglGetFramebufferParameteriv = NULL
cdef GL_GET_INTERNALFORMATI64V cglGetInternalformati64v = NULL
cdef GL_INVALIDATE_TEX_SUB_IMAGE cglInvalidateTexSubImage = NULL
cdef GL_INVALIDATE_TEX_IMAGE cglInvalidateTexImage = NULL
cdef GL_INVALIDATE_BUFFER_SUB_DATA cglInvalidateBufferSubData = NULL
cdef GL_INVALIDATE_BUFFER_DATA cglInvalidateBufferData = NULL
cdef GL_INVALIDATE_FRAMEBUFFER cglInvalidateFramebuffer = NULL
cdef GL_INVALIDATE_SUB_FRAMEBUFFER cglInvalidateSubFramebuffer = NULL
cdef GL_MULTI_DRAW_ARRAYS_INDIRECT cglMultiDrawArraysIndirect = NULL
cdef GL_MULTI_DRAW_ELEMENTS_INDIRECT cglMultiDrawElementsIndirect = NULL
cdef GL_GET_PROGRAM_INTERFACEIV cglGetProgramInterfaceiv = NULL
cdef GL_GET_PROGRAM_RESOURCE_INDEX cglGetProgramResourceIndex = NULL
cdef GL_GET_PROGRAM_RESOURCE_NAME cglGetProgramResourceName = NULL
cdef GL_GET_PROGRAM_RESOURCEIV cglGetProgramResourceiv = NULL
cdef GL_GET_PROGRAM_RESOURCE_LOCATION cglGetProgramResourceLocation = NULL
cdef GL_GET_PROGRAM_RESOURCE_LOCATION_INDEX cglGetProgramResourceLocationIndex = NULL
cdef GL_SHADER_STORAGE_BLOCK_BINDING cglShaderStorageBlockBinding = NULL
cdef GL_TEX_BUFFER_RANGE cglTexBufferRange = NULL
cdef GL_TEX_STORAGE2D_MULTISAMPLE cglTexStorage2DMultisample = NULL
cdef GL_TEX_STORAGE3D_MULTISAMPLE cglTexStorage3DMultisample = NULL
cdef GL_TEXTURE_VIEW cglTextureView = NULL
cdef GL_BIND_VERTEX_BUFFER cglBindVertexBuffer = NULL
cdef GL_VERTEX_ATTRIB_FORMAT cglVertexAttribFormat = NULL
cdef GL_VERTEX_ATTRIB_I_FORMAT cglVertexAttribIFormat = NULL
cdef GL_VERTEX_ATTRIB_L_FORMAT cglVertexAttribLFormat = NULL
cdef GL_VERTEX_ATTRIB_BINDING cglVertexAttribBinding = NULL
cdef GL_VERTEX_BINDING_DIVISOR cglVertexBindingDivisor = NULL
cdef GL_DEBUG_MESSAGE_CONTROL cglDebugMessageControl = NULL
cdef GL_DEBUG_MESSAGE_INSERT cglDebugMessageInsert = NULL
cdef GL_DEBUG_MESSAGE_CALLBACK cglDebugMessageCallback = NULL
cdef GL_GET_DEBUG_MESSAGE_LOG cglGetDebugMessageLog = NULL
cdef GL_PUSH_DEBUG_GROUP cglPushDebugGroup = NULL
cdef GL_POP_DEBUG_GROUP cglPopDebugGroup = NULL
cdef GL_OBJECT_LABEL cglObjectLabel = NULL
cdef GL_GET_OBJECT_LABEL cglGetObjectLabel = NULL
cdef GL_OBJECT_PTR_LABEL cglObjectPtrLabel = NULL
cdef GL_GET_OBJECT_PTR_LABEL cglGetObjectPtrLabel = NULL
cdef GL_GET_POINTERV cglGetPointerv = NULL


cdef void GetglClearBufferData(GLenum target, GLenum internalformat, GLenum format, GLenum type, const void *data):
    global cglClearBufferData
    cglClearBufferData = <GL_CLEAR_BUFFER_DATA>getFunction(b"glClearBufferData")
    cglClearBufferData(target, internalformat, format, type, data)

cdef void GetglClearBufferSubData(GLenum target, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data):
    global cglClearBufferSubData
    cglClearBufferSubData = <GL_CLEAR_BUFFER_SUB_DATA>getFunction(b"glClearBufferSubData")
    cglClearBufferSubData(target, internalformat, offset, size, format, type, data)

cdef void GetglDispatchCompute(GLuint num_groups_x, GLuint num_groups_y, GLuint num_groups_z):
    global cglDispatchCompute
    cglDispatchCompute = <GL_DISPATCH_COMPUTE>getFunction(b"glDispatchCompute")
    cglDispatchCompute(num_groups_x, num_groups_y, num_groups_z)

cdef void GetglDispatchComputeIndirect(GLintptr indirect):
    global cglDispatchComputeIndirect
    cglDispatchComputeIndirect = <GL_DISPATCH_COMPUTE_INDIRECT>getFunction(b"glDispatchComputeIndirect")
    cglDispatchComputeIndirect(indirect)

cdef void GetglCopyImageSubData(GLuint srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei srcDepth):
    global cglCopyImageSubData
    cglCopyImageSubData = <GL_COPY_IMAGE_SUB_DATA>getFunction(b"glCopyImageSubData")
    cglCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth)

cdef void GetglFramebufferParameteri(GLenum target, GLenum pname, GLint param):
    global cglFramebufferParameteri
    cglFramebufferParameteri = <GL_FRAMEBUFFER_PARAMETERI>getFunction(b"glFramebufferParameteri")
    cglFramebufferParameteri(target, pname, param)

cdef void GetglGetFramebufferParameteriv(GLenum target, GLenum pname, GLint *params):
    global cglGetFramebufferParameteriv
    cglGetFramebufferParameteriv = <GL_GET_FRAMEBUFFER_PARAMETERIV>getFunction(b"glGetFramebufferParameteriv")
    cglGetFramebufferParameteriv(target, pname, params)

cdef void GetglGetInternalformati64v(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint64 *params):
    global cglGetInternalformati64v
    cglGetInternalformati64v = <GL_GET_INTERNALFORMATI64V>getFunction(b"glGetInternalformati64v")
    cglGetInternalformati64v(target, internalformat, pname, count, params)

cdef void GetglInvalidateTexSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth):
    global cglInvalidateTexSubImage
    cglInvalidateTexSubImage = <GL_INVALIDATE_TEX_SUB_IMAGE>getFunction(b"glInvalidateTexSubImage")
    cglInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth)

cdef void GetglInvalidateTexImage(GLuint texture, GLint level):
    global cglInvalidateTexImage
    cglInvalidateTexImage = <GL_INVALIDATE_TEX_IMAGE>getFunction(b"glInvalidateTexImage")
    cglInvalidateTexImage(texture, level)

cdef void GetglInvalidateBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr length):
    global cglInvalidateBufferSubData
    cglInvalidateBufferSubData = <GL_INVALIDATE_BUFFER_SUB_DATA>getFunction(b"glInvalidateBufferSubData")
    cglInvalidateBufferSubData(buffer, offset, length)

cdef void GetglInvalidateBufferData(GLuint buffer):
    global cglInvalidateBufferData
    cglInvalidateBufferData = <GL_INVALIDATE_BUFFER_DATA>getFunction(b"glInvalidateBufferData")
    cglInvalidateBufferData(buffer)

cdef void GetglInvalidateFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments):
    global cglInvalidateFramebuffer
    cglInvalidateFramebuffer = <GL_INVALIDATE_FRAMEBUFFER>getFunction(b"glInvalidateFramebuffer")
    cglInvalidateFramebuffer(target, numAttachments, attachments)

cdef void GetglInvalidateSubFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglInvalidateSubFramebuffer
    cglInvalidateSubFramebuffer = <GL_INVALIDATE_SUB_FRAMEBUFFER>getFunction(b"glInvalidateSubFramebuffer")
    cglInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height)

cdef void GetglMultiDrawArraysIndirect(GLenum mode, const void *indirect, GLsizei drawcount, GLsizei stride):
    global cglMultiDrawArraysIndirect
    cglMultiDrawArraysIndirect = <GL_MULTI_DRAW_ARRAYS_INDIRECT>getFunction(b"glMultiDrawArraysIndirect")
    cglMultiDrawArraysIndirect(mode, indirect, drawcount, stride)

cdef void GetglMultiDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei stride):
    global cglMultiDrawElementsIndirect
    cglMultiDrawElementsIndirect = <GL_MULTI_DRAW_ELEMENTS_INDIRECT>getFunction(b"glMultiDrawElementsIndirect")
    cglMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride)

cdef void GetglGetProgramInterfaceiv(GLuint program, GLenum programInterface, GLenum pname, GLint *params):
    global cglGetProgramInterfaceiv
    cglGetProgramInterfaceiv = <GL_GET_PROGRAM_INTERFACEIV>getFunction(b"glGetProgramInterfaceiv")
    cglGetProgramInterfaceiv(program, programInterface, pname, params)

cdef GLuint GetglGetProgramResourceIndex(GLuint program, GLenum programInterface, const GLchar *name):
    global cglGetProgramResourceIndex
    cglGetProgramResourceIndex = <GL_GET_PROGRAM_RESOURCE_INDEX>getFunction(b"glGetProgramResourceIndex")
    cglGetProgramResourceIndex(program, programInterface, name)

cdef void GetglGetProgramResourceName(GLuint program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    global cglGetProgramResourceName
    cglGetProgramResourceName = <GL_GET_PROGRAM_RESOURCE_NAME>getFunction(b"glGetProgramResourceName")
    cglGetProgramResourceName(program, programInterface, index, bufSize, length, name)

cdef void GetglGetProgramResourceiv(GLuint program, GLenum programInterface, GLuint index, GLsizei propCount, const GLenum *props, GLsizei count, GLsizei *length, GLint *params):
    global cglGetProgramResourceiv
    cglGetProgramResourceiv = <GL_GET_PROGRAM_RESOURCEIV>getFunction(b"glGetProgramResourceiv")
    cglGetProgramResourceiv(program, programInterface, index, propCount, props, count, length, params)

cdef GLint GetglGetProgramResourceLocation(GLuint program, GLenum programInterface, const GLchar *name):
    global cglGetProgramResourceLocation
    cglGetProgramResourceLocation = <GL_GET_PROGRAM_RESOURCE_LOCATION>getFunction(b"glGetProgramResourceLocation")
    cglGetProgramResourceLocation(program, programInterface, name)

cdef GLint GetglGetProgramResourceLocationIndex(GLuint program, GLenum programInterface, const GLchar *name):
    global cglGetProgramResourceLocationIndex
    cglGetProgramResourceLocationIndex = <GL_GET_PROGRAM_RESOURCE_LOCATION_INDEX>getFunction(b"glGetProgramResourceLocationIndex")
    cglGetProgramResourceLocationIndex(program, programInterface, name)

cdef void GetglShaderStorageBlockBinding(GLuint program, GLuint storageBlockIndex, GLuint storageBlockBinding):
    global cglShaderStorageBlockBinding
    cglShaderStorageBlockBinding = <GL_SHADER_STORAGE_BLOCK_BINDING>getFunction(b"glShaderStorageBlockBinding")
    cglShaderStorageBlockBinding(program, storageBlockIndex, storageBlockBinding)

cdef void GetglTexBufferRange(GLenum target, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size):
    global cglTexBufferRange
    cglTexBufferRange = <GL_TEX_BUFFER_RANGE>getFunction(b"glTexBufferRange")
    cglTexBufferRange(target, internalformat, buffer, offset, size)

cdef void GetglTexStorage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    global cglTexStorage2DMultisample
    cglTexStorage2DMultisample = <GL_TEX_STORAGE2D_MULTISAMPLE>getFunction(b"glTexStorage2DMultisample")
    cglTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

cdef void GetglTexStorage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    global cglTexStorage3DMultisample
    cglTexStorage3DMultisample = <GL_TEX_STORAGE3D_MULTISAMPLE>getFunction(b"glTexStorage3DMultisample")
    cglTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

cdef void GetglTextureView(GLuint texture, GLenum target, GLuint origtexture, GLenum internalformat, GLuint minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers):
    global cglTextureView
    cglTextureView = <GL_TEXTURE_VIEW>getFunction(b"glTextureView")
    cglTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers)

cdef void GetglBindVertexBuffer(GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride):
    global cglBindVertexBuffer
    cglBindVertexBuffer = <GL_BIND_VERTEX_BUFFER>getFunction(b"glBindVertexBuffer")
    cglBindVertexBuffer(bindingindex, buffer, offset, stride)

cdef void GetglVertexAttribFormat(GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset):
    global cglVertexAttribFormat
    cglVertexAttribFormat = <GL_VERTEX_ATTRIB_FORMAT>getFunction(b"glVertexAttribFormat")
    cglVertexAttribFormat(attribindex, size, type, normalized, relativeoffset)

cdef void GetglVertexAttribIFormat(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    global cglVertexAttribIFormat
    cglVertexAttribIFormat = <GL_VERTEX_ATTRIB_I_FORMAT>getFunction(b"glVertexAttribIFormat")
    cglVertexAttribIFormat(attribindex, size, type, relativeoffset)

cdef void GetglVertexAttribLFormat(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    global cglVertexAttribLFormat
    cglVertexAttribLFormat = <GL_VERTEX_ATTRIB_L_FORMAT>getFunction(b"glVertexAttribLFormat")
    cglVertexAttribLFormat(attribindex, size, type, relativeoffset)

cdef void GetglVertexAttribBinding(GLuint attribindex, GLuint bindingindex):
    global cglVertexAttribBinding
    cglVertexAttribBinding = <GL_VERTEX_ATTRIB_BINDING>getFunction(b"glVertexAttribBinding")
    cglVertexAttribBinding(attribindex, bindingindex)

cdef void GetglVertexBindingDivisor(GLuint bindingindex, GLuint divisor):
    global cglVertexBindingDivisor
    cglVertexBindingDivisor = <GL_VERTEX_BINDING_DIVISOR>getFunction(b"glVertexBindingDivisor")
    cglVertexBindingDivisor(bindingindex, divisor)

cdef void GetglDebugMessageControl(GLenum source, GLenum type, GLenum severity, GLsizei count, const GLuint *ids, GLboolean enabled):
    global cglDebugMessageControl
    cglDebugMessageControl = <GL_DEBUG_MESSAGE_CONTROL>getFunction(b"glDebugMessageControl")
    cglDebugMessageControl(source, type, severity, count, ids, enabled)

cdef void GetglDebugMessageInsert(GLenum source, GLenum type, GLuint id, GLenum severity, GLsizei length, const GLchar *buf):
    global cglDebugMessageInsert
    cglDebugMessageInsert = <GL_DEBUG_MESSAGE_INSERT>getFunction(b"glDebugMessageInsert")
    cglDebugMessageInsert(source, type, id, severity, length, buf)

cdef void GetglDebugMessageCallback(GLDEBUGPROC callback, const void *userParam):
    global cglDebugMessageCallback
    cglDebugMessageCallback = <GL_DEBUG_MESSAGE_CALLBACK>getFunction(b"glDebugMessageCallback")
    cglDebugMessageCallback(callback, userParam)

cdef GLuint GetglGetDebugMessageLog(GLuint count, GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids, GLenum *severities, GLsizei *lengths, GLchar *messageLog):
    global cglGetDebugMessageLog
    cglGetDebugMessageLog = <GL_GET_DEBUG_MESSAGE_LOG>getFunction(b"glGetDebugMessageLog")
    cglGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog)

cdef void GetglPushDebugGroup(GLenum source, GLuint id, GLsizei length, const GLchar *message):
    global cglPushDebugGroup
    cglPushDebugGroup = <GL_PUSH_DEBUG_GROUP>getFunction(b"glPushDebugGroup")
    cglPushDebugGroup(source, id, length, message)

cdef void GetglPopDebugGroup():
    global cglPopDebugGroup
    cglPopDebugGroup = <GL_POP_DEBUG_GROUP>getFunction(b"glPopDebugGroup")
    cglPopDebugGroup()

cdef void GetglObjectLabel(GLenum identifier, GLuint name, GLsizei length, const GLchar *label):
    global cglObjectLabel
    cglObjectLabel = <GL_OBJECT_LABEL>getFunction(b"glObjectLabel")
    cglObjectLabel(identifier, name, length, label)

cdef void GetglGetObjectLabel(GLenum identifier, GLuint name, GLsizei bufSize, GLsizei *length, GLchar *label):
    global cglGetObjectLabel
    cglGetObjectLabel = <GL_GET_OBJECT_LABEL>getFunction(b"glGetObjectLabel")
    cglGetObjectLabel(identifier, name, bufSize, length, label)

cdef void GetglObjectPtrLabel(const void *ptr, GLsizei length, const GLchar *label):
    global cglObjectPtrLabel
    cglObjectPtrLabel = <GL_OBJECT_PTR_LABEL>getFunction(b"glObjectPtrLabel")
    cglObjectPtrLabel(ptr, length, label)

cdef void GetglGetObjectPtrLabel(const void *ptr, GLsizei bufSize, GLsizei *length, GLchar *label):
    global cglGetObjectPtrLabel
    cglGetObjectPtrLabel = <GL_GET_OBJECT_PTR_LABEL>getFunction(b"glGetObjectPtrLabel")
    cglGetObjectPtrLabel(ptr, bufSize, length, label)

cdef void GetglGetPointerv(GLenum pname, void **params):
    global cglGetPointerv
    cglGetPointerv = <GL_GET_POINTERV>getFunction(b"glGetPointerv")
    cglGetPointerv(pname, params)

cglClearBufferData = GetglClearBufferData
cglClearBufferSubData = GetglClearBufferSubData
cglDispatchCompute = GetglDispatchCompute
cglDispatchComputeIndirect = GetglDispatchComputeIndirect
cglCopyImageSubData = GetglCopyImageSubData
cglFramebufferParameteri = GetglFramebufferParameteri
cglGetFramebufferParameteriv = GetglGetFramebufferParameteriv
cglGetInternalformati64v = GetglGetInternalformati64v
cglInvalidateTexSubImage = GetglInvalidateTexSubImage
cglInvalidateTexImage = GetglInvalidateTexImage
cglInvalidateBufferSubData = GetglInvalidateBufferSubData
cglInvalidateBufferData = GetglInvalidateBufferData
cglInvalidateFramebuffer = GetglInvalidateFramebuffer
cglInvalidateSubFramebuffer = GetglInvalidateSubFramebuffer
cglMultiDrawArraysIndirect = GetglMultiDrawArraysIndirect
cglMultiDrawElementsIndirect = GetglMultiDrawElementsIndirect
cglGetProgramInterfaceiv = GetglGetProgramInterfaceiv
cglGetProgramResourceIndex = GetglGetProgramResourceIndex
cglGetProgramResourceName = GetglGetProgramResourceName
cglGetProgramResourceiv = GetglGetProgramResourceiv
cglGetProgramResourceLocation = GetglGetProgramResourceLocation
cglGetProgramResourceLocationIndex = GetglGetProgramResourceLocationIndex
cglShaderStorageBlockBinding = GetglShaderStorageBlockBinding
cglTexBufferRange = GetglTexBufferRange
cglTexStorage2DMultisample = GetglTexStorage2DMultisample
cglTexStorage3DMultisample = GetglTexStorage3DMultisample
cglTextureView = GetglTextureView
cglBindVertexBuffer = GetglBindVertexBuffer
cglVertexAttribFormat = GetglVertexAttribFormat
cglVertexAttribIFormat = GetglVertexAttribIFormat
cglVertexAttribLFormat = GetglVertexAttribLFormat
cglVertexAttribBinding = GetglVertexAttribBinding
cglVertexBindingDivisor = GetglVertexBindingDivisor
cglDebugMessageControl = GetglDebugMessageControl
cglDebugMessageInsert = GetglDebugMessageInsert
cglDebugMessageCallback = GetglDebugMessageCallback
cglGetDebugMessageLog = GetglGetDebugMessageLog
cglPushDebugGroup = GetglPushDebugGroup
cglPopDebugGroup = GetglPopDebugGroup
cglObjectLabel = GetglObjectLabel
cglGetObjectLabel = GetglGetObjectLabel
cglObjectPtrLabel = GetglObjectPtrLabel
cglGetObjectPtrLabel = GetglGetObjectPtrLabel
cglGetPointerv = GetglGetPointerv


cpdef void glClearBufferData(GLenum target, GLenum internalformat, GLenum format, GLenum type, const void *data):
    cglClearBufferData(target, internalformat, format, type, data)

cpdef void glClearBufferSubData(GLenum target, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data):
    cglClearBufferSubData(target, internalformat, offset, size, format, type, data)

cpdef void glDispatchCompute(GLuint num_groups_x, GLuint num_groups_y, GLuint num_groups_z):
    cglDispatchCompute(num_groups_x, num_groups_y, num_groups_z)

cpdef void glDispatchComputeIndirect(GLintptr indirect):
    cglDispatchComputeIndirect(indirect)

cpdef void glCopyImageSubData(GLuint srcName, GLenum srcTarget, GLint srcLevel, GLint srcX, GLint srcY, GLint srcZ, GLuint dstName, GLenum dstTarget, GLint dstLevel, GLint dstX, GLint dstY, GLint dstZ, GLsizei srcWidth, GLsizei srcHeight, GLsizei srcDepth):
    cglCopyImageSubData(srcName, srcTarget, srcLevel, srcX, srcY, srcZ, dstName, dstTarget, dstLevel, dstX, dstY, dstZ, srcWidth, srcHeight, srcDepth)

cpdef void glFramebufferParameteri(GLenum target, GLenum pname, GLint param):
    cglFramebufferParameteri(target, pname, param)

cpdef void glGetFramebufferParameteriv(GLenum target, GLenum pname, GLint *params):
    cglGetFramebufferParameteriv(target, pname, params)

cpdef void glGetInternalformati64v(GLenum target, GLenum internalformat, GLenum pname, GLsizei count, GLint64 *params):
    cglGetInternalformati64v(target, internalformat, pname, count, params)

cpdef void glInvalidateTexSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth):
    cglInvalidateTexSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth)

cpdef void glInvalidateTexImage(GLuint texture, GLint level):
    cglInvalidateTexImage(texture, level)

cpdef void glInvalidateBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr length):
    cglInvalidateBufferSubData(buffer, offset, length)

cpdef void glInvalidateBufferData(GLuint buffer):
    cglInvalidateBufferData(buffer)

cpdef void glInvalidateFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments):
    cglInvalidateFramebuffer(target, numAttachments, attachments)

cpdef void glInvalidateSubFramebuffer(GLenum target, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height):
    cglInvalidateSubFramebuffer(target, numAttachments, attachments, x, y, width, height)

cpdef void glMultiDrawArraysIndirect(GLenum mode, const void *indirect, GLsizei drawcount, GLsizei stride):
    cglMultiDrawArraysIndirect(mode, indirect, drawcount, stride)

cpdef void glMultiDrawElementsIndirect(GLenum mode, GLenum type, const void *indirect, GLsizei drawcount, GLsizei stride):
    cglMultiDrawElementsIndirect(mode, type, indirect, drawcount, stride)

cpdef void glGetProgramInterfaceiv(GLuint program, GLenum programInterface, GLenum pname, GLint *params):
    cglGetProgramInterfaceiv(program, programInterface, pname, params)

cpdef GLuint glGetProgramResourceIndex(GLuint program, GLenum programInterface, const GLchar *name):
    cglGetProgramResourceIndex(program, programInterface, name)

cpdef void glGetProgramResourceName(GLuint program, GLenum programInterface, GLuint index, GLsizei bufSize, GLsizei *length, GLchar *name):
    cglGetProgramResourceName(program, programInterface, index, bufSize, length, name)

cpdef void glGetProgramResourceiv(GLuint program, GLenum programInterface, GLuint index, GLsizei propCount, const GLenum *props, GLsizei count, GLsizei *length, GLint *params):
    cglGetProgramResourceiv(program, programInterface, index, propCount, props, count, length, params)

cpdef GLint glGetProgramResourceLocation(GLuint program, GLenum programInterface, const GLchar *name):
    cglGetProgramResourceLocation(program, programInterface, name)

cpdef GLint glGetProgramResourceLocationIndex(GLuint program, GLenum programInterface, const GLchar *name):
    cglGetProgramResourceLocationIndex(program, programInterface, name)

cpdef void glShaderStorageBlockBinding(GLuint program, GLuint storageBlockIndex, GLuint storageBlockBinding):
    cglShaderStorageBlockBinding(program, storageBlockIndex, storageBlockBinding)

cpdef void glTexBufferRange(GLenum target, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size):
    cglTexBufferRange(target, internalformat, buffer, offset, size)

cpdef void glTexStorage2DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    cglTexStorage2DMultisample(target, samples, internalformat, width, height, fixedsamplelocations)

cpdef void glTexStorage3DMultisample(GLenum target, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    cglTexStorage3DMultisample(target, samples, internalformat, width, height, depth, fixedsamplelocations)

cpdef void glTextureView(GLuint texture, GLenum target, GLuint origtexture, GLenum internalformat, GLuint minlevel, GLuint numlevels, GLuint minlayer, GLuint numlayers):
    cglTextureView(texture, target, origtexture, internalformat, minlevel, numlevels, minlayer, numlayers)

cpdef void glBindVertexBuffer(GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride):
    cglBindVertexBuffer(bindingindex, buffer, offset, stride)

cpdef void glVertexAttribFormat(GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset):
    cglVertexAttribFormat(attribindex, size, type, normalized, relativeoffset)

cpdef void glVertexAttribIFormat(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    cglVertexAttribIFormat(attribindex, size, type, relativeoffset)

cpdef void glVertexAttribLFormat(GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    cglVertexAttribLFormat(attribindex, size, type, relativeoffset)

cpdef void glVertexAttribBinding(GLuint attribindex, GLuint bindingindex):
    cglVertexAttribBinding(attribindex, bindingindex)

cpdef void glVertexBindingDivisor(GLuint bindingindex, GLuint divisor):
    cglVertexBindingDivisor(bindingindex, divisor)

cpdef void glDebugMessageControl(GLenum source, GLenum type, GLenum severity, GLsizei count, const GLuint *ids, GLboolean enabled):
    cglDebugMessageControl(source, type, severity, count, ids, enabled)

cpdef void glDebugMessageInsert(GLenum source, GLenum type, GLuint id, GLenum severity, GLsizei length, const GLchar *buf):
    cglDebugMessageInsert(source, type, id, severity, length, buf)

cpdef void glDebugMessageCallback(GLDEBUGPROC callback, const void *userParam):
    cglDebugMessageCallback(callback, userParam)

cpdef GLuint glGetDebugMessageLog(GLuint count, GLsizei bufSize, GLenum *sources, GLenum *types, GLuint *ids, GLenum *severities, GLsizei *lengths, GLchar *messageLog):
    cglGetDebugMessageLog(count, bufSize, sources, types, ids, severities, lengths, messageLog)

cpdef void glPushDebugGroup(GLenum source, GLuint id, GLsizei length, const GLchar *message):
    cglPushDebugGroup(source, id, length, message)

cpdef void glPopDebugGroup():
    cglPopDebugGroup()

cpdef void glObjectLabel(GLenum identifier, GLuint name, GLsizei length, const GLchar *label):
    cglObjectLabel(identifier, name, length, label)

cpdef void glGetObjectLabel(GLenum identifier, GLuint name, GLsizei bufSize, GLsizei *length, GLchar *label):
    cglGetObjectLabel(identifier, name, bufSize, length, label)

cpdef void glObjectPtrLabel(const void *ptr, GLsizei length, const GLchar *label):
    cglObjectPtrLabel(ptr, length, label)

cpdef void glGetObjectPtrLabel(const void *ptr, GLsizei bufSize, GLsizei *length, GLchar *label):
    cglGetObjectPtrLabel(ptr, bufSize, length, label)

cpdef void glGetPointerv(GLenum pname, void **params):
    cglGetPointerv(pname, params)
