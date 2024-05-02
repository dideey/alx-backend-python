#!/usr/bin/env python3
"""importing Tuple from and union typing module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """func to return tuple"""
    return (k, v ** 2)
