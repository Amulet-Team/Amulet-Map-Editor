# Amulet Map Editor

<a href="https://github.com/Amulet-Team/Amulet-Map-Editor/releases"><img alt="TravisCI" src="https://travis-ci.org/Amulet-Team/Amulet-Map-Editor.svg"></a>
[![Documentation Status](https://readthedocs.org/projects/amulet-map-editor/badge/?version=develop)](https://amulet-map-editor.readthedocs.io/en/develop/?badge=develop)

A new Minecraft world editor and converter that supports all versions since Java 1.12 and Bedrock 1.7.

![edit](resource/img/edit.jpg)

## Running compiled builds

Download the zip file for your operating system from the list of [compiled builds](https://github.com/Amulet-Team/Amulet-Map-Editor/releases). (Currently Windows only)

Extract the contained folder to a location on your computer and run the executable.

## Running from Source

### Requirements

[Python 3.7.0+](https://www.python.org/)

In order to run Amulet from source, you will need to install the following packages and the dependancies for those packages:

The following can be easily installed using `python -m pip install -r requirements.txt`

For linux run `python -m pip install -r requirements_linux.txt`

- numpy
- wxpython
- pyopengl
- [Amulet-Core](https://github.com/Amulet-Team/Amulet-Core)  The library to handle loading and saving data to the world formats.
- [Amulet-NBT](https://github.com/Amulet-Team/Amulet-NBT)  The library to handle reading and saving NBT and SNBT.
- [PyMCTranslate](https://github.com/gentlegiantJGC/PyMCTranslate)  The library to handle block, block entity, entity and biome translation. between versions
- [Minecraft-Model-Reader](https://github.com/gentlegiantJGC/Minecraft-Model-Reader)  The library to handle loading block models and textures from a resource pack for use in the renderer.

run `python main.py`

## Contributing

For information about contributing to this project, please read the [contribution](contributing.md) file.
