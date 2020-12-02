from amulet_map_editor.programs.edit.api.tool import BaseSelectOperationUI
from amulet_map_editor.programs.edit.api.operations import OperationStorageType, export_operations


class SelectExportOperationUI(BaseSelectOperationUI):
    @property
    def name(self) -> str:
        return "Export"

    @property
    def _operations(self) -> OperationStorageType:
        return export_operations
