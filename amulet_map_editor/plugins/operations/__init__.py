"""
# Example plugin

def structure_callable(world, dimension, source_box) -> Selection:  # see below. Only required if "structure_callable" is defined
    pass

def operation(world, dimension, source_box):
    pass

def show_ui(parent, world: World, options: dict) -> dict:  # see below. Only needed if using wxoptions
    # create a UI and show it (probably best using wx.Dialog)
    # build the UI using the options that were returned last time (or an empty dictionary if it is the first)
    # and return the options how you wish

export = {
    # required
    "v": 1,  # a version 1 plugin
    "name": "Plugin Name",  # the name of the plugin
    "operation": operation,  # the actual function to call when running the plugin
    "inputs": ["src_box"],  # a list of inputs to give to the plugin. World class is passed in as the first and these following
        # possible inputs (max one from each list)
        ["src_box"]  # the box selected by the user
        [
            "dst_box"  # the destination selected by the user. The presence of this triggers the UI to enable the functionality
            "dst_box_multiple"  # a list of destination boxes selected by the user. The presence of this triggers the UI to enable the functionality
            # requires either a callable at "structure_callable" to create and return a Structure or "src_box" to extract the src
        ],
            [  # dst_... needs to be enabled to use this
                "structure"  # an extracted Structure as returned by structure_callable or the area of the World selected by src_box
            ]
        [
            "options",  # "options" key must exist
            "wxoptions"  # "wxoptions" key must exist
        ]

    # optional (based on inputs)
    "options": {},  # a simple system of defining options from which a simple UI can be created
    "wxoptions": show_ui,  # a more complex system allowing users to work directly with wx
    # The result is passed to the related slot in inputs
    "structure_callable": structure_callable  # this function is run before selecting the destination locations and returns a Structure for use there
}


normal filters
    input box in editor
    options
    function with inputs
    
copy/extract
    input box in editor
    function with inputs
    
paste/import
    select input file/structure in memory                       options
    editor deals with picking location(s)
    function run with input structure and output locations      main operation
    
clone
    input box in editor
    run operation button
    selection extracted (either using inbuilt function or structure_callable
    editor deals with picking location(s) based on the structure
    function run with input structure and output locations      main operation    
    
    
select operation
select box if required
pick options if valid
run operation
    if dst_box or dst_box_multiple is defined a pre-operation function is optional
        if defined run structure_callable
            given the same inputs as main operation minus destination box
            returns Structure
        else
            extract the src_box and use that
        select destination in UI
    main operation
"""

import os
import glob
import importlib.util
from amulet import log
from typing import Dict

operations: Dict[str, dict] = {}
options: Dict[str, dict] = {}

_input_options = ["src_box", "dst_box", "dst_box_multiple", "structure", "options", "wxoptions"]


def _load_module(module_path: str):
    spec = importlib.util.spec_from_file_location(os.path.basename(module_path), module_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _load_operations(path: str):
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
                    if "structure_callable" in plugin:
                        if not callable(plugin["structure_callable"]):
                            log.error(f'Error loading plugin {os.path.basename(fpath)}. "structure_callable" must be a callable if defined.')
                            continue
                    elif "src_box" not in inputs:
                        log.error(f'Error loading plugin {os.path.basename(fpath)}. "src_box" or "structure_callable" must be defined if "dst_box" or "dst_box_multiple" are.')
                        continue

                elif "structure" in inputs:
                    log.error(f'Error loading plugin {os.path.basename(fpath)}. "structure" cannot be defined if "dst_box" or "dst_box_multiple" are not.')
                    continue
                elif "structure_callable" in plugin:
                    log.error(f'Error loading plugin {os.path.basename(fpath)}. "structure_callable" cannot be defined if "dst_box" or "dst_box_multiple" are not.')
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

                if not all(v in _input_options for v in inputs):
                    for v in inputs:
                        if v not in _input_options:
                            log.error(f'Error loading plugin {os.path.basename(fpath)}. "{v}" is not a valid value in "inputs".')
                    continue

                operations[fpath] = plugin


def load_operations():
    operations.clear()
    for path in [os.path.dirname(__file__), "plugins"]:
        _load_operations(path)


load_operations()
