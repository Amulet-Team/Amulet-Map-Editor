from amulet.operations.paste import paste

export = {
    "v": 1,  # a version 1 plugin
    "name": "Clone",  # the name of the plugin
    "operation": paste,  # the actual function to call when running the plugin
    "inputs": ["src_box", "structure", "dst_box"]  # the inputs to give to the plugin
}
