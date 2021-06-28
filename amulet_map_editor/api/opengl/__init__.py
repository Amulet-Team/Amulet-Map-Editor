from .context_manager import ContextManager
from .drawable import Drawable
from .thread_generator import ThreadedObject, ThreadedObjectContainer


def check_opengl(checked=False):
    try:
        import OpenGL.GL
    except ImportError as e:
        import os
        import ctypes.util

        uname = os.uname()
        if uname[0] == "Darwin" and uname[2] >= "20." and not checked:
            real_find_library = ctypes.util.find_library

            def find_library(name):
                if name in {"OpenGL", "GLUT"}:  # add more names here if necessary
                    return f"/System/Library/Frameworks/{name}.framework/{name}"
                return real_find_library(name)

            ctypes.util.find_library = find_library
            check_opengl(True)
        else:
            raise e
