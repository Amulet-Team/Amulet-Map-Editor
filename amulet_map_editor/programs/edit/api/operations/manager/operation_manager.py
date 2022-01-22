import sys
from typing import Tuple, Dict, Type
from types import ModuleType
import os
import traceback
import pkgutil
import importlib

from .loader import (
    BaseOperationLoader,
    OperationLoader,
    UIOperationLoader,
)
from .util import STOCK_PLUGINS_DIR, STOCK_PLUGINS_NAME, CUSTOM_PLUGINS_DIR

from amulet_map_editor import log


class BaseOperationManager:
    OperationClass: Type[BaseOperationLoader] = None

    def __init__(self, group_name: str):
        """Set up an operation manager that handles operations for a set group.

        :param group_name: The name of the group. This is used to pick the directory.
        """
        # The loaded operations. Stored under their identifier.
        assert issubclass(self.OperationClass, BaseOperationLoader)
        self._group_name = group_name
        self._operations: Dict[str, BaseOperationLoader] = {}
        self.reload()

    @property
    def operations(self) -> Tuple[BaseOperationLoader, ...]:
        return tuple(self._operations.values())

    def get_operation(self, operation_id: str):
        return self._operations[operation_id]

    def __getitem__(self, operation_id: str):
        return self._operations[operation_id]

    def reload(self):
        """Unload the old operations and reload them all.
        If new operations are created, load them.
        If old operations were removed, remove them."""
        self._operations.clear()
        self._load_internal_submodules(
            os.path.join(STOCK_PLUGINS_DIR, self._group_name),
            ".".join([STOCK_PLUGINS_NAME, self._group_name]),
        )
        self._load_external_submodules(
            os.path.join(CUSTOM_PLUGINS_DIR, self._group_name)
        )

    def _load_internal_submodules(self, package_path: str, package_name: str):
        """
        Load submodules from within a known package.

        :param package_path: The file path of the package to load submodules from.
        :param package_name: The python path of the package to load submodules from.
        """
        self._load_submodules(package_path, f"{package_name}.")

    def _load_external_submodules(self, path: str):
        """
        Load submodules from an external package.

        Note that the path will be added to the system path.

        :param path: The path to the directory to find modules in.
        """
        # clean the path
        path = os.path.abspath(path)

        # create the directory
        os.makedirs(path, exist_ok=True)

        if path not in sys.path:
            # The path modules are loaded from should be on the system path
            sys.path.append(path)

        self._load_submodules(path)

    def _load_submodules(self, path: str, package: str = ""):
        """
        Load all operations in a path.
        You should not use this directly.
        Use _load_internal_submodules or _load_external_submodules

        :param path: The path to load modules from.
        :param package: The package name prefix
        """
        # clean the path
        path = os.path.abspath(path)

        for _, module_name, _ in pkgutil.iter_modules([path]):
            module_name = f"{package}{module_name}"
            try:
                mod = importlib.import_module(module_name)
                mod = importlib.reload(mod)
            except ImportError:
                log.warning(
                    f"Failed to import {module_name}.\n{traceback.format_exc()}"
                )
            except SyntaxError:
                log.warning(
                    f"There was a syntax error in {module_name}.\n{traceback.format_exc()}"
                )
            else:
                if (
                    os.path.dirname(
                        mod.__path__[0] if hasattr(mod, "__path__") else mod.__file__
                    )
                    == path
                ):
                    # If the loaded module is actually in the path it was loaded from.
                    # There may be cases where the name is shadowed by another module.
                    self._load_module(module_name, mod)
                else:
                    log.warning(
                        f"Module {module_name} shadows another module. Try using a different module name."
                    )

    def _load_module(self, obj_path: str, mod: ModuleType):
        if hasattr(mod, "export"):
            export = mod.export
            if isinstance(export, dict):
                self._load_operation(obj_path, export)
            elif isinstance(export, (list, tuple)):
                for i, export_dict in export:
                    self._load_operation(f"{obj_path}[{i}]", export_dict)
            else:
                log.error(f"The format of export in {obj_path} is invalid.")
        else:
            log.error(f"export is not present in {obj_path}")

    def _load_operation(self, identifier: str, export_dict: dict):
        """Create an instance of a subclass of BaseOperationLoader to load the operation.
        When finished and the class is valid store it in self._operations

        :param identifier: A unique identifier for this operation. <path>[0]
        :param export_dict: The dictionary defining the operation.
        :return:
        """
        op = self.OperationClass(identifier, export_dict)
        if op.is_valid:
            self._operations[op.identifier] = op


class OperationManager(BaseOperationManager):
    OperationClass = OperationLoader
    """A class to manage a group of function operations that run immediately when called."""


class UIOperationManager(BaseOperationManager):
    OperationClass = UIOperationLoader
    """A class to manage a group of UI operations that return a wx UI when called."""
