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
>>> {  # requires a dst_location feature to be enabled. Only valid in main inputs
>>>     "structure": Structure  # an extracted Structure as returned by structure_callable or the area of the World selected by src_box
>>> }
>>> {
>>>     "options": dict,  # "options" or "wxoptions" feature must be enabled
>>> }
"""
import functools
import os
import glob
import importlib.util
from amulet import log
from typing import Dict, List


def _load_module_file(module_path: str):
    spec = importlib.util.spec_from_file_location(
        os.path.basename(module_path), module_path
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _load_module_directory(module_path):
    import sys

    spec = importlib.util.spec_from_file_location(
        os.path.basename(os.path.dirname(module_path)), module_path
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def _error(name, msg):
    log.error(f"Error loading plugin {name}. {msg}")


def parse_export(plugin: dict, operations_dict, path):
    error = functools.partial(_error, path)

    if not isinstance(plugin, dict):
        error("Export must be a dictionary.")
        return
    if not isinstance(plugin.get("name", None), str):
        error('"name" in export must exist and be a string.')
        return
    plugin_name = plugin["name"]
    structure_callable_options = ["options"]
    input_options = ["options"]
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
            if "wxoptions" not in plugin:
                error(
                    '"wxoptions" key must be defined if wxoptions feature is enabled.'
                )
                stop = True
                break
            elif not callable(plugin["wxoptions"]):
                error('"wxoptions" must be callable.')
                stop = True
                break
            elif "options" in features:
                error(
                    "Only one of options and wxoptions features may be enabled at once."
                )
                stop = True
                break
        elif feature == "options":
            if "options" not in plugin:
                error('"options" key must be defined if options feature is enabled.')
                stop = True
                break
            elif "wxoptions" in features:
                error(
                    "Only one of options and wxoptions features may be enabled at once."
                )
                stop = True
                break
        elif feature == "dst_location_absolute":
            if dst_ui_enabled:
                error("Only one dst_location feature can be enabled at once")
            dst_ui_enabled = True
            input_options.append("dst_location")
            input_options.append("structure")
    if stop:
        return

    if dst_ui_enabled:
        if "structure_callable" in plugin:
            if not callable(plugin["structure_callable"]):
                error('"structure_callable" must be a callable if defined.')
                return
            structure_callable_enabled = True
        else:
            if "src_selection" not in features:
                features.append("src_selection")
            structure_callable_enabled = False
    else:
        structure_callable_enabled = False

    plugin_operations = [
        (
            "operation",
            plugin.get("operation", None),
            plugin.get("inputs", []),
            input_options,
        )
    ]
    if structure_callable_enabled:
        plugin_operations.append(
            (
                "structure_callable",
                plugin.get("structure_callable", None),
                plugin.get("structure_callable_inputs", []),
                structure_callable_options,
            )
        )
    for name, operation, inputs, options in plugin_operations:
        if not callable(operation):
            error(f'"{name}" in export must exist and be a function.')
            stop = True
            return
        if not isinstance(inputs, list):
            error(f'"{name}" inputs in export must be a list.')
            stop = True
            return
        for inp in inputs:
            if inp not in options:
                error(f'"{inp}" is not a supported input for "{name}"')
                stop = True
                return
    if stop:
        return

    operations_dict[plugin_name] = plugin


def _load_operations(operations: Dict[str, dict], path: str):
    if os.path.isdir(path):
        for fpath in glob.iglob(os.path.join(path, "*.py")):
            if fpath.endswith("__init__.py"):
                continue

            mod = _load_module_file(fpath)
            if hasattr(mod, "export"):
                plugin = getattr(mod, "export")
                parse_export(plugin, operations, os.path.basename(fpath))
            elif hasattr(mod, "exports"):
                for plugin in getattr(mod, "exports"):
                    parse_export(plugin, operations, os.path.basename(fpath))

        for dpath in glob.iglob(os.path.join(path, "**", "__init__.py")):
            mod = _load_module_directory(dpath)
            if hasattr(mod, "export"):
                plugin = getattr(mod, "export")
                parse_export(
                    plugin, operations, os.path.basename(os.path.dirname(dpath))
                )
            elif hasattr(mod, "exports"):
                for plugin in getattr(mod, "exports"):
                    parse_export(
                        plugin, operations, os.path.basename(os.path.dirname(dpath))
                    )


def load_operations(paths: List[str]):
    operations = {}
    for path in paths:
        _load_operations(operations, path)
    return operations
