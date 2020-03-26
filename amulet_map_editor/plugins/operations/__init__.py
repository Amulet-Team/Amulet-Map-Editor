"""
>>> # Example plugin
>>> from typing import List, Any, Callable, Dict, Optional
>>> from amulet.api.selection import Selection
>>> from amulet.api.structure import Structure
>>> from amulet.api.world import World
>>> WX_OBJ = Any
>>> Dimension = Any
>>> Options = Dict
>>> Destination = {"x": int, "y": int, "z": int}
>>>
>>> def show_ui(parent, world: World, options: dict) -> dict:  # see below. Only needed if using wxoptions
>>>     # create a UI and show it (probably best using wx.Dialog)
>>>     # build the UI using the options that were returned last time (or an empty dictionary if it is the first)
>>>     # and return the options how you wish
>>>
>>> export = {
>>>     # required
>>>     "v": 1,  # a version 1 plugin
>>>     "name": "Plugin Name",  # the name of the plugin
>>>     "features": List[str], # a list of features that enable functionality in the UI
>>>         # the valid options are: (any invalid options will cause the operation to fail to load)
>>>         "src_selection"  # The user is required to select an area before running the plugin. They will be prompted if they do not.
>>>         "dst_selection_absolute"  # This enables a UI to select a destination location. It also enables an optional callable and inputs at structure_callable.
>>>         # If the callable is defined it will be run. If not the selection is extracted and used.
>>>         # After the function has run the user will be shown a UI to pick a destination location for the Structure that was returned.
>>>         # TODO: "options"  # a simple system to create a UI to be shown to the user. Enables "options" key
>>>         "wxoptions"  # enables "wxoptions" key storing a callable allowing direct use of wx
>>>
>>>     "options": dict,  # requires "options" in features. A simple system of defining options from which a simple UI can be created
>>>     "wxoptions": Callable[[WX_OBJ, World, Options], Options],  # a more complex system allowing users to work directly with wx
>>>
>>>     # if one of the dst_selection options is enabled the following is valid
>>>     "structure_callable_inputs": List[str],  # see inputs below
>>>     "structure_callable": Callable[[World, Dimension, ...], Structure]  # World and Dimension are always the first two inputs. Above inputs follow.
>>>     # this function is run before selecting the destination locations and returns a Structure for use there
>>>
>>>     "inputs": List[str],  # see inputs below
>>>     "operation": Callable[[World, Dimension, ...], Optional[Any]],  # the actual function to call when running the plugin
>>>       # World and Dimension are always the first two inputs. Above inputs follow.
>>> }
>>>
>>> # Input format
>>> # a list of inputs to give to the plugin. World class and dimension are first and these follow
>>> # possible inputs (max one from each group)
>>> {"src_selection": Selection}  # the user created selection
>>> {  # requires respective feature to be enabled
>>>     "dst_selection": Destination  # the destination selected by the user. Only valid in main inputs
>>>     "dst_selection_multiple": List[Destination]  # a list of destinations selected by the user. Only valid in main inputs
>>>     # requires either a callable at "structure_callable" to create and return a Structure or "src_box" to extract the src
>>> },
>>> {  # requires a dst_selection feature to be enabled. Only valid in main inputs
>>>     "structure": Structure  # an extracted Structure as returned by structure_callable or the area of the World selected by src_box
>>> }
>>> {  # requires respective option feature to be enabled
>>>     "options": dict,  # "options" key must exist
>>>     "wxoptions": dict  # "wxoptions" key must exist
>>> }


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
