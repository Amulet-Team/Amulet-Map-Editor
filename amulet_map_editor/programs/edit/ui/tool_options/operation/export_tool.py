from .select_operation import BaseSelectOperationUI
from amulet_map_editor import plugins


class SelectExportOperationUI(BaseSelectOperationUI):
    @property
    def _operations(self):
        return plugins.export_operations
