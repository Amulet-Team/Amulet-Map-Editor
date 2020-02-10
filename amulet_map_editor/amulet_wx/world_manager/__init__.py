import wx
import os
from typing import List
from amulet_map_editor.amulet_wx.wx_util import SimpleNotebook, SimplePanel
from amulet import world_interface
import importlib
import pkgutil

# this is where most of the magic will happen

_extensions: List['BaseWorldTool'] = []


def load_extensions():
    if not _extensions:
        for _, name, _ in pkgutil.iter_modules([os.path.join(os.path.dirname(__file__), 'extensions')]):
            # load module and confirm that all required attributes are defined
            module = importlib.import_module(f'amulet_map_editor.amulet_wx.world_manager.extensions.{name}')

            if hasattr(module, 'export'):
                export = getattr(module, 'export')
                if 'ui' in export and issubclass(export['ui'], BaseWorldTool):
                    _extensions.append([export.get('name', 'missingno'), export['ui']])


class WorldManagerUI(SimpleNotebook):
    def __init__(self, parent, path):
        SimpleNotebook.__init__(
            self,
            parent,
            wx.NB_LEFT
        )
        self.world = world_interface.load_world(path)
        self.world_name = self.world.world_wrapper.world_name
        self._load_extensions()

    def _load_extensions(self):
        load_extensions()
        for extension_name, extension in _extensions:
            self.AddPage(extension(self, self.world), extension_name, True)

    def close_world(self):
        self.GetParent().DeletePage(self.GetParent().FindPage(self))
        self.Destroy()
        for ext in self._extensions:
            ext.close()
        self.world.close()



class BaseWorldTool(SimplePanel):

    def enable(self):
        """Run when the panel is shown/enabled"""
        pass

    def disable(self):
        """Run when the panel is hidden/disabled"""
        pass

    def close(self):
        """Run when the world is closed"""
        pass
