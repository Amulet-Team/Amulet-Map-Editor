#!/usr/bin/env python3


def _on_error(e):
    """Code to handle errors"""
    try:
        import traceback
        import sys
        import os

    except ImportError as e:
        # Something has gone seriously wrong
        print(e)
        print("Failed to import requirements. Check that you extracted correctly.")
        input("Press ENTER to continue.")
    else:
        err = "\n".join(
            [traceback.format_exc()]
            + ["Failed to import requirements. Check that you extracted correctly."]
            * isinstance(e, ImportError)
            + [str(e)]
        )
        print(err)
        try:
            with open("crash.log", "w") as f:
                f.write(err)
        except OSError:
            pass
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
    import platformdirs

    if sys.platform == "linux" and wx.VERSION >= (4, 1, 1):
        # bug 247
        os.environ["PYOPENGL_PLATFORM"] = "egl"
except Exception as e_:
    _on_error(e_)


def _init_log():
    logs_path = os.environ["LOG_DIR"]
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
        # Initialise default paths.
        data_dir = platformdirs.user_data_dir("AmuletMapEditor", "AmuletTeam")
        os.environ.setdefault("DATA_DIR", data_dir)
        config_dir = platformdirs.user_config_dir("AmuletMapEditor", "AmuletTeam")
        if config_dir == data_dir:
            config_dir = os.path.join(data_dir, "Config")
        os.environ.setdefault("CONFIG_DIR", config_dir)
        os.environ.setdefault(
            "CACHE_DIR", platformdirs.user_cache_dir("AmuletMapEditor", "AmuletTeam")
        )
        os.environ.setdefault(
            "LOG_DIR", platformdirs.user_log_dir("AmuletMapEditor", "AmuletTeam")
        )

        _init_log()
        from amulet_map_editor.api.framework import AmuletApp

    except Exception as e:
        _on_error(e)
    else:
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
