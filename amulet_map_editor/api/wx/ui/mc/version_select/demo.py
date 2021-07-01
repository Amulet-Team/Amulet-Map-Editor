import wx
from amulet_map_editor.api.wx.ui.mc.version_select.platform_select import (
    demo as platform_demo,
)
from amulet_map_editor.api.wx.ui.mc.version_select.version_select import (
    demo as version_demo,
)


def demo():
    """
    Show a demo version of the UI.
    An app instance must be created first.
    """
    platform_demo()
    version_demo()


if __name__ == "__main__":

    def main():
        app = wx.App()
        demo()
        app.MainLoop()

    main()
