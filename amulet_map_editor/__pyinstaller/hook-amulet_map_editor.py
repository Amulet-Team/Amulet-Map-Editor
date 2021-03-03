import pkgutil

from amulet_map_editor import api, programs

hiddenimports = [
    name for _, name, _ in pkgutil.walk_packages(api.__path__, api.__name__ + ".")
] + [
    name
    for _, name, _ in pkgutil.walk_packages(programs.__path__, programs.__name__ + ".")
]
