from amulet_map_editor.plugins import load_operations
import os
from typing import Dict

import_operations: Dict[str, dict] = {}
options: Dict[str, dict] = {}


def load():
    global import_operations
    os.makedirs(os.path.join("plugins", "import_operations"), exist_ok=True)
    import_operations = load_operations([
        os.path.dirname(__file__),
        os.path.join("plugins", "import_operations")
    ])


load()
