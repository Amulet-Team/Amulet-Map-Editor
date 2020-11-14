# -*- mode: python ; coding: utf-8 -*-

# python -m PyInstaller -y Amulet.spec

from PyInstaller.utils.hooks import collect_submodules

import sys
import os
import shutil
import glob
import amulet
import PyMCTranslate
import minecraft_model_reader

sys.modules["FixTk"] = None

AMULET_PATH = amulet.__path__[0]
PYMCT_PATH = os.path.abspath(os.path.dirname(PyMCTranslate.__file__))
REAL_PYMCT_PATH = PYMCT_PATH if not os.path.islink(PYMCT_PATH) else os.readlink(PYMCT_PATH)  # I have this linked by a symbolic link
MINECRAFT_MODEL_READER = os.path.abspath(os.path.dirname(minecraft_model_reader.__file__))

AMULET_MAP_EDITOR = os.path.abspath(os.path.join(".", "build", "lib", "amulet_map_editor"))
if not os.path.isfile(os.path.join(AMULET_MAP_EDITOR, "__main__.py")):
    print(AMULET_MAP_EDITOR)
    raise Exception("There is no built version of amulet-map-editor. Run setup.py build first.")

block_cipher = None

hidden = []
hidden.extend(collect_submodules("pkg_resources"))
hidden.extend(collect_submodules("amulet_map_editor"))
hidden.extend(collect_submodules("wx"))
hidden.extend(collect_submodules("OpenGL"))
hidden.extend(collect_submodules("OpenGL.GL"))
hidden.extend(collect_submodules("OpenGL.GL.shaders"))

a = Analysis(
    [os.path.join(AMULET_MAP_EDITOR, "__main__.py")],
    # pathex=[".", "amulet_map_editor"],
    binaries=[],
    datas=[],
    hiddenimports=hidden,
    hookspath=[],
    runtime_hooks=[],
    excludes=["FixTk", "tcl", "tk", "_tkinter", "tkinter", "Tkinter"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

a.datas += Tree(AMULET_PATH, "amulet", excludes=["*.pyc"])
a.datas += Tree(AMULET_MAP_EDITOR, "amulet_map_editor", excludes=["*.pyc"])
a.datas += Tree(MINECRAFT_MODEL_READER, "minecraft_model_reader", excludes=["*.pyc"])
a.datas += Tree(PYMCT_PATH, "PyMCTranslate", excludes=["*.pyc", "json"])
a.datas += [(os.path.join("PyMCTranslate", "build_number"), os.path.join(PYMCT_PATH, "build_number"), "DATA")]

for d in filter(lambda dt: "PyMCTranslate" in dt[0], a.datas):
    print("\t", d)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher
)
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
    icon="icon.ico"
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="Amulet"
)

app = BUNDLE(
    coll,
    name="amulet.app",
    icon="icon.ico",
    bundle_identifier="com.amulet-editor.amulet_map_editor"
)
