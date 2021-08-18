# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_DEPTH_BUFFER_BIT = 0x00000100
cdef GLenum GL_STENCIL_BUFFER_BIT = 0x00000400
cdef GLenum GL_COLOR_BUFFER_BIT = 0x00004000
cdef GLenum GL_FALSE = 0
cdef GLenum GL_TRUE = 1
cdef GLenum GL_POINTS = 0x0000
cdef GLenum GL_LINES = 0x0001
cdef GLenum GL_LINE_LOOP = 0x0002
cdef GLenum GL_LINE_STRIP = 0x0003
cdef GLenum GL_TRIANGLES = 0x0004
cdef GLenum GL_TRIANGLE_STRIP = 0x0005
cdef GLenum GL_TRIANGLE_FAN = 0x0006
cdef GLenum GL_QUADS = 0x0007
cdef GLenum GL_NEVER = 0x0200
cdef GLenum GL_LESS = 0x0201
cdef GLenum GL_EQUAL = 0x0202
cdef GLenum GL_LEQUAL = 0x0203
cdef GLenum GL_GREATER = 0x0204
cdef GLenum GL_NOTEQUAL = 0x0205
cdef GLenum GL_GEQUAL = 0x0206
cdef GLenum GL_ALWAYS = 0x0207
cdef GLenum GL_ZERO = 0
cdef GLenum GL_ONE = 1
cdef GLenum GL_SRC_COLOR = 0x0300
cdef GLenum GL_ONE_MINUS_SRC_COLOR = 0x0301
cdef GLenum GL_SRC_ALPHA = 0x0302
cdef GLenum GL_ONE_MINUS_SRC_ALPHA = 0x0303
cdef GLenum GL_DST_ALPHA = 0x0304
cdef GLenum GL_ONE_MINUS_DST_ALPHA = 0x0305
cdef GLenum GL_DST_COLOR = 0x0306
cdef GLenum GL_ONE_MINUS_DST_COLOR = 0x0307
cdef GLenum GL_SRC_ALPHA_SATURATE = 0x0308
cdef GLenum GL_NONE = 0
cdef GLenum GL_FRONT_LEFT = 0x0400
cdef GLenum GL_FRONT_RIGHT = 0x0401
cdef GLenum GL_BACK_LEFT = 0x0402
cdef GLenum GL_BACK_RIGHT = 0x0403
cdef GLenum GL_FRONT = 0x0404
cdef GLenum GL_BACK = 0x0405
cdef GLenum GL_LEFT = 0x0406
cdef GLenum GL_RIGHT = 0x0407
cdef GLenum GL_FRONT_AND_BACK = 0x0408
cdef GLenum GL_NO_ERROR = 0
cdef GLenum GL_INVALID_ENUM = 0x0500
cdef GLenum GL_INVALID_VALUE = 0x0501
cdef GLenum GL_INVALID_OPERATION = 0x0502
cdef GLenum GL_OUT_OF_MEMORY = 0x0505
cdef GLenum GL_CW = 0x0900
cdef GLenum GL_CCW = 0x0901
cdef GLenum GL_POINT_SIZE = 0x0B11
cdef GLenum GL_POINT_SIZE_RANGE = 0x0B12
cdef GLenum GL_POINT_SIZE_GRANULARITY = 0x0B13
cdef GLenum GL_LINE_SMOOTH = 0x0B20
cdef GLenum GL_LINE_WIDTH = 0x0B21
cdef GLenum GL_LINE_WIDTH_RANGE = 0x0B22
cdef GLenum GL_LINE_WIDTH_GRANULARITY = 0x0B23
cdef GLenum GL_POLYGON_MODE = 0x0B40
cdef GLenum GL_POLYGON_SMOOTH = 0x0B41
cdef GLenum GL_CULL_FACE = 0x0B44
cdef GLenum GL_CULL_FACE_MODE = 0x0B45
cdef GLenum GL_FRONT_FACE = 0x0B46
cdef GLenum GL_DEPTH_RANGE = 0x0B70
cdef GLenum GL_DEPTH_TEST = 0x0B71
cdef GLenum GL_DEPTH_WRITEMASK = 0x0B72
cdef GLenum GL_DEPTH_CLEAR_VALUE = 0x0B73
cdef GLenum GL_DEPTH_FUNC = 0x0B74
cdef GLenum GL_STENCIL_TEST = 0x0B90
cdef GLenum GL_STENCIL_CLEAR_VALUE = 0x0B91
cdef GLenum GL_STENCIL_FUNC = 0x0B92
cdef GLenum GL_STENCIL_VALUE_MASK = 0x0B93
cdef GLenum GL_STENCIL_FAIL = 0x0B94
cdef GLenum GL_STENCIL_PASS_DEPTH_FAIL = 0x0B95
cdef GLenum GL_STENCIL_PASS_DEPTH_PASS = 0x0B96
cdef GLenum GL_STENCIL_REF = 0x0B97
cdef GLenum GL_STENCIL_WRITEMASK = 0x0B98
cdef GLenum GL_VIEWPORT = 0x0BA2
cdef GLenum GL_DITHER = 0x0BD0
cdef GLenum GL_BLEND_DST = 0x0BE0
cdef GLenum GL_BLEND_SRC = 0x0BE1
cdef GLenum GL_BLEND = 0x0BE2
cdef GLenum GL_LOGIC_OP_MODE = 0x0BF0
cdef GLenum GL_DRAW_BUFFER = 0x0C01
cdef GLenum GL_READ_BUFFER = 0x0C02
cdef GLenum GL_SCISSOR_BOX = 0x0C10
cdef GLenum GL_SCISSOR_TEST = 0x0C11
cdef GLenum GL_COLOR_CLEAR_VALUE = 0x0C22
cdef GLenum GL_COLOR_WRITEMASK = 0x0C23
cdef GLenum GL_DOUBLEBUFFER = 0x0C32
cdef GLenum GL_STEREO = 0x0C33
cdef GLenum GL_LINE_SMOOTH_HINT = 0x0C52
cdef GLenum GL_POLYGON_SMOOTH_HINT = 0x0C53
cdef GLenum GL_UNPACK_SWAP_BYTES = 0x0CF0
cdef GLenum GL_UNPACK_LSB_FIRST = 0x0CF1
cdef GLenum GL_UNPACK_ROW_LENGTH = 0x0CF2
cdef GLenum GL_UNPACK_SKIP_ROWS = 0x0CF3
cdef GLenum GL_UNPACK_SKIP_PIXELS = 0x0CF4
cdef GLenum GL_UNPACK_ALIGNMENT = 0x0CF5
cdef GLenum GL_PACK_SWAP_BYTES = 0x0D00
cdef GLenum GL_PACK_LSB_FIRST = 0x0D01
cdef GLenum GL_PACK_ROW_LENGTH = 0x0D02
cdef GLenum GL_PACK_SKIP_ROWS = 0x0D03
cdef GLenum GL_PACK_SKIP_PIXELS = 0x0D04
cdef GLenum GL_PACK_ALIGNMENT = 0x0D05
cdef GLenum GL_MAX_TEXTURE_SIZE = 0x0D33
cdef GLenum GL_MAX_VIEWPORT_DIMS = 0x0D3A
cdef GLenum GL_SUBPIXEL_BITS = 0x0D50
cdef GLenum GL_TEXTURE_1D = 0x0DE0
cdef GLenum GL_TEXTURE_2D = 0x0DE1
cdef GLenum GL_TEXTURE_WIDTH = 0x1000
cdef GLenum GL_TEXTURE_HEIGHT = 0x1001
cdef GLenum GL_TEXTURE_BORDER_COLOR = 0x1004
cdef GLenum GL_DONT_CARE = 0x1100
cdef GLenum GL_FASTEST = 0x1101
cdef GLenum GL_NICEST = 0x1102
cdef GLenum GL_BYTE = 0x1400
cdef GLenum GL_UNSIGNED_BYTE = 0x1401
cdef GLenum GL_SHORT = 0x1402
cdef GLenum GL_UNSIGNED_SHORT = 0x1403
cdef GLenum GL_INT = 0x1404
cdef GLenum GL_UNSIGNED_INT = 0x1405
cdef GLenum GL_FLOAT = 0x1406
cdef GLenum GL_STACK_OVERFLOW = 0x0503
cdef GLenum GL_STACK_UNDERFLOW = 0x0504
cdef GLenum GL_CLEAR = 0x1500
cdef GLenum GL_AND = 0x1501
cdef GLenum GL_AND_REVERSE = 0x1502
cdef GLenum GL_COPY = 0x1503
cdef GLenum GL_AND_INVERTED = 0x1504
cdef GLenum GL_NOOP = 0x1505
cdef GLenum GL_XOR = 0x1506
cdef GLenum GL_OR = 0x1507
cdef GLenum GL_NOR = 0x1508
cdef GLenum GL_EQUIV = 0x1509
cdef GLenum GL_INVERT = 0x150A
cdef GLenum GL_OR_REVERSE = 0x150B
cdef GLenum GL_COPY_INVERTED = 0x150C
cdef GLenum GL_OR_INVERTED = 0x150D
cdef GLenum GL_NAND = 0x150E
cdef GLenum GL_SET = 0x150F
cdef GLenum GL_TEXTURE = 0x1702
cdef GLenum GL_COLOR = 0x1800
cdef GLenum GL_DEPTH = 0x1801
cdef GLenum GL_STENCIL = 0x1802
cdef GLenum GL_STENCIL_INDEX = 0x1901
cdef GLenum GL_DEPTH_COMPONENT = 0x1902
cdef GLenum GL_RED = 0x1903
cdef GLenum GL_GREEN = 0x1904
cdef GLenum GL_BLUE = 0x1905
cdef GLenum GL_ALPHA = 0x1906
cdef GLenum GL_RGB = 0x1907
cdef GLenum GL_RGBA = 0x1908
cdef GLenum GL_POINT = 0x1B00
cdef GLenum GL_LINE = 0x1B01
cdef GLenum GL_FILL = 0x1B02
cdef GLenum GL_KEEP = 0x1E00
cdef GLenum GL_REPLACE = 0x1E01
cdef GLenum GL_INCR = 0x1E02
cdef GLenum GL_DECR = 0x1E03
cdef GLenum GL_VENDOR = 0x1F00
cdef GLenum GL_RENDERER = 0x1F01
cdef GLenum GL_VERSION = 0x1F02
cdef GLenum GL_EXTENSIONS = 0x1F03
cdef GLenum GL_NEAREST = 0x2600
cdef GLenum GL_LINEAR = 0x2601
cdef GLenum GL_NEAREST_MIPMAP_NEAREST = 0x2700
cdef GLenum GL_LINEAR_MIPMAP_NEAREST = 0x2701
cdef GLenum GL_NEAREST_MIPMAP_LINEAR = 0x2702
cdef GLenum GL_LINEAR_MIPMAP_LINEAR = 0x2703
cdef GLenum GL_TEXTURE_MAG_FILTER = 0x2800
cdef GLenum GL_TEXTURE_MIN_FILTER = 0x2801
cdef GLenum GL_TEXTURE_WRAP_S = 0x2802
cdef GLenum GL_TEXTURE_WRAP_T = 0x2803
cdef GLenum GL_REPEAT = 0x2901
cdef GLenum GL_CURRENT_BIT = 0x00000001
cdef GLenum GL_POINT_BIT = 0x00000002
cdef GLenum GL_LINE_BIT = 0x00000004
cdef GLenum GL_POLYGON_BIT = 0x00000008
cdef GLenum GL_POLYGON_STIPPLE_BIT = 0x00000010
cdef GLenum GL_PIXEL_MODE_BIT = 0x00000020
cdef GLenum GL_LIGHTING_BIT = 0x00000040
cdef GLenum GL_FOG_BIT = 0x00000080
cdef GLenum GL_ACCUM_BUFFER_BIT = 0x00000200
cdef GLenum GL_VIEWPORT_BIT = 0x00000800
cdef GLenum GL_TRANSFORM_BIT = 0x00001000
cdef GLenum GL_ENABLE_BIT = 0x00002000
cdef GLenum GL_HINT_BIT = 0x00008000
cdef GLenum GL_EVAL_BIT = 0x00010000
cdef GLenum GL_LIST_BIT = 0x00020000
cdef GLenum GL_TEXTURE_BIT = 0x00040000
cdef GLenum GL_SCISSOR_BIT = 0x00080000
cdef GLenum GL_ALL_ATTRIB_BITS = 0xFFFFFFFF
cdef GLenum GL_QUAD_STRIP = 0x0008
cdef GLenum GL_POLYGON = 0x0009
cdef GLenum GL_ACCUM = 0x0100
cdef GLenum GL_LOAD = 0x0101
cdef GLenum GL_RETURN = 0x0102
cdef GLenum GL_MULT = 0x0103
cdef GLenum GL_ADD = 0x0104
cdef GLenum GL_AUX0 = 0x0409
cdef GLenum GL_AUX1 = 0x040A
cdef GLenum GL_AUX2 = 0x040B
cdef GLenum GL_AUX3 = 0x040C
cdef GLenum GL_2D = 0x0600
cdef GLenum GL_3D = 0x0601
cdef GLenum GL_3D_COLOR = 0x0602
cdef GLenum GL_3D_COLOR_TEXTURE = 0x0603
cdef GLenum GL_4D_COLOR_TEXTURE = 0x0604
cdef GLenum GL_PASS_THROUGH_TOKEN = 0x0700
cdef GLenum GL_POINT_TOKEN = 0x0701
cdef GLenum GL_LINE_TOKEN = 0x0702
cdef GLenum GL_POLYGON_TOKEN = 0x0703
cdef GLenum GL_BITMAP_TOKEN = 0x0704
cdef GLenum GL_DRAW_PIXEL_TOKEN = 0x0705
cdef GLenum GL_COPY_PIXEL_TOKEN = 0x0706
cdef GLenum GL_LINE_RESET_TOKEN = 0x0707
cdef GLenum GL_EXP = 0x0800
cdef GLenum GL_EXP2 = 0x0801
cdef GLenum GL_COEFF = 0x0A00
cdef GLenum GL_ORDER = 0x0A01
cdef GLenum GL_DOMAIN = 0x0A02
cdef GLenum GL_PIXEL_MAP_I_TO_I = 0x0C70
cdef GLenum GL_PIXEL_MAP_S_TO_S = 0x0C71
cdef GLenum GL_PIXEL_MAP_I_TO_R = 0x0C72
cdef GLenum GL_PIXEL_MAP_I_TO_G = 0x0C73
cdef GLenum GL_PIXEL_MAP_I_TO_B = 0x0C74
cdef GLenum GL_PIXEL_MAP_I_TO_A = 0x0C75
cdef GLenum GL_PIXEL_MAP_R_TO_R = 0x0C76
cdef GLenum GL_PIXEL_MAP_G_TO_G = 0x0C77
cdef GLenum GL_PIXEL_MAP_B_TO_B = 0x0C78
cdef GLenum GL_PIXEL_MAP_A_TO_A = 0x0C79
cdef GLenum GL_CURRENT_COLOR = 0x0B00
cdef GLenum GL_CURRENT_INDEX = 0x0B01
cdef GLenum GL_CURRENT_NORMAL = 0x0B02
cdef GLenum GL_CURRENT_TEXTURE_COORDS = 0x0B03
cdef GLenum GL_CURRENT_RASTER_COLOR = 0x0B04
cdef GLenum GL_CURRENT_RASTER_INDEX = 0x0B05
cdef GLenum GL_CURRENT_RASTER_TEXTURE_COORDS = 0x0B06
cdef GLenum GL_CURRENT_RASTER_POSITION = 0x0B07
cdef GLenum GL_CURRENT_RASTER_POSITION_VALID = 0x0B08
cdef GLenum GL_CURRENT_RASTER_DISTANCE = 0x0B09
cdef GLenum GL_POINT_SMOOTH = 0x0B10
cdef GLenum GL_LINE_STIPPLE = 0x0B24
cdef GLenum GL_LINE_STIPPLE_PATTERN = 0x0B25
cdef GLenum GL_LINE_STIPPLE_REPEAT = 0x0B26
cdef GLenum GL_LIST_MODE = 0x0B30
cdef GLenum GL_MAX_LIST_NESTING = 0x0B31
cdef GLenum GL_LIST_BASE = 0x0B32
cdef GLenum GL_LIST_INDEX = 0x0B33
cdef GLenum GL_POLYGON_STIPPLE = 0x0B42
cdef GLenum GL_EDGE_FLAG = 0x0B43
cdef GLenum GL_LIGHTING = 0x0B50
cdef GLenum GL_LIGHT_MODEL_LOCAL_VIEWER = 0x0B51
cdef GLenum GL_LIGHT_MODEL_TWO_SIDE = 0x0B52
cdef GLenum GL_LIGHT_MODEL_AMBIENT = 0x0B53
cdef GLenum GL_SHADE_MODEL = 0x0B54
cdef GLenum GL_COLOR_MATERIAL_FACE = 0x0B55
cdef GLenum GL_COLOR_MATERIAL_PARAMETER = 0x0B56
cdef GLenum GL_COLOR_MATERIAL = 0x0B57
cdef GLenum GL_FOG = 0x0B60
cdef GLenum GL_FOG_INDEX = 0x0B61
cdef GLenum GL_FOG_DENSITY = 0x0B62
cdef GLenum GL_FOG_START = 0x0B63
cdef GLenum GL_FOG_END = 0x0B64
cdef GLenum GL_FOG_MODE = 0x0B65
cdef GLenum GL_FOG_COLOR = 0x0B66
cdef GLenum GL_ACCUM_CLEAR_VALUE = 0x0B80
cdef GLenum GL_MATRIX_MODE = 0x0BA0
cdef GLenum GL_NORMALIZE = 0x0BA1
cdef GLenum GL_MODELVIEW_STACK_DEPTH = 0x0BA3
cdef GLenum GL_PROJECTION_STACK_DEPTH = 0x0BA4
cdef GLenum GL_TEXTURE_STACK_DEPTH = 0x0BA5
cdef GLenum GL_MODELVIEW_MATRIX = 0x0BA6
cdef GLenum GL_PROJECTION_MATRIX = 0x0BA7
cdef GLenum GL_TEXTURE_MATRIX = 0x0BA8
cdef GLenum GL_ATTRIB_STACK_DEPTH = 0x0BB0
cdef GLenum GL_ALPHA_TEST = 0x0BC0
cdef GLenum GL_ALPHA_TEST_FUNC = 0x0BC1
cdef GLenum GL_ALPHA_TEST_REF = 0x0BC2
cdef GLenum GL_LOGIC_OP = 0x0BF1
cdef GLenum GL_AUX_BUFFERS = 0x0C00
cdef GLenum GL_INDEX_CLEAR_VALUE = 0x0C20
cdef GLenum GL_INDEX_WRITEMASK = 0x0C21
cdef GLenum GL_INDEX_MODE = 0x0C30
cdef GLenum GL_RGBA_MODE = 0x0C31
cdef GLenum GL_RENDER_MODE = 0x0C40
cdef GLenum GL_PERSPECTIVE_CORRECTION_HINT = 0x0C50
cdef GLenum GL_POINT_SMOOTH_HINT = 0x0C51
cdef GLenum GL_FOG_HINT = 0x0C54
cdef GLenum GL_TEXTURE_GEN_S = 0x0C60
cdef GLenum GL_TEXTURE_GEN_T = 0x0C61
cdef GLenum GL_TEXTURE_GEN_R = 0x0C62
cdef GLenum GL_TEXTURE_GEN_Q = 0x0C63
cdef GLenum GL_PIXEL_MAP_I_TO_I_SIZE = 0x0CB0
cdef GLenum GL_PIXEL_MAP_S_TO_S_SIZE = 0x0CB1
cdef GLenum GL_PIXEL_MAP_I_TO_R_SIZE = 0x0CB2
cdef GLenum GL_PIXEL_MAP_I_TO_G_SIZE = 0x0CB3
cdef GLenum GL_PIXEL_MAP_I_TO_B_SIZE = 0x0CB4
cdef GLenum GL_PIXEL_MAP_I_TO_A_SIZE = 0x0CB5
cdef GLenum GL_PIXEL_MAP_R_TO_R_SIZE = 0x0CB6
cdef GLenum GL_PIXEL_MAP_G_TO_G_SIZE = 0x0CB7
cdef GLenum GL_PIXEL_MAP_B_TO_B_SIZE = 0x0CB8
cdef GLenum GL_PIXEL_MAP_A_TO_A_SIZE = 0x0CB9
cdef GLenum GL_MAP_COLOR = 0x0D10
cdef GLenum GL_MAP_STENCIL = 0x0D11
cdef GLenum GL_INDEX_SHIFT = 0x0D12
cdef GLenum GL_INDEX_OFFSET = 0x0D13
cdef GLenum GL_RED_SCALE = 0x0D14
cdef GLenum GL_RED_BIAS = 0x0D15
cdef GLenum GL_ZOOM_X = 0x0D16
cdef GLenum GL_ZOOM_Y = 0x0D17
cdef GLenum GL_GREEN_SCALE = 0x0D18
cdef GLenum GL_GREEN_BIAS = 0x0D19
cdef GLenum GL_BLUE_SCALE = 0x0D1A
cdef GLenum GL_BLUE_BIAS = 0x0D1B
cdef GLenum GL_ALPHA_SCALE = 0x0D1C
cdef GLenum GL_ALPHA_BIAS = 0x0D1D
cdef GLenum GL_DEPTH_SCALE = 0x0D1E
cdef GLenum GL_DEPTH_BIAS = 0x0D1F
cdef GLenum GL_MAX_EVAL_ORDER = 0x0D30
cdef GLenum GL_MAX_LIGHTS = 0x0D31
cdef GLenum GL_MAX_CLIP_PLANES = 0x0D32
cdef GLenum GL_MAX_PIXEL_MAP_TABLE = 0x0D34
cdef GLenum GL_MAX_ATTRIB_STACK_DEPTH = 0x0D35
cdef GLenum GL_MAX_MODELVIEW_STACK_DEPTH = 0x0D36
cdef GLenum GL_MAX_NAME_STACK_DEPTH = 0x0D37
cdef GLenum GL_MAX_PROJECTION_STACK_DEPTH = 0x0D38
cdef GLenum GL_MAX_TEXTURE_STACK_DEPTH = 0x0D39
cdef GLenum GL_INDEX_BITS = 0x0D51
cdef GLenum GL_RED_BITS = 0x0D52
cdef GLenum GL_GREEN_BITS = 0x0D53
cdef GLenum GL_BLUE_BITS = 0x0D54
cdef GLenum GL_ALPHA_BITS = 0x0D55
cdef GLenum GL_DEPTH_BITS = 0x0D56
cdef GLenum GL_STENCIL_BITS = 0x0D57
cdef GLenum GL_ACCUM_RED_BITS = 0x0D58
cdef GLenum GL_ACCUM_GREEN_BITS = 0x0D59
cdef GLenum GL_ACCUM_BLUE_BITS = 0x0D5A
cdef GLenum GL_ACCUM_ALPHA_BITS = 0x0D5B
cdef GLenum GL_NAME_STACK_DEPTH = 0x0D70
cdef GLenum GL_AUTO_NORMAL = 0x0D80
cdef GLenum GL_MAP1_COLOR_4 = 0x0D90
cdef GLenum GL_MAP1_INDEX = 0x0D91
cdef GLenum GL_MAP1_NORMAL = 0x0D92
cdef GLenum GL_MAP1_TEXTURE_COORD_1 = 0x0D93
cdef GLenum GL_MAP1_TEXTURE_COORD_2 = 0x0D94
cdef GLenum GL_MAP1_TEXTURE_COORD_3 = 0x0D95
cdef GLenum GL_MAP1_TEXTURE_COORD_4 = 0x0D96
cdef GLenum GL_MAP1_VERTEX_3 = 0x0D97
cdef GLenum GL_MAP1_VERTEX_4 = 0x0D98
cdef GLenum GL_MAP2_COLOR_4 = 0x0DB0
cdef GLenum GL_MAP2_INDEX = 0x0DB1
cdef GLenum GL_MAP2_NORMAL = 0x0DB2
cdef GLenum GL_MAP2_TEXTURE_COORD_1 = 0x0DB3
cdef GLenum GL_MAP2_TEXTURE_COORD_2 = 0x0DB4
cdef GLenum GL_MAP2_TEXTURE_COORD_3 = 0x0DB5
cdef GLenum GL_MAP2_TEXTURE_COORD_4 = 0x0DB6
cdef GLenum GL_MAP2_VERTEX_3 = 0x0DB7
cdef GLenum GL_MAP2_VERTEX_4 = 0x0DB8
cdef GLenum GL_MAP1_GRID_DOMAIN = 0x0DD0
cdef GLenum GL_MAP1_GRID_SEGMENTS = 0x0DD1
cdef GLenum GL_MAP2_GRID_DOMAIN = 0x0DD2
cdef GLenum GL_MAP2_GRID_SEGMENTS = 0x0DD3
cdef GLenum GL_TEXTURE_COMPONENTS = 0x1003
cdef GLenum GL_TEXTURE_BORDER = 0x1005
cdef GLenum GL_AMBIENT = 0x1200
cdef GLenum GL_DIFFUSE = 0x1201
cdef GLenum GL_SPECULAR = 0x1202
cdef GLenum GL_POSITION = 0x1203
cdef GLenum GL_SPOT_DIRECTION = 0x1204
cdef GLenum GL_SPOT_EXPONENT = 0x1205
cdef GLenum GL_SPOT_CUTOFF = 0x1206
cdef GLenum GL_CONSTANT_ATTENUATION = 0x1207
cdef GLenum GL_LINEAR_ATTENUATION = 0x1208
cdef GLenum GL_QUADRATIC_ATTENUATION = 0x1209
cdef GLenum GL_COMPILE = 0x1300
cdef GLenum GL_COMPILE_AND_EXECUTE = 0x1301
cdef GLenum GL_2_BYTES = 0x1407
cdef GLenum GL_3_BYTES = 0x1408
cdef GLenum GL_4_BYTES = 0x1409
cdef GLenum GL_EMISSION = 0x1600
cdef GLenum GL_SHININESS = 0x1601
cdef GLenum GL_AMBIENT_AND_DIFFUSE = 0x1602
cdef GLenum GL_COLOR_INDEXES = 0x1603
cdef GLenum GL_MODELVIEW = 0x1700
cdef GLenum GL_PROJECTION = 0x1701
cdef GLenum GL_COLOR_INDEX = 0x1900
cdef GLenum GL_LUMINANCE = 0x1909
cdef GLenum GL_LUMINANCE_ALPHA = 0x190A
cdef GLenum GL_BITMAP = 0x1A00
cdef GLenum GL_RENDER = 0x1C00
cdef GLenum GL_FEEDBACK = 0x1C01
cdef GLenum GL_SELECT = 0x1C02
cdef GLenum GL_FLAT = 0x1D00
cdef GLenum GL_SMOOTH = 0x1D01
cdef GLenum GL_S = 0x2000
cdef GLenum GL_T = 0x2001
cdef GLenum GL_R = 0x2002
cdef GLenum GL_Q = 0x2003
cdef GLenum GL_MODULATE = 0x2100
cdef GLenum GL_DECAL = 0x2101
cdef GLenum GL_TEXTURE_ENV_MODE = 0x2200
cdef GLenum GL_TEXTURE_ENV_COLOR = 0x2201
cdef GLenum GL_TEXTURE_ENV = 0x2300
cdef GLenum GL_EYE_LINEAR = 0x2400
cdef GLenum GL_OBJECT_LINEAR = 0x2401
cdef GLenum GL_SPHERE_MAP = 0x2402
cdef GLenum GL_TEXTURE_GEN_MODE = 0x2500
cdef GLenum GL_OBJECT_PLANE = 0x2501
cdef GLenum GL_EYE_PLANE = 0x2502
cdef GLenum GL_CLAMP = 0x2900
cdef GLenum GL_CLIP_PLANE0 = 0x3000
cdef GLenum GL_CLIP_PLANE1 = 0x3001
cdef GLenum GL_CLIP_PLANE2 = 0x3002
cdef GLenum GL_CLIP_PLANE3 = 0x3003
cdef GLenum GL_CLIP_PLANE4 = 0x3004
cdef GLenum GL_CLIP_PLANE5 = 0x3005
cdef GLenum GL_LIGHT0 = 0x4000
cdef GLenum GL_LIGHT1 = 0x4001
cdef GLenum GL_LIGHT2 = 0x4002
cdef GLenum GL_LIGHT3 = 0x4003
cdef GLenum GL_LIGHT4 = 0x4004
cdef GLenum GL_LIGHT5 = 0x4005
cdef GLenum GL_LIGHT6 = 0x4006
cdef GLenum GL_LIGHT7 = 0x4007

ctypedef void (*GL_CULL_FACE)(GLenum mode)
ctypedef void (*GL_FRONT_FACE)(GLenum mode)
ctypedef void (*GL_HINT)(GLenum target, GLenum mode)
ctypedef void (*GL_LINE_WIDTH)(GLfloat width)
ctypedef void (*GL_POINT_SIZE)(GLfloat size)
ctypedef void (*GL_POLYGON_MODE)(GLenum face, GLenum mode)
ctypedef void (*GL_SCISSOR)(GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*GL_TEX_PARAMETERF)(GLenum target, GLenum pname, GLfloat param)
ctypedef void (*GL_TEX_PARAMETERFV)(GLenum target, GLenum pname, const GLfloat *params)
ctypedef void (*GL_TEX_PARAMETERI)(GLenum target, GLenum pname, GLint param)
ctypedef void (*GL_TEX_PARAMETERIV)(GLenum target, GLenum pname, const GLint *params)
ctypedef void (*GL_TEX_IMAGE1D)(GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const void *pixels)
ctypedef void (*GL_TEX_IMAGE2D)(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *pixels)
ctypedef void (*GL_DRAW_BUFFER)(GLenum buf)
ctypedef void (*GL_CLEAR)(GLbitfield mask)
ctypedef void (*GL_CLEAR_COLOR)(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
ctypedef void (*GL_CLEAR_STENCIL)(GLint s)
ctypedef void (*GL_CLEAR_DEPTH)(GLdouble depth)
ctypedef void (*GL_STENCIL_MASK)(GLuint mask)
ctypedef void (*GL_COLOR_MASK)(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha)
ctypedef void (*GL_DEPTH_MASK)(GLboolean flag)
ctypedef void (*GL_DISABLE)(GLenum cap)
ctypedef void (*GL_ENABLE)(GLenum cap)
ctypedef void (*GL_FINISH)()
ctypedef void (*GL_FLUSH)()
ctypedef void (*GL_BLEND_FUNC)(GLenum sfactor, GLenum dfactor)
ctypedef void (*GL_LOGIC_OP)(GLenum opcode)
ctypedef void (*GL_STENCIL_FUNC)(GLenum func, GLint ref, GLuint mask)
ctypedef void (*GL_STENCIL_OP)(GLenum fail, GLenum zfail, GLenum zpass)
ctypedef void (*GL_DEPTH_FUNC)(GLenum func)
ctypedef void (*GL_PIXEL_STOREF)(GLenum pname, GLfloat param)
ctypedef void (*GL_PIXEL_STOREI)(GLenum pname, GLint param)
ctypedef void (*GL_READ_BUFFER)(GLenum src)
ctypedef void (*GL_READ_PIXELS)(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, void *pixels)
ctypedef void (*GL_GET_BOOLEANV)(GLenum pname, GLboolean *data)
ctypedef void (*GL_GET_DOUBLEV)(GLenum pname, GLdouble *data)
ctypedef GLenum (*GL_GET_ERROR)()
ctypedef void (*GL_GET_FLOATV)(GLenum pname, GLfloat *data)
ctypedef void (*GL_GET_INTEGERV)(GLenum pname, GLint *data)
ctypedef const GLubyte *(*GL_GET_STRING)(GLenum name)
ctypedef void (*GL_GET_TEX_IMAGE)(GLenum target, GLint level, GLenum format, GLenum type, void *pixels)
ctypedef void (*GL_GET_TEX_PARAMETERFV)(GLenum target, GLenum pname, GLfloat *params)
ctypedef void (*GL_GET_TEX_PARAMETERIV)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*GL_GET_TEX_LEVEL_PARAMETERFV)(GLenum target, GLint level, GLenum pname, GLfloat *params)
ctypedef void (*GL_GET_TEX_LEVEL_PARAMETERIV)(GLenum target, GLint level, GLenum pname, GLint *params)
ctypedef GLboolean (*GL_IS_ENABLED)(GLenum cap)
ctypedef void (*GL_DEPTH_RANGE)(GLdouble n, GLdouble f)
ctypedef void (*GL_VIEWPORT)(GLint x, GLint y, GLsizei width, GLsizei height)
ctypedef void (*GL_NEW_LIST)(GLuint list, GLenum mode)
ctypedef void (*GL_END_LIST)()
ctypedef void (*GL_CALL_LIST)(GLuint list)
ctypedef void (*GL_CALL_LISTS)(GLsizei n, GLenum type, const void *lists)
ctypedef void (*GL_DELETE_LISTS)(GLuint list, GLsizei range)
ctypedef GLuint (*GL_GEN_LISTS)(GLsizei range)
ctypedef void (*GL_LIST_BASE)(GLuint base)
ctypedef void (*GL_BEGIN)(GLenum mode)
ctypedef void (*GL_BITMAP)(GLsizei width, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte *bitmap)
ctypedef void (*GL_COLOR3B)(GLbyte red, GLbyte green, GLbyte blue)
ctypedef void (*GL_COLOR3BV)(const GLbyte *v)
ctypedef void (*GL_COLOR3D)(GLdouble red, GLdouble green, GLdouble blue)
ctypedef void (*GL_COLOR3DV)(const GLdouble *v)
ctypedef void (*GL_COLOR3F)(GLfloat red, GLfloat green, GLfloat blue)
ctypedef void (*GL_COLOR3FV)(const GLfloat *v)
ctypedef void (*GL_COLOR3I)(GLint red, GLint green, GLint blue)
ctypedef void (*GL_COLOR3IV)(const GLint *v)
ctypedef void (*GL_COLOR3S)(GLshort red, GLshort green, GLshort blue)
ctypedef void (*GL_COLOR3SV)(const GLshort *v)
ctypedef void (*GL_COLOR3UB)(GLubyte red, GLubyte green, GLubyte blue)
ctypedef void (*GL_COLOR3UBV)(const GLubyte *v)
ctypedef void (*GL_COLOR3UI)(GLuint red, GLuint green, GLuint blue)
ctypedef void (*GL_COLOR3UIV)(const GLuint *v)
ctypedef void (*GL_COLOR3US)(GLushort red, GLushort green, GLushort blue)
ctypedef void (*GL_COLOR3USV)(const GLushort *v)
ctypedef void (*GL_COLOR4B)(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha)
ctypedef void (*GL_COLOR4BV)(const GLbyte *v)
ctypedef void (*GL_COLOR4D)(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha)
ctypedef void (*GL_COLOR4DV)(const GLdouble *v)
ctypedef void (*GL_COLOR4F)(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
ctypedef void (*GL_COLOR4FV)(const GLfloat *v)
ctypedef void (*GL_COLOR4I)(GLint red, GLint green, GLint blue, GLint alpha)
ctypedef void (*GL_COLOR4IV)(const GLint *v)
ctypedef void (*GL_COLOR4S)(GLshort red, GLshort green, GLshort blue, GLshort alpha)
ctypedef void (*GL_COLOR4SV)(const GLshort *v)
ctypedef void (*GL_COLOR4UB)(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha)
ctypedef void (*GL_COLOR4UBV)(const GLubyte *v)
ctypedef void (*GL_COLOR4UI)(GLuint red, GLuint green, GLuint blue, GLuint alpha)
ctypedef void (*GL_COLOR4UIV)(const GLuint *v)
ctypedef void (*GL_COLOR4US)(GLushort red, GLushort green, GLushort blue, GLushort alpha)
ctypedef void (*GL_COLOR4USV)(const GLushort *v)
ctypedef void (*GL_EDGE_FLAG)(GLboolean flag)
ctypedef void (*GL_EDGE_FLAGV)(const GLboolean *flag)
ctypedef void (*GL_END)()
ctypedef void (*GL_INDEXD)(GLdouble c)
ctypedef void (*GL_INDEXDV)(const GLdouble *c)
ctypedef void (*GL_INDEXF)(GLfloat c)
ctypedef void (*GL_INDEXFV)(const GLfloat *c)
ctypedef void (*GL_INDEXI)(GLint c)
ctypedef void (*GL_INDEXIV)(const GLint *c)
ctypedef void (*GL_INDEXS)(GLshort c)
ctypedef void (*GL_INDEXSV)(const GLshort *c)
ctypedef void (*GL_NORMAL3B)(GLbyte nx, GLbyte ny, GLbyte nz)
ctypedef void (*GL_NORMAL3BV)(const GLbyte *v)
ctypedef void (*GL_NORMAL3D)(GLdouble nx, GLdouble ny, GLdouble nz)
ctypedef void (*GL_NORMAL3DV)(const GLdouble *v)
ctypedef void (*GL_NORMAL3F)(GLfloat nx, GLfloat ny, GLfloat nz)
ctypedef void (*GL_NORMAL3FV)(const GLfloat *v)
ctypedef void (*GL_NORMAL3I)(GLint nx, GLint ny, GLint nz)
ctypedef void (*GL_NORMAL3IV)(const GLint *v)
ctypedef void (*GL_NORMAL3S)(GLshort nx, GLshort ny, GLshort nz)
ctypedef void (*GL_NORMAL3SV)(const GLshort *v)
ctypedef void (*GL_RASTER_POS2D)(GLdouble x, GLdouble y)
ctypedef void (*GL_RASTER_POS2DV)(const GLdouble *v)
ctypedef void (*GL_RASTER_POS2F)(GLfloat x, GLfloat y)
ctypedef void (*GL_RASTER_POS2FV)(const GLfloat *v)
ctypedef void (*GL_RASTER_POS2I)(GLint x, GLint y)
ctypedef void (*GL_RASTER_POS2IV)(const GLint *v)
ctypedef void (*GL_RASTER_POS2S)(GLshort x, GLshort y)
ctypedef void (*GL_RASTER_POS2SV)(const GLshort *v)
ctypedef void (*GL_RASTER_POS3D)(GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*GL_RASTER_POS3DV)(const GLdouble *v)
ctypedef void (*GL_RASTER_POS3F)(GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*GL_RASTER_POS3FV)(const GLfloat *v)
ctypedef void (*GL_RASTER_POS3I)(GLint x, GLint y, GLint z)
ctypedef void (*GL_RASTER_POS3IV)(const GLint *v)
ctypedef void (*GL_RASTER_POS3S)(GLshort x, GLshort y, GLshort z)
ctypedef void (*GL_RASTER_POS3SV)(const GLshort *v)
ctypedef void (*GL_RASTER_POS4D)(GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*GL_RASTER_POS4DV)(const GLdouble *v)
ctypedef void (*GL_RASTER_POS4F)(GLfloat x, GLfloat y, GLfloat z, GLfloat w)
ctypedef void (*GL_RASTER_POS4FV)(const GLfloat *v)
ctypedef void (*GL_RASTER_POS4I)(GLint x, GLint y, GLint z, GLint w)
ctypedef void (*GL_RASTER_POS4IV)(const GLint *v)
ctypedef void (*GL_RASTER_POS4S)(GLshort x, GLshort y, GLshort z, GLshort w)
ctypedef void (*GL_RASTER_POS4SV)(const GLshort *v)
ctypedef void (*GL_RECTD)(GLdouble x1, GLdouble y1, GLdouble x2, GLdouble y2)
ctypedef void (*GL_RECTDV)(const GLdouble *v1, const GLdouble *v2)
ctypedef void (*GL_RECTF)(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2)
ctypedef void (*GL_RECTFV)(const GLfloat *v1, const GLfloat *v2)
ctypedef void (*GL_RECTI)(GLint x1, GLint y1, GLint x2, GLint y2)
ctypedef void (*GL_RECTIV)(const GLint *v1, const GLint *v2)
ctypedef void (*GL_RECTS)(GLshort x1, GLshort y1, GLshort x2, GLshort y2)
ctypedef void (*GL_RECTSV)(const GLshort *v1, const GLshort *v2)
ctypedef void (*GL_TEX_COORD1D)(GLdouble s)
ctypedef void (*GL_TEX_COORD1DV)(const GLdouble *v)
ctypedef void (*GL_TEX_COORD1F)(GLfloat s)
ctypedef void (*GL_TEX_COORD1FV)(const GLfloat *v)
ctypedef void (*GL_TEX_COORD1I)(GLint s)
ctypedef void (*GL_TEX_COORD1IV)(const GLint *v)
ctypedef void (*GL_TEX_COORD1S)(GLshort s)
ctypedef void (*GL_TEX_COORD1SV)(const GLshort *v)
ctypedef void (*GL_TEX_COORD2D)(GLdouble s, GLdouble t)
ctypedef void (*GL_TEX_COORD2DV)(const GLdouble *v)
ctypedef void (*GL_TEX_COORD2F)(GLfloat s, GLfloat t)
ctypedef void (*GL_TEX_COORD2FV)(const GLfloat *v)
ctypedef void (*GL_TEX_COORD2I)(GLint s, GLint t)
ctypedef void (*GL_TEX_COORD2IV)(const GLint *v)
ctypedef void (*GL_TEX_COORD2S)(GLshort s, GLshort t)
ctypedef void (*GL_TEX_COORD2SV)(const GLshort *v)
ctypedef void (*GL_TEX_COORD3D)(GLdouble s, GLdouble t, GLdouble r)
ctypedef void (*GL_TEX_COORD3DV)(const GLdouble *v)
ctypedef void (*GL_TEX_COORD3F)(GLfloat s, GLfloat t, GLfloat r)
ctypedef void (*GL_TEX_COORD3FV)(const GLfloat *v)
ctypedef void (*GL_TEX_COORD3I)(GLint s, GLint t, GLint r)
ctypedef void (*GL_TEX_COORD3IV)(const GLint *v)
ctypedef void (*GL_TEX_COORD3S)(GLshort s, GLshort t, GLshort r)
ctypedef void (*GL_TEX_COORD3SV)(const GLshort *v)
ctypedef void (*GL_TEX_COORD4D)(GLdouble s, GLdouble t, GLdouble r, GLdouble q)
ctypedef void (*GL_TEX_COORD4DV)(const GLdouble *v)
ctypedef void (*GL_TEX_COORD4F)(GLfloat s, GLfloat t, GLfloat r, GLfloat q)
ctypedef void (*GL_TEX_COORD4FV)(const GLfloat *v)
ctypedef void (*GL_TEX_COORD4I)(GLint s, GLint t, GLint r, GLint q)
ctypedef void (*GL_TEX_COORD4IV)(const GLint *v)
ctypedef void (*GL_TEX_COORD4S)(GLshort s, GLshort t, GLshort r, GLshort q)
ctypedef void (*GL_TEX_COORD4SV)(const GLshort *v)
ctypedef void (*GL_VERTEX2D)(GLdouble x, GLdouble y)
ctypedef void (*GL_VERTEX2DV)(const GLdouble *v)
ctypedef void (*GL_VERTEX2F)(GLfloat x, GLfloat y)
ctypedef void (*GL_VERTEX2FV)(const GLfloat *v)
ctypedef void (*GL_VERTEX2I)(GLint x, GLint y)
ctypedef void (*GL_VERTEX2IV)(const GLint *v)
ctypedef void (*GL_VERTEX2S)(GLshort x, GLshort y)
ctypedef void (*GL_VERTEX2SV)(const GLshort *v)
ctypedef void (*GL_VERTEX3D)(GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*GL_VERTEX3DV)(const GLdouble *v)
ctypedef void (*GL_VERTEX3F)(GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*GL_VERTEX3FV)(const GLfloat *v)
ctypedef void (*GL_VERTEX3I)(GLint x, GLint y, GLint z)
ctypedef void (*GL_VERTEX3IV)(const GLint *v)
ctypedef void (*GL_VERTEX3S)(GLshort x, GLshort y, GLshort z)
ctypedef void (*GL_VERTEX3SV)(const GLshort *v)
ctypedef void (*GL_VERTEX4D)(GLdouble x, GLdouble y, GLdouble z, GLdouble w)
ctypedef void (*GL_VERTEX4DV)(const GLdouble *v)
ctypedef void (*GL_VERTEX4F)(GLfloat x, GLfloat y, GLfloat z, GLfloat w)
ctypedef void (*GL_VERTEX4FV)(const GLfloat *v)
ctypedef void (*GL_VERTEX4I)(GLint x, GLint y, GLint z, GLint w)
ctypedef void (*GL_VERTEX4IV)(const GLint *v)
ctypedef void (*GL_VERTEX4S)(GLshort x, GLshort y, GLshort z, GLshort w)
ctypedef void (*GL_VERTEX4SV)(const GLshort *v)
ctypedef void (*GL_CLIP_PLANE)(GLenum plane, const GLdouble *equation)
ctypedef void (*GL_COLOR_MATERIAL)(GLenum face, GLenum mode)
ctypedef void (*GL_FOGF)(GLenum pname, GLfloat param)
ctypedef void (*GL_FOGFV)(GLenum pname, const GLfloat *params)
ctypedef void (*GL_FOGI)(GLenum pname, GLint param)
ctypedef void (*GL_FOGIV)(GLenum pname, const GLint *params)
ctypedef void (*GL_LIGHTF)(GLenum light, GLenum pname, GLfloat param)
ctypedef void (*GL_LIGHTFV)(GLenum light, GLenum pname, const GLfloat *params)
ctypedef void (*GL_LIGHTI)(GLenum light, GLenum pname, GLint param)
ctypedef void (*GL_LIGHTIV)(GLenum light, GLenum pname, const GLint *params)
ctypedef void (*GL_LIGHT_MODELF)(GLenum pname, GLfloat param)
ctypedef void (*GL_LIGHT_MODELFV)(GLenum pname, const GLfloat *params)
ctypedef void (*GL_LIGHT_MODELI)(GLenum pname, GLint param)
ctypedef void (*GL_LIGHT_MODELIV)(GLenum pname, const GLint *params)
ctypedef void (*GL_LINE_STIPPLE)(GLint factor, GLushort pattern)
ctypedef void (*GL_MATERIALF)(GLenum face, GLenum pname, GLfloat param)
ctypedef void (*GL_MATERIALFV)(GLenum face, GLenum pname, const GLfloat *params)
ctypedef void (*GL_MATERIALI)(GLenum face, GLenum pname, GLint param)
ctypedef void (*GL_MATERIALIV)(GLenum face, GLenum pname, const GLint *params)
ctypedef void (*GL_POLYGON_STIPPLE)(const GLubyte *mask)
ctypedef void (*GL_SHADE_MODEL)(GLenum mode)
ctypedef void (*GL_TEX_ENVF)(GLenum target, GLenum pname, GLfloat param)
ctypedef void (*GL_TEX_ENVFV)(GLenum target, GLenum pname, const GLfloat *params)
ctypedef void (*GL_TEX_ENVI)(GLenum target, GLenum pname, GLint param)
ctypedef void (*GL_TEX_ENVIV)(GLenum target, GLenum pname, const GLint *params)
ctypedef void (*GL_TEX_GEND)(GLenum coord, GLenum pname, GLdouble param)
ctypedef void (*GL_TEX_GENDV)(GLenum coord, GLenum pname, const GLdouble *params)
ctypedef void (*GL_TEX_GENF)(GLenum coord, GLenum pname, GLfloat param)
ctypedef void (*GL_TEX_GENFV)(GLenum coord, GLenum pname, const GLfloat *params)
ctypedef void (*GL_TEX_GENI)(GLenum coord, GLenum pname, GLint param)
ctypedef void (*GL_TEX_GENIV)(GLenum coord, GLenum pname, const GLint *params)
ctypedef void (*GL_FEEDBACK_BUFFER)(GLsizei size, GLenum type, GLfloat *buffer)
ctypedef void (*GL_SELECT_BUFFER)(GLsizei size, GLuint *buffer)
ctypedef GLint (*GL_RENDER_MODE)(GLenum mode)
ctypedef void (*GL_INIT_NAMES)()
ctypedef void (*GL_LOAD_NAME)(GLuint name)
ctypedef void (*GL_PASS_THROUGH)(GLfloat token)
ctypedef void (*GL_POP_NAME)()
ctypedef void (*GL_PUSH_NAME)(GLuint name)
ctypedef void (*GL_CLEAR_ACCUM)(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha)
ctypedef void (*GL_CLEAR_INDEX)(GLfloat c)
ctypedef void (*GL_INDEX_MASK)(GLuint mask)
ctypedef void (*GL_ACCUM)(GLenum op, GLfloat value)
ctypedef void (*GL_POP_ATTRIB)()
ctypedef void (*GL_PUSH_ATTRIB)(GLbitfield mask)
ctypedef void (*GL_MAP1D)(GLenum target, GLdouble u1, GLdouble u2, GLint stride, GLint order, const GLdouble *points)
ctypedef void (*GL_MAP1F)(GLenum target, GLfloat u1, GLfloat u2, GLint stride, GLint order, const GLfloat *points)
ctypedef void (*GL_MAP2D)(GLenum target, GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint vstride, GLint vorder, const GLdouble *points)
ctypedef void (*GL_MAP2F)(GLenum target, GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride, GLint vorder, const GLfloat *points)
ctypedef void (*GL_MAP_GRID1D)(GLint un, GLdouble u1, GLdouble u2)
ctypedef void (*GL_MAP_GRID1F)(GLint un, GLfloat u1, GLfloat u2)
ctypedef void (*GL_MAP_GRID2D)(GLint un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2)
ctypedef void (*GL_MAP_GRID2F)(GLint un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2)
ctypedef void (*GL_EVAL_COORD1D)(GLdouble u)
ctypedef void (*GL_EVAL_COORD1DV)(const GLdouble *u)
ctypedef void (*GL_EVAL_COORD1F)(GLfloat u)
ctypedef void (*GL_EVAL_COORD1FV)(const GLfloat *u)
ctypedef void (*GL_EVAL_COORD2D)(GLdouble u, GLdouble v)
ctypedef void (*GL_EVAL_COORD2DV)(const GLdouble *u)
ctypedef void (*GL_EVAL_COORD2F)(GLfloat u, GLfloat v)
ctypedef void (*GL_EVAL_COORD2FV)(const GLfloat *u)
ctypedef void (*GL_EVAL_MESH1)(GLenum mode, GLint i1, GLint i2)
ctypedef void (*GL_EVAL_POINT1)(GLint i)
ctypedef void (*GL_EVAL_MESH2)(GLenum mode, GLint i1, GLint i2, GLint j1, GLint j2)
ctypedef void (*GL_EVAL_POINT2)(GLint i, GLint j)
ctypedef void (*GL_ALPHA_FUNC)(GLenum func, GLfloat ref)
ctypedef void (*GL_PIXEL_ZOOM)(GLfloat xfactor, GLfloat yfactor)
ctypedef void (*GL_PIXEL_TRANSFERF)(GLenum pname, GLfloat param)
ctypedef void (*GL_PIXEL_TRANSFERI)(GLenum pname, GLint param)
ctypedef void (*GL_PIXEL_MAPFV)(GLenum map, GLsizei mapsize, const GLfloat *values)
ctypedef void (*GL_PIXEL_MAPUIV)(GLenum map, GLsizei mapsize, const GLuint *values)
ctypedef void (*GL_PIXEL_MAPUSV)(GLenum map, GLsizei mapsize, const GLushort *values)
ctypedef void (*GL_COPY_PIXELS)(GLint x, GLint y, GLsizei width, GLsizei height, GLenum type)
ctypedef void (*GL_DRAW_PIXELS)(GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels)
ctypedef void (*GL_GET_CLIP_PLANE)(GLenum plane, GLdouble *equation)
ctypedef void (*GL_GET_LIGHTFV)(GLenum light, GLenum pname, GLfloat *params)
ctypedef void (*GL_GET_LIGHTIV)(GLenum light, GLenum pname, GLint *params)
ctypedef void (*GL_GET_MAPDV)(GLenum target, GLenum query, GLdouble *v)
ctypedef void (*GL_GET_MAPFV)(GLenum target, GLenum query, GLfloat *v)
ctypedef void (*GL_GET_MAPIV)(GLenum target, GLenum query, GLint *v)
ctypedef void (*GL_GET_MATERIALFV)(GLenum face, GLenum pname, GLfloat *params)
ctypedef void (*GL_GET_MATERIALIV)(GLenum face, GLenum pname, GLint *params)
ctypedef void (*GL_GET_PIXEL_MAPFV)(GLenum map, GLfloat *values)
ctypedef void (*GL_GET_PIXEL_MAPUIV)(GLenum map, GLuint *values)
ctypedef void (*GL_GET_PIXEL_MAPUSV)(GLenum map, GLushort *values)
ctypedef void (*GL_GET_POLYGON_STIPPLE)(GLubyte *mask)
ctypedef void (*GL_GET_TEX_ENVFV)(GLenum target, GLenum pname, GLfloat *params)
ctypedef void (*GL_GET_TEX_ENVIV)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*GL_GET_TEX_GENDV)(GLenum coord, GLenum pname, GLdouble *params)
ctypedef void (*GL_GET_TEX_GENFV)(GLenum coord, GLenum pname, GLfloat *params)
ctypedef void (*GL_GET_TEX_GENIV)(GLenum coord, GLenum pname, GLint *params)
ctypedef GLboolean (*GL_IS_LIST)(GLuint list)
ctypedef void (*GL_FRUSTUM)(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
ctypedef void (*GL_LOAD_IDENTITY)()
ctypedef void (*GL_LOAD_MATRIXF)(const GLfloat *m)
ctypedef void (*GL_LOAD_MATRIXD)(const GLdouble *m)
ctypedef void (*GL_MATRIX_MODE)(GLenum mode)
ctypedef void (*GL_MULT_MATRIXF)(const GLfloat *m)
ctypedef void (*GL_MULT_MATRIXD)(const GLdouble *m)
ctypedef void (*GL_ORTHO)(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar)
ctypedef void (*GL_POP_MATRIX)()
ctypedef void (*GL_PUSH_MATRIX)()
ctypedef void (*GL_ROTATED)(GLdouble angle, GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*GL_ROTATEF)(GLfloat angle, GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*GL_SCALED)(GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*GL_SCALEF)(GLfloat x, GLfloat y, GLfloat z)
ctypedef void (*GL_TRANSLATED)(GLdouble x, GLdouble y, GLdouble z)
ctypedef void (*GL_TRANSLATEF)(GLfloat x, GLfloat y, GLfloat z)

cdef GL_CULL_FACE cglCullFace = NULL
cdef GL_FRONT_FACE cglFrontFace = NULL
cdef GL_HINT cglHint = NULL
cdef GL_LINE_WIDTH cglLineWidth = NULL
cdef GL_POINT_SIZE cglPointSize = NULL
cdef GL_POLYGON_MODE cglPolygonMode = NULL
cdef GL_SCISSOR cglScissor = NULL
cdef GL_TEX_PARAMETERF cglTexParameterf = NULL
cdef GL_TEX_PARAMETERFV cglTexParameterfv = NULL
cdef GL_TEX_PARAMETERI cglTexParameteri = NULL
cdef GL_TEX_PARAMETERIV cglTexParameteriv = NULL
cdef GL_TEX_IMAGE1D cglTexImage1D = NULL
cdef GL_TEX_IMAGE2D cglTexImage2D = NULL
cdef GL_DRAW_BUFFER cglDrawBuffer = NULL
cdef GL_CLEAR cglClear = NULL
cdef GL_CLEAR_COLOR cglClearColor = NULL
cdef GL_CLEAR_STENCIL cglClearStencil = NULL
cdef GL_CLEAR_DEPTH cglClearDepth = NULL
cdef GL_STENCIL_MASK cglStencilMask = NULL
cdef GL_COLOR_MASK cglColorMask = NULL
cdef GL_DEPTH_MASK cglDepthMask = NULL
cdef GL_DISABLE cglDisable = NULL
cdef GL_ENABLE cglEnable = NULL
cdef GL_FINISH cglFinish = NULL
cdef GL_FLUSH cglFlush = NULL
cdef GL_BLEND_FUNC cglBlendFunc = NULL
cdef GL_LOGIC_OP cglLogicOp = NULL
cdef GL_STENCIL_FUNC cglStencilFunc = NULL
cdef GL_STENCIL_OP cglStencilOp = NULL
cdef GL_DEPTH_FUNC cglDepthFunc = NULL
cdef GL_PIXEL_STOREF cglPixelStoref = NULL
cdef GL_PIXEL_STOREI cglPixelStorei = NULL
cdef GL_READ_BUFFER cglReadBuffer = NULL
cdef GL_READ_PIXELS cglReadPixels = NULL
cdef GL_GET_BOOLEANV cglGetBooleanv = NULL
cdef GL_GET_DOUBLEV cglGetDoublev = NULL
cdef GL_GET_ERROR cglGetError = NULL
cdef GL_GET_FLOATV cglGetFloatv = NULL
cdef GL_GET_INTEGERV cglGetIntegerv = NULL
cdef GL_GET_STRING cglGetString = NULL
cdef GL_GET_TEX_IMAGE cglGetTexImage = NULL
cdef GL_GET_TEX_PARAMETERFV cglGetTexParameterfv = NULL
cdef GL_GET_TEX_PARAMETERIV cglGetTexParameteriv = NULL
cdef GL_GET_TEX_LEVEL_PARAMETERFV cglGetTexLevelParameterfv = NULL
cdef GL_GET_TEX_LEVEL_PARAMETERIV cglGetTexLevelParameteriv = NULL
cdef GL_IS_ENABLED cglIsEnabled = NULL
cdef GL_DEPTH_RANGE cglDepthRange = NULL
cdef GL_VIEWPORT cglViewport = NULL
cdef GL_NEW_LIST cglNewList = NULL
cdef GL_END_LIST cglEndList = NULL
cdef GL_CALL_LIST cglCallList = NULL
cdef GL_CALL_LISTS cglCallLists = NULL
cdef GL_DELETE_LISTS cglDeleteLists = NULL
cdef GL_GEN_LISTS cglGenLists = NULL
cdef GL_LIST_BASE cglListBase = NULL
cdef GL_BEGIN cglBegin = NULL
cdef GL_BITMAP cglBitmap = NULL
cdef GL_COLOR3B cglColor3b = NULL
cdef GL_COLOR3BV cglColor3bv = NULL
cdef GL_COLOR3D cglColor3d = NULL
cdef GL_COLOR3DV cglColor3dv = NULL
cdef GL_COLOR3F cglColor3f = NULL
cdef GL_COLOR3FV cglColor3fv = NULL
cdef GL_COLOR3I cglColor3i = NULL
cdef GL_COLOR3IV cglColor3iv = NULL
cdef GL_COLOR3S cglColor3s = NULL
cdef GL_COLOR3SV cglColor3sv = NULL
cdef GL_COLOR3UB cglColor3ub = NULL
cdef GL_COLOR3UBV cglColor3ubv = NULL
cdef GL_COLOR3UI cglColor3ui = NULL
cdef GL_COLOR3UIV cglColor3uiv = NULL
cdef GL_COLOR3US cglColor3us = NULL
cdef GL_COLOR3USV cglColor3usv = NULL
cdef GL_COLOR4B cglColor4b = NULL
cdef GL_COLOR4BV cglColor4bv = NULL
cdef GL_COLOR4D cglColor4d = NULL
cdef GL_COLOR4DV cglColor4dv = NULL
cdef GL_COLOR4F cglColor4f = NULL
cdef GL_COLOR4FV cglColor4fv = NULL
cdef GL_COLOR4I cglColor4i = NULL
cdef GL_COLOR4IV cglColor4iv = NULL
cdef GL_COLOR4S cglColor4s = NULL
cdef GL_COLOR4SV cglColor4sv = NULL
cdef GL_COLOR4UB cglColor4ub = NULL
cdef GL_COLOR4UBV cglColor4ubv = NULL
cdef GL_COLOR4UI cglColor4ui = NULL
cdef GL_COLOR4UIV cglColor4uiv = NULL
cdef GL_COLOR4US cglColor4us = NULL
cdef GL_COLOR4USV cglColor4usv = NULL
cdef GL_EDGE_FLAG cglEdgeFlag = NULL
cdef GL_EDGE_FLAGV cglEdgeFlagv = NULL
cdef GL_END cglEnd = NULL
cdef GL_INDEXD cglIndexd = NULL
cdef GL_INDEXDV cglIndexdv = NULL
cdef GL_INDEXF cglIndexf = NULL
cdef GL_INDEXFV cglIndexfv = NULL
cdef GL_INDEXI cglIndexi = NULL
cdef GL_INDEXIV cglIndexiv = NULL
cdef GL_INDEXS cglIndexs = NULL
cdef GL_INDEXSV cglIndexsv = NULL
cdef GL_NORMAL3B cglNormal3b = NULL
cdef GL_NORMAL3BV cglNormal3bv = NULL
cdef GL_NORMAL3D cglNormal3d = NULL
cdef GL_NORMAL3DV cglNormal3dv = NULL
cdef GL_NORMAL3F cglNormal3f = NULL
cdef GL_NORMAL3FV cglNormal3fv = NULL
cdef GL_NORMAL3I cglNormal3i = NULL
cdef GL_NORMAL3IV cglNormal3iv = NULL
cdef GL_NORMAL3S cglNormal3s = NULL
cdef GL_NORMAL3SV cglNormal3sv = NULL
cdef GL_RASTER_POS2D cglRasterPos2d = NULL
cdef GL_RASTER_POS2DV cglRasterPos2dv = NULL
cdef GL_RASTER_POS2F cglRasterPos2f = NULL
cdef GL_RASTER_POS2FV cglRasterPos2fv = NULL
cdef GL_RASTER_POS2I cglRasterPos2i = NULL
cdef GL_RASTER_POS2IV cglRasterPos2iv = NULL
cdef GL_RASTER_POS2S cglRasterPos2s = NULL
cdef GL_RASTER_POS2SV cglRasterPos2sv = NULL
cdef GL_RASTER_POS3D cglRasterPos3d = NULL
cdef GL_RASTER_POS3DV cglRasterPos3dv = NULL
cdef GL_RASTER_POS3F cglRasterPos3f = NULL
cdef GL_RASTER_POS3FV cglRasterPos3fv = NULL
cdef GL_RASTER_POS3I cglRasterPos3i = NULL
cdef GL_RASTER_POS3IV cglRasterPos3iv = NULL
cdef GL_RASTER_POS3S cglRasterPos3s = NULL
cdef GL_RASTER_POS3SV cglRasterPos3sv = NULL
cdef GL_RASTER_POS4D cglRasterPos4d = NULL
cdef GL_RASTER_POS4DV cglRasterPos4dv = NULL
cdef GL_RASTER_POS4F cglRasterPos4f = NULL
cdef GL_RASTER_POS4FV cglRasterPos4fv = NULL
cdef GL_RASTER_POS4I cglRasterPos4i = NULL
cdef GL_RASTER_POS4IV cglRasterPos4iv = NULL
cdef GL_RASTER_POS4S cglRasterPos4s = NULL
cdef GL_RASTER_POS4SV cglRasterPos4sv = NULL
cdef GL_RECTD cglRectd = NULL
cdef GL_RECTDV cglRectdv = NULL
cdef GL_RECTF cglRectf = NULL
cdef GL_RECTFV cglRectfv = NULL
cdef GL_RECTI cglRecti = NULL
cdef GL_RECTIV cglRectiv = NULL
cdef GL_RECTS cglRects = NULL
cdef GL_RECTSV cglRectsv = NULL
cdef GL_TEX_COORD1D cglTexCoord1d = NULL
cdef GL_TEX_COORD1DV cglTexCoord1dv = NULL
cdef GL_TEX_COORD1F cglTexCoord1f = NULL
cdef GL_TEX_COORD1FV cglTexCoord1fv = NULL
cdef GL_TEX_COORD1I cglTexCoord1i = NULL
cdef GL_TEX_COORD1IV cglTexCoord1iv = NULL
cdef GL_TEX_COORD1S cglTexCoord1s = NULL
cdef GL_TEX_COORD1SV cglTexCoord1sv = NULL
cdef GL_TEX_COORD2D cglTexCoord2d = NULL
cdef GL_TEX_COORD2DV cglTexCoord2dv = NULL
cdef GL_TEX_COORD2F cglTexCoord2f = NULL
cdef GL_TEX_COORD2FV cglTexCoord2fv = NULL
cdef GL_TEX_COORD2I cglTexCoord2i = NULL
cdef GL_TEX_COORD2IV cglTexCoord2iv = NULL
cdef GL_TEX_COORD2S cglTexCoord2s = NULL
cdef GL_TEX_COORD2SV cglTexCoord2sv = NULL
cdef GL_TEX_COORD3D cglTexCoord3d = NULL
cdef GL_TEX_COORD3DV cglTexCoord3dv = NULL
cdef GL_TEX_COORD3F cglTexCoord3f = NULL
cdef GL_TEX_COORD3FV cglTexCoord3fv = NULL
cdef GL_TEX_COORD3I cglTexCoord3i = NULL
cdef GL_TEX_COORD3IV cglTexCoord3iv = NULL
cdef GL_TEX_COORD3S cglTexCoord3s = NULL
cdef GL_TEX_COORD3SV cglTexCoord3sv = NULL
cdef GL_TEX_COORD4D cglTexCoord4d = NULL
cdef GL_TEX_COORD4DV cglTexCoord4dv = NULL
cdef GL_TEX_COORD4F cglTexCoord4f = NULL
cdef GL_TEX_COORD4FV cglTexCoord4fv = NULL
cdef GL_TEX_COORD4I cglTexCoord4i = NULL
cdef GL_TEX_COORD4IV cglTexCoord4iv = NULL
cdef GL_TEX_COORD4S cglTexCoord4s = NULL
cdef GL_TEX_COORD4SV cglTexCoord4sv = NULL
cdef GL_VERTEX2D cglVertex2d = NULL
cdef GL_VERTEX2DV cglVertex2dv = NULL
cdef GL_VERTEX2F cglVertex2f = NULL
cdef GL_VERTEX2FV cglVertex2fv = NULL
cdef GL_VERTEX2I cglVertex2i = NULL
cdef GL_VERTEX2IV cglVertex2iv = NULL
cdef GL_VERTEX2S cglVertex2s = NULL
cdef GL_VERTEX2SV cglVertex2sv = NULL
cdef GL_VERTEX3D cglVertex3d = NULL
cdef GL_VERTEX3DV cglVertex3dv = NULL
cdef GL_VERTEX3F cglVertex3f = NULL
cdef GL_VERTEX3FV cglVertex3fv = NULL
cdef GL_VERTEX3I cglVertex3i = NULL
cdef GL_VERTEX3IV cglVertex3iv = NULL
cdef GL_VERTEX3S cglVertex3s = NULL
cdef GL_VERTEX3SV cglVertex3sv = NULL
cdef GL_VERTEX4D cglVertex4d = NULL
cdef GL_VERTEX4DV cglVertex4dv = NULL
cdef GL_VERTEX4F cglVertex4f = NULL
cdef GL_VERTEX4FV cglVertex4fv = NULL
cdef GL_VERTEX4I cglVertex4i = NULL
cdef GL_VERTEX4IV cglVertex4iv = NULL
cdef GL_VERTEX4S cglVertex4s = NULL
cdef GL_VERTEX4SV cglVertex4sv = NULL
cdef GL_CLIP_PLANE cglClipPlane = NULL
cdef GL_COLOR_MATERIAL cglColorMaterial = NULL
cdef GL_FOGF cglFogf = NULL
cdef GL_FOGFV cglFogfv = NULL
cdef GL_FOGI cglFogi = NULL
cdef GL_FOGIV cglFogiv = NULL
cdef GL_LIGHTF cglLightf = NULL
cdef GL_LIGHTFV cglLightfv = NULL
cdef GL_LIGHTI cglLighti = NULL
cdef GL_LIGHTIV cglLightiv = NULL
cdef GL_LIGHT_MODELF cglLightModelf = NULL
cdef GL_LIGHT_MODELFV cglLightModelfv = NULL
cdef GL_LIGHT_MODELI cglLightModeli = NULL
cdef GL_LIGHT_MODELIV cglLightModeliv = NULL
cdef GL_LINE_STIPPLE cglLineStipple = NULL
cdef GL_MATERIALF cglMaterialf = NULL
cdef GL_MATERIALFV cglMaterialfv = NULL
cdef GL_MATERIALI cglMateriali = NULL
cdef GL_MATERIALIV cglMaterialiv = NULL
cdef GL_POLYGON_STIPPLE cglPolygonStipple = NULL
cdef GL_SHADE_MODEL cglShadeModel = NULL
cdef GL_TEX_ENVF cglTexEnvf = NULL
cdef GL_TEX_ENVFV cglTexEnvfv = NULL
cdef GL_TEX_ENVI cglTexEnvi = NULL
cdef GL_TEX_ENVIV cglTexEnviv = NULL
cdef GL_TEX_GEND cglTexGend = NULL
cdef GL_TEX_GENDV cglTexGendv = NULL
cdef GL_TEX_GENF cglTexGenf = NULL
cdef GL_TEX_GENFV cglTexGenfv = NULL
cdef GL_TEX_GENI cglTexGeni = NULL
cdef GL_TEX_GENIV cglTexGeniv = NULL
cdef GL_FEEDBACK_BUFFER cglFeedbackBuffer = NULL
cdef GL_SELECT_BUFFER cglSelectBuffer = NULL
cdef GL_RENDER_MODE cglRenderMode = NULL
cdef GL_INIT_NAMES cglInitNames = NULL
cdef GL_LOAD_NAME cglLoadName = NULL
cdef GL_PASS_THROUGH cglPassThrough = NULL
cdef GL_POP_NAME cglPopName = NULL
cdef GL_PUSH_NAME cglPushName = NULL
cdef GL_CLEAR_ACCUM cglClearAccum = NULL
cdef GL_CLEAR_INDEX cglClearIndex = NULL
cdef GL_INDEX_MASK cglIndexMask = NULL
cdef GL_ACCUM cglAccum = NULL
cdef GL_POP_ATTRIB cglPopAttrib = NULL
cdef GL_PUSH_ATTRIB cglPushAttrib = NULL
cdef GL_MAP1D cglMap1d = NULL
cdef GL_MAP1F cglMap1f = NULL
cdef GL_MAP2D cglMap2d = NULL
cdef GL_MAP2F cglMap2f = NULL
cdef GL_MAP_GRID1D cglMapGrid1d = NULL
cdef GL_MAP_GRID1F cglMapGrid1f = NULL
cdef GL_MAP_GRID2D cglMapGrid2d = NULL
cdef GL_MAP_GRID2F cglMapGrid2f = NULL
cdef GL_EVAL_COORD1D cglEvalCoord1d = NULL
cdef GL_EVAL_COORD1DV cglEvalCoord1dv = NULL
cdef GL_EVAL_COORD1F cglEvalCoord1f = NULL
cdef GL_EVAL_COORD1FV cglEvalCoord1fv = NULL
cdef GL_EVAL_COORD2D cglEvalCoord2d = NULL
cdef GL_EVAL_COORD2DV cglEvalCoord2dv = NULL
cdef GL_EVAL_COORD2F cglEvalCoord2f = NULL
cdef GL_EVAL_COORD2FV cglEvalCoord2fv = NULL
cdef GL_EVAL_MESH1 cglEvalMesh1 = NULL
cdef GL_EVAL_POINT1 cglEvalPoint1 = NULL
cdef GL_EVAL_MESH2 cglEvalMesh2 = NULL
cdef GL_EVAL_POINT2 cglEvalPoint2 = NULL
cdef GL_ALPHA_FUNC cglAlphaFunc = NULL
cdef GL_PIXEL_ZOOM cglPixelZoom = NULL
cdef GL_PIXEL_TRANSFERF cglPixelTransferf = NULL
cdef GL_PIXEL_TRANSFERI cglPixelTransferi = NULL
cdef GL_PIXEL_MAPFV cglPixelMapfv = NULL
cdef GL_PIXEL_MAPUIV cglPixelMapuiv = NULL
cdef GL_PIXEL_MAPUSV cglPixelMapusv = NULL
cdef GL_COPY_PIXELS cglCopyPixels = NULL
cdef GL_DRAW_PIXELS cglDrawPixels = NULL
cdef GL_GET_CLIP_PLANE cglGetClipPlane = NULL
cdef GL_GET_LIGHTFV cglGetLightfv = NULL
cdef GL_GET_LIGHTIV cglGetLightiv = NULL
cdef GL_GET_MAPDV cglGetMapdv = NULL
cdef GL_GET_MAPFV cglGetMapfv = NULL
cdef GL_GET_MAPIV cglGetMapiv = NULL
cdef GL_GET_MATERIALFV cglGetMaterialfv = NULL
cdef GL_GET_MATERIALIV cglGetMaterialiv = NULL
cdef GL_GET_PIXEL_MAPFV cglGetPixelMapfv = NULL
cdef GL_GET_PIXEL_MAPUIV cglGetPixelMapuiv = NULL
cdef GL_GET_PIXEL_MAPUSV cglGetPixelMapusv = NULL
cdef GL_GET_POLYGON_STIPPLE cglGetPolygonStipple = NULL
cdef GL_GET_TEX_ENVFV cglGetTexEnvfv = NULL
cdef GL_GET_TEX_ENVIV cglGetTexEnviv = NULL
cdef GL_GET_TEX_GENDV cglGetTexGendv = NULL
cdef GL_GET_TEX_GENFV cglGetTexGenfv = NULL
cdef GL_GET_TEX_GENIV cglGetTexGeniv = NULL
cdef GL_IS_LIST cglIsList = NULL
cdef GL_FRUSTUM cglFrustum = NULL
cdef GL_LOAD_IDENTITY cglLoadIdentity = NULL
cdef GL_LOAD_MATRIXF cglLoadMatrixf = NULL
cdef GL_LOAD_MATRIXD cglLoadMatrixd = NULL
cdef GL_MATRIX_MODE cglMatrixMode = NULL
cdef GL_MULT_MATRIXF cglMultMatrixf = NULL
cdef GL_MULT_MATRIXD cglMultMatrixd = NULL
cdef GL_ORTHO cglOrtho = NULL
cdef GL_POP_MATRIX cglPopMatrix = NULL
cdef GL_PUSH_MATRIX cglPushMatrix = NULL
cdef GL_ROTATED cglRotated = NULL
cdef GL_ROTATEF cglRotatef = NULL
cdef GL_SCALED cglScaled = NULL
cdef GL_SCALEF cglScalef = NULL
cdef GL_TRANSLATED cglTranslated = NULL
cdef GL_TRANSLATEF cglTranslatef = NULL


cdef void GetglCullFace(GLenum mode):
    global cglCullFace
    cglCullFace = <GL_CULL_FACE>getFunction(b"glCullFace")
    cglCullFace(mode)

cdef void GetglFrontFace(GLenum mode):
    global cglFrontFace
    cglFrontFace = <GL_FRONT_FACE>getFunction(b"glFrontFace")
    cglFrontFace(mode)

cdef void GetglHint(GLenum target, GLenum mode):
    global cglHint
    cglHint = <GL_HINT>getFunction(b"glHint")
    cglHint(target, mode)

cdef void GetglLineWidth(GLfloat width):
    global cglLineWidth
    cglLineWidth = <GL_LINE_WIDTH>getFunction(b"glLineWidth")
    cglLineWidth(width)

cdef void GetglPointSize(GLfloat size):
    global cglPointSize
    cglPointSize = <GL_POINT_SIZE>getFunction(b"glPointSize")
    cglPointSize(size)

cdef void GetglPolygonMode(GLenum face, GLenum mode):
    global cglPolygonMode
    cglPolygonMode = <GL_POLYGON_MODE>getFunction(b"glPolygonMode")
    cglPolygonMode(face, mode)

cdef void GetglScissor(GLint x, GLint y, GLsizei width, GLsizei height):
    global cglScissor
    cglScissor = <GL_SCISSOR>getFunction(b"glScissor")
    cglScissor(x, y, width, height)

cdef void GetglTexParameterf(GLenum target, GLenum pname, GLfloat param):
    global cglTexParameterf
    cglTexParameterf = <GL_TEX_PARAMETERF>getFunction(b"glTexParameterf")
    cglTexParameterf(target, pname, param)

cdef void GetglTexParameterfv(GLenum target, GLenum pname, const GLfloat *params):
    global cglTexParameterfv
    cglTexParameterfv = <GL_TEX_PARAMETERFV>getFunction(b"glTexParameterfv")
    cglTexParameterfv(target, pname, params)

cdef void GetglTexParameteri(GLenum target, GLenum pname, GLint param):
    global cglTexParameteri
    cglTexParameteri = <GL_TEX_PARAMETERI>getFunction(b"glTexParameteri")
    cglTexParameteri(target, pname, param)

cdef void GetglTexParameteriv(GLenum target, GLenum pname, const GLint *params):
    global cglTexParameteriv
    cglTexParameteriv = <GL_TEX_PARAMETERIV>getFunction(b"glTexParameteriv")
    cglTexParameteriv(target, pname, params)

cdef void GetglTexImage1D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const void *pixels):
    global cglTexImage1D
    cglTexImage1D = <GL_TEX_IMAGE1D>getFunction(b"glTexImage1D")
    cglTexImage1D(target, level, internalformat, width, border, format, type, pixels)

cdef void GetglTexImage2D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *pixels):
    global cglTexImage2D
    cglTexImage2D = <GL_TEX_IMAGE2D>getFunction(b"glTexImage2D")
    cglTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)

cdef void GetglDrawBuffer(GLenum buf):
    global cglDrawBuffer
    cglDrawBuffer = <GL_DRAW_BUFFER>getFunction(b"glDrawBuffer")
    cglDrawBuffer(buf)

cdef void GetglClear(GLbitfield mask):
    global cglClear
    cglClear = <GL_CLEAR>getFunction(b"glClear")
    cglClear(mask)

cdef void GetglClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    global cglClearColor
    cglClearColor = <GL_CLEAR_COLOR>getFunction(b"glClearColor")
    cglClearColor(red, green, blue, alpha)

cdef void GetglClearStencil(GLint s):
    global cglClearStencil
    cglClearStencil = <GL_CLEAR_STENCIL>getFunction(b"glClearStencil")
    cglClearStencil(s)

cdef void GetglClearDepth(GLdouble depth):
    global cglClearDepth
    cglClearDepth = <GL_CLEAR_DEPTH>getFunction(b"glClearDepth")
    cglClearDepth(depth)

cdef void GetglStencilMask(GLuint mask):
    global cglStencilMask
    cglStencilMask = <GL_STENCIL_MASK>getFunction(b"glStencilMask")
    cglStencilMask(mask)

cdef void GetglColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha):
    global cglColorMask
    cglColorMask = <GL_COLOR_MASK>getFunction(b"glColorMask")
    cglColorMask(red, green, blue, alpha)

cdef void GetglDepthMask(GLboolean flag):
    global cglDepthMask
    cglDepthMask = <GL_DEPTH_MASK>getFunction(b"glDepthMask")
    cglDepthMask(flag)

cdef void GetglDisable(GLenum cap):
    global cglDisable
    cglDisable = <GL_DISABLE>getFunction(b"glDisable")
    cglDisable(cap)

cdef void GetglEnable(GLenum cap):
    global cglEnable
    cglEnable = <GL_ENABLE>getFunction(b"glEnable")
    cglEnable(cap)

cdef void GetglFinish():
    global cglFinish
    cglFinish = <GL_FINISH>getFunction(b"glFinish")
    cglFinish()

cdef void GetglFlush():
    global cglFlush
    cglFlush = <GL_FLUSH>getFunction(b"glFlush")
    cglFlush()

cdef void GetglBlendFunc(GLenum sfactor, GLenum dfactor):
    global cglBlendFunc
    cglBlendFunc = <GL_BLEND_FUNC>getFunction(b"glBlendFunc")
    cglBlendFunc(sfactor, dfactor)

cdef void GetglLogicOp(GLenum opcode):
    global cglLogicOp
    cglLogicOp = <GL_LOGIC_OP>getFunction(b"glLogicOp")
    cglLogicOp(opcode)

cdef void GetglStencilFunc(GLenum func, GLint ref, GLuint mask):
    global cglStencilFunc
    cglStencilFunc = <GL_STENCIL_FUNC>getFunction(b"glStencilFunc")
    cglStencilFunc(func, ref, mask)

cdef void GetglStencilOp(GLenum fail, GLenum zfail, GLenum zpass):
    global cglStencilOp
    cglStencilOp = <GL_STENCIL_OP>getFunction(b"glStencilOp")
    cglStencilOp(fail, zfail, zpass)

cdef void GetglDepthFunc(GLenum func):
    global cglDepthFunc
    cglDepthFunc = <GL_DEPTH_FUNC>getFunction(b"glDepthFunc")
    cglDepthFunc(func)

cdef void GetglPixelStoref(GLenum pname, GLfloat param):
    global cglPixelStoref
    cglPixelStoref = <GL_PIXEL_STOREF>getFunction(b"glPixelStoref")
    cglPixelStoref(pname, param)

cdef void GetglPixelStorei(GLenum pname, GLint param):
    global cglPixelStorei
    cglPixelStorei = <GL_PIXEL_STOREI>getFunction(b"glPixelStorei")
    cglPixelStorei(pname, param)

cdef void GetglReadBuffer(GLenum src):
    global cglReadBuffer
    cglReadBuffer = <GL_READ_BUFFER>getFunction(b"glReadBuffer")
    cglReadBuffer(src)

cdef void GetglReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, void *pixels):
    global cglReadPixels
    cglReadPixels = <GL_READ_PIXELS>getFunction(b"glReadPixels")
    cglReadPixels(x, y, width, height, format, type, pixels)

cdef void GetglGetBooleanv(GLenum pname, GLboolean *data):
    global cglGetBooleanv
    cglGetBooleanv = <GL_GET_BOOLEANV>getFunction(b"glGetBooleanv")
    cglGetBooleanv(pname, data)

cdef void GetglGetDoublev(GLenum pname, GLdouble *data):
    global cglGetDoublev
    cglGetDoublev = <GL_GET_DOUBLEV>getFunction(b"glGetDoublev")
    cglGetDoublev(pname, data)

cdef GLenum GetglGetError():
    global cglGetError
    cglGetError = <GL_GET_ERROR>getFunction(b"glGetError")
    cglGetError()

cdef void GetglGetFloatv(GLenum pname, GLfloat *data):
    global cglGetFloatv
    cglGetFloatv = <GL_GET_FLOATV>getFunction(b"glGetFloatv")
    cglGetFloatv(pname, data)

cdef void GetglGetIntegerv(GLenum pname, GLint *data):
    global cglGetIntegerv
    cglGetIntegerv = <GL_GET_INTEGERV>getFunction(b"glGetIntegerv")
    cglGetIntegerv(pname, data)

cdef const GLubyte *GetglGetString(GLenum name):
    global cglGetString
    cglGetString = <GL_GET_STRING>getFunction(b"glGetString")
    cglGetString(name)

cdef void GetglGetTexImage(GLenum target, GLint level, GLenum format, GLenum type, void *pixels):
    global cglGetTexImage
    cglGetTexImage = <GL_GET_TEX_IMAGE>getFunction(b"glGetTexImage")
    cglGetTexImage(target, level, format, type, pixels)

cdef void GetglGetTexParameterfv(GLenum target, GLenum pname, GLfloat *params):
    global cglGetTexParameterfv
    cglGetTexParameterfv = <GL_GET_TEX_PARAMETERFV>getFunction(b"glGetTexParameterfv")
    cglGetTexParameterfv(target, pname, params)

cdef void GetglGetTexParameteriv(GLenum target, GLenum pname, GLint *params):
    global cglGetTexParameteriv
    cglGetTexParameteriv = <GL_GET_TEX_PARAMETERIV>getFunction(b"glGetTexParameteriv")
    cglGetTexParameteriv(target, pname, params)

cdef void GetglGetTexLevelParameterfv(GLenum target, GLint level, GLenum pname, GLfloat *params):
    global cglGetTexLevelParameterfv
    cglGetTexLevelParameterfv = <GL_GET_TEX_LEVEL_PARAMETERFV>getFunction(b"glGetTexLevelParameterfv")
    cglGetTexLevelParameterfv(target, level, pname, params)

cdef void GetglGetTexLevelParameteriv(GLenum target, GLint level, GLenum pname, GLint *params):
    global cglGetTexLevelParameteriv
    cglGetTexLevelParameteriv = <GL_GET_TEX_LEVEL_PARAMETERIV>getFunction(b"glGetTexLevelParameteriv")
    cglGetTexLevelParameteriv(target, level, pname, params)

cdef GLboolean GetglIsEnabled(GLenum cap):
    global cglIsEnabled
    cglIsEnabled = <GL_IS_ENABLED>getFunction(b"glIsEnabled")
    cglIsEnabled(cap)

cdef void GetglDepthRange(GLdouble n, GLdouble f):
    global cglDepthRange
    cglDepthRange = <GL_DEPTH_RANGE>getFunction(b"glDepthRange")
    cglDepthRange(n, f)

cdef void GetglViewport(GLint x, GLint y, GLsizei width, GLsizei height):
    global cglViewport
    cglViewport = <GL_VIEWPORT>getFunction(b"glViewport")
    cglViewport(x, y, width, height)

cdef void GetglNewList(GLuint list, GLenum mode):
    global cglNewList
    cglNewList = <GL_NEW_LIST>getFunction(b"glNewList")
    cglNewList(list, mode)

cdef void GetglEndList():
    global cglEndList
    cglEndList = <GL_END_LIST>getFunction(b"glEndList")
    cglEndList()

cdef void GetglCallList(GLuint list):
    global cglCallList
    cglCallList = <GL_CALL_LIST>getFunction(b"glCallList")
    cglCallList(list)

cdef void GetglCallLists(GLsizei n, GLenum type, const void *lists):
    global cglCallLists
    cglCallLists = <GL_CALL_LISTS>getFunction(b"glCallLists")
    cglCallLists(n, type, lists)

cdef void GetglDeleteLists(GLuint list, GLsizei range):
    global cglDeleteLists
    cglDeleteLists = <GL_DELETE_LISTS>getFunction(b"glDeleteLists")
    cglDeleteLists(list, range)

cdef GLuint GetglGenLists(GLsizei range):
    global cglGenLists
    cglGenLists = <GL_GEN_LISTS>getFunction(b"glGenLists")
    cglGenLists(range)

cdef void GetglListBase(GLuint base):
    global cglListBase
    cglListBase = <GL_LIST_BASE>getFunction(b"glListBase")
    cglListBase(base)

cdef void GetglBegin(GLenum mode):
    global cglBegin
    cglBegin = <GL_BEGIN>getFunction(b"glBegin")
    cglBegin(mode)

cdef void GetglBitmap(GLsizei width, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte *bitmap):
    global cglBitmap
    cglBitmap = <GL_BITMAP>getFunction(b"glBitmap")
    cglBitmap(width, height, xorig, yorig, xmove, ymove, bitmap)

cdef void GetglColor3b(GLbyte red, GLbyte green, GLbyte blue):
    global cglColor3b
    cglColor3b = <GL_COLOR3B>getFunction(b"glColor3b")
    cglColor3b(red, green, blue)

cdef void GetglColor3bv(const GLbyte *v):
    global cglColor3bv
    cglColor3bv = <GL_COLOR3BV>getFunction(b"glColor3bv")
    cglColor3bv(v)

cdef void GetglColor3d(GLdouble red, GLdouble green, GLdouble blue):
    global cglColor3d
    cglColor3d = <GL_COLOR3D>getFunction(b"glColor3d")
    cglColor3d(red, green, blue)

cdef void GetglColor3dv(const GLdouble *v):
    global cglColor3dv
    cglColor3dv = <GL_COLOR3DV>getFunction(b"glColor3dv")
    cglColor3dv(v)

cdef void GetglColor3f(GLfloat red, GLfloat green, GLfloat blue):
    global cglColor3f
    cglColor3f = <GL_COLOR3F>getFunction(b"glColor3f")
    cglColor3f(red, green, blue)

cdef void GetglColor3fv(const GLfloat *v):
    global cglColor3fv
    cglColor3fv = <GL_COLOR3FV>getFunction(b"glColor3fv")
    cglColor3fv(v)

cdef void GetglColor3i(GLint red, GLint green, GLint blue):
    global cglColor3i
    cglColor3i = <GL_COLOR3I>getFunction(b"glColor3i")
    cglColor3i(red, green, blue)

cdef void GetglColor3iv(const GLint *v):
    global cglColor3iv
    cglColor3iv = <GL_COLOR3IV>getFunction(b"glColor3iv")
    cglColor3iv(v)

cdef void GetglColor3s(GLshort red, GLshort green, GLshort blue):
    global cglColor3s
    cglColor3s = <GL_COLOR3S>getFunction(b"glColor3s")
    cglColor3s(red, green, blue)

cdef void GetglColor3sv(const GLshort *v):
    global cglColor3sv
    cglColor3sv = <GL_COLOR3SV>getFunction(b"glColor3sv")
    cglColor3sv(v)

cdef void GetglColor3ub(GLubyte red, GLubyte green, GLubyte blue):
    global cglColor3ub
    cglColor3ub = <GL_COLOR3UB>getFunction(b"glColor3ub")
    cglColor3ub(red, green, blue)

cdef void GetglColor3ubv(const GLubyte *v):
    global cglColor3ubv
    cglColor3ubv = <GL_COLOR3UBV>getFunction(b"glColor3ubv")
    cglColor3ubv(v)

cdef void GetglColor3ui(GLuint red, GLuint green, GLuint blue):
    global cglColor3ui
    cglColor3ui = <GL_COLOR3UI>getFunction(b"glColor3ui")
    cglColor3ui(red, green, blue)

cdef void GetglColor3uiv(const GLuint *v):
    global cglColor3uiv
    cglColor3uiv = <GL_COLOR3UIV>getFunction(b"glColor3uiv")
    cglColor3uiv(v)

cdef void GetglColor3us(GLushort red, GLushort green, GLushort blue):
    global cglColor3us
    cglColor3us = <GL_COLOR3US>getFunction(b"glColor3us")
    cglColor3us(red, green, blue)

cdef void GetglColor3usv(const GLushort *v):
    global cglColor3usv
    cglColor3usv = <GL_COLOR3USV>getFunction(b"glColor3usv")
    cglColor3usv(v)

cdef void GetglColor4b(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha):
    global cglColor4b
    cglColor4b = <GL_COLOR4B>getFunction(b"glColor4b")
    cglColor4b(red, green, blue, alpha)

cdef void GetglColor4bv(const GLbyte *v):
    global cglColor4bv
    cglColor4bv = <GL_COLOR4BV>getFunction(b"glColor4bv")
    cglColor4bv(v)

cdef void GetglColor4d(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha):
    global cglColor4d
    cglColor4d = <GL_COLOR4D>getFunction(b"glColor4d")
    cglColor4d(red, green, blue, alpha)

cdef void GetglColor4dv(const GLdouble *v):
    global cglColor4dv
    cglColor4dv = <GL_COLOR4DV>getFunction(b"glColor4dv")
    cglColor4dv(v)

cdef void GetglColor4f(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    global cglColor4f
    cglColor4f = <GL_COLOR4F>getFunction(b"glColor4f")
    cglColor4f(red, green, blue, alpha)

cdef void GetglColor4fv(const GLfloat *v):
    global cglColor4fv
    cglColor4fv = <GL_COLOR4FV>getFunction(b"glColor4fv")
    cglColor4fv(v)

cdef void GetglColor4i(GLint red, GLint green, GLint blue, GLint alpha):
    global cglColor4i
    cglColor4i = <GL_COLOR4I>getFunction(b"glColor4i")
    cglColor4i(red, green, blue, alpha)

cdef void GetglColor4iv(const GLint *v):
    global cglColor4iv
    cglColor4iv = <GL_COLOR4IV>getFunction(b"glColor4iv")
    cglColor4iv(v)

cdef void GetglColor4s(GLshort red, GLshort green, GLshort blue, GLshort alpha):
    global cglColor4s
    cglColor4s = <GL_COLOR4S>getFunction(b"glColor4s")
    cglColor4s(red, green, blue, alpha)

cdef void GetglColor4sv(const GLshort *v):
    global cglColor4sv
    cglColor4sv = <GL_COLOR4SV>getFunction(b"glColor4sv")
    cglColor4sv(v)

cdef void GetglColor4ub(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha):
    global cglColor4ub
    cglColor4ub = <GL_COLOR4UB>getFunction(b"glColor4ub")
    cglColor4ub(red, green, blue, alpha)

cdef void GetglColor4ubv(const GLubyte *v):
    global cglColor4ubv
    cglColor4ubv = <GL_COLOR4UBV>getFunction(b"glColor4ubv")
    cglColor4ubv(v)

cdef void GetglColor4ui(GLuint red, GLuint green, GLuint blue, GLuint alpha):
    global cglColor4ui
    cglColor4ui = <GL_COLOR4UI>getFunction(b"glColor4ui")
    cglColor4ui(red, green, blue, alpha)

cdef void GetglColor4uiv(const GLuint *v):
    global cglColor4uiv
    cglColor4uiv = <GL_COLOR4UIV>getFunction(b"glColor4uiv")
    cglColor4uiv(v)

cdef void GetglColor4us(GLushort red, GLushort green, GLushort blue, GLushort alpha):
    global cglColor4us
    cglColor4us = <GL_COLOR4US>getFunction(b"glColor4us")
    cglColor4us(red, green, blue, alpha)

cdef void GetglColor4usv(const GLushort *v):
    global cglColor4usv
    cglColor4usv = <GL_COLOR4USV>getFunction(b"glColor4usv")
    cglColor4usv(v)

cdef void GetglEdgeFlag(GLboolean flag):
    global cglEdgeFlag
    cglEdgeFlag = <GL_EDGE_FLAG>getFunction(b"glEdgeFlag")
    cglEdgeFlag(flag)

cdef void GetglEdgeFlagv(const GLboolean *flag):
    global cglEdgeFlagv
    cglEdgeFlagv = <GL_EDGE_FLAGV>getFunction(b"glEdgeFlagv")
    cglEdgeFlagv(flag)

cdef void GetglEnd():
    global cglEnd
    cglEnd = <GL_END>getFunction(b"glEnd")
    cglEnd()

cdef void GetglIndexd(GLdouble c):
    global cglIndexd
    cglIndexd = <GL_INDEXD>getFunction(b"glIndexd")
    cglIndexd(c)

cdef void GetglIndexdv(const GLdouble *c):
    global cglIndexdv
    cglIndexdv = <GL_INDEXDV>getFunction(b"glIndexdv")
    cglIndexdv(c)

cdef void GetglIndexf(GLfloat c):
    global cglIndexf
    cglIndexf = <GL_INDEXF>getFunction(b"glIndexf")
    cglIndexf(c)

cdef void GetglIndexfv(const GLfloat *c):
    global cglIndexfv
    cglIndexfv = <GL_INDEXFV>getFunction(b"glIndexfv")
    cglIndexfv(c)

cdef void GetglIndexi(GLint c):
    global cglIndexi
    cglIndexi = <GL_INDEXI>getFunction(b"glIndexi")
    cglIndexi(c)

cdef void GetglIndexiv(const GLint *c):
    global cglIndexiv
    cglIndexiv = <GL_INDEXIV>getFunction(b"glIndexiv")
    cglIndexiv(c)

cdef void GetglIndexs(GLshort c):
    global cglIndexs
    cglIndexs = <GL_INDEXS>getFunction(b"glIndexs")
    cglIndexs(c)

cdef void GetglIndexsv(const GLshort *c):
    global cglIndexsv
    cglIndexsv = <GL_INDEXSV>getFunction(b"glIndexsv")
    cglIndexsv(c)

cdef void GetglNormal3b(GLbyte nx, GLbyte ny, GLbyte nz):
    global cglNormal3b
    cglNormal3b = <GL_NORMAL3B>getFunction(b"glNormal3b")
    cglNormal3b(nx, ny, nz)

cdef void GetglNormal3bv(const GLbyte *v):
    global cglNormal3bv
    cglNormal3bv = <GL_NORMAL3BV>getFunction(b"glNormal3bv")
    cglNormal3bv(v)

cdef void GetglNormal3d(GLdouble nx, GLdouble ny, GLdouble nz):
    global cglNormal3d
    cglNormal3d = <GL_NORMAL3D>getFunction(b"glNormal3d")
    cglNormal3d(nx, ny, nz)

cdef void GetglNormal3dv(const GLdouble *v):
    global cglNormal3dv
    cglNormal3dv = <GL_NORMAL3DV>getFunction(b"glNormal3dv")
    cglNormal3dv(v)

cdef void GetglNormal3f(GLfloat nx, GLfloat ny, GLfloat nz):
    global cglNormal3f
    cglNormal3f = <GL_NORMAL3F>getFunction(b"glNormal3f")
    cglNormal3f(nx, ny, nz)

cdef void GetglNormal3fv(const GLfloat *v):
    global cglNormal3fv
    cglNormal3fv = <GL_NORMAL3FV>getFunction(b"glNormal3fv")
    cglNormal3fv(v)

cdef void GetglNormal3i(GLint nx, GLint ny, GLint nz):
    global cglNormal3i
    cglNormal3i = <GL_NORMAL3I>getFunction(b"glNormal3i")
    cglNormal3i(nx, ny, nz)

cdef void GetglNormal3iv(const GLint *v):
    global cglNormal3iv
    cglNormal3iv = <GL_NORMAL3IV>getFunction(b"glNormal3iv")
    cglNormal3iv(v)

cdef void GetglNormal3s(GLshort nx, GLshort ny, GLshort nz):
    global cglNormal3s
    cglNormal3s = <GL_NORMAL3S>getFunction(b"glNormal3s")
    cglNormal3s(nx, ny, nz)

cdef void GetglNormal3sv(const GLshort *v):
    global cglNormal3sv
    cglNormal3sv = <GL_NORMAL3SV>getFunction(b"glNormal3sv")
    cglNormal3sv(v)

cdef void GetglRasterPos2d(GLdouble x, GLdouble y):
    global cglRasterPos2d
    cglRasterPos2d = <GL_RASTER_POS2D>getFunction(b"glRasterPos2d")
    cglRasterPos2d(x, y)

cdef void GetglRasterPos2dv(const GLdouble *v):
    global cglRasterPos2dv
    cglRasterPos2dv = <GL_RASTER_POS2DV>getFunction(b"glRasterPos2dv")
    cglRasterPos2dv(v)

cdef void GetglRasterPos2f(GLfloat x, GLfloat y):
    global cglRasterPos2f
    cglRasterPos2f = <GL_RASTER_POS2F>getFunction(b"glRasterPos2f")
    cglRasterPos2f(x, y)

cdef void GetglRasterPos2fv(const GLfloat *v):
    global cglRasterPos2fv
    cglRasterPos2fv = <GL_RASTER_POS2FV>getFunction(b"glRasterPos2fv")
    cglRasterPos2fv(v)

cdef void GetglRasterPos2i(GLint x, GLint y):
    global cglRasterPos2i
    cglRasterPos2i = <GL_RASTER_POS2I>getFunction(b"glRasterPos2i")
    cglRasterPos2i(x, y)

cdef void GetglRasterPos2iv(const GLint *v):
    global cglRasterPos2iv
    cglRasterPos2iv = <GL_RASTER_POS2IV>getFunction(b"glRasterPos2iv")
    cglRasterPos2iv(v)

cdef void GetglRasterPos2s(GLshort x, GLshort y):
    global cglRasterPos2s
    cglRasterPos2s = <GL_RASTER_POS2S>getFunction(b"glRasterPos2s")
    cglRasterPos2s(x, y)

cdef void GetglRasterPos2sv(const GLshort *v):
    global cglRasterPos2sv
    cglRasterPos2sv = <GL_RASTER_POS2SV>getFunction(b"glRasterPos2sv")
    cglRasterPos2sv(v)

cdef void GetglRasterPos3d(GLdouble x, GLdouble y, GLdouble z):
    global cglRasterPos3d
    cglRasterPos3d = <GL_RASTER_POS3D>getFunction(b"glRasterPos3d")
    cglRasterPos3d(x, y, z)

cdef void GetglRasterPos3dv(const GLdouble *v):
    global cglRasterPos3dv
    cglRasterPos3dv = <GL_RASTER_POS3DV>getFunction(b"glRasterPos3dv")
    cglRasterPos3dv(v)

cdef void GetglRasterPos3f(GLfloat x, GLfloat y, GLfloat z):
    global cglRasterPos3f
    cglRasterPos3f = <GL_RASTER_POS3F>getFunction(b"glRasterPos3f")
    cglRasterPos3f(x, y, z)

cdef void GetglRasterPos3fv(const GLfloat *v):
    global cglRasterPos3fv
    cglRasterPos3fv = <GL_RASTER_POS3FV>getFunction(b"glRasterPos3fv")
    cglRasterPos3fv(v)

cdef void GetglRasterPos3i(GLint x, GLint y, GLint z):
    global cglRasterPos3i
    cglRasterPos3i = <GL_RASTER_POS3I>getFunction(b"glRasterPos3i")
    cglRasterPos3i(x, y, z)

cdef void GetglRasterPos3iv(const GLint *v):
    global cglRasterPos3iv
    cglRasterPos3iv = <GL_RASTER_POS3IV>getFunction(b"glRasterPos3iv")
    cglRasterPos3iv(v)

cdef void GetglRasterPos3s(GLshort x, GLshort y, GLshort z):
    global cglRasterPos3s
    cglRasterPos3s = <GL_RASTER_POS3S>getFunction(b"glRasterPos3s")
    cglRasterPos3s(x, y, z)

cdef void GetglRasterPos3sv(const GLshort *v):
    global cglRasterPos3sv
    cglRasterPos3sv = <GL_RASTER_POS3SV>getFunction(b"glRasterPos3sv")
    cglRasterPos3sv(v)

cdef void GetglRasterPos4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglRasterPos4d
    cglRasterPos4d = <GL_RASTER_POS4D>getFunction(b"glRasterPos4d")
    cglRasterPos4d(x, y, z, w)

cdef void GetglRasterPos4dv(const GLdouble *v):
    global cglRasterPos4dv
    cglRasterPos4dv = <GL_RASTER_POS4DV>getFunction(b"glRasterPos4dv")
    cglRasterPos4dv(v)

cdef void GetglRasterPos4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    global cglRasterPos4f
    cglRasterPos4f = <GL_RASTER_POS4F>getFunction(b"glRasterPos4f")
    cglRasterPos4f(x, y, z, w)

cdef void GetglRasterPos4fv(const GLfloat *v):
    global cglRasterPos4fv
    cglRasterPos4fv = <GL_RASTER_POS4FV>getFunction(b"glRasterPos4fv")
    cglRasterPos4fv(v)

cdef void GetglRasterPos4i(GLint x, GLint y, GLint z, GLint w):
    global cglRasterPos4i
    cglRasterPos4i = <GL_RASTER_POS4I>getFunction(b"glRasterPos4i")
    cglRasterPos4i(x, y, z, w)

cdef void GetglRasterPos4iv(const GLint *v):
    global cglRasterPos4iv
    cglRasterPos4iv = <GL_RASTER_POS4IV>getFunction(b"glRasterPos4iv")
    cglRasterPos4iv(v)

cdef void GetglRasterPos4s(GLshort x, GLshort y, GLshort z, GLshort w):
    global cglRasterPos4s
    cglRasterPos4s = <GL_RASTER_POS4S>getFunction(b"glRasterPos4s")
    cglRasterPos4s(x, y, z, w)

cdef void GetglRasterPos4sv(const GLshort *v):
    global cglRasterPos4sv
    cglRasterPos4sv = <GL_RASTER_POS4SV>getFunction(b"glRasterPos4sv")
    cglRasterPos4sv(v)

cdef void GetglRectd(GLdouble x1, GLdouble y1, GLdouble x2, GLdouble y2):
    global cglRectd
    cglRectd = <GL_RECTD>getFunction(b"glRectd")
    cglRectd(x1, y1, x2, y2)

cdef void GetglRectdv(const GLdouble *v1, const GLdouble *v2):
    global cglRectdv
    cglRectdv = <GL_RECTDV>getFunction(b"glRectdv")
    cglRectdv(v1, v2)

cdef void GetglRectf(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2):
    global cglRectf
    cglRectf = <GL_RECTF>getFunction(b"glRectf")
    cglRectf(x1, y1, x2, y2)

cdef void GetglRectfv(const GLfloat *v1, const GLfloat *v2):
    global cglRectfv
    cglRectfv = <GL_RECTFV>getFunction(b"glRectfv")
    cglRectfv(v1, v2)

cdef void GetglRecti(GLint x1, GLint y1, GLint x2, GLint y2):
    global cglRecti
    cglRecti = <GL_RECTI>getFunction(b"glRecti")
    cglRecti(x1, y1, x2, y2)

cdef void GetglRectiv(const GLint *v1, const GLint *v2):
    global cglRectiv
    cglRectiv = <GL_RECTIV>getFunction(b"glRectiv")
    cglRectiv(v1, v2)

cdef void GetglRects(GLshort x1, GLshort y1, GLshort x2, GLshort y2):
    global cglRects
    cglRects = <GL_RECTS>getFunction(b"glRects")
    cglRects(x1, y1, x2, y2)

cdef void GetglRectsv(const GLshort *v1, const GLshort *v2):
    global cglRectsv
    cglRectsv = <GL_RECTSV>getFunction(b"glRectsv")
    cglRectsv(v1, v2)

cdef void GetglTexCoord1d(GLdouble s):
    global cglTexCoord1d
    cglTexCoord1d = <GL_TEX_COORD1D>getFunction(b"glTexCoord1d")
    cglTexCoord1d(s)

cdef void GetglTexCoord1dv(const GLdouble *v):
    global cglTexCoord1dv
    cglTexCoord1dv = <GL_TEX_COORD1DV>getFunction(b"glTexCoord1dv")
    cglTexCoord1dv(v)

cdef void GetglTexCoord1f(GLfloat s):
    global cglTexCoord1f
    cglTexCoord1f = <GL_TEX_COORD1F>getFunction(b"glTexCoord1f")
    cglTexCoord1f(s)

cdef void GetglTexCoord1fv(const GLfloat *v):
    global cglTexCoord1fv
    cglTexCoord1fv = <GL_TEX_COORD1FV>getFunction(b"glTexCoord1fv")
    cglTexCoord1fv(v)

cdef void GetglTexCoord1i(GLint s):
    global cglTexCoord1i
    cglTexCoord1i = <GL_TEX_COORD1I>getFunction(b"glTexCoord1i")
    cglTexCoord1i(s)

cdef void GetglTexCoord1iv(const GLint *v):
    global cglTexCoord1iv
    cglTexCoord1iv = <GL_TEX_COORD1IV>getFunction(b"glTexCoord1iv")
    cglTexCoord1iv(v)

cdef void GetglTexCoord1s(GLshort s):
    global cglTexCoord1s
    cglTexCoord1s = <GL_TEX_COORD1S>getFunction(b"glTexCoord1s")
    cglTexCoord1s(s)

cdef void GetglTexCoord1sv(const GLshort *v):
    global cglTexCoord1sv
    cglTexCoord1sv = <GL_TEX_COORD1SV>getFunction(b"glTexCoord1sv")
    cglTexCoord1sv(v)

cdef void GetglTexCoord2d(GLdouble s, GLdouble t):
    global cglTexCoord2d
    cglTexCoord2d = <GL_TEX_COORD2D>getFunction(b"glTexCoord2d")
    cglTexCoord2d(s, t)

cdef void GetglTexCoord2dv(const GLdouble *v):
    global cglTexCoord2dv
    cglTexCoord2dv = <GL_TEX_COORD2DV>getFunction(b"glTexCoord2dv")
    cglTexCoord2dv(v)

cdef void GetglTexCoord2f(GLfloat s, GLfloat t):
    global cglTexCoord2f
    cglTexCoord2f = <GL_TEX_COORD2F>getFunction(b"glTexCoord2f")
    cglTexCoord2f(s, t)

cdef void GetglTexCoord2fv(const GLfloat *v):
    global cglTexCoord2fv
    cglTexCoord2fv = <GL_TEX_COORD2FV>getFunction(b"glTexCoord2fv")
    cglTexCoord2fv(v)

cdef void GetglTexCoord2i(GLint s, GLint t):
    global cglTexCoord2i
    cglTexCoord2i = <GL_TEX_COORD2I>getFunction(b"glTexCoord2i")
    cglTexCoord2i(s, t)

cdef void GetglTexCoord2iv(const GLint *v):
    global cglTexCoord2iv
    cglTexCoord2iv = <GL_TEX_COORD2IV>getFunction(b"glTexCoord2iv")
    cglTexCoord2iv(v)

cdef void GetglTexCoord2s(GLshort s, GLshort t):
    global cglTexCoord2s
    cglTexCoord2s = <GL_TEX_COORD2S>getFunction(b"glTexCoord2s")
    cglTexCoord2s(s, t)

cdef void GetglTexCoord2sv(const GLshort *v):
    global cglTexCoord2sv
    cglTexCoord2sv = <GL_TEX_COORD2SV>getFunction(b"glTexCoord2sv")
    cglTexCoord2sv(v)

cdef void GetglTexCoord3d(GLdouble s, GLdouble t, GLdouble r):
    global cglTexCoord3d
    cglTexCoord3d = <GL_TEX_COORD3D>getFunction(b"glTexCoord3d")
    cglTexCoord3d(s, t, r)

cdef void GetglTexCoord3dv(const GLdouble *v):
    global cglTexCoord3dv
    cglTexCoord3dv = <GL_TEX_COORD3DV>getFunction(b"glTexCoord3dv")
    cglTexCoord3dv(v)

cdef void GetglTexCoord3f(GLfloat s, GLfloat t, GLfloat r):
    global cglTexCoord3f
    cglTexCoord3f = <GL_TEX_COORD3F>getFunction(b"glTexCoord3f")
    cglTexCoord3f(s, t, r)

cdef void GetglTexCoord3fv(const GLfloat *v):
    global cglTexCoord3fv
    cglTexCoord3fv = <GL_TEX_COORD3FV>getFunction(b"glTexCoord3fv")
    cglTexCoord3fv(v)

cdef void GetglTexCoord3i(GLint s, GLint t, GLint r):
    global cglTexCoord3i
    cglTexCoord3i = <GL_TEX_COORD3I>getFunction(b"glTexCoord3i")
    cglTexCoord3i(s, t, r)

cdef void GetglTexCoord3iv(const GLint *v):
    global cglTexCoord3iv
    cglTexCoord3iv = <GL_TEX_COORD3IV>getFunction(b"glTexCoord3iv")
    cglTexCoord3iv(v)

cdef void GetglTexCoord3s(GLshort s, GLshort t, GLshort r):
    global cglTexCoord3s
    cglTexCoord3s = <GL_TEX_COORD3S>getFunction(b"glTexCoord3s")
    cglTexCoord3s(s, t, r)

cdef void GetglTexCoord3sv(const GLshort *v):
    global cglTexCoord3sv
    cglTexCoord3sv = <GL_TEX_COORD3SV>getFunction(b"glTexCoord3sv")
    cglTexCoord3sv(v)

cdef void GetglTexCoord4d(GLdouble s, GLdouble t, GLdouble r, GLdouble q):
    global cglTexCoord4d
    cglTexCoord4d = <GL_TEX_COORD4D>getFunction(b"glTexCoord4d")
    cglTexCoord4d(s, t, r, q)

cdef void GetglTexCoord4dv(const GLdouble *v):
    global cglTexCoord4dv
    cglTexCoord4dv = <GL_TEX_COORD4DV>getFunction(b"glTexCoord4dv")
    cglTexCoord4dv(v)

cdef void GetglTexCoord4f(GLfloat s, GLfloat t, GLfloat r, GLfloat q):
    global cglTexCoord4f
    cglTexCoord4f = <GL_TEX_COORD4F>getFunction(b"glTexCoord4f")
    cglTexCoord4f(s, t, r, q)

cdef void GetglTexCoord4fv(const GLfloat *v):
    global cglTexCoord4fv
    cglTexCoord4fv = <GL_TEX_COORD4FV>getFunction(b"glTexCoord4fv")
    cglTexCoord4fv(v)

cdef void GetglTexCoord4i(GLint s, GLint t, GLint r, GLint q):
    global cglTexCoord4i
    cglTexCoord4i = <GL_TEX_COORD4I>getFunction(b"glTexCoord4i")
    cglTexCoord4i(s, t, r, q)

cdef void GetglTexCoord4iv(const GLint *v):
    global cglTexCoord4iv
    cglTexCoord4iv = <GL_TEX_COORD4IV>getFunction(b"glTexCoord4iv")
    cglTexCoord4iv(v)

cdef void GetglTexCoord4s(GLshort s, GLshort t, GLshort r, GLshort q):
    global cglTexCoord4s
    cglTexCoord4s = <GL_TEX_COORD4S>getFunction(b"glTexCoord4s")
    cglTexCoord4s(s, t, r, q)

cdef void GetglTexCoord4sv(const GLshort *v):
    global cglTexCoord4sv
    cglTexCoord4sv = <GL_TEX_COORD4SV>getFunction(b"glTexCoord4sv")
    cglTexCoord4sv(v)

cdef void GetglVertex2d(GLdouble x, GLdouble y):
    global cglVertex2d
    cglVertex2d = <GL_VERTEX2D>getFunction(b"glVertex2d")
    cglVertex2d(x, y)

cdef void GetglVertex2dv(const GLdouble *v):
    global cglVertex2dv
    cglVertex2dv = <GL_VERTEX2DV>getFunction(b"glVertex2dv")
    cglVertex2dv(v)

cdef void GetglVertex2f(GLfloat x, GLfloat y):
    global cglVertex2f
    cglVertex2f = <GL_VERTEX2F>getFunction(b"glVertex2f")
    cglVertex2f(x, y)

cdef void GetglVertex2fv(const GLfloat *v):
    global cglVertex2fv
    cglVertex2fv = <GL_VERTEX2FV>getFunction(b"glVertex2fv")
    cglVertex2fv(v)

cdef void GetglVertex2i(GLint x, GLint y):
    global cglVertex2i
    cglVertex2i = <GL_VERTEX2I>getFunction(b"glVertex2i")
    cglVertex2i(x, y)

cdef void GetglVertex2iv(const GLint *v):
    global cglVertex2iv
    cglVertex2iv = <GL_VERTEX2IV>getFunction(b"glVertex2iv")
    cglVertex2iv(v)

cdef void GetglVertex2s(GLshort x, GLshort y):
    global cglVertex2s
    cglVertex2s = <GL_VERTEX2S>getFunction(b"glVertex2s")
    cglVertex2s(x, y)

cdef void GetglVertex2sv(const GLshort *v):
    global cglVertex2sv
    cglVertex2sv = <GL_VERTEX2SV>getFunction(b"glVertex2sv")
    cglVertex2sv(v)

cdef void GetglVertex3d(GLdouble x, GLdouble y, GLdouble z):
    global cglVertex3d
    cglVertex3d = <GL_VERTEX3D>getFunction(b"glVertex3d")
    cglVertex3d(x, y, z)

cdef void GetglVertex3dv(const GLdouble *v):
    global cglVertex3dv
    cglVertex3dv = <GL_VERTEX3DV>getFunction(b"glVertex3dv")
    cglVertex3dv(v)

cdef void GetglVertex3f(GLfloat x, GLfloat y, GLfloat z):
    global cglVertex3f
    cglVertex3f = <GL_VERTEX3F>getFunction(b"glVertex3f")
    cglVertex3f(x, y, z)

cdef void GetglVertex3fv(const GLfloat *v):
    global cglVertex3fv
    cglVertex3fv = <GL_VERTEX3FV>getFunction(b"glVertex3fv")
    cglVertex3fv(v)

cdef void GetglVertex3i(GLint x, GLint y, GLint z):
    global cglVertex3i
    cglVertex3i = <GL_VERTEX3I>getFunction(b"glVertex3i")
    cglVertex3i(x, y, z)

cdef void GetglVertex3iv(const GLint *v):
    global cglVertex3iv
    cglVertex3iv = <GL_VERTEX3IV>getFunction(b"glVertex3iv")
    cglVertex3iv(v)

cdef void GetglVertex3s(GLshort x, GLshort y, GLshort z):
    global cglVertex3s
    cglVertex3s = <GL_VERTEX3S>getFunction(b"glVertex3s")
    cglVertex3s(x, y, z)

cdef void GetglVertex3sv(const GLshort *v):
    global cglVertex3sv
    cglVertex3sv = <GL_VERTEX3SV>getFunction(b"glVertex3sv")
    cglVertex3sv(v)

cdef void GetglVertex4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    global cglVertex4d
    cglVertex4d = <GL_VERTEX4D>getFunction(b"glVertex4d")
    cglVertex4d(x, y, z, w)

cdef void GetglVertex4dv(const GLdouble *v):
    global cglVertex4dv
    cglVertex4dv = <GL_VERTEX4DV>getFunction(b"glVertex4dv")
    cglVertex4dv(v)

cdef void GetglVertex4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    global cglVertex4f
    cglVertex4f = <GL_VERTEX4F>getFunction(b"glVertex4f")
    cglVertex4f(x, y, z, w)

cdef void GetglVertex4fv(const GLfloat *v):
    global cglVertex4fv
    cglVertex4fv = <GL_VERTEX4FV>getFunction(b"glVertex4fv")
    cglVertex4fv(v)

cdef void GetglVertex4i(GLint x, GLint y, GLint z, GLint w):
    global cglVertex4i
    cglVertex4i = <GL_VERTEX4I>getFunction(b"glVertex4i")
    cglVertex4i(x, y, z, w)

cdef void GetglVertex4iv(const GLint *v):
    global cglVertex4iv
    cglVertex4iv = <GL_VERTEX4IV>getFunction(b"glVertex4iv")
    cglVertex4iv(v)

cdef void GetglVertex4s(GLshort x, GLshort y, GLshort z, GLshort w):
    global cglVertex4s
    cglVertex4s = <GL_VERTEX4S>getFunction(b"glVertex4s")
    cglVertex4s(x, y, z, w)

cdef void GetglVertex4sv(const GLshort *v):
    global cglVertex4sv
    cglVertex4sv = <GL_VERTEX4SV>getFunction(b"glVertex4sv")
    cglVertex4sv(v)

cdef void GetglClipPlane(GLenum plane, const GLdouble *equation):
    global cglClipPlane
    cglClipPlane = <GL_CLIP_PLANE>getFunction(b"glClipPlane")
    cglClipPlane(plane, equation)

cdef void GetglColorMaterial(GLenum face, GLenum mode):
    global cglColorMaterial
    cglColorMaterial = <GL_COLOR_MATERIAL>getFunction(b"glColorMaterial")
    cglColorMaterial(face, mode)

cdef void GetglFogf(GLenum pname, GLfloat param):
    global cglFogf
    cglFogf = <GL_FOGF>getFunction(b"glFogf")
    cglFogf(pname, param)

cdef void GetglFogfv(GLenum pname, const GLfloat *params):
    global cglFogfv
    cglFogfv = <GL_FOGFV>getFunction(b"glFogfv")
    cglFogfv(pname, params)

cdef void GetglFogi(GLenum pname, GLint param):
    global cglFogi
    cglFogi = <GL_FOGI>getFunction(b"glFogi")
    cglFogi(pname, param)

cdef void GetglFogiv(GLenum pname, const GLint *params):
    global cglFogiv
    cglFogiv = <GL_FOGIV>getFunction(b"glFogiv")
    cglFogiv(pname, params)

cdef void GetglLightf(GLenum light, GLenum pname, GLfloat param):
    global cglLightf
    cglLightf = <GL_LIGHTF>getFunction(b"glLightf")
    cglLightf(light, pname, param)

cdef void GetglLightfv(GLenum light, GLenum pname, const GLfloat *params):
    global cglLightfv
    cglLightfv = <GL_LIGHTFV>getFunction(b"glLightfv")
    cglLightfv(light, pname, params)

cdef void GetglLighti(GLenum light, GLenum pname, GLint param):
    global cglLighti
    cglLighti = <GL_LIGHTI>getFunction(b"glLighti")
    cglLighti(light, pname, param)

cdef void GetglLightiv(GLenum light, GLenum pname, const GLint *params):
    global cglLightiv
    cglLightiv = <GL_LIGHTIV>getFunction(b"glLightiv")
    cglLightiv(light, pname, params)

cdef void GetglLightModelf(GLenum pname, GLfloat param):
    global cglLightModelf
    cglLightModelf = <GL_LIGHT_MODELF>getFunction(b"glLightModelf")
    cglLightModelf(pname, param)

cdef void GetglLightModelfv(GLenum pname, const GLfloat *params):
    global cglLightModelfv
    cglLightModelfv = <GL_LIGHT_MODELFV>getFunction(b"glLightModelfv")
    cglLightModelfv(pname, params)

cdef void GetglLightModeli(GLenum pname, GLint param):
    global cglLightModeli
    cglLightModeli = <GL_LIGHT_MODELI>getFunction(b"glLightModeli")
    cglLightModeli(pname, param)

cdef void GetglLightModeliv(GLenum pname, const GLint *params):
    global cglLightModeliv
    cglLightModeliv = <GL_LIGHT_MODELIV>getFunction(b"glLightModeliv")
    cglLightModeliv(pname, params)

cdef void GetglLineStipple(GLint factor, GLushort pattern):
    global cglLineStipple
    cglLineStipple = <GL_LINE_STIPPLE>getFunction(b"glLineStipple")
    cglLineStipple(factor, pattern)

cdef void GetglMaterialf(GLenum face, GLenum pname, GLfloat param):
    global cglMaterialf
    cglMaterialf = <GL_MATERIALF>getFunction(b"glMaterialf")
    cglMaterialf(face, pname, param)

cdef void GetglMaterialfv(GLenum face, GLenum pname, const GLfloat *params):
    global cglMaterialfv
    cglMaterialfv = <GL_MATERIALFV>getFunction(b"glMaterialfv")
    cglMaterialfv(face, pname, params)

cdef void GetglMateriali(GLenum face, GLenum pname, GLint param):
    global cglMateriali
    cglMateriali = <GL_MATERIALI>getFunction(b"glMateriali")
    cglMateriali(face, pname, param)

cdef void GetglMaterialiv(GLenum face, GLenum pname, const GLint *params):
    global cglMaterialiv
    cglMaterialiv = <GL_MATERIALIV>getFunction(b"glMaterialiv")
    cglMaterialiv(face, pname, params)

cdef void GetglPolygonStipple(const GLubyte *mask):
    global cglPolygonStipple
    cglPolygonStipple = <GL_POLYGON_STIPPLE>getFunction(b"glPolygonStipple")
    cglPolygonStipple(mask)

cdef void GetglShadeModel(GLenum mode):
    global cglShadeModel
    cglShadeModel = <GL_SHADE_MODEL>getFunction(b"glShadeModel")
    cglShadeModel(mode)

cdef void GetglTexEnvf(GLenum target, GLenum pname, GLfloat param):
    global cglTexEnvf
    cglTexEnvf = <GL_TEX_ENVF>getFunction(b"glTexEnvf")
    cglTexEnvf(target, pname, param)

cdef void GetglTexEnvfv(GLenum target, GLenum pname, const GLfloat *params):
    global cglTexEnvfv
    cglTexEnvfv = <GL_TEX_ENVFV>getFunction(b"glTexEnvfv")
    cglTexEnvfv(target, pname, params)

cdef void GetglTexEnvi(GLenum target, GLenum pname, GLint param):
    global cglTexEnvi
    cglTexEnvi = <GL_TEX_ENVI>getFunction(b"glTexEnvi")
    cglTexEnvi(target, pname, param)

cdef void GetglTexEnviv(GLenum target, GLenum pname, const GLint *params):
    global cglTexEnviv
    cglTexEnviv = <GL_TEX_ENVIV>getFunction(b"glTexEnviv")
    cglTexEnviv(target, pname, params)

cdef void GetglTexGend(GLenum coord, GLenum pname, GLdouble param):
    global cglTexGend
    cglTexGend = <GL_TEX_GEND>getFunction(b"glTexGend")
    cglTexGend(coord, pname, param)

cdef void GetglTexGendv(GLenum coord, GLenum pname, const GLdouble *params):
    global cglTexGendv
    cglTexGendv = <GL_TEX_GENDV>getFunction(b"glTexGendv")
    cglTexGendv(coord, pname, params)

cdef void GetglTexGenf(GLenum coord, GLenum pname, GLfloat param):
    global cglTexGenf
    cglTexGenf = <GL_TEX_GENF>getFunction(b"glTexGenf")
    cglTexGenf(coord, pname, param)

cdef void GetglTexGenfv(GLenum coord, GLenum pname, const GLfloat *params):
    global cglTexGenfv
    cglTexGenfv = <GL_TEX_GENFV>getFunction(b"glTexGenfv")
    cglTexGenfv(coord, pname, params)

cdef void GetglTexGeni(GLenum coord, GLenum pname, GLint param):
    global cglTexGeni
    cglTexGeni = <GL_TEX_GENI>getFunction(b"glTexGeni")
    cglTexGeni(coord, pname, param)

cdef void GetglTexGeniv(GLenum coord, GLenum pname, const GLint *params):
    global cglTexGeniv
    cglTexGeniv = <GL_TEX_GENIV>getFunction(b"glTexGeniv")
    cglTexGeniv(coord, pname, params)

cdef void GetglFeedbackBuffer(GLsizei size, GLenum type, GLfloat *buffer):
    global cglFeedbackBuffer
    cglFeedbackBuffer = <GL_FEEDBACK_BUFFER>getFunction(b"glFeedbackBuffer")
    cglFeedbackBuffer(size, type, buffer)

cdef void GetglSelectBuffer(GLsizei size, GLuint *buffer):
    global cglSelectBuffer
    cglSelectBuffer = <GL_SELECT_BUFFER>getFunction(b"glSelectBuffer")
    cglSelectBuffer(size, buffer)

cdef GLint GetglRenderMode(GLenum mode):
    global cglRenderMode
    cglRenderMode = <GL_RENDER_MODE>getFunction(b"glRenderMode")
    cglRenderMode(mode)

cdef void GetglInitNames():
    global cglInitNames
    cglInitNames = <GL_INIT_NAMES>getFunction(b"glInitNames")
    cglInitNames()

cdef void GetglLoadName(GLuint name):
    global cglLoadName
    cglLoadName = <GL_LOAD_NAME>getFunction(b"glLoadName")
    cglLoadName(name)

cdef void GetglPassThrough(GLfloat token):
    global cglPassThrough
    cglPassThrough = <GL_PASS_THROUGH>getFunction(b"glPassThrough")
    cglPassThrough(token)

cdef void GetglPopName():
    global cglPopName
    cglPopName = <GL_POP_NAME>getFunction(b"glPopName")
    cglPopName()

cdef void GetglPushName(GLuint name):
    global cglPushName
    cglPushName = <GL_PUSH_NAME>getFunction(b"glPushName")
    cglPushName(name)

cdef void GetglClearAccum(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    global cglClearAccum
    cglClearAccum = <GL_CLEAR_ACCUM>getFunction(b"glClearAccum")
    cglClearAccum(red, green, blue, alpha)

cdef void GetglClearIndex(GLfloat c):
    global cglClearIndex
    cglClearIndex = <GL_CLEAR_INDEX>getFunction(b"glClearIndex")
    cglClearIndex(c)

cdef void GetglIndexMask(GLuint mask):
    global cglIndexMask
    cglIndexMask = <GL_INDEX_MASK>getFunction(b"glIndexMask")
    cglIndexMask(mask)

cdef void GetglAccum(GLenum op, GLfloat value):
    global cglAccum
    cglAccum = <GL_ACCUM>getFunction(b"glAccum")
    cglAccum(op, value)

cdef void GetglPopAttrib():
    global cglPopAttrib
    cglPopAttrib = <GL_POP_ATTRIB>getFunction(b"glPopAttrib")
    cglPopAttrib()

cdef void GetglPushAttrib(GLbitfield mask):
    global cglPushAttrib
    cglPushAttrib = <GL_PUSH_ATTRIB>getFunction(b"glPushAttrib")
    cglPushAttrib(mask)

cdef void GetglMap1d(GLenum target, GLdouble u1, GLdouble u2, GLint stride, GLint order, const GLdouble *points):
    global cglMap1d
    cglMap1d = <GL_MAP1D>getFunction(b"glMap1d")
    cglMap1d(target, u1, u2, stride, order, points)

cdef void GetglMap1f(GLenum target, GLfloat u1, GLfloat u2, GLint stride, GLint order, const GLfloat *points):
    global cglMap1f
    cglMap1f = <GL_MAP1F>getFunction(b"glMap1f")
    cglMap1f(target, u1, u2, stride, order, points)

cdef void GetglMap2d(GLenum target, GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint vstride, GLint vorder, const GLdouble *points):
    global cglMap2d
    cglMap2d = <GL_MAP2D>getFunction(b"glMap2d")
    cglMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)

cdef void GetglMap2f(GLenum target, GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride, GLint vorder, const GLfloat *points):
    global cglMap2f
    cglMap2f = <GL_MAP2F>getFunction(b"glMap2f")
    cglMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)

cdef void GetglMapGrid1d(GLint un, GLdouble u1, GLdouble u2):
    global cglMapGrid1d
    cglMapGrid1d = <GL_MAP_GRID1D>getFunction(b"glMapGrid1d")
    cglMapGrid1d(un, u1, u2)

cdef void GetglMapGrid1f(GLint un, GLfloat u1, GLfloat u2):
    global cglMapGrid1f
    cglMapGrid1f = <GL_MAP_GRID1F>getFunction(b"glMapGrid1f")
    cglMapGrid1f(un, u1, u2)

cdef void GetglMapGrid2d(GLint un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2):
    global cglMapGrid2d
    cglMapGrid2d = <GL_MAP_GRID2D>getFunction(b"glMapGrid2d")
    cglMapGrid2d(un, u1, u2, vn, v1, v2)

cdef void GetglMapGrid2f(GLint un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2):
    global cglMapGrid2f
    cglMapGrid2f = <GL_MAP_GRID2F>getFunction(b"glMapGrid2f")
    cglMapGrid2f(un, u1, u2, vn, v1, v2)

cdef void GetglEvalCoord1d(GLdouble u):
    global cglEvalCoord1d
    cglEvalCoord1d = <GL_EVAL_COORD1D>getFunction(b"glEvalCoord1d")
    cglEvalCoord1d(u)

cdef void GetglEvalCoord1dv(const GLdouble *u):
    global cglEvalCoord1dv
    cglEvalCoord1dv = <GL_EVAL_COORD1DV>getFunction(b"glEvalCoord1dv")
    cglEvalCoord1dv(u)

cdef void GetglEvalCoord1f(GLfloat u):
    global cglEvalCoord1f
    cglEvalCoord1f = <GL_EVAL_COORD1F>getFunction(b"glEvalCoord1f")
    cglEvalCoord1f(u)

cdef void GetglEvalCoord1fv(const GLfloat *u):
    global cglEvalCoord1fv
    cglEvalCoord1fv = <GL_EVAL_COORD1FV>getFunction(b"glEvalCoord1fv")
    cglEvalCoord1fv(u)

cdef void GetglEvalCoord2d(GLdouble u, GLdouble v):
    global cglEvalCoord2d
    cglEvalCoord2d = <GL_EVAL_COORD2D>getFunction(b"glEvalCoord2d")
    cglEvalCoord2d(u, v)

cdef void GetglEvalCoord2dv(const GLdouble *u):
    global cglEvalCoord2dv
    cglEvalCoord2dv = <GL_EVAL_COORD2DV>getFunction(b"glEvalCoord2dv")
    cglEvalCoord2dv(u)

cdef void GetglEvalCoord2f(GLfloat u, GLfloat v):
    global cglEvalCoord2f
    cglEvalCoord2f = <GL_EVAL_COORD2F>getFunction(b"glEvalCoord2f")
    cglEvalCoord2f(u, v)

cdef void GetglEvalCoord2fv(const GLfloat *u):
    global cglEvalCoord2fv
    cglEvalCoord2fv = <GL_EVAL_COORD2FV>getFunction(b"glEvalCoord2fv")
    cglEvalCoord2fv(u)

cdef void GetglEvalMesh1(GLenum mode, GLint i1, GLint i2):
    global cglEvalMesh1
    cglEvalMesh1 = <GL_EVAL_MESH1>getFunction(b"glEvalMesh1")
    cglEvalMesh1(mode, i1, i2)

cdef void GetglEvalPoint1(GLint i):
    global cglEvalPoint1
    cglEvalPoint1 = <GL_EVAL_POINT1>getFunction(b"glEvalPoint1")
    cglEvalPoint1(i)

cdef void GetglEvalMesh2(GLenum mode, GLint i1, GLint i2, GLint j1, GLint j2):
    global cglEvalMesh2
    cglEvalMesh2 = <GL_EVAL_MESH2>getFunction(b"glEvalMesh2")
    cglEvalMesh2(mode, i1, i2, j1, j2)

cdef void GetglEvalPoint2(GLint i, GLint j):
    global cglEvalPoint2
    cglEvalPoint2 = <GL_EVAL_POINT2>getFunction(b"glEvalPoint2")
    cglEvalPoint2(i, j)

cdef void GetglAlphaFunc(GLenum func, GLfloat ref):
    global cglAlphaFunc
    cglAlphaFunc = <GL_ALPHA_FUNC>getFunction(b"glAlphaFunc")
    cglAlphaFunc(func, ref)

cdef void GetglPixelZoom(GLfloat xfactor, GLfloat yfactor):
    global cglPixelZoom
    cglPixelZoom = <GL_PIXEL_ZOOM>getFunction(b"glPixelZoom")
    cglPixelZoom(xfactor, yfactor)

cdef void GetglPixelTransferf(GLenum pname, GLfloat param):
    global cglPixelTransferf
    cglPixelTransferf = <GL_PIXEL_TRANSFERF>getFunction(b"glPixelTransferf")
    cglPixelTransferf(pname, param)

cdef void GetglPixelTransferi(GLenum pname, GLint param):
    global cglPixelTransferi
    cglPixelTransferi = <GL_PIXEL_TRANSFERI>getFunction(b"glPixelTransferi")
    cglPixelTransferi(pname, param)

cdef void GetglPixelMapfv(GLenum map, GLsizei mapsize, const GLfloat *values):
    global cglPixelMapfv
    cglPixelMapfv = <GL_PIXEL_MAPFV>getFunction(b"glPixelMapfv")
    cglPixelMapfv(map, mapsize, values)

cdef void GetglPixelMapuiv(GLenum map, GLsizei mapsize, const GLuint *values):
    global cglPixelMapuiv
    cglPixelMapuiv = <GL_PIXEL_MAPUIV>getFunction(b"glPixelMapuiv")
    cglPixelMapuiv(map, mapsize, values)

cdef void GetglPixelMapusv(GLenum map, GLsizei mapsize, const GLushort *values):
    global cglPixelMapusv
    cglPixelMapusv = <GL_PIXEL_MAPUSV>getFunction(b"glPixelMapusv")
    cglPixelMapusv(map, mapsize, values)

cdef void GetglCopyPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum type):
    global cglCopyPixels
    cglCopyPixels = <GL_COPY_PIXELS>getFunction(b"glCopyPixels")
    cglCopyPixels(x, y, width, height, type)

cdef void GetglDrawPixels(GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    global cglDrawPixels
    cglDrawPixels = <GL_DRAW_PIXELS>getFunction(b"glDrawPixels")
    cglDrawPixels(width, height, format, type, pixels)

cdef void GetglGetClipPlane(GLenum plane, GLdouble *equation):
    global cglGetClipPlane
    cglGetClipPlane = <GL_GET_CLIP_PLANE>getFunction(b"glGetClipPlane")
    cglGetClipPlane(plane, equation)

cdef void GetglGetLightfv(GLenum light, GLenum pname, GLfloat *params):
    global cglGetLightfv
    cglGetLightfv = <GL_GET_LIGHTFV>getFunction(b"glGetLightfv")
    cglGetLightfv(light, pname, params)

cdef void GetglGetLightiv(GLenum light, GLenum pname, GLint *params):
    global cglGetLightiv
    cglGetLightiv = <GL_GET_LIGHTIV>getFunction(b"glGetLightiv")
    cglGetLightiv(light, pname, params)

cdef void GetglGetMapdv(GLenum target, GLenum query, GLdouble *v):
    global cglGetMapdv
    cglGetMapdv = <GL_GET_MAPDV>getFunction(b"glGetMapdv")
    cglGetMapdv(target, query, v)

cdef void GetglGetMapfv(GLenum target, GLenum query, GLfloat *v):
    global cglGetMapfv
    cglGetMapfv = <GL_GET_MAPFV>getFunction(b"glGetMapfv")
    cglGetMapfv(target, query, v)

cdef void GetglGetMapiv(GLenum target, GLenum query, GLint *v):
    global cglGetMapiv
    cglGetMapiv = <GL_GET_MAPIV>getFunction(b"glGetMapiv")
    cglGetMapiv(target, query, v)

cdef void GetglGetMaterialfv(GLenum face, GLenum pname, GLfloat *params):
    global cglGetMaterialfv
    cglGetMaterialfv = <GL_GET_MATERIALFV>getFunction(b"glGetMaterialfv")
    cglGetMaterialfv(face, pname, params)

cdef void GetglGetMaterialiv(GLenum face, GLenum pname, GLint *params):
    global cglGetMaterialiv
    cglGetMaterialiv = <GL_GET_MATERIALIV>getFunction(b"glGetMaterialiv")
    cglGetMaterialiv(face, pname, params)

cdef void GetglGetPixelMapfv(GLenum map, GLfloat *values):
    global cglGetPixelMapfv
    cglGetPixelMapfv = <GL_GET_PIXEL_MAPFV>getFunction(b"glGetPixelMapfv")
    cglGetPixelMapfv(map, values)

cdef void GetglGetPixelMapuiv(GLenum map, GLuint *values):
    global cglGetPixelMapuiv
    cglGetPixelMapuiv = <GL_GET_PIXEL_MAPUIV>getFunction(b"glGetPixelMapuiv")
    cglGetPixelMapuiv(map, values)

cdef void GetglGetPixelMapusv(GLenum map, GLushort *values):
    global cglGetPixelMapusv
    cglGetPixelMapusv = <GL_GET_PIXEL_MAPUSV>getFunction(b"glGetPixelMapusv")
    cglGetPixelMapusv(map, values)

cdef void GetglGetPolygonStipple(GLubyte *mask):
    global cglGetPolygonStipple
    cglGetPolygonStipple = <GL_GET_POLYGON_STIPPLE>getFunction(b"glGetPolygonStipple")
    cglGetPolygonStipple(mask)

cdef void GetglGetTexEnvfv(GLenum target, GLenum pname, GLfloat *params):
    global cglGetTexEnvfv
    cglGetTexEnvfv = <GL_GET_TEX_ENVFV>getFunction(b"glGetTexEnvfv")
    cglGetTexEnvfv(target, pname, params)

cdef void GetglGetTexEnviv(GLenum target, GLenum pname, GLint *params):
    global cglGetTexEnviv
    cglGetTexEnviv = <GL_GET_TEX_ENVIV>getFunction(b"glGetTexEnviv")
    cglGetTexEnviv(target, pname, params)

cdef void GetglGetTexGendv(GLenum coord, GLenum pname, GLdouble *params):
    global cglGetTexGendv
    cglGetTexGendv = <GL_GET_TEX_GENDV>getFunction(b"glGetTexGendv")
    cglGetTexGendv(coord, pname, params)

cdef void GetglGetTexGenfv(GLenum coord, GLenum pname, GLfloat *params):
    global cglGetTexGenfv
    cglGetTexGenfv = <GL_GET_TEX_GENFV>getFunction(b"glGetTexGenfv")
    cglGetTexGenfv(coord, pname, params)

cdef void GetglGetTexGeniv(GLenum coord, GLenum pname, GLint *params):
    global cglGetTexGeniv
    cglGetTexGeniv = <GL_GET_TEX_GENIV>getFunction(b"glGetTexGeniv")
    cglGetTexGeniv(coord, pname, params)

cdef GLboolean GetglIsList(GLuint list):
    global cglIsList
    cglIsList = <GL_IS_LIST>getFunction(b"glIsList")
    cglIsList(list)

cdef void GetglFrustum(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar):
    global cglFrustum
    cglFrustum = <GL_FRUSTUM>getFunction(b"glFrustum")
    cglFrustum(left, right, bottom, top, zNear, zFar)

cdef void GetglLoadIdentity():
    global cglLoadIdentity
    cglLoadIdentity = <GL_LOAD_IDENTITY>getFunction(b"glLoadIdentity")
    cglLoadIdentity()

cdef void GetglLoadMatrixf(const GLfloat *m):
    global cglLoadMatrixf
    cglLoadMatrixf = <GL_LOAD_MATRIXF>getFunction(b"glLoadMatrixf")
    cglLoadMatrixf(m)

cdef void GetglLoadMatrixd(const GLdouble *m):
    global cglLoadMatrixd
    cglLoadMatrixd = <GL_LOAD_MATRIXD>getFunction(b"glLoadMatrixd")
    cglLoadMatrixd(m)

cdef void GetglMatrixMode(GLenum mode):
    global cglMatrixMode
    cglMatrixMode = <GL_MATRIX_MODE>getFunction(b"glMatrixMode")
    cglMatrixMode(mode)

cdef void GetglMultMatrixf(const GLfloat *m):
    global cglMultMatrixf
    cglMultMatrixf = <GL_MULT_MATRIXF>getFunction(b"glMultMatrixf")
    cglMultMatrixf(m)

cdef void GetglMultMatrixd(const GLdouble *m):
    global cglMultMatrixd
    cglMultMatrixd = <GL_MULT_MATRIXD>getFunction(b"glMultMatrixd")
    cglMultMatrixd(m)

cdef void GetglOrtho(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar):
    global cglOrtho
    cglOrtho = <GL_ORTHO>getFunction(b"glOrtho")
    cglOrtho(left, right, bottom, top, zNear, zFar)

cdef void GetglPopMatrix():
    global cglPopMatrix
    cglPopMatrix = <GL_POP_MATRIX>getFunction(b"glPopMatrix")
    cglPopMatrix()

cdef void GetglPushMatrix():
    global cglPushMatrix
    cglPushMatrix = <GL_PUSH_MATRIX>getFunction(b"glPushMatrix")
    cglPushMatrix()

cdef void GetglRotated(GLdouble angle, GLdouble x, GLdouble y, GLdouble z):
    global cglRotated
    cglRotated = <GL_ROTATED>getFunction(b"glRotated")
    cglRotated(angle, x, y, z)

cdef void GetglRotatef(GLfloat angle, GLfloat x, GLfloat y, GLfloat z):
    global cglRotatef
    cglRotatef = <GL_ROTATEF>getFunction(b"glRotatef")
    cglRotatef(angle, x, y, z)

cdef void GetglScaled(GLdouble x, GLdouble y, GLdouble z):
    global cglScaled
    cglScaled = <GL_SCALED>getFunction(b"glScaled")
    cglScaled(x, y, z)

cdef void GetglScalef(GLfloat x, GLfloat y, GLfloat z):
    global cglScalef
    cglScalef = <GL_SCALEF>getFunction(b"glScalef")
    cglScalef(x, y, z)

cdef void GetglTranslated(GLdouble x, GLdouble y, GLdouble z):
    global cglTranslated
    cglTranslated = <GL_TRANSLATED>getFunction(b"glTranslated")
    cglTranslated(x, y, z)

cdef void GetglTranslatef(GLfloat x, GLfloat y, GLfloat z):
    global cglTranslatef
    cglTranslatef = <GL_TRANSLATEF>getFunction(b"glTranslatef")
    cglTranslatef(x, y, z)

cglCullFace = GetglCullFace
cglFrontFace = GetglFrontFace
cglHint = GetglHint
cglLineWidth = GetglLineWidth
cglPointSize = GetglPointSize
cglPolygonMode = GetglPolygonMode
cglScissor = GetglScissor
cglTexParameterf = GetglTexParameterf
cglTexParameterfv = GetglTexParameterfv
cglTexParameteri = GetglTexParameteri
cglTexParameteriv = GetglTexParameteriv
cglTexImage1D = GetglTexImage1D
cglTexImage2D = GetglTexImage2D
cglDrawBuffer = GetglDrawBuffer
cglClear = GetglClear
cglClearColor = GetglClearColor
cglClearStencil = GetglClearStencil
cglClearDepth = GetglClearDepth
cglStencilMask = GetglStencilMask
cglColorMask = GetglColorMask
cglDepthMask = GetglDepthMask
cglDisable = GetglDisable
cglEnable = GetglEnable
cglFinish = GetglFinish
cglFlush = GetglFlush
cglBlendFunc = GetglBlendFunc
cglLogicOp = GetglLogicOp
cglStencilFunc = GetglStencilFunc
cglStencilOp = GetglStencilOp
cglDepthFunc = GetglDepthFunc
cglPixelStoref = GetglPixelStoref
cglPixelStorei = GetglPixelStorei
cglReadBuffer = GetglReadBuffer
cglReadPixels = GetglReadPixels
cglGetBooleanv = GetglGetBooleanv
cglGetDoublev = GetglGetDoublev
cglGetError = GetglGetError
cglGetFloatv = GetglGetFloatv
cglGetIntegerv = GetglGetIntegerv
cglGetString = GetglGetString
cglGetTexImage = GetglGetTexImage
cglGetTexParameterfv = GetglGetTexParameterfv
cglGetTexParameteriv = GetglGetTexParameteriv
cglGetTexLevelParameterfv = GetglGetTexLevelParameterfv
cglGetTexLevelParameteriv = GetglGetTexLevelParameteriv
cglIsEnabled = GetglIsEnabled
cglDepthRange = GetglDepthRange
cglViewport = GetglViewport
cglNewList = GetglNewList
cglEndList = GetglEndList
cglCallList = GetglCallList
cglCallLists = GetglCallLists
cglDeleteLists = GetglDeleteLists
cglGenLists = GetglGenLists
cglListBase = GetglListBase
cglBegin = GetglBegin
cglBitmap = GetglBitmap
cglColor3b = GetglColor3b
cglColor3bv = GetglColor3bv
cglColor3d = GetglColor3d
cglColor3dv = GetglColor3dv
cglColor3f = GetglColor3f
cglColor3fv = GetglColor3fv
cglColor3i = GetglColor3i
cglColor3iv = GetglColor3iv
cglColor3s = GetglColor3s
cglColor3sv = GetglColor3sv
cglColor3ub = GetglColor3ub
cglColor3ubv = GetglColor3ubv
cglColor3ui = GetglColor3ui
cglColor3uiv = GetglColor3uiv
cglColor3us = GetglColor3us
cglColor3usv = GetglColor3usv
cglColor4b = GetglColor4b
cglColor4bv = GetglColor4bv
cglColor4d = GetglColor4d
cglColor4dv = GetglColor4dv
cglColor4f = GetglColor4f
cglColor4fv = GetglColor4fv
cglColor4i = GetglColor4i
cglColor4iv = GetglColor4iv
cglColor4s = GetglColor4s
cglColor4sv = GetglColor4sv
cglColor4ub = GetglColor4ub
cglColor4ubv = GetglColor4ubv
cglColor4ui = GetglColor4ui
cglColor4uiv = GetglColor4uiv
cglColor4us = GetglColor4us
cglColor4usv = GetglColor4usv
cglEdgeFlag = GetglEdgeFlag
cglEdgeFlagv = GetglEdgeFlagv
cglEnd = GetglEnd
cglIndexd = GetglIndexd
cglIndexdv = GetglIndexdv
cglIndexf = GetglIndexf
cglIndexfv = GetglIndexfv
cglIndexi = GetglIndexi
cglIndexiv = GetglIndexiv
cglIndexs = GetglIndexs
cglIndexsv = GetglIndexsv
cglNormal3b = GetglNormal3b
cglNormal3bv = GetglNormal3bv
cglNormal3d = GetglNormal3d
cglNormal3dv = GetglNormal3dv
cglNormal3f = GetglNormal3f
cglNormal3fv = GetglNormal3fv
cglNormal3i = GetglNormal3i
cglNormal3iv = GetglNormal3iv
cglNormal3s = GetglNormal3s
cglNormal3sv = GetglNormal3sv
cglRasterPos2d = GetglRasterPos2d
cglRasterPos2dv = GetglRasterPos2dv
cglRasterPos2f = GetglRasterPos2f
cglRasterPos2fv = GetglRasterPos2fv
cglRasterPos2i = GetglRasterPos2i
cglRasterPos2iv = GetglRasterPos2iv
cglRasterPos2s = GetglRasterPos2s
cglRasterPos2sv = GetglRasterPos2sv
cglRasterPos3d = GetglRasterPos3d
cglRasterPos3dv = GetglRasterPos3dv
cglRasterPos3f = GetglRasterPos3f
cglRasterPos3fv = GetglRasterPos3fv
cglRasterPos3i = GetglRasterPos3i
cglRasterPos3iv = GetglRasterPos3iv
cglRasterPos3s = GetglRasterPos3s
cglRasterPos3sv = GetglRasterPos3sv
cglRasterPos4d = GetglRasterPos4d
cglRasterPos4dv = GetglRasterPos4dv
cglRasterPos4f = GetglRasterPos4f
cglRasterPos4fv = GetglRasterPos4fv
cglRasterPos4i = GetglRasterPos4i
cglRasterPos4iv = GetglRasterPos4iv
cglRasterPos4s = GetglRasterPos4s
cglRasterPos4sv = GetglRasterPos4sv
cglRectd = GetglRectd
cglRectdv = GetglRectdv
cglRectf = GetglRectf
cglRectfv = GetglRectfv
cglRecti = GetglRecti
cglRectiv = GetglRectiv
cglRects = GetglRects
cglRectsv = GetglRectsv
cglTexCoord1d = GetglTexCoord1d
cglTexCoord1dv = GetglTexCoord1dv
cglTexCoord1f = GetglTexCoord1f
cglTexCoord1fv = GetglTexCoord1fv
cglTexCoord1i = GetglTexCoord1i
cglTexCoord1iv = GetglTexCoord1iv
cglTexCoord1s = GetglTexCoord1s
cglTexCoord1sv = GetglTexCoord1sv
cglTexCoord2d = GetglTexCoord2d
cglTexCoord2dv = GetglTexCoord2dv
cglTexCoord2f = GetglTexCoord2f
cglTexCoord2fv = GetglTexCoord2fv
cglTexCoord2i = GetglTexCoord2i
cglTexCoord2iv = GetglTexCoord2iv
cglTexCoord2s = GetglTexCoord2s
cglTexCoord2sv = GetglTexCoord2sv
cglTexCoord3d = GetglTexCoord3d
cglTexCoord3dv = GetglTexCoord3dv
cglTexCoord3f = GetglTexCoord3f
cglTexCoord3fv = GetglTexCoord3fv
cglTexCoord3i = GetglTexCoord3i
cglTexCoord3iv = GetglTexCoord3iv
cglTexCoord3s = GetglTexCoord3s
cglTexCoord3sv = GetglTexCoord3sv
cglTexCoord4d = GetglTexCoord4d
cglTexCoord4dv = GetglTexCoord4dv
cglTexCoord4f = GetglTexCoord4f
cglTexCoord4fv = GetglTexCoord4fv
cglTexCoord4i = GetglTexCoord4i
cglTexCoord4iv = GetglTexCoord4iv
cglTexCoord4s = GetglTexCoord4s
cglTexCoord4sv = GetglTexCoord4sv
cglVertex2d = GetglVertex2d
cglVertex2dv = GetglVertex2dv
cglVertex2f = GetglVertex2f
cglVertex2fv = GetglVertex2fv
cglVertex2i = GetglVertex2i
cglVertex2iv = GetglVertex2iv
cglVertex2s = GetglVertex2s
cglVertex2sv = GetglVertex2sv
cglVertex3d = GetglVertex3d
cglVertex3dv = GetglVertex3dv
cglVertex3f = GetglVertex3f
cglVertex3fv = GetglVertex3fv
cglVertex3i = GetglVertex3i
cglVertex3iv = GetglVertex3iv
cglVertex3s = GetglVertex3s
cglVertex3sv = GetglVertex3sv
cglVertex4d = GetglVertex4d
cglVertex4dv = GetglVertex4dv
cglVertex4f = GetglVertex4f
cglVertex4fv = GetglVertex4fv
cglVertex4i = GetglVertex4i
cglVertex4iv = GetglVertex4iv
cglVertex4s = GetglVertex4s
cglVertex4sv = GetglVertex4sv
cglClipPlane = GetglClipPlane
cglColorMaterial = GetglColorMaterial
cglFogf = GetglFogf
cglFogfv = GetglFogfv
cglFogi = GetglFogi
cglFogiv = GetglFogiv
cglLightf = GetglLightf
cglLightfv = GetglLightfv
cglLighti = GetglLighti
cglLightiv = GetglLightiv
cglLightModelf = GetglLightModelf
cglLightModelfv = GetglLightModelfv
cglLightModeli = GetglLightModeli
cglLightModeliv = GetglLightModeliv
cglLineStipple = GetglLineStipple
cglMaterialf = GetglMaterialf
cglMaterialfv = GetglMaterialfv
cglMateriali = GetglMateriali
cglMaterialiv = GetglMaterialiv
cglPolygonStipple = GetglPolygonStipple
cglShadeModel = GetglShadeModel
cglTexEnvf = GetglTexEnvf
cglTexEnvfv = GetglTexEnvfv
cglTexEnvi = GetglTexEnvi
cglTexEnviv = GetglTexEnviv
cglTexGend = GetglTexGend
cglTexGendv = GetglTexGendv
cglTexGenf = GetglTexGenf
cglTexGenfv = GetglTexGenfv
cglTexGeni = GetglTexGeni
cglTexGeniv = GetglTexGeniv
cglFeedbackBuffer = GetglFeedbackBuffer
cglSelectBuffer = GetglSelectBuffer
cglRenderMode = GetglRenderMode
cglInitNames = GetglInitNames
cglLoadName = GetglLoadName
cglPassThrough = GetglPassThrough
cglPopName = GetglPopName
cglPushName = GetglPushName
cglClearAccum = GetglClearAccum
cglClearIndex = GetglClearIndex
cglIndexMask = GetglIndexMask
cglAccum = GetglAccum
cglPopAttrib = GetglPopAttrib
cglPushAttrib = GetglPushAttrib
cglMap1d = GetglMap1d
cglMap1f = GetglMap1f
cglMap2d = GetglMap2d
cglMap2f = GetglMap2f
cglMapGrid1d = GetglMapGrid1d
cglMapGrid1f = GetglMapGrid1f
cglMapGrid2d = GetglMapGrid2d
cglMapGrid2f = GetglMapGrid2f
cglEvalCoord1d = GetglEvalCoord1d
cglEvalCoord1dv = GetglEvalCoord1dv
cglEvalCoord1f = GetglEvalCoord1f
cglEvalCoord1fv = GetglEvalCoord1fv
cglEvalCoord2d = GetglEvalCoord2d
cglEvalCoord2dv = GetglEvalCoord2dv
cglEvalCoord2f = GetglEvalCoord2f
cglEvalCoord2fv = GetglEvalCoord2fv
cglEvalMesh1 = GetglEvalMesh1
cglEvalPoint1 = GetglEvalPoint1
cglEvalMesh2 = GetglEvalMesh2
cglEvalPoint2 = GetglEvalPoint2
cglAlphaFunc = GetglAlphaFunc
cglPixelZoom = GetglPixelZoom
cglPixelTransferf = GetglPixelTransferf
cglPixelTransferi = GetglPixelTransferi
cglPixelMapfv = GetglPixelMapfv
cglPixelMapuiv = GetglPixelMapuiv
cglPixelMapusv = GetglPixelMapusv
cglCopyPixels = GetglCopyPixels
cglDrawPixels = GetglDrawPixels
cglGetClipPlane = GetglGetClipPlane
cglGetLightfv = GetglGetLightfv
cglGetLightiv = GetglGetLightiv
cglGetMapdv = GetglGetMapdv
cglGetMapfv = GetglGetMapfv
cglGetMapiv = GetglGetMapiv
cglGetMaterialfv = GetglGetMaterialfv
cglGetMaterialiv = GetglGetMaterialiv
cglGetPixelMapfv = GetglGetPixelMapfv
cglGetPixelMapuiv = GetglGetPixelMapuiv
cglGetPixelMapusv = GetglGetPixelMapusv
cglGetPolygonStipple = GetglGetPolygonStipple
cglGetTexEnvfv = GetglGetTexEnvfv
cglGetTexEnviv = GetglGetTexEnviv
cglGetTexGendv = GetglGetTexGendv
cglGetTexGenfv = GetglGetTexGenfv
cglGetTexGeniv = GetglGetTexGeniv
cglIsList = GetglIsList
cglFrustum = GetglFrustum
cglLoadIdentity = GetglLoadIdentity
cglLoadMatrixf = GetglLoadMatrixf
cglLoadMatrixd = GetglLoadMatrixd
cglMatrixMode = GetglMatrixMode
cglMultMatrixf = GetglMultMatrixf
cglMultMatrixd = GetglMultMatrixd
cglOrtho = GetglOrtho
cglPopMatrix = GetglPopMatrix
cglPushMatrix = GetglPushMatrix
cglRotated = GetglRotated
cglRotatef = GetglRotatef
cglScaled = GetglScaled
cglScalef = GetglScalef
cglTranslated = GetglTranslated
cglTranslatef = GetglTranslatef


cpdef void glCullFace(GLenum mode):
    cglCullFace(mode)

cpdef void glFrontFace(GLenum mode):
    cglFrontFace(mode)

cpdef void glHint(GLenum target, GLenum mode):
    cglHint(target, mode)

cpdef void glLineWidth(GLfloat width):
    cglLineWidth(width)

cpdef void glPointSize(GLfloat size):
    cglPointSize(size)

cpdef void glPolygonMode(GLenum face, GLenum mode):
    cglPolygonMode(face, mode)

cpdef void glScissor(GLint x, GLint y, GLsizei width, GLsizei height):
    cglScissor(x, y, width, height)

cpdef void glTexParameterf(GLenum target, GLenum pname, GLfloat param):
    cglTexParameterf(target, pname, param)

cpdef void glTexParameterfv(GLenum target, GLenum pname, const GLfloat *params):
    cglTexParameterfv(target, pname, params)

cpdef void glTexParameteri(GLenum target, GLenum pname, GLint param):
    cglTexParameteri(target, pname, param)

cpdef void glTexParameteriv(GLenum target, GLenum pname, const GLint *params):
    cglTexParameteriv(target, pname, params)

cpdef void glTexImage1D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLint border, GLenum format, GLenum type, const void *pixels):
    cglTexImage1D(target, level, internalformat, width, border, format, type, pixels)

cpdef void glTexImage2D(GLenum target, GLint level, GLint internalformat, GLsizei width, GLsizei height, GLint border, GLenum format, GLenum type, const void *pixels):
    cglTexImage2D(target, level, internalformat, width, height, border, format, type, pixels)

cpdef void glDrawBuffer(GLenum buf):
    cglDrawBuffer(buf)

cpdef void glClear(GLbitfield mask):
    cglClear(mask)

cpdef void glClearColor(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    cglClearColor(red, green, blue, alpha)

cpdef void glClearStencil(GLint s):
    cglClearStencil(s)

cpdef void glClearDepth(GLdouble depth):
    cglClearDepth(depth)

cpdef void glStencilMask(GLuint mask):
    cglStencilMask(mask)

cpdef void glColorMask(GLboolean red, GLboolean green, GLboolean blue, GLboolean alpha):
    cglColorMask(red, green, blue, alpha)

cpdef void glDepthMask(GLboolean flag):
    cglDepthMask(flag)

cpdef void glDisable(GLenum cap):
    cglDisable(cap)

cpdef void glEnable(GLenum cap):
    cglEnable(cap)

cpdef void glFinish():
    cglFinish()

cpdef void glFlush():
    cglFlush()

cpdef void glBlendFunc(GLenum sfactor, GLenum dfactor):
    cglBlendFunc(sfactor, dfactor)

cpdef void glLogicOp(GLenum opcode):
    cglLogicOp(opcode)

cpdef void glStencilFunc(GLenum func, GLint ref, GLuint mask):
    cglStencilFunc(func, ref, mask)

cpdef void glStencilOp(GLenum fail, GLenum zfail, GLenum zpass):
    cglStencilOp(fail, zfail, zpass)

cpdef void glDepthFunc(GLenum func):
    cglDepthFunc(func)

cpdef void glPixelStoref(GLenum pname, GLfloat param):
    cglPixelStoref(pname, param)

cpdef void glPixelStorei(GLenum pname, GLint param):
    cglPixelStorei(pname, param)

cpdef void glReadBuffer(GLenum src):
    cglReadBuffer(src)

cpdef void glReadPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum format, GLenum type, void *pixels):
    cglReadPixels(x, y, width, height, format, type, pixels)

cpdef void glGetBooleanv(GLenum pname, GLboolean *data):
    cglGetBooleanv(pname, data)

cpdef void glGetDoublev(GLenum pname, GLdouble *data):
    cglGetDoublev(pname, data)

cpdef GLenum glGetError():
    cglGetError()

cpdef void glGetFloatv(GLenum pname, GLfloat *data):
    cglGetFloatv(pname, data)

cpdef void glGetIntegerv(GLenum pname, GLint *data):
    cglGetIntegerv(pname, data)

cpdef const GLubyte *glGetString(GLenum name):
    cglGetString(name)

cpdef void glGetTexImage(GLenum target, GLint level, GLenum format, GLenum type, void *pixels):
    cglGetTexImage(target, level, format, type, pixels)

cpdef void glGetTexParameterfv(GLenum target, GLenum pname, GLfloat *params):
    cglGetTexParameterfv(target, pname, params)

cpdef void glGetTexParameteriv(GLenum target, GLenum pname, GLint *params):
    cglGetTexParameteriv(target, pname, params)

cpdef void glGetTexLevelParameterfv(GLenum target, GLint level, GLenum pname, GLfloat *params):
    cglGetTexLevelParameterfv(target, level, pname, params)

cpdef void glGetTexLevelParameteriv(GLenum target, GLint level, GLenum pname, GLint *params):
    cglGetTexLevelParameteriv(target, level, pname, params)

cpdef GLboolean glIsEnabled(GLenum cap):
    cglIsEnabled(cap)

cpdef void glDepthRange(GLdouble n, GLdouble f):
    cglDepthRange(n, f)

cpdef void glViewport(GLint x, GLint y, GLsizei width, GLsizei height):
    cglViewport(x, y, width, height)

cpdef void glNewList(GLuint list, GLenum mode):
    cglNewList(list, mode)

cpdef void glEndList():
    cglEndList()

cpdef void glCallList(GLuint list):
    cglCallList(list)

cpdef void glCallLists(GLsizei n, GLenum type, const void *lists):
    cglCallLists(n, type, lists)

cpdef void glDeleteLists(GLuint list, GLsizei range):
    cglDeleteLists(list, range)

cpdef GLuint glGenLists(GLsizei range):
    cglGenLists(range)

cpdef void glListBase(GLuint base):
    cglListBase(base)

cpdef void glBegin(GLenum mode):
    cglBegin(mode)

cpdef void glBitmap(GLsizei width, GLsizei height, GLfloat xorig, GLfloat yorig, GLfloat xmove, GLfloat ymove, const GLubyte *bitmap):
    cglBitmap(width, height, xorig, yorig, xmove, ymove, bitmap)

cpdef void glColor3b(GLbyte red, GLbyte green, GLbyte blue):
    cglColor3b(red, green, blue)

cpdef void glColor3bv(const GLbyte *v):
    cglColor3bv(v)

cpdef void glColor3d(GLdouble red, GLdouble green, GLdouble blue):
    cglColor3d(red, green, blue)

cpdef void glColor3dv(const GLdouble *v):
    cglColor3dv(v)

cpdef void glColor3f(GLfloat red, GLfloat green, GLfloat blue):
    cglColor3f(red, green, blue)

cpdef void glColor3fv(const GLfloat *v):
    cglColor3fv(v)

cpdef void glColor3i(GLint red, GLint green, GLint blue):
    cglColor3i(red, green, blue)

cpdef void glColor3iv(const GLint *v):
    cglColor3iv(v)

cpdef void glColor3s(GLshort red, GLshort green, GLshort blue):
    cglColor3s(red, green, blue)

cpdef void glColor3sv(const GLshort *v):
    cglColor3sv(v)

cpdef void glColor3ub(GLubyte red, GLubyte green, GLubyte blue):
    cglColor3ub(red, green, blue)

cpdef void glColor3ubv(const GLubyte *v):
    cglColor3ubv(v)

cpdef void glColor3ui(GLuint red, GLuint green, GLuint blue):
    cglColor3ui(red, green, blue)

cpdef void glColor3uiv(const GLuint *v):
    cglColor3uiv(v)

cpdef void glColor3us(GLushort red, GLushort green, GLushort blue):
    cglColor3us(red, green, blue)

cpdef void glColor3usv(const GLushort *v):
    cglColor3usv(v)

cpdef void glColor4b(GLbyte red, GLbyte green, GLbyte blue, GLbyte alpha):
    cglColor4b(red, green, blue, alpha)

cpdef void glColor4bv(const GLbyte *v):
    cglColor4bv(v)

cpdef void glColor4d(GLdouble red, GLdouble green, GLdouble blue, GLdouble alpha):
    cglColor4d(red, green, blue, alpha)

cpdef void glColor4dv(const GLdouble *v):
    cglColor4dv(v)

cpdef void glColor4f(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    cglColor4f(red, green, blue, alpha)

cpdef void glColor4fv(const GLfloat *v):
    cglColor4fv(v)

cpdef void glColor4i(GLint red, GLint green, GLint blue, GLint alpha):
    cglColor4i(red, green, blue, alpha)

cpdef void glColor4iv(const GLint *v):
    cglColor4iv(v)

cpdef void glColor4s(GLshort red, GLshort green, GLshort blue, GLshort alpha):
    cglColor4s(red, green, blue, alpha)

cpdef void glColor4sv(const GLshort *v):
    cglColor4sv(v)

cpdef void glColor4ub(GLubyte red, GLubyte green, GLubyte blue, GLubyte alpha):
    cglColor4ub(red, green, blue, alpha)

cpdef void glColor4ubv(const GLubyte *v):
    cglColor4ubv(v)

cpdef void glColor4ui(GLuint red, GLuint green, GLuint blue, GLuint alpha):
    cglColor4ui(red, green, blue, alpha)

cpdef void glColor4uiv(const GLuint *v):
    cglColor4uiv(v)

cpdef void glColor4us(GLushort red, GLushort green, GLushort blue, GLushort alpha):
    cglColor4us(red, green, blue, alpha)

cpdef void glColor4usv(const GLushort *v):
    cglColor4usv(v)

cpdef void glEdgeFlag(GLboolean flag):
    cglEdgeFlag(flag)

cpdef void glEdgeFlagv(const GLboolean *flag):
    cglEdgeFlagv(flag)

cpdef void glEnd():
    cglEnd()

cpdef void glIndexd(GLdouble c):
    cglIndexd(c)

cpdef void glIndexdv(const GLdouble *c):
    cglIndexdv(c)

cpdef void glIndexf(GLfloat c):
    cglIndexf(c)

cpdef void glIndexfv(const GLfloat *c):
    cglIndexfv(c)

cpdef void glIndexi(GLint c):
    cglIndexi(c)

cpdef void glIndexiv(const GLint *c):
    cglIndexiv(c)

cpdef void glIndexs(GLshort c):
    cglIndexs(c)

cpdef void glIndexsv(const GLshort *c):
    cglIndexsv(c)

cpdef void glNormal3b(GLbyte nx, GLbyte ny, GLbyte nz):
    cglNormal3b(nx, ny, nz)

cpdef void glNormal3bv(const GLbyte *v):
    cglNormal3bv(v)

cpdef void glNormal3d(GLdouble nx, GLdouble ny, GLdouble nz):
    cglNormal3d(nx, ny, nz)

cpdef void glNormal3dv(const GLdouble *v):
    cglNormal3dv(v)

cpdef void glNormal3f(GLfloat nx, GLfloat ny, GLfloat nz):
    cglNormal3f(nx, ny, nz)

cpdef void glNormal3fv(const GLfloat *v):
    cglNormal3fv(v)

cpdef void glNormal3i(GLint nx, GLint ny, GLint nz):
    cglNormal3i(nx, ny, nz)

cpdef void glNormal3iv(const GLint *v):
    cglNormal3iv(v)

cpdef void glNormal3s(GLshort nx, GLshort ny, GLshort nz):
    cglNormal3s(nx, ny, nz)

cpdef void glNormal3sv(const GLshort *v):
    cglNormal3sv(v)

cpdef void glRasterPos2d(GLdouble x, GLdouble y):
    cglRasterPos2d(x, y)

cpdef void glRasterPos2dv(const GLdouble *v):
    cglRasterPos2dv(v)

cpdef void glRasterPos2f(GLfloat x, GLfloat y):
    cglRasterPos2f(x, y)

cpdef void glRasterPos2fv(const GLfloat *v):
    cglRasterPos2fv(v)

cpdef void glRasterPos2i(GLint x, GLint y):
    cglRasterPos2i(x, y)

cpdef void glRasterPos2iv(const GLint *v):
    cglRasterPos2iv(v)

cpdef void glRasterPos2s(GLshort x, GLshort y):
    cglRasterPos2s(x, y)

cpdef void glRasterPos2sv(const GLshort *v):
    cglRasterPos2sv(v)

cpdef void glRasterPos3d(GLdouble x, GLdouble y, GLdouble z):
    cglRasterPos3d(x, y, z)

cpdef void glRasterPos3dv(const GLdouble *v):
    cglRasterPos3dv(v)

cpdef void glRasterPos3f(GLfloat x, GLfloat y, GLfloat z):
    cglRasterPos3f(x, y, z)

cpdef void glRasterPos3fv(const GLfloat *v):
    cglRasterPos3fv(v)

cpdef void glRasterPos3i(GLint x, GLint y, GLint z):
    cglRasterPos3i(x, y, z)

cpdef void glRasterPos3iv(const GLint *v):
    cglRasterPos3iv(v)

cpdef void glRasterPos3s(GLshort x, GLshort y, GLshort z):
    cglRasterPos3s(x, y, z)

cpdef void glRasterPos3sv(const GLshort *v):
    cglRasterPos3sv(v)

cpdef void glRasterPos4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglRasterPos4d(x, y, z, w)

cpdef void glRasterPos4dv(const GLdouble *v):
    cglRasterPos4dv(v)

cpdef void glRasterPos4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    cglRasterPos4f(x, y, z, w)

cpdef void glRasterPos4fv(const GLfloat *v):
    cglRasterPos4fv(v)

cpdef void glRasterPos4i(GLint x, GLint y, GLint z, GLint w):
    cglRasterPos4i(x, y, z, w)

cpdef void glRasterPos4iv(const GLint *v):
    cglRasterPos4iv(v)

cpdef void glRasterPos4s(GLshort x, GLshort y, GLshort z, GLshort w):
    cglRasterPos4s(x, y, z, w)

cpdef void glRasterPos4sv(const GLshort *v):
    cglRasterPos4sv(v)

cpdef void glRectd(GLdouble x1, GLdouble y1, GLdouble x2, GLdouble y2):
    cglRectd(x1, y1, x2, y2)

cpdef void glRectdv(const GLdouble *v1, const GLdouble *v2):
    cglRectdv(v1, v2)

cpdef void glRectf(GLfloat x1, GLfloat y1, GLfloat x2, GLfloat y2):
    cglRectf(x1, y1, x2, y2)

cpdef void glRectfv(const GLfloat *v1, const GLfloat *v2):
    cglRectfv(v1, v2)

cpdef void glRecti(GLint x1, GLint y1, GLint x2, GLint y2):
    cglRecti(x1, y1, x2, y2)

cpdef void glRectiv(const GLint *v1, const GLint *v2):
    cglRectiv(v1, v2)

cpdef void glRects(GLshort x1, GLshort y1, GLshort x2, GLshort y2):
    cglRects(x1, y1, x2, y2)

cpdef void glRectsv(const GLshort *v1, const GLshort *v2):
    cglRectsv(v1, v2)

cpdef void glTexCoord1d(GLdouble s):
    cglTexCoord1d(s)

cpdef void glTexCoord1dv(const GLdouble *v):
    cglTexCoord1dv(v)

cpdef void glTexCoord1f(GLfloat s):
    cglTexCoord1f(s)

cpdef void glTexCoord1fv(const GLfloat *v):
    cglTexCoord1fv(v)

cpdef void glTexCoord1i(GLint s):
    cglTexCoord1i(s)

cpdef void glTexCoord1iv(const GLint *v):
    cglTexCoord1iv(v)

cpdef void glTexCoord1s(GLshort s):
    cglTexCoord1s(s)

cpdef void glTexCoord1sv(const GLshort *v):
    cglTexCoord1sv(v)

cpdef void glTexCoord2d(GLdouble s, GLdouble t):
    cglTexCoord2d(s, t)

cpdef void glTexCoord2dv(const GLdouble *v):
    cglTexCoord2dv(v)

cpdef void glTexCoord2f(GLfloat s, GLfloat t):
    cglTexCoord2f(s, t)

cpdef void glTexCoord2fv(const GLfloat *v):
    cglTexCoord2fv(v)

cpdef void glTexCoord2i(GLint s, GLint t):
    cglTexCoord2i(s, t)

cpdef void glTexCoord2iv(const GLint *v):
    cglTexCoord2iv(v)

cpdef void glTexCoord2s(GLshort s, GLshort t):
    cglTexCoord2s(s, t)

cpdef void glTexCoord2sv(const GLshort *v):
    cglTexCoord2sv(v)

cpdef void glTexCoord3d(GLdouble s, GLdouble t, GLdouble r):
    cglTexCoord3d(s, t, r)

cpdef void glTexCoord3dv(const GLdouble *v):
    cglTexCoord3dv(v)

cpdef void glTexCoord3f(GLfloat s, GLfloat t, GLfloat r):
    cglTexCoord3f(s, t, r)

cpdef void glTexCoord3fv(const GLfloat *v):
    cglTexCoord3fv(v)

cpdef void glTexCoord3i(GLint s, GLint t, GLint r):
    cglTexCoord3i(s, t, r)

cpdef void glTexCoord3iv(const GLint *v):
    cglTexCoord3iv(v)

cpdef void glTexCoord3s(GLshort s, GLshort t, GLshort r):
    cglTexCoord3s(s, t, r)

cpdef void glTexCoord3sv(const GLshort *v):
    cglTexCoord3sv(v)

cpdef void glTexCoord4d(GLdouble s, GLdouble t, GLdouble r, GLdouble q):
    cglTexCoord4d(s, t, r, q)

cpdef void glTexCoord4dv(const GLdouble *v):
    cglTexCoord4dv(v)

cpdef void glTexCoord4f(GLfloat s, GLfloat t, GLfloat r, GLfloat q):
    cglTexCoord4f(s, t, r, q)

cpdef void glTexCoord4fv(const GLfloat *v):
    cglTexCoord4fv(v)

cpdef void glTexCoord4i(GLint s, GLint t, GLint r, GLint q):
    cglTexCoord4i(s, t, r, q)

cpdef void glTexCoord4iv(const GLint *v):
    cglTexCoord4iv(v)

cpdef void glTexCoord4s(GLshort s, GLshort t, GLshort r, GLshort q):
    cglTexCoord4s(s, t, r, q)

cpdef void glTexCoord4sv(const GLshort *v):
    cglTexCoord4sv(v)

cpdef void glVertex2d(GLdouble x, GLdouble y):
    cglVertex2d(x, y)

cpdef void glVertex2dv(const GLdouble *v):
    cglVertex2dv(v)

cpdef void glVertex2f(GLfloat x, GLfloat y):
    cglVertex2f(x, y)

cpdef void glVertex2fv(const GLfloat *v):
    cglVertex2fv(v)

cpdef void glVertex2i(GLint x, GLint y):
    cglVertex2i(x, y)

cpdef void glVertex2iv(const GLint *v):
    cglVertex2iv(v)

cpdef void glVertex2s(GLshort x, GLshort y):
    cglVertex2s(x, y)

cpdef void glVertex2sv(const GLshort *v):
    cglVertex2sv(v)

cpdef void glVertex3d(GLdouble x, GLdouble y, GLdouble z):
    cglVertex3d(x, y, z)

cpdef void glVertex3dv(const GLdouble *v):
    cglVertex3dv(v)

cpdef void glVertex3f(GLfloat x, GLfloat y, GLfloat z):
    cglVertex3f(x, y, z)

cpdef void glVertex3fv(const GLfloat *v):
    cglVertex3fv(v)

cpdef void glVertex3i(GLint x, GLint y, GLint z):
    cglVertex3i(x, y, z)

cpdef void glVertex3iv(const GLint *v):
    cglVertex3iv(v)

cpdef void glVertex3s(GLshort x, GLshort y, GLshort z):
    cglVertex3s(x, y, z)

cpdef void glVertex3sv(const GLshort *v):
    cglVertex3sv(v)

cpdef void glVertex4d(GLdouble x, GLdouble y, GLdouble z, GLdouble w):
    cglVertex4d(x, y, z, w)

cpdef void glVertex4dv(const GLdouble *v):
    cglVertex4dv(v)

cpdef void glVertex4f(GLfloat x, GLfloat y, GLfloat z, GLfloat w):
    cglVertex4f(x, y, z, w)

cpdef void glVertex4fv(const GLfloat *v):
    cglVertex4fv(v)

cpdef void glVertex4i(GLint x, GLint y, GLint z, GLint w):
    cglVertex4i(x, y, z, w)

cpdef void glVertex4iv(const GLint *v):
    cglVertex4iv(v)

cpdef void glVertex4s(GLshort x, GLshort y, GLshort z, GLshort w):
    cglVertex4s(x, y, z, w)

cpdef void glVertex4sv(const GLshort *v):
    cglVertex4sv(v)

cpdef void glClipPlane(GLenum plane, const GLdouble *equation):
    cglClipPlane(plane, equation)

cpdef void glColorMaterial(GLenum face, GLenum mode):
    cglColorMaterial(face, mode)

cpdef void glFogf(GLenum pname, GLfloat param):
    cglFogf(pname, param)

cpdef void glFogfv(GLenum pname, const GLfloat *params):
    cglFogfv(pname, params)

cpdef void glFogi(GLenum pname, GLint param):
    cglFogi(pname, param)

cpdef void glFogiv(GLenum pname, const GLint *params):
    cglFogiv(pname, params)

cpdef void glLightf(GLenum light, GLenum pname, GLfloat param):
    cglLightf(light, pname, param)

cpdef void glLightfv(GLenum light, GLenum pname, const GLfloat *params):
    cglLightfv(light, pname, params)

cpdef void glLighti(GLenum light, GLenum pname, GLint param):
    cglLighti(light, pname, param)

cpdef void glLightiv(GLenum light, GLenum pname, const GLint *params):
    cglLightiv(light, pname, params)

cpdef void glLightModelf(GLenum pname, GLfloat param):
    cglLightModelf(pname, param)

cpdef void glLightModelfv(GLenum pname, const GLfloat *params):
    cglLightModelfv(pname, params)

cpdef void glLightModeli(GLenum pname, GLint param):
    cglLightModeli(pname, param)

cpdef void glLightModeliv(GLenum pname, const GLint *params):
    cglLightModeliv(pname, params)

cpdef void glLineStipple(GLint factor, GLushort pattern):
    cglLineStipple(factor, pattern)

cpdef void glMaterialf(GLenum face, GLenum pname, GLfloat param):
    cglMaterialf(face, pname, param)

cpdef void glMaterialfv(GLenum face, GLenum pname, const GLfloat *params):
    cglMaterialfv(face, pname, params)

cpdef void glMateriali(GLenum face, GLenum pname, GLint param):
    cglMateriali(face, pname, param)

cpdef void glMaterialiv(GLenum face, GLenum pname, const GLint *params):
    cglMaterialiv(face, pname, params)

cpdef void glPolygonStipple(const GLubyte *mask):
    cglPolygonStipple(mask)

cpdef void glShadeModel(GLenum mode):
    cglShadeModel(mode)

cpdef void glTexEnvf(GLenum target, GLenum pname, GLfloat param):
    cglTexEnvf(target, pname, param)

cpdef void glTexEnvfv(GLenum target, GLenum pname, const GLfloat *params):
    cglTexEnvfv(target, pname, params)

cpdef void glTexEnvi(GLenum target, GLenum pname, GLint param):
    cglTexEnvi(target, pname, param)

cpdef void glTexEnviv(GLenum target, GLenum pname, const GLint *params):
    cglTexEnviv(target, pname, params)

cpdef void glTexGend(GLenum coord, GLenum pname, GLdouble param):
    cglTexGend(coord, pname, param)

cpdef void glTexGendv(GLenum coord, GLenum pname, const GLdouble *params):
    cglTexGendv(coord, pname, params)

cpdef void glTexGenf(GLenum coord, GLenum pname, GLfloat param):
    cglTexGenf(coord, pname, param)

cpdef void glTexGenfv(GLenum coord, GLenum pname, const GLfloat *params):
    cglTexGenfv(coord, pname, params)

cpdef void glTexGeni(GLenum coord, GLenum pname, GLint param):
    cglTexGeni(coord, pname, param)

cpdef void glTexGeniv(GLenum coord, GLenum pname, const GLint *params):
    cglTexGeniv(coord, pname, params)

cpdef void glFeedbackBuffer(GLsizei size, GLenum type, GLfloat *buffer):
    cglFeedbackBuffer(size, type, buffer)

cpdef void glSelectBuffer(GLsizei size, GLuint *buffer):
    cglSelectBuffer(size, buffer)

cpdef GLint glRenderMode(GLenum mode):
    cglRenderMode(mode)

cpdef void glInitNames():
    cglInitNames()

cpdef void glLoadName(GLuint name):
    cglLoadName(name)

cpdef void glPassThrough(GLfloat token):
    cglPassThrough(token)

cpdef void glPopName():
    cglPopName()

cpdef void glPushName(GLuint name):
    cglPushName(name)

cpdef void glClearAccum(GLfloat red, GLfloat green, GLfloat blue, GLfloat alpha):
    cglClearAccum(red, green, blue, alpha)

cpdef void glClearIndex(GLfloat c):
    cglClearIndex(c)

cpdef void glIndexMask(GLuint mask):
    cglIndexMask(mask)

cpdef void glAccum(GLenum op, GLfloat value):
    cglAccum(op, value)

cpdef void glPopAttrib():
    cglPopAttrib()

cpdef void glPushAttrib(GLbitfield mask):
    cglPushAttrib(mask)

cpdef void glMap1d(GLenum target, GLdouble u1, GLdouble u2, GLint stride, GLint order, const GLdouble *points):
    cglMap1d(target, u1, u2, stride, order, points)

cpdef void glMap1f(GLenum target, GLfloat u1, GLfloat u2, GLint stride, GLint order, const GLfloat *points):
    cglMap1f(target, u1, u2, stride, order, points)

cpdef void glMap2d(GLenum target, GLdouble u1, GLdouble u2, GLint ustride, GLint uorder, GLdouble v1, GLdouble v2, GLint vstride, GLint vorder, const GLdouble *points):
    cglMap2d(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)

cpdef void glMap2f(GLenum target, GLfloat u1, GLfloat u2, GLint ustride, GLint uorder, GLfloat v1, GLfloat v2, GLint vstride, GLint vorder, const GLfloat *points):
    cglMap2f(target, u1, u2, ustride, uorder, v1, v2, vstride, vorder, points)

cpdef void glMapGrid1d(GLint un, GLdouble u1, GLdouble u2):
    cglMapGrid1d(un, u1, u2)

cpdef void glMapGrid1f(GLint un, GLfloat u1, GLfloat u2):
    cglMapGrid1f(un, u1, u2)

cpdef void glMapGrid2d(GLint un, GLdouble u1, GLdouble u2, GLint vn, GLdouble v1, GLdouble v2):
    cglMapGrid2d(un, u1, u2, vn, v1, v2)

cpdef void glMapGrid2f(GLint un, GLfloat u1, GLfloat u2, GLint vn, GLfloat v1, GLfloat v2):
    cglMapGrid2f(un, u1, u2, vn, v1, v2)

cpdef void glEvalCoord1d(GLdouble u):
    cglEvalCoord1d(u)

cpdef void glEvalCoord1dv(const GLdouble *u):
    cglEvalCoord1dv(u)

cpdef void glEvalCoord1f(GLfloat u):
    cglEvalCoord1f(u)

cpdef void glEvalCoord1fv(const GLfloat *u):
    cglEvalCoord1fv(u)

cpdef void glEvalCoord2d(GLdouble u, GLdouble v):
    cglEvalCoord2d(u, v)

cpdef void glEvalCoord2dv(const GLdouble *u):
    cglEvalCoord2dv(u)

cpdef void glEvalCoord2f(GLfloat u, GLfloat v):
    cglEvalCoord2f(u, v)

cpdef void glEvalCoord2fv(const GLfloat *u):
    cglEvalCoord2fv(u)

cpdef void glEvalMesh1(GLenum mode, GLint i1, GLint i2):
    cglEvalMesh1(mode, i1, i2)

cpdef void glEvalPoint1(GLint i):
    cglEvalPoint1(i)

cpdef void glEvalMesh2(GLenum mode, GLint i1, GLint i2, GLint j1, GLint j2):
    cglEvalMesh2(mode, i1, i2, j1, j2)

cpdef void glEvalPoint2(GLint i, GLint j):
    cglEvalPoint2(i, j)

cpdef void glAlphaFunc(GLenum func, GLfloat ref):
    cglAlphaFunc(func, ref)

cpdef void glPixelZoom(GLfloat xfactor, GLfloat yfactor):
    cglPixelZoom(xfactor, yfactor)

cpdef void glPixelTransferf(GLenum pname, GLfloat param):
    cglPixelTransferf(pname, param)

cpdef void glPixelTransferi(GLenum pname, GLint param):
    cglPixelTransferi(pname, param)

cpdef void glPixelMapfv(GLenum map, GLsizei mapsize, const GLfloat *values):
    cglPixelMapfv(map, mapsize, values)

cpdef void glPixelMapuiv(GLenum map, GLsizei mapsize, const GLuint *values):
    cglPixelMapuiv(map, mapsize, values)

cpdef void glPixelMapusv(GLenum map, GLsizei mapsize, const GLushort *values):
    cglPixelMapusv(map, mapsize, values)

cpdef void glCopyPixels(GLint x, GLint y, GLsizei width, GLsizei height, GLenum type):
    cglCopyPixels(x, y, width, height, type)

cpdef void glDrawPixels(GLsizei width, GLsizei height, GLenum format, GLenum type, const void *pixels):
    cglDrawPixels(width, height, format, type, pixels)

cpdef void glGetClipPlane(GLenum plane, GLdouble *equation):
    cglGetClipPlane(plane, equation)

cpdef void glGetLightfv(GLenum light, GLenum pname, GLfloat *params):
    cglGetLightfv(light, pname, params)

cpdef void glGetLightiv(GLenum light, GLenum pname, GLint *params):
    cglGetLightiv(light, pname, params)

cpdef void glGetMapdv(GLenum target, GLenum query, GLdouble *v):
    cglGetMapdv(target, query, v)

cpdef void glGetMapfv(GLenum target, GLenum query, GLfloat *v):
    cglGetMapfv(target, query, v)

cpdef void glGetMapiv(GLenum target, GLenum query, GLint *v):
    cglGetMapiv(target, query, v)

cpdef void glGetMaterialfv(GLenum face, GLenum pname, GLfloat *params):
    cglGetMaterialfv(face, pname, params)

cpdef void glGetMaterialiv(GLenum face, GLenum pname, GLint *params):
    cglGetMaterialiv(face, pname, params)

cpdef void glGetPixelMapfv(GLenum map, GLfloat *values):
    cglGetPixelMapfv(map, values)

cpdef void glGetPixelMapuiv(GLenum map, GLuint *values):
    cglGetPixelMapuiv(map, values)

cpdef void glGetPixelMapusv(GLenum map, GLushort *values):
    cglGetPixelMapusv(map, values)

cpdef void glGetPolygonStipple(GLubyte *mask):
    cglGetPolygonStipple(mask)

cpdef void glGetTexEnvfv(GLenum target, GLenum pname, GLfloat *params):
    cglGetTexEnvfv(target, pname, params)

cpdef void glGetTexEnviv(GLenum target, GLenum pname, GLint *params):
    cglGetTexEnviv(target, pname, params)

cpdef void glGetTexGendv(GLenum coord, GLenum pname, GLdouble *params):
    cglGetTexGendv(coord, pname, params)

cpdef void glGetTexGenfv(GLenum coord, GLenum pname, GLfloat *params):
    cglGetTexGenfv(coord, pname, params)

cpdef void glGetTexGeniv(GLenum coord, GLenum pname, GLint *params):
    cglGetTexGeniv(coord, pname, params)

cpdef GLboolean glIsList(GLuint list):
    cglIsList(list)

cpdef void glFrustum(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar):
    cglFrustum(left, right, bottom, top, zNear, zFar)

cpdef void glLoadIdentity():
    cglLoadIdentity()

cpdef void glLoadMatrixf(const GLfloat *m):
    cglLoadMatrixf(m)

cpdef void glLoadMatrixd(const GLdouble *m):
    cglLoadMatrixd(m)

cpdef void glMatrixMode(GLenum mode):
    cglMatrixMode(mode)

cpdef void glMultMatrixf(const GLfloat *m):
    cglMultMatrixf(m)

cpdef void glMultMatrixd(const GLdouble *m):
    cglMultMatrixd(m)

cpdef void glOrtho(GLdouble left, GLdouble right, GLdouble bottom, GLdouble top, GLdouble zNear, GLdouble zFar):
    cglOrtho(left, right, bottom, top, zNear, zFar)

cpdef void glPopMatrix():
    cglPopMatrix()

cpdef void glPushMatrix():
    cglPushMatrix()

cpdef void glRotated(GLdouble angle, GLdouble x, GLdouble y, GLdouble z):
    cglRotated(angle, x, y, z)

cpdef void glRotatef(GLfloat angle, GLfloat x, GLfloat y, GLfloat z):
    cglRotatef(angle, x, y, z)

cpdef void glScaled(GLdouble x, GLdouble y, GLdouble z):
    cglScaled(x, y, z)

cpdef void glScalef(GLfloat x, GLfloat y, GLfloat z):
    cglScalef(x, y, z)

cpdef void glTranslated(GLdouble x, GLdouble y, GLdouble z):
    cglTranslated(x, y, z)

cpdef void glTranslatef(GLfloat x, GLfloat y, GLfloat z):
    cglTranslatef(x, y, z)
