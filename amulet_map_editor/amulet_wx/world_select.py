import os
import wx
from amulet_map_editor import lang
import amulet
from amulet_map_editor.amulet_wx import wx_util

# Windows 	%APPDATA%\.minecraft
# macOS 	~/Library/Application Support/minecraft
# Linux 	~/.minecraft

java_dir = os.path.join(os.getenv('APPDATA'), '.minecraft', 'saves')
bedrock_dir = os.path.join(os.getenv('LOCALAPPDATA'), 'Packages', 'Microsoft.MinecraftUWP_8wekyb3d8bbwe', 'LocalState', 'games', 'com.mojang', 'minecraftWorlds')
# TODO: handle other OSs


minecraft_world_paths = {
    lang.get('java_platform'): java_dir,
    lang.get('bedrock_platform'): bedrock_dir
}


class WorldUI(wx_util.SimplePanel):
    # UI element that holds the world image, name and description
    def __init__(self, parent: 'WorldDirectoryUI', path: str):
        super(WorldUI, self).__init__(
            parent,
            wx.HORIZONTAL
        )

        world = amulet.load_format(path)

        parent.sizer.Add(
            self,
            0,
            wx.ALL,
            5
        )

        img = wx.Image(
            world.world_image_path,
            wx.BITMAP_TYPE_ANY
        ).ConvertToBitmap()

        self.img = wx.StaticBitmap(
            self,
            wx.ID_ANY,
            img,
            (0, 0),
            (128, 128)
        )
        # self.img.SetScaleMode(2)
        self.sizer.Add(self.img)

        self.world_name = wx.StaticText(
            self,
            wx.ID_ANY,
            world.world_name,
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.sizer.Add(self.world_name)


class WorldUIButton(WorldUI):
    # a button that wraps around WorldUI so that WorldUI can be used without the button functionality
    def __init__(self, parent: 'WorldDirectoryUI', path: str, open_world_callback):
        super(WorldUIButton, self).__init__(
            parent,
            path
        )
        self.path = path
        self.open_world_callback = open_world_callback

        self.Bind(wx.EVT_LEFT_UP, self._call_callback)
        self.img.Bind(wx.EVT_LEFT_UP, self._call_callback)
        self.world_name.Bind(wx.EVT_LEFT_UP, self._call_callback)

    def _call_callback(self, evt):
        self.open_world_callback(self.path)


class WorldDirectoryUI(wx.CollapsiblePane):
    # a drop down list of `WorldUIButton`s for a given directory
    def __init__(self, parent: 'WorldSelectUI', path: str, group_name: str, open_world_callback):
        super(WorldDirectoryUI, self).__init__(
            parent,
            wx.ID_ANY,
            group_name
        )
        self.parent = parent
        self.open_world_callback = open_world_callback
        parent.add_object(self)
        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.eval_layout)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        panel = self.GetPane()
        panel.sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(panel.sizer)

        self.worlds = []

        for world in os.listdir(path):
            world_path = os.path.join(path, world)
            if os.path.isdir(world_path):
                try:
                    self.worlds.append(WorldUIButton(panel, world_path, self.open_world_callback))
                except:
                    pass

    def eval_layout(self, evt):
        self.Layout()
        self.parent.FitInside()


class WorldSelectUI(wx_util.SimpleScrollablePanel):
    # a frame containing a refresh button for the UI, a sort order for the worlds
    # and a vertical list of `WorldDirectoryUI`s for each directory
    # perhaps also a select directory option
    def __init__(self, parent, open_world_callback):
        super(WorldSelectUI, self).__init__(
            parent
        )
        self.open_world_callback = open_world_callback

        self.dirs = {}
        self._reload()

        self.Layout()

    def _reload(self):
        # might need to remove them from the sizer first
        self.dirs.clear()
        for group_name, directory in minecraft_world_paths.items():
            if os.path.isdir(directory):
                self.dirs[directory] = WorldDirectoryUI(self, directory, group_name, self.open_world_callback)
