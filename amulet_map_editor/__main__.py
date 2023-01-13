#!/usr/bin/env python3


def _on_error(e):
    """Code to handle errors"""
    err_list = []
    try:
        import traceback

        err_list.append(traceback.format_exc())
    except:
        pass
    if isinstance(e, ImportError):
        err_list.append(
            f"Failed to import requirements. Check that you extracted correctly."
        )
    err_list.append(str(e))
    err = "\n".join(err_list)
    print(err)
    with open("./logs/crash.log", "w") as f:
        f.write(err)
    input("Press ENTER to continue.")
    sys.exit(1)


try:
    import sys

    if sys.version_info[:2] < (3, 7):
        raise Exception("Must be using Python 3.7+")
    import logging
    import os
    import traceback
    import glob
    import time
    import wx

    if sys.platform == "linux" and wx.VERSION >= (4, 1, 1):
        # bug 247
        os.environ["PYOPENGL_PLATFORM"] = "egl"
except Exception as e:
    _on_error(e)


def _init_log():
    logs_path = os.path.join(".", "logs")
    # set up handlers
    os.makedirs(logs_path, exist_ok=True)
    # remove all log files older than a week
    for path in glob.glob(os.path.join(glob.escape(logs_path), "*.log")):
        if (
            os.path.isfile(path)
            and os.path.getmtime(path) < time.time() - 3600 * 24 * 7
        ):
            os.remove(path)

    log = logging.getLogger()
    log.setLevel(logging.DEBUG if "amulet-debug" in sys.argv else logging.INFO)

    file_handler = logging.FileHandler(
        os.path.join(logs_path, f"amulet_{os.getpid()}.log"), "w", encoding="utf-8"
    )
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )
    log.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))
    log.addHandler(console_handler)


def main():
    try:
        _init_log()
        from amulet_map_editor.api.framework import AmuletApp

    except Exception as e:
        _on_error(e)
        AmuletApp = None

    try:
        app = AmuletApp(0)
        app.MainLoop()
    except Exception as e:
        log = logging.getLogger(__name__)
        log.critical(
            f"Amulet Crashed. Sorry about that. Please report it to a developer if you think this is an issue. \n{traceback.format_exc()}"
        )
        input("Press ENTER to continue.")
    sys.exit(0)


if __name__ == "__main__":
    main()
