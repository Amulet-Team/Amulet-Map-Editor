"""Java sign text: empty / non-JSON lines must not crash PyMCTranslate.

Universal-to-Java 1.21.5+ sign functions call from_java_json() on each line.
Blank signs store "" which json.loads rejects (Expecting value: line 1 column 1).
"""

from __future__ import annotations

import json
import sys

_APPLIED = False


def apply_java_sign_json_compat() -> None:
    global _APPLIED
    if _APPLIED:
        return

    from PyMCTranslate.py3.util.raw_text import java_json as java_json_mod
    from PyMCTranslate.py3.util.raw_text.data import PlainTextComponent

    # Load sign translators so already-bound imports can be rewritten.
    try:
        import PyMCTranslate.py3.api.version.code_functions  # noqa: F401
    except Exception:
        pass

    original = java_json_mod.from_java_json

    def from_java_json(s: str):
        if not isinstance(s, str) or not s.strip():
            return PlainTextComponent(text="")
        try:
            return original(s)
        except (json.JSONDecodeError, ValueError, TypeError):
            return PlainTextComponent(text=s)

    java_json_mod.from_java_json = from_java_json
    for module in list(sys.modules.values()):
        if module is not None and getattr(module, "from_java_json", None) is original:
            module.from_java_json = from_java_json

    _APPLIED = True
