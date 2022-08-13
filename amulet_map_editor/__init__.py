import logging

experimental_bedrock_resources = False

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions
from amulet_map_editor.api import config as CONFIG, lang
from amulet_map_editor.api.framework.app import open_level, close_level


# This is here because of the major change in the NBT library
# We have tried updating all the code that will break, but we will inevitably miss some
# This modifies the behaviour of warnings.warn to notify us if the old functionality is still used so we can fix it.
def _patch_warn():
    from threading import Thread
    import warnings
    import urllib.request
    import urllib.parse
    from urllib.error import URLError
    import traceback
    import os
    import getpass

    stacks = set()

    def _call_home(message, category, stack):
        try:
            stack = stack.replace(
                os.getcwd(), "."
            )  # remove the parent path. We don't need it
            stack = stack.replace(
                getpass.getuser(), "%username%"
            )  # Remove the username just in case
        except:
            pass

        if stack not in stacks:
            stacks.add(stack)
            try:
                urllib.request.urlopen(
                    f"https://docs.google.com/forms/d/e/1FAIpQLSfYb44EYR78yJlQAgyf-GTWn1ZlaGNMuIerl_XTpaYN0d8B4Q/formResponse?"
                    f"entry.601089147={urllib.parse.quote(__version__)}&"
                    f"entry.961557167={urllib.parse.quote(message)}&"
                    f"entry.2137739277={urllib.parse.quote(str(category))}&"
                    f"entry.1185835095={urllib.parse.quote(stack)}",
                    timeout=5,
                )
            except URLError:
                pass

    _old_warn = warnings.warn

    def _on_warn(message, category=None, **kwargs):
        _old_warn(message, category, **kwargs)
        t = Thread(
            target=_call_home,
            args=(message, category, "".join(traceback.format_stack(limit=6))),
        )
        t.start()

    warnings.warn = _on_warn


_patch_warn()
