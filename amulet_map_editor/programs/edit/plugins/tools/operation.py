from amulet_map_editor.programs.edit.api.ui.tool import BaseOperationToolUI


class OperationTool(BaseOperationToolUI):
    OperationGroupName = "operations"

    @property
    def name(self) -> str:
        return "Operation"
