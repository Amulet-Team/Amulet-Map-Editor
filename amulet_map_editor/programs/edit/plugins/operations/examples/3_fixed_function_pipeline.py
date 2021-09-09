"""
This licence applies to this file only.

-- begin licence --
MIT License

Copyright (c) 2021 Amulet-Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
-- end licence --
"""

# Fixed function example plugin 3
# see example 2 before looking at this example
# This example shows how to use options with the fixed function pipeline


from amulet.api.selection import SelectionGroup
from amulet.api.level import BaseLevel
from amulet.api.data_types import Dimension

operation_options = {  # options is a dictionary where the key is the description shown to the user and the value describes how to build the UI
    "Text Label": ["label"],  # This will just be a label
    # bool examples  https://wxpython.org/Phoenix/docs/html/wx.CheckBox.html
    "Bool input default": [
        "bool"
    ],  # This will be a check box that takes the default value (unchecked)
    "Bool input False": [
        "bool",
        False,
    ],  # This will be a check box that starts unchecked
    "Bool input True": ["bool", True],  # This will be a check box that starts checked
    # int examples  https://wxpython.org/Phoenix/docs/html/wx.SpinCtrl.html
    "Int input default": ["int"],  # This will be an integer input with starting value 0
    "Int input 10": [
        "int",
        10,
    ],  # This will be an integer input with starting value 10 (or whatever you put in the second slot)
    "Int input 10 bounded": [
        "int",
        10,
        0,
        20,
    ],  # same as above but must be between the third and fourth values
    # float examples  https://wxpython.org/Phoenix/docs/html/wx.SpinCtrlDouble.html
    "Float input default": [
        "float"
    ],  # This will be a float input with starting value 0.0
    "Float input 10": [
        "float",
        10,
    ],  # This will be a float input with starting value 10.0 (or whatever you put in the second slot)
    "Float input 10 bounded": [
        "float",
        10,
        0,
        20,
    ],  # same as above but must be between the third and fourth values
    # string input examples  https://wxpython.org/Phoenix/docs/html/wx.TextCtrl.html
    "String input empty": [
        "str"
    ],  # This will be a text input with an empty starting value
    "String input empty2": ["str", ""],  # Same as the above
    "String input hello": ["str", "hello"],  # Text entry with starting value "hello"
    # string choice examples  https://wxpython.org/Phoenix/docs/html/wx.Choice.html
    "Text choice": ["str_choice", "choice 1", "choice 2", "choice 3"],
    # OS examples
    "File Open picker": ["file_open"],  # UI to pick an existing file
    "File Save picker": ["file_save"],  # UI to pick a file to save to
    "Folder picker": ["directory"],  # UI to pick a directory
}


def operation(
    world: BaseLevel, dimension: Dimension, selection: SelectionGroup, options: dict
):
    # When the user presses the run button this function will be run as normal but
    # since the "options" key was defined in export this function will get another
    # input in the form of a dictionary where the keys are the same as you defined
    # them in the options dictionary above and the values are what the user picked
    # in the UI (bool, int, float, str)
    # If "options" is not defined in export this will just be an empty dictionary
    pass


export = {
    "name": "Fixed Function Pipeline Example 3",
    "operation": operation,
    "options": operation_options,  # The options you defined above should be added here to show in the UI
}
