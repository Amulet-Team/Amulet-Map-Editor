from amulet_map_editor.programs.edit.api.tool import BaseSelectOperationUI
from amulet_map_editor.programs.edit.api.operations import (
    OperationStorageType,
    import_operations,
)


class SelectImportOperationUI(BaseSelectOperationUI):
    @property
    def name(self) -> str:
        return "Import"

    @property
    def _operations(self) -> OperationStorageType:
        return import_operations
