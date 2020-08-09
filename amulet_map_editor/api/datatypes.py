from typing import Dict, Union, Callable, Tuple, Any

MenuData = Dict[
    str,
    Dict[
        str,
        Dict[
            str,
            Union[
                Callable,
                Tuple[Callable],
                Tuple[Callable, str],
                Tuple[Callable, str, Any],
            ],
        ],
    ],
]
