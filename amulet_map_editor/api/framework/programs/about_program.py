import wx
from typing import Callable, TYPE_CHECKING

from amulet_map_editor.api.wx.ui.simple import SimplePanel
from amulet_map_editor.api.wx.ui.select_world import WorldUI
from amulet_map_editor.api.framework.programs import BaseProgram

if TYPE_CHECKING:
    from amulet.api.world import World


class AboutProgram(SimplePanel, BaseProgram):
    def __init__(
        self, container, world: "World", close_self_callback: Callable[[], None]
    ):
        SimplePanel.__init__(self, container)
        self.world = world
        self._close_self_callback = close_self_callback

        self._close_world_button = wx.Button(self, wx.ID_ANY, label="Close World")
        self._close_world_button.Bind(wx.EVT_BUTTON, self._close_world)
        self.add_object(self._close_world_button, 0, wx.ALL | wx.CENTER)

        self.add_object(
            wx.StaticText(self, label="Currently Opened World: "), 0, wx.ALL | wx.CENTER
        )
        self.add_object(WorldUI(self, self.world.world_wrapper), 0, wx.ALL | wx.CENTER)
        self.add_object(
            wx.StaticText(
                self,
                label="Choose from the options on the left what you would like to do.\n"
                "You can switch between these at any time.\n"
                "<=================",
            ),
            0,
            wx.ALL | wx.CENTER,
        )

    def _close_world(self, evt):
        self._close_self_callback()
