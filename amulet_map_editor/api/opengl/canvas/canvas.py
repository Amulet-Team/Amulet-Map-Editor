from typing import Optional
import logging
import sys

import wx
from wx import glcanvas
from OpenGL.GL import (
    GL_DEPTH_TEST,
    glEnable,
    GL_CULL_FACE,
    glDepthFunc,
    GL_LEQUAL,
    GL_BLEND,
    glBlendFunc,
    GL_SRC_ALPHA,
    GL_ONE_MINUS_SRC_ALPHA,
    glGetString,
    GL_VERSION,
)

log = logging.getLogger(__name__)


"""OpenGL workflow:
The initialisation function should be as minimal as possible. No OpenGL functions should be called here. The OpenGL state is not valid until the window is first shown.
You can implement functions that take a while in threads to not block the GUI but they must still not contain OpenGL functions.
Upon the window being shown the OpenGL context is activated and the state can be set in _init_opengl
Objects that need to bind textures or data should do so in the draw function so they can be sure the context is set.
"""


class BaseCanvas(glcanvas.GLCanvas):
    _context: Optional[glcanvas.GLContext]

    def __init__(self, parent: wx.Window):
        """
        Construct the canvas.
        No OpenGL interaction should be done here.
        OpenGL initialisation should be done in _init_opengl which is run after the window is first shown.
        """
        display_attributes = glcanvas.GLAttributes()
        display_attributes.PlatformDefaults().MinRGBA(8, 8, 8, 8).DoubleBuffer().Depth(
            24
        ).EndList()
        super().__init__(
            parent,
            display_attributes,
            size=parent.GetClientSize(),
            style=wx.WANTS_CHARS,
        )
        if sys.platform == "darwin":
            # This is required for MacOS. Amulet-Team/Amulet-Map-Editor#597
            context_attributes = wx.glcanvas.GLContextAttrs()
            context_attributes.CoreProfile().Robust().ResetIsolation().EndList()
            self._context = glcanvas.GLContext(
                self, ctxAttrs=context_attributes
            )  # setup the OpenGL context
        else:
            # This is required for linux and windows.
            # Amulet-Team/Amulet-Map-Editor#84
            # Amulet-Team/Amulet-Map-Editor#856
            self._context = glcanvas.GLContext(self)

        if not self._context.IsOK():
            raise Exception(f"Failed setting up context")

        self._init = False

        self.Bind(wx.EVT_SHOW, self._on_show)

    @property
    def context(self) -> glcanvas.GLContext:
        return self._context

    @property
    def context_identifier(self) -> str:
        # if not self._init:
        #     raise Exception("Cannot access the context until the window has been shown.")
        return str(id(self._context))

    def _on_show(self, evt: wx.ShowEvent):
        if not self._init and evt.IsShown():
            self._init = True
            self._init_opengl()

    def _init_opengl(self):
        """Set up the OpenGL state after the window is first shown."""
        self.SetCurrent(self._context)
        gl_version = glGetString(GL_VERSION)
        if isinstance(gl_version, bytes):
            gl_version = gl_version.decode("utf-8")
        log.info(f"OpenGL Version {gl_version}")
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
