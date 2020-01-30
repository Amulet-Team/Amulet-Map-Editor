from amulet_map_editor.amulet_wx.wx_util import SimplePanel
from amulet_map_editor.amulet_wx.world_select import WorldSelectAndRecentUI
from amulet import world_interface
from amulet.api.world import World
from amulet.world_interface.formats import Format
import wx
from amulet_map_editor import lang
from concurrent.futures import ThreadPoolExecutor

thread_pool_executor = ThreadPoolExecutor(max_workers=1)


class ConvertExtension(SimplePanel):
    def __init__(self, container, world: World):
        super(ConvertExtension, self).__init__(
            container
        )
        self.world = world
        self.add_object(WorldSelectAndRecentUI(self, self._output_world_callback))

        self.footer = SimplePanel(self, wx.HORIZONTAL)
        self.add_object(self.footer, 0)

        self.loading_bar = wx.Gauge(
            self.footer,
            wx.ID_ANY,
            100,
            wx.DefaultPosition,
            wx.DefaultSize,
            wx.GA_HORIZONTAL,
        )
        self.footer.add_object(self.loading_bar, options=wx.ALL | wx.EXPAND)
        self.loading_bar.SetValue(0)

        self.convert_button = wx.Button(self.footer, wx.ID_ANY, label=lang.get('convert'))
        self.footer.add_object(self.convert_button)
        self.convert_button.Bind(wx.EVT_BUTTON, self._convert_event)

        self.out_world_path = None

        self.world_text = wx.StaticText(
            self.footer,
            wx.ID_ANY,
            f'Input World: {self.world.world_wrapper.world_name}\nOutput World:',
            wx.DefaultPosition,
            wx.DefaultSize,
            0,
        )
        self.footer.add_object(self.world_text)

    def _output_world_callback(self, path):
        if path == self.world._directory: # TODO: make a public API for this
            return # TODO: dialogue box?
        try:
            out_world = world_interface.load_format(path)
            self.out_world_path = path

        except:
            return
        self.world_text.SetLabel(
            f'Input World: {self.world.world_wrapper.world_name}\nOutput World:{out_world.world_name}'
        )

    def _update_loading_bar(self, chunk_index, chunk_total):
        wx.CallAfter(self.loading_bar.SetValue, int(100*chunk_index/chunk_total))

    def _convert_event(self, evt):
        # TODO: put this on a separate thread so that the UI does not freeze but disable UI functionality
        thread_pool_executor.submit(self._convert_method)
        # self.world.save(self.out_world, self._update_loading_bar)

    def _convert_method(self):
        out_world = world_interface.load_format(self.out_world_path)
        out_world: Format
        out_world.open()
        self.world.save(out_world, self._update_loading_bar)
        out_world.close()
        self._update_loading_bar(0, 100)
        wx.MessageBox(
            'World conversion completed'
        )


export = {
    "name": "Convert",
    "ui": ConvertExtension
}
