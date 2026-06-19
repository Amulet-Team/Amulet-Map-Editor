#!/usr/bin/env python3


def _log_error(e) -> None:
    """Code to handle errors"""
    try:
        import traceback
        import sys
        import os

    except ImportError as e:
        # Something has gone seriously wrong
        print(e)
        print("Failed to import requirements. Check that you extracted correctly.")
    else:
        msg_lines = [traceback.format_exc()]
        if isinstance(e, ImportError):
            msg_lines.append(
                "Failed to import requirements. Check that you extracted correctly."
            )
        msg_lines.append(str(e))
        err = "\n".join(msg_lines)
        print(err)
        try:
            with open("crash.log", "w") as f:
                f.write(err)
        except OSError:
            pass


try:
    import sys

    if sys.version_info[:2] < (3, 7):
        raise Exception("Must be using Python 3.7+")
    import logging
    import os
    import traceback
    import glob
    import time
    import platformdirs
    from typing import NoReturn
    from types import TracebackType
    import threading
    import faulthandler
    import subprocess
    import multiprocessing
    import amulet_faulthandler
except Exception as e_:
    _log_error(e_)
    input("Press ENTER to continue.")
    sys.exit(1)


def _init_log() -> logging.Logger:
    logs_path = os.environ["LOG_DIR"]
    # set up handlers
    os.makedirs(logs_path, exist_ok=True)
    # remove all log files older than a week
    for path in glob.glob(os.path.join(glob.escape(logs_path), "*")):
        if (
            os.path.isfile(path)
            and os.path.getmtime(path) < time.time() - 3600 * 24 * 7
        ):
            os.remove(path)

    debug = "debug" in os.path.basename(sys.executable) or "--amulet-debug" in sys.argv

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

    if "--disable-py-faulthandler" not in sys.argv:
        # When running via pythonw the stderr is None so log directly to the log file
        faulthandler.enable(log_file)

    amulet_faulthandler.install(
        os.path.join(logs_path, f"amulet_{os.getpid()}.dmp"), debug
    )

    return log


def _app_main() -> int:
    if sys.platform == "linux":
        # bug 247
        os.environ.setdefault("PYOPENGL_PLATFORM", "egl")
        os.environ.setdefault("GDK_BACKEND", "x11")

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

    log = _init_log()

    try:
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

        app = AmuletApp(0)
        app.MainLoop()
    except Exception as e:
        log.critical(
            f"Amulet Crashed. Please report it to a developer. \n{traceback.format_exc()}"
        )
        return 1
    return 0


def main() -> NoReturn:
    is_launcher = False
    try:
        multiprocessing.freeze_support()
        is_launcher = "--amulet-main" not in sys.argv
        if is_launcher:
            if getattr(sys, "frozen", False):
                args = [sys.executable, "--amulet-main"] + sys.argv[1:]
            else:
                args = [sys.executable, __file__, "--amulet-main"] + sys.argv[1:]
            exit_code = subprocess.run(args).returncode
        else:
            exit_code = _app_main()
    except Exception as e:
        _log_error(e)
        exit_code = 1

    if is_launcher and exit_code:
        print(f"Application crashed with exit code {exit_code} (0x{exit_code:0X})")
        print("Please report this issue to a developer.")
        print("Attach the logs in the opened directory with your report.")
        log_dir = os.environ.get("LOG_DIR") or platformdirs.user_log_dir(
            "AmuletMapEditor", "AmuletTeam"
        )
        if sys.platform == "win32":
            os.startfile(log_dir)
        elif sys.platform == "darwin":
            subprocess.run(["open", log_dir])
        else:
            subprocess.run(["xdg-open", log_dir])
        if getattr(sys, "frozen", False) and sys.stdin is not None:
            input(f"Press ENTER to continue.")
    sys.exit(bool(exit_code))


if __name__ == "__main__":
    main()
