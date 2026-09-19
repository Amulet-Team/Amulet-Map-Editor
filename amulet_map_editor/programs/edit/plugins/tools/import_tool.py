import wx
from typing import TYPE_CHECKING
import traceback
import logging

import amulet
from amulet.api.errors import LoaderNoneMatched

from amulet_map_editor import lang
from amulet_map_editor.api.wx.ui.traceback_dialog import TracebackDialog
from amulet_map_editor.programs.edit.api.ui.tool import DefaultBaseToolUI
from amulet_map_editor.programs.edit.api.behaviour import StaticSelectionBehaviour
from amulet_map_editor.programs.edit.api.events import ToolChangeEvent

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

log = logging.getLogger(__name__)


class ImportTool(wx.BoxSizer, DefaultBaseToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        DefaultBaseToolUI.__init__(self, canvas)

        self._selection = StaticSelectionBehaviour(self.canvas)

    @property
    def name(self) -> str:
        return "Import"

    def bind_events(self):
        super().bind_events()
        self._selection.bind_events()

    def enable(self):
        super().enable()
        self._selection.update_selection()
        self._open_file()

    def _open_file(self):
        with wx.FileDialog(
            self.canvas,
            lang.get("program_3d_edit.import.open_file"),
            wildcard="|".join(
                [  # TODO: Automatically load these from the FormatWrapper classes.
                    f"{lang.get('program_3d_edit.import.filter_all')}|*.construction;*.mcstructure;*.schematic;*.schem",
                    f"{lang.get('program_3d_edit.import.filter_construction')}|*.construction",
                    f"{lang.get('program_3d_edit.import.filter_mcstructure')}|*.mcstructure",
                    f"{lang.get('program_3d_edit.import.filter_schematic')}|*.schematic",
                    f"{lang.get('program_3d_edit.import.filter_sponge')}|*.schem",
                ]
            ),
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as fileDialog:
            log.debug(f"Showing Import FileDialog at {fileDialog.GetRect()}")
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                wx.PostEvent(
                    self.canvas,
                    ToolChangeEvent(tool="Select"),
                )
                return
            else:
                pathname = fileDialog.GetPath()
        try:
            level = amulet.load_level(pathname)
        except LoaderNoneMatched:
            msg = lang.get("program_3d_edit.import.no_loader").format(path=pathname)
            log.error(msg)
            wx.MessageBox(msg, lang.get("shared.message"))
        except Exception as e:
            log.error(f"Could not open {pathname}.", exc_info=True)
            with TracebackDialog(
                self.canvas,
                lang.get("program_3d_edit.import.open_failed").format(path=pathname),
                str(e),
                traceback.format_exc(),
            ) as dialog:
                log.debug(f"Showing TracebackDialog at {dialog.GetRect()}")
                dialog.ShowModal()
        else:
            self.canvas.paste(level, level.dimensions[0])
