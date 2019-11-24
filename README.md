# Amulet Map Editor

<a href="https://circleci.com/gh/Amulet-Team/Amulet-Map-Editor"><img alt="CircleCI" src="https://circleci.com/gh/Amulet-Team/Amulet-Map-Editor.svg"></a>
[![Documentation Status](https://readthedocs.org/projects/amulet-map-editor/badge/?version=develop)](https://amulet-map-editor.readthedocs.io/en/develop/?badge=develop)

A new Minecraft world editor that aims to be flexible, extendable, and support most editions of Minecraft.

## Requirements

### Running from Source
In order to run the Amulet Editor from source, you will need to install the following packages and follow the steps to install below:
- Python 3.7.0+
- wxpython
- [Amulet-Core](https://github.com/Amulet-Team/Amulet-Core)

The steps below will install everything needed for Amulet (Instructions for installing Python 3.7 provided when available)

__Note: Make sure to install the `venv` module if it does not come pre-installed with python__

1. Clone the project using `git clone https://github.com/Amulet-Team/Amulet-Map-Editor`
2. Change the working directory to be the directory created when cloning (Ex: `cd Amulet-Editor`)
3. Set up a python virtual environment (run the following commands for your OS in your terminal/command prompt)
   1. __Windows__
      1. Create the virtual environment: `python -m venv ENV`
      2. Activate the environment: `.\ENV\scripts\activate.bat`
   2. __OS X__
      1. Create the virtual environment: `python3.7 -m venv ENV`
         - Depending on how you installed python 3.7, this might instead be: `py -3.7 -m venv ENV`
      2. Activate the environment: `source /ENV/bin/activate`
   3. __Linux__
      1. Install python 3.7 if it's not already installed (run the following commands in your terminal of choice. These are for Debain based distros, use your distros package manager or refer to [#54 (comment)](https://github.com/Amulet-Team/Amulet-Core/issues/54#issuecomment-523046836) if you need to build Python 3.7 from source)
         1. `sudo apt-get update` (Optional)
         2. `sudo apt-get install python-3.7`
         3. Verify that python 3.7 was successfully installed: `python3.7 --version`
      2. Set up a python virtual environment (also run the following commands in the terminal)
         1. Create the virtual environment: `python3.7 -m venv ENV`
         2. Activate the environment: `source /ENV/bin/activate`
4. Install the requirements using `pip install -r requirements.txt`
5. To format your files automatically before committing changes, use `pre-commit install`

### For Development
Follow all of the step above for running from source, then install the following packages:
- [Black](https://github.com/ambv/black) (Required for formatting)
  - Must be ran before pushing a Pull Request
- Sphinx
- [sphinx-autodoc-typehints](https://github.com/agronholm/sphinx-autodoc-typehints)
- [sphinx_rtd_theme](https://github.com/rtfd/sphinx_rtd_theme)

Shortcut: `pip install -r requirements-dev.txt` (This also installs the requirements required for running from source)

For information about contributing to this project, please see the contribution section [below](#contributing)

## Running the program

### Command-line
To run the program in command line mode, run the following command in your operating system's console:
`Amulet_Map_Editor --command-line`

## Documentation

Our online documentation can be found here: https://amulet-map-editor.readthedocs.io/en/latest/

### Building the Documentation
To build the documentation locally, run the following command: `make html` and then navigate to the
generated directory `docs_build/html` in your favorite web browser


## Contributing

### Branch Naming
Branches should be created when a certain bug or feature may take multiple attempts to fix. Naming
them should follow the following convention (even for forked repositories when a pull request is being made):

* For features, use: `impl-<feature name>`
* For bug fixes, use: `bug-<bug tracker ID>`
* For improvements/rewrites, use: `improv-<feature name>`
* For prototyping, use: `proto-<feature name>`

### Code Formatting
For code formatting, we use the formatting utility [black](https://github.com/ambv/black). To run
it on a file, run the following command from your favorite terminal after installing: `black <path to file>`

While formatting is not strictly required for each commit, we ask that after you've finished your
code changes for your Pull Request to run it on every changed file.

### Pull Requests
We ask that submitted Pull Requests give moderately detailed notes about the changes and explain 
any changes that were made to the program outside of those directly related to the feature/bug-fix.
Please make sure to run all tests and include a written verification that all tests have passed.

_Note: We will also re-run all tests before reviewing, this is to mitigate additional changes/commits
needed to pass all tests._

Once a Pull Request is submitted, we will mark the request for review, once that is done, we will
review the changes and provide any notes/things to change. Once all additional changes have been made,
we will merge the request.


## License
This software is available under the MIT license.
