from amulet_map_editor.programs.edit.api.ui.tool import BaseSelectOperationUI


class SelectExportOperationUI(BaseSelectOperationUI):
    OperationGroupName = "export_operations"

    @property
    def name(self) -> str:
        return "Export"
