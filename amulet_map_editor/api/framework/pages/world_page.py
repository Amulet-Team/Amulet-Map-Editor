import threading

import wx
from typing import List, Callable, Tuple, Type, Union, Optional
import traceback
import importlib
import pkgutil

from amulet.api.errors import LoaderNoneMatched
from amulet import load_level

from amulet_map_editor import programs, log, lang
from amulet_map_editor.api.datatypes import MenuData
from amulet_map_editor.api.framework.pages import BasePageUI
from amulet_map_editor.api.framework.programs import BaseProgram, AboutProgram
from amulet_map_editor.api.wx.ui.traceback_dialog import TracebackDialog

_extensions: List[Tuple[str, Type[BaseProgram]]] = []
_fixed_extensions: List[Tuple[str, Type[BaseProgram]]] = [
    (lang.get("program_about.tab_name"), AboutProgram)
]


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
        self._active_extension: int = -1
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

    def _page_change(self, _):
        """Method to fire when the page is changed"""
        if self.GetSelection() != self._active_extension:
            self._enable_active()

    def _disable_active(self):
        if self._active_extension >= 0:
            try:
                self._extensions[self._active_extension].disable()
            except Exception as e:
                log.critical(traceback.format_exc())
            finally:
                self._active_extension = -1

    def _enable_active(self):
        self._disable_active()
        try:
            self._extensions[self.GetSelection()].enable()
            self.GetGrandParent().create_menu()
        except Exception as e:
            log.critical(traceback.format_exc())
            dialog = TracebackDialog(
                self, "Exception loading sub-program", str(e), traceback.format_exc()
            )
            dialog.ShowModal()
            dialog.Destroy()
            self._extensions.pop(self.GetSelection())
            self._active_extension = -1
            self.DeletePage(self.GetSelection())
        else:
            self._active_extension = self.GetSelection()

    def disable(self):
        """Disable all containers in the world page"""
        self._disable_active()

    def enable(self):
        """Enable the world page"""
        self._enable_active()
