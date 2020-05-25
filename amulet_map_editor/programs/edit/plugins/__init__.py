import os
import glob
import importlib.util
from amulet import log
from typing import Dict, List, TYPE_CHECKING, Callable, Any
import wx

if TYPE_CHECKING:
    from ..canvas import ControllableEditCanvas
    from amulet.api.world import World


PathType = str
OperationStorageType = Dict[PathType, "OperationLoader"]


class OperationUI:
    """The base class that all operations must inherit from."""
    pass


class FixedFunctionUI(OperationUI):
    def __init__(self, parent: wx.Window, canvas: "ControllableEditCanvas", world: "World", operation: Callable, options: Dict[str, Any]):
        super().__init__()
        # TODO


class OperationLoadException(Exception):
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
        self._ui = None
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
            self._ui = lambda parent, canvas, world: FixedFunctionUI(parent, canvas, world, operation, options)
        elif mode == "dynamic":
            operation = export_dict.get("operation", None)
            if not issubclass(operation, OperationUI):
                raise OperationLoadException('"operation" must be a subclass of edit.plugins.OperationUI.')
            self._ui = operation
        else:
            raise OperationLoadException('"mode" in export must be either "fixed" or "dynamic".')

    @property
    def name(self) -> str:
        return self._name

    def setup_ui(self, parent: wx.Window, canvas: "ControllableEditCanvas", world: "World"):
        self._ui(parent, canvas, world)


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

plugin_options: Dict[str, dict] = {}


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
        [os.path.join(os.path.dirname(__file__), dir_name)] +
        [os.path.join("plugins", dir_name)] * (dir_name in _public)
    )
    _meta[dir_name].update(name_operations)


def reload_operations():
    """Reload all operations"""
    for dir_name in _meta.keys():
        _reload_operation_name(dir_name)
    merge_operations()


reload_operations()
