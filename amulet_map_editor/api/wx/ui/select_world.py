import os
import wx
import glob
from sys import platform
from typing import List, Dict, Tuple, Callable, TYPE_CHECKING
import traceback

from amulet import load_format
from amulet.api.errors import FormatError

from amulet_map_editor import lang, log, CONFIG
from amulet_map_editor.api.wx.ui import simple
from amulet_map_editor.api.wx.util.ui_preferences import preserve_ui_preferences


if TYPE_CHECKING:
    from amulet.api.wrapper import WorldFormatWrapper


# Windows 	%APPDATA%\.minecraft
# macOS 	~/Library/Application Support/minecraft
# Linux 	~/.minecraft


def get_java_dir():
    if platform == "win32":
        return os.path.join(os.getenv("APPDATA"), ".minecraft")
    elif platform == "darwin":
        return os.path.expanduser("~/Library/Application Support/minecraft")
    else:
        return os.path.expanduser("~/.minecraft")


def get_java_saves_dir():
    return os.path.join(get_java_dir(), "saves")


minecraft_world_paths = {lang.get("world.java_platform"): get_java_saves_dir()}

if platform == "win32":
    minecraft_world_paths[lang.get("world.bedrock_platform")] = os.path.join(
        os.getenv("LOCALAPPDATA"),
        "Packages",
        "Microsoft.MinecraftUWP_8wekyb3d8bbwe",
        "LocalState",
        "games",
        "com.mojang",
        "minecraftWorlds",
    )

world_images: Dict[str, Tuple[int, wx.Bitmap, int]] = {}


def get_world_image(image_path: str) -> Tuple[wx.Bitmap, int]:
    if (
        image_path not in world_images
        or world_images[image_path][0] != os.stat(image_path)[8]
    ):
        img = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
        width = min((img.GetWidth() / img.GetHeight()) * 128, 300)

        world_images[image_path] = (
            os.stat(image_path)[8],
            img.Scale(width, 128, wx.IMAGE_QUALITY_NEAREST).ConvertToBitmap(),
            width,
        )

    return world_images[image_path][1:3]


class WorldUI(simple.SimplePanel):
    # UI element that holds the world image, name and description
    def __init__(self, parent: simple.SimplePanel, world_format: "WorldFormatWrapper"):
        super(WorldUI, self).__init__(parent, wx.HORIZONTAL)
        self.SetWindowStyle(wx.TAB_TRAVERSAL | wx.BORDER_RAISED)

        img, width = get_world_image(world_format.world_image_path)

        self.img = wx.StaticBitmap(self, wx.ID_ANY, img, (0, 0), (width, 128))
        # self.img.SetScaleMode(2)
        self.add_object(self.img, 0)

        self.world_name = wx.StaticText(
            self,
            wx.ID_ANY,
            "\n".join(
                [
                    world_format.world_name,
                    world_format.game_version_string,
                    os.path.join(
                        *os.path.normpath(world_format.path).split(os.sep)[-3:]
                    ),
                ]
            ),
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.add_object(self.world_name, 0)


class WorldUIButton(WorldUI):
    # a button that wraps around WorldUI so that WorldUI can be used without the button functionality
    def __init__(
        self,
        parent: simple.SimplePanel,
        world_format: "WorldFormatWrapper",
        open_world_callback,
    ):
        super(WorldUIButton, self).__init__(parent, world_format)
        self.path = world_format.path
        self.open_world_callback = open_world_callback

        self.Bind(wx.EVT_LEFT_UP, self._call_callback)
        self.img.Bind(wx.EVT_LEFT_UP, self._call_callback)
        self.world_name.Bind(wx.EVT_LEFT_DOWN, self._call_callback)

    def _call_callback(self, evt):
        self.open_world_callback(self.path)


class WorldList(simple.SimplePanel):
    def __init__(self, parent, world_dirs, open_world_callback, sort=True):
        super(WorldList, self).__init__(parent)

        self.worlds = []

        world_formats = []
        for world_path in world_dirs:
            if os.path.isdir(world_path):
                try:
                    world_formats.append(load_format(world_path))
                except FormatError as e:
                    log.info(f"Could not find loader for {world_path} {e}")
                except Exception:
                    log.error(
                        f"Error loading format wrapper for {world_path} {traceback.format_exc()}"
                    )
        if sort:
            world_formats = reversed(sorted(world_formats, key=lambda f: f.last_played))

        for world_format in world_formats:
            try:
                world_button = WorldUIButton(self, world_format, open_world_callback)
                self.add_object(world_button, 0, wx.ALL | wx.EXPAND)
                self.worlds.append(world_button)
            except Exception as e:
                log.info(f"Failed to display world button for {world_format.path} {e}")

        self.Layout()


class CollapseableWorldListUI(wx.CollapsiblePane):
    # a drop down list of `WorldUIButton`s for a given directory
    def __init__(self, parent, paths: List[str], group_name: str, open_world_callback):
        # TODO: perhaps design a custom version of this. It looks kind of ugly on windows
        super(CollapseableWorldListUI, self).__init__(parent, wx.ID_ANY, group_name)
        self.parent = parent
        self.Bind(wx.EVT_COLLAPSIBLEPANE_CHANGED, self.eval_layout)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)

        panel = self.GetPane()
        panel.sizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(panel.sizer)
        panel.sizer.Add(WorldList(panel, paths, open_world_callback), 0, wx.EXPAND)

    def eval_layout(self, evt):
        self.Layout()
        self.parent.FitInside()
        evt.Skip()


class ScrollableWorldsUI(simple.SimpleScrollablePanel):
    # a frame to allow scrolling
    def __init__(self, parent, open_world_callback):
        super(ScrollableWorldsUI, self).__init__(parent)
        self.open_world_callback = open_world_callback

        self.dirs: Dict[str, CollapseableWorldListUI] = {}
        self.reload()

        self.Layout()

    def reload(self):
        for val in self.dirs.values():
            val.Destroy()
        self.dirs.clear()
        for group_name, directory in minecraft_world_paths.items():
            if os.path.isdir(directory):
                world_list = CollapseableWorldListUI(
                    self,
                    glob.glob(os.path.join(glob.escape(directory), "*")),
                    group_name,
                    self.open_world_callback,
                )
                self.add_object(world_list, 0, wx.EXPAND)
                self.dirs[directory] = world_list

    def OnChildFocus(self, event):
        event.Skip()


class WorldSelectUI(simple.SimplePanel):
    # a frame containing a refresh button for the UI, a sort order for the worlds
    # and a vertical list of `WorldDirectoryUI`s for each directory
    # perhaps also a select directory option
    def __init__(self, parent, open_world_callback):
        super(WorldSelectUI, self).__init__(parent)
        self.open_world_callback = open_world_callback
        self.header = simple.SimplePanel(self, wx.HORIZONTAL)
        self.header_open_world = wx.Button(
            self.header, wx.ID_ANY, label=lang.get("select_world.open_world_button")
        )
        self.header_open_world.Bind(wx.EVT_BUTTON, self._open_world)
        self.header.add_object(self.header_open_world)
        self.add_object(self.header, 0, 0)

        self.content = ScrollableWorldsUI(self, open_world_callback)
        self.add_object(self.content, 1, wx.EXPAND)

    def _open_world(self, evt):
        dir_dialog = wx.DirDialog(
            None,
            lang.get("select_world.open_world_dialogue"),
            "",
            wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST,
        )
        try:
            if dir_dialog.ShowModal() == wx.ID_CANCEL:
                return
            path = dir_dialog.GetPath()
        except Exception:
            wx.LogError(lang.get("select_world.select_directory_failed"))
            return
        finally:
            dir_dialog.Destroy()
        self.open_world_callback(path)


class RecentWorldUI(simple.SimplePanel):
    def __init__(self, parent, open_world_callback):
        super(RecentWorldUI, self).__init__(parent)
        self._open_world_callback = open_world_callback

        self.add_object(
            wx.StaticText(
                self,
                wx.ID_ANY,
                lang.get("select_world.recent_worlds"),
                wx.DefaultPosition,
                wx.DefaultSize,
                0,
            ),
            0,
            wx.ALL | wx.ALIGN_CENTER,
        )

        self._world_list = None
        self.rebuild()

    def rebuild(self, new_world: str = None):
        meta: dict = CONFIG.get("amulet_meta", {})
        recent_worlds: list = meta.setdefault("recent_worlds", [])
        if new_world is not None:
            while new_world in recent_worlds:
                recent_worlds.remove(new_world)
            recent_worlds.insert(0, new_world)
            while len(recent_worlds) > 5:
                recent_worlds.pop(5)
        if self._world_list is not None:
            self._world_list.Destroy()
        self._world_list = WorldList(
            self, recent_worlds, self._open_world_callback, sort=False
        )
        self.add_object(self._world_list, 1, wx.EXPAND)
        self.Layout()
        CONFIG.put("amulet_meta", meta)


class WorldSelectAndRecentUI(simple.SimplePanel):
    def __init__(self, parent, open_world_callback):
        super(WorldSelectAndRecentUI, self).__init__(parent, wx.HORIZONTAL)
        self._open_world_callback = open_world_callback
        self.add_object(WorldSelectUI(self, self._update_recent), 1, wx.ALL | wx.EXPAND)
        self._recent_worlds = RecentWorldUI(self, self._update_recent)
        self.add_object(self._recent_worlds, 1, wx.EXPAND)

    def _update_recent(self, path):
        self._recent_worlds.rebuild(path)
        self._open_world_callback(path)


@preserve_ui_preferences
class WorldSelectDialog(wx.Dialog):
    def __init__(self, parent: wx.Window, open_world_callback: Callable[[str], None]):
        super().__init__(
            parent,
            title="World Select",
            pos=wx.Point(50, 50),
            size=wx.Size(*[int(s * 0.95) for s in parent.GetSize()]),
            style=wx.CAPTION | wx.CLOSE_BOX | wx.MAXIMIZE_BOX
            # | wx.MAXIMIZE
            | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL | wx.CLIP_CHILDREN | wx.RESIZE_BORDER,
        )
        self.Bind(wx.EVT_CLOSE, self._hide_event)

        self._open_world_callback = open_world_callback
        self.world_select = WorldSelectAndRecentUI(self, self._run_callback)

    def _run_callback(self, path):
        self._close()
        self._open_world_callback(path)

    def _hide_event(self, evt):
        self._close()
        evt.Skip()

    def _close(self):
        if self.IsModal():
            self.EndModal(0)
        else:
            self.Close()
