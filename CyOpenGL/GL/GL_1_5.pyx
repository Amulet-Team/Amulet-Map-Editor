# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

from CyOpenGL.GL.load_function cimport getFunction

cdef GLenum GL_ARRAY_BUFFER = 0x8892
cdef GLenum GL_ARRAY_BUFFER_BINDING = 0x8894
cdef GLenum GL_BUFFER_ACCESS = 0x88BB
cdef GLenum GL_BUFFER_MAPPED = 0x88BC
cdef GLenum GL_BUFFER_MAP_POINTER = 0x88BD
cdef GLenum GL_BUFFER_SIZE = 0x8764
cdef GLenum GL_BUFFER_USAGE = 0x8765
cdef GLenum GL_COLOR_ARRAY_BUFFER_BINDING = 0x8898
cdef GLenum GL_CURRENT_FOG_COORD = 0x8453
cdef GLenum GL_CURRENT_QUERY = 0x8865
cdef GLenum GL_DYNAMIC_COPY = 0x88EA
cdef GLenum GL_DYNAMIC_DRAW = 0x88E8
cdef GLenum GL_DYNAMIC_READ = 0x88E9
cdef GLenum GL_EDGE_FLAG_ARRAY_BUFFER_BINDING = 0x889B
cdef GLenum GL_ELEMENT_ARRAY_BUFFER = 0x8893
cdef GLenum GL_ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
cdef GLenum GL_FOG_COORD = 0x8451
cdef GLenum GL_FOG_COORDINATE_ARRAY_BUFFER_BINDING = 0x889D
cdef GLenum GL_FOG_COORD_ARRAY = 0x8457
cdef GLenum GL_FOG_COORD_ARRAY_BUFFER_BINDING = 0x889D
cdef GLenum GL_FOG_COORD_ARRAY_POINTER = 0x8456
cdef GLenum GL_FOG_COORD_ARRAY_STRIDE = 0x8455
cdef GLenum GL_FOG_COORD_ARRAY_TYPE = 0x8454
cdef GLenum GL_FOG_COORD_SRC = 0x8450
cdef GLenum GL_INDEX_ARRAY_BUFFER_BINDING = 0x8899
cdef GLenum GL_NORMAL_ARRAY_BUFFER_BINDING = 0x8897
cdef GLenum GL_QUERY_COUNTER_BITS = 0x8864
cdef GLenum GL_QUERY_RESULT = 0x8866
cdef GLenum GL_QUERY_RESULT_AVAILABLE = 0x8867
cdef GLenum GL_READ_ONLY = 0x88B8
cdef GLenum GL_READ_WRITE = 0x88BA
cdef GLenum GL_SAMPLES_PASSED = 0x8914
cdef GLenum GL_SECONDARY_COLOR_ARRAY_BUFFER_BINDING = 0x889C
cdef GLenum GL_SRC0_ALPHA = 0x8588
cdef GLenum GL_SRC0_RGB = 0x8580
cdef GLenum GL_SRC1_ALPHA = 0x8589
cdef GLenum GL_SRC1_RGB = 0x8581
cdef GLenum GL_SRC2_ALPHA = 0x858A
cdef GLenum GL_SRC2_RGB = 0x8582
cdef GLenum GL_STATIC_COPY = 0x88E6
cdef GLenum GL_STATIC_DRAW = 0x88E4
cdef GLenum GL_STATIC_READ = 0x88E5
cdef GLenum GL_STREAM_COPY = 0x88E2
cdef GLenum GL_STREAM_DRAW = 0x88E0
cdef GLenum GL_STREAM_READ = 0x88E1
cdef GLenum GL_TEXTURE_COORD_ARRAY_BUFFER_BINDING = 0x889A
cdef GLenum GL_VERTEX_ARRAY_BUFFER_BINDING = 0x8896
cdef GLenum GL_VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
cdef GLenum GL_WEIGHT_ARRAY_BUFFER_BINDING = 0x889E
cdef GLenum GL_WRITE_ONLY = 0x88B9

ctypedef void (*PFNGLBEGINQUERYPROC)(GLenum target, GLuint id)
ctypedef void (*PFNGLBINDBUFFERPROC)(GLenum target, GLuint buffer)
ctypedef void (*PFNGLBUFFERDATAPROC)(GLenum target, GLsizeiptr size, const void *data, GLenum usage)
ctypedef void (*PFNGLBUFFERSUBDATAPROC)(GLenum target, GLintptr offset, GLsizeiptr size, const void *data)
ctypedef void (*PFNGLDELETEBUFFERSPROC)(GLsizei n, const GLuint *buffers)
ctypedef void (*PFNGLDELETEQUERIESPROC)(GLsizei n, const GLuint *ids)
ctypedef void (*PFNGLENDQUERYPROC)(GLenum target)
ctypedef void (*PFNGLGENBUFFERSPROC)(GLsizei n, GLuint *buffers)
ctypedef void (*PFNGLGENQUERIESPROC)(GLsizei n, GLuint *ids)
ctypedef void (*PFNGLGETBUFFERPARAMETERIVPROC)(GLenum target, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETBUFFERPOINTERVPROC)(GLenum target, GLenum pname, void **params)
ctypedef void (*PFNGLGETBUFFERSUBDATAPROC)(GLenum target, GLintptr offset, GLsizeiptr size, void *data)
ctypedef void (*PFNGLGETQUERYOBJECTIVPROC)(GLuint id, GLenum pname, GLint *params)
ctypedef void (*PFNGLGETQUERYOBJECTUIVPROC)(GLuint id, GLenum pname, GLuint *params)
ctypedef void (*PFNGLGETQUERYIVPROC)(GLenum target, GLenum pname, GLint *params)
ctypedef GLboolean (*PFNGLISBUFFERPROC)(GLuint buffer)
ctypedef GLboolean (*PFNGLISQUERYPROC)(GLuint id)
ctypedef void *(*PFNGLMAPBUFFERPROC)(GLenum target, GLenum access)
ctypedef GLboolean (*PFNGLUNMAPBUFFERPROC)(GLenum target)

cdef PFNGLBEGINQUERYPROC cglBeginQuery = NULL
cdef PFNGLBINDBUFFERPROC cglBindBuffer = NULL
cdef PFNGLBUFFERDATAPROC cglBufferData = NULL
cdef PFNGLBUFFERSUBDATAPROC cglBufferSubData = NULL
cdef PFNGLDELETEBUFFERSPROC cglDeleteBuffers = NULL
cdef PFNGLDELETEQUERIESPROC cglDeleteQueries = NULL
cdef PFNGLENDQUERYPROC cglEndQuery = NULL
cdef PFNGLGENBUFFERSPROC cglGenBuffers = NULL
cdef PFNGLGENQUERIESPROC cglGenQueries = NULL
cdef PFNGLGETBUFFERPARAMETERIVPROC cglGetBufferParameteriv = NULL
cdef PFNGLGETBUFFERPOINTERVPROC cglGetBufferPointerv = NULL
cdef PFNGLGETBUFFERSUBDATAPROC cglGetBufferSubData = NULL
cdef PFNGLGETQUERYOBJECTIVPROC cglGetQueryObjectiv = NULL
cdef PFNGLGETQUERYOBJECTUIVPROC cglGetQueryObjectuiv = NULL
cdef PFNGLGETQUERYIVPROC cglGetQueryiv = NULL
cdef PFNGLISBUFFERPROC cglIsBuffer = NULL
cdef PFNGLISQUERYPROC cglIsQuery = NULL
cdef PFNGLMAPBUFFERPROC cglMapBuffer = NULL
cdef PFNGLUNMAPBUFFERPROC cglUnmapBuffer = NULL


cdef void GetglBeginQuery(GLenum target, GLuint id):
    global cglBeginQuery
    cglBeginQuery = <PFNGLBEGINQUERYPROC>getFunction(b"glBeginQuery")
    cglBeginQuery(target, id)

cdef void GetglBindBuffer(GLenum target, GLuint buffer):
    global cglBindBuffer
    cglBindBuffer = <PFNGLBINDBUFFERPROC>getFunction(b"glBindBuffer")
    cglBindBuffer(target, buffer)

cdef void GetglBufferData(GLenum target, GLsizeiptr size, const void *data, GLenum usage):
    global cglBufferData
    cglBufferData = <PFNGLBUFFERDATAPROC>getFunction(b"glBufferData")
    cglBufferData(target, size, data, usage)

cdef void GetglBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, const void *data):
    global cglBufferSubData
    cglBufferSubData = <PFNGLBUFFERSUBDATAPROC>getFunction(b"glBufferSubData")
    cglBufferSubData(target, offset, size, data)

cdef void GetglDeleteBuffers(GLsizei n, const GLuint *buffers):
    global cglDeleteBuffers
    cglDeleteBuffers = <PFNGLDELETEBUFFERSPROC>getFunction(b"glDeleteBuffers")
    cglDeleteBuffers(n, buffers)

cdef void GetglDeleteQueries(GLsizei n, const GLuint *ids):
    global cglDeleteQueries
    cglDeleteQueries = <PFNGLDELETEQUERIESPROC>getFunction(b"glDeleteQueries")
    cglDeleteQueries(n, ids)

cdef void GetglEndQuery(GLenum target):
    global cglEndQuery
    cglEndQuery = <PFNGLENDQUERYPROC>getFunction(b"glEndQuery")
    cglEndQuery(target)

cdef void GetglGenBuffers(GLsizei n, GLuint *buffers):
    global cglGenBuffers
    cglGenBuffers = <PFNGLGENBUFFERSPROC>getFunction(b"glGenBuffers")
    cglGenBuffers(n, buffers)

cdef void GetglGenQueries(GLsizei n, GLuint *ids):
    global cglGenQueries
    cglGenQueries = <PFNGLGENQUERIESPROC>getFunction(b"glGenQueries")
    cglGenQueries(n, ids)

cdef void GetglGetBufferParameteriv(GLenum target, GLenum pname, GLint *params):
    global cglGetBufferParameteriv
    cglGetBufferParameteriv = <PFNGLGETBUFFERPARAMETERIVPROC>getFunction(b"glGetBufferParameteriv")
    cglGetBufferParameteriv(target, pname, params)

cdef void GetglGetBufferPointerv(GLenum target, GLenum pname, void **params):
    global cglGetBufferPointerv
    cglGetBufferPointerv = <PFNGLGETBUFFERPOINTERVPROC>getFunction(b"glGetBufferPointerv")
    cglGetBufferPointerv(target, pname, params)

cdef void GetglGetBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, void *data):
    global cglGetBufferSubData
    cglGetBufferSubData = <PFNGLGETBUFFERSUBDATAPROC>getFunction(b"glGetBufferSubData")
    cglGetBufferSubData(target, offset, size, data)

cdef void GetglGetQueryObjectiv(GLuint id, GLenum pname, GLint *params):
    global cglGetQueryObjectiv
    cglGetQueryObjectiv = <PFNGLGETQUERYOBJECTIVPROC>getFunction(b"glGetQueryObjectiv")
    cglGetQueryObjectiv(id, pname, params)

cdef void GetglGetQueryObjectuiv(GLuint id, GLenum pname, GLuint *params):
    global cglGetQueryObjectuiv
    cglGetQueryObjectuiv = <PFNGLGETQUERYOBJECTUIVPROC>getFunction(b"glGetQueryObjectuiv")
    cglGetQueryObjectuiv(id, pname, params)

cdef void GetglGetQueryiv(GLenum target, GLenum pname, GLint *params):
    global cglGetQueryiv
    cglGetQueryiv = <PFNGLGETQUERYIVPROC>getFunction(b"glGetQueryiv")
    cglGetQueryiv(target, pname, params)

cdef GLboolean GetglIsBuffer(GLuint buffer):
    global cglIsBuffer
    cglIsBuffer = <PFNGLISBUFFERPROC>getFunction(b"glIsBuffer")
    cglIsBuffer(buffer)

cdef GLboolean GetglIsQuery(GLuint id):
    global cglIsQuery
    cglIsQuery = <PFNGLISQUERYPROC>getFunction(b"glIsQuery")
    cglIsQuery(id)

cdef void *GetglMapBuffer(GLenum target, GLenum access):
    global cglMapBuffer
    cglMapBuffer = <PFNGLMAPBUFFERPROC>getFunction(b"glMapBuffer")
    cglMapBuffer(target, access)

cdef GLboolean GetglUnmapBuffer(GLenum target):
    global cglUnmapBuffer
    cglUnmapBuffer = <PFNGLUNMAPBUFFERPROC>getFunction(b"glUnmapBuffer")
    cglUnmapBuffer(target)

cglBeginQuery = GetglBeginQuery
cglBindBuffer = GetglBindBuffer
cglBufferData = GetglBufferData
cglBufferSubData = GetglBufferSubData
cglDeleteBuffers = GetglDeleteBuffers
cglDeleteQueries = GetglDeleteQueries
cglEndQuery = GetglEndQuery
cglGenBuffers = GetglGenBuffers
cglGenQueries = GetglGenQueries
cglGetBufferParameteriv = GetglGetBufferParameteriv
cglGetBufferPointerv = GetglGetBufferPointerv
cglGetBufferSubData = GetglGetBufferSubData
cglGetQueryObjectiv = GetglGetQueryObjectiv
cglGetQueryObjectuiv = GetglGetQueryObjectuiv
cglGetQueryiv = GetglGetQueryiv
cglIsBuffer = GetglIsBuffer
cglIsQuery = GetglIsQuery
cglMapBuffer = GetglMapBuffer
cglUnmapBuffer = GetglUnmapBuffer


cdef void glBeginQuery(GLenum target, GLuint id):
    cglBeginQuery(target, id)

cdef void glBindBuffer(GLenum target, GLuint buffer):
    cglBindBuffer(target, buffer)

cdef void glBufferData(GLenum target, GLsizeiptr size, const void *data, GLenum usage):
    cglBufferData(target, size, data, usage)

cdef void glBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, const void *data):
    cglBufferSubData(target, offset, size, data)

cdef void glDeleteBuffers(GLsizei n, const GLuint *buffers):
    cglDeleteBuffers(n, buffers)

cdef void glDeleteQueries(GLsizei n, const GLuint *ids):
    cglDeleteQueries(n, ids)

cdef void glEndQuery(GLenum target):
    cglEndQuery(target)

cdef void glGenBuffers(GLsizei n, GLuint *buffers):
    cglGenBuffers(n, buffers)

cdef void glGenQueries(GLsizei n, GLuint *ids):
    cglGenQueries(n, ids)

cdef void glGetBufferParameteriv(GLenum target, GLenum pname, GLint *params):
    cglGetBufferParameteriv(target, pname, params)

cdef void glGetBufferPointerv(GLenum target, GLenum pname, void **params):
    cglGetBufferPointerv(target, pname, params)

cdef void glGetBufferSubData(GLenum target, GLintptr offset, GLsizeiptr size, void *data):
    cglGetBufferSubData(target, offset, size, data)

cdef void glGetQueryObjectiv(GLuint id, GLenum pname, GLint *params):
    cglGetQueryObjectiv(id, pname, params)

cdef void glGetQueryObjectuiv(GLuint id, GLenum pname, GLuint *params):
    cglGetQueryObjectuiv(id, pname, params)

cdef void glGetQueryiv(GLenum target, GLenum pname, GLint *params):
    cglGetQueryiv(target, pname, params)

cdef GLboolean glIsBuffer(GLuint buffer):
    cglIsBuffer(buffer)

cdef GLboolean glIsQuery(GLuint id):
    cglIsQuery(id)

cdef void *glMapBuffer(GLenum target, GLenum access):
    cglMapBuffer(target, access)

cdef GLboolean glUnmapBuffer(GLenum target):
    cglUnmapBuffer(target)
