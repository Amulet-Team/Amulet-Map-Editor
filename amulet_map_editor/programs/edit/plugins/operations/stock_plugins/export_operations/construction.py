from typing import TYPE_CHECKING
import os
import logging

import wx

from amulet.api.selection import SelectionGroup
from amulet.api.errors import ChunkLoadError
from amulet.api.data_types import Dimension, OperationReturnType
from amulet.level.formats.construction import ConstructionFormatWrapper

from amulet_map_editor import lang
from amulet_map_editor.api.wx.ui.version_select import VersionSelect
from amulet_map_editor.programs.edit.api.operations import (
    SimpleOperationPanel,
    OperationError,
)

if TYPE_CHECKING:
    from amulet.api.level import BaseLevel
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

log = logging.getLogger(__name__)


class ExportConstruction(SimpleOperationPanel):
    def __init__(
        self,
        parent: wx.Window,
        canvas: "EditCanvas",
        world: "BaseLevel",
        options_path: str,
    ):
        SimpleOperationPanel.__init__(self, parent, canvas, world, options_path)

        options = self._load_options({})

        self._path = options.get("path", "")

        self._version_define = VersionSelect(
            self,
            world.translation_manager,
            options.get("platform", None) or world.level_wrapper.platform,
            allow_universal=False,
        )
        self._sizer.Add(self._version_define, 0, wx.ALL | wx.EXPAND, 5)

        self._add_run_button(lang.get("shared.export"))
        self.Layout()

    def disable(self):
        self._save_options(
            {
                "path": self._path,
                "platform": self._version_define.platform,
                "version": self._version_define.version_number,
            }
        )

    def _pre_operation(self) -> bool:
        try:
            path = os.path.realpath(self._path)
            fname = os.path.basename(path)
            fdir = os.path.dirname(path)
        except:
            fname = ""
            fdir = ""
        with wx.FileDialog(
            self,
            lang.get("program_3d_edit.export.save_location"),
            defaultDir=fdir,
            defaultFile=fname,
            wildcard="Construction file (*.construction)|*.construction",
            style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT,
        ) as file_dialog:
            log.debug(f"Showing save dialog at {file_dialog.GetRect()}")
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return False
            self._path = file_dialog.GetPath()
        return True

    def _operation(
        self, world: "BaseLevel", dimension: Dimension, selection: SelectionGroup
    ) -> OperationReturnType:
        path = self._path
        platform = self._version_define.platform
        version = self._version_define.version_number
        if isinstance(path, str) and platform and version:
            wrapper = ConstructionFormatWrapper(path)
            wrapper.create_and_open(platform, version, selection, True)
            wrapper.translation_manager = world.translation_manager
            wrapper_dimension = wrapper.dimensions[0]
            chunk_count = len(list(selection.chunk_locations()))
            yield 0, lang.get("program_3d_edit.export.progress").format(
                name=os.path.basename(path)
            )
            for chunk_index, (cx, cz) in enumerate(selection.chunk_locations()):
                try:
                    chunk = world.get_chunk(cx, cz, dimension)
                    wrapper.commit_chunk(chunk, wrapper_dimension)
                except ChunkLoadError:
                    continue
                yield (chunk_index + 1) / chunk_count
            wrapper.save()
            wrapper.close()
        else:
            raise OperationError(
                lang.get("program_3d_edit.export.missing_path_version")
            )


export = {
    "name": "\t" + lang.get("program_3d_edit.export.construction.name"),
    "operation": ExportConstruction,  # the UI class to display
}
