from typing import List
from setuptools import setup, find_packages, Extension
import os
import glob
import shutil
import versioneer

try:
    from Cython.Build import cythonize
except (ImportError, ModuleNotFoundError):
    print("Could not find cython. The cython version will not be built.")
    cythonize = None


class get_numpy_include:
    def __str__(self):
        import numpy

        return numpy.get_include()


# there were issues with other builds carrying over their cache
for d in glob.glob("*.egg-info"):
    shutil.rmtree(d)


def load_requirements(path: str) -> List[str]:
    requirements = []
    with open(path) as f:
        for line in f.readlines():
            line = line.strip()
            if line.startswith("git+") or line.startswith("https:"):
                continue
            elif line.startswith("-r "):
                requirements += load_requirements(line[3:])
            else:
                requirements.append(line)
    return requirements


required_packages = load_requirements("./requirements.txt")

try:
    # try and freeze the requirements if already installed
    from pip._internal.operations import freeze

    first_party = {
        "amulet-core",
        "amulet-nbt",
        "pymctranslate",
        "minecraft-resource-pack",
    }
    installed = {r.split("==")[0].lower(): r for r in freeze.freeze() if "==" in r}
    for index, r in enumerate(required_packages):
        if r[0] != "#" and "~=" in r:
            req = r.split("~=")[0]
            if req in first_party and req in installed:
                required_packages[index] = installed[req]
except:
    pass

package_data = [
    os.path.relpath(path, "amulet_map_editor")
    for path in set(
        glob.glob(os.path.join("amulet_map_editor", "**", "*.*"), recursive=True)
    )
    - set(
        glob.glob(os.path.join("amulet_map_editor", "**", "*.py[cod]"), recursive=True)
    )
]

if cythonize:
    extensions = [
        Extension(
            name="amulet_map_editor.api.opengl.mesh.level.chunk.chunk_builder_cy", sources=["amulet_map_editor/api/opengl/mesh/level/chunk/chunk_builder_cy.pyx"]
        )
    ]
    ext_modules = cythonize(extensions, language_level=3, annotate=True)
else:
    ext_modules = []

setup(
    name="amulet-map-editor",
    version=versioneer.get_version(),
    description="A new Minecraft world editor and converter that supports all versions since Java 1.12 and Bedrock 1.7.",
    author="James Clare, Ben Gothard et al.",
    author_email="amuleteditor@gmail.com",
    install_requires=required_packages,
    packages=find_packages(),
    package_data={"amulet_map_editor": package_data},
    ext_modules=ext_modules,
    include_dirs=[get_numpy_include()],
    cmdclass=versioneer.get_cmdclass(),
    setup_requires=required_packages,
    dependency_links=[
        "https://github.com/Amulet-Team/Amulet-Core",
        "https://github.com/gentlegiantJGC/Minecraft-Model-Reader",
        "https://github.com/gentlegiantJGC/PyMCTranslate",
        "https://github.com/Amulet-Team/Amulet-NBT",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
