import os
import sys
from typing import Optional
from types import ModuleType
import importlib.util

from amulet_map_editor.programs.edit.plugins.operations import stock_plugins


STOCK_PLUGINS_DIR: str = stock_plugins.__path__[0]
STOCK_PLUGINS_NAME: str = stock_plugins.__name__
CUSTOM_PLUGINS_DIR = os.path.abspath("plugins")


def load_module(path: str) -> Optional[ModuleType]:
    """Load a module or package from the file path.
    If it is a module (a file ending .py) then path must be the path to this file.
    If it is a package (a directory optionally containing an __init__.py file) then the path of the directory must be given.

    :param path: The file path of the module/package.
    :return: module if loaded else None
    """
    if os.path.isfile(path):
        spec = importlib.util.spec_from_file_location(path, path)
        if spec is None:
            raise ImportError(f"Could not import {path}")
        mod = importlib.util.module_from_spec(spec)
    elif os.path.isdir(path):
        spec = importlib.util.spec_from_file_location(
            path,
            os.path.join(path, "__init__.py"),
        )
        if spec is None:
            raise ImportError(f"Could not import {path}")
        mod = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = mod
    else:
        return

    spec.loader.exec_module(mod)
    return mod
