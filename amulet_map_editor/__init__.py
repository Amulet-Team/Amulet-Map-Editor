import os
import platformdirs

experimental_bedrock_resources = False

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

# Initialise default paths. These should be initialised in main before this is imported
# but the tests don't run main so a default is required for that case.
data_dir = platformdirs.user_data_dir("AmuletMapEditor", "AmuletTeam")
os.environ.setdefault("DATA_DIR", data_dir)
config_dir = platformdirs.user_config_dir("AmuletMapEditor", "AmuletTeam")
if config_dir == data_dir:
    config_dir = os.path.join(data_dir, "Config")
os.environ.setdefault("CONFIG_DIR", config_dir)
os.environ.setdefault(
    "CACHE_DIR", platformdirs.user_cache_dir("AmuletMapEditor", "AmuletTeam")
)
os.environ.setdefault(
    "LOG_DIR", platformdirs.user_log_dir("AmuletMapEditor", "AmuletTeam")
)

from amulet_map_editor.api import config as CONFIG, lang
from amulet_map_editor.api.framework.app import open_level, close_level
