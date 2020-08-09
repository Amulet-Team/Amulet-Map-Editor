import os

_version_path = os.path.join(os.path.dirname(__file__), "version")
if os.path.isfile(_version_path):
    with open(_version_path) as _f:
        version = _f.read()
else:
    version = "?"
