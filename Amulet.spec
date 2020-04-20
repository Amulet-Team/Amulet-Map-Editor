# -*- mode: python ; coding: utf-8 -*-

# python -m PyInstaller -y Amulet.spec

from PyInstaller.utils.hooks import collect_submodules

import sys
import os
import shutil
import glob
import importlib.util
import amulet
import PyMCTranslate
import minecraft_model_reader

sys.modules['FixTk'] = None

AMULET_PATH = amulet.__path__[0]
PYMCT_PATH = os.path.abspath(os.path.dirname(PyMCTranslate.__file__))
REAL_PYMCT_PATH = PYMCT_PATH if not os.path.islink(PYMCT_PATH) else os.readlink(PYMCT_PATH)  # I have this linked by a symbolic link
AMULET_MAP_EDITOR = os.path.abspath(os.path.join('.', 'amulet_map_editor'))
MINECRAFT_MODEL_READER = os.path.abspath(os.path.dirname(minecraft_model_reader.__file__))

block_cipher = None

hidden = []
hidden.extend(collect_submodules('pkg_resources'))
hidden.extend(collect_submodules('amulet_map_editor'))
hidden.extend(collect_submodules('wx'))
hidden.extend(collect_submodules('OpenGL'))
hidden.extend(collect_submodules('OpenGL.GL'))
hidden.extend(collect_submodules('OpenGL.GL.shaders'))

def load_module(path: str):

    spec = importlib.util.spec_from_file_location(
        os.path.splitext(os.path.basename(path))[0],
        path
    )
    modu = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modu)
    return modu

PYMCT_MINIFY_PATH = os.path.realpath(
        os.path.join(REAL_PYMCT_PATH, '..', 'minify_json.py')
    )

LOCAL_MINIFY_PATH = os.path.realpath(os.path.join('.', 'minify_json.py'))

if os.path.exists(PYMCT_MINIFY_PATH):
    mod = load_module(PYMCT_MINIFY_PATH)
elif os.path.exists(LOCAL_MINIFY_PATH):
    mod = load_module(LOCAL_MINIFY_PATH)
else:
    raise Exception("Couldn't location minify_json.py")

mod.main(PYMCT_PATH)

a = Analysis(['./main.py'],
             pathex=['.', 'amulet_map_editor'],
             binaries=[],
             datas=[],
             hiddenimports=hidden,
             hookspath=[],
             runtime_hooks=[],
             excludes=['FixTk', 'tcl', 'tk', '_tkinter', 'tkinter', 'Tkinter'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += Tree(AMULET_PATH, 'amulet', excludes=['*.pyc'])
a.datas += Tree(AMULET_MAP_EDITOR, 'amulet_map_editor', excludes=['*.pyc'])
a.datas += Tree(MINECRAFT_MODEL_READER, 'minecraft_model_reader', excludes=['*.pyc'])
a.datas += Tree(PYMCT_PATH, 'PyMCTranslate', excludes=['*.pyc', 'json'])

pyz = PYZ(a.pure,
          a.zipped_data,
          cipher=block_cipher
)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='Amulet',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True,
          icon='icon.ico'
)
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='Amulet'
)

delete_files = [
    '**/transparrency_cache.json',
    '**/config.json'
]
delete_folders = [
    '**/world_temp',
    '**/__pycache__',
    '**/minecraft_model_reader/resource_packs/java_vanilla'
]

for fun, path_list in [[os.remove, delete_files], [shutil.rmtree, delete_folders]]:
    for f_ext in path_list:
        glob_path = os.path.join('dist', f_ext)
        for path in glob.iglob(glob_path, recursive=True):
            fun(path)
