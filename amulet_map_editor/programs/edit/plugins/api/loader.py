import os
import glob
import importlib.util
from amulet import log
from typing import Dict, List, TYPE_CHECKING, Callable, Optional, Type, Tuple
import wx
import struct
import hashlib
import inspect

from .fixed_pipeline import FixedFunctionUI
from .operation_ui import OperationUI, OperationUIType
from .data_types import OperationStorageType

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.canvas import EditCanvas
    from amulet.api.world import World

STOCK_PLUGINS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "stock_plugins")
)
CUSTOM_PLUGINS_DIR = os.path.abspath("plugins")

ValidChrs = set("-_.() abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")


class OperationLoadException(Exception):
    """Exception for internal use"""

    pass


class OperationLoader:
    """A class to handle loading and reloading operations from their python modules/packages"""

    def __init__(self, export_dict: dict, path: str, owning_dict: dict):
        self._path = path
        self._name = ""
        self._ui: Optional[
            Callable[[wx.Window, "EditCanvas", "World"], OperationUI]
        ] = None
        self._owning_dict = owning_dict
        self.load(export_dict)

        self.on_load = None
        self.on_store = None

    def load(self, export_dict: dict):
        if not isinstance(export_dict, dict):
            raise OperationLoadException("Export must be a dictionary.")

        if "name" in export_dict:
            self._name = export_dict["name"]
            if not isinstance(self.name, str):
                raise OperationLoadException(
                    '"name" in export must exist and be a string.'
                )
        else:
            raise OperationLoadException('"name" is not defined in export.')

        options_path = os.path.abspath(
            os.path.join(
                "config",
                "edit_plugins",
                f"""{''.join(c for c in self._name if c in ValidChrs)}_{
                struct.unpack(
                    "H",
                    hashlib.sha1(
                        self._path.encode('utf-8')
                    ).digest()[:2]
                )[0]
                }.config""",  # generate a file name that identifiable to the operation but "unique" to the path
            )
        )

        if "operation" in export_dict:
            if inspect.isclass(export_dict["operation"]) and issubclass(
                export_dict["operation"], (wx.Window, wx.Sizer)
            ):
                operation_ui: Type[OperationUI] = export_dict.get("operation", None)
                if not issubclass(operation_ui, OperationUI):
                    raise OperationLoadException(
                        '"operation" must be a subclass of edit.plugins.OperationUI.'
                    )
                self._ui = lambda parent, canvas, world: operation_ui(
                    parent, canvas, world, options_path
                )

            elif callable(export_dict["operation"]):
                operation = export_dict.get("operation", None)
                if not callable(operation):
                    raise OperationLoadException(
                        '"operation" in export must be callable.'
                    )
                if operation.__code__.co_argcount != 4:
                    raise OperationLoadException(
                        '"operation" function in export must have 4 inputs.'
                    )
                options = export_dict.get("options", {})
                if not isinstance(options, dict):
                    raise OperationLoadException(
                        '"operation" in export must be a dictionary if defined.'
                    )
                self._ui = lambda parent, canvas, world: FixedFunctionUI(
                    parent, canvas, world, options_path, operation, options
                )

                if "on_store" in export_dict and "on_load" in export_dict:
                    self.on_load = export_dict["on_load"]
                    self.on_store = export_dict["on_store"]

            else:
                raise OperationLoadException(
                    '"operation" in export must be a callable, or a subclass of wx.Window or wx.Sizer.'
                )
        else:
            raise OperationLoadException('"operation" is not present in export.')

    @property
    def name(self) -> str:
        return self._name

    def reload(self) -> Tuple[Optional["OperationLoader"], bool]:
        global persistent_storage
        if self.on_store:
            persistent_storage[self._path] = self.on_store()

        if not os.path.exists(self._path):
            return None, False

        if os.path.isfile(self._path):
            get_export_dict(
                _load_module_file(self._path), self._owning_dict, self._path
            )
        elif os.path.isdir(self._path):
            get_export_dict(
                _load_module_directory(self._path), self._owning_dict, self._path
            )
        if self.on_load:
            self.on_load(persistent_storage.get(self._path, None))

        return self, True

    def __call__(
        self, parent: wx.Window, canvas: "EditCanvas", world: "World"
    ) -> OperationUIType:
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
        if path in operations_dict:
            operations_dict[path].load(plugin)
        else:
            operations_dict[path] = OperationLoader(plugin, path, operations_dict)
    except OperationLoadException as e:
        log.error(f"Error loading plugin {path}. {e}")
    except Exception as e:
        log.error(f"Exception loading plugin {path}. {e}")


def get_export_dict(mod, operations_: OperationStorageType, path: str):
    if hasattr(mod, "export"):
        plugin = getattr(mod, "export")
        parse_export(plugin, operations_, path)
    elif hasattr(mod, "exports"):
        for plugin in getattr(mod, "exports"):
            parse_export(plugin, operations_, path)


def _load_operations(operations_: OperationStorageType, path: str):
    """load all operations from a specified directory"""
    if os.path.isdir(path):
        for fpath in glob.iglob(os.path.join(glob.escape(path), "*.py")):
            if fpath.endswith("__init__.py"):
                continue

            mod = _load_module_file(fpath)
            get_export_dict(mod, operations_, fpath)

        for dpath in glob.iglob(os.path.join(glob.escape(path), "**", "__init__.py")):
            mod = _load_module_directory(dpath)
            get_export_dict(mod, operations_, os.path.basename(os.path.dirname(dpath)))


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
    "internal_operations": internal_operations,
    "operations": operations,
    "export_operations": export_operations,
    "import_operations": import_operations,
}
_public = {"operations", "export_operations", "import_operations"}

persistent_storage = {}


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
        [os.path.join(STOCK_PLUGINS_DIR, dir_name)]
        + [os.path.join(CUSTOM_PLUGINS_DIR, dir_name)] * (dir_name in _public)
    )
    _meta[dir_name].update(name_operations)


def reload_operations():
    """Reload all operations"""
    for dir_name in _meta.keys():
        _reload_operation_name(dir_name)
    merge_operations()


reload_operations()
