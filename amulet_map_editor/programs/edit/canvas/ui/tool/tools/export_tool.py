from .base_operation import BaseSelectOperationUI
from amulet_map_editor.programs.edit import plugins


class SelectExportOperationUI(BaseSelectOperationUI):
    @property
    def name(self) -> str:
        return "Export"

    @property
    def _operations(self) -> plugins.OperationStorageType:
        return plugins.export_operations
