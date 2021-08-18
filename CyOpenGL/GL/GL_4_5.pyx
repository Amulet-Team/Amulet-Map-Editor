# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_CONTEXT_LOST = 0x0507
cdef GLenum GL_LOWER_LEFT = 0x8CA1
cdef GLenum GL_UPPER_LEFT = 0x8CA2
cdef GLenum GL_NEGATIVE_ONE_TO_ONE = 0x935E
cdef GLenum GL_ZERO_TO_ONE = 0x935F
cdef GLenum GL_CLIP_ORIGIN = 0x935C
cdef GLenum GL_CLIP_DEPTH_MODE = 0x935D
cdef GLenum GL_QUERY_WAIT_INVERTED = 0x8E17
cdef GLenum GL_QUERY_NO_WAIT_INVERTED = 0x8E18
cdef GLenum GL_QUERY_BY_REGION_WAIT_INVERTED = 0x8E19
cdef GLenum GL_QUERY_BY_REGION_NO_WAIT_INVERTED = 0x8E1A
cdef GLenum GL_MAX_CULL_DISTANCES = 0x82F9
cdef GLenum GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES = 0x82FA
cdef GLenum GL_TEXTURE_TARGET = 0x1006
cdef GLenum GL_QUERY_TARGET = 0x82EA
cdef GLenum GL_TEXTURE_BINDING_1D = 0x8068
cdef GLenum GL_TEXTURE_BINDING_1D_ARRAY = 0x8C1C
cdef GLenum GL_TEXTURE_BINDING_2D = 0x8069
cdef GLenum GL_TEXTURE_BINDING_2D_ARRAY = 0x8C1D
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE = 0x9104
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 0x9105
cdef GLenum GL_TEXTURE_BINDING_3D = 0x806A
cdef GLenum GL_TEXTURE_BINDING_BUFFER = 0x8C2C
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP_ARRAY = 0x900A
cdef GLenum GL_TEXTURE_BINDING_RECTANGLE = 0x84F6
cdef GLenum GL_BACK = 0x0405
cdef GLenum GL_NO_ERROR = 0
cdef GLenum GL_GUILTY_CONTEXT_RESET = 0x8253
cdef GLenum GL_INNOCENT_CONTEXT_RESET = 0x8254
cdef GLenum GL_UNKNOWN_CONTEXT_RESET = 0x8255
cdef GLenum GL_RESET_NOTIFICATION_STRATEGY = 0x8256
cdef GLenum GL_LOSE_CONTEXT_ON_RESET = 0x8252
cdef GLenum GL_NO_RESET_NOTIFICATION = 0x8261
cdef GLenum GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT = 0x00000004
cdef GLenum GL_CONTEXT_LOST = 0x0507
cdef GLenum GL_COLOR_TABLE = 0x80D0
cdef GLenum GL_POST_CONVOLUTION_COLOR_TABLE = 0x80D1
cdef GLenum GL_POST_COLOR_MATRIX_COLOR_TABLE = 0x80D2
cdef GLenum GL_PROXY_COLOR_TABLE = 0x80D3
cdef GLenum GL_PROXY_POST_CONVOLUTION_COLOR_TABLE = 0x80D4
cdef GLenum GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE = 0x80D5
cdef GLenum GL_CONVOLUTION_1D = 0x8010
cdef GLenum GL_CONVOLUTION_2D = 0x8011
cdef GLenum GL_SEPARABLE_2D = 0x8012
cdef GLenum GL_HISTOGRAM = 0x8024
cdef GLenum GL_PROXY_HISTOGRAM = 0x8025
cdef GLenum GL_MINMAX = 0x802E
cdef GLenum GL_CONTEXT_RELEASE_BEHAVIOR = 0x82FB
cdef GLenum GL_NONE = 0
cdef GLenum GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH = 0x82FC

ctypedef void (*GL_CLIP_CONTROL)(GLenum origin, GLenum depth)
ctypedef void (*GL_CREATE_TRANSFORM_FEEDBACKS)(GLsizei n, GLuint *ids)
ctypedef void (*GL_TRANSFORM_FEEDBACK_BUFFER_BASE)(GLuint xfb, GLuint index, GLuint buffer)
ctypedef void (*GL_TRANSFORM_FEEDBACK_BUFFER_RANGE)(GLuint xfb, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
ctypedef void (*GL_GET_TRANSFORM_FEEDBACKIV)(GLuint xfb, GLenum pname, GLint *param)
ctypedef void (*GL_GET_TRANSFORM_FEEDBACKI_V)(GLuint xfb, GLenum pname, GLuint index, GLint *param)
ctypedef void (*GL_GET_TRANSFORM_FEEDBACKI64_V)(GLuint xfb, GLenum pname, GLuint index, GLint64 *param)
ctypedef void (*GL_CREATE_BUFFERS)(GLsizei n, GLuint *buffers)
ctypedef void (*GL_NAMED_BUFFER_STORAGE)(GLuint buffer, GLsizeiptr size, const void *data, GLbitfield flags)
ctypedef void (*GL_NAMED_BUFFER_DATA)(GLuint buffer, GLsizeiptr size, const void *data, GLenum usage)
ctypedef void (*GL_NAMED_BUFFER_SUB_DATA)(GLuint buffer, GLintptr offset, GLsizeiptr size, const void *data)
ctypedef void (*GL_COPY_NAMED_BUFFER_SUB_DATA)(GLuint readBuffer, GLuint writeBuffer, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size)
ctypedef void (*GL_CLEAR_NAMED_BUFFER_DATA)(GLuint buffer, GLenum internalformat, GLenum format, GLenum type, const void *data)
ctypedef void (*GL_CLEAR_NAMED_BUFFER_SUB_DATA)(GLuint buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data)
ctypedef void *(*GL_MAP_NAMED_BUFFER)(GLuint buffer, GLenum access)
ctypedef void *(*GL_MAP_NAMED_BUFFER_RANGE)(GLuint buffer, GLintptr offset, GLsizeiptr length, GLbitfield access)
ctypedef GLboolean (*GL_UNMAP_NAMED_BUFFER)(GLuint buffer)
ctypedef void (*GL_FLUSH_MAPPED_NAMED_BUFFER_RANGE)(GLuint buffer, GLintptr offset, GLsizeiptr length)
ctypedef void (*GL_GET_NAMED_BUFFER_PARAMETERIV)(GLuint buffer, GLenum pname, GLint *params)
ctypedef void (*GL_GET_NAMED_BUFFER_PARAMETERI64V)(GLuint buffer, GLenum pname, GLint64 *params)
ctypedef void (*GL_GET_NAMED_BUFFER_POINTERV)(GLuint buffer, GLenum pname, void **params)
ctypedef void (*GL_GET_NAMED_BUFFER_SUB_DATA)(GLuint buffer, GLintptr offset, GLsizeiptr size, void *data)
ctypedef void (*GL_CREATE_FRAMEBUFFERS)(GLsizei n, GLuint *framebuffers)
ctypedef void (*GL_NAMED_FRAMEBUFFER_RENDERBUFFER)(GLuint framebuffer, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
ctypedef void (*GL_NAMED_FRAMEBUFFER_PARAMETERI)(GLuint framebuffer, GLenum pname, GLint param)
ctypedef void (*GL_NAMED_FRAMEBUFFER_TEXTURE)(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level)
ctypedef void (*GL_NAMED_FRAMEBUFFER_TEXTURE_LAYER)(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level, GLint layer)
ctypedef void (*GL_NAMED_FRAMEBUFFER_DRAW_BUFFER)(GLuint framebuffer, GLenum buf)
ctypedef void (*GL_NAMED_FRAMEBUFFER_DRAW_BUFFERS)(GLuint framebuffer, GLsizei n, const GLenum *bufs)
ctypedef void (*GL_NAMED_FRAMEBUFFER_READ_BUFFER)(GLuint framebuffer, GLenum src)
ctypedef void (*GL_INVALIDATE_NAMED_FRAMEBUFFER_DATA)(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments)
ctypedef void (*GL_INVALIDATE_NAMED_FRAMEBUFFER_SUB_DATA)(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*GL_CLEAR_NAMED_FRAMEBUFFERIV)(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLint *value)
ctypedef void (*GL_CLEAR_NAMED_FRAMEBUFFERUIV)(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLuint *value)
ctypedef void (*GL_CLEAR_NAMED_FRAMEBUFFERFV)(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat *value)
ctypedef void (*GL_CLEAR_NAMED_FRAMEBUFFERFI)(GLuint framebuffer, GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil)
ctypedef void (*GL_BLIT_NAMED_FRAMEBUFFER)(GLuint readFramebuffer, GLuint drawFramebuffer, GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
ctypedef GLenum (*GL_CHECK_NAMED_FRAMEBUFFER_STATUS)(GLuint framebuffer, GLenum target)
ctypedef void (*GL_GET_NAMED_FRAMEBUFFER_PARAMETERIV)(GLuint framebuffer, GLenum pname, GLint *param)
ctypedef void (*GL_GET_NAMED_FRAMEBUFFER_ATTACHMENT_PARAMETERIV)(GLuint framebuffer, GLenum attachment, GLenum pname, GLint *params)
ctypedef void (*GL_CREATE_RENDERBUFFERS)(GLsizei n, GLuint *renderbuffers)
ctypedef void (*GL_NAMED_RENDERBUFFER_STORAGE)(GLuint renderbuffer, GLenum internalformat, GLsizei width, GLsizei height)
ctypedef void (*GL_NAMED_RENDERBUFFER_STORAGE_MULTISAMPLE)(GLuint renderbuffer, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height)
ctypedef void (*GL_GET_NAMED_RENDERBUFFER_PARAMETERIV)(GLuint renderbuffer, GLenum pname, GLint *params)
ctypedef void (*GL_CREATE_TEXTURES)(GLenum target, GLsizei n, GLuint *textures)
ctypedef void (*GL_TEXTURE_BUFFER)(GLuint texture, GLenum internalformat, GLuint buffer)
ctypedef void (*GL_TEXTURE_BUFFER_RANGE)(GLuint texture, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size)
ctypedef void (*GL_TEXTURE_STORAGE1D)(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width)
ctypedef void (*GL_TEXTURE_STORAGE2D)(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height)
ctypedef void (*GL_TEXTURE_STORAGE3D)(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth)
ctypedef void (*GL_TEXTURE_STORAGE2D_MULTISAMPLE)(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
ctypedef void (*GL_TEXTURE_STORAGE3D_MULTISAMPLE)(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
ctypedef void (*GL_TEXTURE_SUB_IMAGE1D)(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels)
ctypedef void (*GL_TEXTURE_SUB_IMAGE2D)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
ctypedef void (*GL_TEXTURE_SUB_IMAGE3D)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels)
ctypedef void (*GL_COMPRESSED_TEXTURE_SUB_IMAGE1D)(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*GL_COMPRESSED_TEXTURE_SUB_IMAGE2D)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*GL_COMPRESSED_TEXTURE_SUB_IMAGE3D)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*GL_COPY_TEXTURE_SUB_IMAGE1D)(GLuint texture, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
ctypedef void (*GL_COPY_TEXTURE_SUB_IMAGE2D)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*GL_COPY_TEXTURE_SUB_IMAGE3D)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*GL_TEXTURE_PARAMETERF)(GLuint texture, GLenum pname, GLfloat param)
ctypedef void (*GL_TEXTURE_PARAMETERFV)(GLuint texture, GLenum pname, const GLfloat *param)
ctypedef void (*GL_TEXTURE_PARAMETERI)(GLuint texture, GLenum pname, GLint param)
ctypedef void (*GL_TEXTURE_PARAMETER_IIV)(GLuint texture, GLenum pname, const GLint *params)
ctypedef void (*GL_TEXTURE_PARAMETER_IUIV)(GLuint texture, GLenum pname, const GLuint *params)
ctypedef void (*GL_TEXTURE_PARAMETERIV)(GLuint texture, GLenum pname, const GLint *param)
ctypedef void (*GL_GENERATE_TEXTURE_MIPMAP)(GLuint texture)
ctypedef void (*GL_BIND_TEXTURE_UNIT)(GLuint unit, GLuint texture)
ctypedef void (*GL_GET_TEXTURE_IMAGE)(GLuint texture, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
ctypedef void (*GL_GET_COMPRESSED_TEXTURE_IMAGE)(GLuint texture, GLint level, GLsizei bufSize, void *pixels)
ctypedef void (*GL_GET_TEXTURE_LEVEL_PARAMETERFV)(GLuint texture, GLint level, GLenum pname, GLfloat *params)
ctypedef void (*GL_GET_TEXTURE_LEVEL_PARAMETERIV)(GLuint texture, GLint level, GLenum pname, GLint *params)
ctypedef void (*GL_GET_TEXTURE_PARAMETERFV)(GLuint texture, GLenum pname, GLfloat *params)
ctypedef void (*GL_GET_TEXTURE_PARAMETER_IIV)(GLuint texture, GLenum pname, GLint *params)
ctypedef void (*GL_GET_TEXTURE_PARAMETER_IUIV)(GLuint texture, GLenum pname, GLuint *params)
ctypedef void (*GL_GET_TEXTURE_PARAMETERIV)(GLuint texture, GLenum pname, GLint *params)
ctypedef void (*GL_CREATE_VERTEX_ARRAYS)(GLsizei n, GLuint *arrays)
ctypedef void (*GL_DISABLE_VERTEX_ARRAY_ATTRIB)(GLuint vaobj, GLuint index)
ctypedef void (*GL_ENABLE_VERTEX_ARRAY_ATTRIB)(GLuint vaobj, GLuint index)
ctypedef void (*GL_VERTEX_ARRAY_ELEMENT_BUFFER)(GLuint vaobj, GLuint buffer)
ctypedef void (*GL_VERTEX_ARRAY_VERTEX_BUFFER)(GLuint vaobj, GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)
ctypedef void (*GL_VERTEX_ARRAY_VERTEX_BUFFERS)(GLuint vaobj, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides)
ctypedef void (*GL_VERTEX_ARRAY_ATTRIB_BINDING)(GLuint vaobj, GLuint attribindex, GLuint bindingindex)
ctypedef void (*GL_VERTEX_ARRAY_ATTRIB_FORMAT)(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset)
ctypedef void (*GL_VERTEX_ARRAY_ATTRIB_I_FORMAT)(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
ctypedef void (*GL_VERTEX_ARRAY_ATTRIB_L_FORMAT)(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
ctypedef void (*GL_VERTEX_ARRAY_BINDING_DIVISOR)(GLuint vaobj, GLuint bindingindex, GLuint divisor)
ctypedef void (*GL_GET_VERTEX_ARRAYIV)(GLuint vaobj, GLenum pname, GLint *param)
ctypedef void (*GL_GET_VERTEX_ARRAY_INDEXEDIV)(GLuint vaobj, GLuint index, GLenum pname, GLint *param)
ctypedef void (*GL_GET_VERTEX_ARRAY_INDEXED64IV)(GLuint vaobj, GLuint index, GLenum pname, GLint64 *param)
ctypedef void (*GL_CREATE_SAMPLERS)(GLsizei n, GLuint *samplers)
ctypedef void (*GL_CREATE_PROGRAM_PIPELINES)(GLsizei n, GLuint *pipelines)
ctypedef void (*GL_CREATE_QUERIES)(GLenum target, GLsizei n, GLuint *ids)
ctypedef void (*GL_GET_QUERY_BUFFER_OBJECTI64V)(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
ctypedef void (*GL_GET_QUERY_BUFFER_OBJECTIV)(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
ctypedef void (*GL_GET_QUERY_BUFFER_OBJECTUI64V)(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
ctypedef void (*GL_GET_QUERY_BUFFER_OBJECTUIV)(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
ctypedef void (*GL_MEMORY_BARRIER_BY_REGION)(GLbitfield barriers)
ctypedef void (*GL_GET_TEXTURE_SUB_IMAGE)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
ctypedef void (*GL_GET_COMPRESSED_TEXTURE_SUB_IMAGE)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei bufSize, void *pixels)
ctypedef GLenum (*GL_GET_GRAPHICS_RESET_STATUS)()
ctypedef void (*GL_GETN_COMPRESSED_TEX_IMAGE)(GLenum target, GLint lod, GLsizei bufSize, void *pixels)
ctypedef void (*GL_GETN_TEX_IMAGE)(GLenum target, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
ctypedef void (*GL_GETN_UNIFORMDV)(GLuint program, GLint location, GLsizei bufSize, GLdouble *params)
ctypedef void (*GL_GETN_UNIFORMFV)(GLuint program, GLint location, GLsizei bufSize, GLfloat *params)
ctypedef void (*GL_GETN_UNIFORMIV)(GLuint program, GLint location, GLsizei bufSize, GLint *params)
ctypedef void (*GL_GETN_UNIFORMUIV)(GLuint program, GLint location, GLsizei bufSize, GLuint *params)
ctypedef void (*GL_READN_PIXELS)(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei bufSize, void *data)
ctypedef void (*GL_GETN_MAPDV)(GLenum target, GLenum query, GLsizei bufSize, GLdouble *v)
ctypedef void (*GL_GETN_MAPFV)(GLenum target, GLenum query, GLsizei bufSize, GLfloat *v)
ctypedef void (*GL_GETN_MAPIV)(GLenum target, GLenum query, GLsizei bufSize, GLint *v)
ctypedef void (*GL_GETN_PIXEL_MAPFV)(GLenum map, GLsizei bufSize, GLfloat *values)
ctypedef void (*GL_GETN_PIXEL_MAPUIV)(GLenum map, GLsizei bufSize, GLuint *values)
ctypedef void (*GL_GETN_PIXEL_MAPUSV)(GLenum map, GLsizei bufSize, GLushort *values)
ctypedef void (*GL_GETN_POLYGON_STIPPLE)(GLsizei bufSize, GLubyte *pattern)
ctypedef void (*GL_GETN_COLOR_TABLE)(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *table)
ctypedef void (*GL_GETN_CONVOLUTION_FILTER)(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *image)
ctypedef void (*GL_GETN_SEPARABLE_FILTER)(GLenum target, GLenum format, GLenum type, GLsizei rowBufSize, void *row, GLsizei columnBufSize, void *column, void *span)
ctypedef void (*GL_GETN_HISTOGRAM)(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values)
ctypedef void (*GL_GETN_MINMAX)(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values)
ctypedef void (*GL_TEXTURE_BARRIER)()

cdef GL_CLIP_CONTROL cglClipControl = NULL
cdef GL_CREATE_TRANSFORM_FEEDBACKS cglCreateTransformFeedbacks = NULL
cdef GL_TRANSFORM_FEEDBACK_BUFFER_BASE cglTransformFeedbackBufferBase = NULL
cdef GL_TRANSFORM_FEEDBACK_BUFFER_RANGE cglTransformFeedbackBufferRange = NULL
cdef GL_GET_TRANSFORM_FEEDBACKIV cglGetTransformFeedbackiv = NULL
cdef GL_GET_TRANSFORM_FEEDBACKI_V cglGetTransformFeedbacki_v = NULL
cdef GL_GET_TRANSFORM_FEEDBACKI64_V cglGetTransformFeedbacki64_v = NULL
cdef GL_CREATE_BUFFERS cglCreateBuffers = NULL
cdef GL_NAMED_BUFFER_STORAGE cglNamedBufferStorage = NULL
cdef GL_NAMED_BUFFER_DATA cglNamedBufferData = NULL
cdef GL_NAMED_BUFFER_SUB_DATA cglNamedBufferSubData = NULL
cdef GL_COPY_NAMED_BUFFER_SUB_DATA cglCopyNamedBufferSubData = NULL
cdef GL_CLEAR_NAMED_BUFFER_DATA cglClearNamedBufferData = NULL
cdef GL_CLEAR_NAMED_BUFFER_SUB_DATA cglClearNamedBufferSubData = NULL
cdef GL_MAP_NAMED_BUFFER cglMapNamedBuffer = NULL
cdef GL_MAP_NAMED_BUFFER_RANGE cglMapNamedBufferRange = NULL
cdef GL_UNMAP_NAMED_BUFFER cglUnmapNamedBuffer = NULL
cdef GL_FLUSH_MAPPED_NAMED_BUFFER_RANGE cglFlushMappedNamedBufferRange = NULL
cdef GL_GET_NAMED_BUFFER_PARAMETERIV cglGetNamedBufferParameteriv = NULL
cdef GL_GET_NAMED_BUFFER_PARAMETERI64V cglGetNamedBufferParameteri64v = NULL
cdef GL_GET_NAMED_BUFFER_POINTERV cglGetNamedBufferPointerv = NULL
cdef GL_GET_NAMED_BUFFER_SUB_DATA cglGetNamedBufferSubData = NULL
cdef GL_CREATE_FRAMEBUFFERS cglCreateFramebuffers = NULL
cdef GL_NAMED_FRAMEBUFFER_RENDERBUFFER cglNamedFramebufferRenderbuffer = NULL
cdef GL_NAMED_FRAMEBUFFER_PARAMETERI cglNamedFramebufferParameteri = NULL
cdef GL_NAMED_FRAMEBUFFER_TEXTURE cglNamedFramebufferTexture = NULL
cdef GL_NAMED_FRAMEBUFFER_TEXTURE_LAYER cglNamedFramebufferTextureLayer = NULL
cdef GL_NAMED_FRAMEBUFFER_DRAW_BUFFER cglNamedFramebufferDrawBuffer = NULL
cdef GL_NAMED_FRAMEBUFFER_DRAW_BUFFERS cglNamedFramebufferDrawBuffers = NULL
cdef GL_NAMED_FRAMEBUFFER_READ_BUFFER cglNamedFramebufferReadBuffer = NULL
cdef GL_INVALIDATE_NAMED_FRAMEBUFFER_DATA cglInvalidateNamedFramebufferData = NULL
cdef GL_INVALIDATE_NAMED_FRAMEBUFFER_SUB_DATA cglInvalidateNamedFramebufferSubData = NULL
cdef GL_CLEAR_NAMED_FRAMEBUFFERIV cglClearNamedFramebufferiv = NULL
cdef GL_CLEAR_NAMED_FRAMEBUFFERUIV cglClearNamedFramebufferuiv = NULL
cdef GL_CLEAR_NAMED_FRAMEBUFFERFV cglClearNamedFramebufferfv = NULL
cdef GL_CLEAR_NAMED_FRAMEBUFFERFI cglClearNamedFramebufferfi = NULL
cdef GL_BLIT_NAMED_FRAMEBUFFER cglBlitNamedFramebuffer = NULL
cdef GL_CHECK_NAMED_FRAMEBUFFER_STATUS cglCheckNamedFramebufferStatus = NULL
cdef GL_GET_NAMED_FRAMEBUFFER_PARAMETERIV cglGetNamedFramebufferParameteriv = NULL
cdef GL_GET_NAMED_FRAMEBUFFER_ATTACHMENT_PARAMETERIV cglGetNamedFramebufferAttachmentParameteriv = NULL
cdef GL_CREATE_RENDERBUFFERS cglCreateRenderbuffers = NULL
cdef GL_NAMED_RENDERBUFFER_STORAGE cglNamedRenderbufferStorage = NULL
cdef GL_NAMED_RENDERBUFFER_STORAGE_MULTISAMPLE cglNamedRenderbufferStorageMultisample = NULL
cdef GL_GET_NAMED_RENDERBUFFER_PARAMETERIV cglGetNamedRenderbufferParameteriv = NULL
cdef GL_CREATE_TEXTURES cglCreateTextures = NULL
cdef GL_TEXTURE_BUFFER cglTextureBuffer = NULL
cdef GL_TEXTURE_BUFFER_RANGE cglTextureBufferRange = NULL
cdef GL_TEXTURE_STORAGE1D cglTextureStorage1D = NULL
cdef GL_TEXTURE_STORAGE2D cglTextureStorage2D = NULL
cdef GL_TEXTURE_STORAGE3D cglTextureStorage3D = NULL
cdef GL_TEXTURE_STORAGE2D_MULTISAMPLE cglTextureStorage2DMultisample = NULL
cdef GL_TEXTURE_STORAGE3D_MULTISAMPLE cglTextureStorage3DMultisample = NULL
cdef GL_TEXTURE_SUB_IMAGE1D cglTextureSubImage1D = NULL
cdef GL_TEXTURE_SUB_IMAGE2D cglTextureSubImage2D = NULL
cdef GL_TEXTURE_SUB_IMAGE3D cglTextureSubImage3D = NULL
cdef GL_COMPRESSED_TEXTURE_SUB_IMAGE1D cglCompressedTextureSubImage1D = NULL
cdef GL_COMPRESSED_TEXTURE_SUB_IMAGE2D cglCompressedTextureSubImage2D = NULL
cdef GL_COMPRESSED_TEXTURE_SUB_IMAGE3D cglCompressedTextureSubImage3D = NULL
cdef GL_COPY_TEXTURE_SUB_IMAGE1D cglCopyTextureSubImage1D = NULL
cdef GL_COPY_TEXTURE_SUB_IMAGE2D cglCopyTextureSubImage2D = NULL
cdef GL_COPY_TEXTURE_SUB_IMAGE3D cglCopyTextureSubImage3D = NULL
cdef GL_TEXTURE_PARAMETERF cglTextureParameterf = NULL
cdef GL_TEXTURE_PARAMETERFV cglTextureParameterfv = NULL
cdef GL_TEXTURE_PARAMETERI cglTextureParameteri = NULL
cdef GL_TEXTURE_PARAMETER_IIV cglTextureParameterIiv = NULL
cdef GL_TEXTURE_PARAMETER_IUIV cglTextureParameterIuiv = NULL
cdef GL_TEXTURE_PARAMETERIV cglTextureParameteriv = NULL
cdef GL_GENERATE_TEXTURE_MIPMAP cglGenerateTextureMipmap = NULL
cdef GL_BIND_TEXTURE_UNIT cglBindTextureUnit = NULL
cdef GL_GET_TEXTURE_IMAGE cglGetTextureImage = NULL
cdef GL_GET_COMPRESSED_TEXTURE_IMAGE cglGetCompressedTextureImage = NULL
cdef GL_GET_TEXTURE_LEVEL_PARAMETERFV cglGetTextureLevelParameterfv = NULL
cdef GL_GET_TEXTURE_LEVEL_PARAMETERIV cglGetTextureLevelParameteriv = NULL
cdef GL_GET_TEXTURE_PARAMETERFV cglGetTextureParameterfv = NULL
cdef GL_GET_TEXTURE_PARAMETER_IIV cglGetTextureParameterIiv = NULL
cdef GL_GET_TEXTURE_PARAMETER_IUIV cglGetTextureParameterIuiv = NULL
cdef GL_GET_TEXTURE_PARAMETERIV cglGetTextureParameteriv = NULL
cdef GL_CREATE_VERTEX_ARRAYS cglCreateVertexArrays = NULL
cdef GL_DISABLE_VERTEX_ARRAY_ATTRIB cglDisableVertexArrayAttrib = NULL
cdef GL_ENABLE_VERTEX_ARRAY_ATTRIB cglEnableVertexArrayAttrib = NULL
cdef GL_VERTEX_ARRAY_ELEMENT_BUFFER cglVertexArrayElementBuffer = NULL
cdef GL_VERTEX_ARRAY_VERTEX_BUFFER cglVertexArrayVertexBuffer = NULL
cdef GL_VERTEX_ARRAY_VERTEX_BUFFERS cglVertexArrayVertexBuffers = NULL
cdef GL_VERTEX_ARRAY_ATTRIB_BINDING cglVertexArrayAttribBinding = NULL
cdef GL_VERTEX_ARRAY_ATTRIB_FORMAT cglVertexArrayAttribFormat = NULL
cdef GL_VERTEX_ARRAY_ATTRIB_I_FORMAT cglVertexArrayAttribIFormat = NULL
cdef GL_VERTEX_ARRAY_ATTRIB_L_FORMAT cglVertexArrayAttribLFormat = NULL
cdef GL_VERTEX_ARRAY_BINDING_DIVISOR cglVertexArrayBindingDivisor = NULL
cdef GL_GET_VERTEX_ARRAYIV cglGetVertexArrayiv = NULL
cdef GL_GET_VERTEX_ARRAY_INDEXEDIV cglGetVertexArrayIndexediv = NULL
cdef GL_GET_VERTEX_ARRAY_INDEXED64IV cglGetVertexArrayIndexed64iv = NULL
cdef GL_CREATE_SAMPLERS cglCreateSamplers = NULL
cdef GL_CREATE_PROGRAM_PIPELINES cglCreateProgramPipelines = NULL
cdef GL_CREATE_QUERIES cglCreateQueries = NULL
cdef GL_GET_QUERY_BUFFER_OBJECTI64V cglGetQueryBufferObjecti64v = NULL
cdef GL_GET_QUERY_BUFFER_OBJECTIV cglGetQueryBufferObjectiv = NULL
cdef GL_GET_QUERY_BUFFER_OBJECTUI64V cglGetQueryBufferObjectui64v = NULL
cdef GL_GET_QUERY_BUFFER_OBJECTUIV cglGetQueryBufferObjectuiv = NULL
cdef GL_MEMORY_BARRIER_BY_REGION cglMemoryBarrierByRegion = NULL
cdef GL_GET_TEXTURE_SUB_IMAGE cglGetTextureSubImage = NULL
cdef GL_GET_COMPRESSED_TEXTURE_SUB_IMAGE cglGetCompressedTextureSubImage = NULL
cdef GL_GET_GRAPHICS_RESET_STATUS cglGetGraphicsResetStatus = NULL
cdef GL_GETN_COMPRESSED_TEX_IMAGE cglGetnCompressedTexImage = NULL
cdef GL_GETN_TEX_IMAGE cglGetnTexImage = NULL
cdef GL_GETN_UNIFORMDV cglGetnUniformdv = NULL
cdef GL_GETN_UNIFORMFV cglGetnUniformfv = NULL
cdef GL_GETN_UNIFORMIV cglGetnUniformiv = NULL
cdef GL_GETN_UNIFORMUIV cglGetnUniformuiv = NULL
cdef GL_READN_PIXELS cglReadnPixels = NULL
cdef GL_GETN_MAPDV cglGetnMapdv = NULL
cdef GL_GETN_MAPFV cglGetnMapfv = NULL
cdef GL_GETN_MAPIV cglGetnMapiv = NULL
cdef GL_GETN_PIXEL_MAPFV cglGetnPixelMapfv = NULL
cdef GL_GETN_PIXEL_MAPUIV cglGetnPixelMapuiv = NULL
cdef GL_GETN_PIXEL_MAPUSV cglGetnPixelMapusv = NULL
cdef GL_GETN_POLYGON_STIPPLE cglGetnPolygonStipple = NULL
cdef GL_GETN_COLOR_TABLE cglGetnColorTable = NULL
cdef GL_GETN_CONVOLUTION_FILTER cglGetnConvolutionFilter = NULL
cdef GL_GETN_SEPARABLE_FILTER cglGetnSeparableFilter = NULL
cdef GL_GETN_HISTOGRAM cglGetnHistogram = NULL
cdef GL_GETN_MINMAX cglGetnMinmax = NULL
cdef GL_TEXTURE_BARRIER cglTextureBarrier = NULL


cdef void GetglClipControl(GLenum origin, GLenum depth):
    global cglClipControl
    cglClipControl = <GL_CLIP_CONTROL>getFunction(b"glClipControl")
    cglClipControl(origin, depth)

cdef void GetglCreateTransformFeedbacks(GLsizei n, GLuint *ids):
    global cglCreateTransformFeedbacks
    cglCreateTransformFeedbacks = <GL_CREATE_TRANSFORM_FEEDBACKS>getFunction(b"glCreateTransformFeedbacks")
    cglCreateTransformFeedbacks(n, ids)

cdef void GetglTransformFeedbackBufferBase(GLuint xfb, GLuint index, GLuint buffer):
    global cglTransformFeedbackBufferBase
    cglTransformFeedbackBufferBase = <GL_TRANSFORM_FEEDBACK_BUFFER_BASE>getFunction(b"glTransformFeedbackBufferBase")
    cglTransformFeedbackBufferBase(xfb, index, buffer)

cdef void GetglTransformFeedbackBufferRange(GLuint xfb, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size):
    global cglTransformFeedbackBufferRange
    cglTransformFeedbackBufferRange = <GL_TRANSFORM_FEEDBACK_BUFFER_RANGE>getFunction(b"glTransformFeedbackBufferRange")
    cglTransformFeedbackBufferRange(xfb, index, buffer, offset, size)

cdef void GetglGetTransformFeedbackiv(GLuint xfb, GLenum pname, GLint *param):
    global cglGetTransformFeedbackiv
    cglGetTransformFeedbackiv = <GL_GET_TRANSFORM_FEEDBACKIV>getFunction(b"glGetTransformFeedbackiv")
    cglGetTransformFeedbackiv(xfb, pname, param)

cdef void GetglGetTransformFeedbacki_v(GLuint xfb, GLenum pname, GLuint index, GLint *param):
    global cglGetTransformFeedbacki_v
    cglGetTransformFeedbacki_v = <GL_GET_TRANSFORM_FEEDBACKI_V>getFunction(b"glGetTransformFeedbacki_v")
    cglGetTransformFeedbacki_v(xfb, pname, index, param)

cdef void GetglGetTransformFeedbacki64_v(GLuint xfb, GLenum pname, GLuint index, GLint64 *param):
    global cglGetTransformFeedbacki64_v
    cglGetTransformFeedbacki64_v = <GL_GET_TRANSFORM_FEEDBACKI64_V>getFunction(b"glGetTransformFeedbacki64_v")
    cglGetTransformFeedbacki64_v(xfb, pname, index, param)

cdef void GetglCreateBuffers(GLsizei n, GLuint *buffers):
    global cglCreateBuffers
    cglCreateBuffers = <GL_CREATE_BUFFERS>getFunction(b"glCreateBuffers")
    cglCreateBuffers(n, buffers)

cdef void GetglNamedBufferStorage(GLuint buffer, GLsizeiptr size, const void *data, GLbitfield flags):
    global cglNamedBufferStorage
    cglNamedBufferStorage = <GL_NAMED_BUFFER_STORAGE>getFunction(b"glNamedBufferStorage")
    cglNamedBufferStorage(buffer, size, data, flags)

cdef void GetglNamedBufferData(GLuint buffer, GLsizeiptr size, const void *data, GLenum usage):
    global cglNamedBufferData
    cglNamedBufferData = <GL_NAMED_BUFFER_DATA>getFunction(b"glNamedBufferData")
    cglNamedBufferData(buffer, size, data, usage)

cdef void GetglNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, const void *data):
    global cglNamedBufferSubData
    cglNamedBufferSubData = <GL_NAMED_BUFFER_SUB_DATA>getFunction(b"glNamedBufferSubData")
    cglNamedBufferSubData(buffer, offset, size, data)

cdef void GetglCopyNamedBufferSubData(GLuint readBuffer, GLuint writeBuffer, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size):
    global cglCopyNamedBufferSubData
    cglCopyNamedBufferSubData = <GL_COPY_NAMED_BUFFER_SUB_DATA>getFunction(b"glCopyNamedBufferSubData")
    cglCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size)

cdef void GetglClearNamedBufferData(GLuint buffer, GLenum internalformat, GLenum format, GLenum type, const void *data):
    global cglClearNamedBufferData
    cglClearNamedBufferData = <GL_CLEAR_NAMED_BUFFER_DATA>getFunction(b"glClearNamedBufferData")
    cglClearNamedBufferData(buffer, internalformat, format, type, data)

cdef void GetglClearNamedBufferSubData(GLuint buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data):
    global cglClearNamedBufferSubData
    cglClearNamedBufferSubData = <GL_CLEAR_NAMED_BUFFER_SUB_DATA>getFunction(b"glClearNamedBufferSubData")
    cglClearNamedBufferSubData(buffer, internalformat, offset, size, format, type, data)

cdef void *GetglMapNamedBuffer(GLuint buffer, GLenum access):
    global cglMapNamedBuffer
    cglMapNamedBuffer = <GL_MAP_NAMED_BUFFER>getFunction(b"glMapNamedBuffer")
    cglMapNamedBuffer(buffer, access)

cdef void *GetglMapNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length, GLbitfield access):
    global cglMapNamedBufferRange
    cglMapNamedBufferRange = <GL_MAP_NAMED_BUFFER_RANGE>getFunction(b"glMapNamedBufferRange")
    cglMapNamedBufferRange(buffer, offset, length, access)

cdef GLboolean GetglUnmapNamedBuffer(GLuint buffer):
    global cglUnmapNamedBuffer
    cglUnmapNamedBuffer = <GL_UNMAP_NAMED_BUFFER>getFunction(b"glUnmapNamedBuffer")
    cglUnmapNamedBuffer(buffer)

cdef void GetglFlushMappedNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length):
    global cglFlushMappedNamedBufferRange
    cglFlushMappedNamedBufferRange = <GL_FLUSH_MAPPED_NAMED_BUFFER_RANGE>getFunction(b"glFlushMappedNamedBufferRange")
    cglFlushMappedNamedBufferRange(buffer, offset, length)

cdef void GetglGetNamedBufferParameteriv(GLuint buffer, GLenum pname, GLint *params):
    global cglGetNamedBufferParameteriv
    cglGetNamedBufferParameteriv = <GL_GET_NAMED_BUFFER_PARAMETERIV>getFunction(b"glGetNamedBufferParameteriv")
    cglGetNamedBufferParameteriv(buffer, pname, params)

cdef void GetglGetNamedBufferParameteri64v(GLuint buffer, GLenum pname, GLint64 *params):
    global cglGetNamedBufferParameteri64v
    cglGetNamedBufferParameteri64v = <GL_GET_NAMED_BUFFER_PARAMETERI64V>getFunction(b"glGetNamedBufferParameteri64v")
    cglGetNamedBufferParameteri64v(buffer, pname, params)

cdef void GetglGetNamedBufferPointerv(GLuint buffer, GLenum pname, void **params):
    global cglGetNamedBufferPointerv
    cglGetNamedBufferPointerv = <GL_GET_NAMED_BUFFER_POINTERV>getFunction(b"glGetNamedBufferPointerv")
    cglGetNamedBufferPointerv(buffer, pname, params)

cdef void GetglGetNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, void *data):
    global cglGetNamedBufferSubData
    cglGetNamedBufferSubData = <GL_GET_NAMED_BUFFER_SUB_DATA>getFunction(b"glGetNamedBufferSubData")
    cglGetNamedBufferSubData(buffer, offset, size, data)

cdef void GetglCreateFramebuffers(GLsizei n, GLuint *framebuffers):
    global cglCreateFramebuffers
    cglCreateFramebuffers = <GL_CREATE_FRAMEBUFFERS>getFunction(b"glCreateFramebuffers")
    cglCreateFramebuffers(n, framebuffers)

cdef void GetglNamedFramebufferRenderbuffer(GLuint framebuffer, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer):
    global cglNamedFramebufferRenderbuffer
    cglNamedFramebufferRenderbuffer = <GL_NAMED_FRAMEBUFFER_RENDERBUFFER>getFunction(b"glNamedFramebufferRenderbuffer")
    cglNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer)

cdef void GetglNamedFramebufferParameteri(GLuint framebuffer, GLenum pname, GLint param):
    global cglNamedFramebufferParameteri
    cglNamedFramebufferParameteri = <GL_NAMED_FRAMEBUFFER_PARAMETERI>getFunction(b"glNamedFramebufferParameteri")
    cglNamedFramebufferParameteri(framebuffer, pname, param)

cdef void GetglNamedFramebufferTexture(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level):
    global cglNamedFramebufferTexture
    cglNamedFramebufferTexture = <GL_NAMED_FRAMEBUFFER_TEXTURE>getFunction(b"glNamedFramebufferTexture")
    cglNamedFramebufferTexture(framebuffer, attachment, texture, level)

cdef void GetglNamedFramebufferTextureLayer(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level, GLint layer):
    global cglNamedFramebufferTextureLayer
    cglNamedFramebufferTextureLayer = <GL_NAMED_FRAMEBUFFER_TEXTURE_LAYER>getFunction(b"glNamedFramebufferTextureLayer")
    cglNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer)

cdef void GetglNamedFramebufferDrawBuffer(GLuint framebuffer, GLenum buf):
    global cglNamedFramebufferDrawBuffer
    cglNamedFramebufferDrawBuffer = <GL_NAMED_FRAMEBUFFER_DRAW_BUFFER>getFunction(b"glNamedFramebufferDrawBuffer")
    cglNamedFramebufferDrawBuffer(framebuffer, buf)

cdef void GetglNamedFramebufferDrawBuffers(GLuint framebuffer, GLsizei n, const GLenum *bufs):
    global cglNamedFramebufferDrawBuffers
    cglNamedFramebufferDrawBuffers = <GL_NAMED_FRAMEBUFFER_DRAW_BUFFERS>getFunction(b"glNamedFramebufferDrawBuffers")
    cglNamedFramebufferDrawBuffers(framebuffer, n, bufs)

cdef void GetglNamedFramebufferReadBuffer(GLuint framebuffer, GLenum src):
    global cglNamedFramebufferReadBuffer
    cglNamedFramebufferReadBuffer = <GL_NAMED_FRAMEBUFFER_READ_BUFFER>getFunction(b"glNamedFramebufferReadBuffer")
    cglNamedFramebufferReadBuffer(framebuffer, src)

cdef void GetglInvalidateNamedFramebufferData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments):
    global cglInvalidateNamedFramebufferData
    cglInvalidateNamedFramebufferData = <GL_INVALIDATE_NAMED_FRAMEBUFFER_DATA>getFunction(b"glInvalidateNamedFramebufferData")
    cglInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments)

cdef void GetglInvalidateNamedFramebufferSubData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglInvalidateNamedFramebufferSubData
    cglInvalidateNamedFramebufferSubData = <GL_INVALIDATE_NAMED_FRAMEBUFFER_SUB_DATA>getFunction(b"glInvalidateNamedFramebufferSubData")
    cglInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height)

cdef void GetglClearNamedFramebufferiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLint *value):
    global cglClearNamedFramebufferiv
    cglClearNamedFramebufferiv = <GL_CLEAR_NAMED_FRAMEBUFFERIV>getFunction(b"glClearNamedFramebufferiv")
    cglClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value)

cdef void GetglClearNamedFramebufferuiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLuint *value):
    global cglClearNamedFramebufferuiv
    cglClearNamedFramebufferuiv = <GL_CLEAR_NAMED_FRAMEBUFFERUIV>getFunction(b"glClearNamedFramebufferuiv")
    cglClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value)

cdef void GetglClearNamedFramebufferfv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat *value):
    global cglClearNamedFramebufferfv
    cglClearNamedFramebufferfv = <GL_CLEAR_NAMED_FRAMEBUFFERFV>getFunction(b"glClearNamedFramebufferfv")
    cglClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value)

cdef void GetglClearNamedFramebufferfi(GLuint framebuffer, GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil):
    global cglClearNamedFramebufferfi
    cglClearNamedFramebufferfi = <GL_CLEAR_NAMED_FRAMEBUFFERFI>getFunction(b"glClearNamedFramebufferfi")
    cglClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil)

cdef void GetglBlitNamedFramebuffer(GLuint readFramebuffer, GLuint drawFramebuffer, GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter):
    global cglBlitNamedFramebuffer
    cglBlitNamedFramebuffer = <GL_BLIT_NAMED_FRAMEBUFFER>getFunction(b"glBlitNamedFramebuffer")
    cglBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)

cdef GLenum GetglCheckNamedFramebufferStatus(GLuint framebuffer, GLenum target):
    global cglCheckNamedFramebufferStatus
    cglCheckNamedFramebufferStatus = <GL_CHECK_NAMED_FRAMEBUFFER_STATUS>getFunction(b"glCheckNamedFramebufferStatus")
    cglCheckNamedFramebufferStatus(framebuffer, target)

cdef void GetglGetNamedFramebufferParameteriv(GLuint framebuffer, GLenum pname, GLint *param):
    global cglGetNamedFramebufferParameteriv
    cglGetNamedFramebufferParameteriv = <GL_GET_NAMED_FRAMEBUFFER_PARAMETERIV>getFunction(b"glGetNamedFramebufferParameteriv")
    cglGetNamedFramebufferParameteriv(framebuffer, pname, param)

cdef void GetglGetNamedFramebufferAttachmentParameteriv(GLuint framebuffer, GLenum attachment, GLenum pname, GLint *params):
    global cglGetNamedFramebufferAttachmentParameteriv
    cglGetNamedFramebufferAttachmentParameteriv = <GL_GET_NAMED_FRAMEBUFFER_ATTACHMENT_PARAMETERIV>getFunction(b"glGetNamedFramebufferAttachmentParameteriv")
    cglGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname, params)

cdef void GetglCreateRenderbuffers(GLsizei n, GLuint *renderbuffers):
    global cglCreateRenderbuffers
    cglCreateRenderbuffers = <GL_CREATE_RENDERBUFFERS>getFunction(b"glCreateRenderbuffers")
    cglCreateRenderbuffers(n, renderbuffers)

cdef void GetglNamedRenderbufferStorage(GLuint renderbuffer, GLenum internalformat, GLsizei width, GLsizei height):
    global cglNamedRenderbufferStorage
    cglNamedRenderbufferStorage = <GL_NAMED_RENDERBUFFER_STORAGE>getFunction(b"glNamedRenderbufferStorage")
    cglNamedRenderbufferStorage(renderbuffer, internalformat, width, height)

cdef void GetglNamedRenderbufferStorageMultisample(GLuint renderbuffer, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height):
    global cglNamedRenderbufferStorageMultisample
    cglNamedRenderbufferStorageMultisample = <GL_NAMED_RENDERBUFFER_STORAGE_MULTISAMPLE>getFunction(b"glNamedRenderbufferStorageMultisample")
    cglNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height)

cdef void GetglGetNamedRenderbufferParameteriv(GLuint renderbuffer, GLenum pname, GLint *params):
    global cglGetNamedRenderbufferParameteriv
    cglGetNamedRenderbufferParameteriv = <GL_GET_NAMED_RENDERBUFFER_PARAMETERIV>getFunction(b"glGetNamedRenderbufferParameteriv")
    cglGetNamedRenderbufferParameteriv(renderbuffer, pname, params)

cdef void GetglCreateTextures(GLenum target, GLsizei n, GLuint *textures):
    global cglCreateTextures
    cglCreateTextures = <GL_CREATE_TEXTURES>getFunction(b"glCreateTextures")
    cglCreateTextures(target, n, textures)

cdef void GetglTextureBuffer(GLuint texture, GLenum internalformat, GLuint buffer):
    global cglTextureBuffer
    cglTextureBuffer = <GL_TEXTURE_BUFFER>getFunction(b"glTextureBuffer")
    cglTextureBuffer(texture, internalformat, buffer)

cdef void GetglTextureBufferRange(GLuint texture, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size):
    global cglTextureBufferRange
    cglTextureBufferRange = <GL_TEXTURE_BUFFER_RANGE>getFunction(b"glTextureBufferRange")
    cglTextureBufferRange(texture, internalformat, buffer, offset, size)

cdef void GetglTextureStorage1D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width):
    global cglTextureStorage1D
    cglTextureStorage1D = <GL_TEXTURE_STORAGE1D>getFunction(b"glTextureStorage1D")
    cglTextureStorage1D(texture, levels, internalformat, width)

cdef void GetglTextureStorage2D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height):
    global cglTextureStorage2D
    cglTextureStorage2D = <GL_TEXTURE_STORAGE2D>getFunction(b"glTextureStorage2D")
    cglTextureStorage2D(texture, levels, internalformat, width, height)

cdef void GetglTextureStorage3D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth):
    global cglTextureStorage3D
    cglTextureStorage3D = <GL_TEXTURE_STORAGE3D>getFunction(b"glTextureStorage3D")
    cglTextureStorage3D(texture, levels, internalformat, width, height, depth)

cdef void GetglTextureStorage2DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    global cglTextureStorage2DMultisample
    cglTextureStorage2DMultisample = <GL_TEXTURE_STORAGE2D_MULTISAMPLE>getFunction(b"glTextureStorage2DMultisample")
    cglTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations)

cdef void GetglTextureStorage3DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    global cglTextureStorage3DMultisample
    cglTextureStorage3DMultisample = <GL_TEXTURE_STORAGE3D_MULTISAMPLE>getFunction(b"glTextureStorage3DMultisample")
    cglTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations)

cdef void GetglTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels):
    global cglTextureSubImage1D
    cglTextureSubImage1D = <GL_TEXTURE_SUB_IMAGE1D>getFunction(b"glTextureSubImage1D")
    cglTextureSubImage1D(texture, level, xoffset, width, format, type, pixels)

cdef void GetglTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    global cglTextureSubImage2D
    cglTextureSubImage2D = <GL_TEXTURE_SUB_IMAGE2D>getFunction(b"glTextureSubImage2D")
    cglTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type, pixels)

cdef void GetglTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels):
    global cglTextureSubImage3D
    cglTextureSubImage3D = <GL_TEXTURE_SUB_IMAGE3D>getFunction(b"glTextureSubImage3D")
    cglTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)

cdef void GetglCompressedTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTextureSubImage1D
    cglCompressedTextureSubImage1D = <GL_COMPRESSED_TEXTURE_SUB_IMAGE1D>getFunction(b"glCompressedTextureSubImage1D")
    cglCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize, data)

cdef void GetglCompressedTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTextureSubImage2D
    cglCompressedTextureSubImage2D = <GL_COMPRESSED_TEXTURE_SUB_IMAGE2D>getFunction(b"glCompressedTextureSubImage2D")
    cglCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize, data)

cdef void GetglCompressedTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTextureSubImage3D
    cglCompressedTextureSubImage3D = <GL_COMPRESSED_TEXTURE_SUB_IMAGE3D>getFunction(b"glCompressedTextureSubImage3D")
    cglCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

cdef void GetglCopyTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width):
    global cglCopyTextureSubImage1D
    cglCopyTextureSubImage1D = <GL_COPY_TEXTURE_SUB_IMAGE1D>getFunction(b"glCopyTextureSubImage1D")
    cglCopyTextureSubImage1D(texture, level, xoffset, x, y, width)

cdef void GetglCopyTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglCopyTextureSubImage2D
    cglCopyTextureSubImage2D = <GL_COPY_TEXTURE_SUB_IMAGE2D>getFunction(b"glCopyTextureSubImage2D")
    cglCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height)

cdef void GetglCopyTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglCopyTextureSubImage3D
    cglCopyTextureSubImage3D = <GL_COPY_TEXTURE_SUB_IMAGE3D>getFunction(b"glCopyTextureSubImage3D")
    cglCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height)

cdef void GetglTextureParameterf(GLuint texture, GLenum pname, GLfloat param):
    global cglTextureParameterf
    cglTextureParameterf = <GL_TEXTURE_PARAMETERF>getFunction(b"glTextureParameterf")
    cglTextureParameterf(texture, pname, param)

cdef void GetglTextureParameterfv(GLuint texture, GLenum pname, const GLfloat *param):
    global cglTextureParameterfv
    cglTextureParameterfv = <GL_TEXTURE_PARAMETERFV>getFunction(b"glTextureParameterfv")
    cglTextureParameterfv(texture, pname, param)

cdef void GetglTextureParameteri(GLuint texture, GLenum pname, GLint param):
    global cglTextureParameteri
    cglTextureParameteri = <GL_TEXTURE_PARAMETERI>getFunction(b"glTextureParameteri")
    cglTextureParameteri(texture, pname, param)

cdef void GetglTextureParameterIiv(GLuint texture, GLenum pname, const GLint *params):
    global cglTextureParameterIiv
    cglTextureParameterIiv = <GL_TEXTURE_PARAMETER_IIV>getFunction(b"glTextureParameterIiv")
    cglTextureParameterIiv(texture, pname, params)

cdef void GetglTextureParameterIuiv(GLuint texture, GLenum pname, const GLuint *params):
    global cglTextureParameterIuiv
    cglTextureParameterIuiv = <GL_TEXTURE_PARAMETER_IUIV>getFunction(b"glTextureParameterIuiv")
    cglTextureParameterIuiv(texture, pname, params)

cdef void GetglTextureParameteriv(GLuint texture, GLenum pname, const GLint *param):
    global cglTextureParameteriv
    cglTextureParameteriv = <GL_TEXTURE_PARAMETERIV>getFunction(b"glTextureParameteriv")
    cglTextureParameteriv(texture, pname, param)

cdef void GetglGenerateTextureMipmap(GLuint texture):
    global cglGenerateTextureMipmap
    cglGenerateTextureMipmap = <GL_GENERATE_TEXTURE_MIPMAP>getFunction(b"glGenerateTextureMipmap")
    cglGenerateTextureMipmap(texture)

cdef void GetglBindTextureUnit(GLuint unit, GLuint texture):
    global cglBindTextureUnit
    cglBindTextureUnit = <GL_BIND_TEXTURE_UNIT>getFunction(b"glBindTextureUnit")
    cglBindTextureUnit(unit, texture)

cdef void GetglGetTextureImage(GLuint texture, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    global cglGetTextureImage
    cglGetTextureImage = <GL_GET_TEXTURE_IMAGE>getFunction(b"glGetTextureImage")
    cglGetTextureImage(texture, level, format, type, bufSize, pixels)

cdef void GetglGetCompressedTextureImage(GLuint texture, GLint level, GLsizei bufSize, void *pixels):
    global cglGetCompressedTextureImage
    cglGetCompressedTextureImage = <GL_GET_COMPRESSED_TEXTURE_IMAGE>getFunction(b"glGetCompressedTextureImage")
    cglGetCompressedTextureImage(texture, level, bufSize, pixels)

cdef void GetglGetTextureLevelParameterfv(GLuint texture, GLint level, GLenum pname, GLfloat *params):
    global cglGetTextureLevelParameterfv
    cglGetTextureLevelParameterfv = <GL_GET_TEXTURE_LEVEL_PARAMETERFV>getFunction(b"glGetTextureLevelParameterfv")
    cglGetTextureLevelParameterfv(texture, level, pname, params)

cdef void GetglGetTextureLevelParameteriv(GLuint texture, GLint level, GLenum pname, GLint *params):
    global cglGetTextureLevelParameteriv
    cglGetTextureLevelParameteriv = <GL_GET_TEXTURE_LEVEL_PARAMETERIV>getFunction(b"glGetTextureLevelParameteriv")
    cglGetTextureLevelParameteriv(texture, level, pname, params)

cdef void GetglGetTextureParameterfv(GLuint texture, GLenum pname, GLfloat *params):
    global cglGetTextureParameterfv
    cglGetTextureParameterfv = <GL_GET_TEXTURE_PARAMETERFV>getFunction(b"glGetTextureParameterfv")
    cglGetTextureParameterfv(texture, pname, params)

cdef void GetglGetTextureParameterIiv(GLuint texture, GLenum pname, GLint *params):
    global cglGetTextureParameterIiv
    cglGetTextureParameterIiv = <GL_GET_TEXTURE_PARAMETER_IIV>getFunction(b"glGetTextureParameterIiv")
    cglGetTextureParameterIiv(texture, pname, params)

cdef void GetglGetTextureParameterIuiv(GLuint texture, GLenum pname, GLuint *params):
    global cglGetTextureParameterIuiv
    cglGetTextureParameterIuiv = <GL_GET_TEXTURE_PARAMETER_IUIV>getFunction(b"glGetTextureParameterIuiv")
    cglGetTextureParameterIuiv(texture, pname, params)

cdef void GetglGetTextureParameteriv(GLuint texture, GLenum pname, GLint *params):
    global cglGetTextureParameteriv
    cglGetTextureParameteriv = <GL_GET_TEXTURE_PARAMETERIV>getFunction(b"glGetTextureParameteriv")
    cglGetTextureParameteriv(texture, pname, params)

cdef void GetglCreateVertexArrays(GLsizei n, GLuint *arrays):
    global cglCreateVertexArrays
    cglCreateVertexArrays = <GL_CREATE_VERTEX_ARRAYS>getFunction(b"glCreateVertexArrays")
    cglCreateVertexArrays(n, arrays)

cdef void GetglDisableVertexArrayAttrib(GLuint vaobj, GLuint index):
    global cglDisableVertexArrayAttrib
    cglDisableVertexArrayAttrib = <GL_DISABLE_VERTEX_ARRAY_ATTRIB>getFunction(b"glDisableVertexArrayAttrib")
    cglDisableVertexArrayAttrib(vaobj, index)

cdef void GetglEnableVertexArrayAttrib(GLuint vaobj, GLuint index):
    global cglEnableVertexArrayAttrib
    cglEnableVertexArrayAttrib = <GL_ENABLE_VERTEX_ARRAY_ATTRIB>getFunction(b"glEnableVertexArrayAttrib")
    cglEnableVertexArrayAttrib(vaobj, index)

cdef void GetglVertexArrayElementBuffer(GLuint vaobj, GLuint buffer):
    global cglVertexArrayElementBuffer
    cglVertexArrayElementBuffer = <GL_VERTEX_ARRAY_ELEMENT_BUFFER>getFunction(b"glVertexArrayElementBuffer")
    cglVertexArrayElementBuffer(vaobj, buffer)

cdef void GetglVertexArrayVertexBuffer(GLuint vaobj, GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride):
    global cglVertexArrayVertexBuffer
    cglVertexArrayVertexBuffer = <GL_VERTEX_ARRAY_VERTEX_BUFFER>getFunction(b"glVertexArrayVertexBuffer")
    cglVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride)

cdef void GetglVertexArrayVertexBuffers(GLuint vaobj, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides):
    global cglVertexArrayVertexBuffers
    cglVertexArrayVertexBuffers = <GL_VERTEX_ARRAY_VERTEX_BUFFERS>getFunction(b"glVertexArrayVertexBuffers")
    cglVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides)

cdef void GetglVertexArrayAttribBinding(GLuint vaobj, GLuint attribindex, GLuint bindingindex):
    global cglVertexArrayAttribBinding
    cglVertexArrayAttribBinding = <GL_VERTEX_ARRAY_ATTRIB_BINDING>getFunction(b"glVertexArrayAttribBinding")
    cglVertexArrayAttribBinding(vaobj, attribindex, bindingindex)

cdef void GetglVertexArrayAttribFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset):
    global cglVertexArrayAttribFormat
    cglVertexArrayAttribFormat = <GL_VERTEX_ARRAY_ATTRIB_FORMAT>getFunction(b"glVertexArrayAttribFormat")
    cglVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset)

cdef void GetglVertexArrayAttribIFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    global cglVertexArrayAttribIFormat
    cglVertexArrayAttribIFormat = <GL_VERTEX_ARRAY_ATTRIB_I_FORMAT>getFunction(b"glVertexArrayAttribIFormat")
    cglVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset)

cdef void GetglVertexArrayAttribLFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    global cglVertexArrayAttribLFormat
    cglVertexArrayAttribLFormat = <GL_VERTEX_ARRAY_ATTRIB_L_FORMAT>getFunction(b"glVertexArrayAttribLFormat")
    cglVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset)

cdef void GetglVertexArrayBindingDivisor(GLuint vaobj, GLuint bindingindex, GLuint divisor):
    global cglVertexArrayBindingDivisor
    cglVertexArrayBindingDivisor = <GL_VERTEX_ARRAY_BINDING_DIVISOR>getFunction(b"glVertexArrayBindingDivisor")
    cglVertexArrayBindingDivisor(vaobj, bindingindex, divisor)

cdef void GetglGetVertexArrayiv(GLuint vaobj, GLenum pname, GLint *param):
    global cglGetVertexArrayiv
    cglGetVertexArrayiv = <GL_GET_VERTEX_ARRAYIV>getFunction(b"glGetVertexArrayiv")
    cglGetVertexArrayiv(vaobj, pname, param)

cdef void GetglGetVertexArrayIndexediv(GLuint vaobj, GLuint index, GLenum pname, GLint *param):
    global cglGetVertexArrayIndexediv
    cglGetVertexArrayIndexediv = <GL_GET_VERTEX_ARRAY_INDEXEDIV>getFunction(b"glGetVertexArrayIndexediv")
    cglGetVertexArrayIndexediv(vaobj, index, pname, param)

cdef void GetglGetVertexArrayIndexed64iv(GLuint vaobj, GLuint index, GLenum pname, GLint64 *param):
    global cglGetVertexArrayIndexed64iv
    cglGetVertexArrayIndexed64iv = <GL_GET_VERTEX_ARRAY_INDEXED64IV>getFunction(b"glGetVertexArrayIndexed64iv")
    cglGetVertexArrayIndexed64iv(vaobj, index, pname, param)

cdef void GetglCreateSamplers(GLsizei n, GLuint *samplers):
    global cglCreateSamplers
    cglCreateSamplers = <GL_CREATE_SAMPLERS>getFunction(b"glCreateSamplers")
    cglCreateSamplers(n, samplers)

cdef void GetglCreateProgramPipelines(GLsizei n, GLuint *pipelines):
    global cglCreateProgramPipelines
    cglCreateProgramPipelines = <GL_CREATE_PROGRAM_PIPELINES>getFunction(b"glCreateProgramPipelines")
    cglCreateProgramPipelines(n, pipelines)

cdef void GetglCreateQueries(GLenum target, GLsizei n, GLuint *ids):
    global cglCreateQueries
    cglCreateQueries = <GL_CREATE_QUERIES>getFunction(b"glCreateQueries")
    cglCreateQueries(target, n, ids)

cdef void GetglGetQueryBufferObjecti64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    global cglGetQueryBufferObjecti64v
    cglGetQueryBufferObjecti64v = <GL_GET_QUERY_BUFFER_OBJECTI64V>getFunction(b"glGetQueryBufferObjecti64v")
    cglGetQueryBufferObjecti64v(id, buffer, pname, offset)

cdef void GetglGetQueryBufferObjectiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    global cglGetQueryBufferObjectiv
    cglGetQueryBufferObjectiv = <GL_GET_QUERY_BUFFER_OBJECTIV>getFunction(b"glGetQueryBufferObjectiv")
    cglGetQueryBufferObjectiv(id, buffer, pname, offset)

cdef void GetglGetQueryBufferObjectui64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    global cglGetQueryBufferObjectui64v
    cglGetQueryBufferObjectui64v = <GL_GET_QUERY_BUFFER_OBJECTUI64V>getFunction(b"glGetQueryBufferObjectui64v")
    cglGetQueryBufferObjectui64v(id, buffer, pname, offset)

cdef void GetglGetQueryBufferObjectuiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    global cglGetQueryBufferObjectuiv
    cglGetQueryBufferObjectuiv = <GL_GET_QUERY_BUFFER_OBJECTUIV>getFunction(b"glGetQueryBufferObjectuiv")
    cglGetQueryBufferObjectuiv(id, buffer, pname, offset)

cdef void GetglMemoryBarrierByRegion(GLbitfield barriers):
    global cglMemoryBarrierByRegion
    cglMemoryBarrierByRegion = <GL_MEMORY_BARRIER_BY_REGION>getFunction(b"glMemoryBarrierByRegion")
    cglMemoryBarrierByRegion(barriers)

cdef void GetglGetTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    global cglGetTextureSubImage
    cglGetTextureSubImage = <GL_GET_TEXTURE_SUB_IMAGE>getFunction(b"glGetTextureSubImage")
    cglGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize, pixels)

cdef void GetglGetCompressedTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei bufSize, void *pixels):
    global cglGetCompressedTextureSubImage
    cglGetCompressedTextureSubImage = <GL_GET_COMPRESSED_TEXTURE_SUB_IMAGE>getFunction(b"glGetCompressedTextureSubImage")
    cglGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize, pixels)

cdef GLenum GetglGetGraphicsResetStatus():
    global cglGetGraphicsResetStatus
    cglGetGraphicsResetStatus = <GL_GET_GRAPHICS_RESET_STATUS>getFunction(b"glGetGraphicsResetStatus")
    cglGetGraphicsResetStatus()

cdef void GetglGetnCompressedTexImage(GLenum target, GLint lod, GLsizei bufSize, void *pixels):
    global cglGetnCompressedTexImage
    cglGetnCompressedTexImage = <GL_GETN_COMPRESSED_TEX_IMAGE>getFunction(b"glGetnCompressedTexImage")
    cglGetnCompressedTexImage(target, lod, bufSize, pixels)

cdef void GetglGetnTexImage(GLenum target, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    global cglGetnTexImage
    cglGetnTexImage = <GL_GETN_TEX_IMAGE>getFunction(b"glGetnTexImage")
    cglGetnTexImage(target, level, format, type, bufSize, pixels)

cdef void GetglGetnUniformdv(GLuint program, GLint location, GLsizei bufSize, GLdouble *params):
    global cglGetnUniformdv
    cglGetnUniformdv = <GL_GETN_UNIFORMDV>getFunction(b"glGetnUniformdv")
    cglGetnUniformdv(program, location, bufSize, params)

cdef void GetglGetnUniformfv(GLuint program, GLint location, GLsizei bufSize, GLfloat *params):
    global cglGetnUniformfv
    cglGetnUniformfv = <GL_GETN_UNIFORMFV>getFunction(b"glGetnUniformfv")
    cglGetnUniformfv(program, location, bufSize, params)

cdef void GetglGetnUniformiv(GLuint program, GLint location, GLsizei bufSize, GLint *params):
    global cglGetnUniformiv
    cglGetnUniformiv = <GL_GETN_UNIFORMIV>getFunction(b"glGetnUniformiv")
    cglGetnUniformiv(program, location, bufSize, params)

cdef void GetglGetnUniformuiv(GLuint program, GLint location, GLsizei bufSize, GLuint *params):
    global cglGetnUniformuiv
    cglGetnUniformuiv = <GL_GETN_UNIFORMUIV>getFunction(b"glGetnUniformuiv")
    cglGetnUniformuiv(program, location, bufSize, params)

cdef void GetglReadnPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei bufSize, void *data):
    global cglReadnPixels
    cglReadnPixels = <GL_READN_PIXELS>getFunction(b"glReadnPixels")
    cglReadnPixels(x, y, width, height, format, type, bufSize, data)

cdef void GetglGetnMapdv(GLenum target, GLenum query, GLsizei bufSize, GLdouble *v):
    global cglGetnMapdv
    cglGetnMapdv = <GL_GETN_MAPDV>getFunction(b"glGetnMapdv")
    cglGetnMapdv(target, query, bufSize, v)

cdef void GetglGetnMapfv(GLenum target, GLenum query, GLsizei bufSize, GLfloat *v):
    global cglGetnMapfv
    cglGetnMapfv = <GL_GETN_MAPFV>getFunction(b"glGetnMapfv")
    cglGetnMapfv(target, query, bufSize, v)

cdef void GetglGetnMapiv(GLenum target, GLenum query, GLsizei bufSize, GLint *v):
    global cglGetnMapiv
    cglGetnMapiv = <GL_GETN_MAPIV>getFunction(b"glGetnMapiv")
    cglGetnMapiv(target, query, bufSize, v)

cdef void GetglGetnPixelMapfv(GLenum map, GLsizei bufSize, GLfloat *values):
    global cglGetnPixelMapfv
    cglGetnPixelMapfv = <GL_GETN_PIXEL_MAPFV>getFunction(b"glGetnPixelMapfv")
    cglGetnPixelMapfv(map, bufSize, values)

cdef void GetglGetnPixelMapuiv(GLenum map, GLsizei bufSize, GLuint *values):
    global cglGetnPixelMapuiv
    cglGetnPixelMapuiv = <GL_GETN_PIXEL_MAPUIV>getFunction(b"glGetnPixelMapuiv")
    cglGetnPixelMapuiv(map, bufSize, values)

cdef void GetglGetnPixelMapusv(GLenum map, GLsizei bufSize, GLushort *values):
    global cglGetnPixelMapusv
    cglGetnPixelMapusv = <GL_GETN_PIXEL_MAPUSV>getFunction(b"glGetnPixelMapusv")
    cglGetnPixelMapusv(map, bufSize, values)

cdef void GetglGetnPolygonStipple(GLsizei bufSize, GLubyte *pattern):
    global cglGetnPolygonStipple
    cglGetnPolygonStipple = <GL_GETN_POLYGON_STIPPLE>getFunction(b"glGetnPolygonStipple")
    cglGetnPolygonStipple(bufSize, pattern)

cdef void GetglGetnColorTable(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *table):
    global cglGetnColorTable
    cglGetnColorTable = <GL_GETN_COLOR_TABLE>getFunction(b"glGetnColorTable")
    cglGetnColorTable(target, format, type, bufSize, table)

cdef void GetglGetnConvolutionFilter(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *image):
    global cglGetnConvolutionFilter
    cglGetnConvolutionFilter = <GL_GETN_CONVOLUTION_FILTER>getFunction(b"glGetnConvolutionFilter")
    cglGetnConvolutionFilter(target, format, type, bufSize, image)

cdef void GetglGetnSeparableFilter(GLenum target, GLenum format, GLenum type, GLsizei rowBufSize, void *row, GLsizei columnBufSize, void *column, void *span):
    global cglGetnSeparableFilter
    cglGetnSeparableFilter = <GL_GETN_SEPARABLE_FILTER>getFunction(b"glGetnSeparableFilter")
    cglGetnSeparableFilter(target, format, type, rowBufSize, row, columnBufSize, column, span)

cdef void GetglGetnHistogram(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values):
    global cglGetnHistogram
    cglGetnHistogram = <GL_GETN_HISTOGRAM>getFunction(b"glGetnHistogram")
    cglGetnHistogram(target, reset, format, type, bufSize, values)

cdef void GetglGetnMinmax(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values):
    global cglGetnMinmax
    cglGetnMinmax = <GL_GETN_MINMAX>getFunction(b"glGetnMinmax")
    cglGetnMinmax(target, reset, format, type, bufSize, values)

cdef void GetglTextureBarrier():
    global cglTextureBarrier
    cglTextureBarrier = <GL_TEXTURE_BARRIER>getFunction(b"glTextureBarrier")
    cglTextureBarrier()

cglClipControl = GetglClipControl
cglCreateTransformFeedbacks = GetglCreateTransformFeedbacks
cglTransformFeedbackBufferBase = GetglTransformFeedbackBufferBase
cglTransformFeedbackBufferRange = GetglTransformFeedbackBufferRange
cglGetTransformFeedbackiv = GetglGetTransformFeedbackiv
cglGetTransformFeedbacki_v = GetglGetTransformFeedbacki_v
cglGetTransformFeedbacki64_v = GetglGetTransformFeedbacki64_v
cglCreateBuffers = GetglCreateBuffers
cglNamedBufferStorage = GetglNamedBufferStorage
cglNamedBufferData = GetglNamedBufferData
cglNamedBufferSubData = GetglNamedBufferSubData
cglCopyNamedBufferSubData = GetglCopyNamedBufferSubData
cglClearNamedBufferData = GetglClearNamedBufferData
cglClearNamedBufferSubData = GetglClearNamedBufferSubData
cglMapNamedBuffer = GetglMapNamedBuffer
cglMapNamedBufferRange = GetglMapNamedBufferRange
cglUnmapNamedBuffer = GetglUnmapNamedBuffer
cglFlushMappedNamedBufferRange = GetglFlushMappedNamedBufferRange
cglGetNamedBufferParameteriv = GetglGetNamedBufferParameteriv
cglGetNamedBufferParameteri64v = GetglGetNamedBufferParameteri64v
cglGetNamedBufferPointerv = GetglGetNamedBufferPointerv
cglGetNamedBufferSubData = GetglGetNamedBufferSubData
cglCreateFramebuffers = GetglCreateFramebuffers
cglNamedFramebufferRenderbuffer = GetglNamedFramebufferRenderbuffer
cglNamedFramebufferParameteri = GetglNamedFramebufferParameteri
cglNamedFramebufferTexture = GetglNamedFramebufferTexture
cglNamedFramebufferTextureLayer = GetglNamedFramebufferTextureLayer
cglNamedFramebufferDrawBuffer = GetglNamedFramebufferDrawBuffer
cglNamedFramebufferDrawBuffers = GetglNamedFramebufferDrawBuffers
cglNamedFramebufferReadBuffer = GetglNamedFramebufferReadBuffer
cglInvalidateNamedFramebufferData = GetglInvalidateNamedFramebufferData
cglInvalidateNamedFramebufferSubData = GetglInvalidateNamedFramebufferSubData
cglClearNamedFramebufferiv = GetglClearNamedFramebufferiv
cglClearNamedFramebufferuiv = GetglClearNamedFramebufferuiv
cglClearNamedFramebufferfv = GetglClearNamedFramebufferfv
cglClearNamedFramebufferfi = GetglClearNamedFramebufferfi
cglBlitNamedFramebuffer = GetglBlitNamedFramebuffer
cglCheckNamedFramebufferStatus = GetglCheckNamedFramebufferStatus
cglGetNamedFramebufferParameteriv = GetglGetNamedFramebufferParameteriv
cglGetNamedFramebufferAttachmentParameteriv = GetglGetNamedFramebufferAttachmentParameteriv
cglCreateRenderbuffers = GetglCreateRenderbuffers
cglNamedRenderbufferStorage = GetglNamedRenderbufferStorage
cglNamedRenderbufferStorageMultisample = GetglNamedRenderbufferStorageMultisample
cglGetNamedRenderbufferParameteriv = GetglGetNamedRenderbufferParameteriv
cglCreateTextures = GetglCreateTextures
cglTextureBuffer = GetglTextureBuffer
cglTextureBufferRange = GetglTextureBufferRange
cglTextureStorage1D = GetglTextureStorage1D
cglTextureStorage2D = GetglTextureStorage2D
cglTextureStorage3D = GetglTextureStorage3D
cglTextureStorage2DMultisample = GetglTextureStorage2DMultisample
cglTextureStorage3DMultisample = GetglTextureStorage3DMultisample
cglTextureSubImage1D = GetglTextureSubImage1D
cglTextureSubImage2D = GetglTextureSubImage2D
cglTextureSubImage3D = GetglTextureSubImage3D
cglCompressedTextureSubImage1D = GetglCompressedTextureSubImage1D
cglCompressedTextureSubImage2D = GetglCompressedTextureSubImage2D
cglCompressedTextureSubImage3D = GetglCompressedTextureSubImage3D
cglCopyTextureSubImage1D = GetglCopyTextureSubImage1D
cglCopyTextureSubImage2D = GetglCopyTextureSubImage2D
cglCopyTextureSubImage3D = GetglCopyTextureSubImage3D
cglTextureParameterf = GetglTextureParameterf
cglTextureParameterfv = GetglTextureParameterfv
cglTextureParameteri = GetglTextureParameteri
cglTextureParameterIiv = GetglTextureParameterIiv
cglTextureParameterIuiv = GetglTextureParameterIuiv
cglTextureParameteriv = GetglTextureParameteriv
cglGenerateTextureMipmap = GetglGenerateTextureMipmap
cglBindTextureUnit = GetglBindTextureUnit
cglGetTextureImage = GetglGetTextureImage
cglGetCompressedTextureImage = GetglGetCompressedTextureImage
cglGetTextureLevelParameterfv = GetglGetTextureLevelParameterfv
cglGetTextureLevelParameteriv = GetglGetTextureLevelParameteriv
cglGetTextureParameterfv = GetglGetTextureParameterfv
cglGetTextureParameterIiv = GetglGetTextureParameterIiv
cglGetTextureParameterIuiv = GetglGetTextureParameterIuiv
cglGetTextureParameteriv = GetglGetTextureParameteriv
cglCreateVertexArrays = GetglCreateVertexArrays
cglDisableVertexArrayAttrib = GetglDisableVertexArrayAttrib
cglEnableVertexArrayAttrib = GetglEnableVertexArrayAttrib
cglVertexArrayElementBuffer = GetglVertexArrayElementBuffer
cglVertexArrayVertexBuffer = GetglVertexArrayVertexBuffer
cglVertexArrayVertexBuffers = GetglVertexArrayVertexBuffers
cglVertexArrayAttribBinding = GetglVertexArrayAttribBinding
cglVertexArrayAttribFormat = GetglVertexArrayAttribFormat
cglVertexArrayAttribIFormat = GetglVertexArrayAttribIFormat
cglVertexArrayAttribLFormat = GetglVertexArrayAttribLFormat
cglVertexArrayBindingDivisor = GetglVertexArrayBindingDivisor
cglGetVertexArrayiv = GetglGetVertexArrayiv
cglGetVertexArrayIndexediv = GetglGetVertexArrayIndexediv
cglGetVertexArrayIndexed64iv = GetglGetVertexArrayIndexed64iv
cglCreateSamplers = GetglCreateSamplers
cglCreateProgramPipelines = GetglCreateProgramPipelines
cglCreateQueries = GetglCreateQueries
cglGetQueryBufferObjecti64v = GetglGetQueryBufferObjecti64v
cglGetQueryBufferObjectiv = GetglGetQueryBufferObjectiv
cglGetQueryBufferObjectui64v = GetglGetQueryBufferObjectui64v
cglGetQueryBufferObjectuiv = GetglGetQueryBufferObjectuiv
cglMemoryBarrierByRegion = GetglMemoryBarrierByRegion
cglGetTextureSubImage = GetglGetTextureSubImage
cglGetCompressedTextureSubImage = GetglGetCompressedTextureSubImage
cglGetGraphicsResetStatus = GetglGetGraphicsResetStatus
cglGetnCompressedTexImage = GetglGetnCompressedTexImage
cglGetnTexImage = GetglGetnTexImage
cglGetnUniformdv = GetglGetnUniformdv
cglGetnUniformfv = GetglGetnUniformfv
cglGetnUniformiv = GetglGetnUniformiv
cglGetnUniformuiv = GetglGetnUniformuiv
cglReadnPixels = GetglReadnPixels
cglGetnMapdv = GetglGetnMapdv
cglGetnMapfv = GetglGetnMapfv
cglGetnMapiv = GetglGetnMapiv
cglGetnPixelMapfv = GetglGetnPixelMapfv
cglGetnPixelMapuiv = GetglGetnPixelMapuiv
cglGetnPixelMapusv = GetglGetnPixelMapusv
cglGetnPolygonStipple = GetglGetnPolygonStipple
cglGetnColorTable = GetglGetnColorTable
cglGetnConvolutionFilter = GetglGetnConvolutionFilter
cglGetnSeparableFilter = GetglGetnSeparableFilter
cglGetnHistogram = GetglGetnHistogram
cglGetnMinmax = GetglGetnMinmax
cglTextureBarrier = GetglTextureBarrier


cpdef void glClipControl(GLenum origin, GLenum depth):
    cglClipControl(origin, depth)

cpdef void glCreateTransformFeedbacks(GLsizei n, GLuint *ids):
    cglCreateTransformFeedbacks(n, ids)

cpdef void glTransformFeedbackBufferBase(GLuint xfb, GLuint index, GLuint buffer):
    cglTransformFeedbackBufferBase(xfb, index, buffer)

cpdef void glTransformFeedbackBufferRange(GLuint xfb, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size):
    cglTransformFeedbackBufferRange(xfb, index, buffer, offset, size)

cpdef void glGetTransformFeedbackiv(GLuint xfb, GLenum pname, GLint *param):
    cglGetTransformFeedbackiv(xfb, pname, param)

cpdef void glGetTransformFeedbacki_v(GLuint xfb, GLenum pname, GLuint index, GLint *param):
    cglGetTransformFeedbacki_v(xfb, pname, index, param)

cpdef void glGetTransformFeedbacki64_v(GLuint xfb, GLenum pname, GLuint index, GLint64 *param):
    cglGetTransformFeedbacki64_v(xfb, pname, index, param)

cpdef void glCreateBuffers(GLsizei n, GLuint *buffers):
    cglCreateBuffers(n, buffers)

cpdef void glNamedBufferStorage(GLuint buffer, GLsizeiptr size, const void *data, GLbitfield flags):
    cglNamedBufferStorage(buffer, size, data, flags)

cpdef void glNamedBufferData(GLuint buffer, GLsizeiptr size, const void *data, GLenum usage):
    cglNamedBufferData(buffer, size, data, usage)

cpdef void glNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, const void *data):
    cglNamedBufferSubData(buffer, offset, size, data)

cpdef void glCopyNamedBufferSubData(GLuint readBuffer, GLuint writeBuffer, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size):
    cglCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size)

cpdef void glClearNamedBufferData(GLuint buffer, GLenum internalformat, GLenum format, GLenum type, const void *data):
    cglClearNamedBufferData(buffer, internalformat, format, type, data)

cpdef void glClearNamedBufferSubData(GLuint buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data):
    cglClearNamedBufferSubData(buffer, internalformat, offset, size, format, type, data)

cpdef void *glMapNamedBuffer(GLuint buffer, GLenum access):
    cglMapNamedBuffer(buffer, access)

cpdef void *glMapNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length, GLbitfield access):
    cglMapNamedBufferRange(buffer, offset, length, access)

cpdef GLboolean glUnmapNamedBuffer(GLuint buffer):
    cglUnmapNamedBuffer(buffer)

cpdef void glFlushMappedNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length):
    cglFlushMappedNamedBufferRange(buffer, offset, length)

cpdef void glGetNamedBufferParameteriv(GLuint buffer, GLenum pname, GLint *params):
    cglGetNamedBufferParameteriv(buffer, pname, params)

cpdef void glGetNamedBufferParameteri64v(GLuint buffer, GLenum pname, GLint64 *params):
    cglGetNamedBufferParameteri64v(buffer, pname, params)

cpdef void glGetNamedBufferPointerv(GLuint buffer, GLenum pname, void **params):
    cglGetNamedBufferPointerv(buffer, pname, params)

cpdef void glGetNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, void *data):
    cglGetNamedBufferSubData(buffer, offset, size, data)

cpdef void glCreateFramebuffers(GLsizei n, GLuint *framebuffers):
    cglCreateFramebuffers(n, framebuffers)

cpdef void glNamedFramebufferRenderbuffer(GLuint framebuffer, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer):
    cglNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer)

cpdef void glNamedFramebufferParameteri(GLuint framebuffer, GLenum pname, GLint param):
    cglNamedFramebufferParameteri(framebuffer, pname, param)

cpdef void glNamedFramebufferTexture(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level):
    cglNamedFramebufferTexture(framebuffer, attachment, texture, level)

cpdef void glNamedFramebufferTextureLayer(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level, GLint layer):
    cglNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer)

cpdef void glNamedFramebufferDrawBuffer(GLuint framebuffer, GLenum buf):
    cglNamedFramebufferDrawBuffer(framebuffer, buf)

cpdef void glNamedFramebufferDrawBuffers(GLuint framebuffer, GLsizei n, const GLenum *bufs):
    cglNamedFramebufferDrawBuffers(framebuffer, n, bufs)

cpdef void glNamedFramebufferReadBuffer(GLuint framebuffer, GLenum src):
    cglNamedFramebufferReadBuffer(framebuffer, src)

cpdef void glInvalidateNamedFramebufferData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments):
    cglInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments)

cpdef void glInvalidateNamedFramebufferSubData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height):
    cglInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height)

cpdef void glClearNamedFramebufferiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLint *value):
    cglClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value)

cpdef void glClearNamedFramebufferuiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLuint *value):
    cglClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value)

cpdef void glClearNamedFramebufferfv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat *value):
    cglClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value)

cpdef void glClearNamedFramebufferfi(GLuint framebuffer, GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil):
    cglClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil)

cpdef void glBlitNamedFramebuffer(GLuint readFramebuffer, GLuint drawFramebuffer, GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter):
    cglBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)

cpdef GLenum glCheckNamedFramebufferStatus(GLuint framebuffer, GLenum target):
    cglCheckNamedFramebufferStatus(framebuffer, target)

cpdef void glGetNamedFramebufferParameteriv(GLuint framebuffer, GLenum pname, GLint *param):
    cglGetNamedFramebufferParameteriv(framebuffer, pname, param)

cpdef void glGetNamedFramebufferAttachmentParameteriv(GLuint framebuffer, GLenum attachment, GLenum pname, GLint *params):
    cglGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname, params)

cpdef void glCreateRenderbuffers(GLsizei n, GLuint *renderbuffers):
    cglCreateRenderbuffers(n, renderbuffers)

cpdef void glNamedRenderbufferStorage(GLuint renderbuffer, GLenum internalformat, GLsizei width, GLsizei height):
    cglNamedRenderbufferStorage(renderbuffer, internalformat, width, height)

cpdef void glNamedRenderbufferStorageMultisample(GLuint renderbuffer, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height):
    cglNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height)

cpdef void glGetNamedRenderbufferParameteriv(GLuint renderbuffer, GLenum pname, GLint *params):
    cglGetNamedRenderbufferParameteriv(renderbuffer, pname, params)

cpdef void glCreateTextures(GLenum target, GLsizei n, GLuint *textures):
    cglCreateTextures(target, n, textures)

cpdef void glTextureBuffer(GLuint texture, GLenum internalformat, GLuint buffer):
    cglTextureBuffer(texture, internalformat, buffer)

cpdef void glTextureBufferRange(GLuint texture, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size):
    cglTextureBufferRange(texture, internalformat, buffer, offset, size)

cpdef void glTextureStorage1D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width):
    cglTextureStorage1D(texture, levels, internalformat, width)

cpdef void glTextureStorage2D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height):
    cglTextureStorage2D(texture, levels, internalformat, width, height)

cpdef void glTextureStorage3D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth):
    cglTextureStorage3D(texture, levels, internalformat, width, height, depth)

cpdef void glTextureStorage2DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    cglTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations)

cpdef void glTextureStorage3DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    cglTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations)

cpdef void glTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels):
    cglTextureSubImage1D(texture, level, xoffset, width, format, type, pixels)

cpdef void glTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    cglTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type, pixels)

cpdef void glTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels):
    cglTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)

cpdef void glCompressedTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize, data)

cpdef void glCompressedTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize, data)

cpdef void glCompressedTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

cpdef void glCopyTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width):
    cglCopyTextureSubImage1D(texture, level, xoffset, x, y, width)

cpdef void glCopyTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    cglCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height)

cpdef void glCopyTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    cglCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height)

cpdef void glTextureParameterf(GLuint texture, GLenum pname, GLfloat param):
    cglTextureParameterf(texture, pname, param)

cpdef void glTextureParameterfv(GLuint texture, GLenum pname, const GLfloat *param):
    cglTextureParameterfv(texture, pname, param)

cpdef void glTextureParameteri(GLuint texture, GLenum pname, GLint param):
    cglTextureParameteri(texture, pname, param)

cpdef void glTextureParameterIiv(GLuint texture, GLenum pname, const GLint *params):
    cglTextureParameterIiv(texture, pname, params)

cpdef void glTextureParameterIuiv(GLuint texture, GLenum pname, const GLuint *params):
    cglTextureParameterIuiv(texture, pname, params)

cpdef void glTextureParameteriv(GLuint texture, GLenum pname, const GLint *param):
    cglTextureParameteriv(texture, pname, param)

cpdef void glGenerateTextureMipmap(GLuint texture):
    cglGenerateTextureMipmap(texture)

cpdef void glBindTextureUnit(GLuint unit, GLuint texture):
    cglBindTextureUnit(unit, texture)

cpdef void glGetTextureImage(GLuint texture, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    cglGetTextureImage(texture, level, format, type, bufSize, pixels)

cpdef void glGetCompressedTextureImage(GLuint texture, GLint level, GLsizei bufSize, void *pixels):
    cglGetCompressedTextureImage(texture, level, bufSize, pixels)

cpdef void glGetTextureLevelParameterfv(GLuint texture, GLint level, GLenum pname, GLfloat *params):
    cglGetTextureLevelParameterfv(texture, level, pname, params)

cpdef void glGetTextureLevelParameteriv(GLuint texture, GLint level, GLenum pname, GLint *params):
    cglGetTextureLevelParameteriv(texture, level, pname, params)

cpdef void glGetTextureParameterfv(GLuint texture, GLenum pname, GLfloat *params):
    cglGetTextureParameterfv(texture, pname, params)

cpdef void glGetTextureParameterIiv(GLuint texture, GLenum pname, GLint *params):
    cglGetTextureParameterIiv(texture, pname, params)

cpdef void glGetTextureParameterIuiv(GLuint texture, GLenum pname, GLuint *params):
    cglGetTextureParameterIuiv(texture, pname, params)

cpdef void glGetTextureParameteriv(GLuint texture, GLenum pname, GLint *params):
    cglGetTextureParameteriv(texture, pname, params)

cpdef void glCreateVertexArrays(GLsizei n, GLuint *arrays):
    cglCreateVertexArrays(n, arrays)

cpdef void glDisableVertexArrayAttrib(GLuint vaobj, GLuint index):
    cglDisableVertexArrayAttrib(vaobj, index)

cpdef void glEnableVertexArrayAttrib(GLuint vaobj, GLuint index):
    cglEnableVertexArrayAttrib(vaobj, index)

cpdef void glVertexArrayElementBuffer(GLuint vaobj, GLuint buffer):
    cglVertexArrayElementBuffer(vaobj, buffer)

cpdef void glVertexArrayVertexBuffer(GLuint vaobj, GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride):
    cglVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride)

cpdef void glVertexArrayVertexBuffers(GLuint vaobj, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides):
    cglVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides)

cpdef void glVertexArrayAttribBinding(GLuint vaobj, GLuint attribindex, GLuint bindingindex):
    cglVertexArrayAttribBinding(vaobj, attribindex, bindingindex)

cpdef void glVertexArrayAttribFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset):
    cglVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset)

cpdef void glVertexArrayAttribIFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    cglVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset)

cpdef void glVertexArrayAttribLFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    cglVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset)

cpdef void glVertexArrayBindingDivisor(GLuint vaobj, GLuint bindingindex, GLuint divisor):
    cglVertexArrayBindingDivisor(vaobj, bindingindex, divisor)

cpdef void glGetVertexArrayiv(GLuint vaobj, GLenum pname, GLint *param):
    cglGetVertexArrayiv(vaobj, pname, param)

cpdef void glGetVertexArrayIndexediv(GLuint vaobj, GLuint index, GLenum pname, GLint *param):
    cglGetVertexArrayIndexediv(vaobj, index, pname, param)

cpdef void glGetVertexArrayIndexed64iv(GLuint vaobj, GLuint index, GLenum pname, GLint64 *param):
    cglGetVertexArrayIndexed64iv(vaobj, index, pname, param)

cpdef void glCreateSamplers(GLsizei n, GLuint *samplers):
    cglCreateSamplers(n, samplers)

cpdef void glCreateProgramPipelines(GLsizei n, GLuint *pipelines):
    cglCreateProgramPipelines(n, pipelines)

cpdef void glCreateQueries(GLenum target, GLsizei n, GLuint *ids):
    cglCreateQueries(target, n, ids)

cpdef void glGetQueryBufferObjecti64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    cglGetQueryBufferObjecti64v(id, buffer, pname, offset)

cpdef void glGetQueryBufferObjectiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    cglGetQueryBufferObjectiv(id, buffer, pname, offset)

cpdef void glGetQueryBufferObjectui64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    cglGetQueryBufferObjectui64v(id, buffer, pname, offset)

cpdef void glGetQueryBufferObjectuiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    cglGetQueryBufferObjectuiv(id, buffer, pname, offset)

cpdef void glMemoryBarrierByRegion(GLbitfield barriers):
    cglMemoryBarrierByRegion(barriers)

cpdef void glGetTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    cglGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize, pixels)

cpdef void glGetCompressedTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei bufSize, void *pixels):
    cglGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize, pixels)

cpdef GLenum glGetGraphicsResetStatus():
    cglGetGraphicsResetStatus()

cpdef void glGetnCompressedTexImage(GLenum target, GLint lod, GLsizei bufSize, void *pixels):
    cglGetnCompressedTexImage(target, lod, bufSize, pixels)

cpdef void glGetnTexImage(GLenum target, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    cglGetnTexImage(target, level, format, type, bufSize, pixels)

cpdef void glGetnUniformdv(GLuint program, GLint location, GLsizei bufSize, GLdouble *params):
    cglGetnUniformdv(program, location, bufSize, params)

cpdef void glGetnUniformfv(GLuint program, GLint location, GLsizei bufSize, GLfloat *params):
    cglGetnUniformfv(program, location, bufSize, params)

cpdef void glGetnUniformiv(GLuint program, GLint location, GLsizei bufSize, GLint *params):
    cglGetnUniformiv(program, location, bufSize, params)

cpdef void glGetnUniformuiv(GLuint program, GLint location, GLsizei bufSize, GLuint *params):
    cglGetnUniformuiv(program, location, bufSize, params)

cpdef void glReadnPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei bufSize, void *data):
    cglReadnPixels(x, y, width, height, format, type, bufSize, data)

cpdef void glGetnMapdv(GLenum target, GLenum query, GLsizei bufSize, GLdouble *v):
    cglGetnMapdv(target, query, bufSize, v)

cpdef void glGetnMapfv(GLenum target, GLenum query, GLsizei bufSize, GLfloat *v):
    cglGetnMapfv(target, query, bufSize, v)

cpdef void glGetnMapiv(GLenum target, GLenum query, GLsizei bufSize, GLint *v):
    cglGetnMapiv(target, query, bufSize, v)

cpdef void glGetnPixelMapfv(GLenum map, GLsizei bufSize, GLfloat *values):
    cglGetnPixelMapfv(map, bufSize, values)

cpdef void glGetnPixelMapuiv(GLenum map, GLsizei bufSize, GLuint *values):
    cglGetnPixelMapuiv(map, bufSize, values)

cpdef void glGetnPixelMapusv(GLenum map, GLsizei bufSize, GLushort *values):
    cglGetnPixelMapusv(map, bufSize, values)

cpdef void glGetnPolygonStipple(GLsizei bufSize, GLubyte *pattern):
    cglGetnPolygonStipple(bufSize, pattern)

cpdef void glGetnColorTable(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *table):
    cglGetnColorTable(target, format, type, bufSize, table)

cpdef void glGetnConvolutionFilter(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *image):
    cglGetnConvolutionFilter(target, format, type, bufSize, image)

cpdef void glGetnSeparableFilter(GLenum target, GLenum format, GLenum type, GLsizei rowBufSize, void *row, GLsizei columnBufSize, void *column, void *span):
    cglGetnSeparableFilter(target, format, type, rowBufSize, row, columnBufSize, column, span)

cpdef void glGetnHistogram(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values):
    cglGetnHistogram(target, reset, format, type, bufSize, values)

cpdef void glGetnMinmax(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values):
    cglGetnMinmax(target, reset, format, type, bufSize, values)

cpdef void glTextureBarrier():
    cglTextureBarrier()
