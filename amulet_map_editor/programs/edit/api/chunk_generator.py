import time
from typing import Optional
from threading import Thread

from amulet_map_editor.api.opengl import ThreadedObjectContainer

ThreadingEnabled = True
if ThreadingEnabled:

    class ChunkGenerator(ThreadedObjectContainer):
        def __init__(self):
            ThreadedObjectContainer.__init__(self)
            self._enabled = False
            self._thread: Optional[Thread] = None

        def start(self):
            if not self._enabled:
                if self._thread is not None:
                    raise Exception("Thread being disabled")
                self._enabled = True
                self._thread = Thread(target=self._generate_chunks)
                self._thread.start()

        def stop(self):
            if self._enabled:
                self._enabled = False
                self._thread.join()
                self._thread = None

        def _generate_chunks(self):
            while self._enabled:
                self.thread_action()
                # we need to force the chunk generator to share with the UI code otherwise it eats up all processing time.
                # TODO: find a better way to do this
                time.sleep(0.01)

else:

    class ChunkGenerator(ThreadedObjectContainer):
        def start(self):
            pass

        def stop(self):
            pass
