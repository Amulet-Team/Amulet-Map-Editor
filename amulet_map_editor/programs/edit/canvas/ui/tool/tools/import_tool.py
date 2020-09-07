from .base_operation import BaseSelectOperationUI
from amulet_map_editor.programs.edit import plugins


class SelectImportOperationUI(BaseSelectOperationUI):
    @property
    def name(self) -> str:
        return "Import"

    @property
    def _operations(self) -> plugins.OperationStorageType:
        return plugins.import_operations
