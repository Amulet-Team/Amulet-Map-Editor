from .select_operation import BaseSelectOperationUI
from amulet_map_editor.plugins import export_operations


class SelectExportOperationUI(BaseSelectOperationUI):
    @property
    def _operations(self):
        return export_operations.export_operations
