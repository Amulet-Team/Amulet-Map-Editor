from amulet_map_editor.api.datatypes import MenuData


class BaseProgram:
    def enable(self):
        """Run when the panel is shown/enabled"""
        pass

    def disable(self):
        """Run when the panel is hidden/disabled"""
        pass

    def is_closeable(self) -> bool:
        """
        Check if it is safe to close the UI.
        If this is going to return False it should notify the user.
        :return: True if the program can be closed, False otherwise
        """
        return True

    def close(self):
        """Fully close the UI. Called when destroying the UI."""
        pass

    def menu(self, menu: MenuData) -> MenuData:
        return menu
