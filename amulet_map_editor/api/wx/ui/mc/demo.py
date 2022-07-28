from amulet_map_editor.api.wx.ui.mc.version.demo import demo as version_select_demo
from amulet_map_editor.api.wx.ui.mc.biome.demo import demo as biome_demo
from amulet_map_editor.api.wx.ui.mc.block.demo import demo as block_demo


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    version_select_demo()
    biome_demo()
    block_demo()


if __name__ == "__main__":

    import wx

    app = wx.App()
    demo()
    app.MainLoop()
