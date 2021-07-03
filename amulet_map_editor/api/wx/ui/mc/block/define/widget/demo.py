import wx
from amulet_map_editor.api.wx.ui.mc.block.define.block_define import (
    demo as block_define_demo,
)
from amulet_map_editor.api.wx.ui.mc.block.define.wildcard_block_define import (
    demo as wildcard_block_define_demo,
)


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    block_define_demo()
    wildcard_block_define_demo()


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
