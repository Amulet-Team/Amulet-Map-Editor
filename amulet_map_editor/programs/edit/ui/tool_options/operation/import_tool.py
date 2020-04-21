from .select_operation import BaseSelectOperationUI
from amulet_map_editor.plugins import import_operations


class SelectImportOperationUI(BaseSelectOperationUI):
    @property
    def _operations(self):
        return import_operations.import_operations
