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


For information about contributing to this project, please see the contribution section [below](#contributing)

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
