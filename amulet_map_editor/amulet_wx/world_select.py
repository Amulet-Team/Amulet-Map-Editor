import os
import wx
import glob
from typing import List, Dict, Tuple
from amulet_map_editor import lang, config
from amulet import world_interface
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

world_images = {}


def get_world_image(image_path: str) -> Tuple[wx.Image, int]:
    if image_path not in world_images or world_images[image_path][0] != os.stat(image_path)[8]:
        img = wx.Image(
            image_path,
            wx.BITMAP_TYPE_ANY
        )
        width = min((img.Width / img.Height) * 128, 300)

        world_images[image_path] = (
            os.stat(image_path)[8],
            img.Scale(width, 128, wx.IMAGE_QUALITY_NEAREST).ConvertToBitmap(),
            width
        )

    return world_images[image_path][1:3]


class WorldUI(wx_util.SimplePanel):
    # UI element that holds the world image, name and description
    def __init__(self, parent: wx_util.SimplePanel, path: str):
        super(WorldUI, self).__init__(
            parent,
            wx.HORIZONTAL
        )

        world = world_interface.load_format(path)

        self.BackgroundColour = (190, 190, 200)

        img, width = get_world_image(world.world_image_path)

        self.img = wx.StaticBitmap(
            self,
            wx.ID_ANY,
            img,
            (0, 0),
            (width, 128)
        )
        # self.img.SetScaleMode(2)
        self.add_object(self.img, 0)

        self.world_name = wx.StaticText(
            self,
            wx.ID_ANY,
            '\n'.join([
                world.world_name,
                world.game_version_string,
                os.path.join(*os.path.normpath(path).split(os.sep)[-3:])
            ]),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.add_object(self.world_name, 0)


class WorldUIButton(WorldUI):
    # a button that wraps around WorldUI so that WorldUI can be used without the button functionality
    def __init__(self, parent: wx_util.SimplePanel, path: str, open_world_callback):
        super(WorldUIButton, self).__init__(
            parent,
            path
        )
        self.path = path
        self.open_world_callback = open_world_callback

        self.Bind(wx.EVT_LEFT_UP, self._call_callback)
        self.img.Bind(wx.EVT_LEFT_UP, self._call_callback)
        self.world_name.Bind(wx.EVT_LEFT_DOWN, self._call_callback)

    def _call_callback(self, evt):
        self.open_world_callback(self.path)


class WorldList(wx_util.SimplePanel):
    def __init__(self, parent, world_dirs, open_world_callback):
        super(WorldList, self).__init__(
            parent
        )

        self.worlds = []

        for world_path in world_dirs:
            if os.path.isdir(world_path):
                try:
                    world_button = WorldUIButton(self, world_path, open_world_callback)
                    self.add_object(world_button, 0, wx.ALL | wx.EXPAND)
                    self.worlds.append(world_button)
                except:
                    pass
        self.Layout()


class CollapseableWorldListUI(wx.CollapsiblePane):
    # a drop down list of `WorldUIButton`s for a given directory
    def __init__(self, parent, paths: List[str], group_name: str, open_world_callback):
        # TODO: perhaps design a custom version of this. It looks kind of ugly on windows
        super(CollapseableWorldListUI, self).__init__(
            parent,
            wx.ID_ANY,
            group_name
        )
        self.parent = parent
        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.eval_layout)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        panel = self.GetPane()
        panel.sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(panel.sizer)
        panel.sizer.Add(
            WorldList(
                panel,
                paths,
                open_world_callback
            ),
            0,
            wx.EXPAND
        )

    def eval_layout(self, evt):
        self.Layout()
        self.parent.FitInside()
        evt.Skip()


class ScrollableWorldsUI(wx_util.SimpleScrollablePanel):
    # a frame to allow scrolling
    def __init__(self, parent, open_world_callback):
        super(ScrollableWorldsUI, self).__init__(
            parent
        )
        self.open_world_callback = open_world_callback

        self.dirs: Dict[str, CollapseableWorldListUI] = {}
        self.reload()

        self.Layout()

    def reload(self):
        # might need to remove them from the sizer first
        for val in self.dirs.values():
            val.Destroy()
        self.dirs.clear()
        for group_name, directory in minecraft_world_paths.items():
            if os.path.isdir(directory):
                world_list = CollapseableWorldListUI(self, glob.glob(os.path.join(directory, '*')), group_name, self.open_world_callback)
                self.add_object(world_list, 0, wx.EXPAND)
                self.dirs[directory] = world_list

    def OnChildFocus(self, event):
        event.Skip()


class WorldSelectUI(wx_util.SimplePanel):
    # a frame containing a refresh button for the UI, a sort order for the worlds
    # and a vertical list of `WorldDirectoryUI`s for each directory
    # perhaps also a select directory option
    def __init__(self, parent, open_world_callback):
        super(WorldSelectUI, self).__init__(
            parent
        )
        self.open_world_callback = open_world_callback
        self.header = wx_util.SimplePanel(self, wx.HORIZONTAL)
        self.header_open_world = wx.Button(self.header, wx.ID_ANY, label=lang.get('open_world_button'))
        self.header_open_world.Bind(wx.EVT_BUTTON, self._open_world)
        self.header.add_object(self.header_open_world)
        self.add_object(self.header, 0, 0)

        self.content = ScrollableWorldsUI(self, open_world_callback)
        self.add_object(self.content, 1, wx.EXPAND)

    def _open_world(self, evt):
        dir_dialog = wx.DirDialog(
            None,
            lang.get('open_world_dialogue'),
            "",
            wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,
        )
        try:
            if dir_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = dir_dialog.GetPath()
        except Exception:
            wx.LogError("select_directory_failed")
            return
        finally:
            dir_dialog.Destroy()
        self.open_world_callback(path)


class RecentWorldUI(wx_util.SimplePanel):
    def __init__(self, parent, open_world_callback):
        super(RecentWorldUI, self).__init__(
            parent
        )
        self._open_world_callback = open_world_callback

        self.add_object(
            wx.StaticText(
                self,
                wx.ID_ANY,
                lang.get('recent_worlds'),
                wx.DefaultPosition,
                wx.DefaultSize,
                0,
            ),
            0,
            wx.ALL | wx.ALIGN_CENTER
        )

        self._world_list = None
        self.rebuild()
        # self.Bind(wx.EVT_LEFT_UP, self._rebuild_evt)

    def _rebuild_evt(self, evt):
        print('hi')
        self.rebuild()

    def rebuild(self, new_world: str = None):
        recent_worlds = config.get('recent_worlds')
        if new_world is not None:
            if new_world not in recent_worlds:
                recent_worlds.insert(0, new_world)
            while len(recent_worlds) > 5:
                recent_worlds.pop(5)
        if self._world_list is not None:
            self._world_list.Destroy()
        self._world_list = WorldList(self, recent_worlds, self._open_world_callback)
        self.add_object(self._world_list, 1, wx.EXPAND)
        self.Layout()


class WorldSelectAndRecentUI(wx_util.SimplePanel):
    def __init__(self, parent, open_world_callback):
        super(WorldSelectAndRecentUI, self).__init__(
            parent,
            wx.HORIZONTAL
        )
        self._open_world_callback = open_world_callback
        self.add_object(WorldSelectUI(self, self._update_recent), 2, wx.ALL | wx.EXPAND)
        self._recent_worlds = RecentWorldUI(self, self._update_recent)
        self.add_object(self._recent_worlds, 1, wx.EXPAND)

    def _update_recent(self, path):
        self._recent_worlds.rebuild(path)
        self._open_world_callback(path)
