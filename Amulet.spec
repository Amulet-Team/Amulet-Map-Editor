# -*- mode: python ; coding: utf-8 -*-

# python -m PyInstaller -y Amulet.spec

from PyInstaller.utils.hooks import collect_submodules

from typing import Dict, Tuple, Set
import sys
import os
import glob
import importlib.util
import string
import random
import re

# pyinstaller moves the current directory to the front
# We would prefer to find modules in site packages first
cwd = os.path.normcase(os.path.realpath(os.getcwd()))
sys.path = [path for path in sys.path if os.path.normcase(os.path.realpath(path)) != cwd]
sys.path.append(cwd)

sys.modules["FixTk"] = None


def get_package_path(mod: str):
    return os.path.dirname(importlib.util.find_spec(mod).origin)


AMULET_PATH = get_package_path("amulet")
PYMCT_PATH = get_package_path("PyMCTranslate")
MINECRAFT_MODEL_READER = get_package_path("minecraft_model_reader")
AMULET_MAP_EDITOR = get_package_path("amulet_map_editor")


hidden = []
hidden.extend(collect_submodules("pkg_resources"))
hidden.extend(collect_submodules("minecraft_model_reader"))
hidden.extend(collect_submodules("wx"))
hidden.extend(collect_submodules("OpenGL"))
hidden.extend(collect_submodules("OpenGL.GL"))
hidden.extend(collect_submodules("OpenGL.GL.shaders"))


OBFUSCATE_KEY = "_" + "".join(random.choices(string.ascii_lowercase, k=10))


def obfuscate(mod_path: str):
    """Prefix all private variables (_var or self._var) with _{OBFUSCATE_KEY}"""
    for py_path in glob.glob(os.path.join(mod_path, "**", "*.py"), recursive=True):
        with open(py_path) as f:
            py_code = f.read()
        py_code = re.sub(r"(?<![a-zA-Z0-9_])(?P<name>_[a-zA-Z0-9][a-zA-Z0-9_]*)", lambda match: f"{OBFUSCATE_KEY}{match.group('name')}", py_code)
        with open(py_path, "w") as f:
            f.write(py_code)


obfuscate(AMULET_PATH)
obfuscate(PYMCT_PATH)
obfuscate(MINECRAFT_MODEL_READER)
obfuscate(AMULET_MAP_EDITOR)

a = Analysis(
    [os.path.join(AMULET_MAP_EDITOR, "__main__.py")],
    binaries=[],
    datas=[],
    hiddenimports=hidden,
    hookspath=[
        os.path.join(AMULET_MAP_EDITOR, "__pyinstaller"),
        os.path.join(AMULET_PATH, "__pyinstaller"),
        os.path.join(PYMCT_PATH, "__pyinstaller"),
    ],
    runtime_hooks=[],
    excludes=["FixTk", "tcl", "tk", "_tkinter", "tkinter", "Tkinter"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False,
)

# the paths to each source already added
added_source: Set[str] = set([v[1] for v in a.pure])
# the paths to every source
# {absolute_path: (relative_path, import_path)}
missing_source: Dict[str, Tuple[str, str]] = {}
for module_path in (
    AMULET_MAP_EDITOR,
    AMULET_PATH,
    PYMCT_PATH,
    MINECRAFT_MODEL_READER,
):
    for path in glob.glob(
        os.path.join(os.path.abspath(module_path), "**", "*.py"), recursive=True
    ):
        if path not in added_source:
            rel_path: str = os.path.relpath(path, os.path.dirname(module_path))
            imp_path = rel_path.replace(os.sep, ".")[:-3]
            if imp_path.endswith(".__init__"):
                imp_path = imp_path[:-9]
            missing_source[path] = (rel_path, imp_path)

if missing_source:
    print("These source files are not included in the build.")
    for path in missing_source:
        print("\t", path)

non_data_ext = ["*.pyc", "*.py", "*.dll", "*.so", "*.dylib"]

a.datas += Tree(AMULET_PATH, "amulet", excludes=non_data_ext)
a.datas += Tree(AMULET_MAP_EDITOR, "amulet_map_editor", excludes=non_data_ext)
a.datas += Tree(MINECRAFT_MODEL_READER, "minecraft_model_reader", excludes=non_data_ext)
a.datas += Tree(PYMCT_PATH, "PyMCTranslate", excludes=non_data_ext + ["json"])
a.datas += [
    (
        os.path.join("PyMCTranslate", "build_number"),
        os.path.join(PYMCT_PATH, "build_number"),
        "DATA",
    )
]

print("Added data files")
for d in filter(lambda dt: "PyMCTranslate" in dt[0], a.datas):
    print("\t", d)
sys.stdout.flush()  # fix the log being out of order

pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="amulet_app",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon="icon.ico",
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="Amulet",
)

app = BUNDLE(
    coll,
    name="amulet.app",
    icon="icon.ico",
    bundle_identifier="com.amuletmc.amulet_map_editor",
)
