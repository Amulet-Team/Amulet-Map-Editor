from .java_block_palette import apply_java_26_3_block_palette_compat
from .java_chunk_status import apply_java_26_3_chunk_status_compat
from .java_sign_text import apply_java_sign_json_compat


def apply_java_26_3_compat() -> None:
    apply_java_26_3_block_palette_compat()
    apply_java_26_3_chunk_status_compat()
    apply_java_sign_json_compat()


__all__ = [
    "apply_java_26_3_compat",
    "apply_java_26_3_block_palette_compat",
    "apply_java_26_3_chunk_status_compat",
    "apply_java_sign_json_compat",
]
