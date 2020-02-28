import wx
from wx import glcanvas
from OpenGL.GL import *
import sys
import os
from amulet_map_editor.amulet_wx.world_manager import BaseWorldTool
from amulet_map_editor.amulet_wx.wx_util import SimplePanel
from amulet.api.block import Block

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
    def __init__(self, world_panel: 'World3DPanel', world: 'World'):
        self._keys_pressed = set()
        super().__init__(world_panel, -1, size=world_panel.GetClientSize())
        self._context = glcanvas.GLContext(self)
        self.SetCurrent(self._context)
        glClearColor(0.5, 0.5, 0.5, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LEQUAL)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        os.makedirs('resource_packs', exist_ok=True)
        if not os.path.isfile('resource_packs/readme.txt'):
            with open('resource_packs/readme.txt', 'w') as f:
                f.write('Put the Java resource pack you want loaded in here.')

        resource_packs = [minecraft_model_reader.java_vanilla_latest] + \
                         [minecraft_model_reader.JavaRP(rp) for rp in os.listdir('resource_packs') if os.path.isdir(rp)] + \
                         [minecraft_model_reader.java_vanilla_fix, minecraft_model_reader.JavaRP(os.path.join(os.path.dirname(__file__), 'amulet_resource_pack'))]
        resource_pack = minecraft_model_reader.JavaRPHandler(resource_packs)

        self._render_world = RenderWorld(world, resource_pack)

        self._draw_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._on_draw, self._draw_timer)

        self._input_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._process_inputs, self._input_timer)

        self._gc_timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self._gc, self._gc_timer)

        world_panel.Bind(wx.EVT_SIZE, self._on_resize)

        self.Bind(wx.EVT_KEY_DOWN, self._on_key_press)
        self.Bind(wx.EVT_KEY_UP, self._on_key_release)
        self.Bind(wx.EVT_MOUSEWHEEL, self._mouse_wheel)
        self.Bind(wx.EVT_KILL_FOCUS, self._on_loss_focus)

        self._mouse_x = 0
        self._mouse_y = 0
        self._last_mouse_x = 0
        self._last_mouse_y = 0
        self._mouse_lock = False
        self.Bind(wx.EVT_MIDDLE_UP, self._toggle_mouse_lock)
        self.Bind(wx.EVT_MOTION, self._on_mouse_motion)

    def enable(self):
        self._render_world.enable()
        self._draw_timer.Start(33)
        self._input_timer.Start(33)
        self._gc_timer.Start(10000)

    def disable(self):
        self._draw_timer.Stop()
        self._input_timer.Stop()
        self._gc_timer.Stop()
        self._render_world.disable()

    def close(self):
        self._render_world.close()

    def is_closeable(self):
        return self._render_world.is_closeable()

    def _mouse_wheel(self, evt):
        self._render_world.camera_move_speed += 0.2 * evt.GetWheelRotation() / evt.GetWheelDelta()
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

        pitch = (self._mouse_y - self._last_mouse_y) * 0.07
        yaw = (self._mouse_x - self._last_mouse_x) * 0.07
        self._last_mouse_x, self._last_mouse_y = self._mouse_x, self._mouse_y
        if self._mouse_lock:
            self._last_mouse_x, self._last_mouse_y = self.GetSize()[0]/2, self.GetSize()[1]/2
            self.WarpPointer(self._last_mouse_x, self._last_mouse_y)
        self._render_world.move_camera(forward, up, right, pitch, yaw)
        evt.Skip()

    def _toggle_mouse_lock(self, evt):
        if self._mouse_lock:
            self._release_mouse()
        else:
            self.CaptureMouse()
            wx.SetCursor(wx.Cursor(wx.CURSOR_BLANK))
            self._mouse_x, self._mouse_y = self._last_mouse_x, self._last_mouse_y = evt.GetPosition()
            self._mouse_lock = True

    def _release_mouse(self):
        wx.SetCursor(wx.NullCursor)
        try:
            self.ReleaseMouse()
        except:
            pass
        self._mouse_lock = False

    def _on_mouse_motion(self, evt):
        if self._mouse_lock:
            self._mouse_x, self._mouse_y = evt.GetPosition()

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

    def _on_loss_focus(self, evt):
        self._keys_pressed.clear()
        self._release_mouse()
        evt.Skip()

    def _on_resize(self, event):
        self.set_size(*event.GetSize())

    def set_size(self, width, height):
        glViewport(0, 0, width, height)
        if height > 0:
            self._render_world.aspect_ratio = width / height
        else:
            self._render_world.aspect_ratio = 1
        self.DoSetSize(0, 0, width, height, 0)  # I don't know if this is how you are supposed to do this

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
        super().__init__(parent, wx.HORIZONTAL)
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
        self._menu = None
        self._menu_buttons = []
        self._temp.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        self.Bind(wx.EVT_SIZE, self._on_resize)

    def _on_resize(self, event):
        if self._canvas is not None:
            self._canvas.SetSize(self.GetSize()[0], self.GetSize()[1])
        event.Skip()

    def _set_stone(self, evt):
        cx, cz = int(self._canvas._render_world._camera[0])>>4, int(self._canvas._render_world._camera[2])>>4
        y = int(self._canvas._render_world._camera[1])
        if 0 <= y <= 255:
            chunk = self._world.get_chunk(cx, cz, self._canvas._render_world._dimension)
            chunk.blocks[:, y, :] = self._world.palette.get_add_block(
                Block(
                    namespace='universal_minecraft',
                    base_name='stone'
                )
            )
            chunk.changed = True
            self._world._chunk_history_manager.create_snapshot(self._world._chunk_cache)

    def _undo_event(self, evt):
        print('undo')
        self._world.undo()

    def _redo_event(self, evt):
        print('redo')
        self._world.redo()

    def _save_event(self, evt):
        print('save')
        self._world.save()

    def enable(self):
        if self._canvas is None:
            self.Update()
            self._menu = SimplePanel(self)
            self.add_object(self._menu, 0, wx.EXPAND)

            for text, operation in [
                ['undo', self._undo_event],
                ['redo', self._redo_event],
                ['save', self._save_event],
                ['fill_blocks', self._set_stone]
            ]:
                button = wx.Button(
                    self._menu,
                    wx.ID_ANY,
                    text,
                    wx.DefaultPosition,
                    wx.DefaultSize,
                    0,
                )
                button.Bind(wx.EVT_BUTTON, operation)
                self._menu.add_object(button, 0)
                self._menu_buttons.append(
                    button
                )
            self._canvas = World3dCanvas(self, self._world)
            self.add_object(self._canvas, 0, wx.EXPAND)
            self._temp.Destroy()
            self.GetParent().Layout()
            self._menu.Fit()
            self.Update()
        self._canvas.set_size(self.GetSize()[0], self.GetSize()[1])
        self._canvas.enable()

    def disable(self):
        if self._canvas is not None:
            self._canvas.disable()

    def close(self):
        self.disable()
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
