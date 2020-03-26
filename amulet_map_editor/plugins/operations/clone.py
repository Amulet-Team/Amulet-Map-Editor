from amulet.operations.paste import paste

export = {
    "v": 1,  # a version 1 plugin
    "name": "Clone",  # the name of the plugin
    "features": ["src_selection", "dst_location_absolute"],
    "inputs": ["structure", "dst_location"],  # the inputs to give to the plugin
    "operation": paste  # the actual function to call when running the plugin
}
