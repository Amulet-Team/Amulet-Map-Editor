import wx
from concurrent.futures import ThreadPoolExecutor
import webbrowser
from typing import TYPE_CHECKING, Callable

from amulet import load_format
from amulet.api.level import BaseLevel

from amulet_map_editor import lang, log
from amulet_map_editor.api.wx.ui.simple import SimplePanel
from amulet_map_editor.api.wx.ui.select_world import WorldSelectDialog, WorldUI
from amulet_map_editor.api.datatypes import MenuData
from amulet_map_editor.api.framework.programs import BaseProgram

if TYPE_CHECKING:
    from amulet.api.wrapper import WorldFormatWrapper

thread_pool_executor = ThreadPoolExecutor(max_workers=1)
work_count = 0


class ConvertExtension(SimplePanel, BaseProgram):
    def __init__(
        self, container, world: BaseLevel, close_self_callback: Callable[[], None]
    ):
        SimplePanel.__init__(self, container)
        self.world = world
        self._close_self_callback = close_self_callback

        self._close_world_button = wx.Button(
            self, wx.ID_ANY, label=lang.get("world.close_world")
        )
        self._close_world_button.Bind(wx.EVT_BUTTON, self._close_world)
        self.add_object(self._close_world_button, 0, wx.ALL | wx.CENTER)

        self._input = SimplePanel(self, wx.HORIZONTAL)
        self.add_object(self._input, 0, wx.ALL | wx.CENTER)
        self._input.add_object(
            wx.StaticText(
                self._input,
                wx.ID_ANY,
                "{}: ".format(lang.get("program_convert.input_world")),
                wx.DefaultPosition,
                wx.DefaultSize,
                0,
            ),
            0,
            wx.ALL | wx.CENTER,
        )
        self._input.add_object(
            WorldUI(self._input, self.world.level_wrapper), 0, wx.ALL | wx.CENTER
        )

        self._output = SimplePanel(self, wx.HORIZONTAL)
        self.add_object(self._output, 0, wx.ALL | wx.CENTER)
        self._output.add_object(
            wx.StaticText(
                self._output,
                wx.ID_ANY,
                "{}: ".format(lang.get("program_convert.output_world")),
                wx.DefaultPosition,
                wx.DefaultSize,
                0,
            ),
            0,
            wx.ALL | wx.CENTER,
        )

        self._select_output_button = wx.Button(
            self, wx.ID_ANY, label=lang.get("program_convert.select_output_world")
        )
        self._select_output_button.Bind(wx.EVT_BUTTON, self._show_world_select)
        self.add_object(self._select_output_button, 0, wx.ALL | wx.CENTER)

        self._convert_bar = SimplePanel(self, wx.HORIZONTAL)
        self.add_object(self._convert_bar, 0, wx.ALL | wx.CENTER)

        self.loading_bar = wx.Gauge(
            self._convert_bar,
            wx.ID_ANY,
            100,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.GA_HORIZONTAL,
        )
        self._convert_bar.add_object(self.loading_bar, options=wx.ALL | wx.EXPAND)
        self.loading_bar.SetValue(0)

        self.convert_button = wx.Button(
            self._convert_bar,
            wx.ID_ANY,
            label=lang.get("program_convert.convert_button"),
        )
        self._convert_bar.add_object(self.convert_button)
        self.convert_button.Bind(wx.EVT_BUTTON, self._convert_event)

        self.out_world_path = None

    def menu(self, menu: MenuData) -> MenuData:
        menu.setdefault("&Help", {}).setdefault("control", {}).setdefault(
            "Controls", lambda evt: self._help_controls()
        )
        return menu

    def _help_controls(self):
        webbrowser.open(
            "https://github.com/Amulet-Team/Amulet-Map-Editor/blob/master/amulet_map_editor/programs/convert/readme.md"
        )

    def _show_world_select(self, evt):
        select_world = WorldSelectDialog(self, self._output_world_callback)
        select_world.ShowModal()
        select_world.Destroy()

    def _output_world_callback(self, path):
        if path == self.world.world_path:
            wx.MessageBox(lang.get("program_convert.input_output_must_different"))
            return
        try:
            out_world_format = load_format(path)
            self.out_world_path = path

        except Exception:
            return

        for child in list(self._output.GetChildren())[1:]:
            child.Destroy()
        self._output.add_object(WorldUI(self._output, out_world_format), 0)
        self._output.Layout()
        self._output.Fit()
        self.Layout()
        # self.Fit()

    def _update_loading_bar(self, chunk_index, chunk_total):
        wx.CallAfter(self.loading_bar.SetValue, int(100 * chunk_index / chunk_total))

    def _convert_event(self, evt):
        if self.out_world_path is None:
            wx.MessageBox(lang.get("program_convert.select_before_converting"))
            return
        self.convert_button.Disable()
        global work_count
        work_count += 1
        thread_pool_executor.submit(self._convert_method)
        # self.world.save(self.out_world, self._update_loading_bar)

    def _convert_method(self):
        global work_count
        try:
            out_world = load_format(self.out_world_path)
            log.info(f"Converting world {self.world.level_path} to {out_world.path}")
            out_world: WorldFormatWrapper
            out_world.open()
            self.world.save(out_world, self._update_loading_bar)
            out_world.close()
            message = lang.get("program_convert.conversion_completed")
            log.info(
                f"Finished converting world {self.world.level_path} to {out_world.path}"
            )
        except Exception as e:
            message = f"Error during conversion\n{e}"
            log.error(message, exc_info=True)
        self._update_loading_bar(0, 100)
        self.convert_button.Enable()
        wx.MessageBox(message)
        work_count -= 1

    def is_closeable(self):
        if work_count:
            log.info(
                f"World {self.world.level_path} is still being converted. Please let it finish before closing"
            )
        return work_count == 0

    def _close_world(self, evt):
        self._close_self_callback()
