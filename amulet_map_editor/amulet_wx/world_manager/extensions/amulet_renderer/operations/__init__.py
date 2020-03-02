

"""
# Example plugin
from amulet.operations.clone import clone

def operation(world, source_box, destination_box, options)

export = {
    "v": 1,  # a version 1 plugin
    "name": "Plugin Name",  # the name of the plugin
    "operation": clone,  # the actual function to call when running the plugin
    "inputs": ["src_box", "dst_box", "options"],  # the inputs to give to the plugin

    "options": {},  # a simple system of defining options from which a simple UI can be created
    "wxoptions": wxpanel,  # a more complex system allowing users to work directly with wx
    # only one of the above should be present. The result is passed to the options slot if present (this won't be used if it isn't)
    "features": ["src_box", "dst_box"]  # options beyond a simple UI eg selection box
}
"""

