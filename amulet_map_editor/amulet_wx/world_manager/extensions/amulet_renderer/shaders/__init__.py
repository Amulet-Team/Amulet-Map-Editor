from OpenGL.GL import *
import OpenGL.GL.shaders
import os

shader_dir = os.path.join(os.path.dirname(__file__))
_shaders = {}


def get_shader(shader_name) -> OpenGL.GL.shaders.ShaderProgram:
    if shader_name not in _shaders:
        _shaders[shader_name] = OpenGL.GL.shaders.compileProgram(*[
            _load_shader(os.path.join(shader_dir, shader_file), shader_type) for shader_file, shader_type in [
                [f'{shader_name}.vert', GL_VERTEX_SHADER],
                [f'{shader_name}.frag', GL_FRAGMENT_SHADER]
            ]
        ])
    return _shaders[shader_name]


def _load_shader(shader_path, shader_type):
    with open(shader_path, 'rb') as f:
        shader = f.read()
    return OpenGL.GL.shaders.compileShader(shader, shader_type)
