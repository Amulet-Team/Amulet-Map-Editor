import logging
import time
from threading import Lock, RLock
from typing import Dict, List, Optional, Set, Tuple

import numpy

from amulet.api.errors import ChunkDoesNotExist, ChunkLoadError

from amulet_map_editor.api.opengl.mesh.level.load_queue import ChunkLoadQueue
from amulet_map_editor.api.opengl.resource_pack.resource_pack import model_lock
from .bedrock_fast_scan import BedrockFastScan
from .cache import TILE_CHUNK_SPAN, TILE_PIXELS, OverviewTileCache, tile_of_chunk
from .scan import ERROR_COLOURS, shade, top_colours

log = logging.getLogger(__name__)

ChunkCoords = Tuple[int, int]

# effectively infinite: overview LOAD items must never be distance-dropped
_SCAN_DISTANCE = 2**30


class _Tile:
    __slots__ = ("pixels", "complete", "dirty", "unsaved", "last_saved")

    def __init__(self, pixels: Optional[numpy.ndarray] = None, complete=None):
        if pixels is None:
            pixels = numpy.zeros((TILE_PIXELS, TILE_PIXELS, 4), numpy.uint8)
        self.pixels = pixels
        self.complete: Set[ChunkCoords] = set(complete or ())
        self.dirty = False  # GL texture needs re-upload
        self.unsaved = False  # disk cache needs re-save
        self.last_saved = 0.0  # time.time() of the last eager save (debounce)


class OverviewScanner:
    """Sweeps every chunk of a dimension once, building map-style tile
    images, nearest the camera first. Results persist in a disk cache.

    scan_next() is thread safe and intended to be registered with the
    ChunkGenerator worker pool. Everything else locks internally.
    """

    def __init__(self, level, dimension: str, resource_pack):
        self._level = level
        self._resource_pack = resource_pack
        self._lock = RLock()
        self._palette_lock = Lock()
        self._palette_colours: List[numpy.ndarray] = []
        self._palette_array = numpy.zeros((0, 4), numpy.uint8)
        self._dimension: Optional[str] = None
        self._generation = 0
        self._queue = ChunkLoadQueue(_SCAN_DISTANCE)
        self._tiles: Dict[Tuple[int, int], _Tile] = {}
        self._total = 0
        self._scanned = 0
        self._pending_camera: Optional[Tuple[int, int]] = None
        self._fast_scan: Optional[BedrockFastScan] = None
        self._fast_scanned = 0
        self._slow_scanned = 0
        self._fast_fallbacks = 0
        self.set_dimension(dimension)

    # -- state management ------------------------------------------------

    def set_dimension(self, dimension: str):
        with self._lock:
            if dimension == self._dimension:
                return
            self._generation += 1
            if self._dimension is not None:
                self.flush()
            self._dimension = dimension
            self._queue.clear()
            self._tiles = {}
            self._cache = OverviewTileCache(str(self._level.level_path), dimension)
            for tx, tz in self._cache.list_tiles():
                loaded = self._cache.load_tile(tx, tz)
                if loaded is not None:
                    pixels, complete = loaded
                    tile = _Tile(pixels, complete)
                    self._tiles[(tx, tz)] = tile
            all_coords = set(self._level.all_chunk_coords(dimension))
            self._total = len(all_coords)
            self._scanned = 0
            for coords in all_coords:
                tile = self._tiles.get(tile_of_chunk(*coords))
                if tile is not None and coords in tile.complete:
                    self._scanned += 1
                else:
                    self._queue.push(coords, ChunkLoadQueue.PRIORITY_LOAD)
            self._fast_scan = BedrockFastScan.create(
                self._level, dimension, self._resource_pack
            )
            if self._fast_scan is not None:
                log.info(
                    f"Bedrock fast scan active for {dimension} "
                    f"(raw LevelDB reads, translation only per unique block)"
                )

    def rescan(self):
        with self._lock:
            self._generation += 1
            self._cache.clear()
            dimension = self._dimension
            self._dimension = None  # force set_dimension to run again
            self._tiles = {}
            self.set_dimension(dimension)

    def set_camera_chunk(self, cx: int, cz: int):
        # Deferred handoff: avoid rebuilding the priority heap over every
        # unscanned chunk synchronously on the UI thread. Attribute
        # assignment is atomic under the GIL, so no lock is needed here;
        # scan_next() applies it on a worker thread instead.
        self._pending_camera = (cx, cz)

    def mark_chunk_changed(self, coords: ChunkCoords):
        self._queue.push(coords, ChunkLoadQueue.PRIORITY_URGENT)

    def progress(self) -> float:
        with self._lock:
            if not self._total:
                return 1.0
            return min(1.0, self._scanned / self._total)

    # -- scanning ----------------------------------------------------------

    def _ensure_palette_colours(self, palette) -> numpy.ndarray:
        """Grow the palette-index -> RGBA lookup to cover the palette."""
        if len(self._palette_array) >= len(palette):
            return self._palette_array
        with self._palette_lock:
            while len(self._palette_colours) < len(palette):
                i = len(self._palette_colours)
                try:
                    with model_lock:
                        colour = self._resource_pack.get_block_top_colour(palette[i])
                except Exception:
                    colour = numpy.array((255, 0, 255, 255), numpy.uint8)
                self._palette_colours.append(numpy.asarray(colour, numpy.uint8))
            self._palette_array = numpy.array(self._palette_colours, numpy.uint8)
        return self._palette_array

    def scan_next(self) -> bool:
        """Scan one chunk. Returns True if a chunk was processed."""
        pending = self._pending_camera
        if pending is not None:
            # benign race: a camera update between the read and this clear is dropped until the next crossing
            self._pending_camera = None
            self._queue.set_camera_chunk(*pending)
        item = self._queue.pop()
        if item is None:
            return False
        (cx, cz), priority = item
        # snapshot dimension, generation and fast scanner atomically so a
        # concurrent set_dimension cannot pair a new scanner with a stale
        # dimension/generation (the generation guard in _write_patch is the
        # backstop, but the invariant should not depend on statement order)
        with self._lock:
            dimension = self._dimension
            generation = self._generation
            fast = self._fast_scan
        try:
            # URGENT = in-session edit; the db only holds saved state, so
            # edits must go through level.get_chunk (slow path).
            if fast is not None and priority == ChunkLoadQueue.PRIORITY_LOAD:
                result = fast.scan_chunk(cx, cz)
                if result is not None:
                    colours, heights = result
                    patch = shade(colours, heights)
                    # diagnostic counters; racy += is acceptable (logging only)
                    self._fast_scanned += 1
                else:
                    self._fast_fallbacks += 1
                    patch = self._slow_scan_patch(cx, cz, dimension)
            else:
                patch = self._slow_scan_patch(cx, cz, dimension)
        except Exception:
            log.warning(f"Overview scan failed for chunk ({cx}, {cz})", exc_info=True)
            patch = ERROR_COLOURS
        self._write_patch((cx, cz), patch, generation)
        return True

    def _slow_scan_patch(
        self, cx: int, cz: int, dimension: str
    ) -> Optional[numpy.ndarray]:
        """Compute a chunk's shaded colour patch via the universal-translation
        path (level.get_chunk). Returns None for a non-existent chunk
        (transparent) or ERROR_COLOURS if the chunk failed to load."""
        try:
            chunk = self._level.get_chunk(cx, cz, dimension)
        except ChunkDoesNotExist:
            return None  # transparent
        except ChunkLoadError:
            return ERROR_COLOURS
        blocks = chunk.blocks
        sub_chunks = {
            cy: numpy.asarray(blocks.get_sub_chunk(cy)) for cy in blocks.sub_chunks
        }
        palette_colours = self._ensure_palette_colours(chunk.block_palette)
        colours, heights = top_colours(sub_chunks, palette_colours)
        self._slow_scanned += 1
        return shade(colours, heights)

    def _write_patch(
        self, coords: ChunkCoords, patch: Optional[numpy.ndarray], generation: int
    ):
        """Write a chunk's 16x16 colour patch into its tile.

        :param patch: (16, 16, 4) uint8 indexed (x, z), or None for transparent.
        :param generation: the generation snapshot taken when the scan started;
            if the dimension/cache state has since been swapped, the patch is
            dropped rather than corrupting the new state.
        """
        tile_coords = tile_of_chunk(*coords)
        ox = (coords[0] % TILE_CHUNK_SPAN) * 16
        oz = (coords[1] % TILE_CHUNK_SPAN) * 16
        snapshot = None
        with self._lock:
            if generation != self._generation:
                return  # state was swapped while this chunk was being scanned
            tile = self._tiles.get(tile_coords)
            if tile is None:
                tile = self._tiles[tile_coords] = _Tile()
            target = tile.pixels[oz : oz + 16, ox : ox + 16]
            if patch is None:
                target[:] = 0
            else:
                # patch is (x, z, 4); tile pixels are (z_row, x_col, 4)
                target[:] = patch.transpose(1, 0, 2)
            if coords not in tile.complete:
                tile.complete.add(coords)
                self._scanned += 1
            tile.dirty = True
            tile.unsaved = True
            # Eager-save a complete tile, but debounce so a hot tile (re-saved
            # on every edit wave) hits disk at most once per 5s. When deferred
            # the tile stays unsaved=True, so a later wave or flush() saves it.
            now = time.time()
            if (
                len(tile.complete) >= self._tile_target_count(tile_coords)
                and now - tile.last_saved >= 5.0
            ):
                snapshot = (tile.pixels.copy(), set(tile.complete))
                tile.unsaved = False
                tile.last_saved = now
        # Disk I/O (PNG encode + write) happens outside the lock so it never
        # blocks take_dirty_tiles() on the main thread. The cache layer is
        # crash-safe via atomic replace, and concurrent saves of the same
        # tile are last-writer-wins and harmless.
        if snapshot is not None:
            self._cache.save_tile(tile_coords[0], tile_coords[1], *snapshot)

    def _tile_target_count(self, tile_coords) -> int:
        # tiles are saved when fully scanned; partially-populated edge
        # tiles are saved by flush() on close instead.
        return TILE_CHUNK_SPAN * TILE_CHUNK_SPAN

    def flush(self):
        """Save every unsaved tile. Call on close and dimension switch.

        Snapshots are taken under the lock and the actual disk I/O happens
        afterwards, outside the lock, so it never blocks the main thread.
        """
        with self._lock:
            snapshots = []
            for tile_coords, tile in self._tiles.items():
                if tile.unsaved:
                    snapshots.append(
                        (tile_coords, tile.pixels.copy(), set(tile.complete))
                    )
                    tile.unsaved = False
        for tile_coords, pixels, complete in snapshots:
            self._cache.save_tile(tile_coords[0], tile_coords[1], pixels, complete)

    # -- consumption by the GL layer (main thread) -------------------------

    def take_dirty_tiles(self) -> List[Tuple[int, int, numpy.ndarray]]:
        with self._lock:
            dirty = []
            for (tx, tz), tile in self._tiles.items():
                if tile.dirty:
                    tile.dirty = False
                    dirty.append((tx, tz, tile.pixels.copy()))
            return dirty

    def tile_pixels(self, tx: int, tz: int) -> Optional[numpy.ndarray]:
        with self._lock:
            tile = self._tiles.get((tx, tz))
            if tile is None:
                return None
            return tile.pixels.copy()

    def list_tiles(self) -> List[Tuple[int, int]]:
        with self._lock:
            return list(self._tiles)
