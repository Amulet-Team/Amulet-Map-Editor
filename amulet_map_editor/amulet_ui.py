import wx
import wx.lib.inspection
from wx.lib.agw import flatnotebook
import os
from typing import Dict, Union
import webbrowser

from amulet.api.errors import LoaderNoneMatched
from amulet_map_editor.amulet_wx.ui.select_world import WorldSelectDialog
from amulet_map_editor import lang, version, log, IMG_DIR
from amulet_map_editor.programs import WorldManagerUI
from amulet_map_editor.programs import BaseWorldUI

# Uses a conditional so if this breaks a build, we can just delete the file and it will skip the check
try:
    from amulet_map_editor.util import update_check
except ImportError:
    update_check = None
    log.warning("Could not import update checker")

NOTEBOOK_MENU_STYLE = (
    flatnotebook.FNB_NO_X_BUTTON
    | flatnotebook.FNB_HIDE_ON_SINGLE_TAB
    | flatnotebook.FNB_NAV_BUTTONS_WHEN_NEEDED
)
NOTEBOOK_STYLE = NOTEBOOK_MENU_STYLE | flatnotebook.FNB_X_ON_TAB

CLOSEABLE_PAGE_TYPE = Union[WorldManagerUI]

wx.Image.SetDefaultLoadFlags(0)


class AmuletMainWindow(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=f"Amulet V{version}",
            pos=wx.DefaultPosition,
            size=wx.Size(560, 400),
            style=wx.CAPTION
            | wx.CLOSE_BOX
            | wx.MINIMIZE_BOX
            | wx.MAXIMIZE_BOX
            | wx.MAXIMIZE
            | wx.SYSTEM_MENU
            | wx.TAB_TRAVERSAL
            | wx.CLIP_CHILDREN
            | wx.RESIZE_BORDER,
        )
        self.locale = wx.Locale(
            wx.LANGUAGE_ENGLISH
        )  # TODO: work out proper localisation
        icon = wx.Icon()
        icon.CopyFromBitmap(
            wx.Bitmap(
                os.path.join(os.path.dirname(__file__), "img", "icon64.png"),
                wx.BITMAP_TYPE_ANY,
            )
        )
        self.SetIcon(icon)

        self._open_worlds: Dict[str, CLOSEABLE_PAGE_TYPE] = {}

        self.world_tab_holder = flatnotebook.FlatNotebook(
            self, agwStyle=NOTEBOOK_MENU_STYLE
        )

        self.world_tab_holder.Bind(
            flatnotebook.EVT_FLATNOTEBOOK_PAGE_CLOSING, self._on_page_close
        )

        self._main_menu = AmuletMainMenu(self.world_tab_holder, self._open_world)

        self._last_page: BaseWorldUI = self._main_menu

        self._add_world_tab(self._main_menu, lang.get("main_menu"))

        self.Bind(wx.EVT_CLOSE, self._on_close_app)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self._page_change)

        if update_check is not None:
            self.Bind(
                update_check.EVT_UPDATE_CHECK,
                lambda evt: update_check.show_update_window(self, version, evt),
            )
            update_check.check_for_update(version, self)

        self.Show()

    def create_menu(self):
        menu_dict = {}
        menu_dict.setdefault("&File", {}).setdefault("system", {}).setdefault(
            "Open World", lambda evt: self._show_open_world()
        )
        # menu_dict.setdefault('&File', {}).setdefault('system', {}).setdefault('Create World', lambda: self.world.save())
        menu_dict.setdefault("&File", {}).setdefault("exit", {}).setdefault(
            "Quit", lambda evt: self.Close()
        )
        menu_dict = self._last_page.menu(menu_dict)
        menu_bar = wx.MenuBar()
        for menu_name, menu_data in menu_dict.items():
            menu = wx.Menu()
            separator = False
            for menu_section in menu_data.values():
                if separator:
                    menu.AppendSeparator()
                separator = True
                for menu_item_name, menu_item_options in menu_section.items():
                    callback = None
                    menu_item_description = None
                    wx_id = None
                    if callable(menu_item_options):
                        callback = menu_item_options
                    elif isinstance(menu_item_options, tuple):
                        if len(menu_item_options) >= 1:
                            callback = menu_item_options[0]
                        if len(menu_item_options) >= 2:
                            menu_item_description = menu_item_options[1]
                        if len(menu_item_options) >= 3:
                            wx_id = menu_item_options[2]
                    else:
                        continue

                    if not menu_item_description:
                        menu_item_description = ""
                    if not wx_id:
                        wx_id = wx.ID_ANY

                    menu_item: wx.MenuItem = menu.Append(
                        wx.ID_ANY, menu_item_name, menu_item_description
                    )
                    self.Bind(wx.EVT_MENU, callback, menu_item)
            menu_bar.Append(menu, menu_name)
        self.SetMenuBar(menu_bar)

    def _page_change(self, evt):
        self._disable_enable()

    def _disable_enable(self):
        current: BaseWorldUI = self.world_tab_holder.GetCurrentPage()
        if self._last_page != current:
            if self._last_page is not None:
                self._last_page.disable()
            self._last_page: BaseWorldUI = current
            if self._last_page is self._main_menu:
                self.world_tab_holder.SetAGWWindowStyleFlag(NOTEBOOK_MENU_STYLE)
            else:
                self.world_tab_holder.SetAGWWindowStyleFlag(NOTEBOOK_STYLE)
        if self._last_page is not None:
            self._last_page.enable()

    def _add_world_tab(self, obj, obj_name):
        self.world_tab_holder.AddPage(obj, obj_name, True)
        self._disable_enable()

    def _show_open_world(self):
        select_world = WorldSelectDialog(self, self._open_world)
        select_world.ShowModal()
        select_world.Destroy()

    def _open_world(self, path: str):
        """Open a world panel add add it to the notebook"""
        if path in self._open_worlds:
            self.world_tab_holder.SetSelection(
                self.world_tab_holder.GetPageIndex(self._open_worlds[path])
            )
            self._disable_enable()
        else:
            try:
                world = WorldManagerUI(
                    self.world_tab_holder, path, lambda: self.close_world(path)
                )
            except LoaderNoneMatched as e:
                log.error(e)
                wx.MessageBox(str(e))
            else:
                self._open_worlds[path] = world
                self._add_world_tab(world, world.world_name)

    def close_world(self, path: str):
        """Close a given world and remove it from the notebook"""
        if path in self._open_worlds:
            world = self._open_worlds[path]
            self.world_tab_holder.DeletePage(self.world_tab_holder.GetPageIndex(world))

    def _on_page_close(self, evt: flatnotebook.EVT_FLATNOTEBOOK_PAGE_CLOSING):
        page: CLOSEABLE_PAGE_TYPE = self.world_tab_holder.GetPage(evt.GetSelection())
        if page is not self._main_menu:
            if page.is_closeable():
                path = page.path
                page.disable()
                page.close()
                self._last_page = None
                del self._open_worlds[path]
            else:
                evt.Veto()

    def _on_close_app(self, evt):
        for path, page in list(self._open_worlds.items()):
            self.close_world(path)
        if self.world_tab_holder.GetPageCount() > 1:
            wx.MessageBox("A world is still being used. Please close it first")
        else:
            evt.Skip()


class AmuletMainMenu(wx.Panel, BaseWorldUI):
    def __init__(self, parent: wx.Window, open_world):
        super(AmuletMainMenu, self).__init__(parent)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(sizer)
        sizer.AddStretchSpacer(1)
        self._open_world_callback = open_world
        name_sizer = wx.BoxSizer()
        sizer.Add(name_sizer, 0, wx.CENTER)
        img = wx.Image(os.path.join(IMG_DIR, "icon128.png"), wx.BITMAP_TYPE_ANY)

        icon = wx.StaticBitmap(
            self,
            wx.ID_ANY,
            img.Scale(64, 64, wx.IMAGE_QUALITY_NEAREST).ConvertToBitmap(),
            (0, 0),
            (64, 64),
        )
        icon2 = wx.StaticBitmap(
            self,
            wx.ID_ANY,
            img.Scale(64, 64, wx.IMAGE_QUALITY_NEAREST).ConvertToBitmap(),
            (0, 0),
            (64, 64),
        )
        icon2.Bind(
            wx.EVT_LEFT_DOWN, lambda evt: wx.lib.inspection.InspectionTool().Show()
        )
        name_sizer.Add(icon, flag=wx.CENTER)

        amulet_converter = wx.StaticText(self, label="Amulet")
        amulet_converter.SetFont(wx.Font(40, wx.DECORATIVE, wx.NORMAL, wx.NORMAL))
        name_sizer.Add(amulet_converter, flag=wx.CENTER)
        name_sizer.Add(icon2, flag=wx.CENTER)
        button_font = wx.Font(20, wx.DECORATIVE, wx.NORMAL, wx.NORMAL)
        self._open_world_button = wx.Button(self, label="Open World", size=(400, 70))
        self._open_world_button.SetFont(button_font)
        self._open_world_button.Bind(wx.EVT_BUTTON, self._show_world_select)
        sizer.Add(self._open_world_button, 0, wx.ALL | wx.CENTER, 5)

        self._help_button = wx.Button(self, label="Help", size=(400, 70))
        self._help_button.SetFont(button_font)
        self._help_button.Bind(wx.EVT_BUTTON, self._documentation)
        sizer.Add(self._help_button, 0, wx.ALL | wx.CENTER, 5)

        self._help_button = wx.Button(self, label="Amulet Discord", size=(400, 70))
        self._help_button.SetFont(button_font)
        self._help_button.Bind(wx.EVT_BUTTON, self._discord)
        sizer.Add(self._help_button, 0, wx.ALL | wx.CENTER, 5)

        sizer.AddStretchSpacer(2)

    def _show_world_select(self, evt):
        select_world = WorldSelectDialog(self, self._open_world_callback)
        select_world.ShowModal()
        select_world.Destroy()

    def _documentation(self, evt):
        webbrowser.open(
            "https://github.com/Amulet-Team/Amulet-Map-Editor/blob/master/amulet_map_editor/readme.md"
        )

    def _discord(self, evt):
        webbrowser.open("https://discord.gg/BTm6jnf")

    def enable(self):
        self.GetGrandParent().create_menu()
