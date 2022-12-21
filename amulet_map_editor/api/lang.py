"""
This module manages language support for Amulet.
The language files are in amulet_map_editor/lang with RFC 1766 file names and the .lang extension.
Lines starting with a hash (#) are ignored as comments and blank lines are ignored.
All other lines should have the format `key=value` where `key` is the language key used in the application and `value` is the localised string.
Keys should match the regex [a-z.]+ (lower case a-z and the full stop character) and values can contain any unicode character.
Files must be utf-8 encoded.
"""
import glob
from typing import Dict, Optional, List, Tuple
import os
import locale
import logging
import re

import amulet_map_editor
from amulet_map_editor.api import config as CONFIG

log = logging.getLogger(__name__)

# there might be a proper way to do this but this should be enough for now

_lang_dirs: List[str] = []  # the language directories
_lang: Dict[
    str, str
] = {}  # a storage for the language strings. unique_identifier: language_string

_default_language = "en"
_active_language: Optional[str] = None


def lang_dirs() -> Tuple[str, ...]:
    """Tuple of known language directories."""
    return tuple(_lang_dirs)


def parse_language_id(language_id: str) -> Optional[Tuple[str, str]]:
    """
    Parse an RFC 1766 language id string into a nicer format.

    :param language_id: The RFC 1766 code to parse
    :return: A tuple of the language and region codes (both lower case). The region code may be None.
    """
    match = re.fullmatch(
        r"(?P<language>[a-z]+)([-_](?P<region>[a-z]+))?.*",
        language_id,
        flags=re.IGNORECASE,
    )
    if match is None:
        return None
    region = match.group("region")
    region = "" if region is None else region.lower()
    return match.group("language").lower(), region


def set_language(language_id: str):
    """
    Sets and loads the specified language.
    A restart may be required.

    :param language_id: The RFC 1766 language code to use
    """
    global _active_language
    _active_language = language_id
    cfg = CONFIG.get("amulet_meta", {})
    cfg["lang"] = language_id
    CONFIG.put("amulet_meta", cfg)
    _load_language()


def get_language() -> str:
    """Get the currently active language string."""
    global _active_language
    if _active_language is None:
        # find out what language the user is using.
        try:
            # try getting the OS language
            _active_language = locale.getdefaultlocale()[0]
        except:
            # if that fails use the default language
            _active_language = _default_language

        # if a language is set in the config use that
        _active_language = CONFIG.get("amulet_meta", {}).get("lang", _active_language)

        if _active_language is None:
            _active_language = _default_language
    return _active_language


def get_languages() -> List[str]:
    """Get a list of all supported language codes."""
    langs = set()
    for d in _lang_dirs:
        for l in glob.glob(os.path.join(glob.escape(d), "*.lang")):
            langs.add(os.path.basename(l)[:-5])
    return sorted(langs)


def _load_lang_file(lang_path: str) -> Dict[str, str]:
    """Loads a language file and returns the result as a dictionary.
    Will return an empty dictionary if the path does not exist.

    :param lang_path: The lang file path to load.
    :return: A dictionary mapping the string identifier to the string
    """
    lang = {}
    if not os.path.isfile(lang_path):
        return lang
    with open(lang_path, encoding="utf-8") as f:
        for line in f.readlines():
            lstrip_line = line.lstrip()
            if lstrip_line.startswith("#") or not lstrip_line:
                continue
            split_line = lstrip_line.split("=", 1)
            if len(split_line) == 2:
                unique_identifier = split_line[0].rstrip()
                language_string = split_line[1].replace("\\n", "\n").strip()
                lang[unique_identifier] = language_string
    return lang


def _find_langs(path: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """Find the default, language specific and region specific lang paths."""
    langs = {
        parse_language_id(os.path.basename(lpath)[:-5]): lpath
        for lpath in glob.glob(os.path.join(glob.escape(path), "*.lang"))
    }

    default_key = parse_language_id(_default_language)
    active_key = parse_language_id(get_language())

    default_path = langs.get(default_key, None)
    language_path = None
    region_path = None

    if active_key is not None:
        if active_key[0] != default_key[0]:
            language_path = langs.get((active_key[0], ""), None)
        if active_key[1]:
            region_path = langs.get(active_key, None)

    return default_path, language_path, region_path


def _load_language():
    """Load the translations for the active language."""
    # work out which lang files to load based on the active language
    # lang files from the default langauge
    lang_files = sum(zip(*list(map(_find_langs, lang_dirs()))), ())

    _lang.clear()
    for lang_file in lang_files:
        if lang_file is None:
            continue
        _lang.update(_load_lang_file(lang_file))


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
            _lang_dirs.append(lang_dir)
            _load_language()


# load the normal language directory
register_lang_directory(
    os.path.join(os.path.dirname(amulet_map_editor.__file__), "lang")
)


def get(unique_identifier: str):
    """
    Get the localised string for the translation key

    :param unique_identifier: The translation key to get.
    :return: The translated string.
    """
    if unique_identifier not in _lang:
        # help debugging referenced lang entries that do not exist
        log.info(f"Could not find lang entry for {unique_identifier}")
    return _lang.get(unique_identifier, unique_identifier)
