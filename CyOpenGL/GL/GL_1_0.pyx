# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_MAP2_TEXTURE_COORD_2 = 0x0DB4
cdef GLenum GL_XOR = 0x1506
cdef GLenum GL_SHININESS = 0x1601
cdef GLenum GL_READ_BUFFER = 0x0C02
cdef GLenum GL_RENDERER = 0x1F01
cdef GLenum GL_PROJECTION_STACK_DEPTH = 0x0BA4
cdef GLenum GL_ACCUM_GREEN_BITS = 0x0D59
cdef GLenum GL_LIGHT_MODEL_TWO_SIDE = 0x0B52
cdef GLenum GL_COLOR_MATERIAL_PARAMETER = 0x0B56
cdef GLenum GL_LIGHT2 = 0x4002
cdef GLenum GL_NAME_STACK_DEPTH = 0x0D70
cdef GLenum GL_SRC_ALPHA = 0x0302
cdef GLenum GL_TEXTURE_HEIGHT = 0x1001
cdef GLenum GL_POINT_SIZE_GRANULARITY = 0x0B13
cdef GLenum GL_STENCIL_TEST = 0x0B90
cdef GLenum GL_CURRENT_NORMAL = 0x0B02
cdef GLenum GL_UNPACK_SKIP_PIXELS = 0x0CF4
cdef GLenum GL_STENCIL_BUFFER_BIT = 0x00000400
cdef GLenum GL_ALPHA_BIAS = 0x0D1D
cdef GLenum GL_POLYGON_SMOOTH = 0x0B41
cdef GLenum GL_LOAD = 0x0101
cdef GLenum GL_PIXEL_MAP_I_TO_I_SIZE = 0x0CB0
cdef GLenum GL_RED_BITS = 0x0D52
cdef GLenum GL_LIGHT_MODEL_LOCAL_VIEWER = 0x0B51
cdef GLenum GL_ONE = 1
cdef GLenum GL_LINE_WIDTH_GRANULARITY = 0x0B23
cdef GLenum GL_SRC_ALPHA_SATURATE = 0x0308
cdef GLenum GL_LIGHT_MODEL_AMBIENT = 0x0B53
cdef GLenum GL_RENDER_MODE = 0x0C40
cdef GLenum GL_NOOP = 0x1505
cdef GLenum GL_STENCIL_CLEAR_VALUE = 0x0B91
cdef GLenum GL_MAX_PROJECTION_STACK_DEPTH = 0x0D38
cdef GLenum GL_FOG_HINT = 0x0C54
cdef GLenum GL_LINES = 0x0001
cdef GLenum GL_TEXTURE_WIDTH = 0x1000
cdef GLenum GL_GREEN_BIAS = 0x0D19
cdef GLenum GL_NO_ERROR = 0
cdef GLenum GL_DEPTH_RANGE = 0x0B70
cdef GLenum GL_BLEND_SRC = 0x0BE1
cdef GLenum GL_POINT_SMOOTH_HINT = 0x0C51
cdef GLenum GL_PIXEL_MAP_S_TO_S = 0x0C71
cdef GLenum GL_MAX_TEXTURE_SIZE = 0x0D33
cdef GLenum GL_DST_COLOR = 0x0306
cdef GLenum GL_COLOR_CLEAR_VALUE = 0x0C22
cdef GLenum GL_PASS_THROUGH_TOKEN = 0x0700
cdef GLenum GL_STENCIL_WRITEMASK = 0x0B98
cdef GLenum GL_COPY_PIXEL_TOKEN = 0x0706
cdef GLenum GL_DRAW_BUFFER = 0x0C01
cdef GLenum GL_LINE_SMOOTH = 0x0B20
cdef GLenum GL_MAP1_NORMAL = 0x0D92
cdef GLenum GL_MAP2_GRID_SEGMENTS = 0x0DD3
cdef GLenum GL_POLYGON_STIPPLE = 0x0B42
cdef GLenum GL_POINTS = 0x0000
cdef GLenum GL_TEXTURE_MATRIX = 0x0BA8
cdef GLenum GL_CURRENT_RASTER_TEXTURE_COORDS = 0x0B06
cdef GLenum GL_SPHERE_MAP = 0x2402
cdef GLenum GL_RGBA = 0x1908
cdef GLenum GL_INDEX_WRITEMASK = 0x0C21
cdef GLenum GL_POLYGON_BIT = 0x00000008
cdef GLenum GL_PROJECTION_MATRIX = 0x0BA7
cdef GLenum GL_TRIANGLE_FAN = 0x0006
cdef GLenum GL_BLUE_BITS = 0x0D54
cdef GLenum GL_MODELVIEW_STACK_DEPTH = 0x0BA3
cdef GLenum GL_MAX_PIXEL_MAP_TABLE = 0x0D34
cdef GLenum GL_POINT_SIZE = 0x0B11
cdef GLenum GL_MAP1_TEXTURE_COORD_2 = 0x0D94
cdef GLenum GL_VIEWPORT_BIT = 0x00000800
cdef GLenum GL_OR = 0x1507
cdef GLenum GL_COMPILE = 0x1300
cdef GLenum GL_SMOOTH = 0x1D01
cdef GLenum GL_LIGHT6 = 0x4006
cdef GLenum GL_MAP2_VERTEX_3 = 0x0DB7
cdef GLenum GL_MAP1_TEXTURE_COORD_3 = 0x0D95
cdef GLenum GL_FEEDBACK = 0x1C01
cdef GLenum GL_RED_SCALE = 0x0D14
cdef GLenum GL_LIGHTING = 0x0B50
cdef GLenum GL_INDEX_OFFSET = 0x0D13
cdef GLenum GL_TEXTURE_MIN_FILTER = 0x2801
cdef GLenum GL_STACK_UNDERFLOW = 0x0504
cdef GLenum GL_TEXTURE_GEN_Q = 0x0C63
cdef GLenum GL_MAP2_TEXTURE_COORD_4 = 0x0DB6
cdef GLenum GL_INVALID_OPERATION = 0x0502
cdef GLenum GL_FOG_END = 0x0B64
cdef GLenum GL_TEXTURE_GEN_S = 0x0C60
cdef GLenum GL_S = 0x2000
cdef GLenum GL_MAP2_GRID_DOMAIN = 0x0DD2
cdef GLenum GL_MODULATE = 0x2100
cdef GLenum GL_COLOR_INDEXES = 0x1603
cdef GLenum GL_MAP2_VERTEX_4 = 0x0DB8
cdef GLenum GL_SELECT = 0x1C02
cdef GLenum GL_LUMINANCE = 0x1909
cdef GLenum GL_LIGHT7 = 0x4007
cdef GLenum GL_FALSE = 0
cdef GLenum GL_LIGHT5 = 0x4005
cdef GLenum GL_TEXTURE_GEN_MODE = 0x2500
cdef GLenum GL_LINE_RESET_TOKEN = 0x0707
cdef GLenum GL_EXTENSIONS = 0x1F03
cdef GLenum GL_LINE_TOKEN = 0x0702
cdef GLenum GL_3_BYTES = 0x1408
cdef GLenum GL_ONE_MINUS_DST_ALPHA = 0x0305
cdef GLenum GL_4_BYTES = 0x1409
cdef GLenum GL_TRANSFORM_BIT = 0x00001000
cdef GLenum GL_CURRENT_RASTER_COLOR = 0x0B04
cdef GLenum GL_PIXEL_MAP_B_TO_B = 0x0C78
cdef GLenum GL_CW = 0x0900
cdef GLenum GL_DRAW_PIXEL_TOKEN = 0x0705
cdef GLenum GL_TEXTURE_ENV_MODE = 0x2200
cdef GLenum GL_UNPACK_SKIP_ROWS = 0x0CF3
cdef GLenum GL_CURRENT_RASTER_INDEX = 0x0B05
cdef GLenum GL_INDEX_CLEAR_VALUE = 0x0C20
cdef GLenum GL_LINEAR_MIPMAP_LINEAR = 0x2703
cdef GLenum GL_ACCUM = 0x0100
cdef GLenum GL_UNPACK_ROW_LENGTH = 0x0CF2
cdef GLenum GL_INVALID_VALUE = 0x0501
cdef GLenum GL_PIXEL_MAP_I_TO_G = 0x0C73
cdef GLenum GL_AUX3 = 0x040C
cdef GLenum GL_LINE_LOOP = 0x0002
cdef GLenum GL_ALPHA_BITS = 0x0D55
cdef GLenum GL_RED_BIAS = 0x0D15
cdef GLenum GL_3D = 0x0601
cdef GLenum GL_LINE_STIPPLE = 0x0B24
cdef GLenum GL_CONSTANT_ATTENUATION = 0x1207
cdef GLenum GL_PIXEL_MAP_A_TO_A_SIZE = 0x0CB9
cdef GLenum GL_LOGIC_OP = 0x0BF1
cdef GLenum GL_AMBIENT_AND_DIFFUSE = 0x1602
cdef GLenum GL_CURRENT_TEXTURE_COORDS = 0x0B03
cdef GLenum GL_CURRENT_RASTER_POSITION = 0x0B07
cdef GLenum GL_INDEX_BITS = 0x0D51
cdef GLenum GL_LINE_STIPPLE_PATTERN = 0x0B25
cdef GLenum GL_COLOR = 0x1800
cdef GLenum GL_GREATER = 0x0204
cdef GLenum GL_MAP1_TEXTURE_COORD_4 = 0x0D96
cdef GLenum GL_BLEND = 0x0BE2
cdef GLenum GL_MAP1_INDEX = 0x0D91
cdef GLenum GL_PACK_LSB_FIRST = 0x0D01
cdef GLenum GL_STEREO = 0x0C33
cdef GLenum GL_UNSIGNED_SHORT = 0x1403
cdef GLenum GL_2D = 0x0600
cdef GLenum GL_TRIANGLE_STRIP = 0x0005
cdef GLenum GL_Q = 0x2003
cdef GLenum GL_FOG = 0x0B60
cdef GLenum GL_PERSPECTIVE_CORRECTION_HINT = 0x0C50
cdef GLenum GL_ZERO = 0
cdef GLenum GL_LIST_BIT = 0x00020000
cdef GLenum GL_LINE_WIDTH = 0x0B21
cdef GLenum GL_NOTEQUAL = 0x0205
cdef GLenum GL_DEPTH_TEST = 0x0B71
cdef GLenum GL_MATRIX_MODE = 0x0BA0
cdef GLenum GL_SHADE_MODEL = 0x0B54
cdef GLenum GL_SPECULAR = 0x1202
cdef GLenum GL_CCW = 0x0901
cdef GLenum GL_PIXEL_MAP_A_TO_A = 0x0C79
cdef GLenum GL_MAP1_TEXTURE_COORD_1 = 0x0D93
cdef GLenum GL_COPY_INVERTED = 0x150C
cdef GLenum GL_SHORT = 0x1402
cdef GLenum GL_NONE = 0
cdef GLenum GL_INCR = 0x1E02
cdef GLenum GL_ACCUM_BUFFER_BIT = 0x00000200
cdef GLenum GL_POLYGON_TOKEN = 0x0703
cdef GLenum GL_EDGE_FLAG = 0x0B43
cdef GLenum GL_CLEAR = 0x1500
cdef GLenum GL_ENABLE_BIT = 0x00002000
cdef GLenum GL_INDEX_SHIFT = 0x0D12
cdef GLenum GL_ACCUM_CLEAR_VALUE = 0x0B80
cdef GLenum GL_T = 0x2001
cdef GLenum GL_NEAREST = 0x2600
cdef GLenum GL_GREEN_BITS = 0x0D53
cdef GLenum GL_INDEX_MODE = 0x0C30
cdef GLenum GL_EQUIV = 0x1509
cdef GLenum GL_OBJECT_LINEAR = 0x2401
cdef GLenum GL_STACK_OVERFLOW = 0x0503
cdef GLenum GL_DEPTH_BIAS = 0x0D1F
cdef GLenum GL_UNPACK_SWAP_BYTES = 0x0CF0
cdef GLenum GL_PIXEL_MAP_I_TO_G_SIZE = 0x0CB3
cdef GLenum GL_MAP1_GRID_SEGMENTS = 0x0DD1
cdef GLenum GL_POINT_BIT = 0x00000002
cdef GLenum GL_CLAMP = 0x2900
cdef GLenum GL_BITMAP = 0x1A00
cdef GLenum GL_MAP_COLOR = 0x0D10
cdef GLenum GL_PACK_ALIGNMENT = 0x0D05
cdef GLenum GL_2_BYTES = 0x1407
cdef GLenum GL_CLIP_PLANE2 = 0x3002
cdef GLenum GL_BACK_RIGHT = 0x0403
cdef GLenum GL_ALPHA_SCALE = 0x0D1C
cdef GLenum GL_BACK = 0x0405
cdef GLenum GL_CULL_FACE = 0x0B44
cdef GLenum GL_PIXEL_MAP_S_TO_S_SIZE = 0x0CB1
cdef GLenum GL_SET = 0x150F
cdef GLenum GL_HINT_BIT = 0x00008000
cdef GLenum GL_NEAREST_MIPMAP_NEAREST = 0x2700
cdef GLenum GL_PACK_ROW_LENGTH = 0x0D02
cdef GLenum GL_DECAL = 0x2101
cdef GLenum GL_COLOR_MATERIAL = 0x0B57
cdef GLenum GL_LIST_MODE = 0x0B30
cdef GLenum GL_ACCUM_RED_BITS = 0x0D58
cdef GLenum GL_ONE_MINUS_SRC_ALPHA = 0x0303
cdef GLenum GL_FOG_COLOR = 0x0B66
cdef GLenum GL_DECR = 0x1E03
cdef GLenum GL_AMBIENT = 0x1200
cdef GLenum GL_EQUAL = 0x0202
cdef GLenum GL_ALPHA_TEST = 0x0BC0
cdef GLenum GL_COLOR_MATERIAL_FACE = 0x0B55
cdef GLenum GL_PIXEL_MAP_I_TO_A = 0x0C75
cdef GLenum GL_MAP2_INDEX = 0x0DB1
cdef GLenum GL_CLIP_PLANE5 = 0x3005
cdef GLenum GL_POINT_SIZE_RANGE = 0x0B12
cdef GLenum GL_AND_REVERSE = 0x1502
cdef GLenum GL_STENCIL_INDEX = 0x1901
cdef GLenum GL_ALPHA_TEST_FUNC = 0x0BC1
cdef GLenum GL_COPY = 0x1503
cdef GLenum GL_ALPHA = 0x1906
cdef GLenum GL_PACK_SKIP_ROWS = 0x0D03
cdef GLenum GL_MODELVIEW_MATRIX = 0x0BA6
cdef GLenum GL_TRUE = 1
cdef GLenum GL_ATTRIB_STACK_DEPTH = 0x0BB0
cdef GLenum GL_SCISSOR_BOX = 0x0C10
cdef GLenum GL_PIXEL_MAP_R_TO_R = 0x0C76
cdef GLenum GL_LIST_BASE = 0x0B32
cdef GLenum GL_TEXTURE_WRAP_T = 0x2803
cdef GLenum GL_CURRENT_INDEX = 0x0B01
cdef GLenum GL_STENCIL_REF = 0x0B97
cdef GLenum GL_RIGHT = 0x0407
cdef GLenum GL_OBJECT_PLANE = 0x2501
cdef GLenum GL_REPLACE = 0x1E01
cdef GLenum GL_DOMAIN = 0x0A02
cdef GLenum GL_FOG_DENSITY = 0x0B62
cdef GLenum GL_PACK_SWAP_BYTES = 0x0D00
cdef GLenum GL_LEQUAL = 0x0203
cdef GLenum GL_TEXTURE = 0x1702
cdef GLenum GL_EXP = 0x0800
cdef GLenum GL_UNSIGNED_BYTE = 0x1401
cdef GLenum GL_DITHER = 0x0BD0
cdef GLenum GL_MODELVIEW = 0x1700
cdef GLenum GL_MAP1_VERTEX_4 = 0x0D98
cdef GLenum GL_3D_COLOR_TEXTURE = 0x0603
cdef GLenum GL_CURRENT_COLOR = 0x0B00
cdef GLenum GL_TEXTURE_MAG_FILTER = 0x2800
cdef GLenum GL_DST_ALPHA = 0x0304
cdef GLenum GL_TEXTURE_BIT = 0x00040000
cdef GLenum GL_REPEAT = 0x2901
cdef GLenum GL_AUX_BUFFERS = 0x0C00
cdef GLenum GL_PIXEL_MAP_G_TO_G_SIZE = 0x0CB7
cdef GLenum GL_CLIP_PLANE4 = 0x3004
cdef GLenum GL_STENCIL_BITS = 0x0D57
cdef GLenum GL_NOR = 0x1508
cdef GLenum GL_LIGHTING_BIT = 0x00000040
cdef GLenum GL_POLYGON_MODE = 0x0B40
cdef GLenum GL_VIEWPORT = 0x0BA2
cdef GLenum GL_POINT = 0x1B00
cdef GLenum GL_TEXTURE_ENV = 0x2300
cdef GLenum GL_CURRENT_BIT = 0x00000001
cdef GLenum GL_MAX_VIEWPORT_DIMS = 0x0D3A
cdef GLenum GL_TEXTURE_BORDER = 0x1005
cdef GLenum GL_OR_REVERSE = 0x150B
cdef GLenum GL_EYE_PLANE = 0x2502
cdef GLenum GL_PIXEL_MAP_B_TO_B_SIZE = 0x0CB8
cdef GLenum GL_RENDER = 0x1C00
cdef GLenum GL_BLUE_SCALE = 0x0D1A
cdef GLenum GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
cdef GLenum GL_TEXTURE_2D = 0x0DE1
cdef GLenum GL_POSITION = 0x1203
cdef GLenum GL_BLEND_DST = 0x0BE0
cdef GLenum GL_GREEN = 0x1904
cdef GLenum GL_TEXTURE_WRAP_S = 0x2802
cdef GLenum GL_POINT_SMOOTH = 0x0B10
cdef GLenum GL_MAX_LIST_NESTING = 0x0B31
cdef GLenum GL_SUBPIXEL_BITS = 0x0D50
cdef GLenum GL_DEPTH = 0x1801
cdef GLenum GL_LINE_STRIP = 0x0003
cdef GLenum GL_SRC_COLOR = 0x0300
cdef GLenum GL_DEPTH_FUNC = 0x0B74
cdef GLenum GL_LUMINANCE_ALPHA = 0x190A
cdef GLenum GL_MAX_ATTRIB_STACK_DEPTH = 0x0D35
cdef GLenum GL_FRONT_LEFT = 0x0400
cdef GLenum GL_ONE_MINUS_DST_COLOR = 0x0307
cdef GLenum GL_CLIP_PLANE3 = 0x3003
cdef GLenum GL_GEQUAL = 0x0206
cdef GLenum GL_ACCUM_BLUE_BITS = 0x0D5A
cdef GLenum GL_DEPTH_BITS = 0x0D56
cdef GLenum GL_LINEAR_ATTENUATION = 0x1208
cdef GLenum GL_FLOAT = 0x1406
cdef GLenum GL_MAP1_VERTEX_3 = 0x0D97
cdef GLenum GL_COEFF = 0x0A00
cdef GLenum GL_VERSION = 0x1F02
cdef GLenum GL_EXP2 = 0x0801
cdef GLenum GL_MAP2_TEXTURE_COORD_3 = 0x0DB5
cdef GLenum GL_BLUE = 0x1905
cdef GLenum GL_STENCIL_FUNC = 0x0B92
cdef GLenum GL_MAP2_COLOR_4 = 0x0DB0
cdef GLenum GL_NICEST = 0x1102
cdef GLenum GL_FRONT = 0x0404
cdef GLenum GL_PIXEL_MAP_I_TO_R_SIZE = 0x0CB2
cdef GLenum GL_3D_COLOR = 0x0602
cdef GLenum GL_OUT_OF_MEMORY = 0x0505
cdef GLenum GL_DOUBLEBUFFER = 0x0C32
cdef GLenum GL_FRONT_RIGHT = 0x0401
cdef GLenum GL_NEAREST_MIPMAP_LINEAR = 0x2702
cdef GLenum GL_TEXTURE_1D = 0x0DE0
cdef GLenum GL_OR_INVERTED = 0x150D
cdef GLenum GL_COLOR_BUFFER_BIT = 0x00004000
cdef GLenum GL_COLOR_WRITEMASK = 0x0C23
cdef GLenum GL_DEPTH_SCALE = 0x0D1E
cdef GLenum GL_AND_INVERTED = 0x1504
cdef GLenum GL_ACCUM_ALPHA_BITS = 0x0D5B
cdef GLenum GL_CLIP_PLANE0 = 0x3000
cdef GLenum GL_LIST_INDEX = 0x0B33
cdef GLenum GL_MAX_TEXTURE_STACK_DEPTH = 0x0D39
cdef GLenum GL_POLYGON_STIPPLE_BIT = 0x00000010
cdef GLenum GL_GREEN_SCALE = 0x0D18
cdef GLenum GL_PIXEL_MAP_I_TO_B = 0x0C74
cdef GLenum GL_LOGIC_OP_MODE = 0x0BF0
cdef GLenum GL_PROJECTION = 0x1701
cdef GLenum GL_DEPTH_BUFFER_BIT = 0x00000100
cdef GLenum GL_MAX_EVAL_ORDER = 0x0D30
cdef GLenum GL_ORDER = 0x0A01
cdef GLenum GL_VENDOR = 0x1F00
cdef GLenum GL_MAP2_TEXTURE_COORD_1 = 0x0DB3
cdef GLenum GL_EVAL_BIT = 0x00010000
cdef GLenum GL_PIXEL_MAP_R_TO_R_SIZE = 0x0CB6
cdef GLenum GL_LINE = 0x1B01
cdef GLenum GL_INVALID_ENUM = 0x0500
cdef GLenum GL_DEPTH_COMPONENT = 0x1902
cdef GLenum GL_PIXEL_MAP_I_TO_R = 0x0C72
cdef GLenum GL_BYTE = 0x1400
cdef GLenum GL_DEPTH_WRITEMASK = 0x0B72
cdef GLenum GL_ADD = 0x0104
cdef GLenum GL_4D_COLOR_TEXTURE = 0x0604
cdef GLenum GL_FILL = 0x1B02
cdef GLenum GL_FRONT_FACE = 0x0B46
cdef GLenum GL_TEXTURE_ENV_COLOR = 0x2201
cdef GLenum GL_LINE_STIPPLE_REPEAT = 0x0B26
cdef GLenum GL_LIGHT0 = 0x4000
cdef GLenum GL_AUX1 = 0x040A
cdef GLenum GL_LIGHT4 = 0x4004
cdef GLenum GL_MAP1_GRID_DOMAIN = 0x0DD0
cdef GLenum GL_LESS = 0x0201
cdef GLenum GL_QUADS = 0x0007
cdef GLenum GL_AUTO_NORMAL = 0x0D80
cdef GLenum GL_SPOT_EXPONENT = 0x1205
cdef GLenum GL_MAP1_COLOR_4 = 0x0D90
cdef GLenum GL_TEXTURE_STACK_DEPTH = 0x0BA5
cdef GLenum GL_BACK_LEFT = 0x0402
cdef GLenum GL_CURRENT_RASTER_DISTANCE = 0x0B09
cdef GLenum GL_UNSIGNED_INT = 0x1405
cdef GLenum GL_STENCIL_FAIL = 0x0B94
cdef GLenum GL_LINEAR_MIPMAP_NEAREST = 0x2701
cdef GLenum GL_QUADRATIC_ATTENUATION = 0x1209
cdef GLenum GL_ZOOM_Y = 0x0D17
cdef GLenum GL_EYE_LINEAR = 0x2400
cdef GLenum GL_MAP_STENCIL = 0x0D11
cdef GLenum GL_CURRENT_RASTER_POSITION_VALID = 0x0B08
cdef GLenum GL_POLYGON_SMOOTH_HINT = 0x0C53
cdef GLenum GL_POINT_TOKEN = 0x0701
cdef GLenum GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
cdef GLenum GL_INVERT = 0x150A
cdef GLenum GL_MAP2_NORMAL = 0x0DB2
cdef GLenum GL_SPOT_CUTOFF = 0x1206
cdef GLenum GL_FOG_INDEX = 0x0B61
cdef GLenum GL_PIXEL_MAP_G_TO_G = 0x0C77
cdef GLenum GL_SCISSOR_TEST = 0x0C11
cdef GLenum GL_DONT_CARE = 0x1100
cdef GLenum GL_QUAD_STRIP = 0x0008
cdef GLenum GL_BITMAP_TOKEN = 0x0704
cdef GLenum GL_CLIP_PLANE1 = 0x3001
cdef GLenum GL_EMISSION = 0x1600
cdef GLenum GL_RED = 0x1903
cdef GLenum GL_STENCIL_VALUE_MASK = 0x0B93
cdef GLenum GL_LIGHT1 = 0x4001
cdef GLenum GL_INT = 0x1404
cdef GLenum GL_STENCIL = 0x1802
cdef GLenum GL_TEXTURE_COMPONENTS = 0x1003
cdef GLenum GL_MAX_MODELVIEW_STACK_DEPTH = 0x0D36
cdef GLenum GL_LINE_WIDTH_RANGE = 0x0B22
cdef GLenum GL_LINEAR = 0x2601
cdef GLenum GL_FOG_MODE = 0x0B65
cdef GLenum GL_KEEP = 0x1E00
cdef GLenum GL_ONE_MINUS_SRC_COLOR = 0x0301
cdef GLenum GL_CULL_FACE_MODE = 0x0B45
cdef GLenum GL_TRIANGLES = 0x0004
cdef GLenum GL_AUX0 = 0x0409
cdef GLenum GL_MAX_CLIP_PLANES = 0x0D32
cdef GLenum GL_MAX_LIGHTS = 0x0D31
cdef GLenum GL_DIFFUSE = 0x1201
cdef GLenum GL_NORMALIZE = 0x0BA1
cdef GLenum GL_PIXEL_MAP_I_TO_B_SIZE = 0x0CB4
cdef GLenum GL_RGBA_MODE = 0x0C31
cdef GLenum GL_LEFT = 0x0406
cdef GLenum GL_DEPTH_CLEAR_VALUE = 0x0B73
cdef GLenum GL_NAND = 0x150E
cdef GLenum GL_PIXEL_MODE_BIT = 0x00000020
cdef GLenum GL_R = 0x2002
cdef GLenum GL_UNPACK_LSB_FIRST = 0x0CF1
cdef GLenum GL_AND = 0x1501
cdef GLenum GL_FRONT_AND_BACK = 0x0408
cdef GLenum GL_BLUE_BIAS = 0x0D1B
cdef GLenum GL_PIXEL_MAP_I_TO_I = 0x0C70
cdef GLenum GL_FOG_START = 0x0B63
cdef GLenum GL_ALWAYS = 0x0207
cdef GLenum GL_AUX2 = 0x040B
cdef GLenum GL_COMPILE_AND_EXECUTE = 0x1301
cdef GLenum GL_LINE_SMOOTH_HINT = 0x0C52
cdef GLenum GL_FLAT = 0x1D00
cdef GLenum GL_TEXTURE_GEN_R = 0x0C62
cdef GLenum GL_ZOOM_X = 0x0D16
cdef GLenum GL_POLYGON = 0x0009
cdef GLenum GL_UNPACK_ALIGNMENT = 0x0CF5
cdef GLenum GL_TEXTURE_GEN_T = 0x0C61
cdef GLenum GL_PACK_SKIP_PIXELS = 0x0D04
cdef GLenum GL_LIGHT3 = 0x4003
cdef GLenum GL_RGB = 0x1907
cdef GLenum GL_ALPHA_TEST_REF = 0x0BC2
cdef GLenum GL_MAX_NAME_STACK_DEPTH = 0x0D37
cdef GLenum GL_LINE_BIT = 0x00000004
cdef GLenum GL_FOG_BIT = 0x00000080
cdef GLenum GL_SCISSOR_BIT = 0x00080000
cdef GLenum GL_SPOT_DIRECTION = 0x1204
cdef GLenum GL_TEXTURE_BORDER_COLOR = 0x1004
cdef GLenum GL_ALL_ATTRIB_BITS = 0xFFFFFFFF
cdef GLenum GL_COLOR_INDEX = 0x1900
cdef GLenum GL_RETURN = 0x0102
cdef GLenum GL_FASTEST = 0x1101
cdef GLenum GL_PIXEL_MAP_I_TO_A_SIZE = 0x0CB5
cdef GLenum GL_NEVER = 0x0200
cdef GLenum GL_MULT = 0x0103

ctypedef void (*PFNGLLISTBASEPROC)(GLuint base)
ctypedef void (*PFNGLRASTERPOS2SPROC)(GLshort x, GLshort y)
ctypedef void (*PFNGLLIGHTMODELIPROC)(GLenum pname, GLint param)
ctypedef void (*PFNGLINDEXIVPROC)(const GLint *c)
ctypedef void (*PFNGLTEXPARAMETERIVPROC)(GLenum target, GLenum pname, const GLint *params)
ctypedef void (*PFNGLCOLOR4UBVPROC)(const GLubyte *v)
ctypedef void (*PFNGLREADPIXELSPROC)(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, void *pixels)
ctypedef void (*PFNGLTEXCOORD2FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLPIXELSTOREFPROC)(GLenum pname, GLfloat param)
ctypedef void (*PFNGLLIGHTFVPROC)(GLenum light, GLenum pname, const GLfloat *params)
ctypedef void (*PFNGLDRAWPIXELSPROC)(GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
ctypedef void (*PFNGLCOLOR3UIVPROC)(const GLuint *v)
ctypedef void (*PFNGLMATERIALFVPROC)(GLenum face, GLenum pname, const GLfloat *params)
ctypedef void (*PFNGLFRUSTUMPROC)(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
ctypedef void (*PFNGLVERTEX2FPROC)(GLfloat x, GLfloat y)
ctypedef void (*PFNGLSTENCILFUNCPROC)(GLenum func, GLint ref, GLuint mask)
ctypedef void (*PFNGLTEXENVFPROC)(GLenum target, GLenum pname, GLfloat param)
ctypedef void (*PFNGLRECTSVPROC)(const GLshort *v1, const GLshort *v2)
ctypedef void (*PFNGLEVALCOORD1FVPROC)(const GLfloat *u)
ctypedef void (*PFNGLGETTEXPARAMETERFVPROC)(GLenum target, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLRECTSPROC)(GLshort x1, GLshort y1, GLshort x2, GLshort y2)
ctypedef void (*PFNGLREADBUFFERPROC)(GLenum src)
ctypedef void (*PFNGLRASTERPOS4DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLDEPTHFUNCPROC)(GLenum func)
ctypedef void (*PFNGLTEXGENDPROC)(GLenum coord, GLenum pname, GLdouble param)
ctypedef void (*PFNGLLOADMATRIXFPROC)(const GLfloat *m)
ctypedef void (*PFNGLEVALCOORD2FPROC)(GLfloat u, GLfloat v)
ctypedef void (*PFNGLDELETELISTSPROC)(GLuint list, GLsizei range)
ctypedef void (*PFNGLMULTMATRIXDPROC)(const GLdouble *m)
ctypedef void (*PFNGLPUSHMATRIXPROC)()
ctypedef void (*PFNGLGETMAPDVPROC)(GLenum target, GLenum query, GLdouble *v)
ctypedef void (*PFNGLRASTERPOS4FPROC)(GLfloat x, GLfloat y, GLfloat z, GLfloat w)
ctypedef void (*PFNGLCOLOR4USPROC)(GLushort red, GLushort green, GLushort blue, GLushort alpha)
ctypedef void (*PFNGLTEXGENIVPROC)(GLenum coord, GLenum pname, const GLint *params)
ctypedef void (*PFNGLTEXENVIPROC)(GLenum target, GLenum pname, GLint param)
ctypedef void (*PFNGLTEXENVIVPROC)(GLenum target, GLenum pname, const GLint *params)
ctypedef void (*PFNGLSCALEDPROC)(GLdouble x, GLdouble y, GLdouble z)
ctypedef GLboolean (*PFNGLISENABLEDPROC)(GLenum cap)
ctypedef void (*PFNGLCOLOR3IVPROC)(const GLint *v)
ctypedef void (*PFNGLNORMAL3DPROC)(GLdouble nx, GLdouble ny, GLdouble nz)
ctypedef void (*PFNGLVERTEX4FPROC)(GLfloat x, GLfloat y, GLfloat z, GLfloat w)
ctypedef void (*PFNGLLIGHTMODELIVPROC)(GLenum pname, const GLint *params)
ctypedef void (*PFNGLGETLIGHTFVPROC)(GLenum light, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLRASTERPOS3FPROC)(GLfloat x, GLfloat y, GLfloat z)
ctypedef GLuint (*PFNGLGENLISTSPROC)(GLsizei range)
ctypedef void (*PFNGLEVALCOORD1DVPROC)(const GLdouble *u)
ctypedef void (*PFNGLCLEARINDEXPROC)(GLfloat c)
ctypedef void (*PFNGLINDEXFVPROC)(const GLfloat *c)
ctypedef void (*PFNGLRASTERPOS4SVPROC)(const GLshort *v)
ctypedef void (*PFNGLMAPGRID2FPROC)(GLint un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)
ctypedef void (*PFNGLCOPYPIXELSPROC)(GLint x, GLint y, GLsizei width, GLsizei height, GLenum type)
ctypedef void (*PFNGLVERTEX4IVPROC)(const GLint *v)
ctypedef void (*PFNGLPOPNAMEPROC)()
ctypedef void (*PFNGLTEXCOORD4IPROC)(GLint s, GLint t, GLint r, GLint q)
ctypedef void (*PFNGLDISABLEPROC)(GLenum cap)
ctypedef void (*PFNGLCALLLISTPROC)(GLuint list)
ctypedef void (*PFNGLNORMAL3DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLPOLYGONMODEPROC)(GLenum face, GLenum mode)
ctypedef void (*PFNGLCOLOR3FPROC)(GLfloat red, GLfloat green, GLfloat blue)
ctypedef void (*PFNGLLIGHTIVPROC)(GLenum light, GLenum pname, const GLint *params)
ctypedef void (*PFNGLCOLOR4SVPROC)(const GLshort *v)
ctypedef void (*PFNGLTEXCOORD3SVPROC)(const GLshort *v)
ctypedef void (*PFNGLVERTEX2DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLRASTERPOS4DPROC)(GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*PFNGLMATERIALIPROC)(GLenum face, GLenum pname, GLint param)
ctypedef void (*PFNGLPIXELMAPUIVPROC)(GLenum map, GLsizei mapsize, const GLuint *values)
ctypedef void (*PFNGLROTATEDPROC)(GLdouble angle, GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*PFNGLNORMAL3FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLCOLOR3BPROC)(GLbyte red, GLbyte green, GLbyte blue)
ctypedef void (*PFNGLLOGICOPPROC)(GLenum opcode)
ctypedef void (*PFNGLCOLOR4UIPROC)(GLuint red, GLuint green, GLuint blue, GLuint alpha)
ctypedef void (*PFNGLTEXCOORD3IVPROC)(const GLint *v)
ctypedef void (*PFNGLTEXCOORD1SVPROC)(const GLshort *v)
ctypedef void (*PFNGLGETMATERIALFVPROC)(GLenum face, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLCOLOR3UIPROC)(GLuint red, GLuint green, GLuint blue)
ctypedef void (*PFNGLVERTEX3FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLCLEARDEPTHPROC)(GLdouble depth)
ctypedef void (*PFNGLNEWLISTPROC)(GLuint list, GLenum mode)
ctypedef void (*PFNGLORTHOPROC)(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
ctypedef void (*PFNGLDEPTHMASKPROC)(GLboolean flag)
ctypedef void (*PFNGLVERTEX4SPROC)(GLshort x, GLshort y, GLshort z, GLshort w)
ctypedef void (*PFNGLVERTEX3DPROC)(GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*PFNGLPASSTHROUGHPROC)(GLfloat token)
ctypedef void (*PFNGLENABLEPROC)(GLenum cap)
ctypedef void (*PFNGLFLUSHPROC)()
ctypedef void (*PFNGLLOADNAMEPROC)(GLuint name)
ctypedef void (*PFNGLCALLLISTSPROC)(GLsizei n, GLenum type, const void *lists)
ctypedef void (*PFNGLNORMAL3IPROC)(GLint nx, GLint ny, GLint nz)
ctypedef void (*PFNGLEVALCOORD2FVPROC)(const GLfloat *u)
ctypedef void (*PFNGLPOPMATRIXPROC)()
ctypedef void (*PFNGLFINISHPROC)()
ctypedef void (*PFNGLSELECTBUFFERPROC)(GLsizei size, GLuint *buffer)
ctypedef void (*PFNGLCOLOR3DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLCOLOR4DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLGETBOOLEANVPROC)(GLenum pname, GLboolean *data)
ctypedef void (*PFNGLCOLOR3SVPROC)(const GLshort *v)
ctypedef void (*PFNGLEVALPOINT2PROC)(GLint i, GLint j)
ctypedef void (*PFNGLCLEARACCUMPROC)(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
ctypedef void (*PFNGLCOLOR4BVPROC)(const GLbyte *v)
ctypedef void (*PFNGLVERTEX4DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLTEXCOORD1DPROC)(GLdouble s)
ctypedef void (*PFNGLRASTERPOS3DPROC)(GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*PFNGLTEXCOORD2IVPROC)(const GLint *v)
ctypedef void (*PFNGLACCUMPROC)(GLenum op, GLfloat value)
ctypedef void (*PFNGLCOLOR4USVPROC)(const GLushort *v)
ctypedef void (*PFNGLNORMAL3SVPROC)(const GLshort *v)
ctypedef void (*PFNGLTEXGENFVPROC)(GLenum coord, GLenum pname, const GLfloat *params)
ctypedef void (*PFNGLCOLOR4BPROC)(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha)
ctypedef void (*PFNGLTEXGENIPROC)(GLenum coord, GLenum pname, GLint param)
ctypedef void (*PFNGLCLEARSTENCILPROC)(GLint s)
ctypedef void (*PFNGLVERTEX2DPROC)(GLdouble x, GLdouble y)
ctypedef void (*PFNGLVERTEX4IPROC)(GLint x, GLint y, GLint z, GLint w)
ctypedef void (*PFNGLEVALPOINT1PROC)(GLint i)
ctypedef void (*PFNGLNORMAL3FPROC)(GLfloat nx, GLfloat ny, GLfloat nz)
ctypedef void (*PFNGLEVALMESH1PROC)(GLenum mode, GLint i1, GLint i2)
ctypedef void (*PFNGLTEXCOORD2DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLHINTPROC)(GLenum target, GLenum mode)
ctypedef void (*PFNGLPOINTSIZEPROC)(GLfloat size)
ctypedef void (*PFNGLCLEARCOLORPROC)(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
ctypedef void (*PFNGLTEXCOORD1FPROC)(GLfloat s)
ctypedef void (*PFNGLFRONTFACEPROC)(GLenum mode)
ctypedef void (*PFNGLCOLOR3FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLEDGEFLAGPROC)(GLboolean flag)
ctypedef void (*PFNGLTEXCOORD1SPROC)(GLshort s)
ctypedef void (*PFNGLTEXCOORD2FPROC)(GLfloat s, GLfloat t)
ctypedef void (*PFNGLTEXCOORD4FPROC)(GLfloat s, GLfloat t, GLfloat r, GLfloat q)
ctypedef void (*PFNGLFOGFPROC)(GLenum pname, GLfloat param)
ctypedef void (*PFNGLPUSHATTRIBPROC)(GLbitfield mask)
ctypedef void (*PFNGLCOLOR4FPROC)(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
ctypedef void (*PFNGLBITMAPPROC)(GLsizei width, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte *bitmap)
ctypedef void (*PFNGLCOLOR4DPROC)(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha)
ctypedef void (*PFNGLTEXPARAMETERIPROC)(GLenum target, GLenum pname, GLint param)
ctypedef void (*PFNGLENDLISTPROC)()
ctypedef void (*PFNGLRASTERPOS2IPROC)(GLint x, GLint y)
ctypedef void (*PFNGLRASTERPOS3SVPROC)(const GLshort *v)
ctypedef void (*PFNGLCULLFACEPROC)(GLenum mode)
ctypedef void (*PFNGLGETCLIPPLANEPROC)(GLenum plane, GLdouble *equation)
ctypedef void (*PFNGLRASTERPOS3IVPROC)(const GLint *v)
ctypedef void (*PFNGLTEXCOORD4SVPROC)(const GLshort *v)
ctypedef void (*PFNGLMATERIALIVPROC)(GLenum face, GLenum pname, const GLint *params)
ctypedef void (*PFNGLVIEWPORTPROC)(GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*PFNGLTEXCOORD4IVPROC)(const GLint *v)
ctypedef void (*PFNGLSTENCILOPPROC)(GLenum fail, GLenum zfail, GLenum zpass)
ctypedef void (*PFNGLCOLOR4IVPROC)(const GLint *v)
ctypedef void (*PFNGLCOLOR3USPROC)(GLushort red, GLushort green, GLushort blue)
ctypedef void (*PFNGLTEXPARAMETERFVPROC)(GLenum target, GLenum pname, const GLfloat *params)
ctypedef void (*PFNGLNORMAL3IVPROC)(const GLint *v)
ctypedef void (*PFNGLPIXELZOOMPROC)(GLfloat xfactor, GLfloat yfactor)
ctypedef void (*PFNGLNORMAL3BVPROC)(const GLbyte *v)
ctypedef void (*PFNGLPIXELTRANSFERIPROC)(GLenum pname, GLint param)
ctypedef void (*PFNGLGETTEXENVIVPROC)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*PFNGLDEPTHRANGEPROC)(GLdouble n, GLdouble f)
ctypedef void (*PFNGLRECTIPROC)(GLint x1, GLint y1, GLint x2, GLint y2)
ctypedef void (*PFNGLTEXCOORD1IPROC)(GLint s)
ctypedef void (*PFNGLTEXENVFVPROC)(GLenum target, GLenum pname, const GLfloat *params)
ctypedef void (*PFNGLINDEXDVPROC)(const GLdouble *c)
ctypedef void (*PFNGLVERTEX2SVPROC)(const GLshort *v)
ctypedef void (*PFNGLGETTEXIMAGEPROC)(GLenum target, GLint level, GLenum format, GLenum type, void *pixels)
ctypedef void (*PFNGLRECTFVPROC)(const GLfloat *v1, const GLfloat *v2)
ctypedef void (*PFNGLCOLORMASKPROC)(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha)
ctypedef void (*PFNGLPOPATTRIBPROC)()
ctypedef void (*PFNGLGETMAPFVPROC)(GLenum target, GLenum query, GLfloat *v)
ctypedef void (*PFNGLTEXCOORD2SPROC)(GLshort s, GLshort t)
ctypedef void (*PFNGLSTENCILMASKPROC)(GLuint mask)
ctypedef void (*PFNGLPOLYGONSTIPPLEPROC)(const GLubyte *mask)
ctypedef void (*PFNGLPUSHNAMEPROC)(GLuint name)
ctypedef void (*PFNGLEVALCOORD2DPROC)(GLdouble u, GLdouble v)
ctypedef void (*PFNGLRASTERPOS2DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLGETLIGHTIVPROC)(GLenum light, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETDOUBLEVPROC)(GLenum pname, GLdouble *data)
ctypedef void (*PFNGLTEXCOORD4DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLGETMAPIVPROC)(GLenum target, GLenum query, GLint *v)
ctypedef void (*PFNGLVERTEX2IVPROC)(const GLint *v)
ctypedef void (*PFNGLTEXCOORD4SPROC)(GLshort s, GLshort t, GLshort r, GLshort q)
ctypedef void (*PFNGLDRAWBUFFERPROC)(GLenum buf)
ctypedef void (*PFNGLRECTDPROC)(GLdouble x1, GLdouble y1, GLdouble x2, GLdouble y2)
ctypedef void (*PFNGLPIXELMAPFVPROC)(GLenum map, GLsizei mapsize, const GLfloat *values)
ctypedef GLboolean (*PFNGLISLISTPROC)(GLuint list)
ctypedef void (*PFNGLRASTERPOS4IPROC)(GLint x, GLint y, GLint z, GLint w)
ctypedef void (*PFNGLGETTEXGENDVPROC)(GLenum coord, GLenum pname, GLdouble *params)
ctypedef void (*PFNGLMAP2DPROC)(GLenum target, GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint vstride, GLint vorder, const GLdouble *points)
ctypedef void (*PFNGLTEXCOORD4FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLRASTERPOS2SVPROC)(const GLshort *v)
ctypedef void (*PFNGLLIGHTIPROC)(GLenum light, GLenum pname, GLint param)
ctypedef void (*PFNGLRASTERPOS4SPROC)(GLshort x, GLshort y, GLshort z, GLshort w)
ctypedef void (*PFNGLCOLOR3SPROC)(GLshort red, GLshort green, GLshort blue)
ctypedef void (*PFNGLRASTERPOS2DPROC)(GLdouble x, GLdouble y)
ctypedef void (*PFNGLCOLOR3UBPROC)(GLubyte red, GLubyte green, GLubyte blue)
ctypedef void (*PFNGLRASTERPOS4FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLINDEXSVPROC)(const GLshort *c)
ctypedef void (*PFNGLROTATEFPROC)(GLfloat angle, GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*PFNGLRASTERPOS2FPROC)(GLfloat x, GLfloat y)
ctypedef void (*PFNGLTRANSLATEFPROC)(GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*PFNGLINDEXDPROC)(GLdouble c)
ctypedef void (*PFNGLNORMAL3SPROC)(GLshort nx, GLshort ny, GLshort nz)
ctypedef void (*PFNGLGETTEXGENIVPROC)(GLenum coord, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETINTEGERVPROC)(GLenum pname, GLint *data)
ctypedef void (*PFNGLLIGHTMODELFVPROC)(GLenum pname, const GLfloat *params)
ctypedef void (*PFNGLVERTEX2IPROC)(GLint x, GLint y)
ctypedef void (*PFNGLTEXCOORD1DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLTEXCOORD1FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLCOLOR3IPROC)(GLint red, GLint green, GLint blue)
ctypedef void (*PFNGLVERTEX3IVPROC)(const GLint *v)
ctypedef void (*PFNGLMATRIXMODEPROC)(GLenum mode)
ctypedef void (*PFNGLRECTFPROC)(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2)
ctypedef void (*PFNGLMAP1DPROC)(GLenum target, GLdouble u1, GLdouble u2, GLint stride, GLint order, const GLdouble *points)
ctypedef void (*PFNGLINDEXFPROC)(GLfloat c)
ctypedef void (*PFNGLVERTEX3SVPROC)(const GLshort *v)
ctypedef void (*PFNGLLIGHTMODELFPROC)(GLenum pname, GLfloat param)
ctypedef void (*PFNGLGETPIXELMAPFVPROC)(GLenum map, GLfloat *values)
ctypedef void (*PFNGLPIXELMAPUSVPROC)(GLenum map, GLsizei mapsize, const GLushort *values)
ctypedef void (*PFNGLRASTERPOS4IVPROC)(const GLint *v)
ctypedef void (*PFNGLTEXCOORD3FPROC)(GLfloat s, GLfloat t, GLfloat r)
ctypedef void (*PFNGLLOADMATRIXDPROC)(const GLdouble *m)
ctypedef void (*PFNGLLINEWIDTHPROC)(GLfloat width)
ctypedef void (*PFNGLSCISSORPROC)(GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*PFNGLGETTEXLEVELPARAMETERFVPROC)(GLenum target, GLint level, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLTEXCOORD3FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLLOADIDENTITYPROC)()
ctypedef void (*PFNGLRASTERPOS2FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLTEXPARAMETERFPROC)(GLenum target, GLenum pname, GLfloat param)
ctypedef void (*PFNGLTEXCOORD1IVPROC)(const GLint *v)
ctypedef void (*PFNGLINITNAMESPROC)()
ctypedef void (*PFNGLMAPGRID1FPROC)(GLint un, GLfloat u1, GLfloat u2)
ctypedef void (*PFNGLTEXIMAGE2DPROC)(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *pixels)
ctypedef void (*PFNGLGETPOLYGONSTIPPLEPROC)(GLubyte *mask)
ctypedef void (*PFNGLEVALCOORD2DVPROC)(const GLdouble *u)
ctypedef void (*PFNGLENDPROC)()
ctypedef void (*PFNGLMAPGRID1DPROC)(GLint un, GLdouble u1, GLdouble u2)
ctypedef void (*PFNGLCOLORMATERIALPROC)(GLenum face, GLenum mode)
ctypedef void (*PFNGLMULTMATRIXFPROC)(const GLfloat *m)
ctypedef void (*PFNGLMAP2FPROC)(GLenum target, GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride, GLint vorder, const GLfloat *points)
ctypedef void (*PFNGLPIXELTRANSFERFPROC)(GLenum pname, GLfloat param)
ctypedef void (*PFNGLVERTEX3FPROC)(GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*PFNGLCOLOR3USVPROC)(const GLushort *v)
ctypedef void (*PFNGLCOLOR4FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLPIXELSTOREIPROC)(GLenum pname, GLint param)
ctypedef void (*PFNGLMATERIALFPROC)(GLenum face, GLenum pname, GLfloat param)
ctypedef void (*PFNGLTEXIMAGE1DPROC)(GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const void *pixels)
ctypedef void (*PFNGLVERTEX3DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLLINESTIPPLEPROC)(GLint factor, GLushort pattern)
ctypedef void (*PFNGLCOLOR4SPROC)(GLshort red, GLshort green, GLshort blue, GLshort alpha)
ctypedef void (*PFNGLMAPGRID2DPROC)(GLint un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)
ctypedef void (*PFNGLVERTEX3IPROC)(GLint x, GLint y, GLint z)
ctypedef void (*PFNGLGETTEXLEVELPARAMETERIVPROC)(GLenum target, GLint level, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETMATERIALIVPROC)(GLenum face, GLenum pname, GLint *params)
ctypedef void (*PFNGLVERTEX4DPROC)(GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*PFNGLVERTEX4SVPROC)(const GLshort *v)
ctypedef void (*PFNGLGETTEXPARAMETERIVPROC)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETFLOATVPROC)(GLenum pname, GLfloat *data)
ctypedef void (*PFNGLSHADEMODELPROC)(GLenum mode)
ctypedef void (*PFNGLGETPIXELMAPUIVPROC)(GLenum map, GLuint *values)
ctypedef void (*PFNGLCLIPPLANEPROC)(GLenum plane, const GLdouble *equation)
ctypedef void (*PFNGLGETTEXENVFVPROC)(GLenum target, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLRASTERPOS2IVPROC)(const GLint *v)
ctypedef void (*PFNGLINDEXIPROC)(GLint c)
ctypedef void (*PFNGLVERTEX4FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLINDEXMASKPROC)(GLuint mask)
ctypedef void (*PFNGLRASTERPOS3DVPROC)(const GLdouble *v)
ctypedef void (*PFNGLCOLOR3UBVPROC)(const GLubyte *v)
ctypedef GLenum (*PFNGLGETERRORPROC)()
ctypedef void (*PFNGLCOLOR3BVPROC)(const GLbyte *v)
ctypedef void (*PFNGLTEXCOORD3IPROC)(GLint s, GLint t, GLint r)
ctypedef void (*PFNGLTEXGENFPROC)(GLenum coord, GLenum pname, GLfloat param)
ctypedef const GLubyte *(*PFNGLGETSTRINGPROC)(GLenum name)
ctypedef void (*PFNGLGETTEXGENFVPROC)(GLenum coord, GLenum pname, GLfloat *params)
ctypedef void (*PFNGLRASTERPOS3FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLCOLOR3DPROC)(GLdouble red, GLdouble green, GLdouble blue)
ctypedef void (*PFNGLSCALEFPROC)(GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*PFNGLRASTERPOS3SPROC)(GLshort x, GLshort y, GLshort z)
ctypedef void (*PFNGLEDGEFLAGVPROC)(const GLboolean *flag)
ctypedef void (*PFNGLTEXCOORD2SVPROC)(const GLshort *v)
ctypedef void (*PFNGLTEXCOORD3DPROC)(GLdouble s, GLdouble t, GLdouble r)
ctypedef void (*PFNGLEVALCOORD1DPROC)(GLdouble u)
ctypedef void (*PFNGLCOLOR4IPROC)(GLint red, GLint green, GLint blue, GLint alpha)
ctypedef void (*PFNGLCOLOR4UIVPROC)(const GLuint *v)
ctypedef void (*PFNGLALPHAFUNCPROC)(GLenum func, GLfloat ref)
ctypedef void (*PFNGLVERTEX2FVPROC)(const GLfloat *v)
ctypedef void (*PFNGLGETPIXELMAPUSVPROC)(GLenum map, GLushort *values)
ctypedef void (*PFNGLCLEARPROC)(GLbitfield mask)
ctypedef void (*PFNGLBLENDFUNCPROC)(GLenum sfactor, GLenum dfactor)
ctypedef void (*PFNGLRASTERPOS3IPROC)(GLint x, GLint y, GLint z)
ctypedef void (*PFNGLVERTEX3SPROC)(GLshort x, GLshort y, GLshort z)
ctypedef void (*PFNGLCOLOR4UBPROC)(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha)
ctypedef void (*PFNGLRECTDVPROC)(const GLdouble *v1, const GLdouble *v2)
ctypedef void (*PFNGLNORMAL3BPROC)(GLbyte nx, GLbyte ny, GLbyte nz)
ctypedef void (*PFNGLFOGIPROC)(GLenum pname, GLint param)
ctypedef GLint (*PFNGLRENDERMODEPROC)(GLenum mode)
ctypedef void (*PFNGLEVALCOORD1FPROC)(GLfloat u)
ctypedef void (*PFNGLVERTEX2SPROC)(GLshort x, GLshort y)
ctypedef void (*PFNGLRECTIVPROC)(const GLint *v1, const GLint *v2)
ctypedef void (*PFNGLEVALMESH2PROC)(GLenum mode, GLint i1, GLint i2, GLint j1, GLint j2)
ctypedef void (*PFNGLFOGFVPROC)(GLenum pname, const GLfloat *params)
ctypedef void (*PFNGLTEXCOORD4DPROC)(GLdouble s, GLdouble t, GLdouble r, GLdouble q)
ctypedef void (*PFNGLLIGHTFPROC)(GLenum light, GLenum pname, GLfloat param)
ctypedef void (*PFNGLTEXGENDVPROC)(GLenum coord, GLenum pname, const GLdouble *params)
ctypedef void (*PFNGLBEGINPROC)(GLenum mode)
ctypedef void (*PFNGLFEEDBACKBUFFERPROC)(GLsizei size, GLenum type, GLfloat *buffer)
ctypedef void (*PFNGLINDEXSPROC)(GLshort c)
ctypedef void (*PFNGLFOGIVPROC)(GLenum pname, const GLint *params)
ctypedef void (*PFNGLTRANSLATEDPROC)(GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*PFNGLTEXCOORD3SPROC)(GLshort s, GLshort t, GLshort r)
ctypedef void (*PFNGLTEXCOORD2IPROC)(GLint s, GLint t)
ctypedef void (*PFNGLMAP1FPROC)(GLenum target, GLfloat u1, GLfloat u2, GLint stride, GLint order, const GLfloat *points)
ctypedef void (*PFNGLTEXCOORD2DPROC)(GLdouble s, GLdouble t)
ctypedef void (*PFNGLTEXCOORD3DVPROC)(const GLdouble *v)

cdef PFNGLLISTBASEPROC cglListBase = NULL
cdef PFNGLRASTERPOS2SPROC cglRasterPos2s = NULL
cdef PFNGLLIGHTMODELIPROC cglLightModeli = NULL
cdef PFNGLINDEXIVPROC cglIndexiv = NULL
cdef PFNGLTEXPARAMETERIVPROC cglTexParameteriv = NULL
cdef PFNGLCOLOR4UBVPROC cglColor4ubv = NULL
cdef PFNGLREADPIXELSPROC cglReadPixels = NULL
cdef PFNGLTEXCOORD2FVPROC cglTexCoord2fv = NULL
cdef PFNGLPIXELSTOREFPROC cglPixelStoref = NULL
cdef PFNGLLIGHTFVPROC cglLightfv = NULL
cdef PFNGLDRAWPIXELSPROC cglDrawPixels = NULL
cdef PFNGLCOLOR3UIVPROC cglColor3uiv = NULL
cdef PFNGLMATERIALFVPROC cglMaterialfv = NULL
cdef PFNGLFRUSTUMPROC cglFrustum = NULL
cdef PFNGLVERTEX2FPROC cglVertex2f = NULL
cdef PFNGLSTENCILFUNCPROC cglStencilFunc = NULL
cdef PFNGLTEXENVFPROC cglTexEnvf = NULL
cdef PFNGLRECTSVPROC cglRectsv = NULL
cdef PFNGLEVALCOORD1FVPROC cglEvalCoord1fv = NULL
cdef PFNGLGETTEXPARAMETERFVPROC cglGetTexParameterfv = NULL
cdef PFNGLRECTSPROC cglRects = NULL
cdef PFNGLREADBUFFERPROC cglReadBuffer = NULL
cdef PFNGLRASTERPOS4DVPROC cglRasterPos4dv = NULL
cdef PFNGLDEPTHFUNCPROC cglDepthFunc = NULL
cdef PFNGLTEXGENDPROC cglTexGend = NULL
cdef PFNGLLOADMATRIXFPROC cglLoadMatrixf = NULL
cdef PFNGLEVALCOORD2FPROC cglEvalCoord2f = NULL
cdef PFNGLDELETELISTSPROC cglDeleteLists = NULL
cdef PFNGLMULTMATRIXDPROC cglMultMatrixd = NULL
cdef PFNGLPUSHMATRIXPROC cglPushMatrix = NULL
cdef PFNGLGETMAPDVPROC cglGetMapdv = NULL
cdef PFNGLRASTERPOS4FPROC cglRasterPos4f = NULL
cdef PFNGLCOLOR4USPROC cglColor4us = NULL
cdef PFNGLTEXGENIVPROC cglTexGeniv = NULL
cdef PFNGLTEXENVIPROC cglTexEnvi = NULL
cdef PFNGLTEXENVIVPROC cglTexEnviv = NULL
cdef PFNGLSCALEDPROC cglScaled = NULL
cdef PFNGLISENABLEDPROC cglIsEnabled = NULL
cdef PFNGLCOLOR3IVPROC cglColor3iv = NULL
cdef PFNGLNORMAL3DPROC cglNormal3d = NULL
cdef PFNGLVERTEX4FPROC cglVertex4f = NULL
cdef PFNGLLIGHTMODELIVPROC cglLightModeliv = NULL
cdef PFNGLGETLIGHTFVPROC cglGetLightfv = NULL
cdef PFNGLRASTERPOS3FPROC cglRasterPos3f = NULL
cdef PFNGLGENLISTSPROC cglGenLists = NULL
cdef PFNGLEVALCOORD1DVPROC cglEvalCoord1dv = NULL
cdef PFNGLCLEARINDEXPROC cglClearIndex = NULL
cdef PFNGLINDEXFVPROC cglIndexfv = NULL
cdef PFNGLRASTERPOS4SVPROC cglRasterPos4sv = NULL
cdef PFNGLMAPGRID2FPROC cglMapGrid2f = NULL
cdef PFNGLCOPYPIXELSPROC cglCopyPixels = NULL
cdef PFNGLVERTEX4IVPROC cglVertex4iv = NULL
cdef PFNGLPOPNAMEPROC cglPopName = NULL
cdef PFNGLTEXCOORD4IPROC cglTexCoord4i = NULL
cdef PFNGLDISABLEPROC cglDisable = NULL
cdef PFNGLCALLLISTPROC cglCallList = NULL
cdef PFNGLNORMAL3DVPROC cglNormal3dv = NULL
cdef PFNGLPOLYGONMODEPROC cglPolygonMode = NULL
cdef PFNGLCOLOR3FPROC cglColor3f = NULL
cdef PFNGLLIGHTIVPROC cglLightiv = NULL
cdef PFNGLCOLOR4SVPROC cglColor4sv = NULL
cdef PFNGLTEXCOORD3SVPROC cglTexCoord3sv = NULL
cdef PFNGLVERTEX2DVPROC cglVertex2dv = NULL
cdef PFNGLRASTERPOS4DPROC cglRasterPos4d = NULL
cdef PFNGLMATERIALIPROC cglMateriali = NULL
cdef PFNGLPIXELMAPUIVPROC cglPixelMapuiv = NULL
cdef PFNGLROTATEDPROC cglRotated = NULL
cdef PFNGLNORMAL3FVPROC cglNormal3fv = NULL
cdef PFNGLCOLOR3BPROC cglColor3b = NULL
cdef PFNGLLOGICOPPROC cglLogicOp = NULL
cdef PFNGLCOLOR4UIPROC cglColor4ui = NULL
cdef PFNGLTEXCOORD3IVPROC cglTexCoord3iv = NULL
cdef PFNGLTEXCOORD1SVPROC cglTexCoord1sv = NULL
cdef PFNGLGETMATERIALFVPROC cglGetMaterialfv = NULL
cdef PFNGLCOLOR3UIPROC cglColor3ui = NULL
cdef PFNGLVERTEX3FVPROC cglVertex3fv = NULL
cdef PFNGLCLEARDEPTHPROC cglClearDepth = NULL
cdef PFNGLNEWLISTPROC cglNewList = NULL
cdef PFNGLORTHOPROC cglOrtho = NULL
cdef PFNGLDEPTHMASKPROC cglDepthMask = NULL
cdef PFNGLVERTEX4SPROC cglVertex4s = NULL
cdef PFNGLVERTEX3DPROC cglVertex3d = NULL
cdef PFNGLPASSTHROUGHPROC cglPassThrough = NULL
cdef PFNGLENABLEPROC cglEnable = NULL
cdef PFNGLFLUSHPROC cglFlush = NULL
cdef PFNGLLOADNAMEPROC cglLoadName = NULL
cdef PFNGLCALLLISTSPROC cglCallLists = NULL
cdef PFNGLNORMAL3IPROC cglNormal3i = NULL
cdef PFNGLEVALCOORD2FVPROC cglEvalCoord2fv = NULL
cdef PFNGLPOPMATRIXPROC cglPopMatrix = NULL
cdef PFNGLFINISHPROC cglFinish = NULL
cdef PFNGLSELECTBUFFERPROC cglSelectBuffer = NULL
cdef PFNGLCOLOR3DVPROC cglColor3dv = NULL
cdef PFNGLCOLOR4DVPROC cglColor4dv = NULL
cdef PFNGLGETBOOLEANVPROC cglGetBooleanv = NULL
cdef PFNGLCOLOR3SVPROC cglColor3sv = NULL
cdef PFNGLEVALPOINT2PROC cglEvalPoint2 = NULL
cdef PFNGLCLEARACCUMPROC cglClearAccum = NULL
cdef PFNGLCOLOR4BVPROC cglColor4bv = NULL
cdef PFNGLVERTEX4DVPROC cglVertex4dv = NULL
cdef PFNGLTEXCOORD1DPROC cglTexCoord1d = NULL
cdef PFNGLRASTERPOS3DPROC cglRasterPos3d = NULL
cdef PFNGLTEXCOORD2IVPROC cglTexCoord2iv = NULL
cdef PFNGLACCUMPROC cglAccum = NULL
cdef PFNGLCOLOR4USVPROC cglColor4usv = NULL
cdef PFNGLNORMAL3SVPROC cglNormal3sv = NULL
cdef PFNGLTEXGENFVPROC cglTexGenfv = NULL
cdef PFNGLCOLOR4BPROC cglColor4b = NULL
cdef PFNGLTEXGENIPROC cglTexGeni = NULL
cdef PFNGLCLEARSTENCILPROC cglClearStencil = NULL
cdef PFNGLVERTEX2DPROC cglVertex2d = NULL
cdef PFNGLVERTEX4IPROC cglVertex4i = NULL
cdef PFNGLEVALPOINT1PROC cglEvalPoint1 = NULL
cdef PFNGLNORMAL3FPROC cglNormal3f = NULL
cdef PFNGLEVALMESH1PROC cglEvalMesh1 = NULL
cdef PFNGLTEXCOORD2DVPROC cglTexCoord2dv = NULL
cdef PFNGLHINTPROC cglHint = NULL
cdef PFNGLPOINTSIZEPROC cglPointSize = NULL
cdef PFNGLCLEARCOLORPROC cglClearColor = NULL
cdef PFNGLTEXCOORD1FPROC cglTexCoord1f = NULL
cdef PFNGLFRONTFACEPROC cglFrontFace = NULL
cdef PFNGLCOLOR3FVPROC cglColor3fv = NULL
cdef PFNGLEDGEFLAGPROC cglEdgeFlag = NULL
cdef PFNGLTEXCOORD1SPROC cglTexCoord1s = NULL
cdef PFNGLTEXCOORD2FPROC cglTexCoord2f = NULL
cdef PFNGLTEXCOORD4FPROC cglTexCoord4f = NULL
cdef PFNGLFOGFPROC cglFogf = NULL
cdef PFNGLPUSHATTRIBPROC cglPushAttrib = NULL
cdef PFNGLCOLOR4FPROC cglColor4f = NULL
cdef PFNGLBITMAPPROC cglBitmap = NULL
cdef PFNGLCOLOR4DPROC cglColor4d = NULL
cdef PFNGLTEXPARAMETERIPROC cglTexParameteri = NULL
cdef PFNGLENDLISTPROC cglEndList = NULL
cdef PFNGLRASTERPOS2IPROC cglRasterPos2i = NULL
cdef PFNGLRASTERPOS3SVPROC cglRasterPos3sv = NULL
cdef PFNGLCULLFACEPROC cglCullFace = NULL
cdef PFNGLGETCLIPPLANEPROC cglGetClipPlane = NULL
cdef PFNGLRASTERPOS3IVPROC cglRasterPos3iv = NULL
cdef PFNGLTEXCOORD4SVPROC cglTexCoord4sv = NULL
cdef PFNGLMATERIALIVPROC cglMaterialiv = NULL
cdef PFNGLVIEWPORTPROC cglViewport = NULL
cdef PFNGLTEXCOORD4IVPROC cglTexCoord4iv = NULL
cdef PFNGLSTENCILOPPROC cglStencilOp = NULL
cdef PFNGLCOLOR4IVPROC cglColor4iv = NULL
cdef PFNGLCOLOR3USPROC cglColor3us = NULL
cdef PFNGLTEXPARAMETERFVPROC cglTexParameterfv = NULL
cdef PFNGLNORMAL3IVPROC cglNormal3iv = NULL
cdef PFNGLPIXELZOOMPROC cglPixelZoom = NULL
cdef PFNGLNORMAL3BVPROC cglNormal3bv = NULL
cdef PFNGLPIXELTRANSFERIPROC cglPixelTransferi = NULL
cdef PFNGLGETTEXENVIVPROC cglGetTexEnviv = NULL
cdef PFNGLDEPTHRANGEPROC cglDepthRange = NULL
cdef PFNGLRECTIPROC cglRecti = NULL
cdef PFNGLTEXCOORD1IPROC cglTexCoord1i = NULL
cdef PFNGLTEXENVFVPROC cglTexEnvfv = NULL
cdef PFNGLINDEXDVPROC cglIndexdv = NULL
cdef PFNGLVERTEX2SVPROC cglVertex2sv = NULL
cdef PFNGLGETTEXIMAGEPROC cglGetTexImage = NULL
cdef PFNGLRECTFVPROC cglRectfv = NULL
cdef PFNGLCOLORMASKPROC cglColorMask = NULL
cdef PFNGLPOPATTRIBPROC cglPopAttrib = NULL
cdef PFNGLGETMAPFVPROC cglGetMapfv = NULL
cdef PFNGLTEXCOORD2SPROC cglTexCoord2s = NULL
cdef PFNGLSTENCILMASKPROC cglStencilMask = NULL
cdef PFNGLPOLYGONSTIPPLEPROC cglPolygonStipple = NULL
cdef PFNGLPUSHNAMEPROC cglPushName = NULL
cdef PFNGLEVALCOORD2DPROC cglEvalCoord2d = NULL
cdef PFNGLRASTERPOS2DVPROC cglRasterPos2dv = NULL
cdef PFNGLGETLIGHTIVPROC cglGetLightiv = NULL
cdef PFNGLGETDOUBLEVPROC cglGetDoublev = NULL
cdef PFNGLTEXCOORD4DVPROC cglTexCoord4dv = NULL
cdef PFNGLGETMAPIVPROC cglGetMapiv = NULL
cdef PFNGLVERTEX2IVPROC cglVertex2iv = NULL
cdef PFNGLTEXCOORD4SPROC cglTexCoord4s = NULL
cdef PFNGLDRAWBUFFERPROC cglDrawBuffer = NULL
cdef PFNGLRECTDPROC cglRectd = NULL
cdef PFNGLPIXELMAPFVPROC cglPixelMapfv = NULL
cdef PFNGLISLISTPROC cglIsList = NULL
cdef PFNGLRASTERPOS4IPROC cglRasterPos4i = NULL
cdef PFNGLGETTEXGENDVPROC cglGetTexGendv = NULL
cdef PFNGLMAP2DPROC cglMap2d = NULL
cdef PFNGLTEXCOORD4FVPROC cglTexCoord4fv = NULL
cdef PFNGLRASTERPOS2SVPROC cglRasterPos2sv = NULL
cdef PFNGLLIGHTIPROC cglLighti = NULL
cdef PFNGLRASTERPOS4SPROC cglRasterPos4s = NULL
cdef PFNGLCOLOR3SPROC cglColor3s = NULL
cdef PFNGLRASTERPOS2DPROC cglRasterPos2d = NULL
cdef PFNGLCOLOR3UBPROC cglColor3ub = NULL
cdef PFNGLRASTERPOS4FVPROC cglRasterPos4fv = NULL
cdef PFNGLINDEXSVPROC cglIndexsv = NULL
cdef PFNGLROTATEFPROC cglRotatef = NULL
cdef PFNGLRASTERPOS2FPROC cglRasterPos2f = NULL
cdef PFNGLTRANSLATEFPROC cglTranslatef = NULL
cdef PFNGLINDEXDPROC cglIndexd = NULL
cdef PFNGLNORMAL3SPROC cglNormal3s = NULL
cdef PFNGLGETTEXGENIVPROC cglGetTexGeniv = NULL
cdef PFNGLGETINTEGERVPROC cglGetIntegerv = NULL
cdef PFNGLLIGHTMODELFVPROC cglLightModelfv = NULL
cdef PFNGLVERTEX2IPROC cglVertex2i = NULL
cdef PFNGLTEXCOORD1DVPROC cglTexCoord1dv = NULL
cdef PFNGLTEXCOORD1FVPROC cglTexCoord1fv = NULL
cdef PFNGLCOLOR3IPROC cglColor3i = NULL
cdef PFNGLVERTEX3IVPROC cglVertex3iv = NULL
cdef PFNGLMATRIXMODEPROC cglMatrixMode = NULL
cdef PFNGLRECTFPROC cglRectf = NULL
cdef PFNGLMAP1DPROC cglMap1d = NULL
cdef PFNGLINDEXFPROC cglIndexf = NULL
cdef PFNGLVERTEX3SVPROC cglVertex3sv = NULL
cdef PFNGLLIGHTMODELFPROC cglLightModelf = NULL
cdef PFNGLGETPIXELMAPFVPROC cglGetPixelMapfv = NULL
cdef PFNGLPIXELMAPUSVPROC cglPixelMapusv = NULL
cdef PFNGLRASTERPOS4IVPROC cglRasterPos4iv = NULL
cdef PFNGLTEXCOORD3FPROC cglTexCoord3f = NULL
cdef PFNGLLOADMATRIXDPROC cglLoadMatrixd = NULL
cdef PFNGLLINEWIDTHPROC cglLineWidth = NULL
cdef PFNGLSCISSORPROC cglScissor = NULL
cdef PFNGLGETTEXLEVELPARAMETERFVPROC cglGetTexLevelParameterfv = NULL
cdef PFNGLTEXCOORD3FVPROC cglTexCoord3fv = NULL
cdef PFNGLLOADIDENTITYPROC cglLoadIdentity = NULL
cdef PFNGLRASTERPOS2FVPROC cglRasterPos2fv = NULL
cdef PFNGLTEXPARAMETERFPROC cglTexParameterf = NULL
cdef PFNGLTEXCOORD1IVPROC cglTexCoord1iv = NULL
cdef PFNGLINITNAMESPROC cglInitNames = NULL
cdef PFNGLMAPGRID1FPROC cglMapGrid1f = NULL
cdef PFNGLTEXIMAGE2DPROC cglTexImage2D = NULL
cdef PFNGLGETPOLYGONSTIPPLEPROC cglGetPolygonStipple = NULL
cdef PFNGLEVALCOORD2DVPROC cglEvalCoord2dv = NULL
cdef PFNGLENDPROC cglEnd = NULL
cdef PFNGLMAPGRID1DPROC cglMapGrid1d = NULL
cdef PFNGLCOLORMATERIALPROC cglColorMaterial = NULL
cdef PFNGLMULTMATRIXFPROC cglMultMatrixf = NULL
cdef PFNGLMAP2FPROC cglMap2f = NULL
cdef PFNGLPIXELTRANSFERFPROC cglPixelTransferf = NULL
cdef PFNGLVERTEX3FPROC cglVertex3f = NULL
cdef PFNGLCOLOR3USVPROC cglColor3usv = NULL
cdef PFNGLCOLOR4FVPROC cglColor4fv = NULL
cdef PFNGLPIXELSTOREIPROC cglPixelStorei = NULL
cdef PFNGLMATERIALFPROC cglMaterialf = NULL
cdef PFNGLTEXIMAGE1DPROC cglTexImage1D = NULL
cdef PFNGLVERTEX3DVPROC cglVertex3dv = NULL
cdef PFNGLLINESTIPPLEPROC cglLineStipple = NULL
cdef PFNGLCOLOR4SPROC cglColor4s = NULL
cdef PFNGLMAPGRID2DPROC cglMapGrid2d = NULL
cdef PFNGLVERTEX3IPROC cglVertex3i = NULL
cdef PFNGLGETTEXLEVELPARAMETERIVPROC cglGetTexLevelParameteriv = NULL
cdef PFNGLGETMATERIALIVPROC cglGetMaterialiv = NULL
cdef PFNGLVERTEX4DPROC cglVertex4d = NULL
cdef PFNGLVERTEX4SVPROC cglVertex4sv = NULL
cdef PFNGLGETTEXPARAMETERIVPROC cglGetTexParameteriv = NULL
cdef PFNGLGETFLOATVPROC cglGetFloatv = NULL
cdef PFNGLSHADEMODELPROC cglShadeModel = NULL
cdef PFNGLGETPIXELMAPUIVPROC cglGetPixelMapuiv = NULL
cdef PFNGLCLIPPLANEPROC cglClipPlane = NULL
cdef PFNGLGETTEXENVFVPROC cglGetTexEnvfv = NULL
cdef PFNGLRASTERPOS2IVPROC cglRasterPos2iv = NULL
cdef PFNGLINDEXIPROC cglIndexi = NULL
cdef PFNGLVERTEX4FVPROC cglVertex4fv = NULL
cdef PFNGLINDEXMASKPROC cglIndexMask = NULL
cdef PFNGLRASTERPOS3DVPROC cglRasterPos3dv = NULL
cdef PFNGLCOLOR3UBVPROC cglColor3ubv = NULL
cdef PFNGLGETERRORPROC cglGetError = NULL
cdef PFNGLCOLOR3BVPROC cglColor3bv = NULL
cdef PFNGLTEXCOORD3IPROC cglTexCoord3i = NULL
cdef PFNGLTEXGENFPROC cglTexGenf = NULL
cdef PFNGLGETSTRINGPROC cglGetString = NULL
cdef PFNGLGETTEXGENFVPROC cglGetTexGenfv = NULL
cdef PFNGLRASTERPOS3FVPROC cglRasterPos3fv = NULL
cdef PFNGLCOLOR3DPROC cglColor3d = NULL
cdef PFNGLSCALEFPROC cglScalef = NULL
cdef PFNGLRASTERPOS3SPROC cglRasterPos3s = NULL
cdef PFNGLEDGEFLAGVPROC cglEdgeFlagv = NULL
cdef PFNGLTEXCOORD2SVPROC cglTexCoord2sv = NULL
cdef PFNGLTEXCOORD3DPROC cglTexCoord3d = NULL
cdef PFNGLEVALCOORD1DPROC cglEvalCoord1d = NULL
cdef PFNGLCOLOR4IPROC cglColor4i = NULL
cdef PFNGLCOLOR4UIVPROC cglColor4uiv = NULL
cdef PFNGLALPHAFUNCPROC cglAlphaFunc = NULL
cdef PFNGLVERTEX2FVPROC cglVertex2fv = NULL
cdef PFNGLGETPIXELMAPUSVPROC cglGetPixelMapusv = NULL
cdef PFNGLCLEARPROC cglClear = NULL
cdef PFNGLBLENDFUNCPROC cglBlendFunc = NULL
cdef PFNGLRASTERPOS3IPROC cglRasterPos3i = NULL
cdef PFNGLVERTEX3SPROC cglVertex3s = NULL
cdef PFNGLCOLOR4UBPROC cglColor4ub = NULL
cdef PFNGLRECTDVPROC cglRectdv = NULL
cdef PFNGLNORMAL3BPROC cglNormal3b = NULL
cdef PFNGLFOGIPROC cglFogi = NULL
cdef PFNGLRENDERMODEPROC cglRenderMode = NULL
cdef PFNGLEVALCOORD1FPROC cglEvalCoord1f = NULL
cdef PFNGLVERTEX2SPROC cglVertex2s = NULL
cdef PFNGLRECTIVPROC cglRectiv = NULL
cdef PFNGLEVALMESH2PROC cglEvalMesh2 = NULL
cdef PFNGLFOGFVPROC cglFogfv = NULL
cdef PFNGLTEXCOORD4DPROC cglTexCoord4d = NULL
cdef PFNGLLIGHTFPROC cglLightf = NULL
cdef PFNGLTEXGENDVPROC cglTexGendv = NULL
cdef PFNGLBEGINPROC cglBegin = NULL
cdef PFNGLFEEDBACKBUFFERPROC cglFeedbackBuffer = NULL
cdef PFNGLINDEXSPROC cglIndexs = NULL
cdef PFNGLFOGIVPROC cglFogiv = NULL
cdef PFNGLTRANSLATEDPROC cglTranslated = NULL
cdef PFNGLTEXCOORD3SPROC cglTexCoord3s = NULL
cdef PFNGLTEXCOORD2IPROC cglTexCoord2i = NULL
cdef PFNGLMAP1FPROC cglMap1f = NULL
cdef PFNGLTEXCOORD2DPROC cglTexCoord2d = NULL
cdef PFNGLTEXCOORD3DVPROC cglTexCoord3dv = NULL


cdef void GetglListBase(GLuint base):
    global cglListBase
    cglListBase = <PFNGLLISTBASEPROC>getFunction(b"glListBase")
    cglListBase(base)

cdef void GetglRasterPos2s(GLshort x, GLshort y):
    global cglRasterPos2s
    cglRasterPos2s = <PFNGLRASTERPOS2SPROC>getFunction(b"glRasterPos2s")
    cglRasterPos2s(x, y)

cdef void GetglLightModeli(GLenum pname, GLint param):
    global cglLightModeli
    cglLightModeli = <PFNGLLIGHTMODELIPROC>getFunction(b"glLightModeli")
    cglLightModeli(pname, param)

cdef void GetglIndexiv(const GLint *c):
    global cglIndexiv
    cglIndexiv = <PFNGLINDEXIVPROC>getFunction(b"glIndexiv")
    cglIndexiv(c)

cdef void GetglTexParameteriv(GLenum target, GLenum pname, const GLint *params):
    global cglTexParameteriv
    cglTexParameteriv = <PFNGLTEXPARAMETERIVPROC>getFunction(b"glTexParameteriv")
    cglTexParameteriv(target, pname, params)

cdef void GetglColor4ubv(const GLubyte *v):
    global cglColor4ubv
    cglColor4ubv = <PFNGLCOLOR4UBVPROC>getFunction(b"glColor4ubv")
    cglColor4ubv(v)

cdef void GetglReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, void *pixels):
    global cglReadPixels
    cglReadPixels = <PFNGLREADPIXELSPROC>getFunction(b"glReadPixels")
    cglReadPixels(x, y, width, height, format, type, pixels)

cdef void GetglTexCoord2fv(const GLfloat *v):
    global cglTexCoord2fv
    cglTexCoord2fv = <PFNGLTEXCOORD2FVPROC>getFunction(b"glTexCoord2fv")
    cglTexCoord2fv(v)

cdef void GetglPixelStoref(GLenum pname, GLfloat param):
    global cglPixelStoref
    cglPixelStoref = <PFNGLPIXELSTOREFPROC>getFunction(b"glPixelStoref")
    cglPixelStoref(pname, param)

cdef void GetglLightfv(GLenum light, GLenum pname, const GLfloat *params):
    global cglLightfv
    cglLightfv = <PFNGLLIGHTFVPROC>getFunction(b"glLightfv")
    cglLightfv(light, pname, params)

cdef void GetglDrawPixels(GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    global cglDrawPixels
    cglDrawPixels = <PFNGLDRAWPIXELSPROC>getFunction(b"glDrawPixels")
    cglDrawPixels(width, height, format, type, pixels)

cdef void GetglColor3uiv(const GLuint *v):
    global cglColor3uiv
    cglColor3uiv = <PFNGLCOLOR3UIVPROC>getFunction(b"glColor3uiv")
    cglColor3uiv(v)

cdef void GetglMaterialfv(GLenum face, GLenum pname, const GLfloat *params):
    global cglMaterialfv
    cglMaterialfv = <PFNGLMATERIALFVPROC>getFunction(b"glMaterialfv")
    cglMaterialfv(face, pname, params)

cdef void GetglFrustum(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar):
    global cglFrustum
    cglFrustum = <PFNGLFRUSTUMPROC>getFunction(b"glFrustum")
    cglFrustum(left, right, bottom, top, zNear, zFar)

cdef void GetglVertex2f(GLfloat x, GLfloat y):
    global cglVertex2f
    cglVertex2f = <PFNGLVERTEX2FPROC>getFunction(b"glVertex2f")
    cglVertex2f(x, y)

cdef void GetglStencilFunc(GLenum func, GLint ref, GLuint mask):
    global cglStencilFunc
    cglStencilFunc = <PFNGLSTENCILFUNCPROC>getFunction(b"glStencilFunc")
    cglStencilFunc(func, ref, mask)

cdef void GetglTexEnvf(GLenum target, GLenum pname, GLfloat param):
    global cglTexEnvf
    cglTexEnvf = <PFNGLTEXENVFPROC>getFunction(b"glTexEnvf")
    cglTexEnvf(target, pname, param)

cdef void GetglRectsv(const GLshort *v1, const GLshort *v2):
    global cglRectsv
    cglRectsv = <PFNGLRECTSVPROC>getFunction(b"glRectsv")
    cglRectsv(v1, v2)

cdef void GetglEvalCoord1fv(const GLfloat *u):
    global cglEvalCoord1fv
    cglEvalCoord1fv = <PFNGLEVALCOORD1FVPROC>getFunction(b"glEvalCoord1fv")
    cglEvalCoord1fv(u)

cdef void GetglGetTexParameterfv(GLenum target, GLenum pname, GLfloat *params):
    global cglGetTexParameterfv
    cglGetTexParameterfv = <PFNGLGETTEXPARAMETERFVPROC>getFunction(b"glGetTexParameterfv")
    cglGetTexParameterfv(target, pname, params)

cdef void GetglRects(GLshort x1, GLshort y1, GLshort x2, GLshort y2):
    global cglRects
    cglRects = <PFNGLRECTSPROC>getFunction(b"glRects")
    cglRects(x1, y1, x2, y2)

cdef void GetglReadBuffer(GLenum src):
    global cglReadBuffer
    cglReadBuffer = <PFNGLREADBUFFERPROC>getFunction(b"glReadBuffer")
    cglReadBuffer(src)

cdef void GetglRasterPos4dv(const GLdouble *v):
    global cglRasterPos4dv
    cglRasterPos4dv = <PFNGLRASTERPOS4DVPROC>getFunction(b"glRasterPos4dv")
    cglRasterPos4dv(v)

cdef void GetglDepthFunc(GLenum func):
    global cglDepthFunc
    cglDepthFunc = <PFNGLDEPTHFUNCPROC>getFunction(b"glDepthFunc")
    cglDepthFunc(func)

cdef void GetglTexGend(GLenum coord, GLenum pname, GLdouble param):
    global cglTexGend
    cglTexGend = <PFNGLTEXGENDPROC>getFunction(b"glTexGend")
    cglTexGend(coord, pname, param)

cdef void GetglLoadMatrixf(const GLfloat *m):
    global cglLoadMatrixf
    cglLoadMatrixf = <PFNGLLOADMATRIXFPROC>getFunction(b"glLoadMatrixf")
    cglLoadMatrixf(m)

cdef void GetglEvalCoord2f(GLfloat u, GLfloat v):
    global cglEvalCoord2f
    cglEvalCoord2f = <PFNGLEVALCOORD2FPROC>getFunction(b"glEvalCoord2f")
    cglEvalCoord2f(u, v)

cdef void GetglDeleteLists(GLuint list, GLsizei range):
    global cglDeleteLists
    cglDeleteLists = <PFNGLDELETELISTSPROC>getFunction(b"glDeleteLists")
    cglDeleteLists(list, range)

cdef void GetglMultMatrixd(const GLdouble *m):
    global cglMultMatrixd
    cglMultMatrixd = <PFNGLMULTMATRIXDPROC>getFunction(b"glMultMatrixd")
    cglMultMatrixd(m)

cdef void GetglPushMatrix():
    global cglPushMatrix
    cglPushMatrix = <PFNGLPUSHMATRIXPROC>getFunction(b"glPushMatrix")
    cglPushMatrix()

cdef void GetglGetMapdv(GLenum target, GLenum query, GLdouble *v):
    global cglGetMapdv
    cglGetMapdv = <PFNGLGETMAPDVPROC>getFunction(b"glGetMapdv")
    cglGetMapdv(target, query, v)

cdef void GetglRasterPos4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    global cglRasterPos4f
    cglRasterPos4f = <PFNGLRASTERPOS4FPROC>getFunction(b"glRasterPos4f")
    cglRasterPos4f(x, y, z, w)

cdef void GetglColor4us(GLushort red, GLushort green, GLushort blue, GLushort alpha):
    global cglColor4us
    cglColor4us = <PFNGLCOLOR4USPROC>getFunction(b"glColor4us")
    cglColor4us(red, green, blue, alpha)

cdef void GetglTexGeniv(GLenum coord, GLenum pname, const GLint *params):
    global cglTexGeniv
    cglTexGeniv = <PFNGLTEXGENIVPROC>getFunction(b"glTexGeniv")
    cglTexGeniv(coord, pname, params)

cdef void GetglTexEnvi(GLenum target, GLenum pname, GLint param):
    global cglTexEnvi
    cglTexEnvi = <PFNGLTEXENVIPROC>getFunction(b"glTexEnvi")
    cglTexEnvi(target, pname, param)

cdef void GetglTexEnviv(GLenum target, GLenum pname, const GLint *params):
    global cglTexEnviv
    cglTexEnviv = <PFNGLTEXENVIVPROC>getFunction(b"glTexEnviv")
    cglTexEnviv(target, pname, params)

cdef void GetglScaled(GLdouble x, GLdouble y, GLdouble z):
    global cglScaled
    cglScaled = <PFNGLSCALEDPROC>getFunction(b"glScaled")
    cglScaled(x, y, z)

cdef GLboolean GetglIsEnabled(GLenum cap):
    global cglIsEnabled
    cglIsEnabled = <PFNGLISENABLEDPROC>getFunction(b"glIsEnabled")
    cglIsEnabled(cap)

cdef void GetglColor3iv(const GLint *v):
    global cglColor3iv
    cglColor3iv = <PFNGLCOLOR3IVPROC>getFunction(b"glColor3iv")
    cglColor3iv(v)

cdef void GetglNormal3d(GLdouble nx, GLdouble ny, GLdouble nz):
    global cglNormal3d
    cglNormal3d = <PFNGLNORMAL3DPROC>getFunction(b"glNormal3d")
    cglNormal3d(nx, ny, nz)

cdef void GetglVertex4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    global cglVertex4f
    cglVertex4f = <PFNGLVERTEX4FPROC>getFunction(b"glVertex4f")
    cglVertex4f(x, y, z, w)

cdef void GetglLightModeliv(GLenum pname, const GLint *params):
    global cglLightModeliv
    cglLightModeliv = <PFNGLLIGHTMODELIVPROC>getFunction(b"glLightModeliv")
    cglLightModeliv(pname, params)

cdef void GetglGetLightfv(GLenum light, GLenum pname, GLfloat *params):
    global cglGetLightfv
    cglGetLightfv = <PFNGLGETLIGHTFVPROC>getFunction(b"glGetLightfv")
    cglGetLightfv(light, pname, params)

cdef void GetglRasterPos3f(GLfloat x, GLfloat y, GLfloat z):
    global cglRasterPos3f
    cglRasterPos3f = <PFNGLRASTERPOS3FPROC>getFunction(b"glRasterPos3f")
    cglRasterPos3f(x, y, z)

cdef GLuint GetglGenLists(GLsizei range):
    global cglGenLists
    cglGenLists = <PFNGLGENLISTSPROC>getFunction(b"glGenLists")
    cglGenLists(range)

cdef void GetglEvalCoord1dv(const GLdouble *u):
    global cglEvalCoord1dv
    cglEvalCoord1dv = <PFNGLEVALCOORD1DVPROC>getFunction(b"glEvalCoord1dv")
    cglEvalCoord1dv(u)

cdef void GetglClearIndex(GLfloat c):
    global cglClearIndex
    cglClearIndex = <PFNGLCLEARINDEXPROC>getFunction(b"glClearIndex")
    cglClearIndex(c)

cdef void GetglIndexfv(const GLfloat *c):
    global cglIndexfv
    cglIndexfv = <PFNGLINDEXFVPROC>getFunction(b"glIndexfv")
    cglIndexfv(c)

cdef void GetglRasterPos4sv(const GLshort *v):
    global cglRasterPos4sv
    cglRasterPos4sv = <PFNGLRASTERPOS4SVPROC>getFunction(b"glRasterPos4sv")
    cglRasterPos4sv(v)

cdef void GetglMapGrid2f(GLint un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2):
    global cglMapGrid2f
    cglMapGrid2f = <PFNGLMAPGRID2FPROC>getFunction(b"glMapGrid2f")
    cglMapGrid2f(un, u1, u2, vn, v1, v2)

cdef void GetglCopyPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum type):
    global cglCopyPixels
    cglCopyPixels = <PFNGLCOPYPIXELSPROC>getFunction(b"glCopyPixels")
    cglCopyPixels(x, y, width, height, type)

cdef void GetglVertex4iv(const GLint *v):
    global cglVertex4iv
    cglVertex4iv = <PFNGLVERTEX4IVPROC>getFunction(b"glVertex4iv")
    cglVertex4iv(v)

cdef void GetglPopName():
    global cglPopName
    cglPopName = <PFNGLPOPNAMEPROC>getFunction(b"glPopName")
    cglPopName()

cdef void GetglTexCoord4i(GLint s, GLint t, GLint r, GLint q):
    global cglTexCoord4i
    cglTexCoord4i = <PFNGLTEXCOORD4IPROC>getFunction(b"glTexCoord4i")
    cglTexCoord4i(s, t, r, q)

cdef void GetglDisable(GLenum cap):
    global cglDisable
    cglDisable = <PFNGLDISABLEPROC>getFunction(b"glDisable")
    cglDisable(cap)

cdef void GetglCallList(GLuint list):
    global cglCallList
    cglCallList = <PFNGLCALLLISTPROC>getFunction(b"glCallList")
    cglCallList(list)

cdef void GetglNormal3dv(const GLdouble *v):
    global cglNormal3dv
    cglNormal3dv = <PFNGLNORMAL3DVPROC>getFunction(b"glNormal3dv")
    cglNormal3dv(v)

cdef void GetglPolygonMode(GLenum face, GLenum mode):
    global cglPolygonMode
    cglPolygonMode = <PFNGLPOLYGONMODEPROC>getFunction(b"glPolygonMode")
    cglPolygonMode(face, mode)

cdef void GetglColor3f(GLfloat red, GLfloat green, GLfloat blue):
    global cglColor3f
    cglColor3f = <PFNGLCOLOR3FPROC>getFunction(b"glColor3f")
    cglColor3f(red, green, blue)

cdef void GetglLightiv(GLenum light, GLenum pname, const GLint *params):
    global cglLightiv
    cglLightiv = <PFNGLLIGHTIVPROC>getFunction(b"glLightiv")
    cglLightiv(light, pname, params)

cdef void GetglColor4sv(const GLshort *v):
    global cglColor4sv
    cglColor4sv = <PFNGLCOLOR4SVPROC>getFunction(b"glColor4sv")
    cglColor4sv(v)

cdef void GetglTexCoord3sv(const GLshort *v):
    global cglTexCoord3sv
    cglTexCoord3sv = <PFNGLTEXCOORD3SVPROC>getFunction(b"glTexCoord3sv")
    cglTexCoord3sv(v)

cdef void GetglVertex2dv(const GLdouble *v):
    global cglVertex2dv
    cglVertex2dv = <PFNGLVERTEX2DVPROC>getFunction(b"glVertex2dv")
    cglVertex2dv(v)

cdef void GetglRasterPos4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglRasterPos4d
    cglRasterPos4d = <PFNGLRASTERPOS4DPROC>getFunction(b"glRasterPos4d")
    cglRasterPos4d(x, y, z, w)

cdef void GetglMateriali(GLenum face, GLenum pname, GLint param):
    global cglMateriali
    cglMateriali = <PFNGLMATERIALIPROC>getFunction(b"glMateriali")
    cglMateriali(face, pname, param)

cdef void GetglPixelMapuiv(GLenum map, GLsizei mapsize, const GLuint *values):
    global cglPixelMapuiv
    cglPixelMapuiv = <PFNGLPIXELMAPUIVPROC>getFunction(b"glPixelMapuiv")
    cglPixelMapuiv(map, mapsize, values)

cdef void GetglRotated(GLdouble angle, GLdouble x, GLdouble y, GLdouble z):
    global cglRotated
    cglRotated = <PFNGLROTATEDPROC>getFunction(b"glRotated")
    cglRotated(angle, x, y, z)

cdef void GetglNormal3fv(const GLfloat *v):
    global cglNormal3fv
    cglNormal3fv = <PFNGLNORMAL3FVPROC>getFunction(b"glNormal3fv")
    cglNormal3fv(v)

cdef void GetglColor3b(GLbyte red, GLbyte green, GLbyte blue):
    global cglColor3b
    cglColor3b = <PFNGLCOLOR3BPROC>getFunction(b"glColor3b")
    cglColor3b(red, green, blue)

cdef void GetglLogicOp(GLenum opcode):
    global cglLogicOp
    cglLogicOp = <PFNGLLOGICOPPROC>getFunction(b"glLogicOp")
    cglLogicOp(opcode)

cdef void GetglColor4ui(GLuint red, GLuint green, GLuint blue, GLuint alpha):
    global cglColor4ui
    cglColor4ui = <PFNGLCOLOR4UIPROC>getFunction(b"glColor4ui")
    cglColor4ui(red, green, blue, alpha)

cdef void GetglTexCoord3iv(const GLint *v):
    global cglTexCoord3iv
    cglTexCoord3iv = <PFNGLTEXCOORD3IVPROC>getFunction(b"glTexCoord3iv")
    cglTexCoord3iv(v)

cdef void GetglTexCoord1sv(const GLshort *v):
    global cglTexCoord1sv
    cglTexCoord1sv = <PFNGLTEXCOORD1SVPROC>getFunction(b"glTexCoord1sv")
    cglTexCoord1sv(v)

cdef void GetglGetMaterialfv(GLenum face, GLenum pname, GLfloat *params):
    global cglGetMaterialfv
    cglGetMaterialfv = <PFNGLGETMATERIALFVPROC>getFunction(b"glGetMaterialfv")
    cglGetMaterialfv(face, pname, params)

cdef void GetglColor3ui(GLuint red, GLuint green, GLuint blue):
    global cglColor3ui
    cglColor3ui = <PFNGLCOLOR3UIPROC>getFunction(b"glColor3ui")
    cglColor3ui(red, green, blue)

cdef void GetglVertex3fv(const GLfloat *v):
    global cglVertex3fv
    cglVertex3fv = <PFNGLVERTEX3FVPROC>getFunction(b"glVertex3fv")
    cglVertex3fv(v)

cdef void GetglClearDepth(GLdouble depth):
    global cglClearDepth
    cglClearDepth = <PFNGLCLEARDEPTHPROC>getFunction(b"glClearDepth")
    cglClearDepth(depth)

cdef void GetglNewList(GLuint list, GLenum mode):
    global cglNewList
    cglNewList = <PFNGLNEWLISTPROC>getFunction(b"glNewList")
    cglNewList(list, mode)

cdef void GetglOrtho(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar):
    global cglOrtho
    cglOrtho = <PFNGLORTHOPROC>getFunction(b"glOrtho")
    cglOrtho(left, right, bottom, top, zNear, zFar)

cdef void GetglDepthMask(GLboolean flag):
    global cglDepthMask
    cglDepthMask = <PFNGLDEPTHMASKPROC>getFunction(b"glDepthMask")
    cglDepthMask(flag)

cdef void GetglVertex4s(GLshort x, GLshort y, GLshort z, GLshort w):
    global cglVertex4s
    cglVertex4s = <PFNGLVERTEX4SPROC>getFunction(b"glVertex4s")
    cglVertex4s(x, y, z, w)

cdef void GetglVertex3d(GLdouble x, GLdouble y, GLdouble z):
    global cglVertex3d
    cglVertex3d = <PFNGLVERTEX3DPROC>getFunction(b"glVertex3d")
    cglVertex3d(x, y, z)

cdef void GetglPassThrough(GLfloat token):
    global cglPassThrough
    cglPassThrough = <PFNGLPASSTHROUGHPROC>getFunction(b"glPassThrough")
    cglPassThrough(token)

cdef void GetglEnable(GLenum cap):
    global cglEnable
    cglEnable = <PFNGLENABLEPROC>getFunction(b"glEnable")
    cglEnable(cap)

cdef void GetglFlush():
    global cglFlush
    cglFlush = <PFNGLFLUSHPROC>getFunction(b"glFlush")
    cglFlush()

cdef void GetglLoadName(GLuint name):
    global cglLoadName
    cglLoadName = <PFNGLLOADNAMEPROC>getFunction(b"glLoadName")
    cglLoadName(name)

cdef void GetglCallLists(GLsizei n, GLenum type, const void *lists):
    global cglCallLists
    cglCallLists = <PFNGLCALLLISTSPROC>getFunction(b"glCallLists")
    cglCallLists(n, type, lists)

cdef void GetglNormal3i(GLint nx, GLint ny, GLint nz):
    global cglNormal3i
    cglNormal3i = <PFNGLNORMAL3IPROC>getFunction(b"glNormal3i")
    cglNormal3i(nx, ny, nz)

cdef void GetglEvalCoord2fv(const GLfloat *u):
    global cglEvalCoord2fv
    cglEvalCoord2fv = <PFNGLEVALCOORD2FVPROC>getFunction(b"glEvalCoord2fv")
    cglEvalCoord2fv(u)

cdef void GetglPopMatrix():
    global cglPopMatrix
    cglPopMatrix = <PFNGLPOPMATRIXPROC>getFunction(b"glPopMatrix")
    cglPopMatrix()

cdef void GetglFinish():
    global cglFinish
    cglFinish = <PFNGLFINISHPROC>getFunction(b"glFinish")
    cglFinish()

cdef void GetglSelectBuffer(GLsizei size, GLuint *buffer):
    global cglSelectBuffer
    cglSelectBuffer = <PFNGLSELECTBUFFERPROC>getFunction(b"glSelectBuffer")
    cglSelectBuffer(size, buffer)

cdef void GetglColor3dv(const GLdouble *v):
    global cglColor3dv
    cglColor3dv = <PFNGLCOLOR3DVPROC>getFunction(b"glColor3dv")
    cglColor3dv(v)

cdef void GetglColor4dv(const GLdouble *v):
    global cglColor4dv
    cglColor4dv = <PFNGLCOLOR4DVPROC>getFunction(b"glColor4dv")
    cglColor4dv(v)

cdef void GetglGetBooleanv(GLenum pname, GLboolean *data):
    global cglGetBooleanv
    cglGetBooleanv = <PFNGLGETBOOLEANVPROC>getFunction(b"glGetBooleanv")
    cglGetBooleanv(pname, data)

cdef void GetglColor3sv(const GLshort *v):
    global cglColor3sv
    cglColor3sv = <PFNGLCOLOR3SVPROC>getFunction(b"glColor3sv")
    cglColor3sv(v)

cdef void GetglEvalPoint2(GLint i, GLint j):
    global cglEvalPoint2
    cglEvalPoint2 = <PFNGLEVALPOINT2PROC>getFunction(b"glEvalPoint2")
    cglEvalPoint2(i, j)

cdef void GetglClearAccum(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    global cglClearAccum
    cglClearAccum = <PFNGLCLEARACCUMPROC>getFunction(b"glClearAccum")
    cglClearAccum(red, green, blue, alpha)

cdef void GetglColor4bv(const GLbyte *v):
    global cglColor4bv
    cglColor4bv = <PFNGLCOLOR4BVPROC>getFunction(b"glColor4bv")
    cglColor4bv(v)

cdef void GetglVertex4dv(const GLdouble *v):
    global cglVertex4dv
    cglVertex4dv = <PFNGLVERTEX4DVPROC>getFunction(b"glVertex4dv")
    cglVertex4dv(v)

cdef void GetglTexCoord1d(GLdouble s):
    global cglTexCoord1d
    cglTexCoord1d = <PFNGLTEXCOORD1DPROC>getFunction(b"glTexCoord1d")
    cglTexCoord1d(s)

cdef void GetglRasterPos3d(GLdouble x, GLdouble y, GLdouble z):
    global cglRasterPos3d
    cglRasterPos3d = <PFNGLRASTERPOS3DPROC>getFunction(b"glRasterPos3d")
    cglRasterPos3d(x, y, z)

cdef void GetglTexCoord2iv(const GLint *v):
    global cglTexCoord2iv
    cglTexCoord2iv = <PFNGLTEXCOORD2IVPROC>getFunction(b"glTexCoord2iv")
    cglTexCoord2iv(v)

cdef void GetglAccum(GLenum op, GLfloat value):
    global cglAccum
    cglAccum = <PFNGLACCUMPROC>getFunction(b"glAccum")
    cglAccum(op, value)

cdef void GetglColor4usv(const GLushort *v):
    global cglColor4usv
    cglColor4usv = <PFNGLCOLOR4USVPROC>getFunction(b"glColor4usv")
    cglColor4usv(v)

cdef void GetglNormal3sv(const GLshort *v):
    global cglNormal3sv
    cglNormal3sv = <PFNGLNORMAL3SVPROC>getFunction(b"glNormal3sv")
    cglNormal3sv(v)

cdef void GetglTexGenfv(GLenum coord, GLenum pname, const GLfloat *params):
    global cglTexGenfv
    cglTexGenfv = <PFNGLTEXGENFVPROC>getFunction(b"glTexGenfv")
    cglTexGenfv(coord, pname, params)

cdef void GetglColor4b(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha):
    global cglColor4b
    cglColor4b = <PFNGLCOLOR4BPROC>getFunction(b"glColor4b")
    cglColor4b(red, green, blue, alpha)

cdef void GetglTexGeni(GLenum coord, GLenum pname, GLint param):
    global cglTexGeni
    cglTexGeni = <PFNGLTEXGENIPROC>getFunction(b"glTexGeni")
    cglTexGeni(coord, pname, param)

cdef void GetglClearStencil(GLint s):
    global cglClearStencil
    cglClearStencil = <PFNGLCLEARSTENCILPROC>getFunction(b"glClearStencil")
    cglClearStencil(s)

cdef void GetglVertex2d(GLdouble x, GLdouble y):
    global cglVertex2d
    cglVertex2d = <PFNGLVERTEX2DPROC>getFunction(b"glVertex2d")
    cglVertex2d(x, y)

cdef void GetglVertex4i(GLint x, GLint y, GLint z, GLint w):
    global cglVertex4i
    cglVertex4i = <PFNGLVERTEX4IPROC>getFunction(b"glVertex4i")
    cglVertex4i(x, y, z, w)

cdef void GetglEvalPoint1(GLint i):
    global cglEvalPoint1
    cglEvalPoint1 = <PFNGLEVALPOINT1PROC>getFunction(b"glEvalPoint1")
    cglEvalPoint1(i)

cdef void GetglNormal3f(GLfloat nx, GLfloat ny, GLfloat nz):
    global cglNormal3f
    cglNormal3f = <PFNGLNORMAL3FPROC>getFunction(b"glNormal3f")
    cglNormal3f(nx, ny, nz)

cdef void GetglEvalMesh1(GLenum mode, GLint i1, GLint i2):
    global cglEvalMesh1
    cglEvalMesh1 = <PFNGLEVALMESH1PROC>getFunction(b"glEvalMesh1")
    cglEvalMesh1(mode, i1, i2)

cdef void GetglTexCoord2dv(const GLdouble *v):
    global cglTexCoord2dv
    cglTexCoord2dv = <PFNGLTEXCOORD2DVPROC>getFunction(b"glTexCoord2dv")
    cglTexCoord2dv(v)

cdef void GetglHint(GLenum target, GLenum mode):
    global cglHint
    cglHint = <PFNGLHINTPROC>getFunction(b"glHint")
    cglHint(target, mode)

cdef void GetglPointSize(GLfloat size):
    global cglPointSize
    cglPointSize = <PFNGLPOINTSIZEPROC>getFunction(b"glPointSize")
    cglPointSize(size)

cdef void GetglClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    global cglClearColor
    cglClearColor = <PFNGLCLEARCOLORPROC>getFunction(b"glClearColor")
    cglClearColor(red, green, blue, alpha)

cdef void GetglTexCoord1f(GLfloat s):
    global cglTexCoord1f
    cglTexCoord1f = <PFNGLTEXCOORD1FPROC>getFunction(b"glTexCoord1f")
    cglTexCoord1f(s)

cdef void GetglFrontFace(GLenum mode):
    global cglFrontFace
    cglFrontFace = <PFNGLFRONTFACEPROC>getFunction(b"glFrontFace")
    cglFrontFace(mode)

cdef void GetglColor3fv(const GLfloat *v):
    global cglColor3fv
    cglColor3fv = <PFNGLCOLOR3FVPROC>getFunction(b"glColor3fv")
    cglColor3fv(v)

cdef void GetglEdgeFlag(GLboolean flag):
    global cglEdgeFlag
    cglEdgeFlag = <PFNGLEDGEFLAGPROC>getFunction(b"glEdgeFlag")
    cglEdgeFlag(flag)

cdef void GetglTexCoord1s(GLshort s):
    global cglTexCoord1s
    cglTexCoord1s = <PFNGLTEXCOORD1SPROC>getFunction(b"glTexCoord1s")
    cglTexCoord1s(s)

cdef void GetglTexCoord2f(GLfloat s, GLfloat t):
    global cglTexCoord2f
    cglTexCoord2f = <PFNGLTEXCOORD2FPROC>getFunction(b"glTexCoord2f")
    cglTexCoord2f(s, t)

cdef void GetglTexCoord4f(GLfloat s, GLfloat t, GLfloat r, GLfloat q):
    global cglTexCoord4f
    cglTexCoord4f = <PFNGLTEXCOORD4FPROC>getFunction(b"glTexCoord4f")
    cglTexCoord4f(s, t, r, q)

cdef void GetglFogf(GLenum pname, GLfloat param):
    global cglFogf
    cglFogf = <PFNGLFOGFPROC>getFunction(b"glFogf")
    cglFogf(pname, param)

cdef void GetglPushAttrib(GLbitfield mask):
    global cglPushAttrib
    cglPushAttrib = <PFNGLPUSHATTRIBPROC>getFunction(b"glPushAttrib")
    cglPushAttrib(mask)

cdef void GetglColor4f(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    global cglColor4f
    cglColor4f = <PFNGLCOLOR4FPROC>getFunction(b"glColor4f")
    cglColor4f(red, green, blue, alpha)

cdef void GetglBitmap(GLsizei width, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte *bitmap):
    global cglBitmap
    cglBitmap = <PFNGLBITMAPPROC>getFunction(b"glBitmap")
    cglBitmap(width, height, xorig, yorig, xmove, ymove, bitmap)

cdef void GetglColor4d(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha):
    global cglColor4d
    cglColor4d = <PFNGLCOLOR4DPROC>getFunction(b"glColor4d")
    cglColor4d(red, green, blue, alpha)

cdef void GetglTexParameteri(GLenum target, GLenum pname, GLint param):
    global cglTexParameteri
    cglTexParameteri = <PFNGLTEXPARAMETERIPROC>getFunction(b"glTexParameteri")
    cglTexParameteri(target, pname, param)

cdef void GetglEndList():
    global cglEndList
    cglEndList = <PFNGLENDLISTPROC>getFunction(b"glEndList")
    cglEndList()

cdef void GetglRasterPos2i(GLint x, GLint y):
    global cglRasterPos2i
    cglRasterPos2i = <PFNGLRASTERPOS2IPROC>getFunction(b"glRasterPos2i")
    cglRasterPos2i(x, y)

cdef void GetglRasterPos3sv(const GLshort *v):
    global cglRasterPos3sv
    cglRasterPos3sv = <PFNGLRASTERPOS3SVPROC>getFunction(b"glRasterPos3sv")
    cglRasterPos3sv(v)

cdef void GetglCullFace(GLenum mode):
    global cglCullFace
    cglCullFace = <PFNGLCULLFACEPROC>getFunction(b"glCullFace")
    cglCullFace(mode)

cdef void GetglGetClipPlane(GLenum plane, GLdouble *equation):
    global cglGetClipPlane
    cglGetClipPlane = <PFNGLGETCLIPPLANEPROC>getFunction(b"glGetClipPlane")
    cglGetClipPlane(plane, equation)

cdef void GetglRasterPos3iv(const GLint *v):
    global cglRasterPos3iv
    cglRasterPos3iv = <PFNGLRASTERPOS3IVPROC>getFunction(b"glRasterPos3iv")
    cglRasterPos3iv(v)

cdef void GetglTexCoord4sv(const GLshort *v):
    global cglTexCoord4sv
    cglTexCoord4sv = <PFNGLTEXCOORD4SVPROC>getFunction(b"glTexCoord4sv")
    cglTexCoord4sv(v)

cdef void GetglMaterialiv(GLenum face, GLenum pname, const GLint *params):
    global cglMaterialiv
    cglMaterialiv = <PFNGLMATERIALIVPROC>getFunction(b"glMaterialiv")
    cglMaterialiv(face, pname, params)

cdef void GetglViewport(GLint x, GLint y, GLsizei width, GLsizei height):
    global cglViewport
    cglViewport = <PFNGLVIEWPORTPROC>getFunction(b"glViewport")
    cglViewport(x, y, width, height)

cdef void GetglTexCoord4iv(const GLint *v):
    global cglTexCoord4iv
    cglTexCoord4iv = <PFNGLTEXCOORD4IVPROC>getFunction(b"glTexCoord4iv")
    cglTexCoord4iv(v)

cdef void GetglStencilOp(GLenum fail, GLenum zfail, GLenum zpass):
    global cglStencilOp
    cglStencilOp = <PFNGLSTENCILOPPROC>getFunction(b"glStencilOp")
    cglStencilOp(fail, zfail, zpass)

cdef void GetglColor4iv(const GLint *v):
    global cglColor4iv
    cglColor4iv = <PFNGLCOLOR4IVPROC>getFunction(b"glColor4iv")
    cglColor4iv(v)

cdef void GetglColor3us(GLushort red, GLushort green, GLushort blue):
    global cglColor3us
    cglColor3us = <PFNGLCOLOR3USPROC>getFunction(b"glColor3us")
    cglColor3us(red, green, blue)

cdef void GetglTexParameterfv(GLenum target, GLenum pname, const GLfloat *params):
    global cglTexParameterfv
    cglTexParameterfv = <PFNGLTEXPARAMETERFVPROC>getFunction(b"glTexParameterfv")
    cglTexParameterfv(target, pname, params)

cdef void GetglNormal3iv(const GLint *v):
    global cglNormal3iv
    cglNormal3iv = <PFNGLNORMAL3IVPROC>getFunction(b"glNormal3iv")
    cglNormal3iv(v)

cdef void GetglPixelZoom(GLfloat xfactor, GLfloat yfactor):
    global cglPixelZoom
    cglPixelZoom = <PFNGLPIXELZOOMPROC>getFunction(b"glPixelZoom")
    cglPixelZoom(xfactor, yfactor)

cdef void GetglNormal3bv(const GLbyte *v):
    global cglNormal3bv
    cglNormal3bv = <PFNGLNORMAL3BVPROC>getFunction(b"glNormal3bv")
    cglNormal3bv(v)

cdef void GetglPixelTransferi(GLenum pname, GLint param):
    global cglPixelTransferi
    cglPixelTransferi = <PFNGLPIXELTRANSFERIPROC>getFunction(b"glPixelTransferi")
    cglPixelTransferi(pname, param)

cdef void GetglGetTexEnviv(GLenum target, GLenum pname, GLint *params):
    global cglGetTexEnviv
    cglGetTexEnviv = <PFNGLGETTEXENVIVPROC>getFunction(b"glGetTexEnviv")
    cglGetTexEnviv(target, pname, params)

cdef void GetglDepthRange(GLdouble n, GLdouble f):
    global cglDepthRange
    cglDepthRange = <PFNGLDEPTHRANGEPROC>getFunction(b"glDepthRange")
    cglDepthRange(n, f)

cdef void GetglRecti(GLint x1, GLint y1, GLint x2, GLint y2):
    global cglRecti
    cglRecti = <PFNGLRECTIPROC>getFunction(b"glRecti")
    cglRecti(x1, y1, x2, y2)

cdef void GetglTexCoord1i(GLint s):
    global cglTexCoord1i
    cglTexCoord1i = <PFNGLTEXCOORD1IPROC>getFunction(b"glTexCoord1i")
    cglTexCoord1i(s)

cdef void GetglTexEnvfv(GLenum target, GLenum pname, const GLfloat *params):
    global cglTexEnvfv
    cglTexEnvfv = <PFNGLTEXENVFVPROC>getFunction(b"glTexEnvfv")
    cglTexEnvfv(target, pname, params)

cdef void GetglIndexdv(const GLdouble *c):
    global cglIndexdv
    cglIndexdv = <PFNGLINDEXDVPROC>getFunction(b"glIndexdv")
    cglIndexdv(c)

cdef void GetglVertex2sv(const GLshort *v):
    global cglVertex2sv
    cglVertex2sv = <PFNGLVERTEX2SVPROC>getFunction(b"glVertex2sv")
    cglVertex2sv(v)

cdef void GetglGetTexImage(GLenum target, GLint level, GLenum format, GLenum type, void *pixels):
    global cglGetTexImage
    cglGetTexImage = <PFNGLGETTEXIMAGEPROC>getFunction(b"glGetTexImage")
    cglGetTexImage(target, level, format, type, pixels)

cdef void GetglRectfv(const GLfloat *v1, const GLfloat *v2):
    global cglRectfv
    cglRectfv = <PFNGLRECTFVPROC>getFunction(b"glRectfv")
    cglRectfv(v1, v2)

cdef void GetglColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha):
    global cglColorMask
    cglColorMask = <PFNGLCOLORMASKPROC>getFunction(b"glColorMask")
    cglColorMask(red, green, blue, alpha)

cdef void GetglPopAttrib():
    global cglPopAttrib
    cglPopAttrib = <PFNGLPOPATTRIBPROC>getFunction(b"glPopAttrib")
    cglPopAttrib()

cdef void GetglGetMapfv(GLenum target, GLenum query, GLfloat *v):
    global cglGetMapfv
    cglGetMapfv = <PFNGLGETMAPFVPROC>getFunction(b"glGetMapfv")
    cglGetMapfv(target, query, v)

cdef void GetglTexCoord2s(GLshort s, GLshort t):
    global cglTexCoord2s
    cglTexCoord2s = <PFNGLTEXCOORD2SPROC>getFunction(b"glTexCoord2s")
    cglTexCoord2s(s, t)

cdef void GetglStencilMask(GLuint mask):
    global cglStencilMask
    cglStencilMask = <PFNGLSTENCILMASKPROC>getFunction(b"glStencilMask")
    cglStencilMask(mask)

cdef void GetglPolygonStipple(const GLubyte *mask):
    global cglPolygonStipple
    cglPolygonStipple = <PFNGLPOLYGONSTIPPLEPROC>getFunction(b"glPolygonStipple")
    cglPolygonStipple(mask)

cdef void GetglPushName(GLuint name):
    global cglPushName
    cglPushName = <PFNGLPUSHNAMEPROC>getFunction(b"glPushName")
    cglPushName(name)

cdef void GetglEvalCoord2d(GLdouble u, GLdouble v):
    global cglEvalCoord2d
    cglEvalCoord2d = <PFNGLEVALCOORD2DPROC>getFunction(b"glEvalCoord2d")
    cglEvalCoord2d(u, v)

cdef void GetglRasterPos2dv(const GLdouble *v):
    global cglRasterPos2dv
    cglRasterPos2dv = <PFNGLRASTERPOS2DVPROC>getFunction(b"glRasterPos2dv")
    cglRasterPos2dv(v)

cdef void GetglGetLightiv(GLenum light, GLenum pname, GLint *params):
    global cglGetLightiv
    cglGetLightiv = <PFNGLGETLIGHTIVPROC>getFunction(b"glGetLightiv")
    cglGetLightiv(light, pname, params)

cdef void GetglGetDoublev(GLenum pname, GLdouble *data):
    global cglGetDoublev
    cglGetDoublev = <PFNGLGETDOUBLEVPROC>getFunction(b"glGetDoublev")
    cglGetDoublev(pname, data)

cdef void GetglTexCoord4dv(const GLdouble *v):
    global cglTexCoord4dv
    cglTexCoord4dv = <PFNGLTEXCOORD4DVPROC>getFunction(b"glTexCoord4dv")
    cglTexCoord4dv(v)

cdef void GetglGetMapiv(GLenum target, GLenum query, GLint *v):
    global cglGetMapiv
    cglGetMapiv = <PFNGLGETMAPIVPROC>getFunction(b"glGetMapiv")
    cglGetMapiv(target, query, v)

cdef void GetglVertex2iv(const GLint *v):
    global cglVertex2iv
    cglVertex2iv = <PFNGLVERTEX2IVPROC>getFunction(b"glVertex2iv")
    cglVertex2iv(v)

cdef void GetglTexCoord4s(GLshort s, GLshort t, GLshort r, GLshort q):
    global cglTexCoord4s
    cglTexCoord4s = <PFNGLTEXCOORD4SPROC>getFunction(b"glTexCoord4s")
    cglTexCoord4s(s, t, r, q)

cdef void GetglDrawBuffer(GLenum buf):
    global cglDrawBuffer
    cglDrawBuffer = <PFNGLDRAWBUFFERPROC>getFunction(b"glDrawBuffer")
    cglDrawBuffer(buf)

cdef void GetglRectd(GLdouble x1, GLdouble y1, GLdouble x2, GLdouble y2):
    global cglRectd
    cglRectd = <PFNGLRECTDPROC>getFunction(b"glRectd")
    cglRectd(x1, y1, x2, y2)

cdef void GetglPixelMapfv(GLenum map, GLsizei mapsize, const GLfloat *values):
    global cglPixelMapfv
    cglPixelMapfv = <PFNGLPIXELMAPFVPROC>getFunction(b"glPixelMapfv")
    cglPixelMapfv(map, mapsize, values)

cdef GLboolean GetglIsList(GLuint list):
    global cglIsList
    cglIsList = <PFNGLISLISTPROC>getFunction(b"glIsList")
    cglIsList(list)

cdef void GetglRasterPos4i(GLint x, GLint y, GLint z, GLint w):
    global cglRasterPos4i
    cglRasterPos4i = <PFNGLRASTERPOS4IPROC>getFunction(b"glRasterPos4i")
    cglRasterPos4i(x, y, z, w)

cdef void GetglGetTexGendv(GLenum coord, GLenum pname, GLdouble *params):
    global cglGetTexGendv
    cglGetTexGendv = <PFNGLGETTEXGENDVPROC>getFunction(b"glGetTexGendv")
    cglGetTexGendv(coord, pname, params)

cdef void GetglMap2d(GLenum target, GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint vstride, GLint vorder, const GLdouble *points):
    global cglMap2d
    cglMap2d = <PFNGLMAP2DPROC>getFunction(b"glMap2d")
    cglMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)

cdef void GetglTexCoord4fv(const GLfloat *v):
    global cglTexCoord4fv
    cglTexCoord4fv = <PFNGLTEXCOORD4FVPROC>getFunction(b"glTexCoord4fv")
    cglTexCoord4fv(v)

cdef void GetglRasterPos2sv(const GLshort *v):
    global cglRasterPos2sv
    cglRasterPos2sv = <PFNGLRASTERPOS2SVPROC>getFunction(b"glRasterPos2sv")
    cglRasterPos2sv(v)

cdef void GetglLighti(GLenum light, GLenum pname, GLint param):
    global cglLighti
    cglLighti = <PFNGLLIGHTIPROC>getFunction(b"glLighti")
    cglLighti(light, pname, param)

cdef void GetglRasterPos4s(GLshort x, GLshort y, GLshort z, GLshort w):
    global cglRasterPos4s
    cglRasterPos4s = <PFNGLRASTERPOS4SPROC>getFunction(b"glRasterPos4s")
    cglRasterPos4s(x, y, z, w)

cdef void GetglColor3s(GLshort red, GLshort green, GLshort blue):
    global cglColor3s
    cglColor3s = <PFNGLCOLOR3SPROC>getFunction(b"glColor3s")
    cglColor3s(red, green, blue)

cdef void GetglRasterPos2d(GLdouble x, GLdouble y):
    global cglRasterPos2d
    cglRasterPos2d = <PFNGLRASTERPOS2DPROC>getFunction(b"glRasterPos2d")
    cglRasterPos2d(x, y)

cdef void GetglColor3ub(GLubyte red, GLubyte green, GLubyte blue):
    global cglColor3ub
    cglColor3ub = <PFNGLCOLOR3UBPROC>getFunction(b"glColor3ub")
    cglColor3ub(red, green, blue)

cdef void GetglRasterPos4fv(const GLfloat *v):
    global cglRasterPos4fv
    cglRasterPos4fv = <PFNGLRASTERPOS4FVPROC>getFunction(b"glRasterPos4fv")
    cglRasterPos4fv(v)

cdef void GetglIndexsv(const GLshort *c):
    global cglIndexsv
    cglIndexsv = <PFNGLINDEXSVPROC>getFunction(b"glIndexsv")
    cglIndexsv(c)

cdef void GetglRotatef(GLfloat angle, GLfloat x, GLfloat y, GLfloat z):
    global cglRotatef
    cglRotatef = <PFNGLROTATEFPROC>getFunction(b"glRotatef")
    cglRotatef(angle, x, y, z)

cdef void GetglRasterPos2f(GLfloat x, GLfloat y):
    global cglRasterPos2f
    cglRasterPos2f = <PFNGLRASTERPOS2FPROC>getFunction(b"glRasterPos2f")
    cglRasterPos2f(x, y)

cdef void GetglTranslatef(GLfloat x, GLfloat y, GLfloat z):
    global cglTranslatef
    cglTranslatef = <PFNGLTRANSLATEFPROC>getFunction(b"glTranslatef")
    cglTranslatef(x, y, z)

cdef void GetglIndexd(GLdouble c):
    global cglIndexd
    cglIndexd = <PFNGLINDEXDPROC>getFunction(b"glIndexd")
    cglIndexd(c)

cdef void GetglNormal3s(GLshort nx, GLshort ny, GLshort nz):
    global cglNormal3s
    cglNormal3s = <PFNGLNORMAL3SPROC>getFunction(b"glNormal3s")
    cglNormal3s(nx, ny, nz)

cdef void GetglGetTexGeniv(GLenum coord, GLenum pname, GLint *params):
    global cglGetTexGeniv
    cglGetTexGeniv = <PFNGLGETTEXGENIVPROC>getFunction(b"glGetTexGeniv")
    cglGetTexGeniv(coord, pname, params)

cdef void GetglGetIntegerv(GLenum pname, GLint *data):
    global cglGetIntegerv
    cglGetIntegerv = <PFNGLGETINTEGERVPROC>getFunction(b"glGetIntegerv")
    cglGetIntegerv(pname, data)

cdef void GetglLightModelfv(GLenum pname, const GLfloat *params):
    global cglLightModelfv
    cglLightModelfv = <PFNGLLIGHTMODELFVPROC>getFunction(b"glLightModelfv")
    cglLightModelfv(pname, params)

cdef void GetglVertex2i(GLint x, GLint y):
    global cglVertex2i
    cglVertex2i = <PFNGLVERTEX2IPROC>getFunction(b"glVertex2i")
    cglVertex2i(x, y)

cdef void GetglTexCoord1dv(const GLdouble *v):
    global cglTexCoord1dv
    cglTexCoord1dv = <PFNGLTEXCOORD1DVPROC>getFunction(b"glTexCoord1dv")
    cglTexCoord1dv(v)

cdef void GetglTexCoord1fv(const GLfloat *v):
    global cglTexCoord1fv
    cglTexCoord1fv = <PFNGLTEXCOORD1FVPROC>getFunction(b"glTexCoord1fv")
    cglTexCoord1fv(v)

cdef void GetglColor3i(GLint red, GLint green, GLint blue):
    global cglColor3i
    cglColor3i = <PFNGLCOLOR3IPROC>getFunction(b"glColor3i")
    cglColor3i(red, green, blue)

cdef void GetglVertex3iv(const GLint *v):
    global cglVertex3iv
    cglVertex3iv = <PFNGLVERTEX3IVPROC>getFunction(b"glVertex3iv")
    cglVertex3iv(v)

cdef void GetglMatrixMode(GLenum mode):
    global cglMatrixMode
    cglMatrixMode = <PFNGLMATRIXMODEPROC>getFunction(b"glMatrixMode")
    cglMatrixMode(mode)

cdef void GetglRectf(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2):
    global cglRectf
    cglRectf = <PFNGLRECTFPROC>getFunction(b"glRectf")
    cglRectf(x1, y1, x2, y2)

cdef void GetglMap1d(GLenum target, GLdouble u1, GLdouble u2, GLint stride, GLint order, const GLdouble *points):
    global cglMap1d
    cglMap1d = <PFNGLMAP1DPROC>getFunction(b"glMap1d")
    cglMap1d(target, u1, u2, stride, order, points)

cdef void GetglIndexf(GLfloat c):
    global cglIndexf
    cglIndexf = <PFNGLINDEXFPROC>getFunction(b"glIndexf")
    cglIndexf(c)

cdef void GetglVertex3sv(const GLshort *v):
    global cglVertex3sv
    cglVertex3sv = <PFNGLVERTEX3SVPROC>getFunction(b"glVertex3sv")
    cglVertex3sv(v)

cdef void GetglLightModelf(GLenum pname, GLfloat param):
    global cglLightModelf
    cglLightModelf = <PFNGLLIGHTMODELFPROC>getFunction(b"glLightModelf")
    cglLightModelf(pname, param)

cdef void GetglGetPixelMapfv(GLenum map, GLfloat *values):
    global cglGetPixelMapfv
    cglGetPixelMapfv = <PFNGLGETPIXELMAPFVPROC>getFunction(b"glGetPixelMapfv")
    cglGetPixelMapfv(map, values)

cdef void GetglPixelMapusv(GLenum map, GLsizei mapsize, const GLushort *values):
    global cglPixelMapusv
    cglPixelMapusv = <PFNGLPIXELMAPUSVPROC>getFunction(b"glPixelMapusv")
    cglPixelMapusv(map, mapsize, values)

cdef void GetglRasterPos4iv(const GLint *v):
    global cglRasterPos4iv
    cglRasterPos4iv = <PFNGLRASTERPOS4IVPROC>getFunction(b"glRasterPos4iv")
    cglRasterPos4iv(v)

cdef void GetglTexCoord3f(GLfloat s, GLfloat t, GLfloat r):
    global cglTexCoord3f
    cglTexCoord3f = <PFNGLTEXCOORD3FPROC>getFunction(b"glTexCoord3f")
    cglTexCoord3f(s, t, r)

cdef void GetglLoadMatrixd(const GLdouble *m):
    global cglLoadMatrixd
    cglLoadMatrixd = <PFNGLLOADMATRIXDPROC>getFunction(b"glLoadMatrixd")
    cglLoadMatrixd(m)

cdef void GetglLineWidth(GLfloat width):
    global cglLineWidth
    cglLineWidth = <PFNGLLINEWIDTHPROC>getFunction(b"glLineWidth")
    cglLineWidth(width)

cdef void GetglScissor(GLint x, GLint y, GLsizei width, GLsizei height):
    global cglScissor
    cglScissor = <PFNGLSCISSORPROC>getFunction(b"glScissor")
    cglScissor(x, y, width, height)

cdef void GetglGetTexLevelParameterfv(GLenum target, GLint level, GLenum pname, GLfloat *params):
    global cglGetTexLevelParameterfv
    cglGetTexLevelParameterfv = <PFNGLGETTEXLEVELPARAMETERFVPROC>getFunction(b"glGetTexLevelParameterfv")
    cglGetTexLevelParameterfv(target, level, pname, params)

cdef void GetglTexCoord3fv(const GLfloat *v):
    global cglTexCoord3fv
    cglTexCoord3fv = <PFNGLTEXCOORD3FVPROC>getFunction(b"glTexCoord3fv")
    cglTexCoord3fv(v)

cdef void GetglLoadIdentity():
    global cglLoadIdentity
    cglLoadIdentity = <PFNGLLOADIDENTITYPROC>getFunction(b"glLoadIdentity")
    cglLoadIdentity()

cdef void GetglRasterPos2fv(const GLfloat *v):
    global cglRasterPos2fv
    cglRasterPos2fv = <PFNGLRASTERPOS2FVPROC>getFunction(b"glRasterPos2fv")
    cglRasterPos2fv(v)

cdef void GetglTexParameterf(GLenum target, GLenum pname, GLfloat param):
    global cglTexParameterf
    cglTexParameterf = <PFNGLTEXPARAMETERFPROC>getFunction(b"glTexParameterf")
    cglTexParameterf(target, pname, param)

cdef void GetglTexCoord1iv(const GLint *v):
    global cglTexCoord1iv
    cglTexCoord1iv = <PFNGLTEXCOORD1IVPROC>getFunction(b"glTexCoord1iv")
    cglTexCoord1iv(v)

cdef void GetglInitNames():
    global cglInitNames
    cglInitNames = <PFNGLINITNAMESPROC>getFunction(b"glInitNames")
    cglInitNames()

cdef void GetglMapGrid1f(GLint un, GLfloat u1, GLfloat u2):
    global cglMapGrid1f
    cglMapGrid1f = <PFNGLMAPGRID1FPROC>getFunction(b"glMapGrid1f")
    cglMapGrid1f(un, u1, u2)

cdef void GetglTexImage2D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *pixels):
    global cglTexImage2D
    cglTexImage2D = <PFNGLTEXIMAGE2DPROC>getFunction(b"glTexImage2D")
    cglTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)

cdef void GetglGetPolygonStipple(GLubyte *mask):
    global cglGetPolygonStipple
    cglGetPolygonStipple = <PFNGLGETPOLYGONSTIPPLEPROC>getFunction(b"glGetPolygonStipple")
    cglGetPolygonStipple(mask)

cdef void GetglEvalCoord2dv(const GLdouble *u):
    global cglEvalCoord2dv
    cglEvalCoord2dv = <PFNGLEVALCOORD2DVPROC>getFunction(b"glEvalCoord2dv")
    cglEvalCoord2dv(u)

cdef void GetglEnd():
    global cglEnd
    cglEnd = <PFNGLENDPROC>getFunction(b"glEnd")
    cglEnd()

cdef void GetglMapGrid1d(GLint un, GLdouble u1, GLdouble u2):
    global cglMapGrid1d
    cglMapGrid1d = <PFNGLMAPGRID1DPROC>getFunction(b"glMapGrid1d")
    cglMapGrid1d(un, u1, u2)

cdef void GetglColorMaterial(GLenum face, GLenum mode):
    global cglColorMaterial
    cglColorMaterial = <PFNGLCOLORMATERIALPROC>getFunction(b"glColorMaterial")
    cglColorMaterial(face, mode)

cdef void GetglMultMatrixf(const GLfloat *m):
    global cglMultMatrixf
    cglMultMatrixf = <PFNGLMULTMATRIXFPROC>getFunction(b"glMultMatrixf")
    cglMultMatrixf(m)

cdef void GetglMap2f(GLenum target, GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride, GLint vorder, const GLfloat *points):
    global cglMap2f
    cglMap2f = <PFNGLMAP2FPROC>getFunction(b"glMap2f")
    cglMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)

cdef void GetglPixelTransferf(GLenum pname, GLfloat param):
    global cglPixelTransferf
    cglPixelTransferf = <PFNGLPIXELTRANSFERFPROC>getFunction(b"glPixelTransferf")
    cglPixelTransferf(pname, param)

cdef void GetglVertex3f(GLfloat x, GLfloat y, GLfloat z):
    global cglVertex3f
    cglVertex3f = <PFNGLVERTEX3FPROC>getFunction(b"glVertex3f")
    cglVertex3f(x, y, z)

cdef void GetglColor3usv(const GLushort *v):
    global cglColor3usv
    cglColor3usv = <PFNGLCOLOR3USVPROC>getFunction(b"glColor3usv")
    cglColor3usv(v)

cdef void GetglColor4fv(const GLfloat *v):
    global cglColor4fv
    cglColor4fv = <PFNGLCOLOR4FVPROC>getFunction(b"glColor4fv")
    cglColor4fv(v)

cdef void GetglPixelStorei(GLenum pname, GLint param):
    global cglPixelStorei
    cglPixelStorei = <PFNGLPIXELSTOREIPROC>getFunction(b"glPixelStorei")
    cglPixelStorei(pname, param)

cdef void GetglMaterialf(GLenum face, GLenum pname, GLfloat param):
    global cglMaterialf
    cglMaterialf = <PFNGLMATERIALFPROC>getFunction(b"glMaterialf")
    cglMaterialf(face, pname, param)

cdef void GetglTexImage1D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const void *pixels):
    global cglTexImage1D
    cglTexImage1D = <PFNGLTEXIMAGE1DPROC>getFunction(b"glTexImage1D")
    cglTexImage1D(target, level, internalformat, width, border, format, type, pixels)

cdef void GetglVertex3dv(const GLdouble *v):
    global cglVertex3dv
    cglVertex3dv = <PFNGLVERTEX3DVPROC>getFunction(b"glVertex3dv")
    cglVertex3dv(v)

cdef void GetglLineStipple(GLint factor, GLushort pattern):
    global cglLineStipple
    cglLineStipple = <PFNGLLINESTIPPLEPROC>getFunction(b"glLineStipple")
    cglLineStipple(factor, pattern)

cdef void GetglColor4s(GLshort red, GLshort green, GLshort blue, GLshort alpha):
    global cglColor4s
    cglColor4s = <PFNGLCOLOR4SPROC>getFunction(b"glColor4s")
    cglColor4s(red, green, blue, alpha)

cdef void GetglMapGrid2d(GLint un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2):
    global cglMapGrid2d
    cglMapGrid2d = <PFNGLMAPGRID2DPROC>getFunction(b"glMapGrid2d")
    cglMapGrid2d(un, u1, u2, vn, v1, v2)

cdef void GetglVertex3i(GLint x, GLint y, GLint z):
    global cglVertex3i
    cglVertex3i = <PFNGLVERTEX3IPROC>getFunction(b"glVertex3i")
    cglVertex3i(x, y, z)

cdef void GetglGetTexLevelParameteriv(GLenum target, GLint level, GLenum pname, GLint *params):
    global cglGetTexLevelParameteriv
    cglGetTexLevelParameteriv = <PFNGLGETTEXLEVELPARAMETERIVPROC>getFunction(b"glGetTexLevelParameteriv")
    cglGetTexLevelParameteriv(target, level, pname, params)

cdef void GetglGetMaterialiv(GLenum face, GLenum pname, GLint *params):
    global cglGetMaterialiv
    cglGetMaterialiv = <PFNGLGETMATERIALIVPROC>getFunction(b"glGetMaterialiv")
    cglGetMaterialiv(face, pname, params)

cdef void GetglVertex4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglVertex4d
    cglVertex4d = <PFNGLVERTEX4DPROC>getFunction(b"glVertex4d")
    cglVertex4d(x, y, z, w)

cdef void GetglVertex4sv(const GLshort *v):
    global cglVertex4sv
    cglVertex4sv = <PFNGLVERTEX4SVPROC>getFunction(b"glVertex4sv")
    cglVertex4sv(v)

cdef void GetglGetTexParameteriv(GLenum target, GLenum pname, GLint *params):
    global cglGetTexParameteriv
    cglGetTexParameteriv = <PFNGLGETTEXPARAMETERIVPROC>getFunction(b"glGetTexParameteriv")
    cglGetTexParameteriv(target, pname, params)

cdef void GetglGetFloatv(GLenum pname, GLfloat *data):
    global cglGetFloatv
    cglGetFloatv = <PFNGLGETFLOATVPROC>getFunction(b"glGetFloatv")
    cglGetFloatv(pname, data)

cdef void GetglShadeModel(GLenum mode):
    global cglShadeModel
    cglShadeModel = <PFNGLSHADEMODELPROC>getFunction(b"glShadeModel")
    cglShadeModel(mode)

cdef void GetglGetPixelMapuiv(GLenum map, GLuint *values):
    global cglGetPixelMapuiv
    cglGetPixelMapuiv = <PFNGLGETPIXELMAPUIVPROC>getFunction(b"glGetPixelMapuiv")
    cglGetPixelMapuiv(map, values)

cdef void GetglClipPlane(GLenum plane, const GLdouble *equation):
    global cglClipPlane
    cglClipPlane = <PFNGLCLIPPLANEPROC>getFunction(b"glClipPlane")
    cglClipPlane(plane, equation)

cdef void GetglGetTexEnvfv(GLenum target, GLenum pname, GLfloat *params):
    global cglGetTexEnvfv
    cglGetTexEnvfv = <PFNGLGETTEXENVFVPROC>getFunction(b"glGetTexEnvfv")
    cglGetTexEnvfv(target, pname, params)

cdef void GetglRasterPos2iv(const GLint *v):
    global cglRasterPos2iv
    cglRasterPos2iv = <PFNGLRASTERPOS2IVPROC>getFunction(b"glRasterPos2iv")
    cglRasterPos2iv(v)

cdef void GetglIndexi(GLint c):
    global cglIndexi
    cglIndexi = <PFNGLINDEXIPROC>getFunction(b"glIndexi")
    cglIndexi(c)

cdef void GetglVertex4fv(const GLfloat *v):
    global cglVertex4fv
    cglVertex4fv = <PFNGLVERTEX4FVPROC>getFunction(b"glVertex4fv")
    cglVertex4fv(v)

cdef void GetglIndexMask(GLuint mask):
    global cglIndexMask
    cglIndexMask = <PFNGLINDEXMASKPROC>getFunction(b"glIndexMask")
    cglIndexMask(mask)

cdef void GetglRasterPos3dv(const GLdouble *v):
    global cglRasterPos3dv
    cglRasterPos3dv = <PFNGLRASTERPOS3DVPROC>getFunction(b"glRasterPos3dv")
    cglRasterPos3dv(v)

cdef void GetglColor3ubv(const GLubyte *v):
    global cglColor3ubv
    cglColor3ubv = <PFNGLCOLOR3UBVPROC>getFunction(b"glColor3ubv")
    cglColor3ubv(v)

cdef GLenum GetglGetError():
    global cglGetError
    cglGetError = <PFNGLGETERRORPROC>getFunction(b"glGetError")
    cglGetError()

cdef void GetglColor3bv(const GLbyte *v):
    global cglColor3bv
    cglColor3bv = <PFNGLCOLOR3BVPROC>getFunction(b"glColor3bv")
    cglColor3bv(v)

cdef void GetglTexCoord3i(GLint s, GLint t, GLint r):
    global cglTexCoord3i
    cglTexCoord3i = <PFNGLTEXCOORD3IPROC>getFunction(b"glTexCoord3i")
    cglTexCoord3i(s, t, r)

cdef void GetglTexGenf(GLenum coord, GLenum pname, GLfloat param):
    global cglTexGenf
    cglTexGenf = <PFNGLTEXGENFPROC>getFunction(b"glTexGenf")
    cglTexGenf(coord, pname, param)

cdef const GLubyte *GetglGetString(GLenum name):
    global cglGetString
    cglGetString = <PFNGLGETSTRINGPROC>getFunction(b"glGetString")
    cglGetString(name)

cdef void GetglGetTexGenfv(GLenum coord, GLenum pname, GLfloat *params):
    global cglGetTexGenfv
    cglGetTexGenfv = <PFNGLGETTEXGENFVPROC>getFunction(b"glGetTexGenfv")
    cglGetTexGenfv(coord, pname, params)

cdef void GetglRasterPos3fv(const GLfloat *v):
    global cglRasterPos3fv
    cglRasterPos3fv = <PFNGLRASTERPOS3FVPROC>getFunction(b"glRasterPos3fv")
    cglRasterPos3fv(v)

cdef void GetglColor3d(GLdouble red, GLdouble green, GLdouble blue):
    global cglColor3d
    cglColor3d = <PFNGLCOLOR3DPROC>getFunction(b"glColor3d")
    cglColor3d(red, green, blue)

cdef void GetglScalef(GLfloat x, GLfloat y, GLfloat z):
    global cglScalef
    cglScalef = <PFNGLSCALEFPROC>getFunction(b"glScalef")
    cglScalef(x, y, z)

cdef void GetglRasterPos3s(GLshort x, GLshort y, GLshort z):
    global cglRasterPos3s
    cglRasterPos3s = <PFNGLRASTERPOS3SPROC>getFunction(b"glRasterPos3s")
    cglRasterPos3s(x, y, z)

cdef void GetglEdgeFlagv(const GLboolean *flag):
    global cglEdgeFlagv
    cglEdgeFlagv = <PFNGLEDGEFLAGVPROC>getFunction(b"glEdgeFlagv")
    cglEdgeFlagv(flag)

cdef void GetglTexCoord2sv(const GLshort *v):
    global cglTexCoord2sv
    cglTexCoord2sv = <PFNGLTEXCOORD2SVPROC>getFunction(b"glTexCoord2sv")
    cglTexCoord2sv(v)

cdef void GetglTexCoord3d(GLdouble s, GLdouble t, GLdouble r):
    global cglTexCoord3d
    cglTexCoord3d = <PFNGLTEXCOORD3DPROC>getFunction(b"glTexCoord3d")
    cglTexCoord3d(s, t, r)

cdef void GetglEvalCoord1d(GLdouble u):
    global cglEvalCoord1d
    cglEvalCoord1d = <PFNGLEVALCOORD1DPROC>getFunction(b"glEvalCoord1d")
    cglEvalCoord1d(u)

cdef void GetglColor4i(GLint red, GLint green, GLint blue, GLint alpha):
    global cglColor4i
    cglColor4i = <PFNGLCOLOR4IPROC>getFunction(b"glColor4i")
    cglColor4i(red, green, blue, alpha)

cdef void GetglColor4uiv(const GLuint *v):
    global cglColor4uiv
    cglColor4uiv = <PFNGLCOLOR4UIVPROC>getFunction(b"glColor4uiv")
    cglColor4uiv(v)

cdef void GetglAlphaFunc(GLenum func, GLfloat ref):
    global cglAlphaFunc
    cglAlphaFunc = <PFNGLALPHAFUNCPROC>getFunction(b"glAlphaFunc")
    cglAlphaFunc(func, ref)

cdef void GetglVertex2fv(const GLfloat *v):
    global cglVertex2fv
    cglVertex2fv = <PFNGLVERTEX2FVPROC>getFunction(b"glVertex2fv")
    cglVertex2fv(v)

cdef void GetglGetPixelMapusv(GLenum map, GLushort *values):
    global cglGetPixelMapusv
    cglGetPixelMapusv = <PFNGLGETPIXELMAPUSVPROC>getFunction(b"glGetPixelMapusv")
    cglGetPixelMapusv(map, values)

cdef void GetglClear(GLbitfield mask):
    global cglClear
    cglClear = <PFNGLCLEARPROC>getFunction(b"glClear")
    cglClear(mask)

cdef void GetglBlendFunc(GLenum sfactor, GLenum dfactor):
    global cglBlendFunc
    cglBlendFunc = <PFNGLBLENDFUNCPROC>getFunction(b"glBlendFunc")
    cglBlendFunc(sfactor, dfactor)

cdef void GetglRasterPos3i(GLint x, GLint y, GLint z):
    global cglRasterPos3i
    cglRasterPos3i = <PFNGLRASTERPOS3IPROC>getFunction(b"glRasterPos3i")
    cglRasterPos3i(x, y, z)

cdef void GetglVertex3s(GLshort x, GLshort y, GLshort z):
    global cglVertex3s
    cglVertex3s = <PFNGLVERTEX3SPROC>getFunction(b"glVertex3s")
    cglVertex3s(x, y, z)

cdef void GetglColor4ub(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha):
    global cglColor4ub
    cglColor4ub = <PFNGLCOLOR4UBPROC>getFunction(b"glColor4ub")
    cglColor4ub(red, green, blue, alpha)

cdef void GetglRectdv(const GLdouble *v1, const GLdouble *v2):
    global cglRectdv
    cglRectdv = <PFNGLRECTDVPROC>getFunction(b"glRectdv")
    cglRectdv(v1, v2)

cdef void GetglNormal3b(GLbyte nx, GLbyte ny, GLbyte nz):
    global cglNormal3b
    cglNormal3b = <PFNGLNORMAL3BPROC>getFunction(b"glNormal3b")
    cglNormal3b(nx, ny, nz)

cdef void GetglFogi(GLenum pname, GLint param):
    global cglFogi
    cglFogi = <PFNGLFOGIPROC>getFunction(b"glFogi")
    cglFogi(pname, param)

cdef GLint GetglRenderMode(GLenum mode):
    global cglRenderMode
    cglRenderMode = <PFNGLRENDERMODEPROC>getFunction(b"glRenderMode")
    cglRenderMode(mode)

cdef void GetglEvalCoord1f(GLfloat u):
    global cglEvalCoord1f
    cglEvalCoord1f = <PFNGLEVALCOORD1FPROC>getFunction(b"glEvalCoord1f")
    cglEvalCoord1f(u)

cdef void GetglVertex2s(GLshort x, GLshort y):
    global cglVertex2s
    cglVertex2s = <PFNGLVERTEX2SPROC>getFunction(b"glVertex2s")
    cglVertex2s(x, y)

cdef void GetglRectiv(const GLint *v1, const GLint *v2):
    global cglRectiv
    cglRectiv = <PFNGLRECTIVPROC>getFunction(b"glRectiv")
    cglRectiv(v1, v2)

cdef void GetglEvalMesh2(GLenum mode, GLint i1, GLint i2, GLint j1, GLint j2):
    global cglEvalMesh2
    cglEvalMesh2 = <PFNGLEVALMESH2PROC>getFunction(b"glEvalMesh2")
    cglEvalMesh2(mode, i1, i2, j1, j2)

cdef void GetglFogfv(GLenum pname, const GLfloat *params):
    global cglFogfv
    cglFogfv = <PFNGLFOGFVPROC>getFunction(b"glFogfv")
    cglFogfv(pname, params)

cdef void GetglTexCoord4d(GLdouble s, GLdouble t, GLdouble r, GLdouble q):
    global cglTexCoord4d
    cglTexCoord4d = <PFNGLTEXCOORD4DPROC>getFunction(b"glTexCoord4d")
    cglTexCoord4d(s, t, r, q)

cdef void GetglLightf(GLenum light, GLenum pname, GLfloat param):
    global cglLightf
    cglLightf = <PFNGLLIGHTFPROC>getFunction(b"glLightf")
    cglLightf(light, pname, param)

cdef void GetglTexGendv(GLenum coord, GLenum pname, const GLdouble *params):
    global cglTexGendv
    cglTexGendv = <PFNGLTEXGENDVPROC>getFunction(b"glTexGendv")
    cglTexGendv(coord, pname, params)

cdef void GetglBegin(GLenum mode):
    global cglBegin
    cglBegin = <PFNGLBEGINPROC>getFunction(b"glBegin")
    cglBegin(mode)

cdef void GetglFeedbackBuffer(GLsizei size, GLenum type, GLfloat *buffer):
    global cglFeedbackBuffer
    cglFeedbackBuffer = <PFNGLFEEDBACKBUFFERPROC>getFunction(b"glFeedbackBuffer")
    cglFeedbackBuffer(size, type, buffer)

cdef void GetglIndexs(GLshort c):
    global cglIndexs
    cglIndexs = <PFNGLINDEXSPROC>getFunction(b"glIndexs")
    cglIndexs(c)

cdef void GetglFogiv(GLenum pname, const GLint *params):
    global cglFogiv
    cglFogiv = <PFNGLFOGIVPROC>getFunction(b"glFogiv")
    cglFogiv(pname, params)

cdef void GetglTranslated(GLdouble x, GLdouble y, GLdouble z):
    global cglTranslated
    cglTranslated = <PFNGLTRANSLATEDPROC>getFunction(b"glTranslated")
    cglTranslated(x, y, z)

cdef void GetglTexCoord3s(GLshort s, GLshort t, GLshort r):
    global cglTexCoord3s
    cglTexCoord3s = <PFNGLTEXCOORD3SPROC>getFunction(b"glTexCoord3s")
    cglTexCoord3s(s, t, r)

cdef void GetglTexCoord2i(GLint s, GLint t):
    global cglTexCoord2i
    cglTexCoord2i = <PFNGLTEXCOORD2IPROC>getFunction(b"glTexCoord2i")
    cglTexCoord2i(s, t)

cdef void GetglMap1f(GLenum target, GLfloat u1, GLfloat u2, GLint stride, GLint order, const GLfloat *points):
    global cglMap1f
    cglMap1f = <PFNGLMAP1FPROC>getFunction(b"glMap1f")
    cglMap1f(target, u1, u2, stride, order, points)

cdef void GetglTexCoord2d(GLdouble s, GLdouble t):
    global cglTexCoord2d
    cglTexCoord2d = <PFNGLTEXCOORD2DPROC>getFunction(b"glTexCoord2d")
    cglTexCoord2d(s, t)

cdef void GetglTexCoord3dv(const GLdouble *v):
    global cglTexCoord3dv
    cglTexCoord3dv = <PFNGLTEXCOORD3DVPROC>getFunction(b"glTexCoord3dv")
    cglTexCoord3dv(v)

cglListBase = GetglListBase
cglRasterPos2s = GetglRasterPos2s
cglLightModeli = GetglLightModeli
cglIndexiv = GetglIndexiv
cglTexParameteriv = GetglTexParameteriv
cglColor4ubv = GetglColor4ubv
cglReadPixels = GetglReadPixels
cglTexCoord2fv = GetglTexCoord2fv
cglPixelStoref = GetglPixelStoref
cglLightfv = GetglLightfv
cglDrawPixels = GetglDrawPixels
cglColor3uiv = GetglColor3uiv
cglMaterialfv = GetglMaterialfv
cglFrustum = GetglFrustum
cglVertex2f = GetglVertex2f
cglStencilFunc = GetglStencilFunc
cglTexEnvf = GetglTexEnvf
cglRectsv = GetglRectsv
cglEvalCoord1fv = GetglEvalCoord1fv
cglGetTexParameterfv = GetglGetTexParameterfv
cglRects = GetglRects
cglReadBuffer = GetglReadBuffer
cglRasterPos4dv = GetglRasterPos4dv
cglDepthFunc = GetglDepthFunc
cglTexGend = GetglTexGend
cglLoadMatrixf = GetglLoadMatrixf
cglEvalCoord2f = GetglEvalCoord2f
cglDeleteLists = GetglDeleteLists
cglMultMatrixd = GetglMultMatrixd
cglPushMatrix = GetglPushMatrix
cglGetMapdv = GetglGetMapdv
cglRasterPos4f = GetglRasterPos4f
cglColor4us = GetglColor4us
cglTexGeniv = GetglTexGeniv
cglTexEnvi = GetglTexEnvi
cglTexEnviv = GetglTexEnviv
cglScaled = GetglScaled
cglIsEnabled = GetglIsEnabled
cglColor3iv = GetglColor3iv
cglNormal3d = GetglNormal3d
cglVertex4f = GetglVertex4f
cglLightModeliv = GetglLightModeliv
cglGetLightfv = GetglGetLightfv
cglRasterPos3f = GetglRasterPos3f
cglGenLists = GetglGenLists
cglEvalCoord1dv = GetglEvalCoord1dv
cglClearIndex = GetglClearIndex
cglIndexfv = GetglIndexfv
cglRasterPos4sv = GetglRasterPos4sv
cglMapGrid2f = GetglMapGrid2f
cglCopyPixels = GetglCopyPixels
cglVertex4iv = GetglVertex4iv
cglPopName = GetglPopName
cglTexCoord4i = GetglTexCoord4i
cglDisable = GetglDisable
cglCallList = GetglCallList
cglNormal3dv = GetglNormal3dv
cglPolygonMode = GetglPolygonMode
cglColor3f = GetglColor3f
cglLightiv = GetglLightiv
cglColor4sv = GetglColor4sv
cglTexCoord3sv = GetglTexCoord3sv
cglVertex2dv = GetglVertex2dv
cglRasterPos4d = GetglRasterPos4d
cglMateriali = GetglMateriali
cglPixelMapuiv = GetglPixelMapuiv
cglRotated = GetglRotated
cglNormal3fv = GetglNormal3fv
cglColor3b = GetglColor3b
cglLogicOp = GetglLogicOp
cglColor4ui = GetglColor4ui
cglTexCoord3iv = GetglTexCoord3iv
cglTexCoord1sv = GetglTexCoord1sv
cglGetMaterialfv = GetglGetMaterialfv
cglColor3ui = GetglColor3ui
cglVertex3fv = GetglVertex3fv
cglClearDepth = GetglClearDepth
cglNewList = GetglNewList
cglOrtho = GetglOrtho
cglDepthMask = GetglDepthMask
cglVertex4s = GetglVertex4s
cglVertex3d = GetglVertex3d
cglPassThrough = GetglPassThrough
cglEnable = GetglEnable
cglFlush = GetglFlush
cglLoadName = GetglLoadName
cglCallLists = GetglCallLists
cglNormal3i = GetglNormal3i
cglEvalCoord2fv = GetglEvalCoord2fv
cglPopMatrix = GetglPopMatrix
cglFinish = GetglFinish
cglSelectBuffer = GetglSelectBuffer
cglColor3dv = GetglColor3dv
cglColor4dv = GetglColor4dv
cglGetBooleanv = GetglGetBooleanv
cglColor3sv = GetglColor3sv
cglEvalPoint2 = GetglEvalPoint2
cglClearAccum = GetglClearAccum
cglColor4bv = GetglColor4bv
cglVertex4dv = GetglVertex4dv
cglTexCoord1d = GetglTexCoord1d
cglRasterPos3d = GetglRasterPos3d
cglTexCoord2iv = GetglTexCoord2iv
cglAccum = GetglAccum
cglColor4usv = GetglColor4usv
cglNormal3sv = GetglNormal3sv
cglTexGenfv = GetglTexGenfv
cglColor4b = GetglColor4b
cglTexGeni = GetglTexGeni
cglClearStencil = GetglClearStencil
cglVertex2d = GetglVertex2d
cglVertex4i = GetglVertex4i
cglEvalPoint1 = GetglEvalPoint1
cglNormal3f = GetglNormal3f
cglEvalMesh1 = GetglEvalMesh1
cglTexCoord2dv = GetglTexCoord2dv
cglHint = GetglHint
cglPointSize = GetglPointSize
cglClearColor = GetglClearColor
cglTexCoord1f = GetglTexCoord1f
cglFrontFace = GetglFrontFace
cglColor3fv = GetglColor3fv
cglEdgeFlag = GetglEdgeFlag
cglTexCoord1s = GetglTexCoord1s
cglTexCoord2f = GetglTexCoord2f
cglTexCoord4f = GetglTexCoord4f
cglFogf = GetglFogf
cglPushAttrib = GetglPushAttrib
cglColor4f = GetglColor4f
cglBitmap = GetglBitmap
cglColor4d = GetglColor4d
cglTexParameteri = GetglTexParameteri
cglEndList = GetglEndList
cglRasterPos2i = GetglRasterPos2i
cglRasterPos3sv = GetglRasterPos3sv
cglCullFace = GetglCullFace
cglGetClipPlane = GetglGetClipPlane
cglRasterPos3iv = GetglRasterPos3iv
cglTexCoord4sv = GetglTexCoord4sv
cglMaterialiv = GetglMaterialiv
cglViewport = GetglViewport
cglTexCoord4iv = GetglTexCoord4iv
cglStencilOp = GetglStencilOp
cglColor4iv = GetglColor4iv
cglColor3us = GetglColor3us
cglTexParameterfv = GetglTexParameterfv
cglNormal3iv = GetglNormal3iv
cglPixelZoom = GetglPixelZoom
cglNormal3bv = GetglNormal3bv
cglPixelTransferi = GetglPixelTransferi
cglGetTexEnviv = GetglGetTexEnviv
cglDepthRange = GetglDepthRange
cglRecti = GetglRecti
cglTexCoord1i = GetglTexCoord1i
cglTexEnvfv = GetglTexEnvfv
cglIndexdv = GetglIndexdv
cglVertex2sv = GetglVertex2sv
cglGetTexImage = GetglGetTexImage
cglRectfv = GetglRectfv
cglColorMask = GetglColorMask
cglPopAttrib = GetglPopAttrib
cglGetMapfv = GetglGetMapfv
cglTexCoord2s = GetglTexCoord2s
cglStencilMask = GetglStencilMask
cglPolygonStipple = GetglPolygonStipple
cglPushName = GetglPushName
cglEvalCoord2d = GetglEvalCoord2d
cglRasterPos2dv = GetglRasterPos2dv
cglGetLightiv = GetglGetLightiv
cglGetDoublev = GetglGetDoublev
cglTexCoord4dv = GetglTexCoord4dv
cglGetMapiv = GetglGetMapiv
cglVertex2iv = GetglVertex2iv
cglTexCoord4s = GetglTexCoord4s
cglDrawBuffer = GetglDrawBuffer
cglRectd = GetglRectd
cglPixelMapfv = GetglPixelMapfv
cglIsList = GetglIsList
cglRasterPos4i = GetglRasterPos4i
cglGetTexGendv = GetglGetTexGendv
cglMap2d = GetglMap2d
cglTexCoord4fv = GetglTexCoord4fv
cglRasterPos2sv = GetglRasterPos2sv
cglLighti = GetglLighti
cglRasterPos4s = GetglRasterPos4s
cglColor3s = GetglColor3s
cglRasterPos2d = GetglRasterPos2d
cglColor3ub = GetglColor3ub
cglRasterPos4fv = GetglRasterPos4fv
cglIndexsv = GetglIndexsv
cglRotatef = GetglRotatef
cglRasterPos2f = GetglRasterPos2f
cglTranslatef = GetglTranslatef
cglIndexd = GetglIndexd
cglNormal3s = GetglNormal3s
cglGetTexGeniv = GetglGetTexGeniv
cglGetIntegerv = GetglGetIntegerv
cglLightModelfv = GetglLightModelfv
cglVertex2i = GetglVertex2i
cglTexCoord1dv = GetglTexCoord1dv
cglTexCoord1fv = GetglTexCoord1fv
cglColor3i = GetglColor3i
cglVertex3iv = GetglVertex3iv
cglMatrixMode = GetglMatrixMode
cglRectf = GetglRectf
cglMap1d = GetglMap1d
cglIndexf = GetglIndexf
cglVertex3sv = GetglVertex3sv
cglLightModelf = GetglLightModelf
cglGetPixelMapfv = GetglGetPixelMapfv
cglPixelMapusv = GetglPixelMapusv
cglRasterPos4iv = GetglRasterPos4iv
cglTexCoord3f = GetglTexCoord3f
cglLoadMatrixd = GetglLoadMatrixd
cglLineWidth = GetglLineWidth
cglScissor = GetglScissor
cglGetTexLevelParameterfv = GetglGetTexLevelParameterfv
cglTexCoord3fv = GetglTexCoord3fv
cglLoadIdentity = GetglLoadIdentity
cglRasterPos2fv = GetglRasterPos2fv
cglTexParameterf = GetglTexParameterf
cglTexCoord1iv = GetglTexCoord1iv
cglInitNames = GetglInitNames
cglMapGrid1f = GetglMapGrid1f
cglTexImage2D = GetglTexImage2D
cglGetPolygonStipple = GetglGetPolygonStipple
cglEvalCoord2dv = GetglEvalCoord2dv
cglEnd = GetglEnd
cglMapGrid1d = GetglMapGrid1d
cglColorMaterial = GetglColorMaterial
cglMultMatrixf = GetglMultMatrixf
cglMap2f = GetglMap2f
cglPixelTransferf = GetglPixelTransferf
cglVertex3f = GetglVertex3f
cglColor3usv = GetglColor3usv
cglColor4fv = GetglColor4fv
cglPixelStorei = GetglPixelStorei
cglMaterialf = GetglMaterialf
cglTexImage1D = GetglTexImage1D
cglVertex3dv = GetglVertex3dv
cglLineStipple = GetglLineStipple
cglColor4s = GetglColor4s
cglMapGrid2d = GetglMapGrid2d
cglVertex3i = GetglVertex3i
cglGetTexLevelParameteriv = GetglGetTexLevelParameteriv
cglGetMaterialiv = GetglGetMaterialiv
cglVertex4d = GetglVertex4d
cglVertex4sv = GetglVertex4sv
cglGetTexParameteriv = GetglGetTexParameteriv
cglGetFloatv = GetglGetFloatv
cglShadeModel = GetglShadeModel
cglGetPixelMapuiv = GetglGetPixelMapuiv
cglClipPlane = GetglClipPlane
cglGetTexEnvfv = GetglGetTexEnvfv
cglRasterPos2iv = GetglRasterPos2iv
cglIndexi = GetglIndexi
cglVertex4fv = GetglVertex4fv
cglIndexMask = GetglIndexMask
cglRasterPos3dv = GetglRasterPos3dv
cglColor3ubv = GetglColor3ubv
cglGetError = GetglGetError
cglColor3bv = GetglColor3bv
cglTexCoord3i = GetglTexCoord3i
cglTexGenf = GetglTexGenf
cglGetString = GetglGetString
cglGetTexGenfv = GetglGetTexGenfv
cglRasterPos3fv = GetglRasterPos3fv
cglColor3d = GetglColor3d
cglScalef = GetglScalef
cglRasterPos3s = GetglRasterPos3s
cglEdgeFlagv = GetglEdgeFlagv
cglTexCoord2sv = GetglTexCoord2sv
cglTexCoord3d = GetglTexCoord3d
cglEvalCoord1d = GetglEvalCoord1d
cglColor4i = GetglColor4i
cglColor4uiv = GetglColor4uiv
cglAlphaFunc = GetglAlphaFunc
cglVertex2fv = GetglVertex2fv
cglGetPixelMapusv = GetglGetPixelMapusv
cglClear = GetglClear
cglBlendFunc = GetglBlendFunc
cglRasterPos3i = GetglRasterPos3i
cglVertex3s = GetglVertex3s
cglColor4ub = GetglColor4ub
cglRectdv = GetglRectdv
cglNormal3b = GetglNormal3b
cglFogi = GetglFogi
cglRenderMode = GetglRenderMode
cglEvalCoord1f = GetglEvalCoord1f
cglVertex2s = GetglVertex2s
cglRectiv = GetglRectiv
cglEvalMesh2 = GetglEvalMesh2
cglFogfv = GetglFogfv
cglTexCoord4d = GetglTexCoord4d
cglLightf = GetglLightf
cglTexGendv = GetglTexGendv
cglBegin = GetglBegin
cglFeedbackBuffer = GetglFeedbackBuffer
cglIndexs = GetglIndexs
cglFogiv = GetglFogiv
cglTranslated = GetglTranslated
cglTexCoord3s = GetglTexCoord3s
cglTexCoord2i = GetglTexCoord2i
cglMap1f = GetglMap1f
cglTexCoord2d = GetglTexCoord2d
cglTexCoord3dv = GetglTexCoord3dv


cdef void glListBase(GLuint base):
    cglListBase(base)

cdef void glRasterPos2s(GLshort x, GLshort y):
    cglRasterPos2s(x, y)

cdef void glLightModeli(GLenum pname, GLint param):
    cglLightModeli(pname, param)

cdef void glIndexiv(const GLint *c):
    cglIndexiv(c)

cdef void glTexParameteriv(GLenum target, GLenum pname, const GLint *params):
    cglTexParameteriv(target, pname, params)

cdef void glColor4ubv(const GLubyte *v):
    cglColor4ubv(v)

cdef void glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, void *pixels):
    cglReadPixels(x, y, width, height, format, type, pixels)

cdef void glTexCoord2fv(const GLfloat *v):
    cglTexCoord2fv(v)

cdef void glPixelStoref(GLenum pname, GLfloat param):
    cglPixelStoref(pname, param)

cdef void glLightfv(GLenum light, GLenum pname, const GLfloat *params):
    cglLightfv(light, pname, params)

cdef void glDrawPixels(GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    cglDrawPixels(width, height, format, type, pixels)

cdef void glColor3uiv(const GLuint *v):
    cglColor3uiv(v)

cdef void glMaterialfv(GLenum face, GLenum pname, const GLfloat *params):
    cglMaterialfv(face, pname, params)

cdef void glFrustum(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar):
    cglFrustum(left, right, bottom, top, zNear, zFar)

cdef void glVertex2f(GLfloat x, GLfloat y):
    cglVertex2f(x, y)

cdef void glStencilFunc(GLenum func, GLint ref, GLuint mask):
    cglStencilFunc(func, ref, mask)

cdef void glTexEnvf(GLenum target, GLenum pname, GLfloat param):
    cglTexEnvf(target, pname, param)

cdef void glRectsv(const GLshort *v1, const GLshort *v2):
    cglRectsv(v1, v2)

cdef void glEvalCoord1fv(const GLfloat *u):
    cglEvalCoord1fv(u)

cdef void glGetTexParameterfv(GLenum target, GLenum pname, GLfloat *params):
    cglGetTexParameterfv(target, pname, params)

cdef void glRects(GLshort x1, GLshort y1, GLshort x2, GLshort y2):
    cglRects(x1, y1, x2, y2)

cdef void glReadBuffer(GLenum src):
    cglReadBuffer(src)

cdef void glRasterPos4dv(const GLdouble *v):
    cglRasterPos4dv(v)

cdef void glDepthFunc(GLenum func):
    cglDepthFunc(func)

cdef void glTexGend(GLenum coord, GLenum pname, GLdouble param):
    cglTexGend(coord, pname, param)

cdef void glLoadMatrixf(const GLfloat *m):
    cglLoadMatrixf(m)

cdef void glEvalCoord2f(GLfloat u, GLfloat v):
    cglEvalCoord2f(u, v)

cdef void glDeleteLists(GLuint list, GLsizei range):
    cglDeleteLists(list, range)

cdef void glMultMatrixd(const GLdouble *m):
    cglMultMatrixd(m)

cdef void glPushMatrix():
    cglPushMatrix()

cdef void glGetMapdv(GLenum target, GLenum query, GLdouble *v):
    cglGetMapdv(target, query, v)

cdef void glRasterPos4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    cglRasterPos4f(x, y, z, w)

cdef void glColor4us(GLushort red, GLushort green, GLushort blue, GLushort alpha):
    cglColor4us(red, green, blue, alpha)

cdef void glTexGeniv(GLenum coord, GLenum pname, const GLint *params):
    cglTexGeniv(coord, pname, params)

cdef void glTexEnvi(GLenum target, GLenum pname, GLint param):
    cglTexEnvi(target, pname, param)

cdef void glTexEnviv(GLenum target, GLenum pname, const GLint *params):
    cglTexEnviv(target, pname, params)

cdef void glScaled(GLdouble x, GLdouble y, GLdouble z):
    cglScaled(x, y, z)

cdef GLboolean glIsEnabled(GLenum cap):
    cglIsEnabled(cap)

cdef void glColor3iv(const GLint *v):
    cglColor3iv(v)

cdef void glNormal3d(GLdouble nx, GLdouble ny, GLdouble nz):
    cglNormal3d(nx, ny, nz)

cdef void glVertex4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    cglVertex4f(x, y, z, w)

cdef void glLightModeliv(GLenum pname, const GLint *params):
    cglLightModeliv(pname, params)

cdef void glGetLightfv(GLenum light, GLenum pname, GLfloat *params):
    cglGetLightfv(light, pname, params)

cdef void glRasterPos3f(GLfloat x, GLfloat y, GLfloat z):
    cglRasterPos3f(x, y, z)

cdef GLuint glGenLists(GLsizei range):
    cglGenLists(range)

cdef void glEvalCoord1dv(const GLdouble *u):
    cglEvalCoord1dv(u)

cdef void glClearIndex(GLfloat c):
    cglClearIndex(c)

cdef void glIndexfv(const GLfloat *c):
    cglIndexfv(c)

cdef void glRasterPos4sv(const GLshort *v):
    cglRasterPos4sv(v)

cdef void glMapGrid2f(GLint un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2):
    cglMapGrid2f(un, u1, u2, vn, v1, v2)

cdef void glCopyPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum type):
    cglCopyPixels(x, y, width, height, type)

cdef void glVertex4iv(const GLint *v):
    cglVertex4iv(v)

cdef void glPopName():
    cglPopName()

cdef void glTexCoord4i(GLint s, GLint t, GLint r, GLint q):
    cglTexCoord4i(s, t, r, q)

cdef void glDisable(GLenum cap):
    cglDisable(cap)

cdef void glCallList(GLuint list):
    cglCallList(list)

cdef void glNormal3dv(const GLdouble *v):
    cglNormal3dv(v)

cdef void glPolygonMode(GLenum face, GLenum mode):
    cglPolygonMode(face, mode)

cdef void glColor3f(GLfloat red, GLfloat green, GLfloat blue):
    cglColor3f(red, green, blue)

cdef void glLightiv(GLenum light, GLenum pname, const GLint *params):
    cglLightiv(light, pname, params)

cdef void glColor4sv(const GLshort *v):
    cglColor4sv(v)

cdef void glTexCoord3sv(const GLshort *v):
    cglTexCoord3sv(v)

cdef void glVertex2dv(const GLdouble *v):
    cglVertex2dv(v)

cdef void glRasterPos4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglRasterPos4d(x, y, z, w)

cdef void glMateriali(GLenum face, GLenum pname, GLint param):
    cglMateriali(face, pname, param)

cdef void glPixelMapuiv(GLenum map, GLsizei mapsize, const GLuint *values):
    cglPixelMapuiv(map, mapsize, values)

cdef void glRotated(GLdouble angle, GLdouble x, GLdouble y, GLdouble z):
    cglRotated(angle, x, y, z)

cdef void glNormal3fv(const GLfloat *v):
    cglNormal3fv(v)

cdef void glColor3b(GLbyte red, GLbyte green, GLbyte blue):
    cglColor3b(red, green, blue)

cdef void glLogicOp(GLenum opcode):
    cglLogicOp(opcode)

cdef void glColor4ui(GLuint red, GLuint green, GLuint blue, GLuint alpha):
    cglColor4ui(red, green, blue, alpha)

cdef void glTexCoord3iv(const GLint *v):
    cglTexCoord3iv(v)

cdef void glTexCoord1sv(const GLshort *v):
    cglTexCoord1sv(v)

cdef void glGetMaterialfv(GLenum face, GLenum pname, GLfloat *params):
    cglGetMaterialfv(face, pname, params)

cdef void glColor3ui(GLuint red, GLuint green, GLuint blue):
    cglColor3ui(red, green, blue)

cdef void glVertex3fv(const GLfloat *v):
    cglVertex3fv(v)

cdef void glClearDepth(GLdouble depth):
    cglClearDepth(depth)

cdef void glNewList(GLuint list, GLenum mode):
    cglNewList(list, mode)

cdef void glOrtho(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar):
    cglOrtho(left, right, bottom, top, zNear, zFar)

cdef void glDepthMask(GLboolean flag):
    cglDepthMask(flag)

cdef void glVertex4s(GLshort x, GLshort y, GLshort z, GLshort w):
    cglVertex4s(x, y, z, w)

cdef void glVertex3d(GLdouble x, GLdouble y, GLdouble z):
    cglVertex3d(x, y, z)

cdef void glPassThrough(GLfloat token):
    cglPassThrough(token)

cdef void glEnable(GLenum cap):
    cglEnable(cap)

cdef void glFlush():
    cglFlush()

cdef void glLoadName(GLuint name):
    cglLoadName(name)

cdef void glCallLists(GLsizei n, GLenum type, const void *lists):
    cglCallLists(n, type, lists)

cdef void glNormal3i(GLint nx, GLint ny, GLint nz):
    cglNormal3i(nx, ny, nz)

cdef void glEvalCoord2fv(const GLfloat *u):
    cglEvalCoord2fv(u)

cdef void glPopMatrix():
    cglPopMatrix()

cdef void glFinish():
    cglFinish()

cdef void glSelectBuffer(GLsizei size, GLuint *buffer):
    cglSelectBuffer(size, buffer)

cdef void glColor3dv(const GLdouble *v):
    cglColor3dv(v)

cdef void glColor4dv(const GLdouble *v):
    cglColor4dv(v)

cdef void glGetBooleanv(GLenum pname, GLboolean *data):
    cglGetBooleanv(pname, data)

cdef void glColor3sv(const GLshort *v):
    cglColor3sv(v)

cdef void glEvalPoint2(GLint i, GLint j):
    cglEvalPoint2(i, j)

cdef void glClearAccum(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    cglClearAccum(red, green, blue, alpha)

cdef void glColor4bv(const GLbyte *v):
    cglColor4bv(v)

cdef void glVertex4dv(const GLdouble *v):
    cglVertex4dv(v)

cdef void glTexCoord1d(GLdouble s):
    cglTexCoord1d(s)

cdef void glRasterPos3d(GLdouble x, GLdouble y, GLdouble z):
    cglRasterPos3d(x, y, z)

cdef void glTexCoord2iv(const GLint *v):
    cglTexCoord2iv(v)

cdef void glAccum(GLenum op, GLfloat value):
    cglAccum(op, value)

cdef void glColor4usv(const GLushort *v):
    cglColor4usv(v)

cdef void glNormal3sv(const GLshort *v):
    cglNormal3sv(v)

cdef void glTexGenfv(GLenum coord, GLenum pname, const GLfloat *params):
    cglTexGenfv(coord, pname, params)

cdef void glColor4b(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha):
    cglColor4b(red, green, blue, alpha)

cdef void glTexGeni(GLenum coord, GLenum pname, GLint param):
    cglTexGeni(coord, pname, param)

cdef void glClearStencil(GLint s):
    cglClearStencil(s)

cdef void glVertex2d(GLdouble x, GLdouble y):
    cglVertex2d(x, y)

cdef void glVertex4i(GLint x, GLint y, GLint z, GLint w):
    cglVertex4i(x, y, z, w)

cdef void glEvalPoint1(GLint i):
    cglEvalPoint1(i)

cdef void glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz):
    cglNormal3f(nx, ny, nz)

cdef void glEvalMesh1(GLenum mode, GLint i1, GLint i2):
    cglEvalMesh1(mode, i1, i2)

cdef void glTexCoord2dv(const GLdouble *v):
    cglTexCoord2dv(v)

cdef void glHint(GLenum target, GLenum mode):
    cglHint(target, mode)

cdef void glPointSize(GLfloat size):
    cglPointSize(size)

cdef void glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    cglClearColor(red, green, blue, alpha)

cdef void glTexCoord1f(GLfloat s):
    cglTexCoord1f(s)

cdef void glFrontFace(GLenum mode):
    cglFrontFace(mode)

cdef void glColor3fv(const GLfloat *v):
    cglColor3fv(v)

cdef void glEdgeFlag(GLboolean flag):
    cglEdgeFlag(flag)

cdef void glTexCoord1s(GLshort s):
    cglTexCoord1s(s)

cdef void glTexCoord2f(GLfloat s, GLfloat t):
    cglTexCoord2f(s, t)

cdef void glTexCoord4f(GLfloat s, GLfloat t, GLfloat r, GLfloat q):
    cglTexCoord4f(s, t, r, q)

cdef void glFogf(GLenum pname, GLfloat param):
    cglFogf(pname, param)

cdef void glPushAttrib(GLbitfield mask):
    cglPushAttrib(mask)

cdef void glColor4f(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    cglColor4f(red, green, blue, alpha)

cdef void glBitmap(GLsizei width, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte *bitmap):
    cglBitmap(width, height, xorig, yorig, xmove, ymove, bitmap)

cdef void glColor4d(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha):
    cglColor4d(red, green, blue, alpha)

cdef void glTexParameteri(GLenum target, GLenum pname, GLint param):
    cglTexParameteri(target, pname, param)

cdef void glEndList():
    cglEndList()

cdef void glRasterPos2i(GLint x, GLint y):
    cglRasterPos2i(x, y)

cdef void glRasterPos3sv(const GLshort *v):
    cglRasterPos3sv(v)

cdef void glCullFace(GLenum mode):
    cglCullFace(mode)

cdef void glGetClipPlane(GLenum plane, GLdouble *equation):
    cglGetClipPlane(plane, equation)

cdef void glRasterPos3iv(const GLint *v):
    cglRasterPos3iv(v)

cdef void glTexCoord4sv(const GLshort *v):
    cglTexCoord4sv(v)

cdef void glMaterialiv(GLenum face, GLenum pname, const GLint *params):
    cglMaterialiv(face, pname, params)

cdef void glViewport(GLint x, GLint y, GLsizei width, GLsizei height):
    cglViewport(x, y, width, height)

cdef void glTexCoord4iv(const GLint *v):
    cglTexCoord4iv(v)

cdef void glStencilOp(GLenum fail, GLenum zfail, GLenum zpass):
    cglStencilOp(fail, zfail, zpass)

cdef void glColor4iv(const GLint *v):
    cglColor4iv(v)

cdef void glColor3us(GLushort red, GLushort green, GLushort blue):
    cglColor3us(red, green, blue)

cdef void glTexParameterfv(GLenum target, GLenum pname, const GLfloat *params):
    cglTexParameterfv(target, pname, params)

cdef void glNormal3iv(const GLint *v):
    cglNormal3iv(v)

cdef void glPixelZoom(GLfloat xfactor, GLfloat yfactor):
    cglPixelZoom(xfactor, yfactor)

cdef void glNormal3bv(const GLbyte *v):
    cglNormal3bv(v)

cdef void glPixelTransferi(GLenum pname, GLint param):
    cglPixelTransferi(pname, param)

cdef void glGetTexEnviv(GLenum target, GLenum pname, GLint *params):
    cglGetTexEnviv(target, pname, params)

cdef void glDepthRange(GLdouble n, GLdouble f):
    cglDepthRange(n, f)

cdef void glRecti(GLint x1, GLint y1, GLint x2, GLint y2):
    cglRecti(x1, y1, x2, y2)

cdef void glTexCoord1i(GLint s):
    cglTexCoord1i(s)

cdef void glTexEnvfv(GLenum target, GLenum pname, const GLfloat *params):
    cglTexEnvfv(target, pname, params)

cdef void glIndexdv(const GLdouble *c):
    cglIndexdv(c)

cdef void glVertex2sv(const GLshort *v):
    cglVertex2sv(v)

cdef void glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type, void *pixels):
    cglGetTexImage(target, level, format, type, pixels)

cdef void glRectfv(const GLfloat *v1, const GLfloat *v2):
    cglRectfv(v1, v2)

cdef void glColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha):
    cglColorMask(red, green, blue, alpha)

cdef void glPopAttrib():
    cglPopAttrib()

cdef void glGetMapfv(GLenum target, GLenum query, GLfloat *v):
    cglGetMapfv(target, query, v)

cdef void glTexCoord2s(GLshort s, GLshort t):
    cglTexCoord2s(s, t)

cdef void glStencilMask(GLuint mask):
    cglStencilMask(mask)

cdef void glPolygonStipple(const GLubyte *mask):
    cglPolygonStipple(mask)

cdef void glPushName(GLuint name):
    cglPushName(name)

cdef void glEvalCoord2d(GLdouble u, GLdouble v):
    cglEvalCoord2d(u, v)

cdef void glRasterPos2dv(const GLdouble *v):
    cglRasterPos2dv(v)

cdef void glGetLightiv(GLenum light, GLenum pname, GLint *params):
    cglGetLightiv(light, pname, params)

cdef void glGetDoublev(GLenum pname, GLdouble *data):
    cglGetDoublev(pname, data)

cdef void glTexCoord4dv(const GLdouble *v):
    cglTexCoord4dv(v)

cdef void glGetMapiv(GLenum target, GLenum query, GLint *v):
    cglGetMapiv(target, query, v)

cdef void glVertex2iv(const GLint *v):
    cglVertex2iv(v)

cdef void glTexCoord4s(GLshort s, GLshort t, GLshort r, GLshort q):
    cglTexCoord4s(s, t, r, q)

cdef void glDrawBuffer(GLenum buf):
    cglDrawBuffer(buf)

cdef void glRectd(GLdouble x1, GLdouble y1, GLdouble x2, GLdouble y2):
    cglRectd(x1, y1, x2, y2)

cdef void glPixelMapfv(GLenum map, GLsizei mapsize, const GLfloat *values):
    cglPixelMapfv(map, mapsize, values)

cdef GLboolean glIsList(GLuint list):
    cglIsList(list)

cdef void glRasterPos4i(GLint x, GLint y, GLint z, GLint w):
    cglRasterPos4i(x, y, z, w)

cdef void glGetTexGendv(GLenum coord, GLenum pname, GLdouble *params):
    cglGetTexGendv(coord, pname, params)

cdef void glMap2d(GLenum target, GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint vstride, GLint vorder, const GLdouble *points):
    cglMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)

cdef void glTexCoord4fv(const GLfloat *v):
    cglTexCoord4fv(v)

cdef void glRasterPos2sv(const GLshort *v):
    cglRasterPos2sv(v)

cdef void glLighti(GLenum light, GLenum pname, GLint param):
    cglLighti(light, pname, param)

cdef void glRasterPos4s(GLshort x, GLshort y, GLshort z, GLshort w):
    cglRasterPos4s(x, y, z, w)

cdef void glColor3s(GLshort red, GLshort green, GLshort blue):
    cglColor3s(red, green, blue)

cdef void glRasterPos2d(GLdouble x, GLdouble y):
    cglRasterPos2d(x, y)

cdef void glColor3ub(GLubyte red, GLubyte green, GLubyte blue):
    cglColor3ub(red, green, blue)

cdef void glRasterPos4fv(const GLfloat *v):
    cglRasterPos4fv(v)

cdef void glIndexsv(const GLshort *c):
    cglIndexsv(c)

cdef void glRotatef(GLfloat angle, GLfloat x, GLfloat y, GLfloat z):
    cglRotatef(angle, x, y, z)

cdef void glRasterPos2f(GLfloat x, GLfloat y):
    cglRasterPos2f(x, y)

cdef void glTranslatef(GLfloat x, GLfloat y, GLfloat z):
    cglTranslatef(x, y, z)

cdef void glIndexd(GLdouble c):
    cglIndexd(c)

cdef void glNormal3s(GLshort nx, GLshort ny, GLshort nz):
    cglNormal3s(nx, ny, nz)

cdef void glGetTexGeniv(GLenum coord, GLenum pname, GLint *params):
    cglGetTexGeniv(coord, pname, params)

cdef void glGetIntegerv(GLenum pname, GLint *data):
    cglGetIntegerv(pname, data)

cdef void glLightModelfv(GLenum pname, const GLfloat *params):
    cglLightModelfv(pname, params)

cdef void glVertex2i(GLint x, GLint y):
    cglVertex2i(x, y)

cdef void glTexCoord1dv(const GLdouble *v):
    cglTexCoord1dv(v)

cdef void glTexCoord1fv(const GLfloat *v):
    cglTexCoord1fv(v)

cdef void glColor3i(GLint red, GLint green, GLint blue):
    cglColor3i(red, green, blue)

cdef void glVertex3iv(const GLint *v):
    cglVertex3iv(v)

cdef void glMatrixMode(GLenum mode):
    cglMatrixMode(mode)

cdef void glRectf(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2):
    cglRectf(x1, y1, x2, y2)

cdef void glMap1d(GLenum target, GLdouble u1, GLdouble u2, GLint stride, GLint order, const GLdouble *points):
    cglMap1d(target, u1, u2, stride, order, points)

cdef void glIndexf(GLfloat c):
    cglIndexf(c)

cdef void glVertex3sv(const GLshort *v):
    cglVertex3sv(v)

cdef void glLightModelf(GLenum pname, GLfloat param):
    cglLightModelf(pname, param)

cdef void glGetPixelMapfv(GLenum map, GLfloat *values):
    cglGetPixelMapfv(map, values)

cdef void glPixelMapusv(GLenum map, GLsizei mapsize, const GLushort *values):
    cglPixelMapusv(map, mapsize, values)

cdef void glRasterPos4iv(const GLint *v):
    cglRasterPos4iv(v)

cdef void glTexCoord3f(GLfloat s, GLfloat t, GLfloat r):
    cglTexCoord3f(s, t, r)

cdef void glLoadMatrixd(const GLdouble *m):
    cglLoadMatrixd(m)

cdef void glLineWidth(GLfloat width):
    cglLineWidth(width)

cdef void glScissor(GLint x, GLint y, GLsizei width, GLsizei height):
    cglScissor(x, y, width, height)

cdef void glGetTexLevelParameterfv(GLenum target, GLint level, GLenum pname, GLfloat *params):
    cglGetTexLevelParameterfv(target, level, pname, params)

cdef void glTexCoord3fv(const GLfloat *v):
    cglTexCoord3fv(v)

cdef void glLoadIdentity():
    cglLoadIdentity()

cdef void glRasterPos2fv(const GLfloat *v):
    cglRasterPos2fv(v)

cdef void glTexParameterf(GLenum target, GLenum pname, GLfloat param):
    cglTexParameterf(target, pname, param)

cdef void glTexCoord1iv(const GLint *v):
    cglTexCoord1iv(v)

cdef void glInitNames():
    cglInitNames()

cdef void glMapGrid1f(GLint un, GLfloat u1, GLfloat u2):
    cglMapGrid1f(un, u1, u2)

cdef void glTexImage2D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *pixels):
    cglTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)

cdef void glGetPolygonStipple(GLubyte *mask):
    cglGetPolygonStipple(mask)

cdef void glEvalCoord2dv(const GLdouble *u):
    cglEvalCoord2dv(u)

cdef void glEnd():
    cglEnd()

cdef void glMapGrid1d(GLint un, GLdouble u1, GLdouble u2):
    cglMapGrid1d(un, u1, u2)

cdef void glColorMaterial(GLenum face, GLenum mode):
    cglColorMaterial(face, mode)

cdef void glMultMatrixf(const GLfloat *m):
    cglMultMatrixf(m)

cdef void glMap2f(GLenum target, GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride, GLint vorder, const GLfloat *points):
    cglMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)

cdef void glPixelTransferf(GLenum pname, GLfloat param):
    cglPixelTransferf(pname, param)

cdef void glVertex3f(GLfloat x, GLfloat y, GLfloat z):
    cglVertex3f(x, y, z)

cdef void glColor3usv(const GLushort *v):
    cglColor3usv(v)

cdef void glColor4fv(const GLfloat *v):
    cglColor4fv(v)

cdef void glPixelStorei(GLenum pname, GLint param):
    cglPixelStorei(pname, param)

cdef void glMaterialf(GLenum face, GLenum pname, GLfloat param):
    cglMaterialf(face, pname, param)

cdef void glTexImage1D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const void *pixels):
    cglTexImage1D(target, level, internalformat, width, border, format, type, pixels)

cdef void glVertex3dv(const GLdouble *v):
    cglVertex3dv(v)

cdef void glLineStipple(GLint factor, GLushort pattern):
    cglLineStipple(factor, pattern)

cdef void glColor4s(GLshort red, GLshort green, GLshort blue, GLshort alpha):
    cglColor4s(red, green, blue, alpha)

cdef void glMapGrid2d(GLint un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2):
    cglMapGrid2d(un, u1, u2, vn, v1, v2)

cdef void glVertex3i(GLint x, GLint y, GLint z):
    cglVertex3i(x, y, z)

cdef void glGetTexLevelParameteriv(GLenum target, GLint level, GLenum pname, GLint *params):
    cglGetTexLevelParameteriv(target, level, pname, params)

cdef void glGetMaterialiv(GLenum face, GLenum pname, GLint *params):
    cglGetMaterialiv(face, pname, params)

cdef void glVertex4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglVertex4d(x, y, z, w)

cdef void glVertex4sv(const GLshort *v):
    cglVertex4sv(v)

cdef void glGetTexParameteriv(GLenum target, GLenum pname, GLint *params):
    cglGetTexParameteriv(target, pname, params)

cdef void glGetFloatv(GLenum pname, GLfloat *data):
    cglGetFloatv(pname, data)

cdef void glShadeModel(GLenum mode):
    cglShadeModel(mode)

cdef void glGetPixelMapuiv(GLenum map, GLuint *values):
    cglGetPixelMapuiv(map, values)

cdef void glClipPlane(GLenum plane, const GLdouble *equation):
    cglClipPlane(plane, equation)

cdef void glGetTexEnvfv(GLenum target, GLenum pname, GLfloat *params):
    cglGetTexEnvfv(target, pname, params)

cdef void glRasterPos2iv(const GLint *v):
    cglRasterPos2iv(v)

cdef void glIndexi(GLint c):
    cglIndexi(c)

cdef void glVertex4fv(const GLfloat *v):
    cglVertex4fv(v)

cdef void glIndexMask(GLuint mask):
    cglIndexMask(mask)

cdef void glRasterPos3dv(const GLdouble *v):
    cglRasterPos3dv(v)

cdef void glColor3ubv(const GLubyte *v):
    cglColor3ubv(v)

cdef GLenum glGetError():
    cglGetError()

cdef void glColor3bv(const GLbyte *v):
    cglColor3bv(v)

cdef void glTexCoord3i(GLint s, GLint t, GLint r):
    cglTexCoord3i(s, t, r)

cdef void glTexGenf(GLenum coord, GLenum pname, GLfloat param):
    cglTexGenf(coord, pname, param)

cdef const GLubyte *glGetString(GLenum name):
    cglGetString(name)

cdef void glGetTexGenfv(GLenum coord, GLenum pname, GLfloat *params):
    cglGetTexGenfv(coord, pname, params)

cdef void glRasterPos3fv(const GLfloat *v):
    cglRasterPos3fv(v)

cdef void glColor3d(GLdouble red, GLdouble green, GLdouble blue):
    cglColor3d(red, green, blue)

cdef void glScalef(GLfloat x, GLfloat y, GLfloat z):
    cglScalef(x, y, z)

cdef void glRasterPos3s(GLshort x, GLshort y, GLshort z):
    cglRasterPos3s(x, y, z)

cdef void glEdgeFlagv(const GLboolean *flag):
    cglEdgeFlagv(flag)

cdef void glTexCoord2sv(const GLshort *v):
    cglTexCoord2sv(v)

cdef void glTexCoord3d(GLdouble s, GLdouble t, GLdouble r):
    cglTexCoord3d(s, t, r)

cdef void glEvalCoord1d(GLdouble u):
    cglEvalCoord1d(u)

cdef void glColor4i(GLint red, GLint green, GLint blue, GLint alpha):
    cglColor4i(red, green, blue, alpha)

cdef void glColor4uiv(const GLuint *v):
    cglColor4uiv(v)

cdef void glAlphaFunc(GLenum func, GLfloat ref):
    cglAlphaFunc(func, ref)

cdef void glVertex2fv(const GLfloat *v):
    cglVertex2fv(v)

cdef void glGetPixelMapusv(GLenum map, GLushort *values):
    cglGetPixelMapusv(map, values)

cdef void glClear(GLbitfield mask):
    cglClear(mask)

cdef void glBlendFunc(GLenum sfactor, GLenum dfactor):
    cglBlendFunc(sfactor, dfactor)

cdef void glRasterPos3i(GLint x, GLint y, GLint z):
    cglRasterPos3i(x, y, z)

cdef void glVertex3s(GLshort x, GLshort y, GLshort z):
    cglVertex3s(x, y, z)

cdef void glColor4ub(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha):
    cglColor4ub(red, green, blue, alpha)

cdef void glRectdv(const GLdouble *v1, const GLdouble *v2):
    cglRectdv(v1, v2)

cdef void glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz):
    cglNormal3b(nx, ny, nz)

cdef void glFogi(GLenum pname, GLint param):
    cglFogi(pname, param)

cdef GLint glRenderMode(GLenum mode):
    cglRenderMode(mode)

cdef void glEvalCoord1f(GLfloat u):
    cglEvalCoord1f(u)

cdef void glVertex2s(GLshort x, GLshort y):
    cglVertex2s(x, y)

cdef void glRectiv(const GLint *v1, const GLint *v2):
    cglRectiv(v1, v2)

cdef void glEvalMesh2(GLenum mode, GLint i1, GLint i2, GLint j1, GLint j2):
    cglEvalMesh2(mode, i1, i2, j1, j2)

cdef void glFogfv(GLenum pname, const GLfloat *params):
    cglFogfv(pname, params)

cdef void glTexCoord4d(GLdouble s, GLdouble t, GLdouble r, GLdouble q):
    cglTexCoord4d(s, t, r, q)

cdef void glLightf(GLenum light, GLenum pname, GLfloat param):
    cglLightf(light, pname, param)

cdef void glTexGendv(GLenum coord, GLenum pname, const GLdouble *params):
    cglTexGendv(coord, pname, params)

cdef void glBegin(GLenum mode):
    cglBegin(mode)

cdef void glFeedbackBuffer(GLsizei size, GLenum type, GLfloat *buffer):
    cglFeedbackBuffer(size, type, buffer)

cdef void glIndexs(GLshort c):
    cglIndexs(c)

cdef void glFogiv(GLenum pname, const GLint *params):
    cglFogiv(pname, params)

cdef void glTranslated(GLdouble x, GLdouble y, GLdouble z):
    cglTranslated(x, y, z)

cdef void glTexCoord3s(GLshort s, GLshort t, GLshort r):
    cglTexCoord3s(s, t, r)

cdef void glTexCoord2i(GLint s, GLint t):
    cglTexCoord2i(s, t)

cdef void glMap1f(GLenum target, GLfloat u1, GLfloat u2, GLint stride, GLint order, const GLfloat *points):
    cglMap1f(target, u1, u2, stride, order, points)

cdef void glTexCoord2d(GLdouble s, GLdouble t):
    cglTexCoord2d(s, t)

cdef void glTexCoord3dv(const GLdouble *v):
    cglTexCoord3dv(v)
