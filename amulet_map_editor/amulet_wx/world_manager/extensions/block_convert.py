from amulet_map_editor.amulet_wx.block_select import VersionSelect, BlockSelect, BlockDefine
from amulet_map_editor.amulet_wx.world_manager import BaseWorldTool
from amulet.api.world import World
import wx
from concurrent.futures import ThreadPoolExecutor

thread_pool_executor = ThreadPoolExecutor(max_workers=1)
work_count = 0


class ConvertExtension(BaseWorldTool):
    def __init__(self, container, world: World):
        super(ConvertExtension, self).__init__(
            container
        )
        self.world = world
        self._version_select = BlockDefine(self, world.world_wrapper.translation_manager)
        self._version_select.populate()
        self.add_object(self._version_select, 0, wx.EXPAND)


export = {
    "name": "Block Convert",
    "ui": ConvertExtension
}
