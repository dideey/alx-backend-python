#!/usr/bin/env python3
"""importing from typing module"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """takes a list of strings and returns a list of tuples"""
    return [(i, len(i)) for i in lst]
