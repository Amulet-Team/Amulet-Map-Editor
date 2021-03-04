from typing import List


class ThreadedObject:
    """Data/Geometry generation controlled by an external thread."""

    def thread_action(self):
        """The action the thread will call."""
        raise NotImplementedError

    @property
    def thread_weighting(self) -> int:
        """The number of times the thread_action should be called."""
        return 1


class ThreadedObjectContainer(ThreadedObject):
    def __init__(self):
        self._objects: List[ThreadedObject] = []
        self._obj_index = 0
        self._obj_sub_index = 0

    def register(self, thread_object: ThreadedObject):
        assert isinstance(thread_object, ThreadedObject)
        if thread_object in self._objects:
            raise Exception("ThreadedObject object is already registered.")
        self._objects.append(thread_object)

    def unregister(self, thread_object: ThreadedObject):
        assert isinstance(thread_object, ThreadedObject)
        if thread_object not in self._objects:
            raise Exception("ThreadedObject object was not already registered.")
        self._objects.remove(thread_object)

    def thread_action(self):
        """The action the thread will call."""
        if self._obj_index >= len(self._objects):
            self._obj_index = 0
            self._obj_sub_index = 0
        while (
            self._obj_index < len(self._objects)
            and self._objects[self._obj_index].thread_weighting < self._obj_sub_index
        ):
            self._obj_index += 1
            self._obj_sub_index = 0

        if self._obj_index < len(self._objects):
            self._objects[self._obj_index].thread_action()
            self._obj_sub_index += 1

    @property
    def thread_weighting(self) -> int:
        """The number of times the thread_action should be called."""
        return sum(obj.thread_weighting for obj in self._objects)
