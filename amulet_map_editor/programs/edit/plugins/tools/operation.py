from amulet_map_editor.programs.edit.api.tool import BaseSelectOperationUI
from amulet_map_editor.programs.edit.api.operations import OperationStorageType, operations


class SelectOperationUI(BaseSelectOperationUI):
    @property
    def name(self) -> str:
        return "Operation"

    @property
    def _operations(self) -> OperationStorageType:
        return operations
