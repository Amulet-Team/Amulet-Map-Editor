import wx
from amulet_map_editor.api.wx.ui.mc.block.properties.single import (
    demo as single_properties_demo,
)
from amulet_map_editor.api.wx.ui.mc.block.properties.multiple import (
    demo as multiple_properties_demo,
)


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    single_properties_demo()
    multiple_properties_demo()


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
