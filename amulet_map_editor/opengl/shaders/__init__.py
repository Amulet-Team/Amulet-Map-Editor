from OpenGL.GL import *
import OpenGL.GL.shaders
import os
from typing import Dict, Tuple, Any

shader_dir = os.path.join(os.path.dirname(__file__))
_shaders: Dict[Tuple[str, str], Any] = {}


def get_shader(
    context_identifier: str, shader_name: str
) -> OpenGL.GL.shaders.ShaderProgram:
    shader_key = (context_identifier, shader_name)
    if shader_key not in _shaders:

        def compile_shader():
            return OpenGL.GL.shaders.compileProgram(
                _load_shader(
                    os.path.join(shader_dir, f"{shader_name}.vert"), GL_VERTEX_SHADER
                ),
                _load_shader(
                    os.path.join(shader_dir, f"{shader_name}.frag"), GL_FRAGMENT_SHADER
                ),
            )

        try:
            shader = compile_shader()
        except OpenGL.GL.shaders.ShaderValidationError:  # on Mac the above fails if there is no VBO bound
            glBindVertexArray(glGenVertexArrays(1))
            shader = compile_shader()
            glBindVertexArray(0)

        _shaders[shader_key] = shader
    return _shaders[shader_key]


def _load_shader(shader_path, shader_type):
    with open(shader_path, "rb") as f:
        shader = f.read()
    return OpenGL.GL.shaders.compileShader(shader, shader_type)
