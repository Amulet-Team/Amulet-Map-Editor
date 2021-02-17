import webbrowser
import wx
import wx.lib.inspection

from amulet_map_editor.api import image, lang
from .base_page import BasePageUI
from amulet_map_editor.api.wx.ui.select_world import WorldSelectDialog


class AmuletMainMenu(wx.Panel, BasePageUI):
    def __init__(self, parent: wx.Window, open_world):
        super(AmuletMainMenu, self).__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        sizer.AddStretchSpacer(1)
        self._open_world_callback = open_world
        name_sizer = wx.BoxSizer()
        sizer.Add(name_sizer, 0, wx.CENTER)
        icon_img = image.logo.icon128.bitmap(64, 64)

        icon = wx.StaticBitmap(self, wx.ID_ANY, icon_img, (0, 0), (64, 64))
        icon2 = wx.StaticBitmap(self, wx.ID_ANY, icon_img, (0, 0), (64, 64))
        icon2.Bind(
            wx.EVT_LEFT_DOWN, lambda evt: wx.lib.inspection.InspectionTool().Show()
        )
        name_sizer.Add(icon, flag=wx.CENTER)

        amulet_converter = wx.StaticText(self, label="Amulet")
        amulet_converter.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        name_sizer.Add(amulet_converter, flag=wx.CENTER)
        name_sizer.Add(icon2, flag=wx.CENTER)
        button_font = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self._open_world_button = wx.Button(
            self, label=lang.get("main_menu.open_world"), size=(400, 70)
        )
        self._open_world_button.SetFont(button_font)
        self._open_world_button.Bind(wx.EVT_BUTTON, self._show_world_select)
        sizer.Add(self._open_world_button, 0, wx.ALL | wx.CENTER, 5)

        self._help_button = wx.Button(
            self, label=lang.get("main_menu.help"), size=(400, 70)
        )
        self._help_button.SetFont(button_font)
        self._help_button.Bind(wx.EVT_BUTTON, self._documentation)
        sizer.Add(self._help_button, 0, wx.ALL | wx.CENTER, 5)

        self._help_button = wx.Button(self, label="Amulet Discord", size=(400, 70))
        self._help_button.SetFont(button_font)
        self._help_button.Bind(wx.EVT_BUTTON, self._discord)
        sizer.Add(self._help_button, 0, wx.ALL | wx.CENTER, 5)

        sizer.AddStretchSpacer(2)

    def _show_world_select(self, _):
        select_world = WorldSelectDialog(self, self._open_world_callback)
        select_world.ShowModal()
        select_world.Destroy()

    @staticmethod
    def _documentation(_):
        webbrowser.open(
            "https://github.com/Amulet-Team/Amulet-Map-Editor/blob/master/amulet_map_editor/readme.md"
        )

    @staticmethod
    def _discord(_):
        webbrowser.open("https://discord.gg/BTm6jnf")

    def enable(self):
        self.GetGrandParent().create_menu()
