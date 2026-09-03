from __future__ import annotations

from typing import TYPE_CHECKING
import os
import sys
import subprocess
from threading import Thread

import wx

from amulet.api.level.world import WorldFormatWrapper
from amulet.level.formats.leveldb_world import LevelDBFormat

from amulet_map_editor.api import lang
from amulet_map_editor.api.wx.ui.select_world import get_world_image
from amulet_map_editor.api.wx.ui.image_widget import ImageWidget
from amulet_map_editor.api.framework.programs import BaseProgram

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel


class AboutProgram(wx.Panel, BaseProgram):
    def __init__(self, container: wx.Window, world: BaseLevel):
        super().__init__(container)
        self._level = world

        level_wrapper = world.level_wrapper
        self._level_path = level_wrapper.path

        self._sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self._sizer)

        self._sizer.Add(
            wx.StaticText(
                self,
                label=f"{lang.get('program_about.choose_from_options')}\n<=================",
            ),
            0,
            wx.ALL | wx.ALIGN_LEFT,
            5,
        )

        self._sizer.Add(
            wx.StaticLine(self, style=wx.LI_HORIZONTAL),
            0,
            wx.ALL | wx.EXPAND,
        )

        self._sizer.AddSpacer(20)

        self._currently_opened_text = wx.StaticText(
            self,
            label=lang.get("program_about.currently_opened_world"),
        )
        self._currently_opened_text.SetFont(
            wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        )
        self._sizer.Add(
            self._currently_opened_text, 0, wx.ALL | wx.ALIGN_CENTRE_HORIZONTAL, 5
        )

        if isinstance(level_wrapper, WorldFormatWrapper):
            img = get_world_image(level_wrapper.world_image_path)
            self._world_image = ImageWidget(
                self, img, wx.Size(int(128 * img.GetWidth() / img.GetHeight()), 128)
            )
            self._sizer.Add(self._world_image, 0, wx.ALIGN_CENTER_HORIZONTAL)

        self._world_name = wx.StaticText(
            self, label=level_wrapper.level_name, style=wx.ALIGN_CENTER_HORIZONTAL
        )
        self._world_name.SetFont(wx.Font(15, wx.DEFAULT, wx.NORMAL, wx.NORMAL))
        self._sizer.Add(self._world_name, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self._world_version = wx.StaticText(
            self,
            label=level_wrapper.game_version_string,
            style=wx.ALIGN_CENTER_HORIZONTAL,
        )
        self._sizer.Add(self._world_version, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self._world_path = wx.StaticText(
            self,
            label=os.path.normpath(self._level_path).replace("\\", "/"),
            style=wx.ST_ELLIPSIZE_START,
        )
        font = self._world_path.GetFont()
        font.SetUnderlined(True)
        self._world_path.SetFont(font)
        self._world_path.SetForegroundColour(wx.Colour(0, 0, 238))
        self._world_path.Bind(wx.EVT_LEFT_UP, self._open_level)
        self._sizer.Add(self._world_path, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        if isinstance(level_wrapper, LevelDBFormat):
            self._sizer.AddSpacer(20)
            self._sizer.Add(
                wx.StaticLine(self, style=wx.LI_HORIZONTAL),
                0,
                wx.ALL | wx.EXPAND,
            )
            self._sizer.AddSpacer(20)

            self._compact_button = wx.Button(
                self, label=lang.get("program_about.compact_level")
            )
            self._compact_button.SetToolTip(
                lang.get("program_about.compact_level_tooltip")
            )
            font = self._compact_button.GetFont()
            font.SetPointSize(15)
            self._compact_button.SetFont(font)
            self._compact_button.Bind(wx.EVT_BUTTON, self._compact_level)
            self._sizer.Add(
                self._compact_button, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5
            )

    def _open_level(self, evt: wx.Event) -> None:
        path = self._level_path
        if os.path.isfile(path):
            path = os.path.dirname(path)
        if sys.platform == "win32":
            os.startfile(path)
        elif sys.platform == "darwin":
            subprocess.run(["open", path])
        else:
            subprocess.run(["xdg-open", path])

    def _compact_level(self, evt: wx.Event) -> None:
        level_wrapper = self._level.level_wrapper
        if isinstance(level_wrapper, LevelDBFormat):
            db = level_wrapper.level_db
            dialog = wx.ProgressDialog(
                "Amulet",
                lang.get("program_about.compacting_level"),
                maximum=10_000,
                parent=self,
                style=wx.PD_APP_MODAL | wx.PD_ELAPSED_TIME,
            )
            dialog.Fit()

            def compact() -> None:
                db.compact()
                wx.CallAfter(dialog.Destroy)

            # Set up a thread to run the actual operation
            thread = Thread(target=compact)
            thread.start()
