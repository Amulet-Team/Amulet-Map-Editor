# -*- mode: python ; coding: utf-8 -*-

# python -m PyInstaller -y Amulet.spec

from PyInstaller.utils.hooks import collect_submodules

from typing import Dict, Tuple, Set
import sys
import os
import glob

# pyinstaller moves the current directory to the front
# We would prefer to find modules in site packages first
cwd = os.path.normcase(os.path.realpath(os.getcwd()))
sys.path = [path for path in sys.path if os.path.normcase(os.path.realpath(path)) != cwd]
sys.path.append(cwd)

import amulet
import amulet_nbt
import PyMCTranslate
import minecraft_model_reader
import amulet_map_editor

sys.modules["FixTk"] = None

AMULET_NBT_PATH = amulet_nbt.__path__[0]
AMULET_PATH = amulet.__path__[0]
PYMCT_PATH = PyMCTranslate.__path__[0]
MINECRAFT_MODEL_READER = minecraft_model_reader.__path__[0]
AMULET_MAP_EDITOR = amulet_map_editor.__path__[0]


hidden = []
hidden.extend(collect_submodules("pkg_resources"))
hidden.extend(collect_submodules("minecraft_model_reader"))
hidden.extend(collect_submodules("wx"))
hidden.extend(collect_submodules("OpenGL"))
hidden.extend(collect_submodules("OpenGL.GL"))
hidden.extend(collect_submodules("OpenGL.GL.shaders"))


a = Analysis(
    [os.path.join(AMULET_MAP_EDITOR, "__main__.py")],
    binaries=[],
    datas=[],
    hiddenimports=hidden,
    hookspath=[
        os.path.join(AMULET_MAP_EDITOR, "__pyinstaller"),
        os.path.join(AMULET_PATH, "__pyinstaller"),
        os.path.join(PYMCT_PATH, "__pyinstaller"),
        os.path.join(AMULET_NBT_PATH, "__pyinstaller"),
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
        os.path.join(glob.escape(os.path.abspath(module_path)), "**", "*.py"), recursive=True
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
