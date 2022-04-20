import logging
import sys
import os

log = logging.getLogger("amulet_map_editor")


def _init_logging():
    loggers = [
        log,
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

    # set up handlers
    os.makedirs(os.path.join(".", "logs"), exist_ok=True)
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
