import wx
from typing import List, Callable, Tuple, Type, Union, Optional
import traceback
import importlib
import pkgutil
import re

from amulet.api.errors import LoaderNoneMatched
from amulet import load_level

import amulet_map_editor
from amulet_map_editor import programs, log, lang
from amulet_map_editor.api.datatypes import MenuData
from amulet_map_editor.api.framework.pages import BasePageUI
from amulet_map_editor.api.framework.programs import BaseProgram, AboutProgram

_extensions: List[Tuple[str, Type[BaseProgram]]] = []
_fixed_extensions: List[Tuple[str, Type[BaseProgram]]] = [
    (lang.get("program_about.tab_name"), AboutProgram)
]


def load_extensions():
    if not _extensions:
        _extensions.extend(_fixed_extensions)
        prefix = f"{programs.__name__}."

        extensions = []

        # source support
        for _, name, _ in pkgutil.iter_modules(programs.__path__, prefix):
            extensions.append(load_extension(name))

        # pyinstaller support
        toc = set()
        for importer in pkgutil.iter_importers(amulet_map_editor.__name__):
            if hasattr(importer, "toc"):
                toc |= importer.toc
        match = re.compile(f"^{re.escape(prefix)}[a-zA-Z0-9_]*$")
        for name in toc:
            if match.fullmatch(name):
                extensions.append(load_extension(name))

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
    def __init__(
        self, parent: wx.Window, path: str, close_self_callback: Callable[[], None]
    ):
        super().__init__(parent, style=wx.NB_LEFT)
        self._path = path
        self._close_self_callback = close_self_callback
        try:
            self.world = load_level(path)
        except LoaderNoneMatched as e:
            self.Destroy()
            raise e
        self.world_name = self.world.level_wrapper.level_name
        self._extensions: List[BaseProgram] = []
        self._last_extension: int = -1
        self._load_extensions()
        self.Bind(wx.EVT_NOTEBOOK_PAGE_CHANGED, self._page_change)

    @property
    def path(self) -> str:
        return self._path

    def menu(self, menu: MenuData) -> MenuData:
        menu.setdefault(lang.get("menu_bar.file.menu_name"), {}).setdefault(
            "exit", {}
        ).setdefault(
            lang.get("menu_bar.file.close_world"), lambda evt: self._close_self_callback
        )
        return self._extensions[self.GetSelection()].menu(menu)

    def _load_extensions(self):
        """Load and create instances of each of the extensions"""
        load_extensions()
        select = True
        for extension_name, extension in _extensions:
            try:
                ext = extension(self, self.world, self._close_self_callback)
                self._extensions.append(ext)
                self.AddPage(ext, extension_name, select)
                select = False
            except Exception as e:
                log.exception(
                    f"Failed to load extension {extension_name}\n{e}\n{traceback.format_exc()}"
                )
                continue

    def is_closeable(self) -> bool:
        """Check if all extensions are safe to be closed"""
        return all(e.is_closeable() for e in self._extensions)

    def close(self):
        """Close the world and destroy the UI
        Check is_closeable before running this"""
        for ext in self._extensions:
            ext.close()
        dialog = None

        def init_dialog():
            nonlocal dialog
            dialog = wx.ProgressDialog(
                "Closing World",
                "Please be patient. This may take a little while.",
                maximum=100,
                parent=self,
                style=wx.PD_APP_MODAL | wx.PD_ELAPSED_TIME | wx.PD_AUTO_HIDE,
            )
            dialog.Fit()
            dialog.Update(99)

        timer = wx.CallLater(200, init_dialog)
        self.world.close()
        if dialog is None:
            timer.Stop()
        else:
            dialog.Update(100)

    def _page_change(self, _):
        """Method to fire when the page is changed"""
        if self.GetSelection() != self._last_extension:
            self._extensions[self._last_extension].disable()
            self._extensions[self.GetSelection()].enable()
            self.GetGrandParent().create_menu()
            self._last_extension = self.GetSelection()

    def disable(self):
        self._extensions[self.GetSelection()].disable()

    def enable(self):
        self._extensions[self.GetSelection()].enable()
        self.GetGrandParent().create_menu()
