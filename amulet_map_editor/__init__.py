experimental_bedrock_resources = False
from amulet_map_editor.api import lang, config as CONFIG, log
from .api import version, AmuletUI

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
