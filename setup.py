import codecs
import os
import re

from setuptools import setup, find_packages


###################################################################

NAME = "amulet-map-editor"
PACKAGES = find_packages()
META_PATH = os.path.join("amulet_map_editor", "__init__.py")
KEYWORDS = ["minecraft", "map editor"]
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: End Users/Desktop",
    "Natural Language :: English",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Microsoft :: Windows",
    "Operating System :: MacOS",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: POSIX :: Linux",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Games/Entertainment",
    "Private :: Do Not Upload",
]
PACKAGE_DATA={
    "": ["*.png", "*.mcmeta", "*.lang", "version"],
    "amulet_map_editor.opengl": ["*.frag", "*.vert"]
}
PYTHON_REQUIRES='~=3.7'
INSTALL_REQUIRES = []

###################################################################

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(HERE, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read(META_PATH)


def find_meta(meta):
    """
    Extract __*meta*__ from META_FILE.
    """
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta),
        META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


if __name__ == "__main__":
    setup(
        name=NAME,
        description=find_meta("description"),
        license=find_meta("license"),
        url=find_meta("url"),
        version=read(os.path.join("amulet_map_editor", "version")),
        author=find_meta("author"),
#        author_email=find_meta("email"),
        maintainer=find_meta("author"),
#        maintainer_email=find_meta("email"),
        keywords=KEYWORDS,
        long_description=read("README.md"),
        long_description_content_type="text/markdown",
        packages=PACKAGES,
        zip_safe=False,
        classifiers=CLASSIFIERS,
        include_package_data=True,
        package_data=PACKAGE_DATA,
        python_requires=PYTHON_REQUIRES,
        install_requires=INSTALL_REQUIRES,
        entry_points={
            "gui_scripts": [
                "amulet-map-editor = amulet_map_editor.load:run",
            ]
        }
    )
