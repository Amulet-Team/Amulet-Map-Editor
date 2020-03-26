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
>>>         "dst_location_absolute"  # This enables a UI to select a destination location. It also enables an optional callable and inputs at structure_callable.
>>>         # If the callable is defined it will be run. If not the selection is extracted and used.
>>>         # After the function has run the user will be shown a UI to pick a destination location for the Structure that was returned.
>>>         # TODO: "options"  # a simple system to create a UI to be shown to the user. Enables "options" key
>>>         "wxoptions"  # enables "wxoptions" key storing a callable allowing direct use of wx
>>>
>>>     "options": dict,  # requires "options" in features. A simple system of defining options from which a simple UI can be created
>>>     "wxoptions": Callable[[WX_OBJ, World, Options], Options],  # a more complex system allowing users to work directly with wx
>>>
>>>     # if one of the dst_location options is enabled the following is valid
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
>>>     "dst_location": Destination  # the destination selected by the user. Only valid in main inputs
>>>     "dst_location_multiple": List[Destination]  # a list of destinations selected by the user. Only valid in main inputs
>>>     # requires either a callable at "structure_callable" to create and return a Structure or "src_box" to extract the src
>>> },
>>> {  # requires a dst_location feature to be enabled. Only valid in main inputs
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

            def error(msg):
                log.error(f'Error loading plugin {os.path.basename(fpath)}. {msg}')
            mod = _load_module(fpath)
            if hasattr(mod, "export"):
                plugin = getattr(mod, "export")
                if not isinstance(plugin, dict):
                    error('Export must be a dictionary.')
                    continue
                if not isinstance(plugin.get("name", None), str):
                    error('"name" in export must exist and be a string.')
                    continue
                structure_callable_options = []
                input_options = []
                dst_ui_enabled = False
                features = plugin.get("features", [])
                feature_index = 0
                stop = False
                while feature_index < len(features):
                    feature = features[feature_index]
                    feature_index += 1
                    if feature == "src_selection":
                        structure_callable_options.append("src_selection")
                        input_options.append("src_selection")
                    elif feature == "wxoptions":
                        structure_callable_options.append("wxoptions")
                        input_options.append("wxoptions")
                        if "wxoptions" not in plugin:
                            error('"wxoptions" key must be defined if wxoptions function is enabled.')
                            stop = True
                            break
                        elif not callable(plugin["wxoptions"]):
                            error('"wxoptions" must be callable.')
                            stop = True
                            break
                        elif "options" in features:
                            error('Only one of options and wxoptions features may be enabled at once.')
                            stop = True
                            break
                    elif feature == "options":
                        structure_callable_options.append("options")
                        input_options.append("options")
                        if "options" not in plugin:
                            error('"options" key must be defined if options function is enabled.')
                            stop = True
                            break
                        elif "wxoptions" in features:
                            error('Only one of options and wxoptions features may be enabled at once.')
                            stop = True
                            break
                    elif feature == "dst_location_absolute":
                        if dst_ui_enabled:
                            error("Only one dst_location feature can be enabled at once")
                        dst_ui_enabled = True
                        input_options.append("dst_location")
                        input_options.append("structure")
                if stop:
                    continue

                if dst_ui_enabled:
                    if "structure_callable" in plugin:
                        if not callable(plugin["structure_callable"]):
                            error('"structure_callable" must be a callable if defined.')
                            continue
                        structure_callable_enabled = True
                    else:
                        if "src_selection" not in features:
                            features.append("src_selection")
                        structure_callable_enabled = False
                else:
                    structure_callable_enabled = False

                plugin_operations = [("operation", plugin.get("operation", None), plugin.get("inputs", []), input_options)]
                if structure_callable_enabled:
                    plugin_operations.append(("structure_callable", plugin.get("structure_callable", None), plugin.get("structure_callable_inputs", []), structure_callable_options))
                for name, operation, inputs, options in plugin_operations:
                    if not callable(operation):
                        error(f'"{name}" in export must exist and be a function.')
                        stop = True
                        break
                    if not isinstance(inputs, list):
                        error(f'"{name}" inputs in export must be a list.')
                        stop = True
                        break
                    for inp in inputs:
                        if inp not in options:
                            error(f'"{inp}" is not a supported input for "{name}"')
                            stop = True
                            break
                if stop:
                    continue

                operations[fpath] = plugin


def load_operations():
    operations.clear()
    for path in [os.path.dirname(__file__), "plugins"]:
        _load_operations(path)


load_operations()
