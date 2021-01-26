from amulet_map_editor.programs.edit.api.ui.tool import BaseSelectOperationUI


class SelectImportOperationUI(BaseSelectOperationUI):
    OperationGroupName = "import_operations"

    @property
    def name(self) -> str:
        return "Import"
