from amulet_map_editor.amulet_wx.wx_util import SimpleNotebook, SimplePanel
import amulet

# this is where most of the magic will happen


class WorldManagerUI(SimpleNotebook):
    def __init__(self, parent, path):
        SimpleNotebook.__init__(
            self,
            parent
        )
        self.world = amulet.load_world(path)
        self.world_name = self.world.world_wrapper.world_name
        test = SimplePanel(self)
        self.AddPage(test, "test", True)

    def _load_extensions(self):
        pass