ctypedef unsigned int GLenum
ctypedef unsigned char GLboolean
ctypedef unsigned int GLbitfield
ctypedef void GLvoid
ctypedef signed char GLbyte
ctypedef short GLshort
ctypedef int GLint
ctypedef int GLclampx
ctypedef unsigned char GLubyte
ctypedef unsigned short GLushort
ctypedef unsigned int GLuint
ctypedef int GLsizei
ctypedef float GLfloat
ctypedef float GLclampf
ctypedef double GLdouble
ctypedef double GLclampd
ctypedef void *GLeglClientBufferEXT
ctypedef void *GLeglImageOES
ctypedef char GLchar
ctypedef char GLcharARB
ctypedef int GLhandleARB
ctypedef unsigned short GLhalfARB
ctypedef unsigned short GLhalf
ctypedef GLint GLfixed
ctypedef int * GLintptr
ctypedef int GLsizeiptr
ctypedef int GLint64
ctypedef int GLuint64
ctypedef ptrdiff_t GLintptrARB
ctypedef ptrdiff_t GLsizeiptrARB
ctypedef int GLint64EXT
ctypedef int GLuint64EXT
ctypedef int *GLsync
ctypedef void ( *GLDEBUGPROC)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,const void *userParam)
ctypedef void ( *GLDEBUGPROCARB)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,const void *userParam)
ctypedef void ( *GLDEBUGPROCKHR)(GLenum source,GLenum type,GLuint id,GLenum severity,GLsizei length,const GLchar *message,const void *userParam)
ctypedef void ( *GLDEBUGPROCAMD)(GLuint id,GLenum category,GLenum severity,GLsizei length,const GLchar *message,void *userParam)
ctypedef unsigned short GLhalfNV
ctypedef GLintptr GLvdpauSurfaceNV
ctypedef void ( *GLVULKANPROCNV)()

cdef GLenum GL_2D
cdef GLenum GL_2_BYTES
cdef GLenum GL_3D
cdef GLenum GL_3D_COLOR
cdef GLenum GL_3D_COLOR_TEXTURE
cdef GLenum GL_3_BYTES
cdef GLenum GL_4D_COLOR_TEXTURE
cdef GLenum GL_4_BYTES
cdef GLenum GL_ACCUM
cdef GLenum GL_ACCUM_ALPHA_BITS
cdef GLenum GL_ACCUM_BLUE_BITS
cdef GLenum GL_ACCUM_BUFFER_BIT
cdef GLenum GL_ACCUM_CLEAR_VALUE
cdef GLenum GL_ACCUM_GREEN_BITS
cdef GLenum GL_ACCUM_RED_BITS
cdef GLenum GL_ADD
cdef GLenum GL_ALL_ATTRIB_BITS
cdef GLenum GL_ALPHA
cdef GLenum GL_ALPHA_BIAS
cdef GLenum GL_ALPHA_BITS
cdef GLenum GL_ALPHA_SCALE
cdef GLenum GL_ALPHA_TEST
cdef GLenum GL_ALPHA_TEST_FUNC
cdef GLenum GL_ALPHA_TEST_REF
cdef GLenum GL_ALWAYS
cdef GLenum GL_AMBIENT
cdef GLenum GL_AMBIENT_AND_DIFFUSE
cdef GLenum GL_AND
cdef GLenum GL_AND_INVERTED
cdef GLenum GL_AND_REVERSE
cdef GLenum GL_ATTRIB_STACK_DEPTH
cdef GLenum GL_AUTO_NORMAL
cdef GLenum GL_AUX0
cdef GLenum GL_AUX1
cdef GLenum GL_AUX2
cdef GLenum GL_AUX3
cdef GLenum GL_AUX_BUFFERS
cdef GLenum GL_BACK
cdef GLenum GL_BACK_LEFT
cdef GLenum GL_BACK_RIGHT
cdef GLenum GL_BITMAP
cdef GLenum GL_BITMAP_TOKEN
cdef GLenum GL_BLEND
cdef GLenum GL_BLEND_DST
cdef GLenum GL_BLEND_SRC
cdef GLenum GL_BLUE
cdef GLenum GL_BLUE_BIAS
cdef GLenum GL_BLUE_BITS
cdef GLenum GL_BLUE_SCALE
cdef GLenum GL_BYTE
cdef GLenum GL_CCW
cdef GLenum GL_CLAMP
cdef GLenum GL_CLEAR
cdef GLenum GL_CLIP_PLANE0
cdef GLenum GL_CLIP_PLANE1
cdef GLenum GL_CLIP_PLANE2
cdef GLenum GL_CLIP_PLANE3
cdef GLenum GL_CLIP_PLANE4
cdef GLenum GL_CLIP_PLANE5
cdef GLenum GL_COEFF
cdef GLenum GL_COLOR
cdef GLenum GL_COLOR_BUFFER_BIT
cdef GLenum GL_COLOR_CLEAR_VALUE
cdef GLenum GL_COLOR_INDEX
cdef GLenum GL_COLOR_INDEXES
cdef GLenum GL_COLOR_MATERIAL
cdef GLenum GL_COLOR_MATERIAL_FACE
cdef GLenum GL_COLOR_MATERIAL_PARAMETER
cdef GLenum GL_COLOR_WRITEMASK
cdef GLenum GL_COMPILE
cdef GLenum GL_COMPILE_AND_EXECUTE
cdef GLenum GL_CONSTANT_ATTENUATION
cdef GLenum GL_COPY
cdef GLenum GL_COPY_INVERTED
cdef GLenum GL_COPY_PIXEL_TOKEN
cdef GLenum GL_CULL_FACE
cdef GLenum GL_CULL_FACE_MODE
cdef GLenum GL_CURRENT_BIT
cdef GLenum GL_CURRENT_COLOR
cdef GLenum GL_CURRENT_INDEX
cdef GLenum GL_CURRENT_NORMAL
cdef GLenum GL_CURRENT_RASTER_COLOR
cdef GLenum GL_CURRENT_RASTER_DISTANCE
cdef GLenum GL_CURRENT_RASTER_INDEX
cdef GLenum GL_CURRENT_RASTER_POSITION
cdef GLenum GL_CURRENT_RASTER_POSITION_VALID
cdef GLenum GL_CURRENT_RASTER_TEXTURE_COORDS
cdef GLenum GL_CURRENT_TEXTURE_COORDS
cdef GLenum GL_CW
cdef GLenum GL_DECAL
cdef GLenum GL_DECR
cdef GLenum GL_DEPTH
cdef GLenum GL_DEPTH_BIAS
cdef GLenum GL_DEPTH_BITS
cdef GLenum GL_DEPTH_BUFFER_BIT
cdef GLenum GL_DEPTH_CLEAR_VALUE
cdef GLenum GL_DEPTH_COMPONENT
cdef GLenum GL_DEPTH_FUNC
cdef GLenum GL_DEPTH_RANGE
cdef GLenum GL_DEPTH_SCALE
cdef GLenum GL_DEPTH_TEST
cdef GLenum GL_DEPTH_WRITEMASK
cdef GLenum GL_DIFFUSE
cdef GLenum GL_DITHER
cdef GLenum GL_DOMAIN
cdef GLenum GL_DONT_CARE
cdef GLenum GL_DOUBLEBUFFER
cdef GLenum GL_DRAW_BUFFER
cdef GLenum GL_DRAW_PIXEL_TOKEN
cdef GLenum GL_DST_ALPHA
cdef GLenum GL_DST_COLOR
cdef GLenum GL_EDGE_FLAG
cdef GLenum GL_EMISSION
cdef GLenum GL_ENABLE_BIT
cdef GLenum GL_EQUAL
cdef GLenum GL_EQUIV
cdef GLenum GL_EVAL_BIT
cdef GLenum GL_EXP
cdef GLenum GL_EXP2
cdef GLenum GL_EXTENSIONS
cdef GLenum GL_EYE_LINEAR
cdef GLenum GL_EYE_PLANE
cdef GLenum GL_FALSE
cdef GLenum GL_FASTEST
cdef GLenum GL_FEEDBACK
cdef GLenum GL_FILL
cdef GLenum GL_FLAT
cdef GLenum GL_FLOAT
cdef GLenum GL_FOG
cdef GLenum GL_FOG_BIT
cdef GLenum GL_FOG_COLOR
cdef GLenum GL_FOG_DENSITY
cdef GLenum GL_FOG_END
cdef GLenum GL_FOG_HINT
cdef GLenum GL_FOG_INDEX
cdef GLenum GL_FOG_MODE
cdef GLenum GL_FOG_START
cdef GLenum GL_FRONT
cdef GLenum GL_FRONT_AND_BACK
cdef GLenum GL_FRONT_FACE
cdef GLenum GL_FRONT_LEFT
cdef GLenum GL_FRONT_RIGHT
cdef GLenum GL_GEQUAL
cdef GLenum GL_GREATER
cdef GLenum GL_GREEN
cdef GLenum GL_GREEN_BIAS
cdef GLenum GL_GREEN_BITS
cdef GLenum GL_GREEN_SCALE
cdef GLenum GL_HINT_BIT
cdef GLenum GL_INCR
cdef GLenum GL_INDEX_BITS
cdef GLenum GL_INDEX_CLEAR_VALUE
cdef GLenum GL_INDEX_MODE
cdef GLenum GL_INDEX_OFFSET
cdef GLenum GL_INDEX_SHIFT
cdef GLenum GL_INDEX_WRITEMASK
cdef GLenum GL_INT
cdef GLenum GL_INVALID_ENUM
cdef GLenum GL_INVALID_OPERATION
cdef GLenum GL_INVALID_VALUE
cdef GLenum GL_INVERT
cdef GLenum GL_KEEP
cdef GLenum GL_LEFT
cdef GLenum GL_LEQUAL
cdef GLenum GL_LESS
cdef GLenum GL_LIGHT0
cdef GLenum GL_LIGHT1
cdef GLenum GL_LIGHT2
cdef GLenum GL_LIGHT3
cdef GLenum GL_LIGHT4
cdef GLenum GL_LIGHT5
cdef GLenum GL_LIGHT6
cdef GLenum GL_LIGHT7
cdef GLenum GL_LIGHTING
cdef GLenum GL_LIGHTING_BIT
cdef GLenum GL_LIGHT_MODEL_AMBIENT
cdef GLenum GL_LIGHT_MODEL_LOCAL_VIEWER
cdef GLenum GL_LIGHT_MODEL_TWO_SIDE
cdef GLenum GL_LINE
cdef GLenum GL_LINEAR
cdef GLenum GL_LINEAR_ATTENUATION
cdef GLenum GL_LINEAR_MIPMAP_LINEAR
cdef GLenum GL_LINEAR_MIPMAP_NEAREST
cdef GLenum GL_LINES
cdef GLenum GL_LINE_BIT
cdef GLenum GL_LINE_LOOP
cdef GLenum GL_LINE_RESET_TOKEN
cdef GLenum GL_LINE_SMOOTH
cdef GLenum GL_LINE_SMOOTH_HINT
cdef GLenum GL_LINE_STIPPLE
cdef GLenum GL_LINE_STIPPLE_PATTERN
cdef GLenum GL_LINE_STIPPLE_REPEAT
cdef GLenum GL_LINE_STRIP
cdef GLenum GL_LINE_TOKEN
cdef GLenum GL_LINE_WIDTH
cdef GLenum GL_LINE_WIDTH_GRANULARITY
cdef GLenum GL_LINE_WIDTH_RANGE
cdef GLenum GL_LIST_BASE
cdef GLenum GL_LIST_BIT
cdef GLenum GL_LIST_INDEX
cdef GLenum GL_LIST_MODE
cdef GLenum GL_LOAD
cdef GLenum GL_LOGIC_OP
cdef GLenum GL_LOGIC_OP_MODE
cdef GLenum GL_LUMINANCE
cdef GLenum GL_LUMINANCE_ALPHA
cdef GLenum GL_MAP1_COLOR_4
cdef GLenum GL_MAP1_GRID_DOMAIN
cdef GLenum GL_MAP1_GRID_SEGMENTS
cdef GLenum GL_MAP1_INDEX
cdef GLenum GL_MAP1_NORMAL
cdef GLenum GL_MAP1_TEXTURE_COORD_1
cdef GLenum GL_MAP1_TEXTURE_COORD_2
cdef GLenum GL_MAP1_TEXTURE_COORD_3
cdef GLenum GL_MAP1_TEXTURE_COORD_4
cdef GLenum GL_MAP1_VERTEX_3
cdef GLenum GL_MAP1_VERTEX_4
cdef GLenum GL_MAP2_COLOR_4
cdef GLenum GL_MAP2_GRID_DOMAIN
cdef GLenum GL_MAP2_GRID_SEGMENTS
cdef GLenum GL_MAP2_INDEX
cdef GLenum GL_MAP2_NORMAL
cdef GLenum GL_MAP2_TEXTURE_COORD_1
cdef GLenum GL_MAP2_TEXTURE_COORD_2
cdef GLenum GL_MAP2_TEXTURE_COORD_3
cdef GLenum GL_MAP2_TEXTURE_COORD_4
cdef GLenum GL_MAP2_VERTEX_3
cdef GLenum GL_MAP2_VERTEX_4
cdef GLenum GL_MAP_COLOR
cdef GLenum GL_MAP_STENCIL
cdef GLenum GL_MATRIX_MODE
cdef GLenum GL_MAX_ATTRIB_STACK_DEPTH
cdef GLenum GL_MAX_CLIP_PLANES
cdef GLenum GL_MAX_EVAL_ORDER
cdef GLenum GL_MAX_LIGHTS
cdef GLenum GL_MAX_LIST_NESTING
cdef GLenum GL_MAX_MODELVIEW_STACK_DEPTH
cdef GLenum GL_MAX_NAME_STACK_DEPTH
cdef GLenum GL_MAX_PIXEL_MAP_TABLE
cdef GLenum GL_MAX_PROJECTION_STACK_DEPTH
cdef GLenum GL_MAX_TEXTURE_SIZE
cdef GLenum GL_MAX_TEXTURE_STACK_DEPTH
cdef GLenum GL_MAX_VIEWPORT_DIMS
cdef GLenum GL_MODELVIEW
cdef GLenum GL_MODELVIEW_MATRIX
cdef GLenum GL_MODELVIEW_STACK_DEPTH
cdef GLenum GL_MODULATE
cdef GLenum GL_MULT
cdef GLenum GL_NAME_STACK_DEPTH
cdef GLenum GL_NAND
cdef GLenum GL_NEAREST
cdef GLenum GL_NEAREST_MIPMAP_LINEAR
cdef GLenum GL_NEAREST_MIPMAP_NEAREST
cdef GLenum GL_NEVER
cdef GLenum GL_NICEST
cdef GLenum GL_NONE
cdef GLenum GL_NOOP
cdef GLenum GL_NOR
cdef GLenum GL_NORMALIZE
cdef GLenum GL_NOTEQUAL
cdef GLenum GL_NO_ERROR
cdef GLenum GL_OBJECT_LINEAR
cdef GLenum GL_OBJECT_PLANE
cdef GLenum GL_ONE
cdef GLenum GL_ONE_MINUS_DST_ALPHA
cdef GLenum GL_ONE_MINUS_DST_COLOR
cdef GLenum GL_ONE_MINUS_SRC_ALPHA
cdef GLenum GL_ONE_MINUS_SRC_COLOR
cdef GLenum GL_OR
cdef GLenum GL_ORDER
cdef GLenum GL_OR_INVERTED
cdef GLenum GL_OR_REVERSE
cdef GLenum GL_OUT_OF_MEMORY
cdef GLenum GL_PACK_ALIGNMENT
cdef GLenum GL_PACK_LSB_FIRST
cdef GLenum GL_PACK_ROW_LENGTH
cdef GLenum GL_PACK_SKIP_PIXELS
cdef GLenum GL_PACK_SKIP_ROWS
cdef GLenum GL_PACK_SWAP_BYTES
cdef GLenum GL_PASS_THROUGH_TOKEN
cdef GLenum GL_PERSPECTIVE_CORRECTION_HINT
cdef GLenum GL_PIXEL_MAP_A_TO_A
cdef GLenum GL_PIXEL_MAP_A_TO_A_SIZE
cdef GLenum GL_PIXEL_MAP_B_TO_B
cdef GLenum GL_PIXEL_MAP_B_TO_B_SIZE
cdef GLenum GL_PIXEL_MAP_G_TO_G
cdef GLenum GL_PIXEL_MAP_G_TO_G_SIZE
cdef GLenum GL_PIXEL_MAP_I_TO_A
cdef GLenum GL_PIXEL_MAP_I_TO_A_SIZE
cdef GLenum GL_PIXEL_MAP_I_TO_B
cdef GLenum GL_PIXEL_MAP_I_TO_B_SIZE
cdef GLenum GL_PIXEL_MAP_I_TO_G
cdef GLenum GL_PIXEL_MAP_I_TO_G_SIZE
cdef GLenum GL_PIXEL_MAP_I_TO_I
cdef GLenum GL_PIXEL_MAP_I_TO_I_SIZE
cdef GLenum GL_PIXEL_MAP_I_TO_R
cdef GLenum GL_PIXEL_MAP_I_TO_R_SIZE
cdef GLenum GL_PIXEL_MAP_R_TO_R
cdef GLenum GL_PIXEL_MAP_R_TO_R_SIZE
cdef GLenum GL_PIXEL_MAP_S_TO_S
cdef GLenum GL_PIXEL_MAP_S_TO_S_SIZE
cdef GLenum GL_PIXEL_MODE_BIT
cdef GLenum GL_POINT
cdef GLenum GL_POINTS
cdef GLenum GL_POINT_BIT
cdef GLenum GL_POINT_SIZE
cdef GLenum GL_POINT_SIZE_GRANULARITY
cdef GLenum GL_POINT_SIZE_RANGE
cdef GLenum GL_POINT_SMOOTH
cdef GLenum GL_POINT_SMOOTH_HINT
cdef GLenum GL_POINT_TOKEN
cdef GLenum GL_POLYGON
cdef GLenum GL_POLYGON_BIT
cdef GLenum GL_POLYGON_MODE
cdef GLenum GL_POLYGON_SMOOTH
cdef GLenum GL_POLYGON_SMOOTH_HINT
cdef GLenum GL_POLYGON_STIPPLE
cdef GLenum GL_POLYGON_STIPPLE_BIT
cdef GLenum GL_POLYGON_TOKEN
cdef GLenum GL_POSITION
cdef GLenum GL_PROJECTION
cdef GLenum GL_PROJECTION_MATRIX
cdef GLenum GL_PROJECTION_STACK_DEPTH
cdef GLenum GL_Q
cdef GLenum GL_QUADRATIC_ATTENUATION
cdef GLenum GL_QUADS
cdef GLenum GL_QUAD_STRIP
cdef GLenum GL_R
cdef GLenum GL_READ_BUFFER
cdef GLenum GL_RED
cdef GLenum GL_RED_BIAS
cdef GLenum GL_RED_BITS
cdef GLenum GL_RED_SCALE
cdef GLenum GL_RENDER
cdef GLenum GL_RENDERER
cdef GLenum GL_RENDER_MODE
cdef GLenum GL_REPEAT
cdef GLenum GL_REPLACE
cdef GLenum GL_RETURN
cdef GLenum GL_RGB
cdef GLenum GL_RGBA
cdef GLenum GL_RGBA_MODE
cdef GLenum GL_RIGHT
cdef GLenum GL_S
cdef GLenum GL_SCISSOR_BIT
cdef GLenum GL_SCISSOR_BOX
cdef GLenum GL_SCISSOR_TEST
cdef GLenum GL_SELECT
cdef GLenum GL_SET
cdef GLenum GL_SHADE_MODEL
cdef GLenum GL_SHININESS
cdef GLenum GL_SHORT
cdef GLenum GL_SMOOTH
cdef GLenum GL_SPECULAR
cdef GLenum GL_SPHERE_MAP
cdef GLenum GL_SPOT_CUTOFF
cdef GLenum GL_SPOT_DIRECTION
cdef GLenum GL_SPOT_EXPONENT
cdef GLenum GL_SRC_ALPHA
cdef GLenum GL_SRC_ALPHA_SATURATE
cdef GLenum GL_SRC_COLOR
cdef GLenum GL_STACK_OVERFLOW
cdef GLenum GL_STACK_UNDERFLOW
cdef GLenum GL_STENCIL
cdef GLenum GL_STENCIL_BITS
cdef GLenum GL_STENCIL_BUFFER_BIT
cdef GLenum GL_STENCIL_CLEAR_VALUE
cdef GLenum GL_STENCIL_FAIL
cdef GLenum GL_STENCIL_FUNC
cdef GLenum GL_STENCIL_INDEX
cdef GLenum GL_STENCIL_PASS_DEPTH_FAIL
cdef GLenum GL_STENCIL_PASS_DEPTH_PASS
cdef GLenum GL_STENCIL_REF
cdef GLenum GL_STENCIL_TEST
cdef GLenum GL_STENCIL_VALUE_MASK
cdef GLenum GL_STENCIL_WRITEMASK
cdef GLenum GL_STEREO
cdef GLenum GL_SUBPIXEL_BITS
cdef GLenum GL_T
cdef GLenum GL_TEXTURE
cdef GLenum GL_TEXTURE_1D
cdef GLenum GL_TEXTURE_2D
cdef GLenum GL_TEXTURE_BIT
cdef GLenum GL_TEXTURE_BORDER
cdef GLenum GL_TEXTURE_BORDER_COLOR
cdef GLenum GL_TEXTURE_COMPONENTS
cdef GLenum GL_TEXTURE_ENV
cdef GLenum GL_TEXTURE_ENV_COLOR
cdef GLenum GL_TEXTURE_ENV_MODE
cdef GLenum GL_TEXTURE_GEN_MODE
cdef GLenum GL_TEXTURE_GEN_Q
cdef GLenum GL_TEXTURE_GEN_R
cdef GLenum GL_TEXTURE_GEN_S
cdef GLenum GL_TEXTURE_GEN_T
cdef GLenum GL_TEXTURE_HEIGHT
cdef GLenum GL_TEXTURE_MAG_FILTER
cdef GLenum GL_TEXTURE_MATRIX
cdef GLenum GL_TEXTURE_MIN_FILTER
cdef GLenum GL_TEXTURE_STACK_DEPTH
cdef GLenum GL_TEXTURE_WIDTH
cdef GLenum GL_TEXTURE_WRAP_S
cdef GLenum GL_TEXTURE_WRAP_T
cdef GLenum GL_TRANSFORM_BIT
cdef GLenum GL_TRIANGLES
cdef GLenum GL_TRIANGLE_FAN
cdef GLenum GL_TRIANGLE_STRIP
cdef GLenum GL_TRUE
cdef GLenum GL_UNPACK_ALIGNMENT
cdef GLenum GL_UNPACK_LSB_FIRST
cdef GLenum GL_UNPACK_ROW_LENGTH
cdef GLenum GL_UNPACK_SKIP_PIXELS
cdef GLenum GL_UNPACK_SKIP_ROWS
cdef GLenum GL_UNPACK_SWAP_BYTES
cdef GLenum GL_UNSIGNED_BYTE
cdef GLenum GL_UNSIGNED_INT
cdef GLenum GL_UNSIGNED_SHORT
cdef GLenum GL_VENDOR
cdef GLenum GL_VERSION
cdef GLenum GL_VIEWPORT
cdef GLenum GL_VIEWPORT_BIT
cdef GLenum GL_XOR
cdef GLenum GL_ZERO
cdef GLenum GL_ZOOM_X
cdef GLenum GL_ZOOM_Y
cdef void glAccum(GLenum op, GLfloat value)
cdef void glAlphaFunc(GLenum func, GLfloat ref)
cdef void glBegin(GLenum mode)
cdef void glBitmap(GLsizei width, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte *bitmap)
cdef void glBlendFunc(GLenum sfactor, GLenum dfactor)
cdef void glCallList(GLuint list)
cdef void glCallLists(GLsizei n, GLenum type, const void *lists)
cdef void glClear(GLbitfield mask)
cdef void glClearAccum(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
cdef void glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
cdef void glClearDepth(GLdouble depth)
cdef void glClearIndex(GLfloat c)
cdef void glClearStencil(GLint s)
cdef void glClipPlane(GLenum plane, const GLdouble *equation)
cdef void glColor3b(GLbyte red, GLbyte green, GLbyte blue)
cdef void glColor3bv(const GLbyte *v)
cdef void glColor3d(GLdouble red, GLdouble green, GLdouble blue)
cdef void glColor3dv(const GLdouble *v)
cdef void glColor3f(GLfloat red, GLfloat green, GLfloat blue)
cdef void glColor3fv(const GLfloat *v)
cdef void glColor3i(GLint red, GLint green, GLint blue)
cdef void glColor3iv(const GLint *v)
cdef void glColor3s(GLshort red, GLshort green, GLshort blue)
cdef void glColor3sv(const GLshort *v)
cdef void glColor3ub(GLubyte red, GLubyte green, GLubyte blue)
cdef void glColor3ubv(const GLubyte *v)
cdef void glColor3ui(GLuint red, GLuint green, GLuint blue)
cdef void glColor3uiv(const GLuint *v)
cdef void glColor3us(GLushort red, GLushort green, GLushort blue)
cdef void glColor3usv(const GLushort *v)
cdef void glColor4b(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha)
cdef void glColor4bv(const GLbyte *v)
cdef void glColor4d(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha)
cdef void glColor4dv(const GLdouble *v)
cdef void glColor4f(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
cdef void glColor4fv(const GLfloat *v)
cdef void glColor4i(GLint red, GLint green, GLint blue, GLint alpha)
cdef void glColor4iv(const GLint *v)
cdef void glColor4s(GLshort red, GLshort green, GLshort blue, GLshort alpha)
cdef void glColor4sv(const GLshort *v)
cdef void glColor4ub(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha)
cdef void glColor4ubv(const GLubyte *v)
cdef void glColor4ui(GLuint red, GLuint green, GLuint blue, GLuint alpha)
cdef void glColor4uiv(const GLuint *v)
cdef void glColor4us(GLushort red, GLushort green, GLushort blue, GLushort alpha)
cdef void glColor4usv(const GLushort *v)
cdef void glColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha)
cdef void glColorMaterial(GLenum face, GLenum mode)
cdef void glCopyPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum type)
cdef void glCullFace(GLenum mode)
cdef void glDeleteLists(GLuint list, GLsizei range)
cdef void glDepthFunc(GLenum func)
cdef void glDepthMask(GLboolean flag)
cdef void glDepthRange(GLdouble n, GLdouble f)
cdef void glDisable(GLenum cap)
cdef void glDrawBuffer(GLenum buf)
cdef void glDrawPixels(GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
cdef void glEdgeFlag(GLboolean flag)
cdef void glEdgeFlagv(const GLboolean *flag)
cdef void glEnable(GLenum cap)
cdef void glEnd()
cdef void glEndList()
cdef void glEvalCoord1d(GLdouble u)
cdef void glEvalCoord1dv(const GLdouble *u)
cdef void glEvalCoord1f(GLfloat u)
cdef void glEvalCoord1fv(const GLfloat *u)
cdef void glEvalCoord2d(GLdouble u, GLdouble v)
cdef void glEvalCoord2dv(const GLdouble *u)
cdef void glEvalCoord2f(GLfloat u, GLfloat v)
cdef void glEvalCoord2fv(const GLfloat *u)
cdef void glEvalMesh1(GLenum mode, GLint i1, GLint i2)
cdef void glEvalMesh2(GLenum mode, GLint i1, GLint i2, GLint j1, GLint j2)
cdef void glEvalPoint1(GLint i)
cdef void glEvalPoint2(GLint i, GLint j)
cdef void glFeedbackBuffer(GLsizei size, GLenum type, GLfloat *buffer)
cdef void glFinish()
cdef void glFlush()
cdef void glFogf(GLenum pname, GLfloat param)
cdef void glFogfv(GLenum pname, const GLfloat *params)
cdef void glFogi(GLenum pname, GLint param)
cdef void glFogiv(GLenum pname, const GLint *params)
cdef void glFrontFace(GLenum mode)
cdef void glFrustum(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
cdef GLuint glGenLists(GLsizei range)
cdef void glGetBooleanv(GLenum pname, GLboolean *data)
cdef void glGetClipPlane(GLenum plane, GLdouble *equation)
cdef void glGetDoublev(GLenum pname, GLdouble *data)
cdef GLenum glGetError()
cdef void glGetFloatv(GLenum pname, GLfloat *data)
cdef void glGetIntegerv(GLenum pname, GLint *data)
cdef void glGetLightfv(GLenum light, GLenum pname, GLfloat *params)
cdef void glGetLightiv(GLenum light, GLenum pname, GLint *params)
cdef void glGetMapdv(GLenum target, GLenum query, GLdouble *v)
cdef void glGetMapfv(GLenum target, GLenum query, GLfloat *v)
cdef void glGetMapiv(GLenum target, GLenum query, GLint *v)
cdef void glGetMaterialfv(GLenum face, GLenum pname, GLfloat *params)
cdef void glGetMaterialiv(GLenum face, GLenum pname, GLint *params)
cdef void glGetPixelMapfv(GLenum map, GLfloat *values)
cdef void glGetPixelMapuiv(GLenum map, GLuint *values)
cdef void glGetPixelMapusv(GLenum map, GLushort *values)
cdef void glGetPolygonStipple(GLubyte *mask)
cdef const GLubyte *glGetString(GLenum name)
cdef void glGetTexEnvfv(GLenum target, GLenum pname, GLfloat *params)
cdef void glGetTexEnviv(GLenum target, GLenum pname, GLint *params)
cdef void glGetTexGendv(GLenum coord, GLenum pname, GLdouble *params)
cdef void glGetTexGenfv(GLenum coord, GLenum pname, GLfloat *params)
cdef void glGetTexGeniv(GLenum coord, GLenum pname, GLint *params)
cdef void glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type, void *pixels)
cdef void glGetTexLevelParameterfv(GLenum target, GLint level, GLenum pname, GLfloat *params)
cdef void glGetTexLevelParameteriv(GLenum target, GLint level, GLenum pname, GLint *params)
cdef void glGetTexParameterfv(GLenum target, GLenum pname, GLfloat *params)
cdef void glGetTexParameteriv(GLenum target, GLenum pname, GLint *params)
cdef void glHint(GLenum target, GLenum mode)
cdef void glIndexMask(GLuint mask)
cdef void glIndexd(GLdouble c)
cdef void glIndexdv(const GLdouble *c)
cdef void glIndexf(GLfloat c)
cdef void glIndexfv(const GLfloat *c)
cdef void glIndexi(GLint c)
cdef void glIndexiv(const GLint *c)
cdef void glIndexs(GLshort c)
cdef void glIndexsv(const GLshort *c)
cdef void glInitNames()
cdef GLboolean glIsEnabled(GLenum cap)
cdef GLboolean glIsList(GLuint list)
cdef void glLightModelf(GLenum pname, GLfloat param)
cdef void glLightModelfv(GLenum pname, const GLfloat *params)
cdef void glLightModeli(GLenum pname, GLint param)
cdef void glLightModeliv(GLenum pname, const GLint *params)
cdef void glLightf(GLenum light, GLenum pname, GLfloat param)
cdef void glLightfv(GLenum light, GLenum pname, const GLfloat *params)
cdef void glLighti(GLenum light, GLenum pname, GLint param)
cdef void glLightiv(GLenum light, GLenum pname, const GLint *params)
cdef void glLineStipple(GLint factor, GLushort pattern)
cdef void glLineWidth(GLfloat width)
cdef void glListBase(GLuint base)
cdef void glLoadIdentity()
cdef void glLoadMatrixd(const GLdouble *m)
cdef void glLoadMatrixf(const GLfloat *m)
cdef void glLoadName(GLuint name)
cdef void glLogicOp(GLenum opcode)
cdef void glMap1d(GLenum target, GLdouble u1, GLdouble u2, GLint stride, GLint order, const GLdouble *points)
cdef void glMap1f(GLenum target, GLfloat u1, GLfloat u2, GLint stride, GLint order, const GLfloat *points)
cdef void glMap2d(GLenum target, GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint vstride, GLint vorder, const GLdouble *points)
cdef void glMap2f(GLenum target, GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride, GLint vorder, const GLfloat *points)
cdef void glMapGrid1d(GLint un, GLdouble u1, GLdouble u2)
cdef void glMapGrid1f(GLint un, GLfloat u1, GLfloat u2)
cdef void glMapGrid2d(GLint un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)
cdef void glMapGrid2f(GLint un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)
cdef void glMaterialf(GLenum face, GLenum pname, GLfloat param)
cdef void glMaterialfv(GLenum face, GLenum pname, const GLfloat *params)
cdef void glMateriali(GLenum face, GLenum pname, GLint param)
cdef void glMaterialiv(GLenum face, GLenum pname, const GLint *params)
cdef void glMatrixMode(GLenum mode)
cdef void glMultMatrixd(const GLdouble *m)
cdef void glMultMatrixf(const GLfloat *m)
cdef void glNewList(GLuint list, GLenum mode)
cdef void glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz)
cdef void glNormal3bv(const GLbyte *v)
cdef void glNormal3d(GLdouble nx, GLdouble ny, GLdouble nz)
cdef void glNormal3dv(const GLdouble *v)
cdef void glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz)
cdef void glNormal3fv(const GLfloat *v)
cdef void glNormal3i(GLint nx, GLint ny, GLint nz)
cdef void glNormal3iv(const GLint *v)
cdef void glNormal3s(GLshort nx, GLshort ny, GLshort nz)
cdef void glNormal3sv(const GLshort *v)
cdef void glOrtho(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
cdef void glPassThrough(GLfloat token)
cdef void glPixelMapfv(GLenum map, GLsizei mapsize, const GLfloat *values)
cdef void glPixelMapuiv(GLenum map, GLsizei mapsize, const GLuint *values)
cdef void glPixelMapusv(GLenum map, GLsizei mapsize, const GLushort *values)
cdef void glPixelStoref(GLenum pname, GLfloat param)
cdef void glPixelStorei(GLenum pname, GLint param)
cdef void glPixelTransferf(GLenum pname, GLfloat param)
cdef void glPixelTransferi(GLenum pname, GLint param)
cdef void glPixelZoom(GLfloat xfactor, GLfloat yfactor)
cdef void glPointSize(GLfloat size)
cdef void glPolygonMode(GLenum face, GLenum mode)
cdef void glPolygonStipple(const GLubyte *mask)
cdef void glPopAttrib()
cdef void glPopMatrix()
cdef void glPopName()
cdef void glPushAttrib(GLbitfield mask)
cdef void glPushMatrix()
cdef void glPushName(GLuint name)
cdef void glRasterPos2d(GLdouble x, GLdouble y)
cdef void glRasterPos2dv(const GLdouble *v)
cdef void glRasterPos2f(GLfloat x, GLfloat y)
cdef void glRasterPos2fv(const GLfloat *v)
cdef void glRasterPos2i(GLint x, GLint y)
cdef void glRasterPos2iv(const GLint *v)
cdef void glRasterPos2s(GLshort x, GLshort y)
cdef void glRasterPos2sv(const GLshort *v)
cdef void glRasterPos3d(GLdouble x, GLdouble y, GLdouble z)
cdef void glRasterPos3dv(const GLdouble *v)
cdef void glRasterPos3f(GLfloat x, GLfloat y, GLfloat z)
cdef void glRasterPos3fv(const GLfloat *v)
cdef void glRasterPos3i(GLint x, GLint y, GLint z)
cdef void glRasterPos3iv(const GLint *v)
cdef void glRasterPos3s(GLshort x, GLshort y, GLshort z)
cdef void glRasterPos3sv(const GLshort *v)
cdef void glRasterPos4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w)
cdef void glRasterPos4dv(const GLdouble *v)
cdef void glRasterPos4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w)
cdef void glRasterPos4fv(const GLfloat *v)
cdef void glRasterPos4i(GLint x, GLint y, GLint z, GLint w)
cdef void glRasterPos4iv(const GLint *v)
cdef void glRasterPos4s(GLshort x, GLshort y, GLshort z, GLshort w)
cdef void glRasterPos4sv(const GLshort *v)
cdef void glReadBuffer(GLenum src)
cdef void glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, void *pixels)
cdef void glRectd(GLdouble x1, GLdouble y1, GLdouble x2, GLdouble y2)
cdef void glRectdv(const GLdouble *v1, const GLdouble *v2)
cdef void glRectf(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2)
cdef void glRectfv(const GLfloat *v1, const GLfloat *v2)
cdef void glRecti(GLint x1, GLint y1, GLint x2, GLint y2)
cdef void glRectiv(const GLint *v1, const GLint *v2)
cdef void glRects(GLshort x1, GLshort y1, GLshort x2, GLshort y2)
cdef void glRectsv(const GLshort *v1, const GLshort *v2)
cdef GLint glRenderMode(GLenum mode)
cdef void glRotated(GLdouble angle, GLdouble x, GLdouble y, GLdouble z)
cdef void glRotatef(GLfloat angle, GLfloat x, GLfloat y, GLfloat z)
cdef void glScaled(GLdouble x, GLdouble y, GLdouble z)
cdef void glScalef(GLfloat x, GLfloat y, GLfloat z)
cdef void glScissor(GLint x, GLint y, GLsizei width, GLsizei height)
cdef void glSelectBuffer(GLsizei size, GLuint *buffer)
cdef void glShadeModel(GLenum mode)
cdef void glStencilFunc(GLenum func, GLint ref, GLuint mask)
cdef void glStencilMask(GLuint mask)
cdef void glStencilOp(GLenum fail, GLenum zfail, GLenum zpass)
cdef void glTexCoord1d(GLdouble s)
cdef void glTexCoord1dv(const GLdouble *v)
cdef void glTexCoord1f(GLfloat s)
cdef void glTexCoord1fv(const GLfloat *v)
cdef void glTexCoord1i(GLint s)
cdef void glTexCoord1iv(const GLint *v)
cdef void glTexCoord1s(GLshort s)
cdef void glTexCoord1sv(const GLshort *v)
cdef void glTexCoord2d(GLdouble s, GLdouble t)
cdef void glTexCoord2dv(const GLdouble *v)
cdef void glTexCoord2f(GLfloat s, GLfloat t)
cdef void glTexCoord2fv(const GLfloat *v)
cdef void glTexCoord2i(GLint s, GLint t)
cdef void glTexCoord2iv(const GLint *v)
cdef void glTexCoord2s(GLshort s, GLshort t)
cdef void glTexCoord2sv(const GLshort *v)
cdef void glTexCoord3d(GLdouble s, GLdouble t, GLdouble r)
cdef void glTexCoord3dv(const GLdouble *v)
cdef void glTexCoord3f(GLfloat s, GLfloat t, GLfloat r)
cdef void glTexCoord3fv(const GLfloat *v)
cdef void glTexCoord3i(GLint s, GLint t, GLint r)
cdef void glTexCoord3iv(const GLint *v)
cdef void glTexCoord3s(GLshort s, GLshort t, GLshort r)
cdef void glTexCoord3sv(const GLshort *v)
cdef void glTexCoord4d(GLdouble s, GLdouble t, GLdouble r, GLdouble q)
cdef void glTexCoord4dv(const GLdouble *v)
cdef void glTexCoord4f(GLfloat s, GLfloat t, GLfloat r, GLfloat q)
cdef void glTexCoord4fv(const GLfloat *v)
cdef void glTexCoord4i(GLint s, GLint t, GLint r, GLint q)
cdef void glTexCoord4iv(const GLint *v)
cdef void glTexCoord4s(GLshort s, GLshort t, GLshort r, GLshort q)
cdef void glTexCoord4sv(const GLshort *v)
cdef void glTexEnvf(GLenum target, GLenum pname, GLfloat param)
cdef void glTexEnvfv(GLenum target, GLenum pname, const GLfloat *params)
cdef void glTexEnvi(GLenum target, GLenum pname, GLint param)
cdef void glTexEnviv(GLenum target, GLenum pname, const GLint *params)
cdef void glTexGend(GLenum coord, GLenum pname, GLdouble param)
cdef void glTexGendv(GLenum coord, GLenum pname, const GLdouble *params)
cdef void glTexGenf(GLenum coord, GLenum pname, GLfloat param)
cdef void glTexGenfv(GLenum coord, GLenum pname, const GLfloat *params)
cdef void glTexGeni(GLenum coord, GLenum pname, GLint param)
cdef void glTexGeniv(GLenum coord, GLenum pname, const GLint *params)
cdef void glTexImage1D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const void *pixels)
cdef void glTexImage2D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *pixels)
cdef void glTexParameterf(GLenum target, GLenum pname, GLfloat param)
cdef void glTexParameterfv(GLenum target, GLenum pname, const GLfloat *params)
cdef void glTexParameteri(GLenum target, GLenum pname, GLint param)
cdef void glTexParameteriv(GLenum target, GLenum pname, const GLint *params)
cdef void glTranslated(GLdouble x, GLdouble y, GLdouble z)
cdef void glTranslatef(GLfloat x, GLfloat y, GLfloat z)
cdef void glVertex2d(GLdouble x, GLdouble y)
cdef void glVertex2dv(const GLdouble *v)
cdef void glVertex2f(GLfloat x, GLfloat y)
cdef void glVertex2fv(const GLfloat *v)
cdef void glVertex2i(GLint x, GLint y)
cdef void glVertex2iv(const GLint *v)
cdef void glVertex2s(GLshort x, GLshort y)
cdef void glVertex2sv(const GLshort *v)
cdef void glVertex3d(GLdouble x, GLdouble y, GLdouble z)
cdef void glVertex3dv(const GLdouble *v)
cdef void glVertex3f(GLfloat x, GLfloat y, GLfloat z)
cdef void glVertex3fv(const GLfloat *v)
cdef void glVertex3i(GLint x, GLint y, GLint z)
cdef void glVertex3iv(const GLint *v)
cdef void glVertex3s(GLshort x, GLshort y, GLshort z)
cdef void glVertex3sv(const GLshort *v)
cdef void glVertex4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w)
cdef void glVertex4dv(const GLdouble *v)
cdef void glVertex4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w)
cdef void glVertex4fv(const GLfloat *v)
cdef void glVertex4i(GLint x, GLint y, GLint z, GLint w)
cdef void glVertex4iv(const GLint *v)
cdef void glVertex4s(GLshort x, GLshort y, GLshort z, GLshort w)
cdef void glVertex4sv(const GLshort *v)
cdef void glViewport(GLint x, GLint y, GLsizei width, GLsizei height)
