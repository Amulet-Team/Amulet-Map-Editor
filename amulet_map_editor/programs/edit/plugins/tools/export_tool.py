from amulet_map_editor.programs.edit.api.ui.tool import BaseOperationToolUI


class ExportTool(BaseOperationToolUI):
    OperationGroupName = "export_operations"

    @property
    def name(self) -> str:
        return "Export"
