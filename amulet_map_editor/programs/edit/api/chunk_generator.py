from typing import Optional
import time
from concurrent.futures import ThreadPoolExecutor, Future

from amulet_map_editor.api.opengl import ThreadedObjectContainer

ThreadingEnabled = True
if ThreadingEnabled:

    class ChunkGenerator(ThreadedObjectContainer, ThreadPoolExecutor):
        def __init__(self):
            ThreadedObjectContainer.__init__(self)
            ThreadPoolExecutor.__init__(self, max_workers=1)
            self._enabled = False
            self._generator: Optional[Future] = None

        def start(self):
            if not self._enabled:
                self._enabled = True
                self._generator = self.submit(self._generate_chunks)

        def stop(self):
            if self._enabled:
                self._enabled = False
                self._generator.result()

        def _generate_chunks(self):
            while self._enabled:
                start_time = time.time()
                while time.time() - start_time < 1 / 120:
                    self.thread_action()
                time.sleep(1 / 60)


else:

    class ChunkGenerator(ThreadedObjectContainer):
        def start(self):
            pass

        def stop(self):
            pass
