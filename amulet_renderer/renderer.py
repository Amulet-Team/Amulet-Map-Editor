import wx
from wx import glcanvas
from OpenGL.GL import *
from amulet_renderer import shaders
import numpy
import sys

vertex_shader = """
# version 330
in layout(location = 0) vec3 positions;
in layout(location = 1) vec3 colors;
out vec3 newColor;
void main(){
    gl_Position = vec4(positions, 1.0);
    newColor = colors;
}
"""

fragment_shader = """
# version 330
in vec3 newColor;
out vec4 outColor;
void main(){
    outColor = vec4(newColor, 1.0);
}
"""


class World3dCanvas(glcanvas.GLCanvas):
    def __init__(self, parent: 'World3DPanel'):
        self.world_panel = parent
        super().__init__(parent, -1, size=parent.parent_frame.GetClientSize())
        self.context = glcanvas.GLContext(self)
        self.SetCurrent(self.context)

        model = Geometry()

        self.Bind(wx.EVT_PAINT, self.OnDraw)
        self.world_panel.Bind(wx.EVT_SIZE, self.OnResize)

    def OnResize(self, event):
        size = event.GetSize()
        print(size)
        glViewport(0, 0, size[0], size[1])

    def OnDraw(self, event):
        glClear(GL_COLOR_BUFFER_BIT)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        self.SwapBuffers()


class Geometry:
    def __init__(self):
        self.main_shader = shaders.load_shader('render_chunk')
        self.create_geometry()

    def create_geometry(self):
        # triangle   vertices      colors
        triangle = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                    0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                    0.0, 0.5, 0.0, 0.0, 0.0, 1.0]

        triangle = numpy.array(triangle, dtype=numpy.float32)

        VBO = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, VBO)
        glBufferData(GL_ARRAY_BUFFER, len(triangle) * 4, triangle, GL_STATIC_DRAW)

        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)

        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
        glEnableVertexAttribArray(1)

        glClearColor(0.1, 0.15, 0.1, 1.0)

        glUseProgram(self.main_shader)


class World3DPanel(wx.Panel):
    def __init__(self, parent: 'MainFrame'):
        self.parent_frame = parent
        super().__init__(parent)
        self.canvas = World3dCanvas(self)


if __name__ == "__main__":
    class MainFrame(wx.Frame):
        def __init__(self):
            self.size = (400, 300)
            wx.Frame.__init__(self, None, title="3D World View", size=self.size,
                              style=wx.DEFAULT_FRAME_STYLE | wx.FULL_REPAINT_ON_RESIZE)
            self.SetMinSize(self.size)
            self.Bind(wx.EVT_CLOSE, self.on_close)

            self.panel = World3DPanel(self)

        def on_close(self, event):
            self.Destroy()
            sys.exit(0)


    class App(wx.App):
        def OnInit(self):
            frame = MainFrame()
            frame.Show()
            return True


    app = App()
    app.MainLoop()
