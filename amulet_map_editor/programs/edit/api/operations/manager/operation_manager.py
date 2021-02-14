from typing import Tuple, Dict
import os
import traceback

from .loader import (
    BaseOperationLoader,
    OperationLoader,
    UIOperationLoader,
)
from .util import STOCK_PLUGINS_DIR, CUSTOM_PLUGINS_DIR, load_module

from amulet_map_editor import log


class BaseOperationManager:
    OperationClass: BaseOperationLoader = None

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
        self._load_dir(os.path.join(STOCK_PLUGINS_DIR, self._group_name))
        self._load_dir(os.path.join(CUSTOM_PLUGINS_DIR, self._group_name))

    def _load_dir(self, path: str):
        """Load all operations in a set directory."""
        os.makedirs(path, exist_ok=True)
        for obj_name in os.listdir(path):
            if obj_name in {"__init__.py", "__pycache__"}:
                continue
            obj_path = os.path.join(path, obj_name)
            if os.path.isfile(obj_path) and not obj_path.endswith(".py"):
                continue
            try:
                mod = load_module(obj_path)
            except ImportError:
                log.warning(f"Failed to import {obj_path}.\n{traceback.format_exc()}")
            else:
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
