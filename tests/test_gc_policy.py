from amulet_map_editor.api.opengl.mesh.level.gc_policy import (
    select_regions_to_evict,
)


def test_no_eviction_under_budget():
    regions = [((0, 0), 100, 1), ((1, 0), 100, 2)]
    assert select_regions_to_evict(regions, budget_bytes=500, protected=set()) == []


def test_evicts_oldest_drawn_first():
    regions = [((0, 0), 100, 5), ((1, 0), 100, 1), ((2, 0), 100, 3)]
    evicted = select_regions_to_evict(regions, budget_bytes=200, protected=set())
    assert evicted == [(1, 0)]


def test_evicts_multiple_until_under_budget():
    regions = [((0, 0), 100, 5), ((1, 0), 100, 1), ((2, 0), 100, 3)]
    evicted = select_regions_to_evict(regions, budget_bytes=100, protected=set())
    assert evicted == [(1, 0), (2, 0)]


def test_protected_regions_never_evicted():
    regions = [((0, 0), 100, 1), ((1, 0), 100, 2)]
    evicted = select_regions_to_evict(
        regions, budget_bytes=50, protected={(0, 0), (1, 0)}
    )
    assert evicted == []
