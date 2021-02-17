from typing import Dict, Set
import os
import locale

import amulet_map_editor
from amulet_map_editor.api import config as CONFIG, log

# there might be a proper way to do this but this should be enough for now

_lang_dirs: Set[str] = set()  # the language directories
_lang: Dict[
    str, str
] = {}  # a storage for the language strings. unique_identifier: language_string

_default_language = "en_US"

# find out what language the user is using.
try:
    # try getting the OS language
    _language = locale.getdefaultlocale()[0]
except:
    # if that fails use the default language
    _language = _default_language

# if a language is set in the config use that
_language = CONFIG.get("amulet_meta", {}).get("lang", _language)


def register_lang_directory(lang_dir: str):
    """Register a new language directory.
    Use this, if you are a third party program, to register new translations for your program.

    :param lang_dir: The directory containing language files to register. Files must be of the format <language_code>.lang eg en_US.lang
    :return:
    """
    if os.path.isdir(lang_dir):
        if lang_dir in _lang_dirs:
            log.warning(
                f"The language directory {lang_dir} has already been registered."
            )
        else:
            _lang_dirs.add(lang_dir)
            default_lang_path = os.path.join(lang_dir, f"{_default_language}.lang")
            default_lang = _load_lang_file(default_lang_path)
            if _default_language != _language:
                # if the language set is not the default load the language
                lang_path = os.path.join(lang_dir, f"{_language}.lang")
                lang = _load_lang_file(lang_path)

                # sanity check to make sure that all entries in the user language are in the default
                diff = set(lang).difference(set(default_lang))
                if diff:
                    print(
                        f"There are {len(diff)} language entries defined in {lang_path} that are not defined in {default_lang_path}\n{diff}"
                    )

                # merge in the user language
                default_lang.update(lang)

            # merge the loaded language entries
            for unique_identifier, language_string in default_lang.items():
                if unique_identifier in _lang:
                    log.warning(
                        f"The language entry {unique_identifier} added in {lang_dir} is already used. Please add a unique prefix."
                    )
                else:
                    _lang[unique_identifier] = language_string


def _load_lang_file(lang_path: str) -> Dict[str, str]:
    """Loads a language file and returns the result as a dictionary.
    Will return an empty dictionary if the path does not exist.

    :param lang_path: The lang file path to load.
    :return: A dictionary mapping the string identifier to the string
    """
    lang = {}
    if os.path.isfile(lang_path):
        with open(lang_path, encoding="utf-8") as f:
            for line in f.readlines():
                split_line = line.split("=", 1)
                if len(split_line) == 2:
                    unique_identifier = split_line[0].strip()
                    language_string = split_line[1].replace("\\n", "\n").strip()
                    lang[unique_identifier] = language_string
    return lang


# load the normal language directory
register_lang_directory(
    os.path.join(os.path.dirname(amulet_map_editor.__file__), "lang")
)


def get(unique_identifier):
    if unique_identifier not in _lang:
        # help debugging referenced lang entries that do not exist
        log.info(f"Could not find lang entry for {unique_identifier}")
    return _lang.get(unique_identifier, unique_identifier)
