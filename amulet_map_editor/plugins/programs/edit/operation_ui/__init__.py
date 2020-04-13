from amulet_map_editor.amulet_wx.simple import SimplePanel

from .select_destination import SelectDestinationUI
from .select_operation import SelectOperationUI


class OperationUI(SimplePanel):
    def __init__(self, parent):
        super().__init__(parent)
