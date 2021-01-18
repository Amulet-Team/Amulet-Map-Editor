import os
import locale
from amulet_map_editor.api import config

# there might be a proper way to do this but this should be enough for now

_lang = {}
lang_dir = os.path.dirname(__file__)
default_lang = "en_US"


def _load_langauge(lang: str):
    lang_path = os.path.join(lang_dir, lang + ".lang")
    if os.path.isfile(lang_path):
        with open(lang_path, "r", encoding = 'utf-8') as f:
            for line in f.readlines():
                line = line.split("=", 1)
                if len(line) != 2:
                    continue
                _lang[line[0].strip()] = line[1].replace("\\n", "\n").strip()


def load_language(lang: str):
    """Load the contents of a language file from lang over """
    _lang.clear()
    _load_langauge(default_lang)
    if lang != default_lang:
        _load_langauge(lang)


load_language(config.get("amulet_meta", {}).get("lang", locale.getdefaultlocale()[0]))


def get(key):
    return _lang.get(key, key)
