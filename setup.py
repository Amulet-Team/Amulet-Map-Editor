from typing import List, Tuple
from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel
from Cython.Build import cythonize
import glob
import sys
import numpy
import subprocess
import logging
import re
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


GCCPattern = re.compile(r"gcc version (?P<major>\d+)\.(?P<minor>\d+)")
ClangPattern = re.compile(r"clang(?:-|\s+version\s+)(?P<major>\d+)\.(?P<minor>\d+)")


def get_openmp_args() -> Tuple[List[str], List[str], List[str], List[str]]:
    # This has been lifted from here https://github.com/cython/cython/blob/606bd8cf235149c3be6876d0f5ae60032c8aab6c/runtests.py
    import sysconfig
    from distutils import ccompiler

    def get_openmp_args_for(arg) -> Tuple[List[str], List[str]]:
        """arg == 'CC' or 'CXX'"""
        cc = (
            sysconfig.get_config_var(arg) or ccompiler.get_default_compiler()
        ).split()[0]
        if cc == "msvc":
            # Microsoft Visual C
            return ["/openmp"], []
        elif cc:
            # Try GCC and Clang
            try:
                out = subprocess.check_output([cc, "-v"]).decode()
            except ChildProcessError:
                logging.exception(f"Could not resolve unknown compiler {cc}")
            else:
                gcc_match = GCCPattern.search(out)
                if gcc_match:
                    if (gcc_match.group("major"), gcc_match.group("minor")) >= (4, 2):
                        return ["-fopenmp"], ["-fopenmp"]
                    return [], []
                clang_match = ClangPattern.search(out)
                if clang_match:
                    # if (clang_match.group("major"), clang_match.group("minor")) >= (3, 7):
                    #     return ['-fopenmp'], ['-fopenmp']
                    return [], []
        # If all else fails disable openmp
        return [], []

    omp_ccargs, omp_clargs = get_openmp_args_for("CC")
    omp_cppcargs, omp_cpplargs = get_openmp_args_for("CXX")

    return omp_ccargs, omp_clargs, omp_cppcargs, omp_cpplargs


# build cython extensions
if next(glob.iglob("amulet_map_editor/**/*.pyx", recursive=True), None):
    # This throws an error if it does not match any files
    omp_ccargs, omp_clargs, omp_cppcargs, omp_cpplargs = get_openmp_args()
    ext = cythonize(
        "amulet_map_editor/**/*.pyx",
        aliases={
            "OPENMP_CCARGS": omp_ccargs,
            "OPENMP_CLARGS": omp_clargs,
            "OPENMP_CPPCARGS": omp_cppcargs,
            "OPENMP_CPPLARGS": omp_cpplargs,
        },
    )
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
