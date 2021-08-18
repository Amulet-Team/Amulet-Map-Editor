# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_BUFFER_SIZE = 0x8764
cdef GLenum GL_BUFFER_USAGE = 0x8765
cdef GLenum GL_QUERY_COUNTER_BITS = 0x8864
cdef GLenum GL_CURRENT_QUERY = 0x8865
cdef GLenum GL_QUERY_RESULT = 0x8866
cdef GLenum GL_QUERY_RESULT_AVAILABLE = 0x8867
cdef GLenum GL_ARRAY_BUFFER = 0x8892
cdef GLenum GL_ELEMENT_ARRAY_BUFFER = 0x8893
cdef GLenum GL_ARRAY_BUFFER_BINDING = 0x8894
cdef GLenum GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
cdef GLenum GL_READ_ONLY = 0x88B8
cdef GLenum GL_WRITE_ONLY = 0x88B9
cdef GLenum GL_READ_WRITE = 0x88BA
cdef GLenum GL_BUFFER_ACCESS = 0x88BB
cdef GLenum GL_BUFFER_MAPPED = 0x88BC
cdef GLenum GL_BUFFER_MAP_POINTER = 0x88BD
cdef GLenum GL_STREAM_DRAW = 0x88E0
cdef GLenum GL_STREAM_READ = 0x88E1
cdef GLenum GL_STREAM_COPY = 0x88E2
cdef GLenum GL_STATIC_DRAW = 0x88E4
cdef GLenum GL_STATIC_READ = 0x88E5
cdef GLenum GL_STATIC_COPY = 0x88E6
cdef GLenum GL_DYNAMIC_DRAW = 0x88E8
cdef GLenum GL_DYNAMIC_READ = 0x88E9
cdef GLenum GL_DYNAMIC_COPY = 0x88EA
cdef GLenum GL_SAMPLES_PASSED = 0x8914
cdef GLenum GL_SRC1_ALPHA = 0x8589
cdef GLenum GL_VERTEX_ARRAY_BUFFER_BINDING = 0x8896
cdef GLenum GL_NORMAL_ARRAY_BUFFER_BINDING = 0x8897
cdef GLenum GL_COLOR_ARRAY_BUFFER_BINDING = 0x8898
cdef GLenum GL_INDEX_ARRAY_BUFFER_BINDING = 0x8899
cdef GLenum GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 0x889A
cdef GLenum GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = 0x889B
cdef GLenum GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = 0x889C
cdef GLenum GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = 0x889D
cdef GLenum GL_WEIGHT_ARRAY_BUFFER_BINDING = 0x889E
cdef GLenum GL_FOG_COORD_SRC = 0x8450
cdef GLenum GL_FOG_COORD = 0x8451
cdef GLenum GL_CURRENT_FOG_COORD = 0x8453
cdef GLenum GL_FOG_COORD_ARRAY_TYPE = 0x8454
cdef GLenum GL_FOG_COORD_ARRAY_STRIDE = 0x8455
cdef GLenum GL_FOG_COORD_ARRAY_POINTER = 0x8456
cdef GLenum GL_FOG_COORD_ARRAY = 0x8457
cdef GLenum GL_FOG_COORD_ARRAY_BUFFER_BINDING = 0x889D
cdef GLenum GL_SRC0_RGB = 0x8580
cdef GLenum GL_SRC1_RGB = 0x8581
cdef GLenum GL_SRC2_RGB = 0x8582
cdef GLenum GL_SRC0_ALPHA = 0x8588
cdef GLenum GL_SRC2_ALPHA = 0x858A

ctypedef void (*GL_GEN_QUERIES)(GLsizei n, GLuint *ids)
ctypedef void (*GL_DELETE_QUERIES)(GLsizei n, const GLuint *ids)
ctypedef GLboolean (*GL_IS_QUERY)(GLuint id)
ctypedef void (*GL_BEGIN_QUERY)(GLenum target, GLuint id)
ctypedef void (*GL_END_QUERY)(GLenum target)
ctypedef void (*GL_GET_QUERYIV)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*GL_GET_QUERY_OBJECTIV)(GLuint id, GLenum pname, GLint *params)
ctypedef void (*GL_GET_QUERY_OBJECTUIV)(GLuint id, GLenum pname, GLuint *params)
ctypedef void (*GL_BIND_BUFFER)(GLenum target, GLuint buffer)
ctypedef void (*GL_DELETE_BUFFERS)(GLsizei n, const GLuint *buffers)
ctypedef void (*GL_GEN_BUFFERS)(GLsizei n, GLuint *buffers)
ctypedef GLboolean (*GL_IS_BUFFER)(GLuint buffer)
ctypedef void (*GL_BUFFER_DATA)(GLenum target, GLsizeiptr size, const void *data, GLenum usage)
ctypedef void (*GL_BUFFER_SUB_DATA)(GLenum target, GLintptr offset, GLsizeiptr size, const void *data)
ctypedef void (*GL_GET_BUFFER_SUB_DATA)(GLenum target, GLintptr offset, GLsizeiptr size, void *data)
ctypedef void *(*GL_MAP_BUFFER)(GLenum target, GLenum access)
ctypedef GLboolean (*GL_UNMAP_BUFFER)(GLenum target)
ctypedef void (*GL_GET_BUFFER_PARAMETERIV)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*GL_GET_BUFFER_POINTERV)(GLenum target, GLenum pname, void **params)

cdef GL_GEN_QUERIES cglGenQueries = NULL
cdef GL_DELETE_QUERIES cglDeleteQueries = NULL
cdef GL_IS_QUERY cglIsQuery = NULL
cdef GL_BEGIN_QUERY cglBeginQuery = NULL
cdef GL_END_QUERY cglEndQuery = NULL
cdef GL_GET_QUERYIV cglGetQueryiv = NULL
cdef GL_GET_QUERY_OBJECTIV cglGetQueryObjectiv = NULL
cdef GL_GET_QUERY_OBJECTUIV cglGetQueryObjectuiv = NULL
cdef GL_BIND_BUFFER cglBindBuffer = NULL
cdef GL_DELETE_BUFFERS cglDeleteBuffers = NULL
cdef GL_GEN_BUFFERS cglGenBuffers = NULL
cdef GL_IS_BUFFER cglIsBuffer = NULL
cdef GL_BUFFER_DATA cglBufferData = NULL
cdef GL_BUFFER_SUB_DATA cglBufferSubData = NULL
cdef GL_GET_BUFFER_SUB_DATA cglGetBufferSubData = NULL
cdef GL_MAP_BUFFER cglMapBuffer = NULL
cdef GL_UNMAP_BUFFER cglUnmapBuffer = NULL
cdef GL_GET_BUFFER_PARAMETERIV cglGetBufferParameteriv = NULL
cdef GL_GET_BUFFER_POINTERV cglGetBufferPointerv = NULL


cdef void GetglGenQueries(GLsizei n, GLuint *ids):
    global cglGenQueries
    cglGenQueries = <GL_GEN_QUERIES>getFunction(b"glGenQueries")
    cglGenQueries(n, ids)

cdef void GetglDeleteQueries(GLsizei n, const GLuint *ids):
    global cglDeleteQueries
    cglDeleteQueries = <GL_DELETE_QUERIES>getFunction(b"glDeleteQueries")
    cglDeleteQueries(n, ids)

cdef GLboolean GetglIsQuery(GLuint id):
    global cglIsQuery
    cglIsQuery = <GL_IS_QUERY>getFunction(b"glIsQuery")
    cglIsQuery(id)

cdef void GetglBeginQuery(GLenum target, GLuint id):
    global cglBeginQuery
    cglBeginQuery = <GL_BEGIN_QUERY>getFunction(b"glBeginQuery")
    cglBeginQuery(target, id)

cdef void GetglEndQuery(GLenum target):
    global cglEndQuery
    cglEndQuery = <GL_END_QUERY>getFunction(b"glEndQuery")
    cglEndQuery(target)

cdef void GetglGetQueryiv(GLenum target, GLenum pname, GLint *params):
    global cglGetQueryiv
    cglGetQueryiv = <GL_GET_QUERYIV>getFunction(b"glGetQueryiv")
    cglGetQueryiv(target, pname, params)

cdef void GetglGetQueryObjectiv(GLuint id, GLenum pname, GLint *params):
    global cglGetQueryObjectiv
    cglGetQueryObjectiv = <GL_GET_QUERY_OBJECTIV>getFunction(b"glGetQueryObjectiv")
    cglGetQueryObjectiv(id, pname, params)

cdef void GetglGetQueryObjectuiv(GLuint id, GLenum pname, GLuint *params):
    global cglGetQueryObjectuiv
    cglGetQueryObjectuiv = <GL_GET_QUERY_OBJECTUIV>getFunction(b"glGetQueryObjectuiv")
    cglGetQueryObjectuiv(id, pname, params)

cdef void GetglBindBuffer(GLenum target, GLuint buffer):
    global cglBindBuffer
    cglBindBuffer = <GL_BIND_BUFFER>getFunction(b"glBindBuffer")
    cglBindBuffer(target, buffer)

cdef void GetglDeleteBuffers(GLsizei n, const GLuint *buffers):
    global cglDeleteBuffers
    cglDeleteBuffers = <GL_DELETE_BUFFERS>getFunction(b"glDeleteBuffers")
    cglDeleteBuffers(n, buffers)

cdef void GetglGenBuffers(GLsizei n, GLuint *buffers):
    global cglGenBuffers
    cglGenBuffers = <GL_GEN_BUFFERS>getFunction(b"glGenBuffers")
    cglGenBuffers(n, buffers)

cdef GLboolean GetglIsBuffer(GLuint buffer):
    global cglIsBuffer
    cglIsBuffer = <GL_IS_BUFFER>getFunction(b"glIsBuffer")
    cglIsBuffer(buffer)

cdef void GetglBufferData(GLenum target, GLsizeiptr size, const void *data, GLenum usage):
    global cglBufferData
    cglBufferData = <GL_BUFFER_DATA>getFunction(b"glBufferData")
    cglBufferData(target, size, data, usage)

cdef void GetglBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, const void *data):
    global cglBufferSubData
    cglBufferSubData = <GL_BUFFER_SUB_DATA>getFunction(b"glBufferSubData")
    cglBufferSubData(target, offset, size, data)

cdef void GetglGetBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, void *data):
    global cglGetBufferSubData
    cglGetBufferSubData = <GL_GET_BUFFER_SUB_DATA>getFunction(b"glGetBufferSubData")
    cglGetBufferSubData(target, offset, size, data)

cdef void *GetglMapBuffer(GLenum target, GLenum access):
    global cglMapBuffer
    cglMapBuffer = <GL_MAP_BUFFER>getFunction(b"glMapBuffer")
    cglMapBuffer(target, access)

cdef GLboolean GetglUnmapBuffer(GLenum target):
    global cglUnmapBuffer
    cglUnmapBuffer = <GL_UNMAP_BUFFER>getFunction(b"glUnmapBuffer")
    cglUnmapBuffer(target)

cdef void GetglGetBufferParameteriv(GLenum target, GLenum pname, GLint *params):
    global cglGetBufferParameteriv
    cglGetBufferParameteriv = <GL_GET_BUFFER_PARAMETERIV>getFunction(b"glGetBufferParameteriv")
    cglGetBufferParameteriv(target, pname, params)

cdef void GetglGetBufferPointerv(GLenum target, GLenum pname, void **params):
    global cglGetBufferPointerv
    cglGetBufferPointerv = <GL_GET_BUFFER_POINTERV>getFunction(b"glGetBufferPointerv")
    cglGetBufferPointerv(target, pname, params)

cglGenQueries = GetglGenQueries
cglDeleteQueries = GetglDeleteQueries
cglIsQuery = GetglIsQuery
cglBeginQuery = GetglBeginQuery
cglEndQuery = GetglEndQuery
cglGetQueryiv = GetglGetQueryiv
cglGetQueryObjectiv = GetglGetQueryObjectiv
cglGetQueryObjectuiv = GetglGetQueryObjectuiv
cglBindBuffer = GetglBindBuffer
cglDeleteBuffers = GetglDeleteBuffers
cglGenBuffers = GetglGenBuffers
cglIsBuffer = GetglIsBuffer
cglBufferData = GetglBufferData
cglBufferSubData = GetglBufferSubData
cglGetBufferSubData = GetglGetBufferSubData
cglMapBuffer = GetglMapBuffer
cglUnmapBuffer = GetglUnmapBuffer
cglGetBufferParameteriv = GetglGetBufferParameteriv
cglGetBufferPointerv = GetglGetBufferPointerv


cpdef void glGenQueries(GLsizei n, GLuint *ids):
    cglGenQueries(n, ids)

cpdef void glDeleteQueries(GLsizei n, const GLuint *ids):
    cglDeleteQueries(n, ids)

cpdef GLboolean glIsQuery(GLuint id):
    cglIsQuery(id)

cpdef void glBeginQuery(GLenum target, GLuint id):
    cglBeginQuery(target, id)

cpdef void glEndQuery(GLenum target):
    cglEndQuery(target)

cpdef void glGetQueryiv(GLenum target, GLenum pname, GLint *params):
    cglGetQueryiv(target, pname, params)

cpdef void glGetQueryObjectiv(GLuint id, GLenum pname, GLint *params):
    cglGetQueryObjectiv(id, pname, params)

cpdef void glGetQueryObjectuiv(GLuint id, GLenum pname, GLuint *params):
    cglGetQueryObjectuiv(id, pname, params)

cpdef void glBindBuffer(GLenum target, GLuint buffer):
    cglBindBuffer(target, buffer)

cpdef void glDeleteBuffers(GLsizei n, const GLuint *buffers):
    cglDeleteBuffers(n, buffers)

cpdef void glGenBuffers(GLsizei n, GLuint *buffers):
    cglGenBuffers(n, buffers)

cpdef GLboolean glIsBuffer(GLuint buffer):
    cglIsBuffer(buffer)

cpdef void glBufferData(GLenum target, GLsizeiptr size, const void *data, GLenum usage):
    cglBufferData(target, size, data, usage)

cpdef void glBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, const void *data):
    cglBufferSubData(target, offset, size, data)

cpdef void glGetBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, void *data):
    cglGetBufferSubData(target, offset, size, data)

cpdef void *glMapBuffer(GLenum target, GLenum access):
    cglMapBuffer(target, access)

cpdef GLboolean glUnmapBuffer(GLenum target):
    cglUnmapBuffer(target)

cpdef void glGetBufferParameteriv(GLenum target, GLenum pname, GLint *params):
    cglGetBufferParameteriv(target, pname, params)

cpdef void glGetBufferPointerv(GLenum target, GLenum pname, void **params):
    cglGetBufferPointerv(target, pname, params)
