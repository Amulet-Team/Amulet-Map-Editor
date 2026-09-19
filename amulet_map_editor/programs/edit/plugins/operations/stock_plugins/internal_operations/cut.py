from typing import TYPE_CHECKING

from amulet.api.structure import structure_cache
from amulet.api.data_types import Dimension, OperationReturnType
from amulet.api.selection import SelectionGroup
from amulet_map_editor import lang
from amulet_map_editor.programs.edit.plugins.operations.stock_plugins.internal_operations.delete import (
    delete,
)
from amulet_map_editor.programs.edit.api.operations import OperationError

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel


def cut(
    world: "BaseLevel", dimension: Dimension, selection: SelectionGroup
) -> OperationReturnType:
    if selection:
        yield 0, lang.get("program_3d_edit.operation.cutting")
        structure = world.extract_structure(selection, dimension)
        structure_cache.add_structure(structure, structure.dimensions[0])
        yield from delete(
            world,
            dimension,
            selection,
        )
    else:
        raise OperationError(
            lang.get("program_3d_edit.operation.cut_no_selection")
        )
