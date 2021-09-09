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

# Fixed function example plugin 2
# see example 1 before looking at this example
# Notes about the operation


from amulet.api.selection import SelectionGroup
from amulet.api.level import BaseLevel
from amulet.api.data_types import Dimension


# Notes about the operation
# The operation is allowed to yield floats in the range 0 to 1.
#       This is used to update the loading bar in the UI. Without this the UI may appear to be not responding
#       It can optionally also yield a float and a string. The float is the same as the above and the string is used to display in the loading bar
# The operation is allowed to return a value however nothing will be done with it


def operation(
    world: BaseLevel, dimension: Dimension, selection: SelectionGroup, options: dict
):
    for i in range(10):
        # do some logic
        yield (i + 1) / 10

    for i in range(10):
        # do some logic
        yield (i + 1) / 10, f"Step {i} of 10"
    return "hello"  # This will not actually do anything but is allowed


export = {
    "name": "Fixed Function Pipeline Example 2",
    "operation": operation,
}
