import os

from amulet_map_editor.programs.edit.plugins.operations import stock_plugins


STOCK_PLUGINS_DIR: str = stock_plugins.__path__[0]
STOCK_PLUGINS_NAME: str = stock_plugins.__name__
CUSTOM_PLUGINS_DIR = os.path.join(os.environ["DATA_DIR"], "plugins")
