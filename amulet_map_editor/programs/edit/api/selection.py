from typing import Tuple, Optional, Any, TYPE_CHECKING
import wx
import numpy
import weakref
from amulet.api.selection import SelectionGroup, SelectionBox
from amulet.api.history.history_manager import ObjectHistoryManager
from amulet.api.history import Changeable

from amulet_map_editor import log

if TYPE_CHECKING:
    from amulet_map_editor.programs.edit.api.canvas import EditCanvas

BoxType = Tuple[Tuple[int, int, int], Tuple[int, int, int]]  # min and max positions


_SelectionChangeEventType = wx.NewEventType()
EVT_SELECTION_CHANGE = wx.PyEventBinder(_SelectionChangeEventType)


class SelectionChangeEvent(wx.PyEvent):
    """Run when the selection is changed by third party code."""

    def __init__(self):
        wx.PyEvent.__init__(self, eventType=_SelectionChangeEventType)


class SelectionManager(Changeable):
    """A class containing the raw representation of the selection with methods to access and change it."""

    def __init__(self, canvas: "EditCanvas"):
        super().__init__()
        self._selection_corners: Tuple[BoxType, ...] = ()
        self._selection_group: SelectionGroup = SelectionGroup()
        self._canvas = weakref.ref(canvas)

        self._timer = wx.Timer(canvas)

    @property
    def canvas(self) -> "EditCanvas":
        return self._canvas()

    def bind_events(self):
        """Set up all events required to run."""
        self.canvas.Bind(wx.EVT_TIMER, self._create_undo_point, self._timer)

    def _create_undo_point(self, evt):
        self.canvas.create_undo_point(False, True)
        evt.Skip()

    def _start_undo_point(self):
        """Start a timer to create an undo point after a period of time.
        If this is called again before the timer runs then the last call will not happen."""
        self._timer.StartOnce(400)

    @property
    def selection_corners(
        self,
    ) -> Tuple[Tuple[Tuple[int, int, int], Tuple[int, int, int]], ...]:
        """Get the minimum and maximum points of each selection
        :return: The minimum and maximum points of each selection
        """
        return self._selection_corners

    @selection_corners.setter
    def selection_corners(
        self,
        selection_corners: Tuple[
            Tuple[Tuple[int, int, int], Tuple[int, int, int]], ...
        ],
    ):
        """Set the minimum and maximum points of each selection
        Will create events that allow the program to update.

        :param selection_corners: The minimum and maximum points of each selection
        :return:
        """
        self.set_selection_corners(selection_corners)
        self._start_undo_point()

    def set_selection_corners(
        self,
        selection_corners: Tuple[
            Tuple[Tuple[int, int, int], Tuple[int, int, int]], ...
        ],
    ):
        """Set the minimum and maximum points of each selection
        Note this method will not trigger the history logic.
        You may instead want the selection_corners setter method.

        :param selection_corners: The minimum and maximum points of each selection
        :return:
        """
        selections = []
        for points in selection_corners:
            if (
                type(points) in (tuple, list)
                and len(points) == 2
                and all(
                    type(point) in (tuple, list)
                    and len(point) == 3
                    and all(isinstance(p, (int, numpy.integer)) for p in point)
                    for point in points
                )
            ):
                selections.append(
                    tuple(tuple(int(p) for p in point) for point in points)
                )
            else:
                log.error(
                    f"selection_corners must be of the format Tuple[Tuple[Tuple[int, int, int], Tuple[int, int, int]], ...]"
                )

        self.changed = True
        self._selection_corners = tuple(selections)
        self._selection_group = SelectionGroup(
            [SelectionBox(*box) for box in self._selection_corners]
        )
        wx.PostEvent(self._canvas(), SelectionChangeEvent())

    @property
    def selection_group(self) -> SelectionGroup:
        """Get the selection as a `SelectionGroup`
        :return: `SelectionGroup`
        """
        return self._selection_group

    @selection_group.setter
    def selection_group(self, selection_group: SelectionGroup):
        """Set the selection from a `SelectionGroup` class
        Will create events that allow the program to update.

        :param selection_group: The `SelectionGroup` to pull the data from
        :return:
        """
        self.set_selection_group(selection_group)
        self._start_undo_point()

    def set_selection_group(self, selection_group: SelectionGroup):
        """Set the selection from a `SelectionGroup` class
        Note this method will not trigger the history logic.
        You may instead want the selection_group setter method.

        :param selection_group: The `SelectionGroup` to pull the data from
        :return:
        """
        self.changed = True
        self._selection_corners = [
            (box.min, box.max) for box in selection_group.selection_boxes
        ]
        self._selection_group = selection_group
        wx.PostEvent(self._canvas(), SelectionChangeEvent())


class SelectionHistoryManager(ObjectHistoryManager):
    def __init__(self, selection_manager: SelectionManager):
        super().__init__(selection_manager)

    @property
    def value(self) -> SelectionManager:
        return self._value

    def _unpack_value(self, value: Optional[Any]):
        self.value.set_selection_corners(value)

    def _pack_value(self, value: SelectionManager) -> Optional[Any]:
        return value.selection_corners
