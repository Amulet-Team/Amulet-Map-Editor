import wx
from wx import glcanvas
from OpenGL.GL import (
    GL_DEPTH_TEST,
    glEnable,
    glGenTextures,
    GL_CULL_FACE,
    glDepthFunc,
    GL_LEQUAL,
    GL_BLEND,
    glBlendFunc,
    GL_SRC_ALPHA,
    GL_ONE_MINUS_SRC_ALPHA,
    glDeleteTextures,
)
from OpenGL.error import GLError

import uuid
import sys

from amulet_map_editor import log


class BaseCanvas(glcanvas.GLCanvas):
    def __init__(self, parent: wx.Window):
        display_attributes = wx.glcanvas.GLAttributes()
        display_attributes.PlatformDefaults().MinRGBA(8, 8, 8, 8).DoubleBuffer().Depth(
            24
        ).EndList()
        super().__init__(
            parent,
            display_attributes,
            size=parent.GetClientSize(),
            style=wx.WANTS_CHARS,
        )

        # create a UUID for the context. Used to get shaders
        self._context_identifier = str(uuid.uuid4())

        if sys.platform == "linux":
            # setup the OpenGL context. This apparently fixes #84
            self._context = glcanvas.GLContext(self)
            self.SetCurrent(self._context)
            self._gl_texture_atlas = glGenTextures(1)  # Create the atlas texture location
        else:
            try:
                context_attributes = wx.glcanvas.GLContextAttrs()
                context_attributes.CoreProfile().OGLVersion(
                    3, 3
                ).Robust().ResetIsolation().EndList()
                self._context = glcanvas.GLContext(
                    self, ctxAttrs=context_attributes
                )  # setup the OpenGL context
                self.SetCurrent(self._context)
                self._gl_texture_atlas = glGenTextures(1)  # Create the atlas texture location
            except GLError:
                log.info("Failed setting up modern OpenGL. Falling back to legacy OpenGL.")
                try:
                    context_attributes = wx.glcanvas.GLContextAttrs()
                    context_attributes.CoreProfile().OGLVersion(
                        2, 1
                    ).Robust().ResetIsolation().EndList()
                    self._context = glcanvas.GLContext(
                        self, ctxAttrs=context_attributes
                    )  # setup the OpenGL context
                    self.SetCurrent(self._context)
                    self._gl_texture_atlas = glGenTextures(1)  # Create the atlas texture location
                except GLError as e:
                    log.error("Failed setting up legacy OpenGL.")
                    raise e
        self._setup_opengl()  # set some OpenGL states

    @property
    def context_identifier(self) -> str:
        return self._context_identifier

    def _setup_opengl(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def _close(self):
        glDeleteTextures([self._gl_texture_atlas])
