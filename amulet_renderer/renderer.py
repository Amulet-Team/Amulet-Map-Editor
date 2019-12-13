import wx
from wx import glcanvas
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
from amulet_renderer.render_world import RenderWorld, RenderChunk
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from amulet.api.world import World


class World3dCanvas(glcanvas.GLCanvas):
    def __init__(self, parent: 'World3DPanel', world: 'World'):
        self.world_panel = parent
        super().__init__(parent, -1, size=parent.parent_frame.GetClientSize())
        self.context = glcanvas.GLContext(self)
        self.SetCurrent(self.context)
        glClearColor(0.5, 0.5, 0.5, 1.0)
        glEnable(GL_DEPTH_TEST)
        glDepthFunc(GL_LESS)

        self.render_world = RenderWorld(world)

        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.OnDraw, self.timer)
        self.timer.Start(33)
        self.world_panel.Bind(wx.EVT_SIZE, self.OnResize)

    def OnResize(self, event):
        width, height = event.GetSize()
        glViewport(0, 0, width, height)
        self.render_world.projection[1] = width/height

    def OnDraw(self, event):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.render_world.draw(self.render_world.transformation_matrix)
        self.SwapBuffers()


class World3DPanel(wx.Panel):
    def __init__(self, parent: 'MainFrame', world: 'World'):
        self.parent_frame = parent
        super().__init__(parent)
        self.canvas = World3dCanvas(self, world)

        self.Bind(wx.EVT_SIZE, self.OnResize)

    def OnResize(self, event):
        self.canvas.SetSize(self.GetSize()[0], self.GetSize()[1])
        event.Skip()


if __name__ == "__main__":
    class MainFrame(wx.Frame):
        def __init__(self):
            self.size = (400, 300)
            wx.Frame.__init__(self, None, title="3D World View", size=self.size,
                              style=wx.DEFAULT_FRAME_STYLE | wx.FULL_REPAINT_ON_RESIZE)
            self.SetMinSize(self.size)
            self.Bind(wx.EVT_CLOSE, self.on_close)

            world_path = sys.argv[1]
            import amulet.world_interface
            world = amulet.world_interface.load_world(world_path)

            self.panel = World3DPanel(self, world)

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
