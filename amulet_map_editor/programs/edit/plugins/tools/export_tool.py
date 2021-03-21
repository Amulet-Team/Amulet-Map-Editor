from amulet_map_editor.programs.edit.api.ui.tool import BaseOperationChoiceToolUI


class ExportTool(BaseOperationChoiceToolUI):
    OperationGroupName = "export_operations"

    @property
    def name(self) -> str:
        return "Export"
