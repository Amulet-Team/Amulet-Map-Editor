from typing import List, Optional
from setuptools import setup, find_packages
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

# Find the newest compatible version for the first party libraries.
# This does not do any dependency resolution so the dependencies should already be compatible.
# This makes sure that the source versions are using the same dependencies as the compiled version.
# This also makes sure that the source version is using the newest version of the dependency.
try:
    # This used to use the internal pip freeze logic but with the new build system
    # the packages are not installed first so it no longer works.
    # Instead look on PyPi for the newest version.
    import json
    import urllib.request
    import re
    from packaging.requirements import Requirement
    from packaging.version import Version

    first_party = {
        "amulet-core",
        "amulet-nbt",
        "pymctranslate",
        "minecraft-resource-pack",
    }

    def get_compatible_version(requirement_str: str) -> Optional[str]:
        """
        Converts something like "amulet-core~=1.4.0" to "amulet-core==1.4.7"
        :param requirement_str: "amulet-core~=1.4.0"
        :return: "amulet-core==1.4.7"
        """
        try:
            requirement = Requirement(requirement_str)
            if requirement.name in first_party:
                release_versions = []
                pypi_json = json.load(
                    urllib.request.urlopen(
                        f"https://pypi.org/pypi/{requirement.name}/json"
                    )
                )
                for version, files in pypi_json["releases"].items():
                    # for each release
                    if any(not f["yanked"] for f in files):
                        # If the are files that have not been yanked
                        try:
                            release_versions.append(Version(version))
                        except:
                            continue
                release_versions.sort(reverse=True)
                for release_version in release_versions:
                    if release_version in requirement.specifier:
                        return f"{requirement.name}=={release_version}"
        except:
            pass
        return None

    def fix_requirements():
        for index, req in enumerate(required_packages):
            fixed_req = get_compatible_version(req)
            if fixed_req is not None:
                required_packages[index] = fixed_req

    fix_requirements()
except Exception as e:
    print("Failed to bake versions:", e)

if next(glob.iglob("amulet_map_editor/**/*.pyx", recursive=True), None):
    # This throws an error if it does not match any files
    ext = cythonize("amulet_map_editor/**/*.pyx")
else:
    ext = ()


setup(
    install_requires=required_packages,
    packages=find_packages(),
    include_package_data=True,
    cmdclass=versioneer.get_cmdclass(),
    ext_modules=ext,
    include_dirs=[numpy.get_include()],
)
