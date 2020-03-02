

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

