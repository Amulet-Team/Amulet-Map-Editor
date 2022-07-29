import logging
import sys
import os
import glob
import time


def _init_logging():
    loggers = [
        logging.getLogger("amulet_map_editor"),
        logging.getLogger("amulet"),
        logging.getLogger("minecraft_model_reader"),
        logging.getLogger("PyMCTranslate"),
    ]

    # reset all existing handlers
    for logger in loggers:
        while logger.hasHandlers():
            handler = logger.handlers[0]
            logger.removeHandler(handler)
            handler.close()
        logger.setLevel(logging.DEBUG if "amulet-debug" in sys.argv else logging.INFO)

    logs_path = os.path.join(".", "logs")
    # set up handlers
    os.makedirs(logs_path, exist_ok=True)
    # remove all log files older than a week
    for path in glob.glob(os.path.join(logs_path, "*.log")):
        if (
            os.path.isfile(path)
            and os.path.getmtime(path) < time.time() - 3600 * 24 * 7
        ):
            os.remove(path)

    file_handler = logging.FileHandler(
        os.path.join(".", "logs", f"amulet_{os.getpid()}.log"), "w", encoding="utf-8"
    )
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    )

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter("%(levelname)s - %(message)s"))

    # bind the handlers to each logger
    for logger in loggers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)


_init_logging()
