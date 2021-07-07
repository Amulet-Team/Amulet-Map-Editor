import wx
from amulet_map_editor.api.wx.ui.mc.block.define.button.normal import (
    demo as normal_button_demo,
)
from amulet_map_editor.api.wx.ui.mc.block.define.button.wildcard import (
    demo as wildcard_button_demo,
)


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    normal_button_demo()
    wildcard_button_demo()


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
