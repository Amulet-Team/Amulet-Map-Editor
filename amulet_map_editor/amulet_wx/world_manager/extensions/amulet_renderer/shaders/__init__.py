from OpenGL.GL import *
import OpenGL.GL.shaders
import os
from typing import Dict, Tuple, Any

shader_dir = os.path.join(os.path.dirname(__file__))
_shaders: Dict[Tuple[str, str], Any] = {}


def get_shader(renderer_key: str, shader_name: str) -> OpenGL.GL.shaders.ShaderProgram:
    shader_key = (renderer_key, shader_name)
    if shader_key not in _shaders:
        _shaders[shader_key] = OpenGL.GL.shaders.compileProgram(
            _load_shader(os.path.join(shader_dir, f'{shader_name}.vert'), GL_VERTEX_SHADER),
            _load_shader(os.path.join(shader_dir, f'{shader_name}.frag'), GL_FRAGMENT_SHADER)
        )
    return _shaders[shader_key]


def _load_shader(shader_path, shader_type):
    with open(shader_path, 'rb') as f:
        shader = f.read()
    return OpenGL.GL.shaders.compileShader(shader, shader_type)
