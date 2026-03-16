from PyInstaller.utils.hooks import collect_data_files, collect_submodules

hiddenimports = [
    *collect_submodules("amulet_map_editor"),
    *collect_submodules("PIL"),
    *collect_submodules("pkg_resources"),
    *collect_submodules("minecraft_model_reader"),
    *collect_submodules("wx"),
    *collect_submodules("OpenGL"),
    *collect_submodules("OpenGL.GL"),
    *collect_submodules("OpenGL.GL.shaders"),
]

datas = collect_data_files(
    "amulet_map_editor",
    includes=[
        "**/*.png",
        "**/*.json",
        "**/*.frag",
        "**/*.vert",
        "**/*.lang",
        "**/*.mcmeta",
    ],
)
