"""
normal filters
    input box in editor
    options
    function with inputs
    
copy/extract
    input box in editor
    function with inputs
    
paste/import
    select input file/structure in memory                       options
    editor deals with picking location(s)
    function run with input structure and output locations      main operation
    
clone
    input box in editor
    run operation button
    selection extracted (either using inbuilt function or structure_callable
    editor deals with picking location(s) based on the structure
    function run with input structure and output locations      main operation    
    
    
select operation
select box if required
pick options if valid
run operation
    if dst_box or dst_box_multiple is defined a pre-operation function is optional
        if defined run structure_callable
            given the same inputs as main operation minus destination box
            returns Structure
        else
            extract the src_box and use that
        select destination in UI
    main operation
"""

from amulet_map_editor.plugins import load_operations
import os
from typing import Dict

operations: Dict[str, dict] = {}
options: Dict[str, dict] = {}


def load():
    global operations
    os.makedirs(os.path.join("plugins", "operations"), exist_ok=True)
    operations = load_operations([
        os.path.dirname(__file__),
        os.path.join("plugins", "operations")
    ])


load()
