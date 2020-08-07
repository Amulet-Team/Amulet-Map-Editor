from amulet_map_editor.programs.edit import plugins
from .base_operation import BaseSelectOperationUI


class SelectOperationUI(BaseSelectOperationUI):
    @property
    def _operations(self) -> plugins.OperationStorageType:
        return plugins.operations
