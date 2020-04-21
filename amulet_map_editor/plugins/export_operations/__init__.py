from amulet_map_editor.plugins import load_operations
import os
from typing import Dict

export_operations: Dict[str, dict] = {}
options: Dict[str, dict] = {}


def load():
    global export_operations
    os.makedirs(os.path.join("plugins", "export_operations"), exist_ok=True)
    export_operations = load_operations([
        os.path.dirname(__file__),
        os.path.join("plugins", "export_operations")
    ])


load()
