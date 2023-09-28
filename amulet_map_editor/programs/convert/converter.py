from threading import Thread

from amulet import load_format
from amulet import load_level
from amulet_map_editor import lang


class Converter:
    def __init__(self, world_path: str, out_world_path: str):
        self.world_path = world_path
        self.out_world_path = out_world_path

        self._thread = Thread(target=self._convert_method)
        self._thread.start()

    def _convert_method(self):
        try:
            world = load_level(self.world_path)
            out_world = load_format(self.out_world_path)
            out_world: WorldFormatWrapper
            out_world.open()
            world.save(out_world, None)
            out_world.close()
            print(lang.get("program_convert.conversion_completed"))
        except Exception as e:
            print("Error during conversion\n{e}")
