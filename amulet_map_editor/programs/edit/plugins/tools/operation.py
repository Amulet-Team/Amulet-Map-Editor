from amulet_map_editor.programs.edit.api.tool import BaseSelectOperationUI


class SelectOperationUI(BaseSelectOperationUI):
    OperationGroupName = "operations"

    @property
    def name(self) -> str:
        return "Operation"
