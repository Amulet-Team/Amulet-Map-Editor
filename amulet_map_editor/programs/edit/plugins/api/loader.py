import os
import glob
import importlib.util
from amulet import log
from typing import Dict, List, TYPE_CHECKING, Callable, Optional, Type
import wx
import struct
import hashlib

from .fixed_pipeline import FixedFunctionUI
from .operation_ui import OperationUI, OperationUIType
from .data_types import OperationStorageType

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas import EditCanvas
    from amulet.api.world import World


STOCK_PLUGINS_DIR = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)), "stock_plugins"))
CUSTOM_PLUGINS_DIR = os.path.abspath("plugins")


class OperationLoadException(Exception):
    """Exception for internal use"""
    pass


class OperationLoader:
    """A class to handle loading and reloading operations from their python modules/packages"""
    def __init__(
            self,
            export_dict: dict,
            path: str
    ):
        self._path = path
        self._name = ""
        self._ui: Optional[Callable[[wx.Window, "EditCanvas", "World"], OperationUI]] = None
        self._load(export_dict)

    def _load(self, export_dict: dict):
        if not isinstance(export_dict, dict):
            raise OperationLoadException("Export must be a dictionary.")

        if "name" in export_dict:
            self._name = export_dict["name"]
            if not isinstance(self.name, str):
                raise OperationLoadException('"name" in export must exist and be a string.')
        else:
            raise OperationLoadException('"name" is not defined in export.')

        options_path = os.path.abspath(
            os.path.join(
                "config",
                "edit_plugins",
                f"""{self._name}_{
                    struct.unpack(
                        "H",
                        hashlib.sha1(
                            self._path.encode('utf-8')
                        ).digest()[:2]
                    )[0]
                }"""  # generate a file name that identifiable to the operation but "unique" to the path
            )
        )

        mode = export_dict.get("mode", "fixed")
        if not isinstance(mode, str):
            raise OperationLoadException('"name" in export is not a string.')

        if mode == "fixed":
            operation = export_dict.get("operation", None)
            if not callable(operation):
                raise OperationLoadException('"operation" in export must be callable.')
            if operation.__code__.co_argcount != 4:
                raise OperationLoadException('"operation" function in export must have 4 inputs.')
            options = export_dict.get("options", {})
            if not isinstance(options, dict):
                raise OperationLoadException('"operation" in export must be a dictionary if defined.')
            self._ui = lambda parent, canvas, world: FixedFunctionUI(parent, canvas, world, options_path, operation, options)
        elif mode == "dynamic":
            operation_ui: Type[OperationUI] = export_dict.get("operation", None)
            if not issubclass(operation_ui, OperationUI):
                raise OperationLoadException('"operation" must be a subclass of edit.plugins.OperationUI.')
            if not issubclass(operation_ui, (wx.Window, wx.Sizer)):
                raise OperationLoadException('"operation" must be a subclass of wx.Window or wx.Sizer.')
            self._ui = lambda parent, canvas, world: operation_ui(parent, canvas, world, options_path)
        else:
            raise OperationLoadException('"mode" in export must be either "fixed" or "dynamic".')

    @property
    def name(self) -> str:
        return self._name

    def __call__(self, parent: wx.Window, canvas: "EditCanvas", world: "World") -> OperationUIType:
        return self._ui(parent, canvas, world)


def _load_module_file(module_path: str):
    spec = importlib.util.spec_from_file_location(
        os.path.basename(module_path), module_path
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _load_module_directory(module_path):
    import sys

    spec = importlib.util.spec_from_file_location(
        os.path.basename(os.path.dirname(module_path)), module_path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def parse_export(plugin: dict, operations_dict: Dict[str, OperationLoader], path: str):
    try:
        operations_dict[path] = OperationLoader(plugin, path)
    except OperationLoadException as e:
        log.error(f"Error loading plugin {path}. {e}")
    except Exception as e:
        log.error(f"Exception loading plugin {path}. {e}")


def _load_operations(operations_: OperationStorageType, path: str):
    """load all operations from a specified directory"""
    if os.path.isdir(path):
        for fpath in glob.iglob(os.path.join(path, "*.py")):
            if fpath.endswith("__init__.py"):
                continue

            mod = _load_module_file(fpath)
            if hasattr(mod, "export"):
                plugin = getattr(mod, "export")
                parse_export(plugin, operations_, fpath)
            elif hasattr(mod, "exports"):
                for plugin in getattr(mod, "exports"):
                    parse_export(plugin, operations_, fpath)

        for dpath in glob.iglob(os.path.join(path, "**", "__init__.py")):
            mod = _load_module_directory(dpath)
            if hasattr(mod, "export"):
                plugin = getattr(mod, "export")
                parse_export(
                    plugin, operations_, os.path.basename(os.path.dirname(dpath))
                )
            elif hasattr(mod, "exports"):
                for plugin in getattr(mod, "exports"):
                    parse_export(
                        plugin, operations_, os.path.basename(os.path.dirname(dpath))
                    )


def _load_operations_group(dir_paths: List[str]):
    """Load operations from a list of directory paths"""
    operations_: OperationStorageType = {}
    for dir_path in dir_paths:
        _load_operations(operations_, dir_path)
    return operations_


all_operations: OperationStorageType = {}
internal_operations: OperationStorageType = {}
operations: OperationStorageType = {}
export_operations: OperationStorageType = {}
import_operations: OperationStorageType = {}
_meta: Dict[str, OperationStorageType] = {
    'internal_operations': internal_operations,
    'operations': operations,
    'export_operations': export_operations,
    'import_operations': import_operations
}
_public = {
    'operations',
    'export_operations',
    'import_operations'
}


def merge_operations():
    """Merge all loaded operations into all_operations"""
    all_operations.clear()
    for ops in _meta.values():
        all_operations.update(ops)


def _reload_operation_name(dir_name):
    """reload all operations in a directory name."""
    if dir_name in _public:
        os.makedirs(os.path.join("plugins", dir_name), exist_ok=True)
    _meta[dir_name].clear()
    name_operations = _load_operations_group(
        [os.path.join(STOCK_PLUGINS_DIR, dir_name)] +
        [os.path.join(CUSTOM_PLUGINS_DIR, dir_name)] * (dir_name in _public)
    )
    _meta[dir_name].update(name_operations)


def reload_operations():
    """Reload all operations"""
    for dir_name in _meta.keys():
        _reload_operation_name(dir_name)
    merge_operations()


reload_operations()
