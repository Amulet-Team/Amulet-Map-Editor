"""
# Example plugin
from amulet.operations.clone import clone

def operation(world, source_box, destination_box, options)

export = {
    "v": 1,  # a version 1 plugin
    "name": "Plugin Name",  # the name of the plugin
    "operation": clone,  # the actual function to call when running the plugin
    "inputs": [],  # a list of inputs to give to the plugin. World class is passed in as the first and these following
        # possible inputs (max one from each list)
        ["src_box"]  # the box selected by the user
        [
            "dst_box"  # the destination selected by the user (box same size of src_box. "src_box" is required). The presence of this triggers the UI to enable the functionality
            "dst_box_multiple"  # a list of destination boxes selected by the user (boxes same size of src_box. "src_box" is required). The presence of this triggers the UI to enable the functionality
        ]
        [
            "options",  # "options" key must exist
            "wxoptions"  # "wxoptions" key must exist
        ]
    "options": {},  # a simple system of defining options from which a simple UI can be created
    "wxoptions": wxpanel,  # a more complex system allowing users to work directly with wx
    # The result is passed to the related slot in inputs
}
"""

import os
import glob
import importlib.util
from amulet import log

operations = []

_input_options = ["src_box", "dst_box", "dst_box_multiple", "options", "wxoptions"]


def _load_module(module_path: str):
    spec = importlib.util.spec_from_file_location(os.path.basename(module_path), module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _load_modules(path: str):
    if os.path.isdir(path):
        for fpath in glob.iglob(os.path.join(path, "*.py")):
            if fpath == __file__:
                continue
            mod = _load_module(fpath)
            if hasattr(mod, "export"):
                plugin = getattr(mod, "export")
                if not isinstance(plugin, dict):
                    log.error(f'Error loading plugin {os.path.basename(fpath)}. Export must be a dictionary.')
                    continue
                if not isinstance(plugin.get("name", None), str):
                    log.error(f'Error loading plugin {os.path.basename(fpath)}. "name" in export must exist and be a string.')
                    continue
                if not callable(plugin.get("operation", None)):
                    log.error(f'Error loading plugin {os.path.basename(fpath)}. "operation" in export must exist and be a function.')
                    continue
                inputs = plugin.get("inputs", [])
                if not isinstance(inputs, list):
                    log.error(f'Error loading plugin {os.path.basename(fpath)}. "inputs" in export must be a list.')
                    continue
                if "dst_box" in inputs or "dst_box_multiple" in inputs:
                    if "src_box" not in inputs:
                        log.error(f'Error loading plugin {os.path.basename(fpath)}. "src_box" must be defined in "inputs" if "dst_box" or "dst_box_multiple" are.')
                        continue

                if "options" in inputs and "wxoptions" in inputs:
                    log.error(f'Error loading plugin {os.path.basename(fpath)}. Only one of "options" and "wxoptions" may be defined in "inputs" at once.')
                    continue
                elif "options" in inputs and "options" not in plugin:
                    log.error(f'Error loading plugin {os.path.basename(fpath)}. "options" was specificed in "inputs" but was not present in the dictionary.')
                    continue
                elif "wxoptions" in inputs and "wxoptions" not in plugin:
                    log.error(f'Error loading plugin {os.path.basename(fpath)}. "wxoptions" was specificed in "inputs" but was not present in the dictionary.')
                    continue


def load_operations():
    operations.clear()
    for path in [os.path.dirname(__file__), "plugins"]:
        _load_modules(path)
