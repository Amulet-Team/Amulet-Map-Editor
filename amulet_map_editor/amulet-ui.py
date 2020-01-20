import wx
from amulet_map_editor.amulet_wx.world_select import WorldSelectAndRecentUI
from amulet_map_editor import lang
from amulet_map_editor.amulet_wx.world_manager import WorldManagerUI

import wx.lib.inspection


class AmuletMainWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=wx.EmptyString,
            pos=wx.DefaultPosition,
            size=wx.Size(560, 400),
            style=wx.CAPTION
            | wx.CLOSE_BOX
            | wx.MINIMIZE_BOX
            | wx.SYSTEM_MENU
            | wx.TAB_TRAVERSAL
            | wx.CLIP_CHILDREN
            | wx.RESIZE_BORDER,
        )

        self.open_worlds = []

        # self.sizer = wx.BoxSizer(wx.VERTICAL)
        # self.SetSizer(self.sizer)

        self.world_tab_holder = wx.Notebook(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0
        )

        self._add_world_tab(
            WorldSelectAndRecentUI(self.world_tab_holder, self._open_world),
            lang.get('main_menu')
        )

        # self.sizer.Add(self.world_tab_holder, 1, wx.EXPAND | wx.ALL, 5)
        # self.Layout()
        # self.Centre(wx.BOTH)
        self.Show()

    def _add_world_tab(self, obj, obj_name):
        # TODO: find a way for the tab to be optionally closeable
        self.world_tab_holder.AddPage(obj, obj_name, True)

    def _remove_world_tab(self, obj):
        self.world_tab_holder.RemovePage(obj)

    def _open_world(self, path):
        world = WorldManagerUI(self.world_tab_holder, path, self._remove_world_tab)
        self._add_world_tab(world, world.world_name)


if __name__ == "__main__":
    app = wx.App()
    frame = AmuletMainWindow(None)
    wx.lib.inspection.InspectionTool().Show()
    app.MainLoop()
