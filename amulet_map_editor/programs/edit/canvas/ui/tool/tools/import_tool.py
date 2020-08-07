from amulet_map_editor.programs.edit import plugins
from .base_operation import BaseSelectOperationUI


class SelectImportOperationUI(BaseSelectOperationUI):
    @property
    def _operations(self) -> plugins.OperationStorageType:
        return plugins.import_operations
