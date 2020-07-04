from .util import config as CONFIG
from .util.log import log
from . import lang
import os

__description__ = 'A new Minecraft world editor and converter that supports all versions since Java 1.12 and Bedrock 1.7'
__url__ = "https://www.amulet-editor.com/"
__uri__ = __url__
__doc__ = __description__ + " <" + __uri__ + ">"

__author__ = 'Amulet Team'

__license__ = "MIT"
__copyright__ = "Copyright (c) 2018-2020 Amulet Team"

_version_path = os.path.join(os.path.dirname(__file__), 'version')
if os.path.isfile(_version_path):
    with open(_version_path) as _f:
        version = _f.read()
else:
    version = '?'

IMG_DIR = os.path.join(os.path.dirname(__file__), 'img')
