import threading

import wx
from typing import List, Tuple, Type, Union, Optional
import traceback
import importlib
import pkgutil
import logging

from amulet.api.errors import LoaderNoneMatched
from amulet import load_level

from amulet_map_editor import programs, lang
from amulet_map_editor.api.datatypes import MenuData
from amulet_map_editor.api.framework import app
from amulet_map_editor.api.framework.pages import BasePageUI
from amulet_map_editor.api.framework.programs import BaseProgram, AboutProgram
from amulet_map_editor.api.wx.ui.traceback_dialog import TracebackDialog

_extensions: List[Tuple[str, Type[BaseProgram]]] = []
_fixed_extensions: List[Tuple[str, Type[BaseProgram]]] = [
    (lang.get("program_about.tab_name"), AboutProgram)
]

log = logging.getLogger(__name__)


def load_extensions():
    if not _extensions:
        _extensions.extend(_fixed_extensions)

        extensions = []

        for _, module_name, _ in pkgutil.iter_modules(
            programs.__path__, f"{programs.__name__}."
        ):
            extensions.append(load_extension(module_name))

        _extensions.extend(
            sorted((ext for ext in extensions if ext is not None), key=lambda x: x[0])
        )


def load_extension(
    module_name: str,
) -> Optional[Tuple[str, Union[Type[BaseProgram], Type[wx.Window]]]]:
    # load module and confirm that all required attributes are defined
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        log.warning(f"Failed to import {module_name}.\n{traceback.format_exc()}")
    else:
        if hasattr(module, "export"):
            export = getattr(module, "export")
            if isinstance(export, dict):
                ui = export.get("ui", None)
                name = export.get("name", None)
                if (
                    isinstance(name, str)
                    and issubclass(ui, BaseProgram)
                    and issubclass(ui, wx.Window)
                ):
                    return name, ui


class WorldPageUI(wx.Notebook, BasePageUI):
    def __init__(self, parent: wx.Window, path: str):
        super().__init__(parent, style=wx.NB_LEFT)
        self._path = path
        try:
            self.world = load_level(path)
        except LoaderNoneMatched as e:
            self.Destroy()
            raise e
        self.world_name = self.world.level_wrapper.level_name
        self._load_extensions()
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGING, self._page_changing, self)
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self._page_changed, self)

    def GetPage(self, page) -> BaseProgram:
        wx_page = super().GetPage(page)
        if not isinstance(wx_page, BaseProgram):
            raise Exception("GetPage did not return BaseProgram instance.")
        return wx_page

    @property
    def path(self) -> str:
        return self._path

    def menu(self, menu: MenuData) -> MenuData:
        menu.setdefault(lang.get("menu_bar.file.menu_name"), {}).setdefault(
            "exit", {}
        ).setdefault(
            lang.get("menu_bar.file.close_world"),
            lambda evt: app.close_level(self.path),
        )
        return self.GetPage(self.GetSelection()).menu(menu)

    def _load_extensions(self):
        """Load and create instances of each of the extensions"""
        load_extensions()
        select = True
        for extension_name, extension in _extensions:
            try:
                ext = extension(self, self.world)
                self.AddPage(ext, extension_name, select)
                select = False
            except Exception as e:
                log.exception(
                    f"Failed to load extension {extension_name}\n{e}\n{traceback.format_exc()}"
                )
                continue

    def can_close(self) -> bool:
        """Check if all extensions are safe to be closed"""
        return all(
            self.GetPage(page).can_close() for page in range(self.GetPageCount())
        )

    def close(self):
        """
        Close the world and destroy the UI
        Check can_close before running this
        """
        for page in range(self.GetPageCount()):
            self.GetPage(page).close()

        # close the world in a new thread
        thread = threading.Thread(target=self.world.close)
        thread.start()
        # sleep a little
        thread.join(0.1)
        if thread.is_alive():
            # if not closed yet open a dialog to warn the user.
            # We do this on a delay so that it does not flick up for a split second
            dialog = wx.ProgressDialog(
                "Closing World",
                "Please be patient. This may take a little while.",
                maximum=100,
                style=wx.PD_APP_MODAL | wx.PD_ELAPSED_TIME | wx.PD_AUTO_HIDE,
            )
            dialog.Fit()
            dialog.Update(99)
            # wait until the world is closed then close the dialog
            while thread.is_alive():
                wx.GetApp().Yield()
                thread.join(0.1)
            dialog.Destroy()

    def _page_changing(self, evt: wx.BookCtrlEvent):
        """Method to fire when the page is changing."""
        if (
            self.GetSelection() != wx.NOT_FOUND
            and not self.GetPage(self.GetSelection()).can_disable()
        ):
            evt.Veto()

    def _page_changed(self, evt: wx.BookCtrlEvent):
        """Method to fire when the page has changed."""
        self._disable_page(evt.GetOldSelection())
        self._enable_page(evt.GetSelection())

    def _disable_page(self, page: Optional[int] = None):
        """Disable a page. Defaults to the current page."""
        page = self.GetSelection() if page is None else page
        if page != wx.NOT_FOUND:
            try:
                self.GetPage(page).disable()
            except Exception as e:
                log.critical(traceback.format_exc())
                # raise e

    def _enable_page(self, page: Optional[int] = None):
        """Enable a page. Defaults to the current page."""
        page = self.GetSelection() if page is None else page
        if page != wx.NOT_FOUND:
            try:
                self.GetPage(page).enable()
                self.GetTopLevelParent().create_menu()
            except Exception as e:
                log.critical(traceback.format_exc())
                dialog = TracebackDialog(
                    self,
                    "Exception loading sub-program",
                    str(e),
                    traceback.format_exc(),
                )
                dialog.ShowModal()
                dialog.Destroy()
                self.DeletePage(page)

    def can_disable(self) -> bool:
        return (
            self.GetSelection() == wx.NOT_FOUND
            or self.GetPage(self.GetSelection()).can_disable()
        )

    def disable(self):
        """Disable all containers in the world page"""
        self._disable_page()

    def enable(self):
        """Enable the world page"""
        self._enable_page()
