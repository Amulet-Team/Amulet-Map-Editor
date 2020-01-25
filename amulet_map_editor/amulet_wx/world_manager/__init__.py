import wx
import os
from amulet_map_editor.amulet_wx.wx_util import SimpleNotebook, SimplePanel
from amulet import world_interface
import importlib
import pkgutil

# this is where most of the magic will happen


class WorldManagerUI(SimpleNotebook):
    def __init__(self, parent, path, close_world_method):
        SimpleNotebook.__init__(
            self,
            parent
        )
        self.close_world_method = close_world_method
        self.Bind(wx.EVT_MIDDLE_DCLICK, self._close_self)
        self.world = world_interface.load_world(path)
        self.world_name = self.world.world_wrapper.world_name
        self._load_extensions()

    def _load_extensions(self):
        load()
        for extension_name, extension in _extensions:
            self.AddPage(extension(self, self.world), extension_name, True)

    def _close_self(self, evt):
        self.close_world_method(self)
        self.Destroy()


# class ExtensionTemplate(SimplePanel):
#     def __init__(self, container, world):
#         super(ExtensionTemplate, self).__init__(
#             container
#         )


_extensions = []


def load():
    _extensions.clear()
    for _, name, _ in pkgutil.iter_modules([os.path.join(os.path.dirname(__file__), 'extensions')]):
        # load module and confirm that all required attributes are defined
        module = importlib.import_module(f'amulet_map_editor.amulet_wx.world_manager.extensions.{name}')
        importlib.reload(module)

        if hasattr(module, 'export'):
            export = getattr(module, 'export')
            if 'ui' in export and issubclass(export['ui'], wx.Panel):
                _extensions.append([export.get('name', 'missingno'), export['ui']])
