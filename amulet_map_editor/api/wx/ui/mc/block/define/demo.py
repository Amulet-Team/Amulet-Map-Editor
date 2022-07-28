import wx
from amulet_map_editor.api.wx.ui.mc.block.define.button.demo import (
    demo as block_button_demo,
)
from amulet_map_editor.api.wx.ui.mc.block.define.widget.demo import (
    demo as block_widget_demo,
)


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    block_button_demo()
    block_widget_demo()


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
