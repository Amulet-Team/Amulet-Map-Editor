import webbrowser
import wx
import wx.lib.inspection

from amulet_map_editor.api import image, lang
from .base_page import BasePageUI
from amulet_map_editor.api.wx.ui.select_world import open_level_from_dialog


class AmuletMainMenu(wx.Panel, BasePageUI):
    def __init__(self, parent: wx.Window):
        super(AmuletMainMenu, self).__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        sizer.AddStretchSpacer(1)
        name_sizer = wx.BoxSizer()
        sizer.Add(name_sizer, 0, wx.CENTER)
        icon_img = image.logo.amulet_logo.bitmap(64, 64)

        icon = wx.StaticBitmap(self, wx.ID_ANY, icon_img, (0, 0), (64, 64))
        icon2 = wx.StaticBitmap(self, wx.ID_ANY, icon_img, (0, 0), (64, 64))
        icon2.Bind(
            wx.EVT_LEFT_DOWN, lambda evt: wx.lib.inspection.InspectionTool().Show()
        )
        name_sizer.Add(icon, flag=wx.CENTER)

        amulet_name = wx.StaticText(self, label="Amulet")
        amulet_name.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        name_sizer.Add(amulet_name, flag=wx.CENTER | wx.LEFT | wx.RIGHT, border=10)
        name_sizer.Add(icon2, flag=wx.CENTER)
        button_font = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self._open_world_button = wx.Button(
            self, label=lang.get("main_menu.open_world"), size=(400, 70)
        )
        self._open_world_button.SetFont(button_font)
        self._open_world_button.Bind(wx.EVT_BUTTON, lambda _: open_level_from_dialog(self))
        sizer.Add(self._open_world_button, 0, wx.ALL | wx.CENTER, 5)

        self._help_button = wx.Button(
            self, label=lang.get("main_menu.help"), size=(400, 70)
        )
        self._help_button.SetToolTip(lang.get("app.browser_open_tooltip"))
        self._help_button.SetFont(button_font)
        self._help_button.Bind(wx.EVT_BUTTON, self._documentation)
        sizer.Add(self._help_button, 0, wx.ALL | wx.CENTER, 5)

        self._discord_button = wx.Button(
            self, label=lang.get("main_menu.discord"), size=(400, 70)
        )
        self._discord_button.SetToolTip(lang.get("app.browser_open_tooltip"))
        self._discord_button.SetFont(button_font)
        self._discord_button.Bind(wx.EVT_BUTTON, self._discord)
        sizer.Add(self._discord_button, 0, wx.ALL | wx.CENTER, 5)

        sizer.AddStretchSpacer(2)

    @staticmethod
    def _documentation(_):
        webbrowser.open(
            "https://github.com/Amulet-Team/Amulet-Map-Editor/blob/master/amulet_map_editor/readme.md"
        )

    @staticmethod
    def _discord(_):
        webbrowser.open("https://discord.gg/BTm6jnf")

    def enable(self):
        self.GetTopLevelParent().create_menu()
