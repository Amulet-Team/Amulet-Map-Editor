# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_TEXTURE_BINDING_BUFFER = 0x8C2C
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP_ARRAY = 0x900A
cdef GLenum GL_COLOR_TABLE = 0x80D0
cdef GLenum GL_POST_COLOR_MATRIX_COLOR_TABLE = 0x80D2
cdef GLenum GL_MINMAX = 0x802E
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE_ARRAY = 0x9105
cdef GLenum GL_NO_ERROR = 0
cdef GLenum GL_HISTOGRAM = 0x8024
cdef GLenum GL_NONE = 0
cdef GLenum GL_TEXTURE_BINDING_CUBE_MAP = 0x8514
cdef GLenum GL_CONTEXT_RELEASE_BEHAVIOR = 0x82FB
cdef GLenum GL_TEXTURE_BINDING_3D = 0x806A
cdef GLenum GL_TEXTURE_BINDING_1D_ARRAY = 0x8C1C
cdef GLenum GL_MAX_COMBINED_CLIP_AND_CULL_DISTANCES = 0x82FA
cdef GLenum GL_UNKNOWN_CONTEXT_RESET = 0x8255
cdef GLenum GL_CONVOLUTION_2D = 0x8011
cdef GLenum GL_PROXY_POST_COLOR_MATRIX_COLOR_TABLE = 0x80D5
cdef GLenum GL_LOWER_LEFT = 0x8CA1
cdef GLenum GL_QUERY_NO_WAIT_INVERTED = 0x8E18
cdef GLenum GL_TEXTURE_BINDING_2D = 0x8069
cdef GLenum GL_QUERY_TARGET = 0x82EA
cdef GLenum GL_QUERY_BY_REGION_WAIT_INVERTED = 0x8E19
cdef GLenum GL_TEXTURE_BINDING_2D_MULTISAMPLE = 0x9104
cdef GLenum GL_GUILTY_CONTEXT_RESET = 0x8253
cdef GLenum GL_NEGATIVE_ONE_TO_ONE = 0x935E
cdef GLenum GL_NO_RESET_NOTIFICATION = 0x8261
cdef GLenum GL_QUERY_BY_REGION_NO_WAIT_INVERTED = 0x8E1A
cdef GLenum GL_SEPARABLE_2D = 0x8012
cdef GLenum GL_BACK = 0x0405
cdef GLenum GL_UPPER_LEFT = 0x8CA2
cdef GLenum GL_PROXY_HISTOGRAM = 0x8025
cdef GLenum GL_MAX_CULL_DISTANCES = 0x82F9
cdef GLenum GL_CLIP_DEPTH_MODE = 0x935D
cdef GLenum GL_CLIP_ORIGIN = 0x935C
cdef GLenum GL_LOSE_CONTEXT_ON_RESET = 0x8252
cdef GLenum GL_CONTEXT_FLAG_ROBUST_ACCESS_BIT = 0x00000004
cdef GLenum GL_PROXY_COLOR_TABLE = 0x80D3
cdef GLenum GL_CONVOLUTION_1D = 0x8010
cdef GLenum GL_TEXTURE_TARGET = 0x1006
cdef GLenum GL_RESET_NOTIFICATION_STRATEGY = 0x8256
cdef GLenum GL_QUERY_WAIT_INVERTED = 0x8E17
cdef GLenum GL_ZERO_TO_ONE = 0x935F
cdef GLenum GL_TEXTURE_BINDING_RECTANGLE = 0x84F6
cdef GLenum GL_PROXY_POST_CONVOLUTION_COLOR_TABLE = 0x80D4
cdef GLenum GL_CONTEXT_LOST = 0x0507
cdef GLenum GL_TEXTURE_BINDING_2D_ARRAY = 0x8C1D
cdef GLenum GL_POST_CONVOLUTION_COLOR_TABLE = 0x80D1
cdef GLenum GL_INNOCENT_CONTEXT_RESET = 0x8254
cdef GLenum GL_CONTEXT_RELEASE_BEHAVIOR_FLUSH = 0x82FC
cdef GLenum GL_TEXTURE_BINDING_1D = 0x8068

ctypedef void (*PFNGLCREATESAMPLERSPROC)(GLsizei n, GLuint *samplers)
ctypedef void (*PFNGLVERTEXARRAYVERTEXBUFFERSPROC)(GLuint vaobj, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides)
ctypedef void (*PFNGLTEXTUREPARAMETERFPROC)(GLuint texture, GLenum pname, GLfloat param)
ctypedef void (*PFNGLCLEARNAMEDBUFFERDATAPROC)(GLuint buffer, GLenum internalformat, GLenum format, GLenum type, const void *data)
ctypedef void (*PFNGLVERTEXARRAYATTRIBFORMATPROC)(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset)
ctypedef void (*PFNGLGETNCONVOLUTIONFILTERPROC)(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *image)
ctypedef void (*PFNGLNAMEDFRAMEBUFFERDRAWBUFFERSPROC)(GLuint framebuffer, GLsizei n, const GLenum *bufs)
ctypedef void (*PFNGLNAMEDBUFFERDATAPROC)(GLuint buffer, GLsizeiptr size, const void *data, GLenum usage)
ctypedef void (*PFNGLBINDTEXTUREUNITPROC)(GLuint unit, GLuint texture)
ctypedef void (*PFNGLVERTEXARRAYATTRIBBINDINGPROC)(GLuint vaobj, GLuint attribindex, GLuint bindingindex)
ctypedef void (*PFNGLTEXTURESTORAGE2DMULTISAMPLEPROC)(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations)
ctypedef void (*PFNGLFLUSHMAPPEDNAMEDBUFFERRANGEPROC)(GLuint buffer, GLintptr offset, GLsizeiptr length)
ctypedef void (*PFNGLGETQUERYBUFFEROBJECTUI64VPROC)(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
ctypedef void (*PFNGLDISABLEVERTEXARRAYATTRIBPROC)(GLuint vaobj, GLuint index)
ctypedef void (*PFNGLGETTEXTURELEVELPARAMETERFVPROC)(GLuint texture, GLint level, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLCREATETRANSFORMFEEDBACKSPROC)(GLsizei n, GLuint *ids)
ctypedef void (*PFNGLCLEARNAMEDFRAMEBUFFERUIVPROC)(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLuint *value)
ctypedef void (*PFNGLGETNPIXELMAPFVPROC)(GLenum map, GLsizei bufSize, GLfloat *values)
ctypedef void (*PFNGLNAMEDFRAMEBUFFERREADBUFFERPROC)(GLuint framebuffer, GLenum src)
ctypedef void (*PFNGLCREATERENDERBUFFERSPROC)(GLsizei n, GLuint *renderbuffers)
ctypedef void (*PFNGLCREATEVERTEXARRAYSPROC)(GLsizei n, GLuint *arrays)
ctypedef void (*PFNGLGETNAMEDFRAMEBUFFERATTACHMENTPARAMETERIVPROC)(GLuint framebuffer, GLenum attachment, GLenum pname, GLint *params)
ctypedef void (*PFNGLNAMEDFRAMEBUFFERDRAWBUFFERPROC)(GLuint framebuffer, GLenum buf)
ctypedef void (*PFNGLCREATEBUFFERSPROC)(GLsizei n, GLuint *buffers)
ctypedef void (*PFNGLGETTEXTUREPARAMETERFVPROC)(GLuint texture, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLCOMPRESSEDTEXTURESUBIMAGE3DPROC)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*PFNGLTEXTUREBUFFERRANGEPROC)(GLuint texture, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size)
ctypedef void (*PFNGLTEXTUREBARRIERPROC)()
ctypedef void (*PFNGLTEXTUREPARAMETERFVPROC)(GLuint texture, GLenum pname, const GLfloat *param)
ctypedef void (*PFNGLINVALIDATENAMEDFRAMEBUFFERSUBDATAPROC)(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*PFNGLTEXTUREBUFFERPROC)(GLuint texture, GLenum internalformat, GLuint buffer)
ctypedef void (*PFNGLTEXTUREPARAMETERIPROC)(GLuint texture, GLenum pname, GLint param)
ctypedef void (*PFNGLTEXTURESUBIMAGE1DPROC)(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels)
ctypedef void (*PFNGLCOMPRESSEDTEXTURESUBIMAGE2DPROC)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*PFNGLGETNCOMPRESSEDTEXIMAGEPROC)(GLenum target, GLint lod, GLsizei bufSize, void *pixels)
ctypedef void (*PFNGLGETNTEXIMAGEPROC)(GLenum target, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
ctypedef GLenum (*PFNGLGETGRAPHICSRESETSTATUSPROC)()
ctypedef void (*PFNGLCREATEFRAMEBUFFERSPROC)(GLsizei n, GLuint *framebuffers)
ctypedef void (*PFNGLCREATEPROGRAMPIPELINESPROC)(GLsizei n, GLuint *pipelines)
ctypedef void (*PFNGLTEXTURESTORAGE2DPROC)(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height)
ctypedef void (*PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEPROC)(GLuint renderbuffer, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height)
ctypedef void (*PFNGLVERTEXARRAYBINDINGDIVISORPROC)(GLuint vaobj, GLuint bindingindex, GLuint divisor)
ctypedef void (*PFNGLGETVERTEXARRAYINDEXEDIVPROC)(GLuint vaobj, GLuint index, GLenum pname, GLint *param)
ctypedef void (*PFNGLGETNSEPARABLEFILTERPROC)(GLenum target, GLenum format, GLenum type, GLsizei rowBufSize, void *row, GLsizei columnBufSize, void *column, void *span)
ctypedef void (*PFNGLGETNCOLORTABLEPROC)(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *table)
ctypedef void (*PFNGLGETTEXTUREIMAGEPROC)(GLuint texture, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
ctypedef GLenum (*PFNGLCHECKNAMEDFRAMEBUFFERSTATUSPROC)(GLuint framebuffer, GLenum target)
ctypedef void (*PFNGLCLEARNAMEDFRAMEBUFFERFVPROC)(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat *value)
ctypedef void (*PFNGLGETNAMEDFRAMEBUFFERPARAMETERIVPROC)(GLuint framebuffer, GLenum pname, GLint *param)
ctypedef void (*PFNGLVERTEXARRAYELEMENTBUFFERPROC)(GLuint vaobj, GLuint buffer)
ctypedef void (*PFNGLTRANSFORMFEEDBACKBUFFERRANGEPROC)(GLuint xfb, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size)
ctypedef void (*PFNGLNAMEDFRAMEBUFFERPARAMETERIPROC)(GLuint framebuffer, GLenum pname, GLint param)
ctypedef void (*PFNGLMEMORYBARRIERBYREGIONPROC)(GLbitfield barriers)
ctypedef void (*PFNGLNAMEDBUFFERSTORAGEPROC)(GLuint buffer, GLsizeiptr size, const void *data, GLbitfield flags)
ctypedef void (*PFNGLGETNPOLYGONSTIPPLEPROC)(GLsizei bufSize, GLubyte *pattern)
ctypedef void (*PFNGLTEXTUREPARAMETERIVPROC)(GLuint texture, GLenum pname, const GLint *param)
ctypedef void (*PFNGLGETCOMPRESSEDTEXTUREIMAGEPROC)(GLuint texture, GLint level, GLsizei bufSize, void *pixels)
ctypedef void (*PFNGLTEXTUREPARAMETERIUIVPROC)(GLuint texture, GLenum pname, const GLuint *params)
ctypedef void (*PFNGLTEXTURESTORAGE1DPROC)(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width)
ctypedef void (*PFNGLGETNUNIFORMIVPROC)(GLuint program, GLint location, GLsizei bufSize, GLint *params)
ctypedef void (*PFNGLGETTEXTURESUBIMAGEPROC)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLsizei bufSize, void *pixels)
ctypedef void (*PFNGLBLITNAMEDFRAMEBUFFERPROC)(GLuint readFramebuffer, GLuint drawFramebuffer, GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter)
ctypedef void *(*PFNGLMAPNAMEDBUFFERRANGEPROC)(GLuint buffer, GLintptr offset, GLsizeiptr length, GLbitfield access)
ctypedef void (*PFNGLNAMEDRENDERBUFFERSTORAGEPROC)(GLuint renderbuffer, GLenum internalformat, GLsizei width, GLsizei height)
ctypedef void (*PFNGLGETTEXTURELEVELPARAMETERIVPROC)(GLuint texture, GLint level, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETCOMPRESSEDTEXTURESUBIMAGEPROC)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei bufSize, void *pixels)
ctypedef void (*PFNGLCREATETEXTURESPROC)(GLenum target, GLsizei n, GLuint *textures)
ctypedef void (*PFNGLGETNAMEDRENDERBUFFERPARAMETERIVPROC)(GLuint renderbuffer, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETQUERYBUFFEROBJECTIVPROC)(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
ctypedef void (*PFNGLGETNUNIFORMUIVPROC)(GLuint program, GLint location, GLsizei bufSize, GLuint *params)
ctypedef void (*PFNGLCLIPCONTROLPROC)(GLenum origin, GLenum depth)
ctypedef void (*PFNGLGETTRANSFORMFEEDBACKI_VPROC)(GLuint xfb, GLenum pname, GLuint index, GLint *param)
ctypedef GLboolean (*PFNGLUNMAPNAMEDBUFFERPROC)(GLuint buffer)
ctypedef void (*PFNGLCREATEQUERIESPROC)(GLenum target, GLsizei n, GLuint *ids)
ctypedef void (*PFNGLTEXTURESTORAGE3DMULTISAMPLEPROC)(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations)
ctypedef void (*PFNGLVERTEXARRAYVERTEXBUFFERPROC)(GLuint vaobj, GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride)
ctypedef void (*PFNGLGETTEXTUREPARAMETERIUIVPROC)(GLuint texture, GLenum pname, GLuint *params)
ctypedef void (*PFNGLCLEARNAMEDBUFFERSUBDATAPROC)(GLuint buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data)
ctypedef void (*PFNGLGETNMAPIVPROC)(GLenum target, GLenum query, GLsizei bufSize, GLint *v)
ctypedef void (*PFNGLGETTEXTUREPARAMETERIVPROC)(GLuint texture, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETTRANSFORMFEEDBACKI64_VPROC)(GLuint xfb, GLenum pname, GLuint index, GLint64 *param)
ctypedef void (*PFNGLVERTEXARRAYATTRIBLFORMATPROC)(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
ctypedef void (*PFNGLTEXTUREPARAMETERIIVPROC)(GLuint texture, GLenum pname, const GLint *params)
ctypedef void (*PFNGLGETQUERYBUFFEROBJECTUIVPROC)(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
ctypedef void (*PFNGLGETNUNIFORMDVPROC)(GLuint program, GLint location, GLsizei bufSize, GLdouble *params)
ctypedef void (*PFNGLCOPYTEXTURESUBIMAGE3DPROC)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*PFNGLTEXTURESTORAGE3DPROC)(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth)
ctypedef void (*PFNGLGETNMAPDVPROC)(GLenum target, GLenum query, GLsizei bufSize, GLdouble *v)
ctypedef void (*PFNGLGETQUERYBUFFEROBJECTI64VPROC)(GLuint id, GLuint buffer, GLenum pname, GLintptr offset)
ctypedef void (*PFNGLGETNAMEDBUFFERPOINTERVPROC)(GLuint buffer, GLenum pname, void **params)
ctypedef void (*PFNGLCLEARNAMEDFRAMEBUFFERIVPROC)(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLint *value)
ctypedef void (*PFNGLTEXTURESUBIMAGE2DPROC)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
ctypedef void (*PFNGLGETVERTEXARRAYINDEXED64IVPROC)(GLuint vaobj, GLuint index, GLenum pname, GLint64 *param)
ctypedef void (*PFNGLCLEARNAMEDFRAMEBUFFERFIPROC)(GLuint framebuffer, GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil)
ctypedef void (*PFNGLTRANSFORMFEEDBACKBUFFERBASEPROC)(GLuint xfb, GLuint index, GLuint buffer)
ctypedef void (*PFNGLNAMEDFRAMEBUFFERTEXTURELAYERPROC)(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level, GLint layer)
ctypedef void (*PFNGLGETNMINMAXPROC)(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values)
ctypedef void (*PFNGLCOPYTEXTURESUBIMAGE1DPROC)(GLuint texture, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width)
ctypedef void (*PFNGLGETNUNIFORMFVPROC)(GLuint program, GLint location, GLsizei bufSize, GLfloat *params)
ctypedef void (*PFNGLGETNAMEDBUFFERPARAMETERI64VPROC)(GLuint buffer, GLenum pname, GLint64 *params)
ctypedef void (*PFNGLGETNAMEDBUFFERPARAMETERIVPROC)(GLuint buffer, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETVERTEXARRAYIVPROC)(GLuint vaobj, GLenum pname, GLint *param)
ctypedef void (*PFNGLCOPYTEXTURESUBIMAGE2DPROC)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void *(*PFNGLMAPNAMEDBUFFERPROC)(GLuint buffer, GLenum access)
ctypedef void (*PFNGLNAMEDBUFFERSUBDATAPROC)(GLuint buffer, GLintptr offset, GLsizeiptr size, const void *data)
ctypedef void (*PFNGLGETNHISTOGRAMPROC)(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values)
ctypedef void (*PFNGLNAMEDFRAMEBUFFERRENDERBUFFERPROC)(GLuint framebuffer, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer)
ctypedef void (*PFNGLGETNPIXELMAPUSVPROC)(GLenum map, GLsizei bufSize, GLushort *values)
ctypedef void (*PFNGLGETNAMEDBUFFERSUBDATAPROC)(GLuint buffer, GLintptr offset, GLsizeiptr size, void *data)
ctypedef void (*PFNGLREADNPIXELSPROC)(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei bufSize, void *data)
ctypedef void (*PFNGLCOMPRESSEDTEXTURESUBIMAGE1DPROC)(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data)
ctypedef void (*PFNGLGETTEXTUREPARAMETERIIVPROC)(GLuint texture, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETNMAPFVPROC)(GLenum target, GLenum query, GLsizei bufSize, GLfloat *v)
ctypedef void (*PFNGLGETNPIXELMAPUIVPROC)(GLenum map, GLsizei bufSize, GLuint *values)
ctypedef void (*PFNGLCOPYNAMEDBUFFERSUBDATAPROC)(GLuint readBuffer, GLuint writeBuffer, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size)
ctypedef void (*PFNGLGENERATETEXTUREMIPMAPPROC)(GLuint texture)
ctypedef void (*PFNGLTEXTURESUBIMAGE3DPROC)(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels)
ctypedef void (*PFNGLGETTRANSFORMFEEDBACKIVPROC)(GLuint xfb, GLenum pname, GLint *param)
ctypedef void (*PFNGLENABLEVERTEXARRAYATTRIBPROC)(GLuint vaobj, GLuint index)
ctypedef void (*PFNGLINVALIDATENAMEDFRAMEBUFFERDATAPROC)(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments)
ctypedef void (*PFNGLVERTEXARRAYATTRIBIFORMATPROC)(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset)
ctypedef void (*PFNGLNAMEDFRAMEBUFFERTEXTUREPROC)(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level)

cdef PFNGLCREATESAMPLERSPROC cglCreateSamplers = NULL
cdef PFNGLVERTEXARRAYVERTEXBUFFERSPROC cglVertexArrayVertexBuffers = NULL
cdef PFNGLTEXTUREPARAMETERFPROC cglTextureParameterf = NULL
cdef PFNGLCLEARNAMEDBUFFERDATAPROC cglClearNamedBufferData = NULL
cdef PFNGLVERTEXARRAYATTRIBFORMATPROC cglVertexArrayAttribFormat = NULL
cdef PFNGLGETNCONVOLUTIONFILTERPROC cglGetnConvolutionFilter = NULL
cdef PFNGLNAMEDFRAMEBUFFERDRAWBUFFERSPROC cglNamedFramebufferDrawBuffers = NULL
cdef PFNGLNAMEDBUFFERDATAPROC cglNamedBufferData = NULL
cdef PFNGLBINDTEXTUREUNITPROC cglBindTextureUnit = NULL
cdef PFNGLVERTEXARRAYATTRIBBINDINGPROC cglVertexArrayAttribBinding = NULL
cdef PFNGLTEXTURESTORAGE2DMULTISAMPLEPROC cglTextureStorage2DMultisample = NULL
cdef PFNGLFLUSHMAPPEDNAMEDBUFFERRANGEPROC cglFlushMappedNamedBufferRange = NULL
cdef PFNGLGETQUERYBUFFEROBJECTUI64VPROC cglGetQueryBufferObjectui64v = NULL
cdef PFNGLDISABLEVERTEXARRAYATTRIBPROC cglDisableVertexArrayAttrib = NULL
cdef PFNGLGETTEXTURELEVELPARAMETERFVPROC cglGetTextureLevelParameterfv = NULL
cdef PFNGLCREATETRANSFORMFEEDBACKSPROC cglCreateTransformFeedbacks = NULL
cdef PFNGLCLEARNAMEDFRAMEBUFFERUIVPROC cglClearNamedFramebufferuiv = NULL
cdef PFNGLGETNPIXELMAPFVPROC cglGetnPixelMapfv = NULL
cdef PFNGLNAMEDFRAMEBUFFERREADBUFFERPROC cglNamedFramebufferReadBuffer = NULL
cdef PFNGLCREATERENDERBUFFERSPROC cglCreateRenderbuffers = NULL
cdef PFNGLCREATEVERTEXARRAYSPROC cglCreateVertexArrays = NULL
cdef PFNGLGETNAMEDFRAMEBUFFERATTACHMENTPARAMETERIVPROC cglGetNamedFramebufferAttachmentParameteriv = NULL
cdef PFNGLNAMEDFRAMEBUFFERDRAWBUFFERPROC cglNamedFramebufferDrawBuffer = NULL
cdef PFNGLCREATEBUFFERSPROC cglCreateBuffers = NULL
cdef PFNGLGETTEXTUREPARAMETERFVPROC cglGetTextureParameterfv = NULL
cdef PFNGLCOMPRESSEDTEXTURESUBIMAGE3DPROC cglCompressedTextureSubImage3D = NULL
cdef PFNGLTEXTUREBUFFERRANGEPROC cglTextureBufferRange = NULL
cdef PFNGLTEXTUREBARRIERPROC cglTextureBarrier = NULL
cdef PFNGLTEXTUREPARAMETERFVPROC cglTextureParameterfv = NULL
cdef PFNGLINVALIDATENAMEDFRAMEBUFFERSUBDATAPROC cglInvalidateNamedFramebufferSubData = NULL
cdef PFNGLTEXTUREBUFFERPROC cglTextureBuffer = NULL
cdef PFNGLTEXTUREPARAMETERIPROC cglTextureParameteri = NULL
cdef PFNGLTEXTURESUBIMAGE1DPROC cglTextureSubImage1D = NULL
cdef PFNGLCOMPRESSEDTEXTURESUBIMAGE2DPROC cglCompressedTextureSubImage2D = NULL
cdef PFNGLGETNCOMPRESSEDTEXIMAGEPROC cglGetnCompressedTexImage = NULL
cdef PFNGLGETNTEXIMAGEPROC cglGetnTexImage = NULL
cdef PFNGLGETGRAPHICSRESETSTATUSPROC cglGetGraphicsResetStatus = NULL
cdef PFNGLCREATEFRAMEBUFFERSPROC cglCreateFramebuffers = NULL
cdef PFNGLCREATEPROGRAMPIPELINESPROC cglCreateProgramPipelines = NULL
cdef PFNGLTEXTURESTORAGE2DPROC cglTextureStorage2D = NULL
cdef PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEPROC cglNamedRenderbufferStorageMultisample = NULL
cdef PFNGLVERTEXARRAYBINDINGDIVISORPROC cglVertexArrayBindingDivisor = NULL
cdef PFNGLGETVERTEXARRAYINDEXEDIVPROC cglGetVertexArrayIndexediv = NULL
cdef PFNGLGETNSEPARABLEFILTERPROC cglGetnSeparableFilter = NULL
cdef PFNGLGETNCOLORTABLEPROC cglGetnColorTable = NULL
cdef PFNGLGETTEXTUREIMAGEPROC cglGetTextureImage = NULL
cdef PFNGLCHECKNAMEDFRAMEBUFFERSTATUSPROC cglCheckNamedFramebufferStatus = NULL
cdef PFNGLCLEARNAMEDFRAMEBUFFERFVPROC cglClearNamedFramebufferfv = NULL
cdef PFNGLGETNAMEDFRAMEBUFFERPARAMETERIVPROC cglGetNamedFramebufferParameteriv = NULL
cdef PFNGLVERTEXARRAYELEMENTBUFFERPROC cglVertexArrayElementBuffer = NULL
cdef PFNGLTRANSFORMFEEDBACKBUFFERRANGEPROC cglTransformFeedbackBufferRange = NULL
cdef PFNGLNAMEDFRAMEBUFFERPARAMETERIPROC cglNamedFramebufferParameteri = NULL
cdef PFNGLMEMORYBARRIERBYREGIONPROC cglMemoryBarrierByRegion = NULL
cdef PFNGLNAMEDBUFFERSTORAGEPROC cglNamedBufferStorage = NULL
cdef PFNGLGETNPOLYGONSTIPPLEPROC cglGetnPolygonStipple = NULL
cdef PFNGLTEXTUREPARAMETERIVPROC cglTextureParameteriv = NULL
cdef PFNGLGETCOMPRESSEDTEXTUREIMAGEPROC cglGetCompressedTextureImage = NULL
cdef PFNGLTEXTUREPARAMETERIUIVPROC cglTextureParameterIuiv = NULL
cdef PFNGLTEXTURESTORAGE1DPROC cglTextureStorage1D = NULL
cdef PFNGLGETNUNIFORMIVPROC cglGetnUniformiv = NULL
cdef PFNGLGETTEXTURESUBIMAGEPROC cglGetTextureSubImage = NULL
cdef PFNGLBLITNAMEDFRAMEBUFFERPROC cglBlitNamedFramebuffer = NULL
cdef PFNGLMAPNAMEDBUFFERRANGEPROC cglMapNamedBufferRange = NULL
cdef PFNGLNAMEDRENDERBUFFERSTORAGEPROC cglNamedRenderbufferStorage = NULL
cdef PFNGLGETTEXTURELEVELPARAMETERIVPROC cglGetTextureLevelParameteriv = NULL
cdef PFNGLGETCOMPRESSEDTEXTURESUBIMAGEPROC cglGetCompressedTextureSubImage = NULL
cdef PFNGLCREATETEXTURESPROC cglCreateTextures = NULL
cdef PFNGLGETNAMEDRENDERBUFFERPARAMETERIVPROC cglGetNamedRenderbufferParameteriv = NULL
cdef PFNGLGETQUERYBUFFEROBJECTIVPROC cglGetQueryBufferObjectiv = NULL
cdef PFNGLGETNUNIFORMUIVPROC cglGetnUniformuiv = NULL
cdef PFNGLCLIPCONTROLPROC cglClipControl = NULL
cdef PFNGLGETTRANSFORMFEEDBACKI_VPROC cglGetTransformFeedbacki_v = NULL
cdef PFNGLUNMAPNAMEDBUFFERPROC cglUnmapNamedBuffer = NULL
cdef PFNGLCREATEQUERIESPROC cglCreateQueries = NULL
cdef PFNGLTEXTURESTORAGE3DMULTISAMPLEPROC cglTextureStorage3DMultisample = NULL
cdef PFNGLVERTEXARRAYVERTEXBUFFERPROC cglVertexArrayVertexBuffer = NULL
cdef PFNGLGETTEXTUREPARAMETERIUIVPROC cglGetTextureParameterIuiv = NULL
cdef PFNGLCLEARNAMEDBUFFERSUBDATAPROC cglClearNamedBufferSubData = NULL
cdef PFNGLGETNMAPIVPROC cglGetnMapiv = NULL
cdef PFNGLGETTEXTUREPARAMETERIVPROC cglGetTextureParameteriv = NULL
cdef PFNGLGETTRANSFORMFEEDBACKI64_VPROC cglGetTransformFeedbacki64_v = NULL
cdef PFNGLVERTEXARRAYATTRIBLFORMATPROC cglVertexArrayAttribLFormat = NULL
cdef PFNGLTEXTUREPARAMETERIIVPROC cglTextureParameterIiv = NULL
cdef PFNGLGETQUERYBUFFEROBJECTUIVPROC cglGetQueryBufferObjectuiv = NULL
cdef PFNGLGETNUNIFORMDVPROC cglGetnUniformdv = NULL
cdef PFNGLCOPYTEXTURESUBIMAGE3DPROC cglCopyTextureSubImage3D = NULL
cdef PFNGLTEXTURESTORAGE3DPROC cglTextureStorage3D = NULL
cdef PFNGLGETNMAPDVPROC cglGetnMapdv = NULL
cdef PFNGLGETQUERYBUFFEROBJECTI64VPROC cglGetQueryBufferObjecti64v = NULL
cdef PFNGLGETNAMEDBUFFERPOINTERVPROC cglGetNamedBufferPointerv = NULL
cdef PFNGLCLEARNAMEDFRAMEBUFFERIVPROC cglClearNamedFramebufferiv = NULL
cdef PFNGLTEXTURESUBIMAGE2DPROC cglTextureSubImage2D = NULL
cdef PFNGLGETVERTEXARRAYINDEXED64IVPROC cglGetVertexArrayIndexed64iv = NULL
cdef PFNGLCLEARNAMEDFRAMEBUFFERFIPROC cglClearNamedFramebufferfi = NULL
cdef PFNGLTRANSFORMFEEDBACKBUFFERBASEPROC cglTransformFeedbackBufferBase = NULL
cdef PFNGLNAMEDFRAMEBUFFERTEXTURELAYERPROC cglNamedFramebufferTextureLayer = NULL
cdef PFNGLGETNMINMAXPROC cglGetnMinmax = NULL
cdef PFNGLCOPYTEXTURESUBIMAGE1DPROC cglCopyTextureSubImage1D = NULL
cdef PFNGLGETNUNIFORMFVPROC cglGetnUniformfv = NULL
cdef PFNGLGETNAMEDBUFFERPARAMETERI64VPROC cglGetNamedBufferParameteri64v = NULL
cdef PFNGLGETNAMEDBUFFERPARAMETERIVPROC cglGetNamedBufferParameteriv = NULL
cdef PFNGLGETVERTEXARRAYIVPROC cglGetVertexArrayiv = NULL
cdef PFNGLCOPYTEXTURESUBIMAGE2DPROC cglCopyTextureSubImage2D = NULL
cdef PFNGLMAPNAMEDBUFFERPROC cglMapNamedBuffer = NULL
cdef PFNGLNAMEDBUFFERSUBDATAPROC cglNamedBufferSubData = NULL
cdef PFNGLGETNHISTOGRAMPROC cglGetnHistogram = NULL
cdef PFNGLNAMEDFRAMEBUFFERRENDERBUFFERPROC cglNamedFramebufferRenderbuffer = NULL
cdef PFNGLGETNPIXELMAPUSVPROC cglGetnPixelMapusv = NULL
cdef PFNGLGETNAMEDBUFFERSUBDATAPROC cglGetNamedBufferSubData = NULL
cdef PFNGLREADNPIXELSPROC cglReadnPixels = NULL
cdef PFNGLCOMPRESSEDTEXTURESUBIMAGE1DPROC cglCompressedTextureSubImage1D = NULL
cdef PFNGLGETTEXTUREPARAMETERIIVPROC cglGetTextureParameterIiv = NULL
cdef PFNGLGETNMAPFVPROC cglGetnMapfv = NULL
cdef PFNGLGETNPIXELMAPUIVPROC cglGetnPixelMapuiv = NULL
cdef PFNGLCOPYNAMEDBUFFERSUBDATAPROC cglCopyNamedBufferSubData = NULL
cdef PFNGLGENERATETEXTUREMIPMAPPROC cglGenerateTextureMipmap = NULL
cdef PFNGLTEXTURESUBIMAGE3DPROC cglTextureSubImage3D = NULL
cdef PFNGLGETTRANSFORMFEEDBACKIVPROC cglGetTransformFeedbackiv = NULL
cdef PFNGLENABLEVERTEXARRAYATTRIBPROC cglEnableVertexArrayAttrib = NULL
cdef PFNGLINVALIDATENAMEDFRAMEBUFFERDATAPROC cglInvalidateNamedFramebufferData = NULL
cdef PFNGLVERTEXARRAYATTRIBIFORMATPROC cglVertexArrayAttribIFormat = NULL
cdef PFNGLNAMEDFRAMEBUFFERTEXTUREPROC cglNamedFramebufferTexture = NULL


cdef void GetglCreateSamplers(GLsizei n, GLuint *samplers):
    global cglCreateSamplers
    cglCreateSamplers = <PFNGLCREATESAMPLERSPROC>getFunction(b"glCreateSamplers")
    cglCreateSamplers(n, samplers)

cdef void GetglVertexArrayVertexBuffers(GLuint vaobj, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides):
    global cglVertexArrayVertexBuffers
    cglVertexArrayVertexBuffers = <PFNGLVERTEXARRAYVERTEXBUFFERSPROC>getFunction(b"glVertexArrayVertexBuffers")
    cglVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides)

cdef void GetglTextureParameterf(GLuint texture, GLenum pname, GLfloat param):
    global cglTextureParameterf
    cglTextureParameterf = <PFNGLTEXTUREPARAMETERFPROC>getFunction(b"glTextureParameterf")
    cglTextureParameterf(texture, pname, param)

cdef void GetglClearNamedBufferData(GLuint buffer, GLenum internalformat, GLenum format, GLenum type, const void *data):
    global cglClearNamedBufferData
    cglClearNamedBufferData = <PFNGLCLEARNAMEDBUFFERDATAPROC>getFunction(b"glClearNamedBufferData")
    cglClearNamedBufferData(buffer, internalformat, format, type, data)

cdef void GetglVertexArrayAttribFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset):
    global cglVertexArrayAttribFormat
    cglVertexArrayAttribFormat = <PFNGLVERTEXARRAYATTRIBFORMATPROC>getFunction(b"glVertexArrayAttribFormat")
    cglVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset)

cdef void GetglGetnConvolutionFilter(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *image):
    global cglGetnConvolutionFilter
    cglGetnConvolutionFilter = <PFNGLGETNCONVOLUTIONFILTERPROC>getFunction(b"glGetnConvolutionFilter")
    cglGetnConvolutionFilter(target, format, type, bufSize, image)

cdef void GetglNamedFramebufferDrawBuffers(GLuint framebuffer, GLsizei n, const GLenum *bufs):
    global cglNamedFramebufferDrawBuffers
    cglNamedFramebufferDrawBuffers = <PFNGLNAMEDFRAMEBUFFERDRAWBUFFERSPROC>getFunction(b"glNamedFramebufferDrawBuffers")
    cglNamedFramebufferDrawBuffers(framebuffer, n, bufs)

cdef void GetglNamedBufferData(GLuint buffer, GLsizeiptr size, const void *data, GLenum usage):
    global cglNamedBufferData
    cglNamedBufferData = <PFNGLNAMEDBUFFERDATAPROC>getFunction(b"glNamedBufferData")
    cglNamedBufferData(buffer, size, data, usage)

cdef void GetglBindTextureUnit(GLuint unit, GLuint texture):
    global cglBindTextureUnit
    cglBindTextureUnit = <PFNGLBINDTEXTUREUNITPROC>getFunction(b"glBindTextureUnit")
    cglBindTextureUnit(unit, texture)

cdef void GetglVertexArrayAttribBinding(GLuint vaobj, GLuint attribindex, GLuint bindingindex):
    global cglVertexArrayAttribBinding
    cglVertexArrayAttribBinding = <PFNGLVERTEXARRAYATTRIBBINDINGPROC>getFunction(b"glVertexArrayAttribBinding")
    cglVertexArrayAttribBinding(vaobj, attribindex, bindingindex)

cdef void GetglTextureStorage2DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    global cglTextureStorage2DMultisample
    cglTextureStorage2DMultisample = <PFNGLTEXTURESTORAGE2DMULTISAMPLEPROC>getFunction(b"glTextureStorage2DMultisample")
    cglTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations)

cdef void GetglFlushMappedNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length):
    global cglFlushMappedNamedBufferRange
    cglFlushMappedNamedBufferRange = <PFNGLFLUSHMAPPEDNAMEDBUFFERRANGEPROC>getFunction(b"glFlushMappedNamedBufferRange")
    cglFlushMappedNamedBufferRange(buffer, offset, length)

cdef void GetglGetQueryBufferObjectui64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    global cglGetQueryBufferObjectui64v
    cglGetQueryBufferObjectui64v = <PFNGLGETQUERYBUFFEROBJECTUI64VPROC>getFunction(b"glGetQueryBufferObjectui64v")
    cglGetQueryBufferObjectui64v(id, buffer, pname, offset)

cdef void GetglDisableVertexArrayAttrib(GLuint vaobj, GLuint index):
    global cglDisableVertexArrayAttrib
    cglDisableVertexArrayAttrib = <PFNGLDISABLEVERTEXARRAYATTRIBPROC>getFunction(b"glDisableVertexArrayAttrib")
    cglDisableVertexArrayAttrib(vaobj, index)

cdef void GetglGetTextureLevelParameterfv(GLuint texture, GLint level, GLenum pname, GLfloat *params):
    global cglGetTextureLevelParameterfv
    cglGetTextureLevelParameterfv = <PFNGLGETTEXTURELEVELPARAMETERFVPROC>getFunction(b"glGetTextureLevelParameterfv")
    cglGetTextureLevelParameterfv(texture, level, pname, params)

cdef void GetglCreateTransformFeedbacks(GLsizei n, GLuint *ids):
    global cglCreateTransformFeedbacks
    cglCreateTransformFeedbacks = <PFNGLCREATETRANSFORMFEEDBACKSPROC>getFunction(b"glCreateTransformFeedbacks")
    cglCreateTransformFeedbacks(n, ids)

cdef void GetglClearNamedFramebufferuiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLuint *value):
    global cglClearNamedFramebufferuiv
    cglClearNamedFramebufferuiv = <PFNGLCLEARNAMEDFRAMEBUFFERUIVPROC>getFunction(b"glClearNamedFramebufferuiv")
    cglClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value)

cdef void GetglGetnPixelMapfv(GLenum map, GLsizei bufSize, GLfloat *values):
    global cglGetnPixelMapfv
    cglGetnPixelMapfv = <PFNGLGETNPIXELMAPFVPROC>getFunction(b"glGetnPixelMapfv")
    cglGetnPixelMapfv(map, bufSize, values)

cdef void GetglNamedFramebufferReadBuffer(GLuint framebuffer, GLenum src):
    global cglNamedFramebufferReadBuffer
    cglNamedFramebufferReadBuffer = <PFNGLNAMEDFRAMEBUFFERREADBUFFERPROC>getFunction(b"glNamedFramebufferReadBuffer")
    cglNamedFramebufferReadBuffer(framebuffer, src)

cdef void GetglCreateRenderbuffers(GLsizei n, GLuint *renderbuffers):
    global cglCreateRenderbuffers
    cglCreateRenderbuffers = <PFNGLCREATERENDERBUFFERSPROC>getFunction(b"glCreateRenderbuffers")
    cglCreateRenderbuffers(n, renderbuffers)

cdef void GetglCreateVertexArrays(GLsizei n, GLuint *arrays):
    global cglCreateVertexArrays
    cglCreateVertexArrays = <PFNGLCREATEVERTEXARRAYSPROC>getFunction(b"glCreateVertexArrays")
    cglCreateVertexArrays(n, arrays)

cdef void GetglGetNamedFramebufferAttachmentParameteriv(GLuint framebuffer, GLenum attachment, GLenum pname, GLint *params):
    global cglGetNamedFramebufferAttachmentParameteriv
    cglGetNamedFramebufferAttachmentParameteriv = <PFNGLGETNAMEDFRAMEBUFFERATTACHMENTPARAMETERIVPROC>getFunction(b"glGetNamedFramebufferAttachmentParameteriv")
    cglGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname, params)

cdef void GetglNamedFramebufferDrawBuffer(GLuint framebuffer, GLenum buf):
    global cglNamedFramebufferDrawBuffer
    cglNamedFramebufferDrawBuffer = <PFNGLNAMEDFRAMEBUFFERDRAWBUFFERPROC>getFunction(b"glNamedFramebufferDrawBuffer")
    cglNamedFramebufferDrawBuffer(framebuffer, buf)

cdef void GetglCreateBuffers(GLsizei n, GLuint *buffers):
    global cglCreateBuffers
    cglCreateBuffers = <PFNGLCREATEBUFFERSPROC>getFunction(b"glCreateBuffers")
    cglCreateBuffers(n, buffers)

cdef void GetglGetTextureParameterfv(GLuint texture, GLenum pname, GLfloat *params):
    global cglGetTextureParameterfv
    cglGetTextureParameterfv = <PFNGLGETTEXTUREPARAMETERFVPROC>getFunction(b"glGetTextureParameterfv")
    cglGetTextureParameterfv(texture, pname, params)

cdef void GetglCompressedTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTextureSubImage3D
    cglCompressedTextureSubImage3D = <PFNGLCOMPRESSEDTEXTURESUBIMAGE3DPROC>getFunction(b"glCompressedTextureSubImage3D")
    cglCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

cdef void GetglTextureBufferRange(GLuint texture, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size):
    global cglTextureBufferRange
    cglTextureBufferRange = <PFNGLTEXTUREBUFFERRANGEPROC>getFunction(b"glTextureBufferRange")
    cglTextureBufferRange(texture, internalformat, buffer, offset, size)

cdef void GetglTextureBarrier():
    global cglTextureBarrier
    cglTextureBarrier = <PFNGLTEXTUREBARRIERPROC>getFunction(b"glTextureBarrier")
    cglTextureBarrier()

cdef void GetglTextureParameterfv(GLuint texture, GLenum pname, const GLfloat *param):
    global cglTextureParameterfv
    cglTextureParameterfv = <PFNGLTEXTUREPARAMETERFVPROC>getFunction(b"glTextureParameterfv")
    cglTextureParameterfv(texture, pname, param)

cdef void GetglInvalidateNamedFramebufferSubData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglInvalidateNamedFramebufferSubData
    cglInvalidateNamedFramebufferSubData = <PFNGLINVALIDATENAMEDFRAMEBUFFERSUBDATAPROC>getFunction(b"glInvalidateNamedFramebufferSubData")
    cglInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height)

cdef void GetglTextureBuffer(GLuint texture, GLenum internalformat, GLuint buffer):
    global cglTextureBuffer
    cglTextureBuffer = <PFNGLTEXTUREBUFFERPROC>getFunction(b"glTextureBuffer")
    cglTextureBuffer(texture, internalformat, buffer)

cdef void GetglTextureParameteri(GLuint texture, GLenum pname, GLint param):
    global cglTextureParameteri
    cglTextureParameteri = <PFNGLTEXTUREPARAMETERIPROC>getFunction(b"glTextureParameteri")
    cglTextureParameteri(texture, pname, param)

cdef void GetglTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels):
    global cglTextureSubImage1D
    cglTextureSubImage1D = <PFNGLTEXTURESUBIMAGE1DPROC>getFunction(b"glTextureSubImage1D")
    cglTextureSubImage1D(texture, level, xoffset, width, format, type, pixels)

cdef void GetglCompressedTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTextureSubImage2D
    cglCompressedTextureSubImage2D = <PFNGLCOMPRESSEDTEXTURESUBIMAGE2DPROC>getFunction(b"glCompressedTextureSubImage2D")
    cglCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize, data)

cdef void GetglGetnCompressedTexImage(GLenum target, GLint lod, GLsizei bufSize, void *pixels):
    global cglGetnCompressedTexImage
    cglGetnCompressedTexImage = <PFNGLGETNCOMPRESSEDTEXIMAGEPROC>getFunction(b"glGetnCompressedTexImage")
    cglGetnCompressedTexImage(target, lod, bufSize, pixels)

cdef void GetglGetnTexImage(GLenum target, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    global cglGetnTexImage
    cglGetnTexImage = <PFNGLGETNTEXIMAGEPROC>getFunction(b"glGetnTexImage")
    cglGetnTexImage(target, level, format, type, bufSize, pixels)

cdef GLenum GetglGetGraphicsResetStatus():
    global cglGetGraphicsResetStatus
    cglGetGraphicsResetStatus = <PFNGLGETGRAPHICSRESETSTATUSPROC>getFunction(b"glGetGraphicsResetStatus")
    cglGetGraphicsResetStatus()

cdef void GetglCreateFramebuffers(GLsizei n, GLuint *framebuffers):
    global cglCreateFramebuffers
    cglCreateFramebuffers = <PFNGLCREATEFRAMEBUFFERSPROC>getFunction(b"glCreateFramebuffers")
    cglCreateFramebuffers(n, framebuffers)

cdef void GetglCreateProgramPipelines(GLsizei n, GLuint *pipelines):
    global cglCreateProgramPipelines
    cglCreateProgramPipelines = <PFNGLCREATEPROGRAMPIPELINESPROC>getFunction(b"glCreateProgramPipelines")
    cglCreateProgramPipelines(n, pipelines)

cdef void GetglTextureStorage2D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height):
    global cglTextureStorage2D
    cglTextureStorage2D = <PFNGLTEXTURESTORAGE2DPROC>getFunction(b"glTextureStorage2D")
    cglTextureStorage2D(texture, levels, internalformat, width, height)

cdef void GetglNamedRenderbufferStorageMultisample(GLuint renderbuffer, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height):
    global cglNamedRenderbufferStorageMultisample
    cglNamedRenderbufferStorageMultisample = <PFNGLNAMEDRENDERBUFFERSTORAGEMULTISAMPLEPROC>getFunction(b"glNamedRenderbufferStorageMultisample")
    cglNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height)

cdef void GetglVertexArrayBindingDivisor(GLuint vaobj, GLuint bindingindex, GLuint divisor):
    global cglVertexArrayBindingDivisor
    cglVertexArrayBindingDivisor = <PFNGLVERTEXARRAYBINDINGDIVISORPROC>getFunction(b"glVertexArrayBindingDivisor")
    cglVertexArrayBindingDivisor(vaobj, bindingindex, divisor)

cdef void GetglGetVertexArrayIndexediv(GLuint vaobj, GLuint index, GLenum pname, GLint *param):
    global cglGetVertexArrayIndexediv
    cglGetVertexArrayIndexediv = <PFNGLGETVERTEXARRAYINDEXEDIVPROC>getFunction(b"glGetVertexArrayIndexediv")
    cglGetVertexArrayIndexediv(vaobj, index, pname, param)

cdef void GetglGetnSeparableFilter(GLenum target, GLenum format, GLenum type, GLsizei rowBufSize, void *row, GLsizei columnBufSize, void *column, void *span):
    global cglGetnSeparableFilter
    cglGetnSeparableFilter = <PFNGLGETNSEPARABLEFILTERPROC>getFunction(b"glGetnSeparableFilter")
    cglGetnSeparableFilter(target, format, type, rowBufSize, row, columnBufSize, column, span)

cdef void GetglGetnColorTable(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *table):
    global cglGetnColorTable
    cglGetnColorTable = <PFNGLGETNCOLORTABLEPROC>getFunction(b"glGetnColorTable")
    cglGetnColorTable(target, format, type, bufSize, table)

cdef void GetglGetTextureImage(GLuint texture, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    global cglGetTextureImage
    cglGetTextureImage = <PFNGLGETTEXTUREIMAGEPROC>getFunction(b"glGetTextureImage")
    cglGetTextureImage(texture, level, format, type, bufSize, pixels)

cdef GLenum GetglCheckNamedFramebufferStatus(GLuint framebuffer, GLenum target):
    global cglCheckNamedFramebufferStatus
    cglCheckNamedFramebufferStatus = <PFNGLCHECKNAMEDFRAMEBUFFERSTATUSPROC>getFunction(b"glCheckNamedFramebufferStatus")
    cglCheckNamedFramebufferStatus(framebuffer, target)

cdef void GetglClearNamedFramebufferfv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat *value):
    global cglClearNamedFramebufferfv
    cglClearNamedFramebufferfv = <PFNGLCLEARNAMEDFRAMEBUFFERFVPROC>getFunction(b"glClearNamedFramebufferfv")
    cglClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value)

cdef void GetglGetNamedFramebufferParameteriv(GLuint framebuffer, GLenum pname, GLint *param):
    global cglGetNamedFramebufferParameteriv
    cglGetNamedFramebufferParameteriv = <PFNGLGETNAMEDFRAMEBUFFERPARAMETERIVPROC>getFunction(b"glGetNamedFramebufferParameteriv")
    cglGetNamedFramebufferParameteriv(framebuffer, pname, param)

cdef void GetglVertexArrayElementBuffer(GLuint vaobj, GLuint buffer):
    global cglVertexArrayElementBuffer
    cglVertexArrayElementBuffer = <PFNGLVERTEXARRAYELEMENTBUFFERPROC>getFunction(b"glVertexArrayElementBuffer")
    cglVertexArrayElementBuffer(vaobj, buffer)

cdef void GetglTransformFeedbackBufferRange(GLuint xfb, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size):
    global cglTransformFeedbackBufferRange
    cglTransformFeedbackBufferRange = <PFNGLTRANSFORMFEEDBACKBUFFERRANGEPROC>getFunction(b"glTransformFeedbackBufferRange")
    cglTransformFeedbackBufferRange(xfb, index, buffer, offset, size)

cdef void GetglNamedFramebufferParameteri(GLuint framebuffer, GLenum pname, GLint param):
    global cglNamedFramebufferParameteri
    cglNamedFramebufferParameteri = <PFNGLNAMEDFRAMEBUFFERPARAMETERIPROC>getFunction(b"glNamedFramebufferParameteri")
    cglNamedFramebufferParameteri(framebuffer, pname, param)

cdef void GetglMemoryBarrierByRegion(GLbitfield barriers):
    global cglMemoryBarrierByRegion
    cglMemoryBarrierByRegion = <PFNGLMEMORYBARRIERBYREGIONPROC>getFunction(b"glMemoryBarrierByRegion")
    cglMemoryBarrierByRegion(barriers)

cdef void GetglNamedBufferStorage(GLuint buffer, GLsizeiptr size, const void *data, GLbitfield flags):
    global cglNamedBufferStorage
    cglNamedBufferStorage = <PFNGLNAMEDBUFFERSTORAGEPROC>getFunction(b"glNamedBufferStorage")
    cglNamedBufferStorage(buffer, size, data, flags)

cdef void GetglGetnPolygonStipple(GLsizei bufSize, GLubyte *pattern):
    global cglGetnPolygonStipple
    cglGetnPolygonStipple = <PFNGLGETNPOLYGONSTIPPLEPROC>getFunction(b"glGetnPolygonStipple")
    cglGetnPolygonStipple(bufSize, pattern)

cdef void GetglTextureParameteriv(GLuint texture, GLenum pname, const GLint *param):
    global cglTextureParameteriv
    cglTextureParameteriv = <PFNGLTEXTUREPARAMETERIVPROC>getFunction(b"glTextureParameteriv")
    cglTextureParameteriv(texture, pname, param)

cdef void GetglGetCompressedTextureImage(GLuint texture, GLint level, GLsizei bufSize, void *pixels):
    global cglGetCompressedTextureImage
    cglGetCompressedTextureImage = <PFNGLGETCOMPRESSEDTEXTUREIMAGEPROC>getFunction(b"glGetCompressedTextureImage")
    cglGetCompressedTextureImage(texture, level, bufSize, pixels)

cdef void GetglTextureParameterIuiv(GLuint texture, GLenum pname, const GLuint *params):
    global cglTextureParameterIuiv
    cglTextureParameterIuiv = <PFNGLTEXTUREPARAMETERIUIVPROC>getFunction(b"glTextureParameterIuiv")
    cglTextureParameterIuiv(texture, pname, params)

cdef void GetglTextureStorage1D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width):
    global cglTextureStorage1D
    cglTextureStorage1D = <PFNGLTEXTURESTORAGE1DPROC>getFunction(b"glTextureStorage1D")
    cglTextureStorage1D(texture, levels, internalformat, width)

cdef void GetglGetnUniformiv(GLuint program, GLint location, GLsizei bufSize, GLint *params):
    global cglGetnUniformiv
    cglGetnUniformiv = <PFNGLGETNUNIFORMIVPROC>getFunction(b"glGetnUniformiv")
    cglGetnUniformiv(program, location, bufSize, params)

cdef void GetglGetTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    global cglGetTextureSubImage
    cglGetTextureSubImage = <PFNGLGETTEXTURESUBIMAGEPROC>getFunction(b"glGetTextureSubImage")
    cglGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize, pixels)

cdef void GetglBlitNamedFramebuffer(GLuint readFramebuffer, GLuint drawFramebuffer, GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter):
    global cglBlitNamedFramebuffer
    cglBlitNamedFramebuffer = <PFNGLBLITNAMEDFRAMEBUFFERPROC>getFunction(b"glBlitNamedFramebuffer")
    cglBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)

cdef void *GetglMapNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length, GLbitfield access):
    global cglMapNamedBufferRange
    cglMapNamedBufferRange = <PFNGLMAPNAMEDBUFFERRANGEPROC>getFunction(b"glMapNamedBufferRange")
    cglMapNamedBufferRange(buffer, offset, length, access)

cdef void GetglNamedRenderbufferStorage(GLuint renderbuffer, GLenum internalformat, GLsizei width, GLsizei height):
    global cglNamedRenderbufferStorage
    cglNamedRenderbufferStorage = <PFNGLNAMEDRENDERBUFFERSTORAGEPROC>getFunction(b"glNamedRenderbufferStorage")
    cglNamedRenderbufferStorage(renderbuffer, internalformat, width, height)

cdef void GetglGetTextureLevelParameteriv(GLuint texture, GLint level, GLenum pname, GLint *params):
    global cglGetTextureLevelParameteriv
    cglGetTextureLevelParameteriv = <PFNGLGETTEXTURELEVELPARAMETERIVPROC>getFunction(b"glGetTextureLevelParameteriv")
    cglGetTextureLevelParameteriv(texture, level, pname, params)

cdef void GetglGetCompressedTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei bufSize, void *pixels):
    global cglGetCompressedTextureSubImage
    cglGetCompressedTextureSubImage = <PFNGLGETCOMPRESSEDTEXTURESUBIMAGEPROC>getFunction(b"glGetCompressedTextureSubImage")
    cglGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize, pixels)

cdef void GetglCreateTextures(GLenum target, GLsizei n, GLuint *textures):
    global cglCreateTextures
    cglCreateTextures = <PFNGLCREATETEXTURESPROC>getFunction(b"glCreateTextures")
    cglCreateTextures(target, n, textures)

cdef void GetglGetNamedRenderbufferParameteriv(GLuint renderbuffer, GLenum pname, GLint *params):
    global cglGetNamedRenderbufferParameteriv
    cglGetNamedRenderbufferParameteriv = <PFNGLGETNAMEDRENDERBUFFERPARAMETERIVPROC>getFunction(b"glGetNamedRenderbufferParameteriv")
    cglGetNamedRenderbufferParameteriv(renderbuffer, pname, params)

cdef void GetglGetQueryBufferObjectiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    global cglGetQueryBufferObjectiv
    cglGetQueryBufferObjectiv = <PFNGLGETQUERYBUFFEROBJECTIVPROC>getFunction(b"glGetQueryBufferObjectiv")
    cglGetQueryBufferObjectiv(id, buffer, pname, offset)

cdef void GetglGetnUniformuiv(GLuint program, GLint location, GLsizei bufSize, GLuint *params):
    global cglGetnUniformuiv
    cglGetnUniformuiv = <PFNGLGETNUNIFORMUIVPROC>getFunction(b"glGetnUniformuiv")
    cglGetnUniformuiv(program, location, bufSize, params)

cdef void GetglClipControl(GLenum origin, GLenum depth):
    global cglClipControl
    cglClipControl = <PFNGLCLIPCONTROLPROC>getFunction(b"glClipControl")
    cglClipControl(origin, depth)

cdef void GetglGetTransformFeedbacki_v(GLuint xfb, GLenum pname, GLuint index, GLint *param):
    global cglGetTransformFeedbacki_v
    cglGetTransformFeedbacki_v = <PFNGLGETTRANSFORMFEEDBACKI_VPROC>getFunction(b"glGetTransformFeedbacki_v")
    cglGetTransformFeedbacki_v(xfb, pname, index, param)

cdef GLboolean GetglUnmapNamedBuffer(GLuint buffer):
    global cglUnmapNamedBuffer
    cglUnmapNamedBuffer = <PFNGLUNMAPNAMEDBUFFERPROC>getFunction(b"glUnmapNamedBuffer")
    cglUnmapNamedBuffer(buffer)

cdef void GetglCreateQueries(GLenum target, GLsizei n, GLuint *ids):
    global cglCreateQueries
    cglCreateQueries = <PFNGLCREATEQUERIESPROC>getFunction(b"glCreateQueries")
    cglCreateQueries(target, n, ids)

cdef void GetglTextureStorage3DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    global cglTextureStorage3DMultisample
    cglTextureStorage3DMultisample = <PFNGLTEXTURESTORAGE3DMULTISAMPLEPROC>getFunction(b"glTextureStorage3DMultisample")
    cglTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations)

cdef void GetglVertexArrayVertexBuffer(GLuint vaobj, GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride):
    global cglVertexArrayVertexBuffer
    cglVertexArrayVertexBuffer = <PFNGLVERTEXARRAYVERTEXBUFFERPROC>getFunction(b"glVertexArrayVertexBuffer")
    cglVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride)

cdef void GetglGetTextureParameterIuiv(GLuint texture, GLenum pname, GLuint *params):
    global cglGetTextureParameterIuiv
    cglGetTextureParameterIuiv = <PFNGLGETTEXTUREPARAMETERIUIVPROC>getFunction(b"glGetTextureParameterIuiv")
    cglGetTextureParameterIuiv(texture, pname, params)

cdef void GetglClearNamedBufferSubData(GLuint buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data):
    global cglClearNamedBufferSubData
    cglClearNamedBufferSubData = <PFNGLCLEARNAMEDBUFFERSUBDATAPROC>getFunction(b"glClearNamedBufferSubData")
    cglClearNamedBufferSubData(buffer, internalformat, offset, size, format, type, data)

cdef void GetglGetnMapiv(GLenum target, GLenum query, GLsizei bufSize, GLint *v):
    global cglGetnMapiv
    cglGetnMapiv = <PFNGLGETNMAPIVPROC>getFunction(b"glGetnMapiv")
    cglGetnMapiv(target, query, bufSize, v)

cdef void GetglGetTextureParameteriv(GLuint texture, GLenum pname, GLint *params):
    global cglGetTextureParameteriv
    cglGetTextureParameteriv = <PFNGLGETTEXTUREPARAMETERIVPROC>getFunction(b"glGetTextureParameteriv")
    cglGetTextureParameteriv(texture, pname, params)

cdef void GetglGetTransformFeedbacki64_v(GLuint xfb, GLenum pname, GLuint index, GLint64 *param):
    global cglGetTransformFeedbacki64_v
    cglGetTransformFeedbacki64_v = <PFNGLGETTRANSFORMFEEDBACKI64_VPROC>getFunction(b"glGetTransformFeedbacki64_v")
    cglGetTransformFeedbacki64_v(xfb, pname, index, param)

cdef void GetglVertexArrayAttribLFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    global cglVertexArrayAttribLFormat
    cglVertexArrayAttribLFormat = <PFNGLVERTEXARRAYATTRIBLFORMATPROC>getFunction(b"glVertexArrayAttribLFormat")
    cglVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset)

cdef void GetglTextureParameterIiv(GLuint texture, GLenum pname, const GLint *params):
    global cglTextureParameterIiv
    cglTextureParameterIiv = <PFNGLTEXTUREPARAMETERIIVPROC>getFunction(b"glTextureParameterIiv")
    cglTextureParameterIiv(texture, pname, params)

cdef void GetglGetQueryBufferObjectuiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    global cglGetQueryBufferObjectuiv
    cglGetQueryBufferObjectuiv = <PFNGLGETQUERYBUFFEROBJECTUIVPROC>getFunction(b"glGetQueryBufferObjectuiv")
    cglGetQueryBufferObjectuiv(id, buffer, pname, offset)

cdef void GetglGetnUniformdv(GLuint program, GLint location, GLsizei bufSize, GLdouble *params):
    global cglGetnUniformdv
    cglGetnUniformdv = <PFNGLGETNUNIFORMDVPROC>getFunction(b"glGetnUniformdv")
    cglGetnUniformdv(program, location, bufSize, params)

cdef void GetglCopyTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglCopyTextureSubImage3D
    cglCopyTextureSubImage3D = <PFNGLCOPYTEXTURESUBIMAGE3DPROC>getFunction(b"glCopyTextureSubImage3D")
    cglCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height)

cdef void GetglTextureStorage3D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth):
    global cglTextureStorage3D
    cglTextureStorage3D = <PFNGLTEXTURESTORAGE3DPROC>getFunction(b"glTextureStorage3D")
    cglTextureStorage3D(texture, levels, internalformat, width, height, depth)

cdef void GetglGetnMapdv(GLenum target, GLenum query, GLsizei bufSize, GLdouble *v):
    global cglGetnMapdv
    cglGetnMapdv = <PFNGLGETNMAPDVPROC>getFunction(b"glGetnMapdv")
    cglGetnMapdv(target, query, bufSize, v)

cdef void GetglGetQueryBufferObjecti64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    global cglGetQueryBufferObjecti64v
    cglGetQueryBufferObjecti64v = <PFNGLGETQUERYBUFFEROBJECTI64VPROC>getFunction(b"glGetQueryBufferObjecti64v")
    cglGetQueryBufferObjecti64v(id, buffer, pname, offset)

cdef void GetglGetNamedBufferPointerv(GLuint buffer, GLenum pname, void **params):
    global cglGetNamedBufferPointerv
    cglGetNamedBufferPointerv = <PFNGLGETNAMEDBUFFERPOINTERVPROC>getFunction(b"glGetNamedBufferPointerv")
    cglGetNamedBufferPointerv(buffer, pname, params)

cdef void GetglClearNamedFramebufferiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLint *value):
    global cglClearNamedFramebufferiv
    cglClearNamedFramebufferiv = <PFNGLCLEARNAMEDFRAMEBUFFERIVPROC>getFunction(b"glClearNamedFramebufferiv")
    cglClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value)

cdef void GetglTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    global cglTextureSubImage2D
    cglTextureSubImage2D = <PFNGLTEXTURESUBIMAGE2DPROC>getFunction(b"glTextureSubImage2D")
    cglTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type, pixels)

cdef void GetglGetVertexArrayIndexed64iv(GLuint vaobj, GLuint index, GLenum pname, GLint64 *param):
    global cglGetVertexArrayIndexed64iv
    cglGetVertexArrayIndexed64iv = <PFNGLGETVERTEXARRAYINDEXED64IVPROC>getFunction(b"glGetVertexArrayIndexed64iv")
    cglGetVertexArrayIndexed64iv(vaobj, index, pname, param)

cdef void GetglClearNamedFramebufferfi(GLuint framebuffer, GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil):
    global cglClearNamedFramebufferfi
    cglClearNamedFramebufferfi = <PFNGLCLEARNAMEDFRAMEBUFFERFIPROC>getFunction(b"glClearNamedFramebufferfi")
    cglClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil)

cdef void GetglTransformFeedbackBufferBase(GLuint xfb, GLuint index, GLuint buffer):
    global cglTransformFeedbackBufferBase
    cglTransformFeedbackBufferBase = <PFNGLTRANSFORMFEEDBACKBUFFERBASEPROC>getFunction(b"glTransformFeedbackBufferBase")
    cglTransformFeedbackBufferBase(xfb, index, buffer)

cdef void GetglNamedFramebufferTextureLayer(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level, GLint layer):
    global cglNamedFramebufferTextureLayer
    cglNamedFramebufferTextureLayer = <PFNGLNAMEDFRAMEBUFFERTEXTURELAYERPROC>getFunction(b"glNamedFramebufferTextureLayer")
    cglNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer)

cdef void GetglGetnMinmax(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values):
    global cglGetnMinmax
    cglGetnMinmax = <PFNGLGETNMINMAXPROC>getFunction(b"glGetnMinmax")
    cglGetnMinmax(target, reset, format, type, bufSize, values)

cdef void GetglCopyTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width):
    global cglCopyTextureSubImage1D
    cglCopyTextureSubImage1D = <PFNGLCOPYTEXTURESUBIMAGE1DPROC>getFunction(b"glCopyTextureSubImage1D")
    cglCopyTextureSubImage1D(texture, level, xoffset, x, y, width)

cdef void GetglGetnUniformfv(GLuint program, GLint location, GLsizei bufSize, GLfloat *params):
    global cglGetnUniformfv
    cglGetnUniformfv = <PFNGLGETNUNIFORMFVPROC>getFunction(b"glGetnUniformfv")
    cglGetnUniformfv(program, location, bufSize, params)

cdef void GetglGetNamedBufferParameteri64v(GLuint buffer, GLenum pname, GLint64 *params):
    global cglGetNamedBufferParameteri64v
    cglGetNamedBufferParameteri64v = <PFNGLGETNAMEDBUFFERPARAMETERI64VPROC>getFunction(b"glGetNamedBufferParameteri64v")
    cglGetNamedBufferParameteri64v(buffer, pname, params)

cdef void GetglGetNamedBufferParameteriv(GLuint buffer, GLenum pname, GLint *params):
    global cglGetNamedBufferParameteriv
    cglGetNamedBufferParameteriv = <PFNGLGETNAMEDBUFFERPARAMETERIVPROC>getFunction(b"glGetNamedBufferParameteriv")
    cglGetNamedBufferParameteriv(buffer, pname, params)

cdef void GetglGetVertexArrayiv(GLuint vaobj, GLenum pname, GLint *param):
    global cglGetVertexArrayiv
    cglGetVertexArrayiv = <PFNGLGETVERTEXARRAYIVPROC>getFunction(b"glGetVertexArrayiv")
    cglGetVertexArrayiv(vaobj, pname, param)

cdef void GetglCopyTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    global cglCopyTextureSubImage2D
    cglCopyTextureSubImage2D = <PFNGLCOPYTEXTURESUBIMAGE2DPROC>getFunction(b"glCopyTextureSubImage2D")
    cglCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height)

cdef void *GetglMapNamedBuffer(GLuint buffer, GLenum access):
    global cglMapNamedBuffer
    cglMapNamedBuffer = <PFNGLMAPNAMEDBUFFERPROC>getFunction(b"glMapNamedBuffer")
    cglMapNamedBuffer(buffer, access)

cdef void GetglNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, const void *data):
    global cglNamedBufferSubData
    cglNamedBufferSubData = <PFNGLNAMEDBUFFERSUBDATAPROC>getFunction(b"glNamedBufferSubData")
    cglNamedBufferSubData(buffer, offset, size, data)

cdef void GetglGetnHistogram(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values):
    global cglGetnHistogram
    cglGetnHistogram = <PFNGLGETNHISTOGRAMPROC>getFunction(b"glGetnHistogram")
    cglGetnHistogram(target, reset, format, type, bufSize, values)

cdef void GetglNamedFramebufferRenderbuffer(GLuint framebuffer, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer):
    global cglNamedFramebufferRenderbuffer
    cglNamedFramebufferRenderbuffer = <PFNGLNAMEDFRAMEBUFFERRENDERBUFFERPROC>getFunction(b"glNamedFramebufferRenderbuffer")
    cglNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer)

cdef void GetglGetnPixelMapusv(GLenum map, GLsizei bufSize, GLushort *values):
    global cglGetnPixelMapusv
    cglGetnPixelMapusv = <PFNGLGETNPIXELMAPUSVPROC>getFunction(b"glGetnPixelMapusv")
    cglGetnPixelMapusv(map, bufSize, values)

cdef void GetglGetNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, void *data):
    global cglGetNamedBufferSubData
    cglGetNamedBufferSubData = <PFNGLGETNAMEDBUFFERSUBDATAPROC>getFunction(b"glGetNamedBufferSubData")
    cglGetNamedBufferSubData(buffer, offset, size, data)

cdef void GetglReadnPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei bufSize, void *data):
    global cglReadnPixels
    cglReadnPixels = <PFNGLREADNPIXELSPROC>getFunction(b"glReadnPixels")
    cglReadnPixels(x, y, width, height, format, type, bufSize, data)

cdef void GetglCompressedTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data):
    global cglCompressedTextureSubImage1D
    cglCompressedTextureSubImage1D = <PFNGLCOMPRESSEDTEXTURESUBIMAGE1DPROC>getFunction(b"glCompressedTextureSubImage1D")
    cglCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize, data)

cdef void GetglGetTextureParameterIiv(GLuint texture, GLenum pname, GLint *params):
    global cglGetTextureParameterIiv
    cglGetTextureParameterIiv = <PFNGLGETTEXTUREPARAMETERIIVPROC>getFunction(b"glGetTextureParameterIiv")
    cglGetTextureParameterIiv(texture, pname, params)

cdef void GetglGetnMapfv(GLenum target, GLenum query, GLsizei bufSize, GLfloat *v):
    global cglGetnMapfv
    cglGetnMapfv = <PFNGLGETNMAPFVPROC>getFunction(b"glGetnMapfv")
    cglGetnMapfv(target, query, bufSize, v)

cdef void GetglGetnPixelMapuiv(GLenum map, GLsizei bufSize, GLuint *values):
    global cglGetnPixelMapuiv
    cglGetnPixelMapuiv = <PFNGLGETNPIXELMAPUIVPROC>getFunction(b"glGetnPixelMapuiv")
    cglGetnPixelMapuiv(map, bufSize, values)

cdef void GetglCopyNamedBufferSubData(GLuint readBuffer, GLuint writeBuffer, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size):
    global cglCopyNamedBufferSubData
    cglCopyNamedBufferSubData = <PFNGLCOPYNAMEDBUFFERSUBDATAPROC>getFunction(b"glCopyNamedBufferSubData")
    cglCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size)

cdef void GetglGenerateTextureMipmap(GLuint texture):
    global cglGenerateTextureMipmap
    cglGenerateTextureMipmap = <PFNGLGENERATETEXTUREMIPMAPPROC>getFunction(b"glGenerateTextureMipmap")
    cglGenerateTextureMipmap(texture)

cdef void GetglTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels):
    global cglTextureSubImage3D
    cglTextureSubImage3D = <PFNGLTEXTURESUBIMAGE3DPROC>getFunction(b"glTextureSubImage3D")
    cglTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)

cdef void GetglGetTransformFeedbackiv(GLuint xfb, GLenum pname, GLint *param):
    global cglGetTransformFeedbackiv
    cglGetTransformFeedbackiv = <PFNGLGETTRANSFORMFEEDBACKIVPROC>getFunction(b"glGetTransformFeedbackiv")
    cglGetTransformFeedbackiv(xfb, pname, param)

cdef void GetglEnableVertexArrayAttrib(GLuint vaobj, GLuint index):
    global cglEnableVertexArrayAttrib
    cglEnableVertexArrayAttrib = <PFNGLENABLEVERTEXARRAYATTRIBPROC>getFunction(b"glEnableVertexArrayAttrib")
    cglEnableVertexArrayAttrib(vaobj, index)

cdef void GetglInvalidateNamedFramebufferData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments):
    global cglInvalidateNamedFramebufferData
    cglInvalidateNamedFramebufferData = <PFNGLINVALIDATENAMEDFRAMEBUFFERDATAPROC>getFunction(b"glInvalidateNamedFramebufferData")
    cglInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments)

cdef void GetglVertexArrayAttribIFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    global cglVertexArrayAttribIFormat
    cglVertexArrayAttribIFormat = <PFNGLVERTEXARRAYATTRIBIFORMATPROC>getFunction(b"glVertexArrayAttribIFormat")
    cglVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset)

cdef void GetglNamedFramebufferTexture(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level):
    global cglNamedFramebufferTexture
    cglNamedFramebufferTexture = <PFNGLNAMEDFRAMEBUFFERTEXTUREPROC>getFunction(b"glNamedFramebufferTexture")
    cglNamedFramebufferTexture(framebuffer, attachment, texture, level)

cglCreateSamplers = GetglCreateSamplers
cglVertexArrayVertexBuffers = GetglVertexArrayVertexBuffers
cglTextureParameterf = GetglTextureParameterf
cglClearNamedBufferData = GetglClearNamedBufferData
cglVertexArrayAttribFormat = GetglVertexArrayAttribFormat
cglGetnConvolutionFilter = GetglGetnConvolutionFilter
cglNamedFramebufferDrawBuffers = GetglNamedFramebufferDrawBuffers
cglNamedBufferData = GetglNamedBufferData
cglBindTextureUnit = GetglBindTextureUnit
cglVertexArrayAttribBinding = GetglVertexArrayAttribBinding
cglTextureStorage2DMultisample = GetglTextureStorage2DMultisample
cglFlushMappedNamedBufferRange = GetglFlushMappedNamedBufferRange
cglGetQueryBufferObjectui64v = GetglGetQueryBufferObjectui64v
cglDisableVertexArrayAttrib = GetglDisableVertexArrayAttrib
cglGetTextureLevelParameterfv = GetglGetTextureLevelParameterfv
cglCreateTransformFeedbacks = GetglCreateTransformFeedbacks
cglClearNamedFramebufferuiv = GetglClearNamedFramebufferuiv
cglGetnPixelMapfv = GetglGetnPixelMapfv
cglNamedFramebufferReadBuffer = GetglNamedFramebufferReadBuffer
cglCreateRenderbuffers = GetglCreateRenderbuffers
cglCreateVertexArrays = GetglCreateVertexArrays
cglGetNamedFramebufferAttachmentParameteriv = GetglGetNamedFramebufferAttachmentParameteriv
cglNamedFramebufferDrawBuffer = GetglNamedFramebufferDrawBuffer
cglCreateBuffers = GetglCreateBuffers
cglGetTextureParameterfv = GetglGetTextureParameterfv
cglCompressedTextureSubImage3D = GetglCompressedTextureSubImage3D
cglTextureBufferRange = GetglTextureBufferRange
cglTextureBarrier = GetglTextureBarrier
cglTextureParameterfv = GetglTextureParameterfv
cglInvalidateNamedFramebufferSubData = GetglInvalidateNamedFramebufferSubData
cglTextureBuffer = GetglTextureBuffer
cglTextureParameteri = GetglTextureParameteri
cglTextureSubImage1D = GetglTextureSubImage1D
cglCompressedTextureSubImage2D = GetglCompressedTextureSubImage2D
cglGetnCompressedTexImage = GetglGetnCompressedTexImage
cglGetnTexImage = GetglGetnTexImage
cglGetGraphicsResetStatus = GetglGetGraphicsResetStatus
cglCreateFramebuffers = GetglCreateFramebuffers
cglCreateProgramPipelines = GetglCreateProgramPipelines
cglTextureStorage2D = GetglTextureStorage2D
cglNamedRenderbufferStorageMultisample = GetglNamedRenderbufferStorageMultisample
cglVertexArrayBindingDivisor = GetglVertexArrayBindingDivisor
cglGetVertexArrayIndexediv = GetglGetVertexArrayIndexediv
cglGetnSeparableFilter = GetglGetnSeparableFilter
cglGetnColorTable = GetglGetnColorTable
cglGetTextureImage = GetglGetTextureImage
cglCheckNamedFramebufferStatus = GetglCheckNamedFramebufferStatus
cglClearNamedFramebufferfv = GetglClearNamedFramebufferfv
cglGetNamedFramebufferParameteriv = GetglGetNamedFramebufferParameteriv
cglVertexArrayElementBuffer = GetglVertexArrayElementBuffer
cglTransformFeedbackBufferRange = GetglTransformFeedbackBufferRange
cglNamedFramebufferParameteri = GetglNamedFramebufferParameteri
cglMemoryBarrierByRegion = GetglMemoryBarrierByRegion
cglNamedBufferStorage = GetglNamedBufferStorage
cglGetnPolygonStipple = GetglGetnPolygonStipple
cglTextureParameteriv = GetglTextureParameteriv
cglGetCompressedTextureImage = GetglGetCompressedTextureImage
cglTextureParameterIuiv = GetglTextureParameterIuiv
cglTextureStorage1D = GetglTextureStorage1D
cglGetnUniformiv = GetglGetnUniformiv
cglGetTextureSubImage = GetglGetTextureSubImage
cglBlitNamedFramebuffer = GetglBlitNamedFramebuffer
cglMapNamedBufferRange = GetglMapNamedBufferRange
cglNamedRenderbufferStorage = GetglNamedRenderbufferStorage
cglGetTextureLevelParameteriv = GetglGetTextureLevelParameteriv
cglGetCompressedTextureSubImage = GetglGetCompressedTextureSubImage
cglCreateTextures = GetglCreateTextures
cglGetNamedRenderbufferParameteriv = GetglGetNamedRenderbufferParameteriv
cglGetQueryBufferObjectiv = GetglGetQueryBufferObjectiv
cglGetnUniformuiv = GetglGetnUniformuiv
cglClipControl = GetglClipControl
cglGetTransformFeedbacki_v = GetglGetTransformFeedbacki_v
cglUnmapNamedBuffer = GetglUnmapNamedBuffer
cglCreateQueries = GetglCreateQueries
cglTextureStorage3DMultisample = GetglTextureStorage3DMultisample
cglVertexArrayVertexBuffer = GetglVertexArrayVertexBuffer
cglGetTextureParameterIuiv = GetglGetTextureParameterIuiv
cglClearNamedBufferSubData = GetglClearNamedBufferSubData
cglGetnMapiv = GetglGetnMapiv
cglGetTextureParameteriv = GetglGetTextureParameteriv
cglGetTransformFeedbacki64_v = GetglGetTransformFeedbacki64_v
cglVertexArrayAttribLFormat = GetglVertexArrayAttribLFormat
cglTextureParameterIiv = GetglTextureParameterIiv
cglGetQueryBufferObjectuiv = GetglGetQueryBufferObjectuiv
cglGetnUniformdv = GetglGetnUniformdv
cglCopyTextureSubImage3D = GetglCopyTextureSubImage3D
cglTextureStorage3D = GetglTextureStorage3D
cglGetnMapdv = GetglGetnMapdv
cglGetQueryBufferObjecti64v = GetglGetQueryBufferObjecti64v
cglGetNamedBufferPointerv = GetglGetNamedBufferPointerv
cglClearNamedFramebufferiv = GetglClearNamedFramebufferiv
cglTextureSubImage2D = GetglTextureSubImage2D
cglGetVertexArrayIndexed64iv = GetglGetVertexArrayIndexed64iv
cglClearNamedFramebufferfi = GetglClearNamedFramebufferfi
cglTransformFeedbackBufferBase = GetglTransformFeedbackBufferBase
cglNamedFramebufferTextureLayer = GetglNamedFramebufferTextureLayer
cglGetnMinmax = GetglGetnMinmax
cglCopyTextureSubImage1D = GetglCopyTextureSubImage1D
cglGetnUniformfv = GetglGetnUniformfv
cglGetNamedBufferParameteri64v = GetglGetNamedBufferParameteri64v
cglGetNamedBufferParameteriv = GetglGetNamedBufferParameteriv
cglGetVertexArrayiv = GetglGetVertexArrayiv
cglCopyTextureSubImage2D = GetglCopyTextureSubImage2D
cglMapNamedBuffer = GetglMapNamedBuffer
cglNamedBufferSubData = GetglNamedBufferSubData
cglGetnHistogram = GetglGetnHistogram
cglNamedFramebufferRenderbuffer = GetglNamedFramebufferRenderbuffer
cglGetnPixelMapusv = GetglGetnPixelMapusv
cglGetNamedBufferSubData = GetglGetNamedBufferSubData
cglReadnPixels = GetglReadnPixels
cglCompressedTextureSubImage1D = GetglCompressedTextureSubImage1D
cglGetTextureParameterIiv = GetglGetTextureParameterIiv
cglGetnMapfv = GetglGetnMapfv
cglGetnPixelMapuiv = GetglGetnPixelMapuiv
cglCopyNamedBufferSubData = GetglCopyNamedBufferSubData
cglGenerateTextureMipmap = GetglGenerateTextureMipmap
cglTextureSubImage3D = GetglTextureSubImage3D
cglGetTransformFeedbackiv = GetglGetTransformFeedbackiv
cglEnableVertexArrayAttrib = GetglEnableVertexArrayAttrib
cglInvalidateNamedFramebufferData = GetglInvalidateNamedFramebufferData
cglVertexArrayAttribIFormat = GetglVertexArrayAttribIFormat
cglNamedFramebufferTexture = GetglNamedFramebufferTexture


cdef void glCreateSamplers(GLsizei n, GLuint *samplers):
    cglCreateSamplers(n, samplers)

cdef void glVertexArrayVertexBuffers(GLuint vaobj, GLuint first, GLsizei count, const GLuint *buffers, const GLintptr *offsets, const GLsizei *strides):
    cglVertexArrayVertexBuffers(vaobj, first, count, buffers, offsets, strides)

cdef void glTextureParameterf(GLuint texture, GLenum pname, GLfloat param):
    cglTextureParameterf(texture, pname, param)

cdef void glClearNamedBufferData(GLuint buffer, GLenum internalformat, GLenum format, GLenum type, const void *data):
    cglClearNamedBufferData(buffer, internalformat, format, type, data)

cdef void glVertexArrayAttribFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLboolean normalized, GLuint relativeoffset):
    cglVertexArrayAttribFormat(vaobj, attribindex, size, type, normalized, relativeoffset)

cdef void glGetnConvolutionFilter(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *image):
    cglGetnConvolutionFilter(target, format, type, bufSize, image)

cdef void glNamedFramebufferDrawBuffers(GLuint framebuffer, GLsizei n, const GLenum *bufs):
    cglNamedFramebufferDrawBuffers(framebuffer, n, bufs)

cdef void glNamedBufferData(GLuint buffer, GLsizeiptr size, const void *data, GLenum usage):
    cglNamedBufferData(buffer, size, data, usage)

cdef void glBindTextureUnit(GLuint unit, GLuint texture):
    cglBindTextureUnit(unit, texture)

cdef void glVertexArrayAttribBinding(GLuint vaobj, GLuint attribindex, GLuint bindingindex):
    cglVertexArrayAttribBinding(vaobj, attribindex, bindingindex)

cdef void glTextureStorage2DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLboolean fixedsamplelocations):
    cglTextureStorage2DMultisample(texture, samples, internalformat, width, height, fixedsamplelocations)

cdef void glFlushMappedNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length):
    cglFlushMappedNamedBufferRange(buffer, offset, length)

cdef void glGetQueryBufferObjectui64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    cglGetQueryBufferObjectui64v(id, buffer, pname, offset)

cdef void glDisableVertexArrayAttrib(GLuint vaobj, GLuint index):
    cglDisableVertexArrayAttrib(vaobj, index)

cdef void glGetTextureLevelParameterfv(GLuint texture, GLint level, GLenum pname, GLfloat *params):
    cglGetTextureLevelParameterfv(texture, level, pname, params)

cdef void glCreateTransformFeedbacks(GLsizei n, GLuint *ids):
    cglCreateTransformFeedbacks(n, ids)

cdef void glClearNamedFramebufferuiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLuint *value):
    cglClearNamedFramebufferuiv(framebuffer, buffer, drawbuffer, value)

cdef void glGetnPixelMapfv(GLenum map, GLsizei bufSize, GLfloat *values):
    cglGetnPixelMapfv(map, bufSize, values)

cdef void glNamedFramebufferReadBuffer(GLuint framebuffer, GLenum src):
    cglNamedFramebufferReadBuffer(framebuffer, src)

cdef void glCreateRenderbuffers(GLsizei n, GLuint *renderbuffers):
    cglCreateRenderbuffers(n, renderbuffers)

cdef void glCreateVertexArrays(GLsizei n, GLuint *arrays):
    cglCreateVertexArrays(n, arrays)

cdef void glGetNamedFramebufferAttachmentParameteriv(GLuint framebuffer, GLenum attachment, GLenum pname, GLint *params):
    cglGetNamedFramebufferAttachmentParameteriv(framebuffer, attachment, pname, params)

cdef void glNamedFramebufferDrawBuffer(GLuint framebuffer, GLenum buf):
    cglNamedFramebufferDrawBuffer(framebuffer, buf)

cdef void glCreateBuffers(GLsizei n, GLuint *buffers):
    cglCreateBuffers(n, buffers)

cdef void glGetTextureParameterfv(GLuint texture, GLenum pname, GLfloat *params):
    cglGetTextureParameterfv(texture, pname, params)

cdef void glCompressedTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, imageSize, data)

cdef void glTextureBufferRange(GLuint texture, GLenum internalformat, GLuint buffer, GLintptr offset, GLsizeiptr size):
    cglTextureBufferRange(texture, internalformat, buffer, offset, size)

cdef void glTextureBarrier():
    cglTextureBarrier()

cdef void glTextureParameterfv(GLuint texture, GLenum pname, const GLfloat *param):
    cglTextureParameterfv(texture, pname, param)

cdef void glInvalidateNamedFramebufferSubData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments, GLint x, GLint y, GLsizei width, GLsizei height):
    cglInvalidateNamedFramebufferSubData(framebuffer, numAttachments, attachments, x, y, width, height)

cdef void glTextureBuffer(GLuint texture, GLenum internalformat, GLuint buffer):
    cglTextureBuffer(texture, internalformat, buffer)

cdef void glTextureParameteri(GLuint texture, GLenum pname, GLint param):
    cglTextureParameteri(texture, pname, param)

cdef void glTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLenum type, const void *pixels):
    cglTextureSubImage1D(texture, level, xoffset, width, format, type, pixels)

cdef void glCompressedTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, imageSize, data)

cdef void glGetnCompressedTexImage(GLenum target, GLint lod, GLsizei bufSize, void *pixels):
    cglGetnCompressedTexImage(target, lod, bufSize, pixels)

cdef void glGetnTexImage(GLenum target, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    cglGetnTexImage(target, level, format, type, bufSize, pixels)

cdef GLenum glGetGraphicsResetStatus():
    cglGetGraphicsResetStatus()

cdef void glCreateFramebuffers(GLsizei n, GLuint *framebuffers):
    cglCreateFramebuffers(n, framebuffers)

cdef void glCreateProgramPipelines(GLsizei n, GLuint *pipelines):
    cglCreateProgramPipelines(n, pipelines)

cdef void glTextureStorage2D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height):
    cglTextureStorage2D(texture, levels, internalformat, width, height)

cdef void glNamedRenderbufferStorageMultisample(GLuint renderbuffer, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height):
    cglNamedRenderbufferStorageMultisample(renderbuffer, samples, internalformat, width, height)

cdef void glVertexArrayBindingDivisor(GLuint vaobj, GLuint bindingindex, GLuint divisor):
    cglVertexArrayBindingDivisor(vaobj, bindingindex, divisor)

cdef void glGetVertexArrayIndexediv(GLuint vaobj, GLuint index, GLenum pname, GLint *param):
    cglGetVertexArrayIndexediv(vaobj, index, pname, param)

cdef void glGetnSeparableFilter(GLenum target, GLenum format, GLenum type, GLsizei rowBufSize, void *row, GLsizei columnBufSize, void *column, void *span):
    cglGetnSeparableFilter(target, format, type, rowBufSize, row, columnBufSize, column, span)

cdef void glGetnColorTable(GLenum target, GLenum format, GLenum type, GLsizei bufSize, void *table):
    cglGetnColorTable(target, format, type, bufSize, table)

cdef void glGetTextureImage(GLuint texture, GLint level, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    cglGetTextureImage(texture, level, format, type, bufSize, pixels)

cdef GLenum glCheckNamedFramebufferStatus(GLuint framebuffer, GLenum target):
    cglCheckNamedFramebufferStatus(framebuffer, target)

cdef void glClearNamedFramebufferfv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLfloat *value):
    cglClearNamedFramebufferfv(framebuffer, buffer, drawbuffer, value)

cdef void glGetNamedFramebufferParameteriv(GLuint framebuffer, GLenum pname, GLint *param):
    cglGetNamedFramebufferParameteriv(framebuffer, pname, param)

cdef void glVertexArrayElementBuffer(GLuint vaobj, GLuint buffer):
    cglVertexArrayElementBuffer(vaobj, buffer)

cdef void glTransformFeedbackBufferRange(GLuint xfb, GLuint index, GLuint buffer, GLintptr offset, GLsizeiptr size):
    cglTransformFeedbackBufferRange(xfb, index, buffer, offset, size)

cdef void glNamedFramebufferParameteri(GLuint framebuffer, GLenum pname, GLint param):
    cglNamedFramebufferParameteri(framebuffer, pname, param)

cdef void glMemoryBarrierByRegion(GLbitfield barriers):
    cglMemoryBarrierByRegion(barriers)

cdef void glNamedBufferStorage(GLuint buffer, GLsizeiptr size, const void *data, GLbitfield flags):
    cglNamedBufferStorage(buffer, size, data, flags)

cdef void glGetnPolygonStipple(GLsizei bufSize, GLubyte *pattern):
    cglGetnPolygonStipple(bufSize, pattern)

cdef void glTextureParameteriv(GLuint texture, GLenum pname, const GLint *param):
    cglTextureParameteriv(texture, pname, param)

cdef void glGetCompressedTextureImage(GLuint texture, GLint level, GLsizei bufSize, void *pixels):
    cglGetCompressedTextureImage(texture, level, bufSize, pixels)

cdef void glTextureParameterIuiv(GLuint texture, GLenum pname, const GLuint *params):
    cglTextureParameterIuiv(texture, pname, params)

cdef void glTextureStorage1D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width):
    cglTextureStorage1D(texture, levels, internalformat, width)

cdef void glGetnUniformiv(GLuint program, GLint location, GLsizei bufSize, GLint *params):
    cglGetnUniformiv(program, location, bufSize, params)

cdef void glGetTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, GLsizei bufSize, void *pixels):
    cglGetTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, bufSize, pixels)

cdef void glBlitNamedFramebuffer(GLuint readFramebuffer, GLuint drawFramebuffer, GLint srcX0, GLint srcY0, GLint srcX1, GLint srcY1, GLint dstX0, GLint dstY0, GLint dstX1, GLint dstY1, GLbitfield mask, GLenum filter):
    cglBlitNamedFramebuffer(readFramebuffer, drawFramebuffer, srcX0, srcY0, srcX1, srcY1, dstX0, dstY0, dstX1, dstY1, mask, filter)

cdef void *glMapNamedBufferRange(GLuint buffer, GLintptr offset, GLsizeiptr length, GLbitfield access):
    cglMapNamedBufferRange(buffer, offset, length, access)

cdef void glNamedRenderbufferStorage(GLuint renderbuffer, GLenum internalformat, GLsizei width, GLsizei height):
    cglNamedRenderbufferStorage(renderbuffer, internalformat, width, height)

cdef void glGetTextureLevelParameteriv(GLuint texture, GLint level, GLenum pname, GLint *params):
    cglGetTextureLevelParameteriv(texture, level, pname, params)

cdef void glGetCompressedTextureSubImage(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLsizei bufSize, void *pixels):
    cglGetCompressedTextureSubImage(texture, level, xoffset, yoffset, zoffset, width, height, depth, bufSize, pixels)

cdef void glCreateTextures(GLenum target, GLsizei n, GLuint *textures):
    cglCreateTextures(target, n, textures)

cdef void glGetNamedRenderbufferParameteriv(GLuint renderbuffer, GLenum pname, GLint *params):
    cglGetNamedRenderbufferParameteriv(renderbuffer, pname, params)

cdef void glGetQueryBufferObjectiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    cglGetQueryBufferObjectiv(id, buffer, pname, offset)

cdef void glGetnUniformuiv(GLuint program, GLint location, GLsizei bufSize, GLuint *params):
    cglGetnUniformuiv(program, location, bufSize, params)

cdef void glClipControl(GLenum origin, GLenum depth):
    cglClipControl(origin, depth)

cdef void glGetTransformFeedbacki_v(GLuint xfb, GLenum pname, GLuint index, GLint *param):
    cglGetTransformFeedbacki_v(xfb, pname, index, param)

cdef GLboolean glUnmapNamedBuffer(GLuint buffer):
    cglUnmapNamedBuffer(buffer)

cdef void glCreateQueries(GLenum target, GLsizei n, GLuint *ids):
    cglCreateQueries(target, n, ids)

cdef void glTextureStorage3DMultisample(GLuint texture, GLsizei samples, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth, GLboolean fixedsamplelocations):
    cglTextureStorage3DMultisample(texture, samples, internalformat, width, height, depth, fixedsamplelocations)

cdef void glVertexArrayVertexBuffer(GLuint vaobj, GLuint bindingindex, GLuint buffer, GLintptr offset, GLsizei stride):
    cglVertexArrayVertexBuffer(vaobj, bindingindex, buffer, offset, stride)

cdef void glGetTextureParameterIuiv(GLuint texture, GLenum pname, GLuint *params):
    cglGetTextureParameterIuiv(texture, pname, params)

cdef void glClearNamedBufferSubData(GLuint buffer, GLenum internalformat, GLintptr offset, GLsizeiptr size, GLenum format, GLenum type, const void *data):
    cglClearNamedBufferSubData(buffer, internalformat, offset, size, format, type, data)

cdef void glGetnMapiv(GLenum target, GLenum query, GLsizei bufSize, GLint *v):
    cglGetnMapiv(target, query, bufSize, v)

cdef void glGetTextureParameteriv(GLuint texture, GLenum pname, GLint *params):
    cglGetTextureParameteriv(texture, pname, params)

cdef void glGetTransformFeedbacki64_v(GLuint xfb, GLenum pname, GLuint index, GLint64 *param):
    cglGetTransformFeedbacki64_v(xfb, pname, index, param)

cdef void glVertexArrayAttribLFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    cglVertexArrayAttribLFormat(vaobj, attribindex, size, type, relativeoffset)

cdef void glTextureParameterIiv(GLuint texture, GLenum pname, const GLint *params):
    cglTextureParameterIiv(texture, pname, params)

cdef void glGetQueryBufferObjectuiv(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    cglGetQueryBufferObjectuiv(id, buffer, pname, offset)

cdef void glGetnUniformdv(GLuint program, GLint location, GLsizei bufSize, GLdouble *params):
    cglGetnUniformdv(program, location, bufSize, params)

cdef void glCopyTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    cglCopyTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, x, y, width, height)

cdef void glTextureStorage3D(GLuint texture, GLsizei levels, GLenum internalformat, GLsizei width, GLsizei height, GLsizei depth):
    cglTextureStorage3D(texture, levels, internalformat, width, height, depth)

cdef void glGetnMapdv(GLenum target, GLenum query, GLsizei bufSize, GLdouble *v):
    cglGetnMapdv(target, query, bufSize, v)

cdef void glGetQueryBufferObjecti64v(GLuint id, GLuint buffer, GLenum pname, GLintptr offset):
    cglGetQueryBufferObjecti64v(id, buffer, pname, offset)

cdef void glGetNamedBufferPointerv(GLuint buffer, GLenum pname, void **params):
    cglGetNamedBufferPointerv(buffer, pname, params)

cdef void glClearNamedFramebufferiv(GLuint framebuffer, GLenum buffer, GLint drawbuffer, const GLint *value):
    cglClearNamedFramebufferiv(framebuffer, buffer, drawbuffer, value)

cdef void glTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    cglTextureSubImage2D(texture, level, xoffset, yoffset, width, height, format, type, pixels)

cdef void glGetVertexArrayIndexed64iv(GLuint vaobj, GLuint index, GLenum pname, GLint64 *param):
    cglGetVertexArrayIndexed64iv(vaobj, index, pname, param)

cdef void glClearNamedFramebufferfi(GLuint framebuffer, GLenum buffer, GLint drawbuffer, GLfloat depth, GLint stencil):
    cglClearNamedFramebufferfi(framebuffer, buffer, drawbuffer, depth, stencil)

cdef void glTransformFeedbackBufferBase(GLuint xfb, GLuint index, GLuint buffer):
    cglTransformFeedbackBufferBase(xfb, index, buffer)

cdef void glNamedFramebufferTextureLayer(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level, GLint layer):
    cglNamedFramebufferTextureLayer(framebuffer, attachment, texture, level, layer)

cdef void glGetnMinmax(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values):
    cglGetnMinmax(target, reset, format, type, bufSize, values)

cdef void glCopyTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLint x, GLint y, GLsizei width):
    cglCopyTextureSubImage1D(texture, level, xoffset, x, y, width)

cdef void glGetnUniformfv(GLuint program, GLint location, GLsizei bufSize, GLfloat *params):
    cglGetnUniformfv(program, location, bufSize, params)

cdef void glGetNamedBufferParameteri64v(GLuint buffer, GLenum pname, GLint64 *params):
    cglGetNamedBufferParameteri64v(buffer, pname, params)

cdef void glGetNamedBufferParameteriv(GLuint buffer, GLenum pname, GLint *params):
    cglGetNamedBufferParameteriv(buffer, pname, params)

cdef void glGetVertexArrayiv(GLuint vaobj, GLenum pname, GLint *param):
    cglGetVertexArrayiv(vaobj, pname, param)

cdef void glCopyTextureSubImage2D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint x, GLint y, GLsizei width, GLsizei height):
    cglCopyTextureSubImage2D(texture, level, xoffset, yoffset, x, y, width, height)

cdef void *glMapNamedBuffer(GLuint buffer, GLenum access):
    cglMapNamedBuffer(buffer, access)

cdef void glNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, const void *data):
    cglNamedBufferSubData(buffer, offset, size, data)

cdef void glGetnHistogram(GLenum target, GLboolean reset, GLenum format, GLenum type, GLsizei bufSize, void *values):
    cglGetnHistogram(target, reset, format, type, bufSize, values)

cdef void glNamedFramebufferRenderbuffer(GLuint framebuffer, GLenum attachment, GLenum renderbuffertarget, GLuint renderbuffer):
    cglNamedFramebufferRenderbuffer(framebuffer, attachment, renderbuffertarget, renderbuffer)

cdef void glGetnPixelMapusv(GLenum map, GLsizei bufSize, GLushort *values):
    cglGetnPixelMapusv(map, bufSize, values)

cdef void glGetNamedBufferSubData(GLuint buffer, GLintptr offset, GLsizeiptr size, void *data):
    cglGetNamedBufferSubData(buffer, offset, size, data)

cdef void glReadnPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, GLsizei bufSize, void *data):
    cglReadnPixels(x, y, width, height, format, type, bufSize, data)

cdef void glCompressedTextureSubImage1D(GLuint texture, GLint level, GLint xoffset, GLsizei width, GLenum format, GLsizei imageSize, const void *data):
    cglCompressedTextureSubImage1D(texture, level, xoffset, width, format, imageSize, data)

cdef void glGetTextureParameterIiv(GLuint texture, GLenum pname, GLint *params):
    cglGetTextureParameterIiv(texture, pname, params)

cdef void glGetnMapfv(GLenum target, GLenum query, GLsizei bufSize, GLfloat *v):
    cglGetnMapfv(target, query, bufSize, v)

cdef void glGetnPixelMapuiv(GLenum map, GLsizei bufSize, GLuint *values):
    cglGetnPixelMapuiv(map, bufSize, values)

cdef void glCopyNamedBufferSubData(GLuint readBuffer, GLuint writeBuffer, GLintptr readOffset, GLintptr writeOffset, GLsizeiptr size):
    cglCopyNamedBufferSubData(readBuffer, writeBuffer, readOffset, writeOffset, size)

cdef void glGenerateTextureMipmap(GLuint texture):
    cglGenerateTextureMipmap(texture)

cdef void glTextureSubImage3D(GLuint texture, GLint level, GLint xoffset, GLint yoffset, GLint zoffset, GLsizei width, GLsizei height, GLsizei depth, GLenum format, GLenum type, const void *pixels):
    cglTextureSubImage3D(texture, level, xoffset, yoffset, zoffset, width, height, depth, format, type, pixels)

cdef void glGetTransformFeedbackiv(GLuint xfb, GLenum pname, GLint *param):
    cglGetTransformFeedbackiv(xfb, pname, param)

cdef void glEnableVertexArrayAttrib(GLuint vaobj, GLuint index):
    cglEnableVertexArrayAttrib(vaobj, index)

cdef void glInvalidateNamedFramebufferData(GLuint framebuffer, GLsizei numAttachments, const GLenum *attachments):
    cglInvalidateNamedFramebufferData(framebuffer, numAttachments, attachments)

cdef void glVertexArrayAttribIFormat(GLuint vaobj, GLuint attribindex, GLint size, GLenum type, GLuint relativeoffset):
    cglVertexArrayAttribIFormat(vaobj, attribindex, size, type, relativeoffset)

cdef void glNamedFramebufferTexture(GLuint framebuffer, GLenum attachment, GLuint texture, GLint level):
    cglNamedFramebufferTexture(framebuffer, attachment, texture, level)
