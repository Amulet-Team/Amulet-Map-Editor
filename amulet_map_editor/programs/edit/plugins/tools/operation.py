from amulet_map_editor.programs.edit.api.ui.tool import BaseSelectOperationUI


class OperationTool(BaseSelectOperationUI):
    OperationGroupName = "operations"

    @property
    def name(self) -> str:
        return "Operation"
