import os
import json

_default_config = {

}

_config = None
if os.path.isfile('config.json'):
    try:
        with open('config.json') as fc:
            _config = json.load(fc)
    except:
        pass
if not isinstance(_config, dict):
    _config = {}


def get(key):
    if key in _default_config:
        return _config.setdefault(key, _default_config[key])
    else:
        raise KeyError(f'Key "{key}" is not a valid key')


def save():
    with open('config.json', 'w') as f:
        json.dump(_config, f)
