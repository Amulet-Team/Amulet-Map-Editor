"""
This license applies to this file only.

-- begin license --
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
-- end license --
"""

# Fixed function example plugin
# The fixed function operation pipeline works in much the same way as MCEdit Unified filters with some modifications
# You define a function and it will appear in the UI for you to run


from amulet.api.selection import SelectionGroup
from amulet.api.level import BaseLevel
from amulet.api.data_types import Dimension


# for those that are new to python 3 the thing after the colon is the object type that the variable should be
def operation(
    world: BaseLevel, dimension: Dimension, selection: SelectionGroup, options: dict
):
    # world is the object that contains all the data related to the world
    # dimension in a string used to identify the currently loaded dimension. It can be used to access the right dimension from the world
    # selection is an object describing the selections made by the user. It is possible there may not be any boxes selected
    # options will be explored in further examples
    pass


export = {  # This is what the program will actually look for. It describes how the operation will work
    "name": "Fixed Function Pipeline Example 1",  # the name of the plugin
    "operation": operation,  # the actual function to call when running the plugin
}
