from typing import List
from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel
from Cython.Build import cythonize
import glob
import sys
import numpy
import subprocess
import versioneer


first_party = {
    "amulet-core",
    "amulet-nbt",
    "pymctranslate",
    "minecraft-resource-pack",
}


def freeze_requirements(packages: List[str]) -> List[str]:
    # Pip install the requirements to find the newest compatible versions
    # This makes sure that the source versions are using the same dependencies as the compiled version.
    # This also makes sure that the source version is using the newest version of the dependency.
    if any("~=" in r and r.split("~=", 1)[0].lower() in first_party for r in packages):
        print("pip-install")
        try:
            # make sure pip is up to date
            subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            # run pip install
            subprocess.run(
                [sys.executable, "-m", "pip", "install", *packages, "--upgrade"]
            )
            # run pip freeze
            installed = (
                subprocess.check_output(
                    [sys.executable, "-m", "pip", "freeze"], encoding="utf-8"
                )
                .strip()
                .split("\n")
            )
            requirements_map = {r.split("==")[0].lower(): r for r in installed}

            print(installed, requirements_map)
            for index, requirement in enumerate(packages):
                if "~=" in requirement:
                    lib = requirement.split("~=")[0].strip().lower()
                    if lib in first_party and lib in requirements_map:
                        packages[index] = requirements_map[lib]
            print(f"Modified packages to {packages}")
        except Exception as e:
            print("Failed to bake versions:", e)
    return packages


# build cython extensions
if next(glob.iglob("amulet_map_editor/**/*.pyx", recursive=True), None):
    # This throws an error if it does not match any files
    ext = cythonize("amulet_map_editor/**/*.pyx")
else:
    ext = ()


cmdclass = versioneer.get_cmdclass()


# There might be a better way of doing this
# The extra argument needs to be defined in the sdist
# so that it doesn't error. It doesn't actually use it.
class SDist(cmdclass["sdist"]):
    user_options = cmdclass["sdist"].user_options + [
        ("find-libs=", None, ""),
    ]

    def initialize_options(self):
        super().initialize_options()
        self.find_libs = None


class BDistWheel(bdist_wheel):
    user_options = bdist_wheel.user_options + [
        (
            "find-libs=",
            None,
            "Find and fix the newest version of first party libraries. Only used internally.",
        ),
    ]

    def initialize_options(self):
        super().initialize_options()
        self.find_libs = None

    def finalize_options(self):
        if self.find_libs:
            self.distribution.install_requires = freeze_requirements(
                list(self.distribution.install_requires)
            )
        super().finalize_options()


cmdclass["sdist"] = SDist
cmdclass["bdist_wheel"] = BDistWheel


setup(
    version=versioneer.get_version(),
    cmdclass=cmdclass,
    include_dirs=[numpy.get_include()],
    packages=find_packages(),
    ext_modules=ext,
)
