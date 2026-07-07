from typing import Iterable, List, Set, Tuple

RegionCoords = Tuple[int, int]


def select_regions_to_evict(
    regions: Iterable[Tuple[RegionCoords, int, int]],
    budget_bytes: int,
    protected: Set[RegionCoords],
) -> List[RegionCoords]:
    """Pick regions to unload so total geometry memory fits the budget.

    :param regions: (region coords, geometry bytes, last drawn counter)
    :param budget_bytes: the maximum total geometry bytes to keep.
    :param protected: regions that must never be evicted (in render distance).
    :return: region coords to evict, least recently drawn first.
    """
    regions = list(regions)
    total = sum(size for _, size, _ in regions)
    if total <= budget_bytes:
        return []
    evict = []
    candidates = sorted(
        (r for r in regions if r[0] not in protected), key=lambda r: r[2]
    )
    for coords, size, _ in candidates:
        if total <= budget_bytes:
            break
        evict.append(coords)
        total -= size
    return evict
