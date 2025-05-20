from typing import Optional, Callable
import logging

import sys
import wx
from wx.glcanvas import GLCanvas, GLAttributes, GLContext, GLContextAttrs
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
from OpenGL.GL.ARB.explicit_attrib_location import glInitExplicitAttribLocationARB

log = logging.getLogger(__name__)


"""OpenGL workflow:
The initialisation function should be as minimal as possible. No OpenGL functions should be called here. The OpenGL state is not valid until the window is first shown.
You can implement functions that take a while in threads to not block the GUI but they must still not contain OpenGL functions.
Upon the window being shown the OpenGL context is activated and the state can be set in _init_opengl
Objects that need to bind textures or data should do so in the draw function so they can be sure the context is set.
"""

if sys.platform == "linux":
    Canvas_Type = wx.Window
else:
    Canvas_Type = GLCanvas

class BaseCanvas(Canvas_Type):
    _context: Optional[GLContext]

    def __init__(self, parent: wx.Window):
        """
        Construct the canvas.
        No OpenGL interaction should be done here.
        OpenGL initialisation should be done in _init_opengl which is run after the window is first shown.
        """
        display_attributes = GLAttributes()
        display_attributes.PlatformDefaults().MinRGBA(8, 8, 8, 8).DoubleBuffer().Depth(
            24
        ).EndList()
        if Canvas_Type == wx.Window:
            super().__init__(parent)
            # self.SetSizer(self._canvas_sizer)
            self._opengl_canvas = GLCanvas( self,
                display_attributes,
                size=parent.GetClientSize(),
                style=wx.WANTS_CHARS,
            )

            def forward_event(event):
                # Create a new mouse event and send it to the parent
                new_event = wx.MouseEvent(event.GetEventType())
                new_event.SetPosition(event.GetPosition())
                wx.PostEvent(self, new_event)
                event.Skip()  # Continue processing normally
            self._opengl_canvas.Bind(wx.EVT_RIGHT_DOWN, forward_event)
            self._opengl_canvas.Bind(wx.EVT_RIGHT_UP, forward_event)
            self._opengl_canvas.Bind(wx.EVT_LEFT_DOWN, forward_event)
            self._opengl_canvas.Bind(wx.EVT_LEFT_UP, forward_event)
            self._opengl_canvas.Bind(wx.EVT_MOTION, forward_event)
            self._opengl_canvas.Bind(wx.EVT_MOUSEWHEEL, forward_event)
            self._opengl_canvas.Bind(wx.EVT_SIZING, self.resize)
        elif Canvas_Type == GLCanvas:
            super().__init__(
                parent,
                display_attributes,
                size=parent.GetClientSize(),
                style=wx.WANTS_CHARS,
            )
            self._opengl_canvas = self
        else:
            raise NotImplementedError

        # Amulet-Team/Amulet-Map-Editor#84
        # Amulet-Team/Amulet-Map-Editor#597
        # Amulet-Team/Amulet-Map-Editor#856
        def gl3() -> Optional[GLContext]:
            ctx_attrs = GLContextAttrs()
            ctx_attrs.PlatformDefaults()
            ctx_attrs.OGLVersion(3, 3)
            ctx_attrs.CoreProfile()
            ctx_attrs.EndList()
            ctx = GLContext(self._opengl_canvas, ctxAttrs=ctx_attrs)
            if ctx.IsOK():
                return ctx
            return None

        def gl2() -> Optional[GLContext]:
            ctx_attrs = GLContextAttrs()
            ctx_attrs.PlatformDefaults()
            ctx_attrs.OGLVersion(2, 1)
            ctx_attrs.CompatibilityProfile()
            ctx_attrs.EndList()
            ctx = GLContext(self._opengl_canvas, ctxAttrs=ctx_attrs)
            if ctx.IsOK() and glInitExplicitAttribLocationARB():
                return ctx
            return None

        context_constructors: list[Callable[[], Optional[GLContext]]] = [gl3, gl2]
        context = next((constructor() for constructor in context_constructors), None)
        if context is None:
            raise Exception(f"Failed setting up context")

        self._context = context
        self._init = False

        self.Bind(wx.EVT_SHOW, self._on_show)
    
    def resize(self, event):
        self._opengl_canvas.SetCurrent(self._context)
        glViewport(0, 0, event.GetSize().x, event.GetSize().y)

    @property
    def context(self) -> GLContext:
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
        self._opengl_canvas.SetCurrent(self._context)
        gl_version = glGetString(GL_VERSION)
        if isinstance(gl_version, bytes):
            gl_version = gl_version.decode("utf-8")
        log.info(f"OpenGL Version {gl_version}")
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
