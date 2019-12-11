import wx
from wx import glcanvas
from OpenGL.GL import *
import sys
from amulet_renderer.render_chunk import RenderChunk


class World3dCanvas(glcanvas.GLCanvas):
    def __init__(self, parent: 'World3DPanel'):
        self.world_panel = parent
        super().__init__(parent, -1, size=parent.parent_frame.GetClientSize())
        self.context = glcanvas.GLContext(self)
        self.SetCurrent(self.context)

        model = RenderChunk()

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
