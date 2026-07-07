from amulet_map_editor.api.util.system_memory import total_system_memory


def test_returns_plausible_total():
    total = total_system_memory()
    assert isinstance(total, int)
    assert total >= 2**30  # at least 1 GiB on any dev machine
