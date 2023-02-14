from OpenGL.GL import (
    glClearColor,
    glBindVertexArray,
    glGenVertexArrays,
    GL_VERTEX_SHADER,
    GL_FRAGMENT_SHADER,
    glGetString,
    GL_SHADING_LANGUAGE_VERSION,
    GL_VERSION,
)
import OpenGL.GL.shaders
import os
from typing import Dict, Tuple, Any
import re

shader_dir = os.path.join(os.path.dirname(__file__))
_shaders: Dict[Tuple[str, str], Any] = {}

GL_VERSION_MATCH = re.compile(r"^(?P<major>\d+)\.(?P<minor>\d+)?")


def get_shader(
    context_identifier: str, shader_name: str
) -> OpenGL.GL.shaders.ShaderProgram:
    """
    Get the specified shader program.
    This must be called from the same thread that initialised the context
    :param context_identifier: The identifier for the context
    :param shader_name: The name of the shader to load
    :return: The shader program
    """
    shader_key = (context_identifier, shader_name)
    if shader_key not in _shaders:
        gl_version_match = GL_VERSION_MATCH.match(
            glGetString(GL_SHADING_LANGUAGE_VERSION).decode("utf-8")
        )
        if gl_version_match:
            gl_version_tuple = tuple(int(v) for v in gl_version_match.groups())
            if gl_version_tuple >= (3, 30):
                gl_version = "330"  # opengl 3.3
            else:
                gl_version = "120"  # opengl 2.1
        else:
            # in theory this shouldn't happen if the version is correctly formatted.
            gl_version = "330"

        def compile_shader():
            return OpenGL.GL.shaders.compileProgram(
                _load_shader(
                    os.path.join(shader_dir, f"{shader_name}_{gl_version}.vert"),
                    GL_VERTEX_SHADER,
                ),
                _load_shader(
                    os.path.join(shader_dir, f"{shader_name}_{gl_version}.frag"),
                    GL_FRAGMENT_SHADER,
                ),
            )

        try:
            shader = compile_shader()
        except (
            OpenGL.GL.shaders.ShaderValidationError
        ):  # on Mac the above fails if there is no VBO bound
            glBindVertexArray(glGenVertexArrays(1))
            shader = compile_shader()
            glBindVertexArray(0)

        _shaders[shader_key] = shader
    return _shaders[shader_key]


def _load_shader(shader_path, shader_type):
    with open(shader_path, "rb") as f:
        shader = f.read()
    return OpenGL.GL.shaders.compileShader(shader, shader_type)
