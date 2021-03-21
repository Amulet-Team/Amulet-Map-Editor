from amulet_map_editor.programs.edit.api.ui.tool import BaseOperationChoiceToolUI


class OperationTool(BaseOperationChoiceToolUI):
    OperationGroupName = "operations"

    @property
    def name(self) -> str:
        return "Operation"
