import os
import json

colours_path = os.path.join(os.path.dirname(__file__), "colours.json")

if os.path.isfile(colours_path):
    with open(colours_path) as f:
        colours = json.load(f)
    if isinstance(colours, dict):
        colours = {
            key: tuple(float(c) for c in val)
            for key, val in colours.items()
            if isinstance(val, list) and all(isinstance(c, (float, int)) for c in val)
        }
    else:
        colours = {}
else:
    colours = {}
