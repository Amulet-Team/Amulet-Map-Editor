from __future__ import annotations
import wx
from wx.lib.agw import flatnotebook
from typing import Dict, Union
import traceback
import logging

from amulet.api.errors import LoaderNoneMatched
from amulet_map_editor.api import config
from amulet_map_editor.api.wx.ui.select_world import open_level_from_dialog
from amulet_map_editor.api.wx.ui.traceback_dialog import TracebackDialog
from amulet_map_editor import __version__, lang
from amulet_map_editor.api.framework.pages import WorldPageUI
from .pages import AmuletMainMenu, BasePageUI
from .warning_dialog import WarningDialog

from amulet_map_editor.api import image
from amulet_map_editor.api.wx.util.ui_preferences import preserve_ui_preferences

log = logging.getLogger(__name__)

# Uses a conditional so if this breaks a build, we can just delete the file and it will skip the check
try:
    from amulet_map_editor.api.framework import update_check
except ImportError:
    update_check = None
    log.warning("Could not import update checker")

NOTEBOOK_MENU_STYLE = (
    flatnotebook.FNB_NO_X_BUTTON
    | flatnotebook.FNB_HIDE_ON_SINGLE_TAB
    | flatnotebook.FNB_NAV_BUTTONS_WHEN_NEEDED
)
NOTEBOOK_STYLE = NOTEBOOK_MENU_STYLE | flatnotebook.FNB_X_ON_TAB

CLOSEABLE_PAGE_TYPE = Union[WorldPageUI]

wx.Image.SetDefaultLoadFlags(0)


@preserve_ui_preferences
class AmuletUI(wx.Frame):
    """This is the top level frame that Amulet exists within."""

    # The notebook to hold world pages
    _level_notebook: AmuletLevelNotebook

    def __init__(self, parent):
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=f"Amulet V{__version__}",
            pos=wx.DefaultPosition,
            size=wx.Size(1000, 600),
            style=wx.CAPTION
            | wx.CLOSE_BOX
            | wx.MINIMIZE_BOX
            | wx.MAXIMIZE_BOX
            | wx.SYSTEM_MENU
            | wx.TAB_TRAVERSAL
            | wx.CLIP_CHILDREN
            | wx.RESIZE_BORDER,
        )
        self.SetMinSize((625, 440))
        icon = wx.Icon()
        icon.CopyFromBitmap(image.logo.amulet_logo.bitmap())
        self.SetIcon(icon)

        self._level_notebook = AmuletLevelNotebook(self, agwStyle=NOTEBOOK_MENU_STYLE)
        self._level_notebook.init()

        self.Bind(wx.EVT_CLOSE, self._level_notebook.on_app_close)

        meta_config = config.get("amulet_meta", {})
        if not meta_config.get("do_not_show_warning_dialog", False):
            warning_dialog = WarningDialog(self)
            warning_dialog.ShowModal()
            if warning_dialog.do_not_show_again:
                meta_config["do_not_show_warning_dialog"] = True
                config.put("amulet_meta", meta_config)

        if update_check:
            self.Bind(
                update_check.EVT_UPDATE_CHECK,
                lambda evt: update_check.UpdateDialog(
                    self, __version__, evt.GetVersion()
                ).ShowModal(),
            )
            update_check.check_for_update(self, __version__)

    def open_level(self, path: str):
        """Open a level. You should use the method in the app."""
        self._level_notebook.open_level(path)

    def close_level(self, path: str):
        """Close a given level. You should use the method in the app."""
        self._level_notebook.close_level(path)

    def create_menu(self):
        """
        Create the UI menu.

        Adds the top level menu items then extends it from the active page
        """
        menu_dict = {}
        menu_dict.setdefault(lang.get("menu_bar.file.menu_name"), {}).setdefault(
            "system", {}
        ).setdefault(
            lang.get("menu_bar.file.open_world"),
            lambda evt: open_level_from_dialog(self),
        )
        # menu_dict.setdefault(lang.get('menu_bar.file.menu_name'), {}).setdefault('system', {}).setdefault('Create World', lambda: self.world.save())
        menu_dict.setdefault(lang.get("menu_bar.file.menu_name"), {}).setdefault(
            "exit", {}
        ).setdefault(lang.get("menu_bar.file.quit"), lambda evt: self.Close())
        menu_dict = self._level_notebook.extend_menu(menu_dict)
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
                        wx_id, menu_item_name, menu_item_description
                    )
                    self.Bind(wx.EVT_MENU, callback, menu_item)
            menu_bar.Append(menu, menu_name)
        self.SetMenuBar(menu_bar)


class AmuletLevelNotebook(flatnotebook.FlatNotebook):
    """A notebook to hold all world tabs."""

    # The main menu tab
    _main_menu: AmuletMainMenu

    # Storage of open world tabs for easy lookup
    _open_worlds: Dict[str, CLOSEABLE_PAGE_TYPE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Bind(flatnotebook.EVT_FLATNOTEBOOK_PAGE_CLOSING, self._on_page_closing)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self._page_changing, self)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self._page_changed, self)

        self._main_menu = AmuletMainMenu(self)
        self._open_worlds = {}

    def init(self):
        self._add_world_tab(self._main_menu, lang.get("main_menu.tab_name"))

    def open_level(self, path: str):
        """Open a world panel add it to the notebook"""
        if path in self._open_worlds:
            self.SetSelection(self.GetPageIndex(self._open_worlds[path]))
        else:
            try:
                world = WorldPageUI(self, path)
            except LoaderNoneMatched as e:
                log.error(f"Could not find a loader for this world.\n{e}")
                wx.MessageBox(f"{lang.get('select_world.no_loader_found')}\n{e}")
            except Exception as e:
                log.error(lang.get("select_world.loading_world_failed"), exc_info=True)
                dialog = TracebackDialog(
                    self,
                    lang.get("select_world.loading_world_failed"),
                    str(e),
                    traceback.format_exc(),
                )
                dialog.ShowModal()
                dialog.Destroy()
            else:
                self._open_worlds[path] = world
                self._add_world_tab(world, world.world_name)

    def _add_world_tab(self, page: BasePageUI, obj_name: str):
        """Add a tab and enable it."""
        self.AddPage(page, obj_name, True)

    def close_level(self, path: str):
        """Close a given world and remove it from the notebook"""
        if path in self._open_worlds:
            world = self._open_worlds[path]
            # note we don't remove it from the dictionary here
            # delete page starts the deletion but it can be vetoed
            # it is deleted from the dictionary in _on_page_closing
            self.DeletePage(self.GetPageIndex(world))

    def _on_page_closing(self, evt: flatnotebook.EVT_FLATNOTEBOOK_PAGE_CLOSING):
        """Handle the page closing."""
        page: CLOSEABLE_PAGE_TYPE = self.GetPage(evt.GetSelection())
        if page is not self._main_menu:
            if page.can_disable() and page.can_close():
                path = page.path
                page.disable()
                page.close()
                del self._open_worlds[path]
            else:
                evt.Veto()

    def _page_changing(self, evt: wx.BookCtrlEvent):
        if (
            evt.GetOldSelection() != wx.NOT_FOUND
            and not self.GetPage(evt.GetOldSelection()).can_disable()
        ):
            evt.Veto()

    def _page_changed(self, evt: wx.BookCtrlEvent):
        """Handle the page changing."""
        if evt.GetOldSelection() != evt.GetSelection():
            if evt.GetOldSelection() != wx.NOT_FOUND:
                self.GetPage(evt.GetOldSelection()).disable()

            if self.GetCurrentPage() is self._main_menu:
                self.SetAGWWindowStyleFlag(NOTEBOOK_MENU_STYLE)
            else:
                self.SetAGWWindowStyleFlag(NOTEBOOK_STYLE)

        if self.GetCurrentPage() is not None:
            self.GetCurrentPage().enable()

    def on_app_close(self, evt: wx.CloseEvent):
        for path, page in list(self._open_worlds.items()):
            self.close_level(path)
        if self.GetPageCount() > 1:
            wx.MessageBox(lang.get("app.world_still_used"))
        else:
            evt.Skip()

    def extend_menu(self, menu_dict: dict) -> dict:
        return self.GetCurrentPage().menu(menu_dict)
