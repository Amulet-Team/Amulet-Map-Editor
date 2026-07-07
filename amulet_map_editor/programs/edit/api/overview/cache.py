import hashlib
import itertools
import json
import logging
import os
import re
import shutil
import threading
import time
from typing import List, Optional, Set, Tuple

import numpy
from PIL import Image, UnidentifiedImageError

log = logging.getLogger(__name__)

CACHE_VERSION = 1
TILE_CHUNK_SPAN = 32  # chunks along each edge of a tile
TILE_PIXELS = TILE_CHUNK_SPAN * 16  # 512

ChunkCoords = Tuple[int, int]


def tile_of_chunk(cx: int, cz: int) -> Tuple[int, int]:
    """The tile coords containing a given chunk."""
    return cx // TILE_CHUNK_SPAN, cz // TILE_CHUNK_SPAN


class OverviewTileCache:
    """Persists overview tile images and their per-chunk completion state.

    Layout: CACHE_DIR/world_overview/<world hash>/<dimension>/tile.<tx>.<tz>.png
    plus a .json metadata sidecar per tile.
    """

    def __init__(self, level_path: str, dimension: str):
        world_key = hashlib.sha1(level_path.encode("utf-8")).hexdigest()[:16]
        dimension_key = re.sub(r"[^A-Za-z0-9_-]", "_", dimension)
        self._dir = os.path.join(
            os.environ["CACHE_DIR"], "world_overview", world_key, dimension_key
        )
        os.makedirs(self._dir, exist_ok=True)
        # Serialize saves within this process; unique tmp names + replace
        # retries defend against other processes and leftover files.
        self._save_lock = threading.Lock()
        self._tmp_counter = itertools.count()
        # Best-effort sweep of any tmp files left behind by a crash or a
        # concurrent writer that died mid-save.
        try:
            for name in os.listdir(self._dir):
                if name.endswith(".tmp"):
                    try:
                        os.remove(os.path.join(self._dir, name))
                    except OSError:
                        pass
        except OSError:
            pass

    def _tile_png_path(self, tx: int, tz: int) -> str:
        return os.path.join(self._dir, f"tile.{tx}.{tz}.png")

    def _tile_meta_path(self, tx: int, tz: int) -> str:
        return os.path.join(self._dir, f"tile.{tx}.{tz}.json")

    def save_tile(
        self, tx: int, tz: int, pixels: numpy.ndarray, complete: Set[ChunkCoords]
    ):
        # Write each file to a temp path and os.replace it into place — os.replace
        # is atomic per file, so a crash mid-write never leaves a torn file. The
        # PNG is replaced before the JSON: if we crash between the two replaces,
        # the cache ends up with the new pixels but the OLD metadata, whose
        # smaller/different complete-set just causes the affected chunks to be
        # rescanned on next load — self-healing. Doing it in the opposite order
        # could leave metadata claiming chunks are complete that the pixels
        # don't actually contain, which is not self-healing.
        png_path = self._tile_png_path(tx, tz)
        meta_path = self._tile_meta_path(tx, tz)
        # Two workers can complete chunks in the same tile at once and both call
        # save_tile for the same (tx, tz) concurrently. On Windows an open file
        # is exclusively locked, so a shared tmp path collides (Errno 13) and the
        # os.replace fails (WinError 32). Serialize saves and give each write a
        # unique tmp name so writers never contend over the same tmp file.
        with self._save_lock:
            try:
                tmp_png = f"{png_path}.{os.getpid()}-{next(self._tmp_counter)}.tmp"
                # PIL needs an explicit format when the path doesn't end in .png.
                Image.fromarray(pixels, "RGBA").save(tmp_png, format="PNG")
                self._replace_with_retry(tmp_png, png_path)
                tmp_meta = f"{meta_path}.{os.getpid()}-{next(self._tmp_counter)}.tmp"
                with open(tmp_meta, "w") as f:
                    json.dump(
                        {
                            "version": CACHE_VERSION,
                            # int() coerces numpy integer types (e.g. numpy.int64)
                            # that may sneak in from scanner code — json.dump
                            # can't serialize those.
                            "complete": sorted([int(x), int(z)] for x, z in complete),
                        },
                        f,
                    )
                self._replace_with_retry(tmp_meta, meta_path)
            except OSError:
                log.warning(f"Failed to save overview tile ({tx}, {tz})", exc_info=True)

    @staticmethod
    def _replace_with_retry(tmp: str, dst: str, attempts: int = 3, delay: float = 0.05):
        """os.replace with a short retry loop.

        A reader (or, cross-process, another writer) can briefly hold the
        destination open on Windows, making os.replace raise PermissionError
        (Errno 13 / WinError 32). Retry a few times; on final failure remove the
        orphan tmp file and re-raise so the caller's OSError handler logs once.
        """
        for attempt in range(attempts):
            try:
                os.replace(tmp, dst)
                return
            except PermissionError:
                if attempt + 1 >= attempts:
                    try:
                        os.remove(tmp)
                    except OSError:
                        pass
                    raise
                time.sleep(delay)

    def load_tile(
        self, tx: int, tz: int
    ) -> Optional[Tuple[numpy.ndarray, Set[ChunkCoords]]]:
        try:
            with open(self._tile_meta_path(tx, tz)) as f:
                meta = json.load(f)
            if meta.get("version") != CACHE_VERSION:
                return None
            # Context manager so the PNG handle is closed deterministically —
            # a lingering read handle can make a concurrent replace fail.
            with Image.open(self._tile_png_path(tx, tz)) as img:
                pixels = numpy.array(img, numpy.uint8)
            if pixels.shape != (TILE_PIXELS, TILE_PIXELS, 4):
                return None
            complete = {tuple(c) for c in meta["complete"]}
            return pixels, complete
        except FileNotFoundError:
            return None  # cold cache — expected
        except (OSError, ValueError, KeyError, TypeError, UnidentifiedImageError):
            log.warning(
                f"Discarding unreadable overview tile ({tx}, {tz})", exc_info=True
            )
            return None

    def list_tiles(self) -> List[Tuple[int, int]]:
        tiles = []
        try:
            names = os.listdir(self._dir)
        except OSError:
            return tiles
        for name in names:
            match = re.fullmatch(r"tile\.(-?\d+)\.(-?\d+)\.png", name)
            if match:
                tiles.append((int(match.group(1)), int(match.group(2))))
        return tiles

    def clear(self):
        shutil.rmtree(self._dir, ignore_errors=True)
        os.makedirs(self._dir, exist_ok=True)
