import wx
from wx import glcanvas
from OpenGL.GL import *
import sys
import os
import math
from amulet_map_editor.amulet_wx.world_manager import BaseWorldTool

from .render_world import RenderWorld, RenderChunk
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
        self.world_panel = parent
        self.keys_pressed = set()
        super().__init__(parent, -1, size=parent.parent_frame.GetClientSize())
        self.context = glcanvas.GLContext(self)
        self.SetCurrent(self.context)
        glClearColor(0.5, 0.5, 0.5, 1.0)
        glEnable(GL_DEPTH_TEST)
        # glDisable(GL_CULL_FACE)
        glDepthFunc(GL_LESS)

        resource_packs = [minecraft_model_reader.JavaRP(rp) for rp in sys.argv[1:] if os.path.isdir(rp)]
        resource_pack = minecraft_model_reader.JavaRPHandler(resource_packs)

        self.render_world = RenderWorld(world, resource_pack)

        self.draw_timer = wx.Timer(self)
        self.input_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._on_draw, self.draw_timer)
        self.Bind(wx.EVT_TIMER, self.do_input_commands, self.input_timer)

        self.world_panel.Bind(wx.EVT_SIZE, self._on_resize)

        self.Bind(wx.EVT_KEY_DOWN, self.on_key_press)
        self.Bind(wx.EVT_KEY_UP, self.on_key_release)
        self.Bind(wx.EVT_MOUSEWHEEL, self._mouse_wheel)

    def enable(self):
        self.draw_timer.Start(33)
        self.input_timer.Start(33)

    def disable(self):
        self.draw_timer.Stop()
        self.input_timer.Stop()

    def close(self):
        pass

    def _mouse_wheel(self, evt):
        self.render_world.camera_move_speed += evt.GetWheelRotation()/evt.GetWheelDelta()
        if self.render_world.camera_move_speed < 0.1:
            self.render_world.camera_move_speed = 0.1
        evt.Skip()

    def do_input_commands(self, event):
        if key_map['up'] in self.keys_pressed:
            self.render_world.camera_location[1] += self.render_world.camera_move_speed
        if key_map['down'] in self.keys_pressed:
            self.render_world.camera_location[1] -= self.render_world.camera_move_speed
        if key_map['forwards'] in self.keys_pressed:
            self.render_world.camera_location[1] -= self.render_world.camera_move_speed * math.sin(math.radians(self.render_world.camera_rotation[0]))
            self.render_world.camera_location[0] += self.render_world.camera_move_speed * math.cos(math.radians(self.render_world.camera_rotation[0])) * math.sin(math.radians(self.render_world.camera_rotation[1]))
            self.render_world.camera_location[2] -= self.render_world.camera_move_speed * math.cos(math.radians(self.render_world.camera_rotation[0])) * math.cos(math.radians(self.render_world.camera_rotation[1]))
        if key_map['backwards'] in self.keys_pressed:
            self.render_world.camera_location[1] += self.render_world.camera_move_speed * math.sin(math.radians(self.render_world.camera_rotation[0]))
            self.render_world.camera_location[0] -= self.render_world.camera_move_speed * math.cos(math.radians(self.render_world.camera_rotation[0])) * math.sin(math.radians(self.render_world.camera_rotation[1]))
            self.render_world.camera_location[2] += self.render_world.camera_move_speed * math.cos(math.radians(self.render_world.camera_rotation[0])) * math.cos(math.radians(self.render_world.camera_rotation[1]))
        if key_map['left'] in self.keys_pressed:
            self.render_world.camera_location[0] -= self.render_world.camera_move_speed * math.cos(math.radians(self.render_world.camera_rotation[1]))
            self.render_world.camera_location[2] -= self.render_world.camera_move_speed * math.sin(math.radians(self.render_world.camera_rotation[1]))
        if key_map['right'] in self.keys_pressed:
            self.render_world.camera_location[0] += self.render_world.camera_move_speed * math.cos(math.radians(self.render_world.camera_rotation[1]))
            self.render_world.camera_location[2] += self.render_world.camera_move_speed * math.sin(math.radians(self.render_world.camera_rotation[1]))

        if key_map['look_left'] in self.keys_pressed:
            self.render_world.camera_rotation[1] -= self.render_world.camera_move_speed
        if key_map['look_right'] in self.keys_pressed:
            self.render_world.camera_rotation[1] += self.render_world.camera_move_speed
        if key_map['look_up'] in self.keys_pressed:
            self.render_world.camera_rotation[0] -= self.render_world.camera_rotate_speed
            if self.render_world.camera_rotation[0] < -90:
                self.render_world.camera_rotation[0] = -90
        if key_map['look_down'] in self.keys_pressed:
            self.render_world.camera_rotation[0] += self.render_world.camera_rotate_speed
            if self.render_world.camera_rotation[0] > 90:
                self.render_world.camera_rotation[0] = 90

    def on_key_release(self, event):
        key = event.GetUnicodeKey()
        if key == wx.WXK_NONE:
            key = event.GetKeyCode()
        self.keys_pressed.remove(key)

    def on_key_press(self, event):
        key = event.GetUnicodeKey()
        if key == wx.WXK_NONE:
            key = event.GetKeyCode()
        self.keys_pressed.add(key)

    def _on_resize(self, event):
        width, height = event.GetSize()
        self.set_size(width, height)

    def set_size(self, width, height):
        glViewport(0, 0, width, height)
        if height > 0:
            self.render_world.projection[1] = width / height
        else:
            self.render_world.projection[1] = 1

    def _on_draw(self, event):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.render_world.draw(self.render_world.transformation_matrix)
        self.SwapBuffers()


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

        self.Bind(wx.EVT_SIZE, self.OnResize)

    def OnResize(self, event):
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
        print(self.GetSize())
        self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        self._canvas.enable()

    def disable(self):
        if self._canvas is not None:
            self._canvas.disable()

    def close(self):
        if self._canvas is not None:
            self._canvas.close()


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
