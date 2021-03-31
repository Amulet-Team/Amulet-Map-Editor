#!/usr/bin/env python3

import sys

if sys.version_info[:2] < (3, 7):
    raise Exception("Must be using Python 3.7+")

from amulet_map_editor import log
from amulet_map_editor.api.framework import AmuletApp
import traceback

if __name__ == "__main__":
    try:
        app = AmuletApp()
        app.MainLoop()
    except Exception as e:
        log.critical(
            f"Amulet Crashed. Sorry about that. Please report it to a developer if you think this is an issue. \n{traceback.format_exc()}"
        )
        input("Press ENTER to continue.")
