import wx
from amulet_map_editor.api.wx.ui.mc.biome.biome_select import (
    demo as biome_select_demo,
)
from amulet_map_editor.api.wx.ui.mc.biome.biome_define import (
    demo as biome_define_demo,
)


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    biome_select_demo()
    biome_define_demo()


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
