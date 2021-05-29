from amulet_map_editor.api.wx.ui.biome_select.demo import demo as biome_demo
from amulet_map_editor.api.wx.ui.block_select.demo import demo as block_demo
from amulet_map_editor.api.wx.ui.nbt_editor import demo as nbt_editor_demo
from amulet_map_editor.api.wx.ui.select_world import demo as select_world_demo
from amulet_map_editor.api.wx.ui.version_select.demo import demo as version_select_demo


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    biome_demo()
    block_demo()
    nbt_editor_demo()
    select_world_demo()
    version_select_demo()


if __name__ == "__main__":

    import wx

    app = wx.App()
    demo()
    app.MainLoop()
