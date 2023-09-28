from amulet_map_editor import lang
from .convert import ConvertExtension
from .converter import Converter

export = {"name": lang.get("program_convert.tab_name"), "ui": ConvertExtension}
