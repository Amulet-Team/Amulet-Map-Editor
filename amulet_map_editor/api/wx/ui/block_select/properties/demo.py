import wx
from amulet_map_editor.api.wx.ui.block_select.properties.single_properties import (
    demo as single_properties_demo,
)
from amulet_map_editor.api.wx.ui.block_select.properties.wildcard_properties import (
    demo as wildcard_properties_demo,
)


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    single_properties_demo()
    wildcard_properties_demo()


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
