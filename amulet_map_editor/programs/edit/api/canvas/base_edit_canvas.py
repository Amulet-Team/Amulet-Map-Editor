import wx
import traceback
from OpenGL.GL import (
    glClearColor,
    glViewport,
)
import os
from typing import Optional, Generator
import weakref

from minecraft_model_reader.api.resource_pack.java.download_resources import (
    get_java_vanilla_latest_iter,
    get_java_vanilla_fix,
)
from minecraft_model_reader.api.resource_pack.java import (
    JavaResourcePack,
)
from minecraft_model_reader.api.resource_pack.bedrock.download_resources import (
    get_bedrock_vanilla_latest_iter,
    get_bedrock_vanilla_fix,
)
from minecraft_model_reader.api.resource_pack.bedrock import BedrockResourcePack
from minecraft_model_reader.api.resource_pack import (
    load_resource_pack,
    load_resource_pack_manager,
)

from amulet.api.data_types import OperationYieldType, Dimension

from amulet_map_editor import experimental_bedrock_resources
from amulet_map_editor.api.opengl.canvas import EventCanvas
from amulet_map_editor.api.opengl.resource_pack.resource_pack import OpenGLResourcePack
from amulet_map_editor.programs.edit.api.selection import (
    SelectionManager,
    SelectionHistoryManager,
)
import amulet_map_editor.programs.edit as amulet_edit

from amulet_map_editor.api.opengl.camera import ControllableCamera
from amulet_map_editor.api.wx.util.button_input import ButtonInput
from amulet_map_editor.api.wx.util.mouse_movement import MouseMovement
from ..renderer import Renderer

from amulet.api.level import BaseLevel


class BaseEditCanvas(EventCanvas):
    """Adds base logic for drawing everything related to the edit program to the canvas.
    All the user interaction code is implemented in ControllableEditCanvas to make them easier to read."""

    background_colour = (0.61, 0.70, 0.85)

    def __init__(self, parent: wx.Window, world: BaseLevel):
        super().__init__(parent)
        glClearColor(*self.background_colour, 1.0)
        self.Hide()

        self._world = weakref.ref(world)

        self._selection: Optional[SelectionHistoryManager] = SelectionHistoryManager(
            SelectionManager(self)
        )
        self.world.history_manager.register(self._selection, False)

        self._camera: ControllableCamera = ControllableCamera(self)
        self._camera.location_rotation = (0.0, 100.0, 0.0), (45.0, 45.0)
        self._camera.move_speed = 2.0
        self._camera.rotate_speed = 2.0

        self._buttons: ButtonInput = ButtonInput(self)
        self._mouse: MouseMovement = MouseMovement(self)
        self._mouse.set_middle()

        # load the resource packs
        os.makedirs("resource_packs", exist_ok=True)
        if not os.path.isfile("resource_packs/readme.txt"):
            with open("resource_packs/readme.txt", "w") as f:
                f.write("Put the Java resource pack you want loaded in here.")

        self._renderer: Optional[Renderer] = None

    def __setattr__(self, name, value):
        if not self.__dict__.get("_init", False) or hasattr(self, name):
            super().__setattr__(name, value)
        else:
            print(name, value)
            traceback.print_stack()

    def setup(self) -> Generator[OperationYieldType, None, None]:
        """Set up objects that take a while to set up.
        If you want to extend setup subclass the _setup method not this method."""
        yield from self._setup()
        self._finalise()

    def _setup(self) -> Generator[OperationYieldType, None, None]:
        """Set up objects that take a while to set up."""
        user_packs = [
            load_resource_pack(os.path.join("resource_packs", rp))
            for rp in os.listdir("resource_packs")
            if os.path.isdir(os.path.join("resource_packs", rp))
        ]
        if (
            self.world.level_wrapper.platform == "bedrock"
            and experimental_bedrock_resources
        ):
            yield 0.1, "Downloading Bedrock vanilla resource pack"
            gen = get_bedrock_vanilla_latest_iter()
            try:
                while True:
                    yield next(gen) * 0.4 + 0.1
            except StopIteration as e:
                latest_pack = e.value
            yield 0.5, "Loading resource packs"
            fix_pack = get_bedrock_vanilla_fix()
            amulet_pack = load_resource_pack(
                os.path.join(
                    os.path.dirname(amulet_edit.__file__),
                    "amulet_resource_pack",
                    "bedrock",
                )
            )

            user_packs = [
                pack for pack in user_packs if isinstance(pack, BedrockResourcePack)
            ]

            translator = self.world.translation_manager.get_version(
                "bedrock", (999, 0, 0)
            )
        else:
            yield 0.1, "Downloading Java vanilla resource pack"
            gen = get_java_vanilla_latest_iter()
            try:
                while True:
                    yield next(gen) * 0.4 + 0.1
            except StopIteration as e:
                latest_pack = e.value
            yield 0.5, "Loading resource packs"
            fix_pack = get_java_vanilla_fix()
            amulet_pack = load_resource_pack(
                os.path.join(
                    os.path.dirname(amulet_edit.__file__),
                    "amulet_resource_pack",
                    "java",
                )
            )

            user_packs = [
                pack for pack in user_packs if isinstance(pack, JavaResourcePack)
            ]

            translator = self.world.translation_manager.get_version("java", (999, 0, 0))

        resource_pack = load_resource_pack_manager(
            (amulet_pack, latest_pack, *user_packs, fix_pack), load=False
        )
        for i in resource_pack.reload():
            yield i / 4 + 0.5

        opengl_resource_pack = OpenGLResourcePack(resource_pack, translator)

        yield 0.75, "Creating texture atlas"
        for i in opengl_resource_pack.setup():
            yield i / 4 + 0.75

        yield 1.0, "Setting up renderer"

        self._renderer: Optional[Renderer] = Renderer(
            self,
            self.world,
            self.context_identifier,
            opengl_resource_pack,
        )

    def _finalise(self):
        """Any logic that needs to be run after everything has been set up."""
        self.reset_bound_events()
        self._init = True

    def bind_events(self):
        """Set up all events required to run.
        Note this will also bind subclass events."""
        self.Bind(wx.EVT_SIZE, self._on_size)
        self.selection.bind_events()
        self.buttons.bind_events()
        self.mouse.bind_events()
        self.renderer.bind_events()

    def enable(self):
        """Enable the canvas and start it working."""
        self.SetCurrent(self._context)
        self.renderer.enable()
        self.buttons.enable()

    def disable(self):
        """Disable the canvas and unload all geometry."""
        self.renderer.disable()
        self.buttons.disable()

    def is_closeable(self):
        """Check that the canvas and contained data is safe to be closed."""
        return self.renderer.is_closeable()

    def close(self):
        """Close and destroy the canvas and all contained data."""
        self.renderer.close()
        super()._close()

    @property
    def world(self) -> BaseLevel:
        """The amulet-core `BaseLevel` subclass representing the "world" that is open."""
        return self._world()

    @property
    def renderer(self) -> Renderer:
        """The `Renderer` class that handles the drawable objects and draws them."""
        return self._renderer

    @property
    def dimension(self) -> Dimension:
        """The currently loaded dimension in the renderer."""
        return self.renderer.dimension

    @dimension.setter
    def dimension(self, dimension: Dimension):
        """Set the currently loaded dimension in the renderer."""
        self.renderer.dimension = dimension

    @property
    def camera(self) -> ControllableCamera:
        """A class holding the state of the camera with methods to access and modify the state."""
        return self._camera

    @property
    def buttons(self) -> ButtonInput:
        """A class that manages converting button presses into actions based on set keybinds."""
        return self._buttons

    @property
    def mouse(self) -> MouseMovement:
        """A class that manages mouse movement."""
        return self._mouse

    @property
    def selection(self) -> SelectionManager:
        """A simple class for storing the selection state."""
        return self._selection.value

    def _on_size(self, evt):
        wx.CallAfter(self._set_size)
        evt.Skip()

    def _set_size(self):
        size = self.GetClientSize() * self.GetContentScaleFactor()
        width = size.width
        height = size.height
        self.SetCurrent(self._context)
        glViewport(0, 0, width, height)
        if height > 0:
            self.camera.aspect_ratio = width / height
        else:
            self.camera.aspect_ratio = 1
