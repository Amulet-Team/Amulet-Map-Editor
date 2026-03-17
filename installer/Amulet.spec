# -*- mode: python ; coding: utf-8 -*-

# python -m PyInstaller -y installer/Amulet.spec

from typing import TYPE_CHECKING
import sys
import os

# pyinstaller moves the current directory to the front
# We would prefer to find modules in site packages first
cwd = os.path.normcase(os.path.realpath(os.getcwd()))
sys.path = [path for path in sys.path if os.path.normcase(os.path.realpath(path)) != cwd]
sys.path.append(cwd)

import amulet_map_editor

if TYPE_CHECKING:
    from PyInstaller.building.build_main import Analysis
    from PyInstaller.building.api import PYZ, EXE, COLLECT
    from PyInstaller.building.osx import BUNDLE

is_windows = os.name == "nt"

sys.modules["FixTk"] = None

a = Analysis(
    [os.path.join(amulet_map_editor.__path__[0], "__main__.py")],
    binaries=[],
    datas=[],
    runtime_hooks=[],
    excludes=["FixTk", "tcl", "tk", "_tkinter", "tkinter", "Tkinter"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name="amulet",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=is_windows, # Only show the console on Windows
    icon="logo.ico",
    contents_directory="lib"
)
exe_debug = EXE(
    pyz,
    a.scripts,
    exclude_binaries=True,
    name="amulet_debug",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=is_windows, # Only show the console on Windows
    icon="logo.ico",
    contents_directory="lib"
)
coll = COLLECT(
    exe,
    exe_debug,
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
    icon="logo.ico",
    bundle_identifier="com.amuletmc.amulet_map_editor",
)
