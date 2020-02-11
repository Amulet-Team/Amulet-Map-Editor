import wx
from wx import glcanvas
from OpenGL.GL import *
import sys
import os
from amulet_map_editor.amulet_wx.world_manager import BaseWorldTool

from .render_world import RenderWorld
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from amulet.api.world import World
import minecraft_model_reader


key_map = {
    'up': wx.WXK_SPACE,
    'down': wx.WXK_SHIFT,
    'forwards': 87,
    'backwards': 83,
    'left': 65,
    'right': 68,

    'look_left': 74,
    'look_right': 76,
    'look_up': 73,
    'look_down': 75,
}


class World3dCanvas(glcanvas.GLCanvas):
    def __init__(self, parent: 'World3DPanel', world: 'World'):
        self._world_panel = parent
        self._keys_pressed = set()
        super().__init__(parent, -1, size=parent.parent_frame.GetClientSize())
        self._context = glcanvas.GLContext(self)
        self.SetCurrent(self._context)
        glClearColor(0.5, 0.5, 0.5, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LESS)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        resource_packs = [minecraft_model_reader.JavaRP(rp) for rp in sys.argv[1:] if os.path.isdir(rp)]
        resource_pack = minecraft_model_reader.JavaRPHandler(resource_packs)

        self._render_world = RenderWorld(world, resource_pack)

        self._draw_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._on_draw, self._draw_timer)

        self._input_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._process_inputs, self._input_timer)

        self._gc_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._gc, self._gc_timer)

        self._world_panel.Bind(wx.EVT_SIZE, self._on_resize)

        self.Bind(wx.EVT_KEY_DOWN, self._on_key_press)
        self.Bind(wx.EVT_KEY_UP, self._on_key_release)
        self.Bind(wx.EVT_MOUSEWHEEL, self._mouse_wheel)

    def enable(self):
        self._draw_timer.Start(33)
        self._input_timer.Start(33)
        self._gc_timer.Start(1000)

    def disable(self):
        self._draw_timer.Stop()
        self._input_timer.Stop()
        self._gc_timer.Stop()
        self._render_world.run_garbage_collector(True)

    def close(self):
        self._render_world.close()

    def is_closeable(self):
        return self._render_world.is_closeable()

    def _mouse_wheel(self, evt):
        self._render_world.camera_move_speed += evt.GetWheelRotation() / evt.GetWheelDelta()
        if self._render_world.camera_move_speed < 0.1:
            self._render_world.camera_move_speed = 0.1
        evt.Skip()

    def _process_inputs(self, evt):
        forward, up, right, pitch, yaw = 0, 0, 0, 0, 0
        if key_map['up'] in self._keys_pressed:
            up += 1
        if key_map['down'] in self._keys_pressed:
            up -= 1
        if key_map['forwards'] in self._keys_pressed:
            forward += 1
        if key_map['backwards'] in self._keys_pressed:
            forward -= 1
        if key_map['left'] in self._keys_pressed:
            right -= 1
        if key_map['right'] in self._keys_pressed:
            right += 1

        if key_map['look_left'] in self._keys_pressed:
            yaw -= 1
        if key_map['look_right'] in self._keys_pressed:
            yaw += 1
        if key_map['look_up'] in self._keys_pressed:
            pitch -= 1
        if key_map['look_down'] in self._keys_pressed:
            pitch += 1
        self._render_world.move_camera(forward, up, right, pitch, yaw)
        evt.Skip()

    def _on_key_release(self, event):
        key = event.GetUnicodeKey()
        if key == wx.WXK_NONE:
            key = event.GetKeyCode()
        if key in self._keys_pressed:
            self._keys_pressed.remove(key)

    def _on_key_press(self, event):
        key = event.GetUnicodeKey()
        if key == wx.WXK_NONE:
            key = event.GetKeyCode()
        self._keys_pressed.add(key)

    def _on_resize(self, event):
        width, height = event.GetSize()
        self.set_size(width, height)

    def set_size(self, width, height):
        glViewport(0, 0, width, height)
        if height > 0:
            self._render_world.aspect_ratio = width / height
        else:
            self._render_world.aspect_ratio = 1

    def _on_draw(self, event):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self._render_world.draw()
        self.SwapBuffers()
        event.Skip()

    def _gc(self, event):
        self._render_world.run_garbage_collector()
        event.Skip()


class World3DPanel(BaseWorldTool):
    def __init__(self, parent: 'MainFrame', world: 'World'):
        self.parent_frame = parent
        super().__init__(parent)
        self._world = world
        self._canvas = None
        self._temp = wx.StaticText(
            self,
            wx.ID_ANY,
            'Please wait while the renderer loads',
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self._temp.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))

        self.Bind(wx.EVT_SIZE, self._on_resize)

    def _on_resize(self, event):
        if self._canvas is not None:
            self._canvas.SetSize(self.GetSize()[0], self.GetSize()[1])
        event.Skip()

    def enable(self):
        if self._canvas is None:
            self.Update()
            self._canvas = World3dCanvas(self, self._world)
            self._temp.Destroy()
            self.GetParent().Layout()
            self.Update()
        self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        self._canvas.enable()

    def disable(self):
        if self._canvas is not None:
            self._canvas.disable()

    def close(self):
        if self._canvas is not None:
            self._canvas.close()

    def is_closeable(self):
        if self._canvas is not None:
            return self._canvas.is_closeable()
        return True


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
