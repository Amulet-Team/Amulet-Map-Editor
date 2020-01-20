import wx
from amulet_map_editor.amulet_wx.wx_util import SimpleNotebook, SimplePanel
import amulet

# this is where most of the magic will happen


class WorldManagerUI(SimpleNotebook):
    def __init__(self, parent, path, close_world_method):
        SimpleNotebook.__init__(
            self,
            parent
        )
        self.close_world_method = close_world_method
        self.Bind(wx.EVT_MIDDLE_DCLICK, self._close_self)
        self.world = amulet.load_world(path)
        self.world_name = self.world.world_wrapper.world_name
        test = SimplePanel(self)
        self.AddPage(test, "test", True)

    def _load_extensions(self):
        pass

    def _close_self(self, evt):
        self.close_world_method(self)
        self.Destroy()
