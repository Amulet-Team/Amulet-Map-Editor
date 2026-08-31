from __future__ import annotations
import wx
import wx.aui as aui
from typing import Dict, Union
import traceback
import logging
import sys
import os

from amulet.api.errors import LoaderNoneMatched
from amulet_map_editor.api.wx.ui.select_world import open_level_from_dialog
from amulet_map_editor.api.wx.ui.traceback_dialog import TracebackDialog
from amulet_map_editor import __version__, lang
from amulet_map_editor.api.framework.pages import WorldPageUI
from .pages import AmuletMainMenu, BasePageUI

from amulet_map_editor.api import image

log = logging.getLogger(__name__)

NOTEBOOK_MENU_STYLE = (
    aui.AUI_NB_TOP
    | aui.AUI_NB_SCROLL_BUTTONS
    | aui.AUI_NB_TAB_MOVE
    | aui.AUI_NB_MIDDLE_CLICK_CLOSE
)
NOTEBOOK_STYLE = NOTEBOOK_MENU_STYLE | aui.AUI_NB_CLOSE_ON_ACTIVE_TAB

CLOSEABLE_PAGE_TYPE = Union[WorldPageUI]

wx.Image.SetDefaultLoadFlags(0)


class AmuletUI(wx.Frame):
    """This is the top level frame that Amulet exists within."""

    # The notebook to hold world pages
    _level_notebook: AmuletLevelNotebook

    def __init__(self, parent):
        title = f"Amulet {__version__}"
        if not (getattr(sys, "frozen", False) or os.path.exists("/.flatpak-info")):
            title += " (source)"
        wx.Frame.__init__(
            self,
            parent,
            id=wx.ID_ANY,
            title=title,
            pos=wx.DefaultPosition,
            size=wx.Size(1000, 620),
            style=wx.CAPTION
            | wx.CLOSE_BOX
            | wx.MINIMIZE_BOX
            | wx.MAXIMIZE_BOX
            | wx.SYSTEM_MENU
            | wx.TAB_TRAVERSAL
            | wx.CLIP_CHILDREN
            | wx.RESIZE_BORDER,
        )
        self.SetMinSize(wx.Size(570, 670))
        icon = wx.Icon()
        icon.CopyFromBitmap(image.logo.amulet_logo.bitmap())
        self.SetIcon(icon)

        self._level_notebook = AmuletLevelNotebook(self, style=NOTEBOOK_MENU_STYLE)
        self._level_notebook.init()

        self.Bind(wx.EVT_CLOSE, self._level_notebook.on_app_close)

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
                    menu.Bind(wx.EVT_MENU, callback, menu_item)
            menu_bar.Append(menu, menu_name)
        old_menu = self.GetMenuBar()
        self.SetMenuBar(menu_bar)
        if old_menu is not None:
            old_menu.Destroy()


class AmuletLevelNotebook(aui.AuiNotebook):
    """A notebook to hold all world tabs."""

    # The main menu tab
    _main_menu: AmuletMainMenu

    # Storage of open world tabs for easy lookup
    _open_worlds: Dict[str, CLOSEABLE_PAGE_TYPE]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CLOSE, self._on_page_close)
        self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CLOSED, self._on_page_closed)
        self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CHANGING, self._page_changing, self)
        self.Bind(aui.EVT_AUINOTEBOOK_PAGE_CHANGED, self._page_changed, self)

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
                with TracebackDialog(
                    self,
                    lang.get("select_world.loading_world_failed"),
                    str(e),
                    traceback.format_exc(),
                ) as dialog:
                    log.debug(f"Showing TracebackDialog at {dialog.GetRect()}")
                    dialog.ShowModal()
            else:
                self._open_worlds[path] = world
                self._add_world_tab(world, world.world_name)

    def _add_world_tab(self, page: BasePageUI, obj_name: str):
        """Add a tab and enable it."""
        self.AddPage(page, obj_name, True)
        self._update_tab_visibility()

    def close_level(self, path: str):
        """Close a given world and remove it from the notebook"""
        if path in self._open_worlds:
            world = self._open_worlds[path]
            index = self.GetPageIndex(world)
            if self._close_page(index):
                self.DeletePage(index)
                self._update_tab_visibility()

    def _close_page(self, index: int) -> bool:
        """
        Close the page at the given index.
        Returns True if it was closed.
        The caller is responsible for removing the page from the notebook.
        """
        page = self.GetPage(index)
        if page is self._main_menu:
            return False
        if isinstance(page, WorldPageUI):
            if not (page.can_disable() and page.can_close()):
                return False
            path = page.path
            page.disable()
            page.close()
            del self._open_worlds[path]
        return True

    def _on_page_close(self, evt: aui.AuiNotebookEvent):
        """The user clicked a tab's close button."""
        if not self._close_page(evt.GetSelection()):
            evt.Veto()

    def _on_page_closed(self, evt: aui.AuiNotebookEvent):
        """Handle AuiNotebook finishing the removal of a closed page."""
        evt.Skip()
        self._update_tab_visibility()

    def _update_tab_visibility(self):
        """Show or hide the tab bar."""
        if self.GetPageCount() <= 1:
            self.SetTabCtrlHeight(0)
        else:
            self.SetTabCtrlHeight(-1)

    def _page_changing(self, evt: aui.AuiNotebookEvent):
        old_selection_index = evt.GetOldSelection()
        if old_selection_index != wx.NOT_FOUND:
            old_page = self.GetPage(old_selection_index)
            if old_page is not None and not old_page.can_disable():
                evt.Veto()

    def _page_changed(self, evt: aui.AuiNotebookEvent):
        """Handle the page changing."""
        if evt.GetOldSelection() != evt.GetSelection():
            if evt.GetOldSelection() != wx.NOT_FOUND:
                old_page = self.GetPage(evt.GetOldSelection())
                if old_page is not None:
                    old_page.disable()

            if self.GetCurrentPage() is self._main_menu:
                self.SetWindowStyleFlag(NOTEBOOK_MENU_STYLE)
            else:
                self.SetWindowStyleFlag(NOTEBOOK_STYLE)
            self.Refresh()

        if self.GetCurrentPage() is not None:
            self.GetCurrentPage().enable()

    def on_app_close(self, evt: wx.CloseEvent):
        for path in list(self._open_worlds.keys()):
            self.close_level(path)
        if self.GetPageCount() > 1:
            wx.MessageBox(lang.get("app.world_still_used"))
        else:
            evt.Skip()

    def extend_menu(self, menu_dict: dict) -> dict:
        return self.GetCurrentPage().menu(menu_dict)
