experimental_bedrock_resources = False

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
from amulet_map_editor.api import config as CONFIG, log, lang

from amulet_map_editor.api.framework.app import open_level, close_level
