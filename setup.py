from typing import List
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import os
import glob
import shutil
import sys
import numpy

try:
    import versioneer
except ImportError:
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    import versioneer

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

ext = []
if next(glob.iglob("amulet_map_editor/**/*.pyx", recursive=True), None):
    # This throws an error if it does not match any files
    ext += cythonize(
        "amulet_map_editor/**/*.pyx",
        language_level=3,
        annotate=True,
    )
if next(glob.iglob("CyOpenGL/**/*.pyx", recursive=True), None):
    # This throws an error if it does not match any files
    ext += cythonize(
        "CyOpenGL/**/*.pyx",
        language_level=3,
        annotate=True,
    )

setup(
    install_requires=required_packages,
    packages=find_packages(),
    include_package_data=True,
    cmdclass=versioneer.get_cmdclass(),
    ext_modules=ext,
    include_dirs=[numpy.get_include()],
)
