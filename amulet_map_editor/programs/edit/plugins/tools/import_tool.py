from amulet_map_editor.programs.edit.api.tool import BaseSelectOperationUI


class SelectImportOperationUI(BaseSelectOperationUI):
    OperationGroupName = "import_operations"

    @property
    def name(self) -> str:
        return "Import"
