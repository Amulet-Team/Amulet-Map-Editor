import os
import pkgutil
import sys
from typing import Optional
from types import ModuleType
import importlib.util

from amulet_map_editor.programs.edit.plugins.operations import stock_plugins


STOCK_PLUGINS_DIR: str = stock_plugins.__path__[0]
STOCK_PLUGINS_NAME: str = stock_plugins.__name__
CUSTOM_PLUGINS_DIR = os.path.abspath("plugins")
