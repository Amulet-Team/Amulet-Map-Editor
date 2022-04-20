import wx
from typing import TYPE_CHECKING
import traceback
import logging

import amulet
from amulet.api.errors import LoaderNoneMatched

from amulet_map_editor.api.wx.ui.traceback_dialog import TracebackDialog
from amulet_map_editor.programs.edit.api.ui.tool import DefaultBaseToolUI
from amulet_map_editor.programs.edit.api.behaviour import StaticSelectionBehaviour


if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

log = logging.getLogger(__name__)


class ImportTool(wx.BoxSizer, DefaultBaseToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        DefaultBaseToolUI.__init__(self, canvas)

        self._selection = StaticSelectionBehaviour(self.canvas)

        self._open_file_button = wx.Button(canvas, label="Import File")
        self._open_file_button.Bind(wx.EVT_BUTTON, self._on_open_file)
        self.AddStretchSpacer()
        self.Add(self._open_file_button, flag=wx.ALL, border=10)
        self.AddStretchSpacer()

    @property
    def name(self) -> str:
        return "Import"

    def bind_events(self):
        super().bind_events()
        self._selection.bind_events()

    def enable(self):
        super().enable()
        self._selection.update_selection()

    def disable(self):
        super().disable()

    def _on_open_file(self, evt):
        with wx.FileDialog(
            self.canvas,
            "Open a Minecraft data file",
            wildcard="|".join(
                [  # TODO: Automatically load these from the FormatWrapper classes.
                    "All files (*.construction;*.mcstructure;*.schematic)|*.construction;*.mcstructure;*.schematic",
                    "Construction file (*.construction)|*.construction",
                    "Bedrock mcstructure file (*.mcstructure)|*.mcstructure",
                    "Legacy Schematic file (*.schematic)|*.schematic",
                    "Sponge Schematic file (*.schem)|*.schem",
                ]
            ),
            style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST,
        ) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            else:
                pathname = fileDialog.GetPath()
        try:
            level = amulet.load_level(pathname)
        except LoaderNoneMatched:
            msg = f"Could not find a matching loader for {pathname}."
            log.error(msg)
            wx.MessageBox(msg)
        except Exception as e:
            log.error(f"Could not open {pathname}.", exc_info=True)
            dialog = TracebackDialog(
                self.canvas,
                f"Could not open {pathname}.",
                str(e),
                traceback.format_exc(),
            )
            dialog.ShowModal()
            dialog.Destroy()
        else:
            self.canvas.paste(level, level.dimensions[0])
