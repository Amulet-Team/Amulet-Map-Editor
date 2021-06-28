from amulet_map_editor import lang
from amulet_map_editor.api.opengl import check_opengl

check_opengl()

from amulet_map_editor.programs.edit.edit import EditExtension

export = {"name": lang.get("program_3d_edit.tab_name"), "ui": EditExtension}
