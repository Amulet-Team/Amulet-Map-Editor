import wx
from typing import TYPE_CHECKING
import traceback

from amulet_map_editor import log
from amulet_map_editor.programs.edit.api.ui.tool import CameraToolUI
from amulet_map_editor.programs.edit.api.behaviour import StaticSelectionBehaviour
import amulet
from amulet.api.errors import LoaderNoneMatched

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas


class SelectImportOperationUI(wx.BoxSizer, CameraToolUI):
    def __init__(self, canvas: "EditCanvas"):
        wx.BoxSizer.__init__(self, wx.VERTICAL)
        CameraToolUI.__init__(self, canvas)

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
                    "Schematic file (*.schematic)|*.schematic",
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
            wx.MessageBox(f"Could not find a matching loader for {pathname}.")
            log.error(f"Could not find a matching loader for {pathname}.")
        except Exception as e:
            wx.MessageBox(
                f"Could not open {pathname}. Check the console for more details.\n{e}"
            )
            log.error(
                f"Could not open {pathname}. Check the console for more details.\n{traceback.format_exc()}"
            )
        else:
            self.canvas.paste(level, level.dimensions[0])
