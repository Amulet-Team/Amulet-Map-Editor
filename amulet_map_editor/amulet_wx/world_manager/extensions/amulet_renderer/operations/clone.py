from amulet.operations.clone import clone

export = {
    "v": 1,  # a version 1 plugin
    "name": "Clone",  # the name of the plugin
    "operation": clone,  # the actual function to call when running the plugin
    "inputs": ["src_box", "dst_box"]  # the inputs to give to the plugin
}