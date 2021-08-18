# This is based upon https://github.com/branpk/opengl-cython/blob/master/gen_opengl_pxd.py
from typing import Optional, Iterable, Dict, List, Tuple, Callable
from xml.etree.ElementTree import Element, parse as xml_parse
import urllib.request
from dataclasses import dataclass
import os
import re

HEADER = """# cython: language_level=3, boundscheck=False, wraparound=False

from CyOpenGL.GL.load_function cimport getFunction
"""


@dataclass
class TypeEntry:
    name: str
    dtype: str

    def write(self, f):
        f.write(f"{self.dtype}\n")


dtype_map = {
    "khronos_intptr_t ": "int *",
    "khronos_ssize_t": "int",
    "khronos_float_t": "float",
    "khronos_int8_t": "int",
    "khronos_uint8_t": "int",
    "khronos_int16_t": "int",
    "khronos_uint16_t": "int",
    "khronos_int32_t": "int",
    "khronos_uint32_t": "int",
    "khronos_int64_t": "int",
    "khronos_uint64_t": "int",
    # "uint64_t": "int",
    # "int64_t": "int",
    # "struct __GLsync *": "int *",
    # "(void)": "()"
}


class TypeManager:
    def __init__(self, dtypes: List[Element]):
        self._dtypes: Dict[str, TypeEntry] = {}
        for dtypes_ in dtypes:
            self._add_types(dtypes_)

    def _add_types(self, types: Element):
        for dtype in types.findall("type"):
            dtype: Element
            name_element = dtype.find("name")
            if name_element is None:
                name = dtype.get("name")
                if name == "khrplatform":
                    continue
                elif name == "GLhandleARB":
                    typedef = "ctypedef int GLhandleARB"
                else:
                    print(f"Skipping type {name}")
                    continue
            else:
                name = name_element.text
                if name in self._dtypes:
                    print(f"Duplicate type {name}")
                    continue
                typedef = "".join(dtype.itertext())
                if typedef.startswith("typedef "):
                    if dtype.find("apientry"):
                        # function definition
                        typedef = typedef.replace("(void)", "()")
                    else:
                        # type definition
                        typedef = "c" + typedef
                        for old_type, new_type in dtype_map.items():
                            typedef = typedef.replace(old_type, new_type)
                else:
                    print(f"Skipping type {name}")
                    continue
            self._dtypes[name] = TypeEntry(name, typedef)

    @property
    def names(self) -> Iterable[str]:
        return self._dtypes.keys()

    def __iter__(self) -> Iterable[TypeEntry]:
        yield from self._dtypes.values()

    def __getitem__(self, dtype: str) -> TypeEntry:
        return self._dtypes[dtype]

    def __contains__(self, dtype: str):
        return dtype in self._dtypes

    def write(self, f, types: Iterable[str]):
        f.write("\n")
        for dtype in types:
            self._dtypes[dtype].write(f)


@dataclass
class EnumEntry:
    vendor: Optional[str]
    name: str
    value: str

    def write(self, f):
        f.write(f"cdef GLenum {self.name} = {self.value}\n")


class EnumManager:
    def __init__(self, enums: List[Element]):
        self._enums: Dict[str, EnumEntry] = {}
        for enums_ in enums:
            self._add_enums(enums_)

    def _add_enums(self, enums: Element):
        vendor = enums.get("vendor")
        for enum in enums.findall("enum"):
            if enum.get("api", "gl") == "gl":
                name = enum.get("name")
                if name in self._enums:
                    print(f"Duplicate enum {name}")
                    continue
                self._enums[name] = EnumEntry(vendor, name, enum.get("value"))

    @property
    def names(self) -> Iterable[str]:
        return self._enums.keys()

    def __iter__(self) -> Iterable[EnumEntry]:
        yield from self._enums.values()

    def __getitem__(self, enum: str) -> EnumEntry:
        return self._enums[enum]

    def __contains__(self, enum: str):
        return enum in self._enums

    def write(self, f, enums: Iterable[str]):
        f.write("\n")
        for enum in enums:
            self._enums[enum].write(f)


@dataclass
class CommandEntry:
    rtype: str
    name: str
    args: Tuple[Tuple[str, str], ...]

    @property
    def typedef_name(self) -> str:
        return re.sub(
            r"(?<=[a-z])[A-Z]|(?<!^)[A-Z](?=[a-z])", r"_\g<0>", self.name
        ).upper()

    @property
    def cname(self) -> str:
        return f"c{self.name}"

    @property
    def loader_name(self) -> str:
        return f"Get{self.name}"

    @property
    def type_args(self) -> str:
        """
        Argument types and names joined around commas
        :return: eg "GLint location, GLsizei count, GLboolean transpose, const GLfloat *value"
        """
        return ", ".join("".join(arg) for arg in self.args)

    @property
    def arg_names(self) -> str:
        """
        Argument names joined around commas
        :return: eg "location, count, transpose, value"
        """
        return ", ".join(arg[1] for arg in self.args)

    def write_typedef(self, f):
        f.write(f"ctypedef {self.rtype}(*{self.typedef_name})({self.type_args})\n")

    def write_null_function(self, f):
        f.write(f"cdef {self.typedef_name} {self.cname} = NULL\n")

    def write_loader_function(self, f):
        f.write(
            f"\n"
            f"cdef {self.rtype}{self.loader_name}({self.type_args}):\n"
            f"    global {self.cname}\n"
            f'    {self.cname} = <{self.typedef_name}>getFunction(b"{self.name}")\n'
            f"    {self.cname}({self.arg_names})\n"
        )

    def write_set_loader_function(self, f):
        f.write(f"{self.cname} = {self.loader_name}\n")

    def write_public_function(self, f):
        f.write(
            f"\n"
            f"cpdef {self.rtype}{self.name}({self.type_args}):\n"
            f"    {self.cname}({self.arg_names})\n"
        )


class CommandManager:
    def __init__(self, commands: List[Element]):
        self._commands: Dict[str, CommandEntry] = {}
        for commands_ in commands:
            self._add_commands(commands_)

    def _clean_arg(self, args: List[str]) -> Tuple[str, str]:
        if len(args) == 3:
            args = ["".join(args[:2]), args[2]]
        elif len(args) == 4 and args[0] == "const ":
            args = ["".join(args[:3]), args[3]]
        if len(args) > 2:
            raise Exception(args)
        return tuple(args)

    def _add_commands(self, commands: Element):
        for command in commands.findall("command"):
            rtype, name = self._clean_arg(list(command.find("proto").itertext()))
            args = []
            for p in command.findall("param"):
                args.append(self._clean_arg(list(p.itertext())))
            if name in self._commands:
                print(f"Duplicate command {name}")
                continue
            self._commands[name] = CommandEntry(rtype, name, tuple(args))

    @property
    def names(self) -> Iterable[str]:
        return self._commands.keys()

    def __iter__(self) -> Iterable[CommandEntry]:
        yield from self._commands.values()

    def __getitem__(self, command: str) -> CommandEntry:
        return self._commands[command]

    def __contains__(self, command: str):
        return command in self._commands

    def write(self, f, commands: Iterable[str]):
        for fun in (
            "write_typedef",
            "write_null_function",
            "write_loader_function",
            "write_set_loader_function",
            "write_public_function",
        ):
            f.write("\n")
            for command in commands:
                command_entry = self._commands[command]
                getattr(command_entry, fun)(f)


@dataclass
class FeatureEntry:
    api: str
    name: str
    number: str
    types: List[str]
    enums: List[str]
    commands: List[str]

    @property
    def short_name(self) -> str:
        return self.name.replace("VERSION_", "")

    @property
    def file_name(self) -> str:
        return f"{self.short_name}.pyx"

    def write(
        self,
        path: str,
        types: TypeManager,
        enums: EnumManager,
        commands: CommandManager,
    ):
        fpath = os.path.join(path, self.api.upper(), self.file_name)
        os.makedirs(os.path.dirname(fpath), exist_ok=True)
        with open(fpath, "w") as f:
            f.write(HEADER)
            # types.write(f, self.types)
            enums.write(f, self.enums)
            commands.write(f, self.commands)


class FeatureManager:
    def __init__(self, features: List[Element]):
        self._features: Dict[str, FeatureEntry] = {}
        for feature in features:
            self._add_feature(feature)

    def _add_feature(self, feature: Element):
        name = feature.get("name")
        if name in self._features:
            print(f"Duplicate feature {name}")
            return
        api = feature.get("api")
        number = feature.get("number")
        types = [
            t.get("name") for r in feature.findall("require") for t in r.findall("type")
        ]
        enums = [
            t.get("name") for r in feature.findall("require") for t in r.findall("enum")
        ]
        commands = [
            t.get("name")
            for r in feature.findall("require")
            for t in r.findall("command")
        ]

        self._features[name] = FeatureEntry(api, name, number, types, enums, commands)

    @property
    def names(self) -> Iterable[str]:
        return self._features.keys()

    def __iter__(self) -> Iterable[FeatureEntry]:
        yield from self._features.values()

    def __getitem__(self, command: str) -> FeatureEntry:
        return self._features[command]

    def __contains__(self, command: str):
        return command in self._features

    def write(
        self,
        path: str,
        types: TypeManager,
        enums: EnumManager,
        commands: CommandManager,
        filter: Optional[Callable[[FeatureEntry], bool]] = None,
    ):
        if filter:
            features = [feature for feature in self if filter(feature)]
        else:
            features = list(self)
        for feature in features:
            feature.write(path, types, enums, commands)


class GLManager:
    def __init__(self, url: str):
        gl_xml: Element = xml_parse(urllib.request.urlopen(url)).getroot()
        self._types = TypeManager(gl_xml.findall("types"))
        self._enums = EnumManager(gl_xml.findall("enums"))
        self._commands = CommandManager(gl_xml.findall("commands"))
        self._features = FeatureManager(gl_xml.findall("feature"))

    @property
    def types(self) -> TypeManager:
        return self._types

    @property
    def enums(self) -> EnumManager:
        return self._enums

    @property
    def commands(self) -> CommandManager:
        return self._commands

    @property
    def features(self) -> FeatureManager:
        return self._features

    def write(self, path: str):
        self.features.write(path, self.types, self.enums, self.commands, filter=lambda feature: feature.api == "gl")


def main():
    url = "https://raw.githubusercontent.com/KhronosGroup/OpenGL-Registry/master/xml/gl.xml"
    GLManager(url).write(os.path.dirname(__file__))


if __name__ == "__main__":
    main()
