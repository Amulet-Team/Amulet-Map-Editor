import wx

from amulet.api.level import BaseLevel
from amulet_map_editor.api.datatypes import MenuData
from amulet_map_editor.api.framework.base_tab import BaseTab


class BaseProgram(BaseTab):
    def __init__(self, container: wx.Window, world: BaseLevel):
        pass

    def menu(self, menu: MenuData) -> MenuData:
        return menu
