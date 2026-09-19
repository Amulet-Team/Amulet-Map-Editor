"""Java 26.3+ chunk Status names that amulet-core 1.9 does not know."""

from __future__ import annotations

_APPLIED = False

# 26.3 worlds persist this Status. Amulet previously logged it on every chunk
# and defaulted to fully generated; keep that value, just stop the spam.
_JAVA_20_FULL_ALIASES = {
    "minecraft:terrain": 2.0,
}


def apply_java_26_3_chunk_status_compat() -> None:
    global _APPLIED
    if _APPLIED:
        return

    from amulet.api.chunk import status as status_mod

    for name, value in _JAVA_20_FULL_ALIASES.items():
        status_mod.states.setdefault(name, [[status_mod.J20], value])

    _APPLIED = True
