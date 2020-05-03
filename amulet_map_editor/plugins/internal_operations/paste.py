from typing import TYPE_CHECKING
from amulet.operations.paste import paste

from amulet.api.structure import structure_buffer, Structure
from amulet.api.data_types import Dimension

if TYPE_CHECKING:
    from amulet.api.world import World


def get_structure(
    world: "World",
    dimension: Dimension,
) -> Structure:
    if structure_buffer:
        return structure_buffer[-1]
    else:
        raise Exception('You need to copy a selection before pasting.')


export = {
    "v": 1,  # a version 1 plugin
    "name": "Paste",  # the name of the plugin
    "features": ["dst_location_absolute"],
    "structure_callable_inputs": [],
    "structure_callable": get_structure,
    "inputs": ["structure", "options"],  # the inputs to give to the plugin
    "operation": paste  # the actual function to call when running the plugin
}
