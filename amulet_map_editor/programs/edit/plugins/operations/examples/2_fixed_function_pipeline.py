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
