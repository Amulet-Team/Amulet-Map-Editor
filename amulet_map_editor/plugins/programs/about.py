from amulet_map_editor.amulet_wx.world_select import WorldUI
from amulet_map_editor.plugins.programs import BaseWorldProgram
from amulet.api.world import World
import wx


class AboutExtension(BaseWorldProgram):
    def __init__(self, container, world: World):
        super(AboutExtension, self).__init__(
            container
        )
        self.world = world

        self._close_world_button = wx.Button(self, wx.ID_ANY, label='Close World')
        self._close_world_button.Bind(wx.EVT_BUTTON, self._close_world)
        self.add_object(self._close_world_button, 0, wx.ALL | wx.CENTER)

        self.add_object(
            wx.StaticText(
                self,
                label='Currently Opened World: '
            ), 0, wx.ALL | wx.CENTER
        )
        self.add_object(
            WorldUI(self, self.world.world_path), 0, wx.ALL | wx.CENTER
        )
        self.add_object(
            wx.StaticText(
                self,
                label='Choose from the options on the left what you would like to do.\n'
                      'You can switch between these at any time.\n'
                      '<================='
            ), 0, wx.ALL | wx.CENTER
        )

    def _close_world(self, evt):
        self.GetGrandParent().GetParent().close_world(self.world.world_path)


export = {
    "name": "About",
    "ui": AboutExtension
}
