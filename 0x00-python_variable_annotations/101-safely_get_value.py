#!/usr/bin/env python3
"""importing from typing module"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[T, None]:
    """Return the value of a key in a dictionary"""
    if key in dct:
        return dct[key]
    else:
        return default
