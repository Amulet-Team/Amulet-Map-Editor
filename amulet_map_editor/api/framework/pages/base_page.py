from amulet_map_editor.api.datatypes import MenuData


class BasePageUI:
    def disable(self):
        pass

    def enable(self):
        pass

    def close(self):
        pass

    def menu(self, menu: MenuData) -> MenuData:
        return menu
