from amulet_map_editor.api.datatypes import MenuData
from amulet_map_editor.api.framework.base_tab import BaseTab


class BaseProgram(BaseTab):
    def menu(self, menu: MenuData) -> MenuData:
        return menu
