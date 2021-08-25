# cython: language_level=3, boundscheck=False, wraparound=False
# distutils: libraries = opengl32

import os

IF UNAME_SYSNAME == "Windows":
    cdef extern from "<windows.h>":
        ctypedef void *HMODULE
        ctypedef char *LPCSTR
    cdef extern from "<libloaderapi.h>":
        HMODULE LoadLibraryA(LPCSTR lpLibFileName)
        void* GetProcAddress(HMODULE hModule, LPCSTR lpProcName)
    cdef extern from "<gl/gl.h>":
        void* wglGetProcAddress(LPCSTR lpszProc)
    cdef void *getFunction(LPCSTR functionName):
        cdef void* p
        cdef HMODULE module
        p = wglGetProcAddress(functionName)
        if -1 <= <unsigned long>p <= 3:
            module = LoadLibraryA("opengl32.dll")
            p = GetProcAddress(module, functionName)
        return p

ELIF UNAME_SYSNAME == "Darwin":
    cdef void *getFunction(char *functionName):
        raise Exception("Darwin not yet supported")

ELIF UNAME_SYSNAME == "Linux":
    cdef void *getFunction(char *functionName):
        raise Exception("Linux not yet supported")

ELSE:
    cdef void *getFunction(char *functionName):
        raise Exception(f"{os.uname()[0]} not yet supported")
