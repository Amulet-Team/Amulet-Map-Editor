#!/usr/bin/env python3


def main():
    try:
        import sys

        if sys.version_info[:2] < (3, 7):
            raise Exception("Must be using Python 3.7+")

        import os
        import traceback
        import wx
        from amulet_map_editor import log
        from amulet_map_editor.api.framework import AmuletApp

        if sys.platform == "linux" and wx.VERSION >= (4, 1, 1):
            # bug 247
            os.environ["PYOPENGL_PLATFORM"] = "egl"

    except Exception as e:
        err = ""
        try:
            import traceback

            err += traceback.format_exc()
        except:
            pass
        err += (
            f"Failed to import requirements. Check that you extracted correctly.\n{e}"
        )
        print(err)
        with open("./logs/amulet_map_editor_.log", "w") as f:
            f.write(err)
        input("Press ENTER to continue.")
    else:
        try:
            app = AmuletApp(0)
            app.MainLoop()
        except Exception as e:
            log.critical(
                f"Amulet Crashed. Sorry about that. Please report it to a developer if you think this is an issue. \n{traceback.format_exc()}"
            )
            input("Press ENTER to continue.")


if __name__ == "__main__":
    main()
