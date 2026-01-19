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
    from typing import NoReturn
    from types import TracebackType
    import threading
    import faulthandler

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

    debug = "--amulet-debug" in sys.argv

    log_file = open(
        os.path.join(logs_path, f"amulet_{os.getpid()}.log"),
        "w",
        encoding="utf-8",
    )

    file_handler = logging.StreamHandler(log_file)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(levelname)s - %(name)s - %(message)s")
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(
        logging.Formatter(
            "%(levelname)s - %(name)s - %(message)s"
            if debug
            else "%(levelname)s - %(message)s"
        )
    )

    logging.basicConfig(
        level=logging.DEBUG if debug else logging.INFO,
        handlers=[file_handler, console_handler],
        force=True,
    )

    log = logging.getLogger(__name__)

    def error_handler(
        exc_type: type[BaseException],
        exc_value: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        if exc_value is None:
            return
        log.error("Unhandled exception", exc_info=(exc_type, exc_value, exc_tb))

    sys.excepthook = error_handler

    def thread_error_handler(args: threading.ExceptHookArgs) -> None:
        error_handler(args.exc_type, args.exc_value, args.exc_traceback)

    threading.excepthook = thread_error_handler

    # When running via pythonw the stderr is None so log directly to the log file
    faulthandler.enable(log_file)


def main() -> NoReturn:
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
        log = logging.getLogger(__name__)
        log.debug("Importing numpy")
        import numpy

        log.debug("Importing amulet_nbt")
        import amulet_nbt

        log.debug("Importing leveldb")
        import leveldb

        log.debug("Importing PyMCTranslate and amulet")
        import PyMCTranslate
        import amulet

        log.debug("Importing minecraft_model_reader")
        import minecraft_model_reader

        log.debug("Importing amulet_map_editor")
        from amulet_map_editor.api.framework import AmuletApp

        log.debug("Finished importing")

    except Exception as e:
        _on_error(e)
    else:
        try:
            app = AmuletApp(0)
            app.MainLoop()
        except Exception as e:
            log.critical(
                f"Amulet Crashed. Sorry about that. Please report it to a developer if you think this is an issue. \n{traceback.format_exc()}"
            )
            input("Press ENTER to continue.")

    sys.exit(0)


if __name__ == "__main__":
    main()
